# Bismuth bronze

> Fonte: [Bismuth bronze](https://dwarffortresswiki.org/index.php/Bismuth_bronze) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Uses**
- **Melee Weapons Crossbows Bolts Picks Armor Metal crafting Construction**
- **Recipe**
- **1 Tin 2 Copper 1 Bismuth**
- **Properties**
- **Material value 6☼ Impact strength 843.5 MPa Shear strength 241 MPa Fire-safe Not magma-safe Melting point 11868 °U Boiling point 14140 °U Ignition point none Solid density 8250 kg/m³ Liquid density 8020 kg/m³ Specific heat 435 J/kg·K Color tan**
- **Fire-safe:** Not magma-safe

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Bismuth bronze** is an alloy of copper, tin and bismuth, with exactly the same weapon and armor properties as regular bronze. However, it is slightly more valuable (×6 vs ×5) than regular bronze.

## Uses

Just like regular bronze, it can be used to make weapons and armour, along with all furniture and other objects. Bismuth bronze is 20% more valuable than bronze and three times more valuable than its component parts.

## Obtaining

Bismuth bronze is made with the following recipe:

- from bars (not ores): 1 Tin bar + 2 Copper bars + 1 Bismuth bar = 4 Bismuth Bronze bars

Because of these proportions, bismuth bronze is produced in lots of four bars at a time. While the ores must be smelted normally, only one additional fuel is needed to produce those four bars of bismuth bronze from the four bars noted above at a regular smelter. At a magma smelter, fuel isn't an issue, although the additional time and labor of smelting each ore chunk into bars should still be considered.

Bismuth bronze also provides more weapons-grade metal per tin bar than regular bronze, which may be a consideration if cassiterite is rare on your map.

## Trivia

In real life, bismuth bronze is often used in applications where ordinary bronze would corrode, as bismuth bronze is very corrosion-resistant, much like gold. Unlike in *Dwarf Fortress*, real bismuth bronze typically does not contain more than 1-3% bismuth by weight, though in some cases up to 6% bismuth may be used (which is still drastically less than the apparent 25% in-game); however, the first known object made with bismuth bronze (which is an Inca knife dated to 1476-1534) contains about 18% bismuth.

Long bismuth bronze bars.

    you can make a lighter colored bronze by adding bismuth, used temp values from bronze, used by incas, at least according to one source ha ha
    [INORGANIC:BISMUTH_BRONZE]
        [USE_MATERIAL_TEMPLATE:METAL_TEMPLATE]
        [STATE_NAME_ADJ:ALL_SOLID:bismuth bronze]
        [STATE_NAME_ADJ:LIQUID:molten bismuth bronze]
        [STATE_NAME_ADJ:GAS:boiling bismuth bronze]
        [DISPLAY_COLOR:6:6:1]
        [BUILD_COLOR:6:6:1]
        [MATERIAL_VALUE:6]
        [SPEC_HEAT:435]
        [MELTING_POINT:11868]
        [BOILING_POINT:14140]
        [ITEMS_WEAPON][ITEMS_WEAPON_RANGED][ITEMS_AMMO][ITEMS_DIGGER][ITEMS_ARMOR]
        [SOLID_DENSITY:8250] used bronze
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
        [ITEMS_HARD]
        [ITEMS_METAL]
        [ITEMS_BARRED]
        [ITEMS_SCALED]
        [STATE_COLOR:ALL_SOLID:TAN]
