# 命令

源码中命令位于 `src/devCommands`，通常用于开发、调试和结构制作。是否在发布包中可用取决于构建配置；玩家服不应默认开放。

| 命令 | 用途 |
| --- | --- |
| /yetrealm_find_abyss | 玩家调试命令：寻找/传送最近深渊。 |
| /yetrealm_give_abyss_map | 给予深渊藏宝图。 |
| /yetrealm_find_volcano | 寻找/传送最近火山。 |
| /yetrealm_find_astral_site [target] [cellRadius] | 查找附近星界地点：any / stargazer / black_hole。 |
| /yetrealm_release_frost_aurora_core | 触发/测试 Frost Aurora Core 效果。 |
| /yetrealm_summon_elite <entity> [variant] | 召唤指定实体的精英变体。 |
| /yetrealm_enchant_inventory | 调试：为背包物品附魔。 |
| /yetrealm_max_beacon | 调试：在玩家旁生成星界门测试信标。 |
| /yetrealm_debug_ice_queen_shield <level> [durationTicks] | 调试 Ice Queen 护盾阶段。 |
| /yetrealm_debug_ice_queen_counter ready\|burst [durationTicks] | 调试 Ice Queen 反击。 |
| /yetrealm_debug_stargazer_skill <skill> [durationTicks] | 调试 Stargazer 技能。 |
| /yetrealm_structure list/place/info/save | 可编辑结构工具命令。 |
| /yetrealm_structure_debug on\|off\|once\|radius\|status | 结构调试可视化。 |


!!! warning "权限与环境"
    这些命令应视为开发/调试工具。公共服务器启用前请确认权限等级、构建源集和反作弊/领地保护兼容性。
