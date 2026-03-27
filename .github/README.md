# GitHub Agent Entry

## Purpose / 目标

This directory is the AI-agent entry layer for nexus-chronicles.

这个目录是 nexus-chronicles 的 AI Agent 入口层。

## Read Order / 阅读顺序

When an agent starts work, it should read in this order:

当 AI Agent 开始工作时，应按以下顺序读取：

1. `.github/copilot-instructions.md`
2. `factory/README.md`
3. Relevant files under `factory/workflows/`, `factory/standards/`, `factory/templates/`, and `factory/personas/`
4. `factory/topic-board/topic-pool.md` and the public content indexes if the task is topic discovery or drafting

## Entry Points / 入口命令

1. `start-column-draft.prompt.md`
   Start from a user direction.
   从用户给定方向开始起稿。
2. `start-from-candidates.prompt.md`
   Start from the repository topic pool.
   从仓库候选主题池开始。
3. `run-column-review.prompt.md`
   Enter review mode and append review notes.
   进入审稿模式并追加审稿记录。

## Working Contract / 工作约定

1. Use English instructions by default.
   默认使用英文指令。
2. Treat `content/` as output and `factory/` as production logic.
   把 `content/` 视为输出区，把 `factory/` 视为生产逻辑区。
3. Read shared/public sources before making technical claims.
   在写技术判断前，先读取共享或公开事实源。
4. Personal local documents are private background only when explicitly requested.
   个人本地资料只有在明确授权时，才能作为私有背景使用。
5. Keep review comments on the manuscript tail under `Review Trail / 审核记录`.
   审稿意见保留在稿件尾部的 `Review Trail / 审核记录` 区块。
6. Before finishing article work, run or satisfy `.github/scripts/validate_content.py`.
   在结束文章工作前，必须运行或满足 `.github/scripts/validate_content.py` 的校验。
7. Before committing article-related changes, run `.github/scripts/validate_content.py` locally.
   在递交与文章相关的 git 改动前，必须先在本机运行 `.github/scripts/validate_content.py`。
8. Before changing `stage` to `published`, run `.github/scripts/validate_content.py` locally and keep the article unpublished if it fails.
   在把 `stage` 改成 `published` 前，必须先在本机运行 `.github/scripts/validate_content.py`，失败时不得发布。
9. Prefer `make validate-content` as the standard local entry point.
   优先使用 `make validate-content` 作为本地统一验证入口。

## Constraints / 约束

1. Do not write contributor-local paths into shared files.
   不要把贡献者本地路径写进共享文件。
2. Do not confuse repository readers with article audiences.
   不要把仓库读者和文章读者混为一谈。
3. Do not bypass the stage system: `draft` -> `review` -> `revision` -> `published`.
   不要跳过稿件阶段系统：`draft` -> `review` -> `revision` -> `published`。