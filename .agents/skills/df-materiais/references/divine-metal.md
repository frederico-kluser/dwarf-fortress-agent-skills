# Divine metal

> Fonte: [Divine metal](https://dwarffortresswiki.org/index.php/Divine_metal) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Uses**
- **Melee Weapons Crossbows Bolts Picks Armor Anvils Metal crafting Construction**
- **Ore**
- **N/A**
- **Properties**
- **Material value 200☼ Impact strength 2 GPa Shear strength 2 GPa ×1.2 Fire-safe Magma-safe Melting point None Boiling point None Ignition point None Solid density 1000 kg/m³ Liquid density 1000 kg/m³ Molar mass 20000 kg/mol Specific heat 7500 J/kg·K**
- **Fire-safe:** Magma-safe

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

|  |  |
|:--:|----|
|  | This article contains **massive spoilers**. If you do not wish to have your game experience spoiled, **do not scroll down**! |

**Divine metals** are special, procedurally generated metals that can be found in vaults as well as deep underground. Divine metals are used as material for items, weapons and armor used by angels, who ruthlessly protect the vault's priceless treasures. (Similar divine fabrics are used by vault guardians for clothing and soft items.) Weapons made from divine metals have cyan bands on the sprites, though they may be found in the form of spriteless divine equipment.

## Traits

A dwarf wearing armor made with metal made by the gods.\
*Art by Metadomino*

Divine metals appear to have identical material properties and lists of items craftable from them; the only differences between them are the names, colors, and deity associations. All divine metals have high yield values of 1,000,000 KPa and fracture values of 2,000,000 KPa, and perfect strain-at-yield values of 0. They are extremely light, at a solid density of only 1000 kg/m³, and have a superior max edge of 12000. They are granted spheres matching the associated deity that created the metal (and the guardians who wield it), and a descriptive name with the formula of "(adjective) metal" – examples of such are "multicoloured metal", "pale metal", and "twisting metal".

Overall, their material properties are much better than the corresponding values of steel and mostly worse than those of adamantine. They are terrifyingly potent when used for edged weapons, due to their ultra-sharpness, but despite their light weight, even blunt weapons tend to be highly effective (unlike adamantine, which is worthless for blunt weapons). As armor, they are the only form of metal that is immune to dragonfire, as it cannot melt or boil. Despite this immunity to melting when worn as armor, divine metals can be designated for melting at a smelter. Doing so will produce a number of divine metal bars equal to the yield of the item type. The bars can then be used at a metalsmith's forge to create weapons, armor, etc. just like normal metal bars.

Divine metal can't be produced conventionally. However, since divine metal gives same amount of ingots as normal metals when melted, it's easier to replicate divine metal than it is to replicate adamantine.

The object testing arena allows one to test weapons and armour made of divine metals.

You can smell the gods on this sphere.

|  |
|----|
| "Divine metal" in other / Languages / Dwarven / : / Nabaskel / Elven / : / Mecalalethi / Goblin / : / Ngungdubsnusm / Human / : / Nirnorigu |

## Types

Each world will have a random set of 10 of these 26 metals in its raws.

|  |  |  |  |
|----|----|----|----|
| Sphere | Name | Color\* | Sprite |
| Blight | rusted metal | Rust |  |
| Chaos | twisting metal | Red |  |
| Darkness | dark metal | Black |  |
| Dawn | glowing metal | Yellow |  |
| Day | bright metal | White |  |
| Death | pale metal | Pale blue |  |
| Deformity | pock-marked metal | Black |  |
| Disease | blistered metal | Black |  |
| Earth | ruddy metal | Burnt sienna |  |
| Fire | flickering metal | Yellow |  |
| Jewels | faceted metal | Green |  |
| Light | shining metal | White |  |
| Lightning | flashing metal | Yellow |  |
| Moon | translucent metal | Clear |  |
| Mountains | frosty metal | White |  |
| Muck | slick metal | Brown |  |
| Music | singing metal | White |  |
| Night | black metal | Black |  |
| Rainbows | multicolored metal | Clear |  |
| Sky | clear blue metal | Sky blue |  |
| Stars | twinkling metal | White |  |
| Storms | crashing metal | Gray |  |
| Sun | blazing metal | White |  |
| Thunder | booming metal | Gray |  |
| Torture | searing metal | Black |  |
| Volcanos | flowing metal | Red |  |

\*The named colors represent their [`[STATE_COLOR]`](/index.php/Material_definition_token#STATE_COLOR "Material definition token") token, while the background colors are the colors they appear as in-game in ASCII mode. See color.

    Example raws (as extracted from save files in version 0.50.11)

    [INORGANIC:DIVINE_17]
        [GENERATED]
        [DIVINE]
        [DISPLAY_COLOR:7:0:1]
        [BUILD_COLOR:7:0:1]
        [STATE_COLOR:ALL_SOLID:WHITE]
        [USE_MATERIAL_TEMPLATE:METAL_TEMPLATE]
        [STATE_NAME_ADJ:ALL_SOLID:blazing metal]
        [MATERIAL_VALUE:200]
        [SPEC_HEAT:7500]
        [MELTING_POINT:NONE]
        [BOILING_POINT:NONE]
        [ITEMS_WEAPON]
        [ITEMS_WEAPON_RANGED]
        [ITEMS_AMMO]
        [ITEMS_DIGGER]
        [ITEMS_ARMOR]
        [ITEMS_ANVIL]
        [ITEMS_HARD]
        [ITEMS_METAL]
        [ITEMS_BARRED]
        [ITEMS_SCALED]
        [SOLID_DENSITY:1000]
        [LIQUID_DENSITY:1000]
        [MOLAR_MASS:20000]
        [IMPACT_YIELD:1000000]
        [IMPACT_FRACTURE:2000000]
        [IMPACT_STRAIN_AT_YIELD:0]
        [COMPRESSIVE_YIELD:1000000]
        [COMPRESSIVE_FRACTURE:2000000]
        [COMPRESSIVE_STRAIN_AT_YIELD:0]
        [TENSILE_YIELD:1000000]
        [TENSILE_FRACTURE:2000000]
        [TENSILE_STRAIN_AT_YIELD:0]
        [TORSION_YIELD:1000000]
        [TORSION_FRACTURE:2000000]
        [TORSION_STRAIN_AT_YIELD:0]
        [SHEAR_YIELD:1000000]
        [SHEAR_FRACTURE:2000000]
        [SHEAR_STRAIN_AT_YIELD:0]
        [BENDING_YIELD:1000000]
        [BENDING_FRACTURE:2000000]
        [BENDING_STRAIN_AT_YIELD:0]
        [MAX_EDGE:12000]
        [SPHERE:SUN]

    [INORGANIC:DIVINE_15]
        [GENERATED]
        [DIVINE]
        [DISPLAY_COLOR:7:0:1]
        [BUILD_COLOR:7:0:1]
        [STATE_COLOR:ALL_SOLID:WHITE]
        [USE_MATERIAL_TEMPLATE:METAL_TEMPLATE]
        [STATE_NAME_ADJ:ALL_SOLID:twinkling metal]
        [MATERIAL_VALUE:200]
        [SPEC_HEAT:7500]
        [MELTING_POINT:NONE]
        [BOILING_POINT:NONE]
        [ITEMS_WEAPON]
        [ITEMS_WEAPON_RANGED]
        [ITEMS_AMMO]
        [ITEMS_DIGGER]
        [ITEMS_ARMOR]
        [ITEMS_ANVIL]
        [ITEMS_HARD]
        [ITEMS_METAL]
        [ITEMS_BARRED]
        [ITEMS_SCALED]
        [SOLID_DENSITY:1000]
        [LIQUID_DENSITY:1000]
        [MOLAR_MASS:20000]
        [IMPACT_YIELD:1000000]
        [IMPACT_FRACTURE:2000000]
        [IMPACT_STRAIN_AT_YIELD:0]
        [COMPRESSIVE_YIELD:1000000]
        [COMPRESSIVE_FRACTURE:2000000]
        [COMPRESSIVE_STRAIN_AT_YIELD:0]
        [TENSILE_YIELD:1000000]
        [TENSILE_FRACTURE:2000000]
        [TENSILE_STRAIN_AT_YIELD:0]
        [TORSION_YIELD:1000000]
        [TORSION_FRACTURE:2000000]
        [TORSION_STRAIN_AT_YIELD:0]
        [SHEAR_YIELD:1000000]
        [SHEAR_FRACTURE:2000000]
        [SHEAR_STRAIN_AT_YIELD:0]
        [BENDING_YIELD:1000000]
        [BENDING_FRACTURE:2000000]
        [BENDING_STRAIN_AT_YIELD:0]
        [MAX_EDGE:12000]
        [SPHERE:STARS]

    [INORGANIC:DIVINE_11]
        [GENERATED]
        [DIVINE]
        [DISPLAY_COLOR:6:0:1]
        [BUILD_COLOR:6:0:1]
        [STATE_COLOR:ALL_SOLID:YELLOW]
        [USE_MATERIAL_TEMPLATE:METAL_TEMPLATE]
        [STATE_NAME_ADJ:ALL_SOLID:flashing metal]
        [MATERIAL_VALUE:200]
        [SPEC_HEAT:7500]
        [MELTING_POINT:NONE]
        [BOILING_POINT:NONE]
        [ITEMS_WEAPON]
        [ITEMS_WEAPON_RANGED]
        [ITEMS_AMMO]
        [ITEMS_DIGGER]
        [ITEMS_ARMOR]
        [ITEMS_ANVIL]
        [ITEMS_HARD]
        [ITEMS_METAL]
        [ITEMS_BARRED]
        [ITEMS_SCALED]
        [SOLID_DENSITY:1000]
        [LIQUID_DENSITY:1000]
        [MOLAR_MASS:20000]
        [IMPACT_YIELD:1000000]
        [IMPACT_FRACTURE:2000000]
        [IMPACT_STRAIN_AT_YIELD:0]
        [COMPRESSIVE_YIELD:1000000]
        [COMPRESSIVE_FRACTURE:2000000]
        [COMPRESSIVE_STRAIN_AT_YIELD:0]
        [TENSILE_YIELD:1000000]
        [TENSILE_FRACTURE:2000000]
        [TENSILE_STRAIN_AT_YIELD:0]
        [TORSION_YIELD:1000000]
        [TORSION_FRACTURE:2000000]
        [TORSION_STRAIN_AT_YIELD:0]
        [SHEAR_YIELD:1000000]
        [SHEAR_FRACTURE:2000000]
        [SHEAR_STRAIN_AT_YIELD:0]
        [BENDING_YIELD:1000000]
        [BENDING_FRACTURE:2000000]
        [BENDING_STRAIN_AT_YIELD:0]
        [MAX_EDGE:12000]
        [SPHERE:LIGHTNING]

    [INORGANIC:DIVINE_7]
        [GENERATED]
        [DIVINE]
        [DISPLAY_COLOR:4:0:0]
        [BUILD_COLOR:4:0:0]
        [STATE_COLOR:ALL_SOLID:RUST]
        [USE_MATERIAL_TEMPLATE:METAL_TEMPLATE]
        [STATE_NAME_ADJ:ALL_SOLID:rusted metal]
        [MATERIAL_VALUE:200]
        [SPEC_HEAT:7500]
        [MELTING_POINT:NONE]
        [BOILING_POINT:NONE]
        [ITEMS_WEAPON]
        [ITEMS_WEAPON_RANGED]
        [ITEMS_AMMO]
        [ITEMS_DIGGER]
        [ITEMS_ARMOR]
        [ITEMS_ANVIL]
        [ITEMS_HARD]
        [ITEMS_METAL]
        [ITEMS_BARRED]
        [ITEMS_SCALED]
        [SOLID_DENSITY:1000]
        [LIQUID_DENSITY:1000]
        [MOLAR_MASS:20000]
        [IMPACT_YIELD:1000000]
        [IMPACT_FRACTURE:2000000]
        [IMPACT_STRAIN_AT_YIELD:0]
        [COMPRESSIVE_YIELD:1000000]
        [COMPRESSIVE_FRACTURE:2000000]
        [COMPRESSIVE_STRAIN_AT_YIELD:0]
        [TENSILE_YIELD:1000000]
        [TENSILE_FRACTURE:2000000]
        [TENSILE_STRAIN_AT_YIELD:0]
        [TORSION_YIELD:1000000]
        [TORSION_FRACTURE:2000000]
        [TORSION_STRAIN_AT_YIELD:0]
        [SHEAR_YIELD:1000000]
        [SHEAR_FRACTURE:2000000]
        [SHEAR_STRAIN_AT_YIELD:0]
        [BENDING_YIELD:1000000]
        [BENDING_FRACTURE:2000000]
        [BENDING_STRAIN_AT_YIELD:0]
        [MAX_EDGE:12000]
        [SPHERE:BLIGHT]
