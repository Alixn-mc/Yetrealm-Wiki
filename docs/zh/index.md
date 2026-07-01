<div class="yr-hero">
  <h1>Yetrealm 官方 Wiki</h1>
  <p>Yetrealm 将 Minecraft 1.21.1 扩展为以远古宇宙、星界虚空、Boss 追猎、Curios 饰品、长线技能树和世界难度为核心的生存向模组。本 Wiki 是官方长期维护入口：玩家查路线，服主查规则，整合包作者查数据，维护者按源码同步更新。</p>
  <div class="yr-badges">
    <span class="yr-badge">Yetrealm 1.0.1</span>
    <span class="yr-badge">Minecraft 1.21.1</span>
    <span class="yr-badge">NeoForge 21.1.x</span>
    <span class="yr-badge">193 个注册物品</span>
    <span class="yr-badge">27 个方块</span>
    <span class="yr-badge">18 个生物 / Boss</span>
    <span class="yr-badge">61 个技能节点</span>
  </div>
</div>

## 站点入口

<div class="yr-card-grid">
  <div class="yr-card"><h3>从零开始</h3><p>安装依赖、选择世界难度，并沿着古城 → Ancient Universe → Astral Realm 的主路线推进。</p><p><a href="getting-started/progression/">查看生存路线 →</a></p></div>
  <div class="yr-card"><h3>维度与传送门</h3><p>远古之门使用 Ancient Soul 激活；星界之门由五层星界信标在高空生成。</p><p><a href="dimensions/portals/">查看传送门 →</a></p></div>
  <div class="yr-card"><h3>装备与饰品</h3><p>陨铁、青铜、太古合金、等离子四条装备阶梯与 Curios 饰品共同构成终局强度。</p><p><a href="catalog/equipment/">查看装备 →</a></p></div>
  <div class="yr-card"><h3>整合包与服务器</h3><p>世界难度、硬核规则、Curios 槽位、Cosmic Cube 安全选项均可配置。</p><p><a href="reference/config/">查看配置 →</a></p></div>
</div>

## 角色入口

| 你是谁 | 先看 | 然后看 |
| --- | --- | --- |
| 新玩家 | [安装与依赖](getting-started/installation.md) | [生存开局路线](getting-started/progression.md)、[Boss 战](guides/bosses.md) |
| 服主 / 整合包作者 | [世界难度](systems/world-difficulty.md) | [配置项](reference/config.md)、[ID 与数据包](reference/ids-datapacks.md) |
| Wiki 维护者 | [维护手册](reference/maintenance-playbook.md) | [页面模板](reference/page-templates.md)、[贡献与维护](reference/contributing.md) |

## 推荐阅读顺序

1. **安装与依赖**：确认 NeoForge、Curios、Apothic Attributes、GeckoLib 与版本范围。
2. **世界难度**：开新世界时选择 Easy / Vanilla / Challenge / Cursed / Hardcore Cursed / Custom。
3. **生存开局路线**：先定位 Ancient City，取得 Ancient Soul，进入 Ancient Universe。
4. **Boss 与资源路线**：以 Ice Queen、Ancient Dragon、Stargazer 为主要里程碑。
5. **参考索引**：查配方、掉落、进度、ID、配置项和命令。

!!! tip "玩家向一句话路线"
    Ancient City 中央强化深板岩 + Ancient Soul → Ancient Universe → 陨铁/青铜 → Ice Queen → Ancient Dragon → Primordial Alloy → Astral Keystone + 五层 Beacon → Astral Realm → Stargazer → Star Abyss Core → Cosmic Cube / 等离子终局。

!!! note "维护状态"
    站点通过 GitHub Actions 自动部署。每次修改 Wiki 后，本地先运行 `tools/check_build.bat` 或 `tools/check_build.sh`，再提交到 `main`；线上站点会自动更新。
