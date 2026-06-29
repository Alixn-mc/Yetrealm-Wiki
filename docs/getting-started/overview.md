# 概览

Yetrealm 的核心不是单纯增加更多物品，而是把探索、战斗、属性成长和世界规则织成一条长期生存路线。源码中注册了 2 个自定义维度、10 个 Yetrealm 群系、27 个方块、193 个物品与 61 个技能节点。

## 设计主轴

<div class="yr-card-grid">
  <div class="yr-card"><h3>探索驱动</h3><p>关键推进点从 Ancient City 开始，穿过远古传送门后逐步解锁远古宇宙资源、深渊遗迹、火山生态与星界结构。</p></div>
  <div class="yr-card"><h3>战斗进阶</h3><p>Boss 掉落与精英怪奖励推动装备阶梯：Meteorite → Ancient Metal → Primordial Alloy → Plasma。</p></div>
  <div class="yr-card"><h3>饰品构筑</h3><p>Curios 槽位让戒指、护符、项链、背部、足部与腰带成为构筑核心，而不是附属品。</p></div>
  <div class="yr-card"><h3>世界可调</h3><p>新世界可选择预设难度，也可以自定义生物倍率、饥饿、幸运、精英概率、硬核规则与槽位数量。</p></div>
</div>

## 与原版/整合包的交互

- **属性系统**：Yetrealm 自带饥饿上限、跳跃次数、鞘翅速度、拾取范围、命中率、伤害免疫等属性，同时依赖 Apothic Attributes 承载暴击、投射物、火焰/冰霜伤害等构筑。
- **Curios**：饰品在 Curios 槽位中工作，默认额外提供大量戒指/护符/背部槽，适合高强度后期构筑。
- **生存难度**：Cursed 与 Hardcore Cursed 会显著提升怪物生命、伤害、护甲和撕裂能力。服务器应在开服前确定难度，因为世界难度保存于世界数据。
- **经验与铁砧**：Mechanics Guide 明确说明铁砧取消 40 级过于昂贵限制，铁砧和附魔台改为消耗原始经验点。

## 主要内容地图

| 内容 | 代表页面 | 用途 |
| --- | --- | --- |
| 维度 | [Ancient Universe](../dimensions/ancient-universe.md)、[Astral Realm](../dimensions/astral-realm.md) | 查入口、环境、资源和路线 |
| 系统 | [世界难度](../systems/world-difficulty.md)、[技能树](../systems/skill-tree.md)、[Curios](../systems/curios.md) | 查规则和构筑 |
| 图鉴 | [物品](../catalog/items.md)、[装备](../catalog/equipment.md)、[生物](../catalog/entities.md) | 查注册内容与功能 |
| 参考 | [配方](../reference/recipes.md)、[掉落](../reference/loot.md)、[配置](../reference/config.md) | 给服主、整合包作者和维护者使用 |
