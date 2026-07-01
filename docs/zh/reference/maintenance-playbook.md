# 维护手册

本手册用于把 Yetrealm 模组更新稳定同步到官方 Wiki。目标不是一次写完所有内容，而是让每次版本更新都有固定检查面，避免页面、ID、配方和配置说明互相漂移。

## 维护原则

- **源码优先**：玩家可见文本以 `assets/yetrealm/lang/zh_cn.json` 和 `en_us.json` 为准；注册 ID 以 Java 注册类和 `data/yetrealm/` 为准。
- **玩家路径优先**：攻略页先回答“去哪、带什么、打什么、得到什么”。
- **参考页保留 ID**：图鉴和参考页必须保留 `yetrealm:*` ID，方便搜索、报错排查和数据包覆盖。
- **每次改动可验证**：提交前至少运行内容审计和 `mkdocs build --strict`。

## 版本更新流程

1. 确认版本号和依赖范围：读取 `gradle.properties`、`META-INF/neoforge.mods.toml` 和发布包说明。
2. 同步玩家可见文本：对比 `zh_cn.json` / `en_us.json` 中新增、删除或改名的 key。
3. 同步注册表规模：检查 `ModItems`、`ModBlocks`、`ModEntities`、`ModEffects`、`ModAttributes`。
4. 同步数据包内容：检查 `recipe`、`loot_table`、`worldgen`、`skills/skill_tree.json`、Curios 槽位。
5. 同步机制页：世界难度、Cosmic Cube、HUD/食物、技能树、Boss 召唤和传送门逻辑。
6. 更新首页状态：版本号、核心数量、推荐阅读路径和重要变更入口。
7. 运行本地检查并提交。

## 推荐命令

Windows：

```bat
tools\check_build.bat
```

Linux/macOS：

```bash
./tools/check_build.sh
```

手动分步运行：

```bash
python tools/audit_wiki.py
pip install -r requirements.txt
mkdocs build --strict
```

## 源码到 Wiki 的映射

| Wiki 区域 | 主要源码来源 | 维护重点 |
| --- | --- | --- |
| 入门 | `gradle.properties`、`neoforge.mods.toml` | 版本、依赖、推荐难度 |
| 维度与探索 | `data/yetrealm/worldgen/`、传送门 Java 逻辑 | 入口条件、群系、结构、资源 |
| 系统 | `world/`、`storage/cosmic/`、HUD/配置类 | 规则、默认值、服务器风险 |
| 图鉴 | 注册类、语言文件、纹理资源 | ID、显示名、用途、图标 |
| 攻略 | 进度、Boss 逻辑、掉落表 | 路线顺序、召唤条件、奖励 |
| 参考 | `data/yetrealm/`、配置类 | 配方、掉落、命令、数据包路径 |

## 发布前检查清单

- 首页版本号和线上发布版本一致。
- 所有新增页面已加入 `mkdocs.yml` 的 `nav`。
- 页面中没有 `TODO`、`TBD`、`FIXME` 或省略号占位。
- 图片路径存在，尤其是 HTML `<img src="...">` 使用的本地资源。
- 玩家可见中文没有乱码；PowerShell 显示异常时用 UTF-8 重新读取文件确认。
- `tools/check_build.bat` 或 `tools/check_build.sh` 通过。

## 常见维护决策

| 情况 | 处理方式 |
| --- | --- |
| 新增物品但机制未知 | 先写入图鉴 ID 和显示名，说明来源；不要编造效果。 |
| 玩法数值来自 Java 常量 | 在 Wiki 写具体值，并在提交说明中标出来源类。 |
| 机制还在频繁调整 | 在系统页写当前版本行为，不写承诺式未来路线。 |
| 页面过长 | 拆成玩家攻略页和参考索引页；攻略页讲路线，参考页列数据。 |
| 资源路径改名 | 同步 `docs/assets/` 后运行审计，确认图片没有断链。 |
