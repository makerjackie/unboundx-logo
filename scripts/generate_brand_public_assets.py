from __future__ import annotations

import shutil
import subprocess
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


ROOT = Path(__file__).resolve().parent.parent
PUBLIC = ROOT / "public"

ACCENT = "#F26122"
VOID = "#050505"
SURFACE = "#101012"
SURFACE_2 = "#1A1A1E"
TEXT_PRIMARY = "#FFFFFF"
TEXT_SECONDARY = "#A0A0A5"
LIGHT_BG = "#F6F5F2"
LIGHT_TEXT = "#101012"

MARK_ORANGE = "M 10 10 Q 70 40 70 70"
MARK_SECOND = "M 10 70 Q 70 40 70 10"

WORDMARK_UNBOUND = (
    "M25.56 72.79L25.56 72.79Q19.08 72.79 14.15 70.09Q9.22 67.39 6.48 62.57Q3.74 57.74 3.74 51.62"
    "L3.74 51.62L3.74 20.95L16.56 20.95L16.56 52.56Q16.56 55.30 17.75 57.28Q18.94 59.26 20.99 60.30"
    "Q23.04 61.34 25.56 61.34L25.56 61.34Q28.15 61.34 30.10 60.30Q32.04 59.26 33.19 57.31Q34.34 55.37 34.34 52.63"
    "L34.34 52.63L34.34 20.95L47.30 20.95L47.30 51.70Q47.30 57.82 44.57 62.60Q41.83 67.39 36.97 70.09Q32.11 72.79 25.56 72.79ZM68.40 72.00L55.51 72.00L55.51 20.95L64.51 20.95L68.40 31.39L68.40 72.00ZM94.39 58.82L90.72 72.00L60.91 34.13L64.51 20.95L94.39 58.82ZM100.30 72.00L90.72 72.00L87.41 61.27L87.41 20.95L100.30 20.95L100.30 72.00ZM132.05 72.00L119.59 72.00L119.59 62.42L130.25 62.42Q133.27 62.42 135.04 60.73Q136.80 59.04 136.80 56.30L136.80 56.30Q136.80 54.50 136.01 53.10Q135.22 51.70 133.74 50.94Q132.26 50.18 130.25 50.18L130.25 50.18L119.59 50.18L119.59 40.90L129.46 40.90Q131.98 40.90 133.60 39.64Q135.22 38.38 135.22 35.71L135.22 35.71Q135.22 33.05 133.60 31.79Q131.98 30.53 129.46 30.53L129.46 30.53L119.59 30.53L119.59 20.95L132.55 20.95Q137.30 20.95 140.80 22.75Q144.29 24.55 146.16 27.58Q148.03 30.60 148.03 34.42L148.03 34.42Q148.03 39.53 144.54 42.88Q141.05 46.22 134.42 47.02L134.42 47.02L134.42 42.70Q141.77 43.56 145.66 47.41Q149.54 51.26 149.54 57.10L149.54 57.10Q149.54 61.42 147.38 64.76Q145.22 68.11 141.30 70.06Q137.38 72.00 132.05 72.00L132.05 72.00ZM122.04 72.00L109.37 72.00L109.37 20.95L122.04 20.95L122.04 72.00ZM181.01 72.94L181.01 72.94Q175.10 72.94 170.14 70.92Q165.17 68.90 161.46 65.30Q157.75 61.70 155.66 56.84Q153.58 51.98 153.58 46.37L153.58 46.37Q153.58 40.75 155.63 35.96Q157.68 31.18 161.35 27.58Q165.02 23.98 169.99 22.00Q174.96 20.02 180.86 20.02L180.86 20.02Q186.77 20.02 191.74 22.00Q196.70 23.98 200.38 27.58Q204.05 31.18 206.10 36.00Q208.15 40.82 208.15 46.44L208.15 46.44Q208.15 52.06 206.10 56.88Q204.05 61.70 200.38 65.34Q196.70 68.98 191.77 70.96Q186.84 72.94 181.01 72.94ZM180.86 61.42L180.86 61.42Q185.18 61.42 188.35 59.54Q191.52 57.67 193.25 54.29Q194.98 50.90 194.98 46.37L194.98 46.37Q194.98 43.06 194.00 40.32Q193.03 37.58 191.16 35.60Q189.29 33.62 186.70 32.54Q184.10 31.46 180.86 31.46L180.86 31.46Q176.54 31.46 173.38 33.30Q170.21 35.14 168.48 38.52Q166.75 41.90 166.75 46.37L166.75 46.37Q166.75 49.82 167.72 52.60Q168.70 55.37 170.57 57.35Q172.44 59.33 175.03 60.37Q177.62 61.42 180.86 61.42ZM235.66 72.79L235.66 72.79Q229.18 72.79 224.24 70.09Q219.31 67.39 216.58 62.57Q213.84 57.74 213.84 51.62L213.84 51.62L213.84 20.95L226.66 20.95L226.66 52.56Q226.66 55.30 227.84 57.28Q229.03 59.26 231.08 60.30Q233.14 61.34 235.66 61.34L235.66 61.34Q238.25 61.34 240.19 60.30Q242.14 59.26 243.29 57.31Q244.44 55.37 244.44 52.63L244.44 52.63L244.44 20.95L257.40 20.95L257.40 51.70Q257.40 57.82 254.66 62.60Q251.93 67.39 247.07 70.09Q242.21 72.79 235.66 72.79ZM278.50 72.00L265.61 72.00L265.61 20.95L274.61 20.95L278.50 31.39L278.50 72.00ZM304.49 58.82L300.82 72.00L271.01 34.13L274.61 20.95L304.49 58.82ZM310.39 72.00L300.82 72.00L297.50 61.27L297.50 20.95L310.39 20.95L310.39 72.00ZM340.63 72.00L328.18 72.00L328.18 60.91L340.42 60.91Q344.74 60.91 347.94 59.26Q351.14 57.60 352.87 54.32Q354.60 51.05 354.60 46.37L354.60 46.37Q354.60 41.76 352.84 38.56Q351.07 35.35 347.90 33.70Q344.74 32.04 340.42 32.04L340.42 32.04L327.60 32.04L327.60 20.95L340.49 20.95Q346.39 20.95 351.36 22.79Q356.33 24.62 360.00 28.01Q363.67 31.39 365.72 36.07Q367.78 40.75 367.78 46.44L367.78 46.44Q367.78 52.20 365.72 56.88Q363.67 61.56 360.00 64.94Q356.33 68.33 351.40 70.16Q346.46 72.00 340.63 72.00L340.63 72.00ZM332.35 72.00L319.46 72.00L319.46 20.95L332.35 20.95L332.35 72.00Z"
)
WORDMARK_X = (
    "M429.06 72.00L413.94 72.00L400.11 49.25L398.82 49.25L379.38 20.95L394.71 20.95L408.25 42.41"
    "L409.54 42.41L429.06 72.00ZM393.20 72.00L378.51 72.00L397.09 44.71L407.24 49.54L393.20 72.00ZM428.12 20.95L409.83 48.10L399.68 43.20L413.43 20.95L428.12 20.95Z"
)
WORDMARK_TOP = 20.02


def reset_public() -> None:
    if PUBLIC.exists():
        shutil.rmtree(PUBLIC)
    PUBLIC.mkdir(parents=True, exist_ok=True)


def write_public_file(relative_path: str, content: str) -> None:
    path = PUBLIC / relative_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def save_root_file(relative_path: str, content: str) -> None:
    path = ROOT / relative_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def svg_document(view_box: str, body: str, title: str, desc: str) -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="{view_box}" fill="none" role="img" aria-labelledby="title desc">
  <title id="title">{title}</title>
  <desc id="desc">{desc}</desc>
  {body}
</svg>
"""


def symbol_group(
    second_color: str,
    *,
    x: float = 0,
    y: float = 0,
    scale: float = 1.0,
    stroke_width: float = 14,
) -> str:
    return f"""<g transform="translate({x} {y}) scale({scale})">
    <path d="{MARK_ORANGE}" fill="none" stroke="{ACCENT}" stroke-width="{stroke_width}" stroke-linecap="round"/>
    <path d="{MARK_SECOND}" fill="none" stroke="{second_color}" stroke-width="{stroke_width}" stroke-linecap="round"/>
  </g>"""


def wordmark_group(
    text_color: str,
    *,
    x: float = 0,
    y: float = 0,
    scale: float = 1.0,
) -> str:
    return f"""<g transform="translate({x} {y}) scale({scale})">
    <g transform="translate(0 {-WORDMARK_TOP})">
      <path d="{WORDMARK_UNBOUND}" fill="{text_color}"/>
      <path d="{WORDMARK_X}" fill="{ACCENT}"/>
    </g>
  </g>"""


def mark_svg(second_color: str, *, background: str | None = None) -> str:
    background_rect = (
        f'<rect width="128" height="128" rx="32" fill="{background}"/>'
        if background
        else ""
    )
    body = f"""{background_rect}
  {symbol_group(second_color, x=24, y=24, scale=1.14, stroke_width=13)}"""
    return svg_document(
        "0 0 128 128",
        body,
        "UNBOUNDX mark",
        "Two intersecting arcs forming the UNBOUNDX symbol.",
    )


def lockup_svg(second_color: str, text_color: str) -> str:
    body = f"""{symbol_group(second_color, x=22, y=30)}
  {wordmark_group(text_color, x=118, y=38, scale=1)}"""
    return svg_document(
        "0 0 560 140",
        body,
        "UNBOUNDX primary lockup",
        "UNBOUNDX wordmark with the gravity arcs symbol on the left.",
    )


def stacked_svg(second_color: str, text_color: str) -> str:
    body = f"""{symbol_group(second_color, x=145, y=72)}
  {wordmark_group(text_color, x=22, y=210, scale=0.78)}"""
    return svg_document(
        "0 0 380 380",
        body,
        "UNBOUNDX stacked lockup",
        "UNBOUNDX wordmark placed below the gravity arcs symbol.",
    )


def key_visual_svg() -> str:
    body = f"""<rect width="1920" height="1080" fill="{VOID}"/>
  <circle cx="1450" cy="220" r="240" fill="{ACCENT}" opacity="0.10"/>
  <path d="M0 840 L560 520 L1120 820 L1920 180" stroke="{SURFACE_2}" stroke-width="2"/>
  <path d="M0 960 L720 420 L1320 720 L1920 120" stroke="{SURFACE_2}" stroke-width="2"/>
  {symbol_group(TEXT_PRIMARY, x=1140, y=220, scale=6.1)}
  {wordmark_group(TEXT_PRIMARY, x=140, y=210, scale=1.78)}
  <rect x="140" y="400" width="560" height="2" fill="{ACCENT}" opacity="0.7"/>
  <rect x="140" y="456" width="420" height="16" rx="8" fill="{TEXT_SECONDARY}" opacity="0.35"/>
  <rect x="140" y="500" width="520" height="16" rx="8" fill="{TEXT_SECONDARY}" opacity="0.28"/>
  <rect x="140" y="544" width="360" height="16" rx="8" fill="{TEXT_SECONDARY}" opacity="0.22"/>"""
    return svg_document(
        "0 0 1920 1080",
        body,
        "UNBOUNDX key visual",
        "A dark key visual with the gravity arcs symbol and the UNBOUNDX wordmark.",
    )


def social_cover_svg() -> str:
    body = f"""<rect width="1600" height="900" fill="{VOID}"/>
  <circle cx="1240" cy="180" r="220" fill="{ACCENT}" opacity="0.10"/>
  {symbol_group(TEXT_PRIMARY, x=1090, y=320, scale=4.4)}
  {wordmark_group(TEXT_PRIMARY, x=120, y=248, scale=1.5)}
  <rect x="124" y="412" width="460" height="2" fill="{ACCENT}" opacity="0.8"/>
  <rect x="124" y="470" width="660" height="14" rx="7" fill="{TEXT_SECONDARY}" opacity="0.34"/>
  <rect x="124" y="510" width="560" height="14" rx="7" fill="{TEXT_SECONDARY}" opacity="0.24"/>
  <rect x="124" y="550" width="620" height="14" rx="7" fill="{TEXT_SECONDARY}" opacity="0.18"/>"""
    return svg_document(
        "0 0 1600 900",
        body,
        "UNBOUNDX social cover",
        "A social cover asset using the UNBOUNDX logo system on a dark background.",
    )


def app_splash_svg() -> str:
    body = f"""<rect width="1170" height="2532" rx="140" fill="{VOID}"/>
  <circle cx="860" cy="460" r="320" fill="{ACCENT}" opacity="0.12"/>
  {symbol_group(TEXT_PRIMARY, x=258, y=922, scale=8.3)}
  {wordmark_group(TEXT_PRIMARY, x=190, y=1580, scale=1.85)}
  <rect x="248" y="1728" width="674" height="2" fill="{ACCENT}" opacity="0.8"/>"""
    return svg_document(
        "0 0 1170 2532",
        body,
        "UNBOUNDX app splash",
        "A mobile splash screen featuring the UNBOUNDX symbol and wordmark.",
    )


def poster_svg() -> str:
    body = f"""<rect width="1080" height="1440" fill="{VOID}"/>
  <circle cx="790" cy="280" r="260" fill="{ACCENT}" opacity="0.10"/>
  {symbol_group(TEXT_PRIMARY, x=560, y=180, scale=4.8)}
  {wordmark_group(TEXT_PRIMARY, x=108, y=810, scale=1.9)}
  <rect x="112" y="988" width="560" height="2" fill="{ACCENT}" opacity="0.9"/>
  <rect x="112" y="1054" width="708" height="18" rx="9" fill="{TEXT_SECONDARY}" opacity="0.28"/>
  <rect x="112" y="1106" width="520" height="18" rx="9" fill="{TEXT_SECONDARY}" opacity="0.2"/>"""
    return svg_document(
        "0 0 1080 1440",
        body,
        "UNBOUNDX poster",
        "A poster-ready brand asset based on the UNBOUNDX visual system.",
    )


def write_assets() -> None:
    write_public_file("logos/svg/unboundx-mark-dark.svg", mark_svg(TEXT_PRIMARY))
    write_public_file("logos/svg/unboundx-mark-light.svg", mark_svg(LIGHT_TEXT))
    write_public_file("logos/svg/unboundx-lockup-dark.svg", lockup_svg(TEXT_PRIMARY, TEXT_PRIMARY))
    write_public_file("logos/svg/unboundx-lockup-light.svg", lockup_svg(LIGHT_TEXT, LIGHT_TEXT))
    write_public_file("logos/svg/unboundx-stacked-dark.svg", stacked_svg(TEXT_PRIMARY, TEXT_PRIMARY))
    write_public_file("logos/svg/unboundx-stacked-light.svg", stacked_svg(LIGHT_TEXT, LIGHT_TEXT))
    write_public_file("logos/svg/unboundx-favicon.svg", mark_svg(TEXT_PRIMARY, background=VOID))
    write_public_file("logos/svg/unboundx-gravity-arcs-symbol.svg", mark_svg(TEXT_PRIMARY))

    write_public_file("materials/svg/unboundx-key-visual.svg", key_visual_svg())
    write_public_file("materials/svg/unboundx-social-cover.svg", social_cover_svg())
    write_public_file("materials/svg/unboundx-app-splash.svg", app_splash_svg())
    write_public_file("materials/svg/unboundx-poster.svg", poster_svg())

    save_root_file("favicon.svg", mark_svg(TEXT_PRIMARY, background=VOID))


def write_public_readme() -> None:
    write_public_file(
        "README.md",
        """# UNBOUNDX Public Assets

This folder contains the current delivery-ready assets for the latest `index.html` brand site.

- `index.html` / `unboundx-brand-guidelines-dark.html`：线上部署页
- `logos/`：最终 Logo 的 SVG / PNG 交付文件
- `materials/`：主视觉、海报、封面与启动页等常用品牌物料
- `downloads/`：打包好的下载压缩包
""",
    )


def deployify_html(html: str) -> str:
    return html.replace('href="public/downloads/', 'href="./downloads/')


def sync_deploy_pages() -> None:
    index_html = (ROOT / "index.html").read_text(encoding="utf-8")
    dark_html = (ROOT / "unboundx-brand-guidelines-dark.html").read_text(encoding="utf-8")
    favicon = (ROOT / "favicon.svg").read_text(encoding="utf-8")

    write_public_file("index.html", deployify_html(index_html))
    write_public_file(
        "unboundx-brand-guidelines-dark.html",
        deployify_html(dark_html),
    )
    write_public_file("favicon.svg", favicon)


def run_rsvg_convert(svg_path: Path, png_path: Path, width: int, height: int) -> None:
    png_path.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [
            "rsvg-convert",
            "--format",
            "png",
            "--width",
            str(width),
            "--height",
            str(height),
            "--output",
            str(png_path),
            str(svg_path),
        ],
        check=True,
    )


def render_pngs() -> None:
    specs = {
        "logos/svg/unboundx-mark-dark.svg": ("logos/png/unboundx-mark-dark.png", 1024, 1024),
        "logos/svg/unboundx-mark-light.svg": ("logos/png/unboundx-mark-light.png", 1024, 1024),
        "logos/svg/unboundx-lockup-dark.svg": ("logos/png/unboundx-lockup-dark.png", 2400, 600),
        "logos/svg/unboundx-lockup-light.svg": ("logos/png/unboundx-lockup-light.png", 2400, 600),
        "logos/svg/unboundx-stacked-dark.svg": ("logos/png/unboundx-stacked-dark.png", 1400, 1400),
        "logos/svg/unboundx-stacked-light.svg": ("logos/png/unboundx-stacked-light.png", 1400, 1400),
        "logos/svg/unboundx-favicon.svg": ("logos/png/unboundx-favicon.png", 1024, 1024),
        "materials/svg/unboundx-key-visual.svg": ("materials/png/unboundx-key-visual.png", 1920, 1080),
        "materials/svg/unboundx-social-cover.svg": ("materials/png/unboundx-social-cover.png", 1600, 900),
        "materials/svg/unboundx-app-splash.svg": ("materials/png/unboundx-app-splash.png", 1170, 2532),
        "materials/svg/unboundx-poster.svg": ("materials/png/unboundx-poster.png", 1600, 2133),
    }

    for svg_rel, (png_rel, width, height) in specs.items():
        run_rsvg_convert(PUBLIC / svg_rel, PUBLIC / png_rel, width, height)


def zip_bundle(output_name: str, prefixes: list[str]) -> None:
    output = PUBLIC / "downloads" / output_name
    output.parent.mkdir(parents=True, exist_ok=True)

    with ZipFile(output, "w", ZIP_DEFLATED) as archive:
        archive.write(PUBLIC / "README.md", Path("README.md"))
        for prefix in prefixes:
            base = PUBLIC / prefix
            for file in sorted(base.rglob("*")):
                if file.is_file():
                    archive.write(file, file.relative_to(PUBLIC))


def build_bundles() -> None:
    zip_bundle("UNBOUNDX_Logos_SVG.zip", ["logos/svg"])
    zip_bundle("UNBOUNDX_Logos_PNG.zip", ["logos/png"])
    zip_bundle("UNBOUNDX_Materials.zip", ["materials/svg", "materials/png"])
    zip_bundle("UNBOUNDX_Brand_Kit.zip", ["logos", "materials"])


def main() -> None:
    reset_public()
    write_assets()
    write_public_readme()
    render_pngs()
    build_bundles()
    sync_deploy_pages()


if __name__ == "__main__":
    main()
