# UNBOUNDX Logo System

UNBOUNDX 的最终版品牌标识、品牌规范站点、交付物料与设计过程归档仓库。  
品牌核心叙事为 **自由维度 / Free Dimensions**，视觉系统以 **Gravity Arcs / 引力弧线**、**Deep Void** 与 **Aerospace Orange (`#F26122`)** 为基准展开。

## Official Links

- Brand Site: `https://logo.unboundx.tech`
- Repository: `https://github.com/Jackiexiao/unboundx-logo`
- Design Process: `docs/logo-design-process.md`
- Gemini Notes: `docs/gemini-logo-design.md`

## Brand Direction

- **自由维度 / Free Dimensions**：自由、不受限、独立维度、超越常规。
- **X = Dimension**：`X` 在 UNBOUNDX 中不是普通字母，而是“维度”的符号。
- **Gravity Arcs / 引力弧线**：仅保留两条相交弧线，构成最简洁、最稳定的品牌几何形态。
- **Aerospace Orange**：用于在深色界面与线下物料中提供高识别度、高稳定性的品牌主色。

## What’s Included

- `index.html`：当前最新、最终采用的品牌规范页源码。
- `unboundx-brand-guidelines-dark.html`：深色规范页别名。
- `public/logos/`：最终 Logo 的 SVG / PNG 交付文件。
- `public/materials/`：主视觉、封面、海报、启动页等常用品牌物料。
- `public/downloads/`：打包好的下载压缩包。
- `docs/`：设计过程、AI 协作文档与项目说明。
- `archive/history/`：历史探索稿、临时文件与旧版迭代归档。

## Working Notes

- 日常编辑优先修改 `index.html`
- 发布时同步 `unboundx-brand-guidelines-dark.html`
- 根目录 `public/` 是唯一有效的交付资产目录
- `archive/history/` 仅保存历史过程，不参与当前部署
- `unboundx-brand-guidelines-v4-final.html` 已弃用，不再作为当前主稿

## Build & Deploy

- Hosting: Vercel
- Domain: `logo.unboundx.tech`
- DNS: Cloudflare
- Asset build: `python3 scripts/generate_brand_public_assets.py`

## Collaboration

本项目采用「创始人品牌主导 + AI 协作生成」工作流，主要涉及：

- Claude Code
- Codex CLI
- Gemini 3.1 Pro
- HTML / CSS / JS / SVG 代码化生成

最终交付为一个可在线浏览、可直接下载 Brand Kit ZIP 的静态品牌规范站点。

## Ownership

本仓库中的品牌设计、代码资产、文档内容及相关视觉素材著作权归：

**自由维度（深圳）科技有限公司**

保留所有权利。未经书面授权，不得复制、分发、商用或进行二次授权。
