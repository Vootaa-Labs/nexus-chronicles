# Factory

## Overview / 概览

`factory/` is the shared production system for nexus-chronicles.

`factory/` 是 nexus-chronicles 的共享生产工厂。

## Structure / 结构

1. `workflows/` for drafting, topic selection, and editorial flow.
	`workflows/` 用于起稿、选题和编辑流程。
2. `standards/` for metadata, fact-source, language, and scoring rules.
	`standards/` 用于元数据、事实源、语言和评分规则。
3. `review/` for review-unit structures.
	`review/` 用于审稿单元结构。
4. `templates/` for article, brief, index, and topic-card templates.
	`templates/` 用于文章、brief、索引和主题卡模板。
5. `personas/` for shared author personas.
	`personas/` 用于共享作者人格。
6. `topic-board/` for internal topic pools and candidate cards.
	`topic-board/` 用于内部选题池与候选主题卡。

## Boundary / 边界

1. `content/` stores article output.
	`content/` 只存放文章输出。
2. `factory/` stores how articles are produced.
	`factory/` 只存放文章生产方法。
3. `.github/` stores how AI agents enter and operate on the factory.
	`.github/` 只存放 AI Agent 的入口与运行说明。

## Style Rule / 风格规则

1. Shared factory documents should be bilingual English/Chinese.
	共享工厂文档应采用英文/中文双语。
2. Filenames should remain English kebab-case for consistency.
	文件名统一保持英文 kebab-case 风格。