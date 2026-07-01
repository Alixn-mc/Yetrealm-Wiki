# Maintenance Playbook

Use this checklist when syncing a Yetrealm mod update into the official wiki.

## Principles

- Source first: visible text comes from `zh_cn.json` and `en_us.json`; IDs come from registration code and `data/yetrealm/`.
- Player route first: guide pages should answer where to go, what to bring, what to fight, and what reward matters.
- Keep IDs visible: catalog and reference pages should retain `yetrealm:*` identifiers.
- Verify each update: run the audit and `mkdocs build --strict` before publishing.

## Update Flow

1. Confirm version and dependency ranges.
2. Compare language files for renamed or added player-facing text.
3. Check item, block, entity, effect, and attribute registrations.
4. Check recipes, loot tables, worldgen, skills, and Curios tags.
5. Update systems pages for world difficulty, Cosmic Cube, HUD, food, Skill Tree, bosses, and portals.
6. Update the homepage status and recommended route.
7. Run local validation and commit.

