# Installation and Dependencies

## Version Matrix

| Dependency | Type | Version range | Notes |
| --- | --- | --- | --- |
| Minecraft | required | `[1.21.1, 1.21.2)` | Client and server |
| NeoForge | required | `[21.1.234, 21.2)` | Loader |
| Curios API | required | `[9.5.1, )` | Curios slots and equipment logic |
| Apothic Attributes | required | `[2.9.1, )` | Extended combat and attribute scaling |
| GeckoLib | required | `[4.8.3, )` | Animated entities and renderers |
| Apothic Enchanting | optional | `[1.0.0, )` | Enchanting ecosystem compatibility |

!!! warning "Version lock"
    Yetrealm currently targets **Minecraft 1.21.1** and the **NeoForge 21.1.x** line. Cross-version use should be treated as unsupported until worldgen, Curios, Apothic Attributes, and datapack resources are tested again.

## Client Install

1. Install NeoForge for Minecraft 1.21.1.
2. Put Yetrealm and all required dependencies into `mods/`.
3. Start the game once and confirm Yetrealm, Curios, Apothic Attributes, and GeckoLib are loaded.
4. Pick a Yetrealm world mode when creating a world. Modpacks should document the chosen mode before release.

## Server Install

- The server and clients must use the same Yetrealm version and required dependency set.
- For public servers, review [Cosmic Cube](../systems/cosmic-cube.md) and [Config](../reference/config.md) before launch.
- Dimensions, structures, recipes, loot tables, tags, and skills use datapack-style resources. Modpacks can override them, but key IDs should remain compatible.

## Short Modpack Description

```text
Yetrealm adds two progression dimensions, late-game bosses, Curios accessories,
a configurable world difficulty layer, a Skill Tree, and long-term storage.
Recommended world mode: Challenge for normal packs, Cursed/Hardcore Cursed for expert packs.
```

