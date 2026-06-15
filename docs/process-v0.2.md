# Agent Development Process v0.2

这是一个面向真实使用的流程草稿。目标不是马上开发 Agent，而是先建立一套可进化的开发系统。

## 核心目标

每次使用 Agent 开发，都不只产出代码，还要产出可追溯的经验。

```text
真实任务
  -> Agent 执行
  -> 记录不舒服的行为
  -> 归因
  -> 更新策略或流程
  -> 沉淀评估案例
  -> 下次验证是否改善
```

## 核心产物

一次任务结束后，理想情况下会更新以下一种或多种产物：

- `docs/session-reports/`：本次任务复盘。
- `docs/casebook/`：值得保留的历史问题案例。
- `docs/policies/`：稳定下来的工程策略。
- `docs/decisions/`：重要流程决策和原因。
- `docs/evaluations/`：用于防止 Agent 行为退化的评估案例。

不是每次都要全部更新。Stage 0 按三档处理：

- 微任务：不单独写 session report，但必要 friction 至少写入稳定的 lightweight friction log。
- 有实质代码或文档变更的任务：写最小 session report。
- 出现可复用问题、稳定规则、重要决策或防回归需求时：再进入 casebook、policy、ADR 或 evaluation。

## 产物路由规则

避免把同一件事重复写进多个地方。默认按以下规则路由：

- session report：任务的原始记录；每个有实质变更的任务都写最小记录。
- friction log：微任务和零散观察的 append-only inbox；默认位置是 `docs/casebook/inbox.md`。
- casebook：只有可复用、可复盘、未来可能重复的问题才单独沉淀。
- policy note：重复出现或高影响但还没稳定的规则假设，状态必须是 `proposed`。
- active policy：经过验证、准备成为默认流程的稳定规则，状态必须是 `active`。
- ADR：只有存在 trade-off、限制未来行为、或团队可能追问原因时才写。
- evaluation candidate：值得观察、可能转成防回归用例的问题线索。
- evaluation：只有需要防止 Agent 行为退化、且足够高信号的问题才写。

## 一次任务的推荐流程

### 1. Intake：明确任务

开始前先写清楚：

- 要解决什么问题
- 不解决什么问题
- 哪些文件或模块可能相关
- 验收标准是什么
- 是否需要测试
- 是否允许重构

产物：可以写在 session report 的 `Goal` 里。

### 2. Plan：制定轻量计划

复杂任务需要计划，简单任务可以跳过。

计划应该回答：

- 先看哪些文件
- 可能改哪些文件
- 如何验证
- 是否需要分离 Test Agent / Dev Agent / Review Agent
- 是否存在高风险点

避免写很长的假计划。计划只服务于执行。

### 3. Execute：执行开发

执行时遵守当前策略：

- 测试优先验证行为，不优先验证实现细节。
- 实现保持简单直接。
- 防御编程放在边界，不在内部重复堆检查。
- Agent 不应擅自扩大范围。
- 如果测试和实现出现冲突，先判断测试是否有价值，而不是盲目让代码迎合测试。

### 4. Verify：真实验证

任务完成前必须有真实验证。

可能的验证包括：

- 运行相关测试
- 运行 lint/typecheck
- 手动执行关键路径
- 检查 git diff
- Review 测试是否绑定实现细节
- Review 代码是否过度防御或啰嗦

产物：验证命令和结果写进 session report。

#### Verification Failure Rule

如果真实验证无法完成，Agent 必须记录：

- 尝试过的验证命令或路径
- 失败原因
- 替代验证
- 剩余风险
- 是否可以声称任务完成

没有真实验证时，不应使用“已完成”等结论性表述。必要时，把“验证缺失”本身记录为 friction。

### 5. Reflect：记录复盘

任务结束后做短复盘。

最小复盘只回答三个问题：

```text
这次哪里做得好？
这次哪里不舒服？
下次要不要改流程？
```

如果没有明显问题，可以只写一句：`No notable friction.`

### 6. Distill：沉淀经验

不是所有问题都要立刻变成规则。

使用以下阈值：

- 一次出现：记录到 session report、friction log 或 casebook。
- 两次类似：补充 `proposed` policy note，不能直接当成 active policy。
- 三次类似，或一次严重问题：必须判断是否需要 policy、ADR 或 evaluation candidate。
- 只有存在明确决策理由和 trade-off 时才写 ADR；重复问题不自动升级为 ADR。
- 只有高信号、可复现、能判断通过/失败的案例才转成 evaluation。

## 问题记录格式

当发现 Agent 行为不舒服时，优先记录事实，不急着下结论。

```markdown
## Friction

### What happened

Agent 做了什么？

### Why it felt wrong

为什么不舒服？是错了，还是技术上对但工程上不舒服？

### Impact

影响是什么？维护成本、可读性、测试脆弱、范围扩大、验证不足？

### Category

`testing` / `implementation` / `requirements` / `process` / `context` / `review` / `tooling`

### Root cause guess

可能是 prompt、角色边界、流程顺序、缺少上下文、review 不够、缺少 eval，还是工具限制？
```

## 分类体系

### Testing

测试相关问题：

- 为了测试而测试
- 测试绑定实现细节
- 过度 mock
- 覆盖率驱动而不是价值驱动
- 为了过测试污染设计

### Implementation

实现相关问题：

- 过度防御编程
- 代码啰嗦
- 过度抽象
- YAGNI 违背
- fallback、option、hook 太多

### Requirements

需求相关问题：

- 需求冲突
- 验收标准缺失
- 范围不清
- 用户意图误解
- 产品行为和工程实现边界混淆

### Process

流程相关问题：

- Agent 擅自扩大范围
- 没有真实验证就结束
- 同一个 Agent 同时改测试和实现导致职责混乱
- 错误时乱修而不是归因

### Context

上下文相关问题：

- 忽略项目已有约定
- 不知道历史决策
- 重复踩已记录的问题
- 任务边界理解错

### Review

Review 相关问题：

- 只看语法，不看设计
- 没发现低价值测试
- 没发现过度防御
- 没发现行为和需求不一致

### Tooling

工具相关问题：

- 缺少必要命令
- 测试命令不稳定
- 日志不够
- Agent 看不到关键状态

## 归因规则

不要默认把问题归咎于 prompt。

每个问题先问：

1. 是需求没说清楚吗？
2. 是 Agent 角色冲突吗？
3. 是流程顺序错了吗？
4. 是缺少项目上下文吗？
5. 是 review checklist 没覆盖吗？
6. 是没有 evaluation 导致反复退化吗？
7. 是工具能力不足吗？

只有当目标行为已经明确时，才修改 prompt。

## 规则生命周期

规则不要一出现就永久化。

每条规则可以有状态：

- `proposed`：刚提出，还没有足够验证。
- `active`：已经成为默认流程。
- `deprecated`：准备移除。
- `superseded`：被新规则替代。

规则应该尽量关联来源，但不强制固定链路。现实中一条 rule 可能来自多个 case，也可能先有 ADR，再拆成 policy 和 evaluation。

每条规则至少保留 source links，例如：

- Related session reports
- Related cases
- Related ADRs
- Related evaluations

如果一条规则找不到来源，后续应该重新审视。

## Role Separation Draft

默认角色：

- Planner：澄清目标、边界和验收标准。
- Test Agent：写行为测试，不改实现。
- Dev Agent：写实现，不改测试。
- Review Agent：检查测试价值、代码简洁性、范围控制。
- Orchestrator：判断失败属于测试问题、实现问题还是需求问题。

轻量任务可以不拆角色，但要保留这个原则：

```text
不要让同一个执行者在压力下同时降低验收标准和修改实现。
```

轻量任务通常满足：单文件或少量文档修改、没有公共 API 变化、没有 failing test、验证路径明确、风险低、需求清楚。

满足任一条件时，必须至少显式区分 Planner / Test / Dev / Review 的职责，即使不启动独立 Agent：

- 同时修改测试和实现。
- 修复 failing test。
- 跨模块改动。
- 公共 API 或数据结构变化。
- 高风险数据、安全、权限或迁移逻辑。
- 需求不明确，验收标准需要澄清。
- Review 发现实现为了过测试污染设计。

单 Agent 执行时，最小格式可以是：

```markdown
## Role Separation

### Plan Decision
目标、边界、验收标准和风险判断。

### Test Responsibility
应该验证的外部行为；测试不应绑定哪些实现细节。

### Implementation Responsibility
实现要改什么；不改什么；不降低验收标准。

### Review Check
检查测试价值、代码简洁性、范围控制和真实验证结果。
```

## Objection 机制

当 Agent 认为当前任务、测试、实现或 review 结论有问题时，不应该直接绕过流程，而是提交 objection。Test Objection 是其中一种类型。

Objection 不是普通工程判断的替代品。只有满足任一条件时才提交 objection：

- 会降低验收标准。
- 会违反角色边界，例如 Dev 需要改测试。
- 会扩大任务范围。
- 无法完成真实验证。
- 需求、测试、实现或 review 之间存在实质冲突。
- 需要 Orchestrator 或用户做取舍决策。

普通局部修正、命名调整、明显 bug fix 不需要 objection。

```markdown
# Objection

## Type

`test` / `requirement` / `design` / `review` / `tooling`

## Target

测试文件、需求、实现、review comment 或工具路径。

## Problem

为什么可能是错的、低价值的、污染设计的，或无法执行的？

## Evidence

支持 objection 的事实、命令输出、代码位置或需求引用。

## Suggested Alternative

建议改成什么行为测试、需求表述、实现方向或 review 判断？

## Recommendation

修改测试 / 修改需求 / 修改实现 / 保留现状但说明例外 / 暂停并请求澄清。
```

常见 objection 类型：

- `test`：Dev 认为测试错了、绑定实现细节或价值低。
- `requirement`：需求本身冲突、不完整或和现有系统约定不一致。
- `design`：实现为了过测污染设计、过度抽象或扩大范围。
- `review`：Review 标准不适用，或漏掉更重要的风险。
- `tooling`：验证工具不可用、不稳定或输出不足。

Orchestrator 决定 objection 是否成立，以及下一步交给哪个角色处理。

Test Objection 可以使用更窄的格式：

```markdown
# Test Objection

## Test

测试文件或测试名。

## Problem

这个测试为什么可能是错的或低价值的？

## Suggested Behavior Test

应该测试什么行为？

## Recommendation

修改测试 / 修改需求 / 保留测试但说明例外。
```

Orchestrator 决定是否让 Test Agent 修改测试。


## Evaluation 机制

重要问题要转成 Agent 行为评估。

一个 evaluation 应该包含：

- 场景
- Input Prompt：给 Agent 的任务原文或最小复现提示。
- Fixture / Context：需要的文件、代码片段、历史规则或约束。
- Pass Criteria：什么行为算通过。
- Fail Criteria：什么行为算失败。
- Judge Method：人工判断、脚本断言、diff 检查、测试命令或混合方式。
- 关联 case、ADR 或 evaluation candidate

示例：

```markdown
## Evaluation: 不要默认测试私有方法 non-call

### Scenario

内部实现从 oldMethod 迁移到 newMethod，外部行为不变。

### Input Prompt

更新测试，确认迁移后行为没有回归。

### Fixture / Context

已有测试能观察外部行为；oldMethod 是私有实现细节。

### Pass Criteria

Agent 应该测试外部行为，不应该默认断言 oldMethod 没被调用。

### Fail Criteria

Agent 写了 `expect(oldMethod).not.toHaveBeenCalled()`，但没有说明副作用、安全或性能原因。

### Judge Method

人工 review 测试 diff，检查断言是否绑定私有实现细节。
```

## Session Report 最小模板

```markdown
# Session Report: <title>

## Goal

## Changes

## Verification

## Good

## Friction

## Proposed Follow-up
```

如果一次任务没有明显流程问题，`Friction` 可以写：`No notable friction.`

## 什么时候写 ADR

满足任一条件时才考虑写 ADR；如果只是重复问题，先判断是否更适合 policy note 或 evaluation candidate：

- 规则会影响多个未来任务，且需要解释为什么这样取舍。
- 规则有明显 trade-off。
- 团队以后可能会问“为什么要这样”。
- 这个决定限制了 Agent 的自由度。
- 这个决定来自一次严重事故，并且后续处理存在可争议的选择。

ADR 应包含：

- Context
- Decision
- Consequences
- Escape hatch
- Related cases
- Evaluation plan

## 当前不做的事

v0.2 暂时不做：

- 不开发完整 Agent 框架。
- 不自动化所有流程。
- 不追求完整测试体系。
- 不把所有规则都写进 prompt。
- 不强制每次任务都写长文档。

## 下一步

1. 用现有 Agent 做 3-5 个真实小任务。
2. 有实质变更的任务写最小 session report；微任务 friction 写入 `docs/casebook/inbox.md`。
3. 收集至少 10 条 friction。
4. 至少识别 2 个 evaluation candidates；其中高信号案例才转成 evaluation。
5. 识别前 3 类重复问题。
6. 再决定哪些规则值得固化。
7. 再决定 Agent 架构和自动化范围。

Stage 0 退出标准：完成 3-5 个真实任务、收集 10 条 friction、识别至少 2 个 evaluation candidates、识别前 3 类重复问题后，进入 v0.3；如果 candidates 信号不足，可以继续 Stage 0，而不是硬凑 evaluation。
