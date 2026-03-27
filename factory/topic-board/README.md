# Topic Board

## Purpose / 目标

`factory/topic-board/` stores the internal editorial planning board for AI agents and contributors.

`factory/topic-board/` 用于存放 AI Agent 与贡献者共享的内部选题规划内容。

## Contents / 内容

1. `topic-pool.md` keeps the current board state and commissioning priorities.
	`topic-pool.md` 记录当前选题看板状态与优先级。
2. `topic-cards/` stores one card per candidate topic.
	`topic-cards/` 为每个候选主题提供单独主题卡。

## Boundary / 边界

1. This directory is part of the factory, not part of the public GitHub Pages reading surface.
	这个目录属于工厂层，不属于公开 GitHub Pages 阅读层。
2. Readers should browse topic, author, article, and citation indexes under `content/`.
	读者应从 `content/` 下的主题、作者、文章和引用索引进入站点。