# UNBOUNDX Logo 设计全过程记录

## 项目目标

为 UNBOUNDX / 自由维度构建一套可展示、可下载、可归档的数字化品牌视觉系统，并以纯代码方式完成主标、规范页与资产导出能力。

## 方法论

整个项目不是传统的「设计稿 → 切图 → 前端还原」流程，而是直接使用 HTML、CSS、SVG 与 JavaScript 完成设计、展示与资产交付：

- 用 SVG 直接构建 Logo 几何骨架
- 用 CSS 做风格、动效与场景展示
- 用 JavaScript 在浏览器端打包导出 ZIP / SVG / PNG
- 用 GitHub 归档整个探索过程
- 用 Vercel + Cloudflare 发布最终可访问站点

## 设计迭代时间线

### 1. 发散探索阶段

围绕“自由维度 / 多维空间突破 / X / 边界突破”这些关键词，先快速产出大量 Logo 方向：

- `archive/history/unboundx-10-logo-concepts.html`
- `archive/history/unboundx-logo-concepts.html`
- `archive/history/unboundx-logo-candidates.html`
- `archive/history/unboundx-freedom-dimensions-logos.html`
- `archive/history/unboundx-free-dimensions-ultimate.html`
- `archive/history/unboundx-frame-break-logos.html`
- `archive/history/unboundX Logo-claude.html`

这一阶段重点不是直接定稿，而是拉开设计搜索空间，让人类判断哪个方向最有品牌势能。

### 2. 视觉锚点确定

在多轮候选中，最终收敛到“多层嵌套边框 + 穿透式 X”的结构，也就是后续被总结为：

**Dimensional Breakthrough / Echo Break**

它表达了：

- 多层系统、维度与边界
- 中心核心保持稳定
- X 作为突破力量贯穿所有层级

### 3. 规范页逐步成型

定下核心结构后，开始从单个 Logo 升级到品牌规范：

- `archive/history/unboundx-brand-guidelines.html`
- `archive/history/unboundx-brand-guidelines-v2.html`
- `archive/history/unboundx-brand-guidelines-v3.html`
- `unboundx-brand-guidelines-v4-final.html`

演进重点包括：

- 色彩系统统一到 Lava Orange 主轴
- 英文字体与中英混排风格收敛
- Logo 套件（Icon / Lockup / Dark / Light）整理
- 品牌 UI System 加入按钮、表单、玻璃卡片等规范示例
- 应用场景扩展到 Splash Screen、Poster、Key Visual

### 4. 资产交付闭环

最终版本不只是展示页面，还加入了前端下载中心：

- 在线生成 SVG
- 在线生成高分辨率 PNG
- 一键打包为 ZIP 下载

这使页面本身同时具备：

- 品牌展示能力
- 设计资产交付能力
- 对外汇报能力

### 5. Dark Guidelines 最终定稿

在最新版本中，项目正式切换到以 `public/index.html` 为核心的深色规范页方案，并放弃旧的多层框体语言：

- 最新主稿：`public/index.html`
- 深色预览别名：`unboundx-brand-guidelines-dark.html`
- 品牌物料目录：`public/`

这次定稿的关键变化是：

- Logo 彻底重构为两条相交弧线的极简 X
- X 被重新定义为 “Dimension / 维度”
- 品牌主色固定为 `Aerospace Orange #F26122`
- 全站转入 `Deep Void #050505` 黑曜石底色
- 下载区从示意按钮升级为真实可下载的 Brand Kit
- 静态资源结构收敛为单一 `public/`，不再保留额外镜像目录

## AI 协作分工

### Claude Code / Codex CLI

- 帮助整理结构、补全文档与仓库归档
- 负责静态站点部署、仓库整理、发布链路打通
- 协助把设计资产转化成可管理、可复用的工程化结果

### Gemini 3.1 Pro

- 在视觉概念扩散与版本复盘上提供强力支持
- 输出了 `docs/gemini-logo-design.md` 这类设计过程记录
- 参与品牌概念表达、迭代总结与文案归纳

### 人类主导

- 决定品牌方向、气质与最终审美判断
- 选择保留哪些视觉特征
- 对“太粗”“太满”“不够高级”等细节做最终裁决

## 最新更新 (2026-04-06)

### 简化与中文化改进

根据用户反馈，对品牌规范页面进行了以下优化：

#### 1. Logo 设计理念简化
- **原来**: 在页面上展示 4 个详细的设计理念卡片（极简形态、X 代表维度、引力牵引、自由维度）
- **现在**: 简化为一句话核心描述："两条弧线在深色空间中相交，形成向右上方突破的极简 X——橙色象征活力与向前引力，冷白代表精准与秩序，寓意进入全新的独立维度。"
- **详细内容**: 通过"设计理念"按钮弹窗展示

#### 2. 侧边栏与标题全面中文化
- Brand Overview → 品牌概览
- Logo System → 标志系统
- Color Palette → 色彩体系
- Typography → 字体规范
- UI Guidelines → 界面规范
- Applications → 应用案例
- Motion Design → 动效系统
- Promo Film → 宣传片
- Assets → 资源下载

#### 3. Logo 变体标题简化
- Primary Lockup → 标准横版
- Stacked Lockup → 纵向组合
- Icon / Avatar → 图标 / 头像
- Light Mode Reversed → 浅色反转

#### 4. 各章节描述精简
- **色彩体系**: 移除冗长的工程级描述，保留核心信息
- **字体规范**: 简化描述，去除"庞大数据信息流"等过度修饰
- **界面规范**: 精简为核心理念
- **应用案例**: 移除重复的品牌理念强调
- **资源下载**: 简化描述

#### 5. 新增弹窗详情展示
采用与"为什么选择航天橙？"相同的弹窗模式，为以下内容添加详情按钮：

- **Logo 设计理念**: 展示 4 个设计哲学要点
- **动效系统**: 展示系统化沉淀、四大主题、克制与张力
- **宣传片**: 展示输出规格、镜头结构、使用场景

#### 设计原则

1. **简约优先**: 页面主体内容保持简洁，避免信息过载
2. **按需展开**: 详细解释通过弹窗提供，用户可选择性查看
3. **全面中文化**: 所有导航、标题、标签使用中文，提升本地化体验
4. **一致性**: 所有弹窗采用统一的设计模式和交互方式

## 最终交付

- 在线站点：`https://logo.unboundxai.com`
- 代码仓库：`https://github.com/jackiexiao/unboundx-logo`
- 最终规范文件：`public/index.html`
- 深色规范页别名：`unboundx-brand-guidelines-dark.html`
- 品牌素材目录：`public/`
- 历史探索归档：`archive/history/`

## 06. Motion Design

品牌动效系统围绕"维度突破"的核心概念展开，通过轨道旋转、磁场交互、扫光显现与脉冲呼吸四类动效语言，让静态标识获得时间维度上的生命力。

### 核心动效类型

**轨道旋转 (Orbital Spin)**

Logo 外围的弧线轨道以不同速度持续旋转，营造多维空间的层次感。主轨道顺时针 4 秒一周，外层轨道逆向 8 秒一周，形成错位的视觉韵律。这种设计让 Logo 始终处于"运动中的稳定"状态。

```css
.interactive-arc::before {
    border-top-color: #F26122;
    animation: spin 4s linear infinite;
}
```

**磁场交互 (Magnetic Core)**

中心 X 标识具备磁场般的交互特性：鼠标靠近时产生微妙的吸引偏移，点击拖拽时缩放至 0.9 倍并切换为抓取手势。这种物理感的反馈让品牌标识不再是冰冷的图形，而是可感知、可响应的存在。

```css
.magnetic-core {
    transition: transform 0.2s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    cursor: grab;
}
.magnetic-core:active {
    transform: scale(0.9);
    cursor: grabbing;
}
```

**扫光显现 (Reveal Block)**

品牌标题的入场动效采用橙色色块从左至右扫过的方式，先遮盖后显现。色块在 0.6 秒时完全覆盖文字，随后从右侧退出，文字在 0.8 秒时瞬间显现。这种"破开维度"的视觉隐喻强化了品牌突破边界的气质。

```css
@keyframes reveal-block {
    0% { transform: scaleX(0); transform-origin: left; }
    50% { transform: scaleX(1); transform-origin: left; }
    51% { transform: scaleX(1); transform-origin: right; }
    100% { transform: scaleX(0); transform-origin: right; }
}
```

**脉冲呼吸 (Pulse Glow)**

Logo 的发光效果以 2 秒为周期进行呼吸式变化，阴影从 5px 扩散至 20px，透明度在 0.3 至 0.8 之间波动。这种有机的律动让品牌在深色背景中始终保持"活着"的状态，而非静止的装饰。

```css
@keyframes logo-glow {
    0%, 100% { filter: drop-shadow(0 0 5px rgba(242, 97, 34, 0.3)); }
    50% { filter: drop-shadow(0 0 20px rgba(242, 97, 34, 0.8)); }
}
```

### 环境氛围层

**胶片颗粒 (Film Grain)**

全局使用 SVG 噪点滤镜叠加 3% 不透明度的分形噪声，模拟高端胶片质感。这层微妙的颗粒感让数字界面摆脱过度光滑的塑料感，获得更具深度的视觉肌理。

**辉光光晕 (Glow Orb)**

页面中心放置一个 60vw 直径的径向渐变光晕，以 10 秒周期在 0.8 至 1.1 倍之间缓慢缩放。光晕的存在为深色背景注入空间深度，让视觉焦点自然聚集在品牌核心区域。

### 时序编排原则

所有动效遵循"先快后慢"的缓动曲线 `cubic-bezier(0.16, 1, 0.3, 1)`，确保动作启动果断、结束柔和。入场动画采用阶梯式延迟（150ms / 300ms / 450ms），避免所有元素同时出现造成的视觉混乱。

交互反馈控制在 200-400ms 内完成，超过 500ms 的响应会让用户感知到延迟。循环动画的周期设定在 2-10 秒之间，过快会显得焦躁，过慢则失去动感。

## 权利归属

本项目相关品牌设计、视觉系统、代码资产与文档内容著作权归：

**自由维度（深圳）科技有限公司**

保留所有权利。
