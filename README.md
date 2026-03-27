# nexus-chronicles

> A multilingual column universe for Nexus: native-language originals, cross-language citations, and role-driven AI authorship.

## 仓库定位

`nexus-chronicles` 不是传统项目文档仓库，而是 Nexus 项目的内容中台。

它服务三类目标：

1. 以 GitHub Pages 作为自有展示阵地，沉淀 Markdown 专栏内容。
2. 以 Medium 等第三方平台作为分发出口，扩展项目影响力。
3. 以多语言、多角色、多视角的方式持续生产高质量内容，而不是维护单一文档真相源。

## 核心原则

1. 文章以母语原创为主，不做机械翻译。
2. 不同语言作者可以引用原文，并基于本地语境重新写作。
3. 角色设定先于文风，文风先于产量。
4. 内容网络优先于目录堆叠，避免题材枯竭和重复写作。
5. 规则与流程、内容产出、Agent 设定分离管理。

## 目录结构

```text
nexus-chronicles/
├── .github/
│   ├── copilot-instructions.md    GitHub Copilot 工作区规则
│   └── agents/                    三个模型导向的 Copilot Agents
├── playbook/
│   ├── workflows/                 生产流程
│   └── standards/                 元数据、引用、语言扩展规则
├── content/
│   ├── zh/                        中文内容区
│   ├── en/                        英文内容区
│   └── es/                        西班牙语内容区
├── agents/
│   └── roster/                    海洋生物作者设定
├── templates/                     文章模板
├── LICENSE
└── README.md
```

## 三语言机制

当前默认语言为：

1. `zh` 中文
2. `en` English
3. `es` Espanol

这里的多语言不是同一篇内容的平移翻译，而是：

1. 先由某个角色在某个母语中完成原创文章。
2. 其他语言作者引用该文章，并做摘要说明。
3. 引用作者继续写出面向本语言读者的新文章。

这套机制让内容关系更接近论文引用网络，而不是镜像站。

## Agent 与模型

仓库采用两层结构：

1. 作者人格层：海洋生物体系的 AI 撰稿人。
2. 模型执行层：`GPT`、`Claude`、`Gemini` 三类 Copilot Agents。

模型不是作者本身，而是作者生产流程中的执行引擎：

1. `GPT` 偏首稿构建与结构化写作。
2. `Claude` 偏批判审校与论证完整性检查。
3. `Gemini` 偏资料扫描、主题侦察和关联发现。

## 第一阶段使用方式

1. 先确定一个主题、受众和目标语言。
2. 从 `agents/roster/` 中选择一个母语撰稿人。
3. 使用 `templates/article-template.md` 起稿。
4. 按 `playbook/workflows/editorial-pipeline.md` 走完写作、引用、复审和发布。

## GitHub Pages

本仓库当前先完成内容结构与工作流定义。

后续启用 GitHub Pages 时，建议优先选择以下方案之一：

1. 直接使用 GitHub Pages 对 Markdown 目录进行轻量展示。
2. 使用静态站点生成器将 `content/` 渲染为专栏站。

在内容模型稳定之前，不建议过早绑定具体站点框架。

## 许可证

当前仓库默认内容许可证为 `CC BY 4.0`，鼓励传播、引用和再创作，但必须保留署名。

如果未来仓库中增加较多自动化脚本或站点代码，再拆分内容许可证与代码许可证。