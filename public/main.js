document.addEventListener('DOMContentLoaded', () => {
  const sections = Array.from(document.querySelectorAll('section, #home'));
  const navItems = Array.from(document.querySelectorAll('.nav-item a'));
  const mobileNavToggle = document.querySelector('.mobile-nav-toggle');
  const navCloseTriggers = document.querySelectorAll('[data-nav-close]');
  const desktopQuery = window.matchMedia('(min-width: 1025px)');

  const setNavState = (isOpen) => {
    document.body.classList.toggle('nav-open', isOpen);
    if (mobileNavToggle) {
      mobileNavToggle.setAttribute('aria-expanded', String(isOpen));
      mobileNavToggle.setAttribute('aria-label', isOpen ? '关闭导航菜单' : '打开导航菜单');
    }
  };

  const closeNav = () => setNavState(false);
  const toggleNav = () => setNavState(!document.body.classList.contains('nav-open'));

  const updateActiveNav = () => {
    let current = 'home';
    sections.forEach((section) => {
      if (window.scrollY >= section.offsetTop - 220) {
        current = section.getAttribute('id');
      }
    });

    navItems.forEach((item) => {
      item.classList.toggle('active', item.getAttribute('href') === `#${current}`);
    });
  };

  updateActiveNav();
  window.addEventListener('scroll', updateActiveNav, { passive: true });

  if (mobileNavToggle) {
    mobileNavToggle.addEventListener('click', toggleNav);
  }

  navCloseTriggers.forEach((trigger) => {
    trigger.addEventListener('click', closeNav);
  });

  navItems.forEach((item) => {
    item.addEventListener('click', () => {
      if (window.innerWidth <= 1024) {
        closeNav();
      }
    });
  });

  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') {
      closeNav();
    }
  });

  const handleDesktopChange = (event) => {
    if (event.matches) {
      closeNav();
    }
  };

  if (desktopQuery.addEventListener) {
    desktopQuery.addEventListener('change', handleDesktopChange);
  } else if (desktopQuery.addListener) {
    desktopQuery.addListener(handleDesktopChange);
  }

  document.querySelectorAll("[data-dialog-open]").forEach((button) => {
    button.addEventListener("click", () => {
      const dialog = document.getElementById(button.dataset.dialogOpen);
      if (dialog) dialog.showModal();
    });
  });

  document.querySelectorAll("[data-dialog-close]").forEach((button) => {
    button.addEventListener("click", () => {
      const dialog = document.getElementById(button.dataset.dialogClose);
      if (dialog) dialog.close();
    });
  });

  // Copy Prompt Functionality
  const copyBtn = document.getElementById('copyPromptBtn');
  const promptContent = document.getElementById('promptContent');
  if (copyBtn && promptContent) {
    copyBtn.addEventListener('click', async () => {
      try {
        await navigator.clipboard.writeText(promptContent.textContent);
        const originalHTML = copyBtn.innerHTML;
        copyBtn.classList.add('copied');
        copyBtn.innerHTML = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg> Copied!';

        setTimeout(() => {
          copyBtn.classList.remove('copied');
          copyBtn.innerHTML = originalHTML;
        }, 2000);
      } catch (err) {
        console.error('Failed to copy text: ', err);
      }
    });
  }

  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const orangeArcPath = typeof Path2D !== 'undefined'
    ? new Path2D('M35.4 35.4q68.4 34.2 68.4 68.4')
    : null;
  const whiteArcPath = typeof Path2D !== 'undefined'
    ? new Path2D('M35.4 103.8q68.4-34.2 68.4-68.4')
    : null;

  const prepareCanvas = (canvas) => {
    const ctx = canvas?.getContext('2d');
    if (!canvas || !ctx) return null;

    const resize = () => {
      const rect = canvas.getBoundingClientRect();
      const dpr = window.devicePixelRatio || 1;
      canvas.width = Math.max(1, Math.round(rect.width * dpr));
      canvas.height = Math.max(1, Math.round(rect.height * dpr));
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      return rect;
    };

    return { ctx, resize };
  };

  const drawBrandMark = (ctx, x, y, size, opacity = 1) => {
    if (!orangeArcPath || !whiteArcPath) return;

    ctx.save();
    ctx.translate(x - size / 2, y - size / 2);
    ctx.scale(size / 128, size / 128);
    ctx.lineCap = 'round';
    ctx.lineWidth = 14.8;
    ctx.globalAlpha = opacity;
    ctx.strokeStyle = '#F26122';
    ctx.stroke(orangeArcPath);
    ctx.strokeStyle = '#FFFFFF';
    ctx.stroke(whiteArcPath);
    ctx.restore();
    ctx.globalAlpha = 1;
  };

  const setupMotionShowcase = () => {
    const prepared = prepareCanvas(document.getElementById('motion-showcase-canvas'));
    if (!prepared) return;

    const { ctx, resize } = prepared;
    let rect = resize();
    const particles = Array.from({ length: 18 }, (_, index) => ({
      angle: (index / 18) * Math.PI * 2,
      speed: 0.0008 + Math.random() * 0.0014,
      orbit: 82 + (index % 4) * 34 + Math.random() * 12,
      size: index % 3 === 0 ? 3.8 : 2.6,
      color: index % 2 === 0 ? '#F26122' : '#FFFFFF',
      drift: 0.65 + Math.random() * 0.38,
    }));

    const draw = (time = 0) => {
      const width = rect.width;
      const height = rect.height;
      const centerX = width / 2;
      const centerY = height / 2;

      ctx.clearRect(0, 0, width, height);
      ctx.fillStyle = 'rgba(5, 5, 5, 0.14)';
      ctx.fillRect(0, 0, width, height);

      [98, 142, 190].forEach((radius, index) => {
        ctx.beginPath();
        ctx.strokeStyle = index === 1 ? 'rgba(242,97,34,0.14)' : 'rgba(255,255,255,0.08)';
        ctx.lineWidth = 1;
        ctx.setLineDash(index === 2 ? [5, 9] : []);
        ctx.arc(centerX, centerY, radius, 0, Math.PI * 2);
        ctx.stroke();
        ctx.setLineDash([]);
      });

      particles.forEach((particle, index) => {
        const angle = particle.angle + time * particle.speed;
        const radius = particle.orbit + Math.sin(time * 0.001 + index) * 4 * particle.drift;
        const x = centerX + Math.cos(angle) * radius;
        const y = centerY + Math.sin(angle * particle.drift) * (radius * 0.72);

        ctx.beginPath();
        ctx.strokeStyle = particle.color;
        ctx.globalAlpha = particle.color === '#F26122' ? 0.18 : 0.12;
        ctx.lineWidth = 1.4;
        ctx.arc(
          centerX,
          centerY,
          radius,
          angle - 0.34,
          angle
        );
        ctx.stroke();
        ctx.globalAlpha = 1;

        ctx.beginPath();
        ctx.fillStyle = particle.color;
        ctx.arc(x, y, particle.size, 0, Math.PI * 2);
        ctx.fill();
      });

      drawBrandMark(ctx, centerX, centerY, 88, 0.22);
    };

    const handleResize = () => {
      rect = resize();
      draw(1600);
    };

    window.addEventListener('resize', handleResize);

    if (prefersReducedMotion.matches) {
      draw(1800);
      return;
    }

    const animate = (time) => {
      draw(time);
      requestAnimationFrame(animate);
    };

    requestAnimationFrame(animate);
  };

  const setupOrbitCanvas = () => {
    const prepared = prepareCanvas(document.getElementById('motion-orbit-canvas'));
    if (!prepared) return;

    const { ctx, resize } = prepared;
    let rect = resize();

    const draw = (time = 0) => {
      const width = rect.width;
      const height = rect.height;
      const centerX = width / 2;
      const centerY = height / 2;

      ctx.clearRect(0, 0, width, height);

      [42, 60, 78].forEach((radius, index) => {
        ctx.beginPath();
        ctx.strokeStyle = index === 1 ? 'rgba(242,97,34,0.14)' : 'rgba(255,255,255,0.08)';
        ctx.lineWidth = 1;
        ctx.arc(centerX, centerY, radius, 0, Math.PI * 2);
        ctx.stroke();
      });

      for (let index = 0; index < 3; index += 1) {
        const angle = time * 0.0015 + (index * Math.PI * 2) / 3;
        const radius = 42 + index * 18;
        const x = centerX + Math.cos(angle) * radius;
        const y = centerY + Math.sin(angle) * radius;
        const color = index % 2 === 0 ? '#F26122' : '#FFFFFF';

        ctx.beginPath();
        ctx.strokeStyle = color;
        ctx.globalAlpha = 0.22;
        ctx.lineWidth = 2;
        ctx.arc(centerX, centerY, radius, angle - 0.62, angle);
        ctx.stroke();
        ctx.globalAlpha = 1;

        ctx.beginPath();
        ctx.fillStyle = color;
        ctx.arc(x, y, 4.2, 0, Math.PI * 2);
        ctx.fill();
      }

      drawBrandMark(ctx, centerX, centerY, 76);
    };

    const handleResize = () => {
      rect = resize();
      draw(900);
    };

    window.addEventListener('resize', handleResize);

    if (prefersReducedMotion.matches) {
      draw(1200);
      return;
    }

    const animate = (time) => {
      draw(time);
      requestAnimationFrame(animate);
    };

    requestAnimationFrame(animate);
  };

  const setupFieldCanvas = () => {
    const prepared = prepareCanvas(document.getElementById('motion-field-canvas'));
    if (!prepared) return;

    const { ctx, resize } = prepared;
    let rect = resize();
    const rays = Array.from({ length: 14 }, (_, index) => ({
      angle: (index / 14) * Math.PI * 2,
      speed: 0.85 + Math.random() * 0.45,
      maxRadius: 74 + Math.random() * 16,
      phase: Math.random() * Math.PI * 2,
      color: index % 2 === 0 ? '#F26122' : '#FFFFFF',
    }));

    const draw = (time = 0) => {
      const width = rect.width;
      const height = rect.height;
      const centerX = width / 2;
      const centerY = height / 2;

      ctx.clearRect(0, 0, width, height);

      rays.forEach((ray) => {
        const pulse = (Math.sin(time * 0.0022 * ray.speed + ray.phase) + 1) / 2;
        const radius = 22 + pulse * (ray.maxRadius - 22);
        const x = centerX + Math.cos(ray.angle) * radius;
        const y = centerY + Math.sin(ray.angle) * radius;
        const opacity = 1 - (radius - 22) / (ray.maxRadius - 22);

        ctx.beginPath();
        ctx.strokeStyle = ray.color;
        ctx.globalAlpha = opacity * 0.26;
        ctx.lineWidth = 1;
        ctx.moveTo(centerX, centerY);
        ctx.lineTo(x, y);
        ctx.stroke();

        ctx.beginPath();
        ctx.fillStyle = ray.color;
        ctx.globalAlpha = opacity * 0.86;
        ctx.arc(x, y, 3.2, 0, Math.PI * 2);
        ctx.fill();
        ctx.globalAlpha = 1;
      });

      ctx.beginPath();
      ctx.fillStyle = '#F26122';
      ctx.arc(centerX, centerY, 12, 0, Math.PI * 2);
      ctx.fill();

      drawBrandMark(ctx, centerX, centerY, 74, 0.2);
    };

    const handleResize = () => {
      rect = resize();
      draw(1200);
    };

    window.addEventListener('resize', handleResize);

    if (prefersReducedMotion.matches) {
      draw(1600);
      return;
    }

    const animate = (time) => {
      draw(time);
      requestAnimationFrame(animate);
    };

    requestAnimationFrame(animate);
  };

  setupMotionShowcase();
  setupOrbitCanvas();
  setupFieldCanvas();
  });
