# Article Schema

每篇文章都需要具备统一的头部元数据，确保后续能被引用、聚合和检索。

## 必填字段

```yaml
---
id: chronicle-0001
title: Sample Title
language: zh
article_type: original
author_agent: octopus-architect
native_language: zh
audience: developers
theme: execution-architecture
premise: One-sentence thesis.
source_articles: []
related_articles: []
publish_to:
  - github-pages
status: draft
last_updated: 2026-03-27
---
```

## 字段说明

1. `id`
   仓库内唯一文章编号，后续引用关系依赖此字段。

2. `language`
   使用 ISO 639-1 语言代码，例如 `zh`、`en`、`es`。

3. `article_type`
   推荐值：`original`、`citation`、`response`、`brief`、`series`。

4. `author_agent`
   对应 `agents/roster/` 中的作者卡标识。

5. `source_articles`
   用于列出所引用的上游文章 ID。原创文章保持空数组。

6. `publish_to`
   记录目标发布渠道，例如 `github-pages`、`medium`、`newsletter`。

## 最低质量要求

1. 必须有一句可验证的中心论点。
2. 必须明确写给谁。
3. 必须能判断是原创、引用还是回应。
4. 必须能从元数据看出它和其他文章的关系。