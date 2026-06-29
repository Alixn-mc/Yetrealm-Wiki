# 配置项

Yetrealm 使用 Common、Server 与 Client 三类配置。世界难度和 Curios 槽位还会在创建世界时保存到世界数据中。

## Common Config

| 键 | 默认 | 范围 | 说明 |
| --- | --- | --- | --- |
| basePlayerMaxHunger | 20 | 20–200 | 玩家基础最大饥饿值；原版满饥饿为 20。 |
| cosmicCube.externalContainerTransferEnabled | false | 布尔 | 允许 Cosmic Cube 与外部方块库存转移物品。 |
| cosmicCube.allowLegacyContainerFallback | false | 布尔 | 允许在无 NeoForge item handler 能力时访问原版 Container；公共服慎用。 |
| cosmicCube.unpackNestedContainers | false | 布尔 | 允许拆解嵌套容器内容；默认关闭以避免意外改变潜影盒/背包内容。 |
| cosmicCube.maxSharedSpacesPerPlayer | 8 | 0–128 | 每名玩家可拥有的共享空间数量上限。 |
| cosmicCube.maxSharedSpaceNameLength | 32 | 1–64 | 共享空间显示名长度上限。 |


## Server Config

| 键 | 默认 | 范围 | 说明 |
| --- | --- | --- | --- |
| cosmicCube.maxVariantsPerItem | 0 | 0–1,000,000 | 单个空间中同一 item id 的组件/NBT 变体数量上限；0 表示不限。 |


## Client Config

| 键 | 默认 | 说明 |
| --- | --- | --- |
| healthHudStyleMode | CUSTOM_A | 生命 HUD 样式；VANILLA 使用原版覆盖层。 |
| hungerHudStyleMode | CUSTOM_A | 饥饿 HUD 样式；VANILLA 使用原版覆盖层。 |
| armorHudStyleMode | CUSTOM_A | 护甲 HUD 样式；VANILLA 使用原版覆盖层。 |
| foodNutritionTooltipEnabled | true | 是否在食物提示中显示 Yetrealm 饥饿和饱和条。 |
| extraJumpHudEnabled | true | 是否显示额外跳跃次数 HUD。 |
| experienceValueHudEnabled | true | 是否显示总经验值。 |
| jumpFeelOptimizationsEnabled | true | 是否启用高移速下的跳跃手感优化。 |
| lastWorldCreationMode | VANILLA | 记录上次创建世界时选择的 Yetrealm 世界难度。 |


## 世界创建自定义项

参见 [世界难度](../systems/world-difficulty.md)。这些值会写入世界数据，而不是单纯的客户端偏好。
