---
name: 本质蒸馏
description: |
  融合三阶方法论与人物思维蒸馏的认知提炼系统。输入人名/主题/模糊需求，
  自动执行「是什么→为什么→怎么做」三阶蒸馏，生成基于类-属性-方法-路由
  模型的认知操作系统Skill。独有根因追溯、场景路由和递归深入三层能力。
  触发词：「蒸馏」「本质蒸馏」「提炼XX的思维」「XX的认知本质」「造skill」「XX的思维方式」。
  模糊需求也触发：「我想提升决策质量」「有没有一种思维方式能帮我...」「我需要一个思维顾问」。
---

# 本质蒸馏 · 三阶认知提炼系统

> **核心原则**：坡度理解 —— 先点出概念 → 建立联系 → 再详细解释
>
> **设计思想**：认知系统 = Class，心智模型 = 属性，决策启发式 = 方法，场景适配 = 路由，表达DNA = 接口
>
> **蒸馏公式**：三阶方法论（是什么→为什么→怎么做）× 坡度理解 × 类-属性-方法-路由

---

## 核心理念

本质蒸馏不只是提取「他怎么想」，而是追溯「他为什么这么想」，最终构建「怎么运行他的认知系统」。

它提取的不只是认知的**快照**，而是认知的**操作系统**——包含源码（为什么）、运行时（怎么想）、API（怎么用）。

**关键区分**：
- 表层蒸馏：捕捉的是 HOW they think
- 本质蒸馏：捕捉的是 WHY they think that way → HOW they think → HOW TO RUN their cognitive system

---

## 已蒸馏实例

所有已蒸馏的实例存放在 `examples/` 目录下，每个子目录包含完整的Skill（SKILL.md + references）。

**扫描方式**：执行时扫描 `examples/` 目录，读取每个子目录下 `SKILL.md` 的 frontmatter（name + description）即可获取实例信息。不在本文件中硬编码实例列表，避免遗漏和不同步。

**当前实例**（由 README.md 动态维护）：
- `examples/nihaixia.skill/` — 倪海厦
- `examples/socrates.skill/` — 苏格拉底
- `examples/laozi.skill/` — 老子
- `examples/luxun.skill/` — 鲁迅

---

## 执行流程概览

| Phase | 名称 | 核心任务 | 详见 |
|-------|------|---------|------|
| **Phase 0** | 入口分流 | 判断直接路径 vs 诊断路径 | [workflows/person-distillation.md](workflows/person-distillation.md) |
| **Phase 0A** | 需求澄清 | 确认人物、聚焦方向、语料来源 | [workflows/person-distillation.md](workflows/person-distillation.md) |
| **Phase 0B** | 需求诊断 | 从模糊需求反推蒸馏对象 | [workflows/person-distillation.md](workflows/person-distillation.md) |
| **Phase 0.5** | 创建目录 | 建立Skill目录结构 | [workflows/person-distillation.md](workflows/person-distillation.md) |
| **Phase 1** | 信息采集 | 7个Agent并行调研 | [workflows/person-distillation.md](workflows/person-distillation.md) |
| **Phase 1.5** | 调研Review | 展示调研质量摘要 | [workflows/person-distillation.md](workflows/person-distillation.md) |
| **Phase 2** | 三阶蒸馏 | 是什么→为什么→怎么做 | [workflows/person-distillation.md](workflows/person-distillation.md) |
| **Phase 3** | 构建Skill | 填入模板生成Skill | [workflows/person-distillation.md](workflows/person-distillation.md) |
| **Phase 4** | 质量验证 | 三重验证+四层校验+实战 | [workflows/person-distillation.md](workflows/person-distillation.md) |
| **Phase 4.5** | Few-shot生成 | 闭环自增强 | [workflows/person-distillation.md](workflows/person-distillation.md) |
| **Phase 5** | 递归深入 | 对✅模型递归蒸馏 | [workflows/person-distillation.md](workflows/person-distillation.md) |

---

## 核心概念（速览）

| 概念 | 一句话 | 详见 |
|-----|--------|------|
| **三阶蒸馏** | 是什么(认知本质)→为什么(根因追溯)→怎么做(系统建模) | [workflows/person-distillation.md](workflows/person-distillation.md) |
| **根因追溯** | 追溯「他为什么这么想」而非只记录「他怎么想」 | [references/distillation-framework.md](references/distillation-framework.md) |
| **三重验证** | 跨域复现+生成力+排他性筛选心智模型 | [workflows/person-distillation.md](workflows/person-distillation.md) |
| **场景路由** | 不同问题类型调用不同模型组合 | [workflows/person-distillation.md](workflows/person-distillation.md) |
| **表达DNA** | 语气、节奏、用词的可执行规则 | [references/skill-template.md](references/skill-template.md) |
| **矛盾处理** | 保留矛盾，记录为时间性/领域性/本质性张力 | [references/distillation-framework.md](references/distillation-framework.md) |
| **根因可信度** | 🟢确定→🟡强推测→🟠弱推测→⚪未知 | [references/distillation-framework.md](references/distillation-framework.md) |
| **信息不足处理** | 诚实标注局限，不编造因果链 | [references/distillation-framework.md](references/distillation-framework.md) |
| **Agent Prompt模板** | 7个Agent的任务分配和输出要求 | [references/distillation-framework.md](references/distillation-framework.md) |

---

## 质量自检清单

### 心智模型
- [ ] 每个模型都有至少2个不同领域的证据？
- [ ] 模型数量在3-7个之间？
- [ ] 每个模型都有明确的应用场景和局限？
- [ ] 模型之间有张力但不矛盾？

### 根因追溯（本质蒸馏独有）
- [ ] 每个核心模型都有形成根因？
- [ ] 根因的可信度已分级标注？
- [ ] 至少50%的模型有🟢确定或🟡强推测根因？

### 场景路由（本质蒸馏独有）
- [ ] 路由表覆盖≥3个场景？
- [ ] 每个场景的模型组合有依据？
- [ ] 有默认路由和边界说明？

### 表达DNA
- [ ] 读起来有辨识度，不像通用AI？
- [ ] 没有过度模仿变成caricature？
- [ ] 抓住了核心特征而非表面模仿？

### 坡度完整性（本质蒸馏独有）
- [ ] 坡度1：30秒能抓住此人认知本质？
- [ ] 坡度2：2分钟能理解心智模型之间的关系？
- [ ] 坡度3：深入任何模型都有完整证据链？

### 诚实边界
- [ ] 明确写了做不到什么？
- [ ] 标注了信息源和调研时间？
- [ ] 承认了信息不足的维度？

### 整体
- [ ] 用此人的眼睛看一个新问题，能得到有价值的视角？
- [ ] 不是此人原话的拼凑，而是框架的运行？
- [ ] 删掉名字后，还能认出这是谁的思维方式？

---

## 项目结构

```
本质蒸馏/
├── SKILL.md                              # 本文件：主入口
├── references/                           # 方法论参考
│   ├── distillation-framework.md         # 蒸馏方法论详解（Agent模板、根因可信度、矛盾处理、信息不足处理）
│   ├── extraction-framework.md           # 三阶蒸馏方法论详解（原有）
│   └── skill-template.md                 # 认知操作系统Skill模板
├── workflows/                            # 工作流
│   └── person-distillation.md            # 人物蒸馏完整工作流（Phase 0-5）
└── examples/                             # 蒸馏实例（每个都是自包含的）
    └── nihaixia.skill/                   # 实例1：倪海厦
        ├── SKILL.md                      # 倪海厦认知操作系统
        └── references/
            ├── research/                 # 7个Agent调研结果
            ├── essence/                  # 三阶蒸馏结果
            └── sources/                  # 一手素材
```

---

*本质蒸馏 · 三阶认知提炼系统 · 三阶方法论 × 坡度理解 × 类-属性-方法-路由*
