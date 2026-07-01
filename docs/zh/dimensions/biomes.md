# 群系与世界生成

Yetrealm 的数据包资源在 `data/yetrealm/worldgen/` 下定义群系、特征、放置规则、结构与维度生成。以下表格按当前源码中的群系 JSON 生成。

| 群系 ID | 显示名 | 维度 |
| --- | --- | --- |
| ancient_highlands | 远古高山 | Ancient Universe |
| ancient_ocean | 远古海洋 | Ancient Universe |
| ancient_wasteland | 远古荒地 | Ancient Universe |
| ashen_caldera | 灰烬火山口 | Ancient Universe |
| astral_void | 星界虚空 | Astral Realm |
| frozen_reaches | 凛冬古原 | Ancient Universe |
| gloom_darklands | 幽暗之地 | Ancient Universe |
| petrified_flats | 硅化荒原 | Ancient Universe |
| primordial_grove | 远古林地 | Ancient Universe |
| primordial_rainforest | 巨木森林 | Ancient Universe |


## 生成层次

- **Ancient Universe**：使用自定义多噪声/火山口式 biome source，混合高地、荒地、远古海洋、火山、冰原、幽暗地带、石化荒原和原始森林。
- **Astral Realm**：使用固定 `astral_void` 群系和空域式噪声设置，重点是结构、黑洞与星界敌人。
- **结构资源**：源码包含 `ancient_generated_portal`、`ancient_stone_house_ruins`、`ice_snow_castle` 等可编辑结构，以及多类洞穴补给、深渊宝藏、龙巢宝藏和星界结构宝藏战利品表。

## 生态与刷怪概览

| 生态组 | 数据标签 / 区域 | 代表生物 |
| --- | --- | --- |
| 远古森林动物 | #yetrealm:ancient_universe_forest_biomes | Deinotherium、Megaloceros、Rabbit、Armadillo、Donkey |
| 远古陆地敌对 | #yetrealm:ancient_universe_land_biomes | Ash Beast、Cave Goblin、Ancient Ogre |
| 远古海洋/深渊 | Ancient Ocean / Abyssal ocean features | Trilobite Brute、Ammonite Behemoth、Mosasaur、Dunkleosteus、Anglerfish |
| 星界 | Astral Void / astral structures | Astral Worm、Photon Watcher、Starflare Sentinel、Stargazer |


## 整合包调校建议

若整合包会同时加入其他大型世界生成模组，建议重点测试：

- Ancient City 中央门形结构是否仍可被识别；
- Ancient Universe 是否能稳定生成深渊/火山/冰雪城堡/龙巢类目标；
- Astral Realm 高空门、黑洞返回与结构定位是否可用；
- 敌对生物生成权重是否与其他模组冲突。
