# Bronze

> Fonte: [Bronze](https://dwarffortresswiki.org/index.php/Bronze) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Uses**
- **Melee Weapons Crossbows Bolts Picks Armor Metal crafting Construction**
- **Recipe**
- **1 tin bar 1 copper bar - or - 1 cassiterite 1 copper ore**
- **Properties**
- **Material value 5☼ Impact strength 843.5 MPa Shear strength 241 MPa Fire-safe Not magma-safe Melting point 11868 °U Boiling point 14140 °U Ignition point none Solid density 8250 kg/m³ Liquid density 8020 kg/m³ Specific heat 435 J/kg·K Color bronze**
- **Fire-safe:** Not magma-safe

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Bronze** is an alloy of tin and copper, which can be used to create all metallic items in the game.

## Smelting

Bronze can be made at the Smelter or Magma smelter using one of the following recipes:

- from ore: 1 Cassiterite + 1 Native copper, Malachite or Tetrahedrite = 8 Bronze bars
- from bars: 1 Tin bar + 1 Copper bar = 2 Bronze bars

## Use

Bronze can be forged into weapons and armor, and has material qualities very close to iron. Bronze can also be used to make furniture and other objects at a metalsmith's forge. It has a value of 5 and uses the same ingredients as fine pewter (which also has a value of 5). If you find yourself short of tin, use this metal to make your objects of art instead of using fine pewter. If you are using ores to smelt bronze, you can produce 8 bars of weapon-grade metal with one unit of fuel, making it an extremely useful material.

Alternatively, copper and tin can also be alloyed with bismuth, in order to make the alloy bismuth bronze. While this doesn't improve the properties of the materials, it does result in a modest increase in value and cuts the cost in tin in half.

The one major drawback of bronze compared to iron is that it cannot be used to make anvils.

## Material properties

As mentioned before, bronze has material properties that are very similar to those of iron, and is a significant improvement over copper, except for blunt weapons where its superior edge properties are virtually irrelevant. If your fortress is in an area without significant quantities of iron ore, then bronze is a very good substitute. However, the material properties of bronze are inferior to those of steel in virtually every way.

The properties of bismuth bronze are identical in every way to standard bronze, the only differences are that items made from bismuth bronze are 20% more valuable (×6 vs. ×5), and the color of bismuth bronze items in-game is yellow rather than brown.

|  |
|----|
| "Bronze" in other / Languages / Dwarven / : / kilrud / Elven / : / dagi / Goblin / : / susäl / Human / : / zobsha |

Bronze helm.

    [INORGANIC:BRONZE]
        [USE_MATERIAL_TEMPLATE:METAL_TEMPLATE]
        [STATE_NAME_ADJ:ALL_SOLID:bronze]
        [STATE_NAME_ADJ:LIQUID:molten bronze]
        [STATE_NAME_ADJ:GAS:boiling bronze]
        [DISPLAY_COLOR:6:4:0]
        [BUILD_COLOR:6:4:0]
        [MATERIAL_VALUE:5]
        [SPEC_HEAT:435]
        [MELTING_POINT:11868]
        [BOILING_POINT:14140]
        [ITEMS_WEAPON][ITEMS_WEAPON_RANGED][ITEMS_AMMO][ITEMS_DIGGER][ITEMS_ARMOR]
        [ITEMS_HARD]
        [ITEMS_METAL]
        [ITEMS_BARRED]
        [ITEMS_SCALED]
        [SOLID_DENSITY:8250]
        [LIQUID_DENSITY:8020]
        [MOLAR_MASS:80000]
        [IMPACT_YIELD:602000]
        [IMPACT_FRACTURE:843500]
        [IMPACT_STRAIN_AT_YIELD:523]
        [COMPRESSIVE_YIELD:602000]
        [COMPRESSIVE_FRACTURE:843500]
        [COMPRESSIVE_STRAIN_AT_YIELD:523] 115
        [TENSILE_YIELD:172000]
        [TENSILE_FRACTURE:241000]
        [TENSILE_STRAIN_AT_YIELD:156] 110
        [TORSION_YIELD:172000]
        [TORSION_FRACTURE:241000]
        [TORSION_STRAIN_AT_YIELD:420]
        [SHEAR_YIELD:172000]
        [SHEAR_FRACTURE:241000]
        [SHEAR_STRAIN_AT_YIELD:420] 41
        [BENDING_YIELD:172000]
        [BENDING_FRACTURE:241000]
        [BENDING_STRAIN_AT_YIELD:156]
        [MAX_EDGE:10000]
        [STATE_COLOR:ALL_SOLID:BRONZE]
