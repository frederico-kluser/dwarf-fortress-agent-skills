# Armor token

> Fonte: [Armor token](https://dwarffortresswiki.org/index.php/Armor_token) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

\

The tokens for all types of armor on all slots, including shields. Usage column gives information on what types of **armor** the token might be restricted to.

These tokens can only be placed within an ITEM_ARMOR, ITEM_GLOVES, ITEM_SHOES, ITEM_SHIELD, ITEM_HELM, or ITEM_PANTS object definition, most do not function in weapon objects.

## Tokens

|  |  |  |  |
|----|----|----|----|
| Token | Arguments | Usage | Description |
|  NAME | singular:plural | Required | What this item will be called in-game. |
|  ADJECTIVE | adjective | All garments and shields | Appears before the name of the garment's material. E.g. "long cow leather skirt" |
|  MATERIAL_SIZE | value | Required | How much material is needed to make the item. Most important with bars. The number of bars required to make the item is the value divided by three. |
|  ARMORLEVEL | 0 - clothing / 1 - ranged / 2 - melee / 3 - uniform only | All garments and shields | Determines the garment's general purpose. Defaults to 1 for shields, 0 for everything else. / \[ / ARMORLEVEL / :0\] / items are claimed and used by civilians as ordinary / clothing / and are subject to / wear / . / Ranged fighters will spawn with a set of / \[ / ARMORLEVEL / :1\] / gear, while melee fighters use / \[ / ARMORLEVEL / :2\] / . / \[ / ARMORLEVEL / :3\] / helmets and body armor only spawn as part of a / civilization / 's uniform. / Each instance of a civilization chooses a helmet and armor at random, from among non-clothing items they have access to, as their uniform. All soldiers that generate as part of that civilization will use those pieces, and if possible, will layer it with a second piece suitable for their / unit type / . / In previous versions, the armor levels were known as leather, chain, and plate, respectively. |
|  METAL_ARMOR_LEVELS |  | All garments | Metal versions of this item count as one [`[ARMORLEVEL]`](/index.php/Armor_token#ARMORLEVEL "Armor token") higher, typically used to exclude it from civilians. This tag will not work unless [`[ARMORLEVEL]`](/index.php/Armor_token#ARMORLEVEL "Armor token") is explicitly declared: if you leave out [`[ARMORLEVEL]`](/index.php/Armor_token#ARMORLEVEL "Armor token"), even metal armor will default to level 0. |
|  CHAIN_METAL_TEXT |  | All garments | Metal versions of this item will have "chain" added between the material and item name. |
|  PREPLURAL | of | ITEM_ARMOR / ITEM_PANTS | Changes the plural form of this item to " item". Primarily pertains to the stock screens. Example, "suits of" platemail, "pairs of" trousers, etc. |
|  MATERIAL_PLACEHOLDER | adjective | ITEM_ARMOR / ITEM_PANTS | If the item has no material associated with it (e.g. stockpile menus and trade negotiations), this will be displayed in its place. Used for leather armor. |
|  VALUE | value |  | Defines the item value of the armor. Defaults to 10. |
|  UPSTEP | value, MAX | ITEM_GLOVES / ITEM_SHOES / ITEM_SHIELD | Length of gloves or footwear, counted in \[LIMB\] body parts towards the torso. A value of 1 lets gloves cover the lower arms, a value of 2 stretches a boot all the way over the upper leg and so on. Regardless of the value, none of these items can ever extend to cover the upper or lower body. Shields also have this token, but it only seems to affect weight. |
|  UBSTEP | value, MAX | ITEM_ARMOR | Length of the sleeves, counted in \[LIMB\] body parts towards the hands. A value of 0 only protects both halves of the torso, 1 extends over the upper arms and so on. Regardless of the value, body armor can never extend to cover the hands or head. / Currently bugged / Bug / : / 1821 / , high values of UBSTEP will result in the item protecting facial features, fingers, and toes, while leaving those parts that it cannot protect unprotected (but still counting them as steps). |
|  LBSTEP | value or MAX | ITEM_ARMOR / ITEM_PANTS | Length of the legs/hem, counted in \[LIMB\] body parts towards the feet. A value of 0 only covers the lower body, 1 extends over the upper legs and so on. Regardless of the value, body armor or pants can never extend to cover the feet. |
|  BLOCKCHANCE | value | ITEM_SHIELD | Affects the block chance of the shield. Defaults to 10. |
|  SOFT |  | All garments | Clothiers can make this item from all kinds of cloth. If paired with \[LEATHER\], the item has an equal chance of being either in randomly generated outfits. Further uses of this tag are unknown. |
|  HARD |  | All garments | Default state in the absence of a \[SOFT\] token. Actual effects unknown. |
|  METAL |  | All garments | Item can be made from metal. Overrides \[SOFT\] and \[LEATHER\] in randomly generated outfits, if the ARMORLEVEL permits. Civilizations with [\[WOOD_ARMOR\]](/index.php/Entity_token#WOOD_ARMOR "Entity token") will make this item out of wood instead. |
|  BARRED |  | All garments | Craftsmen can make this item from bones. Randomly generated outfits don't include bone armor. |
|  SCALED |  | All garments | Craftsmen can make this item from shells. Randomly generated outfits don't include shell armor. |
|  LEATHER |  | All garments | Leatherworkers can make this item from leather. If paired with \[SOFT\], this item has an equal chance of being either in randomly generated outfits. |
|  SHAPED |  | All garments | Only one shaped piece of clothing can be worn on a single body slot at a time. |
|  STRUCTURAL_ELASTICITY_CHAIN_ALL |  | All garments | Increases the \*\_STRAIN_AT_YIELD properties of the armor's material to 50000, if lower. This makes the garment flex and give way instead of shattering under force. Strong materials that resist cutting will blunt edged attacks into bone-crushing hits instead. |
|  STRUCTURAL_ELASTICITY_CHAIN_METAL |  | All garments | Increases the \*\_STRAIN_AT_YIELD properties of the armor's material to 50000, but only if the garment is made from metal. |
|  STRUCTURAL_ELASTICITY_WOVEN_THREAD |  | All garments | Reduces the armor material's SHEAR_YIELD to 20000, SHEAR_FRACTURE to 30000 and increases the \*\_STRAIN_AT_YIELD properties to 50000, but only if the garment is made from cloth. This makes the item very weak against edged attacks, even if the thread material is normally very strong. |
|  LAYER_SIZE | value | All garments | The item's bulkiness when worn. Aside from the layer limitations, it's a big contributor to the thickness and weight (and therefore price) of the garment. See Armor for more on item sizes and layering. Defaults to 10. |
|  LAYER_PERMIT | value | All garments | The maximum amount of crap that can fit underneath the garment. See Armor for more on item sizes and layering. Defaults to 10. |
|  LAYER | UNDER / OVER / ARMOR / COVER | All garments | Where the item goes in relation to other clothes. Socks cannot be worn on top of boots! / The LAYER_PERMIT of the highest layer is used on a given section of the body - you can fit a lot of shirts and other undergarments underneath a robe, but not if you wear a leather jerkin on top of it, and you can still wear a cloak over the whole ensemble. Defaults to UNDER. |
|  COVERAGE | % value | All garments | How often the garment gets in the way of a contaminant or an attack. Armor with a 5% coverage value, for example, will be near useless because 95% of attacks will bypass it completely. Temperature effects and armor thickness are also influenced. Defaults to 100. |
