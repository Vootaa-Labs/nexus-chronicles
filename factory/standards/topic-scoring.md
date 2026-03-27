# Topic Scoring

## Purpose / 目标

Provide a lightweight scoring model so agents can choose stronger candidate topics automatically.

为候选主题建立轻量评分规则，帮助 Agent 在多个候选题中自动挑选更强的选题。

## Five Scores / 五项评分

每项 1 到 5 分，总分越高越优先：

1. Reader Value
   这篇文章对目标读者是否真的有用。

2. Evidence Strength
   仓库事实源或外部权威来源是否足够支撑。

3. Persona Fit
   是否能体现某个作者角色的独特价值。

4. Citation Potential
   是否容易被其它语言、其它角色引用和再扩展。

5. Novelty
   是否避免与已有内容重复，或能提供新解释。

## Priority Rules / 优先规则

优先选择以下类型：

1. 总分高的主题
2. 跨语言扩展潜力高的主题
3. 代码证据强的技术主题
4. 容易形成专题链路的主题

## Downgrade Rules / 降级规则

出现以下情况时，即使总分高也应降级：

1. 题目太大，写出来注定空泛
2. 证据路线依赖无法访问的来源
3. 与已有文章高度重复
4. 角色视角无法形成明显差异