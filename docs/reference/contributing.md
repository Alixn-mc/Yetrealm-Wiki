# 贡献与维护

## 页面风格

- 玩家攻略优先回答“去哪、带什么、打什么、得到什么”。
- 图鉴页面保留 ID，方便玩家、服主和整合包作者搜索。
- 参考页面面向维护者：配方、掉落、配置项、数据包路径必须准确。
- 新机制首次出现时使用提示框，但不要在每页重复长篇背景。

## 版本更新清单

每次 Yetrealm 更新后建议按以下顺序同步 Wiki：

1. `neoforge.mods.toml`：版本、依赖、描述。
2. `assets/yetrealm/lang/*.json`：显示名、提示、进度文本。
3. `ModItems` / `ModBlocks` / `ModEntities` / `ModEffects` / `ModAttributes`：注册表。
4. `data/yetrealm/recipe` 与 `loot_table`：配方和掉落。
5. `data/yetrealm/worldgen`：群系、结构、维度。
6. `data/yetrealm/skills/skill_tree.json`：技能树节点。
7. `Config` / `ServerConfig` / `ClientConfig` / 世界难度类：配置和规则。

## 本地校验

```bash
pip install -r requirements.txt
mkdocs build --strict
```

如果新增页面，请同步 `mkdocs.yml` 的 `nav`。如果移动资源路径，请检查所有图片相对路径。
