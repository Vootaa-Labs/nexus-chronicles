# Fact Sources

## Purpose / 目标

Define a stable fact-source order so technical claims stay verifiable and shared-repository safe.

为 Nexus 专栏建立稳定的事实源优先级，确保技术判断可验证并符合共享仓库边界。

## Source Priority / 事实源优先级

1. `Vootaa-Labs/nexus-node`
2. `Vootaa-Labs/nexus-move`
3. 本仓库内已有文章及其引用链
4. 外部权威来源，如论文、标准、官方技术博客
5. 贡献者明确指定读取的个人本地资料，仅可作为私有背景，不属于共享事实源

## Usage Rules / 使用规则

1. 只要涉及 Nexus 的具体实现、模块边界、接口行为、依赖关系或工程能力，优先从代码仓库找证据。
2. 共享仓库规则中，只记录组织共享或公开可验证的事实源。
3. 贡献者可以临时要求 AI Agent 阅读个人本地文档作为背景，但这些文档不能直接写入共享仓库，也不能被当作共享证据链的一部分。
4. 外部资料主要用于补充背景、对照方案和理论依据。

## Writing Constraints / 写作约束

1. 代码证据不足时，使用“推测”“可能”“待验证”等表述，不写成确定事实。
2. 引用外部论文时，要说明它是参考系，不代表 Nexus 当前实现已经具备该性质。
3. 文章中如果出现核心技术判断，最好在文末列出事实源仓库或文件路径。
4. 不要把个人本地路径、个人笔记标题或私有目录名称写进共享仓库文件。