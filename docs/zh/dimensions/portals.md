# 传送门与星界信标

Yetrealm 有两条主要跨维度通道：**远古之门** 和 **星界信标门**。两者都由源码中的专门逻辑保护和校验，而不是简单的方块拼接。

## 远古之门：Ancient Soul → Ancient Universe

| 条件 | 说明 |
| --- | --- |
| 使用物品 | <img class="yr-icon" src="../../assets/yetrealm/textures/item/ancient_soul.png" alt="">**◆ 远古灵魂 ◆**<br><span class="yr-id">yetrealm:ancient_soul</span> |
| 使用地点 | 主世界 Ancient City 中央传送门遗迹 |
| 目标方块 | 强化深板岩（`minecraft:reinforced_deepslate`） |
| 目标维度 | `yetrealm:ancient_universe` |
| 关键限制 | 必须在主世界，且需要识别到 Ancient City 门形遗迹 |

步骤：

1. 在主世界找到 Ancient City。
2. 前往中央门形遗迹。
3. 手持 `Ancient Soul` 对中央强化深板岩使用。
4. 传送门管理器会创建/修复主世界与 Ancient Universe 的成对门。

## 星界之门：Astral Keystone → Astral Realm

| 条件 | 说明 |
| --- | --- |
| 使用物品 | <img class="yr-icon" src="../../assets/yetrealm/textures/item/astral_keystone.png" alt="">**✦ 星源棱晶 ✦**<br><span class="yr-id">yetrealm:astral_keystone</span> |
| 目标方块 | Beacon / 信标 |
| 层数要求 | 五层基座：比原版满级信标多一层 |
| 维度限制 | 主世界激活 |
| 传送门位置 | 以信标为中心，约 40 格上方生成 |
| 传送门大小 | 半径约 10 的星界门 |
| Beacon 效果 | 继承并保留原 Beacon 的有效效果、名称和锁定数据 |

!!! note "五层信标"
    原版信标满级为四层。Astral Beacon 要求五层，源码常量名为 `REQUIRED_ASTRAL_BEACON_LEVELS = 5`。如果结构、天空或传送门空间不满足要求，星界信标会被判定为无效并尝试还原。

## 星界信标效果

激活后的 Astral Beacon 会以较大范围维持 Beacon 效果。源码中可见效果范围为 50，持续时间为 30 分钟。传送门生成在上方空域，玩家需要准备上升/飞行/搭建手段。

## 黑洞返回

星界存在返回主世界的黑洞机制，并对应进度“黑洞归来”。从设计上看，它是 Astral Realm 的返航通道，也是进入 Plasma 时代前的重要节点。
