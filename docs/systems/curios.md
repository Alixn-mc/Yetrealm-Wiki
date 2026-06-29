# Curios 饰品位

Yetrealm 依赖 Curios，并在世界创建/Custom 难度中配置额外槽位。默认槽位非常宽松，鼓励玩家围绕戒指、护符、项链、背部与足部构筑。

## 默认额外槽位

| 槽位 ID | 槽位 | 默认新增数量 |
| --- | --- | --- |
| curio | 通用 | 0 |
| head | 头饰 | 2 |
| back | 背部 | 2 |
| bracelet | 手镯 | 2 |
| body | 身体 | 2 |
| ring | 戒指 | 10 |
| necklace | 项链 | 2 |
| charm | 护符 | 5 |
| belt | 腰带 | 2 |
| hands | 手部 | 2 |
| feet | 足部 | 2 |


## 互斥与唯一限制

语言文件中定义了多组互斥提示：

- `[唯一]`：同一类或同一件饰品只能装备一件。
- 自定义靴、磁力戒指、挖矿/冶矿戒指、翅膀、战争戒指均有互斥组。
- 这类限制能阻止同系列效果过度叠加，但不同槽位之间仍能形成强力组合。

## 代表构筑

| 构筑 | 推荐槽位/物品 | 思路 |
| --- | --- | --- |
| 开荒探索 | Rabbit Foot Boots、Night Vision Goggles、Lucky/基础戒指 | 增加跳跃、视野和基础幸运 |
| 远古宇宙战斗 | Abyss Rending Claw、Dragon Ring、Warding Amulet、Frost Aurora Core | 盔甲穿透、反制 Reaper、抗爆发 |
| 星界机动 | Meteorite Wings / Starflow Wings、Enchanted/Lava Firework Rocket | 提高鞘翅飞行速度和移动生存能力 |
| 采矿与收集 | Mining Ring、Ore Smelting Ring、Magnet Ring、Simple Backpack | 范围吸取、自动冶炼、个人背包 |

!!! note "槽位数量是世界配置"
    Custom 世界可以为每类 Curios 槽位设置 0–100。公共服务器应在开服前确定槽位数量，避免玩家构筑因后续修改大幅变化。
