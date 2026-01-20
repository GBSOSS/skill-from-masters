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

### ✅ 2. 强调任务范围要窄（原则1）

**在Step 1中增强：**
- 明确标注"CRITICAL FOR NON-TECHNICAL SKILLS"
- 提供对话示例，展示如何帮助用户缩小范围
- ❌ 坏例子："写邮件的skill"
- ✅ 好例子："给企业CTO的B2B冷邮件"

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
- ❌ 没有提到模型选择（Opus requirement）
- ❌ 研究流程不够明确"直到非常清晰可靠"
- ❌ 没有plan mode指导
- ⚠️  测试框架不够完整和前置

### 改进后的优势：
- ✅ 开头就明确非技术类skill的特殊要求
- ✅ 在Step 1强制帮助用户缩小范围
- ✅ 多处强制要求使用Opus
- ✅ Step 3明确要求持续研究直到"crystal clear"
- ✅ Workflow开头就提示plan mode
- ✅ 新增Step 8（测试设计）和Step 10（迭代）
- ✅ Quality Checklist全面覆盖所有5条原则
- ✅ 示例对话展示完整的最佳实践流程

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
