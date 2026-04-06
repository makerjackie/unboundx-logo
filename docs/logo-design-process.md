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

## 最终交付

- 在线站点：`https://logo.unboundxai.com`
- 代码仓库：`https://github.com/jackiexiao/unboundx-logo`
- 最终规范文件：`public/index.html`
- 深色规范页别名：`unboundx-brand-guidelines-dark.html`
- 品牌素材目录：`public/`
- 历史探索归档：`archive/history/`

## 权利归属

本项目相关品牌设计、视觉系统、代码资产与文档内容著作权归：

**自由维度（深圳）科技有限公司**

保留所有权利。
