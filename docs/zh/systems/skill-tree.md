# 技能树

Yetrealm 的技能树由 `data/yetrealm/skills/skill_tree.json` 驱动。每个节点定义坐标、前置、属性、每级加成、最大等级、图标和消耗。世界难度 Custom 可开关技能树。

## 操作

- 左键：升级。
- 右键：降级。
- `H` / `Space` / `Enter`：回到主界面。
- `Ctrl + 左键/右键`：自动升级/降级。
- `Ctrl + 滚轮`：缩放。
- 创造模式下，`Ctrl + 左键`介绍图标可全部升满，`Ctrl + 右键`可全部降级。

## 节点索引

| 节点 ID | 名称 | 前置 | 属性 | 每级加成 | 操作 | 满级 | 消耗 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| attack_node | 锋利之剑 | — | minecraft:generic.attack_damage | 0.5 | ADD_VALUE | 5 | 50 XP |
| attack_speed_node | 迅捷打击 | attack_node | minecraft:generic.attack_speed | 5% | ADD_MULTIPLIED_BASE | 5 | 150 XP |
| attack_damage_percent_node | 力量涌动 | attack_node | minecraft:generic.attack_damage | 2.5% | ADD_MULTIPLIED_BASE | 10 | 180 XP |
| attack_damage_flat_node | 沉重打击 | crit_chance_node | minecraft:generic.attack_damage | 0.5 | ADD_VALUE | 5 | 800 XP |
| crit_chance_node | 精准打击 | attack_speed_node | apothic_attributes:crit_chance | 0.05 | ADD_VALUE | 5 | 3 × 初级怪物精华 (yetrealm:primary_monster_essence) |
| entity_reach_node | 幻影触及 | attack_damage_percent_node | minecraft:player.entity_interaction_range | 0.2 | ADD_VALUE | 5 | 2 × 中级怪物精华 (yetrealm:intermediate_monster_essence) |
| crit_chance_advanced_node | 致命精准 | prot_pierce_node | apothic_attributes:crit_chance | 0.03 | ADD_VALUE | 10 | 1000 XP |
| hit_rate_node | 必中之眼 | crit_chance_advanced_node | yetrealm:hit_rate | 1.5% | ADD_VALUE | 10 | 1200 XP |
| bow_damage_node | 神射手 | attack_node | apothic_attributes:arrow_damage | 0.05 | ADD_VALUE | 5 | 150 XP |
| crossbow_charge_node | 迅捷上膛 | bow_damage_node | apothic_attributes:draw_speed | 5% | ADD_MULTIPLIED_BASE | 5 | 3 × 初级怪物精华 (yetrealm:primary_monster_essence) |
| projectile_damage_node | 狙击之眼 | arrow_velocity_node | apothic_attributes:projectile_damage | 5% | ADD_MULTIPLIED_BASE | 5 | 4 × 中级怪物精华 (yetrealm:intermediate_monster_essence) |
| arrow_damage_advanced_node | 锐矢专精 | projectile_damage_node | apothic_attributes:arrow_damage | 2.5% | ADD_VALUE | 10 | 3 × 高级怪物精华 (yetrealm:advanced_monster_essence) |
| health_node | 生命之心 | — | minecraft:generic.max_health | 0.5 | ADD_VALUE | 5 | 50 XP |
| armor_node | 坚固护甲 | health_node | minecraft:generic.armor | 0.5 | ADD_VALUE | 10 | 120 XP |
| safe_fall_node | 轻如鸿毛 | armor_node | minecraft:generic.safe_fall_distance | 0.5 | ADD_VALUE | 10 | 200 XP |
| fall_damage_mult_node | 羽落术 | safe_fall_node | minecraft:generic.fall_damage_multiplier | -0.03 | ADD_VALUE | 10 | 3 × 初级怪物精华 (yetrealm:primary_monster_essence) |
| safe_fall_advanced_node | 踏风而行 | fall_damage_mult_node | minecraft:generic.safe_fall_distance | 0.5 | ADD_VALUE | 10 | 3 × 高级怪物精华 (yetrealm:advanced_monster_essence) |
| fall_damage_mult_advanced_node | 羽落真意 | safe_fall_advanced_node | minecraft:generic.fall_damage_multiplier | -3% | ADD_MULTIPLIED_TOTAL | 5 | 1000 XP |
| health_boost_node | 生命强化 | health_node | minecraft:generic.max_health | 0.5 | ADD_VALUE | 10 | 180 XP |
| health_percent_node | 活力涌动 | health_boost_node | minecraft:generic.max_health | 2% | ADD_MULTIPLIED_BASE | 10 | 2 × 中级怪物精华 (yetrealm:intermediate_monster_essence) |
| health_boost_advanced_node | 生命奔涌 | health_percent_node | minecraft:generic.max_health | 0.5 | ADD_VALUE | 10 | 3 × 高级怪物精华 (yetrealm:advanced_monster_essence) |
| health_percent_advanced_node | 不朽脉动 | health_boost_advanced_node | minecraft:generic.max_health | 1% | ADD_MULTIPLIED_BASE | 10 | 1500 XP |
| dodge_chance_node | 幻影身法 | health_percent_advanced_node | apothic_attributes:dodge_chance | 0.01 | ADD_VALUE | 5 | 4 × 高级怪物精华 (yetrealm:advanced_monster_essence) |
| knockback_resist_node | 稳固身躯 | health_node | minecraft:generic.knockback_resistance | 0.04 | ADD_VALUE | 5 | 80 XP |
| toughness_node | 坚韧之躯 | fire_damage_divisor_node | minecraft:generic.armor_toughness | 0.4 | ADD_VALUE | 10 | 4 × 初级怪物精华 (yetrealm:primary_monster_essence) |
| fire_damage_divisor_node | 耐火之躯 | knockback_resist_node | yetrealm:fire_damage_divisor | 0.1 | ADD_VALUE | 5 | 150 XP |
| healing_received_node | 生生不息 | toughness_node | apothic_attributes:healing_received | 0.04 | ADD_VALUE | 5 | 3 × 中级怪物精华 (yetrealm:intermediate_monster_essence) |
| max_absorption_node | 庇护之躯 | healing_received_node | minecraft:generic.max_absorption | 1.5 | ADD_VALUE | 10 | 4 × 高级怪物精华 (yetrealm:advanced_monster_essence) |
| renewed_armor_node | 生机护体 | max_absorption_node | minecraft:generic.armor | 0.5 | ADD_VALUE | 10 | 1800 XP |
| speed_node | 迅捷步伐 | — | minecraft:generic.movement_speed | 0.003 | ADD_VALUE | 5 | 50 XP |
| speed_percent_node | 疾风步伐 | speed_node | minecraft:generic.movement_speed | 2% | ADD_MULTIPLIED_BASE | 5 | 100 XP |
| step_height_node | 灵动跨越 | jump_strength_node | minecraft:generic.step_height | 0.1 | ADD_VALUE | 10 | 90 XP |
| jump_strength_node | 飞檐走壁 | speed_node | minecraft:generic.jump_strength | 10% | ADD_MULTIPLIED_BASE | 5 | 110 XP |
| speed_boost_node | 风驰电掣 | speed_percent_node | minecraft:generic.movement_speed | 2% | ADD_MULTIPLIED_BASE | 5 | 3 × 初级怪物精华 (yetrealm:primary_monster_essence) |
| speed_mult_node | 御风而行 | speed_boost_node | minecraft:generic.movement_speed | 3% | ADD_MULTIPLIED_BASE | 10 | 2 × 中级怪物精华 (yetrealm:intermediate_monster_essence) |
| swim_speed_node | 如鱼得水 | speed_node | neoforge:swim_speed | 0.04 | ADD_VALUE | 10 | 80 XP |
| swim_speed_mult_node | 海洋眷顾 | swim_speed_node | neoforge:swim_speed | 3% | ADD_MULTIPLIED_BASE | 10 | 170 XP |
| swim_speed_essence_node | 深海眷顾 | swim_speed_mult_node | neoforge:swim_speed | 0.05 | ADD_VALUE | 10 | 5 × 初级怪物精华 (yetrealm:primary_monster_essence) |
| mining_node | 急迫挖掘 | — | minecraft:player.block_break_speed | 0.05 | ADD_VALUE | 5 | 50 XP |
| extra_oxygen_node | 深海之肺 | mining_node | minecraft:generic.oxygen_bonus | 0.1 | ADD_VALUE | 5 | 70 XP |
| max_hunger_node | 饥饿上限 | extra_oxygen_node | yetrealm:max_hunger | 1 | ADD_VALUE | 10 | 3 × 中级怪物精华 (yetrealm:intermediate_monster_essence) |
| consumption_speed_node | 迅捷摄取 | max_hunger_node | yetrealm:eating_speed | 8% | ADD_VALUE | 5 | 400 XP |
| submerged_mining_node | 水下灵工 | mining_speed_percent_node | minecraft:player.submerged_mining_speed | 0.04 | ADD_VALUE | 5 | 100 XP |
| mining_speed_percent_node | 撼地者 | mining_node | minecraft:player.block_break_speed | 5% | ADD_MULTIPLIED_BASE | 10 | 150 XP |
| mining_efficiency_node | 挖掘效率 | submerged_mining_node | minecraft:player.mining_efficiency | 1 | ADD_VALUE | 10 | 1000 XP |
| chest_node | 仓储扩容 | mining_node | — | 机制解锁 | — | 3 | 90 XP |
| pickup_range_node | 磁引回收 | chest_node | yetrealm:pickup_range_bonus | 0.3 | ADD_VALUE | 5 | 180 XP |
| luck_node | 命运眷顾 | — | minecraft:generic.luck | 0.5 | ADD_VALUE | 5 | 250 XP |
| xp_gain_node | 经验汲取 | luck_node | apothic_attributes:experience_gained | 0.05 | ADD_VALUE | 10 | 1000 XP |
| luck_xp_node | 福至心灵 | luck_node | minecraft:generic.luck | 0.25 | ADD_VALUE | 10 | 1200 XP |
| luck_item_node | 寻宝猎人 | luck_node | minecraft:generic.luck | 0.25 | ADD_VALUE | 10 | 10 × 初级怪物精华 (yetrealm:primary_monster_essence) |
| xp_gain_item_node | 智慧凝结 | luck_item_node | apothic_attributes:experience_gained | 0.05 | ADD_VALUE | 10 | 8 × 中级怪物精华 (yetrealm:intermediate_monster_essence) |
| elytra_mastery_node | 羽翼掌控 | speed_mult_node | yetrealm:elytra_speed_bonus | 0.4 | ADD_VALUE | 5 | 3 × 高级怪物精华 (yetrealm:advanced_monster_essence) |
| gravity_reduction_node | 轻若无物 | step_height_node | minecraft:generic.gravity | -4% | ADD_MULTIPLIED_TOTAL | 5 | 2 × 中级怪物精华 (yetrealm:intermediate_monster_essence) |
| extra_jump_node | 凌空再跃 | gravity_reduction_node | yetrealm:jump_count | 1 | ADD_VALUE | 2 | 50 × 初级怪物精华 (yetrealm:primary_monster_essence) |
| life_steal_node | 汲命之刃 | attack_damage_flat_node | apothic_attributes:life_steal | 0.01 | ADD_VALUE | 10 | 3 × 高级怪物精华 (yetrealm:advanced_monster_essence) |
| life_steal_overheal_node | 猩红庇护 | life_steal_node | — | 机制解锁 | — | 10 | 1500 XP |
| life_steal_overheal_attack_damage_node | 猩红锋芒 | life_steal_overheal_node | minecraft:generic.attack_damage | 2.5% | ADD_MULTIPLIED_BASE | 10 | 15 × 初级怪物精华 (yetrealm:primary_monster_essence) |
| arrow_velocity_node | 破空箭势 | crossbow_charge_node | apothic_attributes:arrow_velocity | 0.05 | ADD_VALUE | 10 | 500 XP |
| prot_pierce_node | 裂甲伐锋 | crit_damage_axe_node | apothic_attributes:armor_pierce | 0.75 | ADD_VALUE | 10 | 4 × 中级怪物精华 (yetrealm:intermediate_monster_essence) |
| crit_damage_axe_node | 断首之斧 | entity_reach_node | apothic_attributes:crit_damage | 0.03 | ADD_VALUE | 10 | 2 × 高级怪物精华 (yetrealm:advanced_monster_essence) |


## 构筑建议

- 近战路线优先 `attack_node`、攻速、暴击、命中率和护甲/保护穿透。
- 远程路线优先弓箭伤害、弩上弦速度、投射物伤害和箭速。
- 生存路线优先生命、护甲、韧性、闪避、安全摔落、最大伤害吸收。
- 探索路线优先速度、游泳速度、额外氧气、拾取范围、幸运和经验获取。
