# Cosmic Cube

`Cosmic Cube` 是 Yetrealm 的长期存储终端。右键或按 Cosmic Cube 快捷键可打开无限空间终端；自动模式可在关闭、吸入、补货和全自动之间循环。

## 基本行为

| 物品 | 说明 |
| --- | --- |
| **宇宙魔方**<br><span class="yr-id">yetrealm:cosmic_cube</span> | 右键或按宇宙魔方快捷键打开无限空间终端。<br>自动模式：关闭 / 吸入 / 补货 / 全自动<br>自动吸入：开启或关闭；全自动还会启用补货逻辑 |

## 自动模式

| 模式 | 行为 |
| --- | --- |
| 关闭 | 关闭随身自动吸入和自动补货。 |
| 吸入 | 收主背包中已存在、自动收或销毁规则匹配的物品；不处理快捷栏和鼠标物品。 |
| 补货 | 从魔方补满背包/副手已有堆叠；潜行右键容器会补满容器。 |
| 全自动 | 同时收主背包并补货；潜行右键容器会转入内容并展开盒中物。 |


## 与背包的区别

`Simple Backpack` 是个人存储访问钥匙，内容绑定玩家本人，不绑定具体物品；多个简易背包不会创建多个独立空间。Cosmic Cube 则面向更长期、更高容量的物品空间与共享空间。

## 服务器安全配置

| 配置键 | 默认 | 范围 | 说明 |
| --- | --- | --- | --- |
| cosmicCube.externalContainerTransferEnabled | false | true/false | 允许 Cosmic Cube 通过潜行使用容器与外部方块库存转移物品。 |
| cosmicCube.allowLegacyContainerFallback | false | true/false | 当方块没有暴露 NeoForge 物品处理能力时，允许直接访问原版 Container。公共服建议保持关闭。 |
| cosmicCube.unpackNestedContainers | false | true/false | 允许拆解单堆叠嵌套容器中的 DataComponents.CONTAINER 内容。默认关闭以避免潜影盒/背包内容意外变化。 |
| cosmicCube.maxSharedSpacesPerPlayer | 8 | 0–128 | 每名玩家可拥有的共享空间数量上限。 |
| cosmicCube.maxSharedSpaceNameLength | 32 | 1–64 | 共享空间显示名长度上限。 |
| cosmicCube.maxVariantsPerItem | 0 | 0–1,000,000 | 单个 Cosmic Cube 空间中同一 item id 可存储的组件/NBT 变体数量；0 表示不限。 |


!!! warning "公共服建议"
    除非确认领地/权限/容器保护模组覆盖相同访问路径，否则不要开启 legacy container fallback。高并发服务器还应考虑设置 `maxVariantsPerItem`，避免玩家用大量 NBT 变体制造存储压力。
