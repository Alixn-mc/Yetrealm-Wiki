# 状态效果与属性

## 状态效果

| 效果 | 类型 | 说明 |
| --- | --- | --- |
| <img class="yr-icon" src="../../assets/yetrealm/textures/mob_effect/freeze.png" alt="">**冻结**<br><span class="yr-id">yetrealm:freeze</span> | 状态效果 | 由武器、Boss、环境或技能触发 |
| <img class="yr-icon" src="../../assets/yetrealm/textures/mob_effect/confusion.png" alt="">**混乱**<br><span class="yr-id">yetrealm:confusion</span> | 状态效果 | 由武器、Boss、环境或技能触发 |
| <img class="yr-icon" src="../../assets/yetrealm/textures/mob_effect/blindness.png" alt="">**失明**<br><span class="yr-id">yetrealm:blindness</span> | 状态效果 | 由武器、Boss、环境或技能触发 |
| <img class="yr-icon" src="../../assets/yetrealm/textures/mob_effect/bleeding.png" alt="">**出血**<br><span class="yr-id">yetrealm:bleeding</span> | 状态效果 | 由武器、Boss、环境或技能触发 |
| <img class="yr-icon" src="../../assets/yetrealm/textures/mob_effect/radiation.png" alt="">**辐射**<br><span class="yr-id">yetrealm:radiation</span> | 状态效果 | 由武器、Boss、环境或技能触发 |
| <img class="yr-icon" src="../../assets/yetrealm/textures/mob_effect/flare.png" alt="">**耀斑**<br><span class="yr-id">yetrealm:flare</span> | 状态效果 | 由武器、Boss、环境或技能触发 |
| <img class="yr-icon" src="../../assets/yetrealm/textures/mob_effect/well_fed.png" alt="">**吃饱喝足**<br><span class="yr-id">yetrealm:well_fed</span> | 状态效果 | 由武器、Boss、环境或技能触发 |


## Yetrealm 属性

| 属性 | 默认 | 最小 | 最大 |
| --- | --- | --- | --- |
| **冻结进度**<br><span class="yr-id">yetrealm:is_frozen</span> | 0.0D | 0.0D | 1.0D |
| **freeze_immunity_ticks**<br><span class="yr-id">yetrealm:freeze_immunity_ticks</span> | 0.0D | 0.0D | 72000.0D |
| **鞘翅飞行速度**<br><span class="yr-id">yetrealm:elytra_speed_bonus</span> | 0.0D | 0.0D | 10.0D |
| **范围吸取加成**<br><span class="yr-id">yetrealm:pickup_range_bonus</span> | 0.0D | 0.0D | 64.0D |
| **命中率**<br><span class="yr-id">yetrealm:hit_rate</span> | 0.0D | -10.0D | 10.0D |
| **饥饿消耗倍率**<br><span class="yr-id">yetrealm:hunger_consumption_multiplier</span> | 1.0D | 0.0D | 64.0D |
| **食用速度**<br><span class="yr-id">yetrealm:eating_speed</span> | 1.0D | 0.05D | 64.0D |
| **饥饿上限**<br><span class="yr-id">yetrealm:max_hunger</span> | 20.0D | 20.0D | 200.0D |
| **跳跃次数**<br><span class="yr-id">yetrealm:jump_count</span> | 1.0D | 1.0D | 64.0D |
| **伤害免疫**<br><span class="yr-id">yetrealm:damage_immunity</span> | 0.0D | 0.0D | 1024.0D |
| **火焰伤害抗性**<br><span class="yr-id">yetrealm:fire_damage_divisor</span> | 1.0D | 1.0D | 1024.0D |
| **自然生命恢复**<br><span class="yr-id">yetrealm:natural_health_regeneration</span> | 0.0D | 0.0D | 1024.0D |
| **生物刷新速率**<br><span class="yr-id">yetrealm:spawn_multiplier</span> | 1.0D | 0.05D | 1024.0D |


## 战斗规则要点

- 伤害可被防御时，会先减去 `护甲韧性 × 0.25`。
- 玩家闪避率有效上限为 80%。
- 过量治疗生成的护盾只按最大伤害吸收属性封顶。
- 神化火焰伤害与冰霜伤害可作用于投射物远程命中。
- 饥饿值大于 70% 时会触发慢速自然回血。
