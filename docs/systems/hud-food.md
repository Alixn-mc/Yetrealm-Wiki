# HUD、食物与经验

Yetrealm 改动了玩家 HUD、食物提示、饥饿上限、跳跃手感、铁砧和经验消耗。`Mechanics Guide` 是游戏内最重要的规则速查书。

## 客户端 HUD

| 配置键 | 默认 | 说明 |
| --- | --- | --- |
| healthHudStyleMode | CUSTOM_A | 生命 HUD 样式；VANILLA 使用原版覆盖层。 |
| hungerHudStyleMode | CUSTOM_A | 饥饿 HUD 样式；VANILLA 使用原版覆盖层。 |
| armorHudStyleMode | CUSTOM_A | 护甲 HUD 样式；VANILLA 使用原版覆盖层。 |
| foodNutritionTooltipEnabled | true | 食物提示显示 Yetrealm 饥饿与饱和条。 |
| extraJumpHudEnabled | true | 显示额外跳跃剩余次数 HUD。 |
| experienceValueHudEnabled | true | 在经验条旁显示玩家总经验值。 |
| jumpFeelOptimizationsEnabled | true | 启用高移速下的跳跃手感优化。 |


## 永久成长食物

| 物品 | 效果 |
| --- | --- |
| <img class="yr-icon" src="../../assets/yetrealm/textures/item/life_fruit.png" alt="">**生命果**<br><span class="yr-id">yetrealm:life_fruit</span> | 提高生命值上限2点，最多5次 |
| <img class="yr-icon" src="../../assets/yetrealm/textures/item/decayed_flesh.png" alt="">**枯朽肉**<br><span class="yr-id">yetrealm:decayed_flesh</span> | 永久提高饥饿值上限4点，最多5次 |
| <img class="yr-icon" src="../../assets/yetrealm/textures/block/lucky_clover.png" alt="">**金色四叶草**<br><span class="yr-id">yetrealm:lucky_clover</span> | 小概率生成在主世界的地表，大量分布与远古的空岛中，食用永久增加幸运<br>使用上限：3 次（每次幸运 +1） |
| <img class="yr-icon" src="../../assets/yetrealm/textures/item/evil_apple.png" alt="">**邪念苹果**<br><span class="yr-id">yetrealm:evil_apple</span> | 永久使自然精英刷新概率提高 15%<br>三级精英苏醒时间由世界难度或自定义设置决定；硬核模式开局启用 |
| <img class="yr-icon" src="../../assets/yetrealm/textures/item/ancient_tree_fruit.png" alt="">**古木果**<br><span class="yr-id">yetrealm:ancient_tree_fruit</span> | 食用后清除所有负面效果。 |


## Mechanics Guide 摘要

| 条目 |
| --- |
| 1. 幸运值现在增加吃时运方块与生物的额外掉落尝试，并提升经验倍率 |
| 2. 若伤害可被防御，会先减去(护甲韧性*0.25) |
| 3. 溢出的暴击率造成更多伤害（详见神化属性） |
| 4. 原版跳劈固定造成1.5倍伤害，不受暴击伤害加成 |
| 5. 伤害免疫会在最终伤害结算后直接扣减； |
| 若扣减后小于等于0，则本次伤害完全无效 |
| 6. 玩家闪避率的有效上限为80% |
| 7. 过量治疗生成的护盾最多堆到最大伤害吸收值 |
| 只按最大伤害吸收属性封顶，不再额外受最大生命值一半限制 |
| 8. 神化火焰伤害与冰霜伤害也会作用于投射物远程命中 |
| 适用于标记为投射物伤害、且能解析到发射者的弓、弩、三叉戟等远程武器 |
| 9. 优化了高移速下的跳跃手感 |
| 移速越高衰减越接近消失；飞行、鞘翅、骑乘、水中和攀爬状态不会触发 |
| 10. 铁砧取消40级过于昂贵限制 |
| 铁砧与附魔台消耗原始经验点 |
| 11. 饥饿值大于70%时会触发慢速自然回血 |
