# Skill-from-Masters 改进说明

## 改进目标

根据创建高质量非技术类Skill的5条原则，系统性改进 skill-from-masters 本身。

## 5条核心原则

1. **选题要窄** - 非常明确的一个任务（比如B2B冷邮件 vs 项目报告邮件，完全不同的skill）
2. **用Opus** - 不要用任何其他弱的模型（sonnet也不行）
3. **用Skill from master方法** - 先跟它持续沟通，让它找到模型本身、网络上、黄金案例、反例等，直到非常清晰可靠的结论，再写skill
4. **考虑用plan** - 对复杂的任务，宁愿它多思考再行动
5. **让agent思考非常广泛的测试场景** - 看它的测试结果再优化

---

## 具体改进清单

### ✅ 1. 添加"关键要求"专门章节

在SKILL.md开头增加 **"Critical Requirements for Non-Technical Skills"** 章节，明确说明：
- 技术类skill有标准答案，非技术类差异巨大
- 必须遵循的5条原则
- 每条原则都有具体说明和示例

### ✅ 2. 强调任务范围要窄（原则1）+ 新增5层细化框架

**在Step 1中大幅增强：**

#### **新增完整的5层细化框架 (5-Layer Narrowing Framework):**

**Layer 1: Domain Identification** - 领域识别
- 从宽泛任务识别核心领域
- 提供问题模板帮助分类

**Layer 2: Context Constraints (5W1H)** - 场景约束
- 通过WHO/WHAT/WHERE/WHEN/WHY/HOW系统化收集上下文
- 确保理解具体使用场景

**Layer 3: Comparative Narrowing** - 对比式细化
- 提供2-3个相近但不同的具体场景
- 强制用户选择或澄清

**Layer 4: Boundary Validation (Via Negativa)** - 边界验证
- 通过"不是什么"来确认范围
- ✅ 包括什么 / ❌ 不包括什么

**Layer 5: Concrete Case Anchoring** - 具体案例锚定
- 要求用户描述真实的最近案例
- 锁定具体的输入、输出、困难点

#### **新增Stop Condition（停止条件）:**
提供5个检查项判断是否已经够窄：
1. 是否有独特的方法论？
2. 质量标准是否明确？
3. 是否有具体的约束条件？
4. 用户是否提供了具体案例？
5. 是否明确了排除的内容？

**全部YES才够窄，任何NO都要继续细化。**

#### **新增反面案例：**
- ❌ 太宽："写更好的邮件" / "做产品决策" / "创建营销内容"
- ✅ 够窄："给企业CTO的B2B冷邮件" / "B2B SaaS PM的季度路线图优先级" / "技术创始人的LinkedIn思想领导力帖子"

#### **新增快速参考流程图：**
```
宽泛请求 → Layer 1（选域） → Layer 2（5W1H） → Layer 3（选场景）
→ Layer 4（确认边界） → Layer 5（真实案例） → 检查停止条件
→ ✅够窄/❌继续细化
```

### ✅ 3. 明确要求使用Opus（原则2）

**多处强化：**
- 关键要求章节：标注为"MANDATORY"
- Step 9（生成skill时）：明确说明要用 `model: "opus"` 参数
- Quality Checklist：单独检查项确认使用Opus

### ✅ 4. 强化methodology研究直到"非常清晰可靠"（原则3）

**在Step 3中增加Layer 4：**
- 新增"Keep Iterating Until Clear"步骤
- 明确说明：不要在第一轮搜索就停止
- 要求标注"confidence level"
- 继续研究循环直到能自信地说"这是已验证的方法"

**改进要点：**
- 强调要用到模型自己的知识
- 强调要找到当前网络上的最佳实践
- 强调要找到黄金案例和反例

### ✅ 5. 增加Plan Mode指导（原则4）

**在Workflow开头新增"Before Starting"指导：**
- 明确说明何时应该考虑plan mode
- 提供建议用语供agent使用
- 强调对于涉及判断、说服、复杂决策的skill更适合plan mode

**在Quality Checklist中：**
- 新增专门的plan mode检查项

### ✅ 6. 增加完整的测试和迭代框架（原则5）

**新增Step 8: Design Test Scenarios（在生成之前）：**
- 要求设计多样化测试用例
- 包括典型场景、边缘情况、边界条件、失败模式
- 考虑上下文变化（不同expertise level、组织类型、约束条件）
- 定义质量标准和常见错误

**新增Step 10: Test, Review, and Iterate：**
- 明确"不要在第一次生成就停止"
- 提供系统化的迭代流程：
  1. 运行测试场景
  2. 评估结果
  3. 识别差距
  4. 完善方法论
  5. 重新生成
  6. 重复直到质量达标
- 强调让用户参与评估

**在Quality Checklist中：**
- 新增"Testing & Iteration"专门部分，包含4项检查

### ✅ 7. 更新示例对话

改进"Example Interaction"部分，展示：
- ✅ 如何帮助用户缩小范围
- ✅ 如何建议使用plan mode
- ✅ 如何进行深入研究
- ✅ 如何设计测试场景并让用户参与
- ✅ 如何基于测试结果迭代

### ✅ 8. 完善Quality Checklist

将原来的6项扩展为18项，分为5个类别：
1. **Scope & Clarity** (2项)
2. **Methodology Depth** (6项)
3. **Generation Quality** (3项)
4. **Testing & Iteration** (4项)
5. **Plan Mode** (2项，如适用)

---

## 改进效果

### 改进前的问题：
- ❌ 没有区分技术类和非技术类skill的差异
- ❌ 没有强调任务范围要窄
- ❌ **没有系统化的方法帮助用户缩小范围**
- ❌ 没有提到模型选择（Opus requirement）
- ❌ 研究流程不够明确"直到非常清晰可靠"
- ❌ 没有plan mode指导
- ⚠️  测试框架不够完整和前置

### 改进后的优势：
- ✅ 开头就明确非技术类skill的特殊要求
- ✅ **在Step 1增加完整的5层细化框架，系统化引导用户从宽到窄**
- ✅ **提供每一层的问题模板和对话示例**
- ✅ **增加Stop Condition（5个检查项）判断是否够窄**
- ✅ **提供反面案例展示"还不够窄"vs"够窄"**
- ✅ 多处强制要求使用Opus
- ✅ Step 3明确要求持续研究直到"crystal clear"
- ✅ Workflow开头就提示plan mode
- ✅ 新增Step 8（测试设计）和Step 10（迭代）
- ✅ Quality Checklist全面覆盖所有5条原则
- ✅ **Example Interaction展示完整的5层细化过程**（从"写PRD"细化到"B2B SaaS Senior PM的工程向PRD，1-2页，新功能和大增强，最小化工程师问答"）

---

## 🎯 重点改进：5层细化框架详解

**这是本次改进中最核心的新增内容之一。**

### 为什么需要这个框架？

原有的Step 1只是简单地列出几个选项让用户选择，但没有系统化的方法。这导致：
- ❌ 如果用户选的还是太宽，没有后续方法继续细化
- ❌ 没有结构化的问题模板，每次都要临场发挥
- ❌ 不知道什么时候"够窄了"，缺乏明确的停止条件
- ❌ 没有边界验证，容易理解偏差

### 5层框架如何解决？

#### **Layer 1: Domain Identification（领域识别）**
从最宽泛的任务开始分类，快速锁定核心领域。

**示例：**
- "写报告" → 技术？业务？项目管理？研究？
- "做决策" → 产品？招聘？投资？战略？

#### **Layer 2: Context Constraints (5W1H)（场景约束）**
用6个维度系统化收集上下文信息。

**关键点：** 不是随机提问，而是有结构的5W1H框架确保不遗漏关键信息。

#### **Layer 3: Comparative Narrowing（对比式细化）**
给出2-4个相近但不同的具体场景，强制用户做选择。

**为什么有效：**
- 选择比描述容易
- 对比让差异更明显
- 用户可以说"A+C的组合"或"都不是"来进一步澄清

#### **Layer 4: Boundary Validation（边界验证）**
通过"不是什么"来确认理解正确。

**核心思想：** Via Negativa（通过否定）- 通过排除来定义，往往比正面描述更准确。

#### **Layer 5: Concrete Case Anchoring（具体案例锚定）**
要求真实案例，彻底锁定范围。

**关键价值：**
- 真实案例暴露隐藏的约束和痛点
- 提供methodology研究的具体场景
- 给测试提供真实的benchmark

### Stop Condition（停止条件）

**5个检查项判断是否够窄：**

1. ✅ **Unique methodology**: 这个具体场景是否有独特的方法论？（不是泛泛的建议）
2. ✅ **Clear quality bar**: 能否判断输出的"优秀"vs"平庸"？
3. ✅ **Specific constraints**: 是否有具体的约束、规则、tradeoff？
4. ✅ **Concrete example**: 用户是否描述了真实使用场景？
5. ✅ **Excludes alternatives**: 是否明确了不包括的相关任务？

**全部YES → 够窄，继续**
**任何NO → 继续细化**

### 实际效果对比

**改进前：**
```
用户: "我想要一个写邮件的skill"
助手: "有很多种邮件，你想要哪种？"
用户: "销售邮件"
助手: "好的，我开始找sales email的methodology..."
[结果：太宽，methodology冲突，quality bar不清晰]
```

**改进后（使用5层框架）：**
```
用户: "我想要一个写邮件的skill"
助手: [Layer 1] "邮件分很多种，是销售、内部协作、客服还是谈判？"
用户: "销售"
助手: [Layer 2] "让我了解上下文：WHO用？WHAT目标？WHERE组织类型？"
用户: "我是AE，要给企业客户写邮件推动成交"
助手: [Layer 3] "具体是：A.冷邮件首次接触？B.跟进已有联系的客户？C.推动试用转付费？"
用户: "主要是B"
助手: [Layer 4] "确认一下：✅包括已建立初步联系的follow-up，❌不包括cold outreach？"
用户: "对"
助手: [Layer 5] "能描述一个最近的场景吗？谁是收件人？你想推动什么？"
用户: "上周给某企业CTO写邮件，demo后两周没回应，想推动到下一步..."

[结果：非常明确 - "给已demo过的企业客户的follow-up邮件，AE用，推动到下一步（POC或商务谈判）"]
```

---

## 下一步（可选的进一步改进）

1. **添加中文版本的SKILL.md** - 如果目标用户包含中文使用者
2. **扩展methodology database** - 在中文领域专家（如商业、管理、写作等领域）
3. **创建skill quality评估工具** - 自动化检查生成的skill是否符合这5条原则
4. **收集案例研究** - 记录使用改进后流程创建的skills及其效果

---

## 结论

通过系统性地应用5条原则改进 skill-from-masters，我们确保了：
- 非技术类skills有明确的质量标准
- 创建流程强制执行最佳实践
- 从任务定义、研究、生成到测试的完整闭环
- Quality checklist确保不遗漏任何关键步骤

**这正是"self-bootstrapping"的体现** - 用创建优质skill的原则来改进创建skill的skill本身。
