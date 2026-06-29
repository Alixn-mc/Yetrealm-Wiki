# 安装与依赖

## 版本矩阵

| 依赖 | 类型 | 版本范围 | 说明 |
| --- | --- | --- | --- |
| Minecraft | required | [1.21.1, 1.21.2) | 客户端与服务端 |
| NeoForge | required | [21.1.234, 21.2) | 加载器 |
| Curios API | required | [9.5.1, ) | 饰品槽位与装备逻辑 |
| Apothic Attributes | required | [2.9.1, ) | 扩展属性与战斗数值 |
| GeckoLib | required | [4.8.3, ) | 动画实体与渲染 |
| Apothic Enchanting | optional | [1.0.0, ) | 兼容附魔生态 |


!!! warning "版本锁定"
    源码的 `neoforge.mods.toml` 将 Minecraft 锁定在 **1.21.1**，NeoForge 锁定在 **21.1.x**。跨 MC 大版本通常需要重新测试世界生成、Curios、Apothic Attributes 和数据包资源。

## 客户端安装

1. 安装 Minecraft 1.21.1 对应的 NeoForge。
2. 将 Yetrealm 与必需依赖放入 `mods/`。
3. 第一次进入游戏后检查主菜单/模组列表，确保 Curios、Apothic Attributes 与 GeckoLib 均已加载。
4. 创建世界时选择 Yetrealm 世界难度；整合包建议预先决定难度并写入服务端规则说明。

## 服务端安装

- 服务端与客户端必须使用同一 Yetrealm 版本和同一组必需依赖。
- 若开放公共服务器，建议优先查看 [Cosmic Cube](../systems/cosmic-cube.md) 和 [配置项](../reference/config.md) 中的安全说明。
- 维度、结构、配方、战利品和标签均使用数据包格式，整合包可以通过 datapack 覆盖，但必须保留关键 ID 的兼容性。

## 推荐整合包说明

```text
Yetrealm adds two progression dimensions, late-game bosses, Curios accessories,
a configurable world difficulty layer, a skill tree, and long-term storage.
Recommended world mode: Challenge for normal packs, Cursed/Hardcore Cursed for expert packs.
```
