# Editorial Pipeline

## Purpose / 目标

Produce publishable, citable, multilingual-ready columns with the smallest stable workflow.

用最少且稳定的流程产出可发布、可引用、可跨语言扩展的专栏文章。

## User Trigger / 用户触发方式

The user only needs to provide a short instruction plus optional source material.

用户只需要给出一条简短指令，加上可选资料来源。

Recommended inputs / 推荐输入要素：

1. 主题
2. 目标读者
3. 目标语言
4. 作者角色
5. 可选资料来源

Recommended minimal instruction example:

```text
Write an original English column in the voice of octopus-architect for developers about Nexus execution architecture.
Sources: nexus-node/crates/nexus-execution. Use nexus-move only if needed.
```

If the user gives only a direction, a question, or a partial judgment, the agent should not draft immediately. It should first enter a short planning stage.

如果用户给出的只是一个方向、一个问题或一个片面判断，Agent 不应立即机械起稿，而应先进入短暂的策划阶段。

## Editorial Flow / 编辑流程

1. 指令解读
   先判断用户的真实意图是什么：要解释、比较、批判、审计、科普，还是做行业叙事。

2. 策划与选题
   在大致满足用户方向的前提下，自主完成一个最小选题过程：

   1. 收敛主题边界
   2. 判断最适合的文章类型
   3. 判断最合适的目标读者
   4. 选择最合适的作者角色
   5. 初步列出事实源与证据路径

   这一阶段建议先生成一份内部编辑 brief，参考 `factory/templates/editorial-brief-template.md`。

3. 指派母语撰稿人
   从海洋作者系统中选择一个角色，确定其母语和主视角。

4. 约束检查
   在起稿前检查是否满足仓库约束：

   1. 是否有明确受众
   2. 是否有可成立的中心论点
   3. 是否有足够的事实源
   4. 是否适合当前角色口吻
   5. 是否应写成原创、引用、回应或综述

5. 建立原创文章
   先写母语原创版本，禁止直接先做多语言平行稿。

6. 记录引用锚点
   为原创文章写出可引用摘要、核心论点和文章 ID。

7. 触发跨语言写作
   其他语言作者先摘要说明原文，再写自己的专栏版本。

8. 初稿生成
   优先使用起稿 Agent 产出首稿，默认沿用 GitHub Copilot 当前模型设置；如果需要更强区分，再手动切换模型。

9. 进入审稿阶段
   用户明确发出“进入审稿阶段”的指令后，选定合适的审稿人角色，最好与起稿模型不同。

10. 审稿意见单元
   按 `factory/review/review-note-template.md` 输出一份小型审稿单元，至少包含：

   1. 总体判断
   2. 主要问题
   3. 证据缺口
   4. 角色一致性问题
   5. 建议修改动作

11. 模型复审
   `GPT` 负责结构与表达，`Claude` 负责论证与批判，`Gemini` 负责补充关联主题和引用线索。

12. 本地格式验证
   在结束前运行仓库验证脚本，确认稿件元数据、审稿尾部、索引登记与引用登记均满足要求。

13. 发布归档
   在 `content/<language>/` 下归档文章，并回填 `content/indexes/article-index.md`、对应语言索引，以及需要时的引用关系页。

14. 递交与发布门禁
   在 git 提交与文章进入 `published` 状态前，必须先在本机运行 `.github/scripts/validate_content.py`；验证失败时，不得提交为发布结果。

## Autonomy Boundaries / 自主性边界

Agent 可以自主完成以下动作：

1. 从模糊方向中收敛出更具体的文章题目。
2. 自主判断更适合的文章类型和作者人格。
3. 自主决定先读哪些代码、文章和外部材料。
4. 自主决定文章从哪个切口切入更有价值。

Agent 不应擅自越过以下边界：

1. 不能把用户的大方向改成无关主题。
2. 不能伪造代码证据或引用关系。
3. 不能跳过仓库约束直接产出空泛内容。
4. 不能把不确定判断包装成既定事实。

## Fact-Source Rules / 事实源规则

1. 涉及 Nexus 技术细节时，优先从 `nexus-node` 和 `nexus-move` 代码中找证据。
2. 共享仓库规则中，不记录个人本地资料路径或个人背景文档。
3. 如果贡献者明确要求 Agent 读取个人本地资料，该资料只作为临时背景，不自动进入共享事实源。
4. 外部论文和标准文档可以作为补充，但不能替代项目代码事实。

## Prohibited Moves / 禁止事项

1. 不要把“多语言”理解为同步翻译任务。
2. 不要在没有目标读者的前提下起稿。
3. 不要把作者人格与模型能力混为一谈。
4. 不要为了凑量生成没有明确论点的文章。
5. 不要在缺少代码证据时把技术猜测写成确定事实。