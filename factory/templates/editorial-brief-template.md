# Editorial Brief Template

## Purpose / 目标

This template is for internal use before drafting. It helps the agent turn a vague instruction into an executable writing task.

该模板主要供 Agent 在起稿前内部使用，用于把模糊指令收敛成可执行写作任务。

```yaml
brief_id: brief-0001
user_direction: "Raw user instruction"
interpreted_intent: explain
chosen_topic: "Precise topic statement"
article_type: original
target_language: en
target_audience: developers
author_agent: octopus-architect
primary_fact_sources:
  - nexus-node
secondary_fact_sources:
  - nexus-move
constraint_checks:
  audience_defined: true
  thesis_defined: true
  evidence_path_defined: true
  persona_fit: true
risk_notes:
  - Missing shared or public evidence path
```

## Required Content / 必填内容

1. 用户原始方向是什么
2. Agent 判断出的真实意图是什么
3. 最终选题是什么
4. 为什么这个角色适合写
5. 主要证据将从哪里来
6. 当前最大的写作风险是什么

## Usage Rules / 使用原则

1. brief 可以不直接展示给用户，但起稿前应先在内部完成。
2. 如果用户方向已经非常明确，brief 可以极简。
3. 如果用户方向很模糊，brief 应承担选题收敛职责。