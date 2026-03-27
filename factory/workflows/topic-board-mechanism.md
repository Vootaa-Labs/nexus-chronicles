# Topic Board Mechanism

## Purpose / 目标

Maintain a durable topic pool and editorial board so agents can discover high-value topics from repository signals instead of inventing topics from scratch every time.

建立一个可持续更新的选题池和编辑看板，让 Agent 能从仓库信号中自动发现高价值选题，而不是每次都从零开始起题。

## Two Layers / 两层结构

1. 选题池
   存放所有候选主题卡，不论是否已经排期。

2. 选题看板
   用于标记候选主题当前所处状态，例如待观察、待起稿、待引用扩展、已完成。

## Topic Signals / 选题来源

候选主题主要来自五类信号：

1. 语言缺口
   某篇文章已有母语原创，但其它语言尚无引用或回应文章。

2. 主题缺口
   栏目索引里已标出高价值主题，但仍没有正式文章。

3. 证据密度高
   `nexus-node` 或 `nexus-move` 中存在高信息密度模块，适合写成文章。

4. 争议与误读
   项目中容易被误解、夸大、低估或被错误叙述的部分。

5. 叙事机会
   某项能力、思路、边界或应用场景具备对外传播价值。

## Board Status / 看板状态

推荐使用以下状态：

1. `watching`
   候选主题已发现，但尚未收敛。

2. `ready`
   已具备明确读者、角色和证据路径，适合起稿。

3. `in-draft`
   已进入写作。

4. `needs-citation`
   已有原创文章，适合被其它语言引用和再写作。

5. `published`
   已有正式文章。

6. `retired`
   已失去时效性，或与其它主题重复。

## Agent Behavior / Agent 的自动工作方式

当用户不给方向时，Agent 应按以下顺序工作：

1. 读取选题池和语言索引
2. 按评分规则筛掉低价值候选题
3. 结合当前角色能力选择最合适的题
4. 生成一份内部 brief
5. 直接开始起稿，除非缺少关键事实源

## Management Rules / 管理原则

1. 选题池不是待办清单的堆积场。
2. 每个候选题都应说明为什么值得写。
3. 能被多语言引用扩展的主题优先级更高。
4. 无证据路径的题目不要进入 `ready`。