# skill-from-notebook 测试用例

## 测试覆盖

| 路径 | 用例 | 输入类型 | 预期 Skill 类型 |
|-----|------|---------|----------------|
| Path A | A1 | 技术教程 | How-to |
| Path A | A2 | 思维框架 | Framework |
| Path B | B1 | 技术博客 | 逆向写作方法论 |
| Path B | B2 | 项目 README | 逆向 README 写作指南 |

---

## Test A1: How-to 类型（方法论文档）

**输入**: https://cbea.ms/git-commit/

**描述**: 经典的 Git commit message 写作指南，包含 7 条明确规则。

**测试命令**:
```
请用 skill-from-notebook 从这篇文章中提取一个 Skill：
https://cbea.ms/git-commit/
```

**预期结果**:
- [ ] 识别为 Path A（方法论文档）
- [ ] Skill 类型识别为：How-to
- [ ] 提取出 7 条规则作为步骤
- [ ] 生成包含质量检查点的 commit message 写作 Skill

**验证要点**:
- 是否包含 "50 字符限制" 规则
- 是否包含 "使用祈使句" 规则
- 是否有 checklist 格式的检查点

---

## Test A2: Framework 类型

**输入**: 搜索 "SWOT analysis guide" 或使用任意 SWOT 分析方法文章

**描述**: 经典的商业分析框架，包含 4 个分析维度。

**测试命令**:
```
从这篇 SWOT 分析方法的文章提取一个 Skill：
[文章 URL]
```

**预期结果**:
- [ ] 识别为 Path A（方法论文档）
- [ ] Skill 类型识别为：Framework
- [ ] 提取出 4 个维度（Strengths, Weaknesses, Opportunities, Threats）
- [ ] 生成包含应用场景和使用方法的分析框架 Skill

**验证要点**:
- 是否包含核心维度定义
- 是否说明适用场景
- 是否有使用步骤

---

## Test B1: 逆向工程 - 技术博客

**输入**: https://notes.eatonphil.com/2024-04-10-what-makes-a-great-tech-blog.html

**描述**: Phil Eaton 写的一篇关于技术博客的文章，本身就是优秀技术博客的范例。

**测试命令**:
```
这是一篇写得很好的技术博客，请逆向分析它，提取出"如何写技术博客"的 Skill：
https://notes.eatonphil.com/2024-04-10-what-makes-a-great-tech-blog.html
```

**预期结果**:
- [ ] 识别为 Path B（成品范例）
- [ ] 分析文章结构（各部分及占比）
- [ ] 提取质量特征（写作风格、技巧）
- [ ] 逆向推导写作步骤
- [ ] 生成技术博客写作 Skill

**验证要点**:
- 是否分析了文章的结构组成
- 是否提取了"好在哪里"的特征
- 是否有可执行的写作步骤

---

## Test B2: 逆向工程 - README

**输入**: https://github.com/sindresorhus/awesome

**描述**: Awesome 列表的开创者，README 结构清晰、格式规范。

**测试命令**:
```
分析这个项目的 README，逆向提取出"如何写好 README"的 Skill：
https://github.com/sindresorhus/awesome
```

**预期结果**:
- [ ] 识别为 Path B（成品范例）
- [ ] 分析 README 结构
- [ ] 提取格式规范和组织方式
- [ ] 生成 README 写作 Skill

**验证要点**:
- 是否分析了章节结构
- 是否提取了格式特点（badge、目录、分类等）
- 是否有可复用的模板

---

## Test C: 边界情况

### C1: 不适合生成 Skill 的内容

**输入**: 一篇新闻报道或纯观点文章

**预期结果**:
- [ ] 识别为"不适合"
- [ ] 向用户解释原因
- [ ] 不强行生成 Skill

### C2: 混合类型

**输入**: 既包含教程又包含范例的文章

**预期结果**:
- [ ] 正确识别主要类型
- [ ] 或询问用户想要哪种提取方式

---

## 测试执行记录

| 日期 | 用例 | 结果 | 备注 |
|-----|------|------|------|
| | A1 | | |
| | A2 | | |
| | B1 | | |
| | B2 | | |
| | C1 | | |
| | C2 | | |

---

## 参考资源

- 设计文档: [docs/skill-from-notebook-design.md](../../docs/skill-from-notebook-design.md)
- Skill 实现: [SKILL.md](./SKILL.md)
