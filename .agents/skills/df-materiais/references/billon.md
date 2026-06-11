# Billon

> Fonte: [Billon](https://dwarffortresswiki.org/index.php/Billon) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Uses**
- **Metal crafting Construction**
- **Recipe**
- **1 silver bar 1 copper bar - or - 1 silver ore 1 copper ore**
- **Properties**
- **Material value 6☼ Impact strength 770 MPa Shear strength 220 MPa Fire-safe Not magma-safe Melting point 11952 °U Boiling point 14611 °U Ignition point none Solid density 8930 kg/m³ Liquid density 8020 kg/m³ Specific heat 385 J/kg·K Color pale brown**
- **Fire-safe:** Not magma-safe

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Billon** is an alloy of equal parts silver and copper. Historically, billon was used to mint coins, but it remains to be seen if billon coins will be useful when the dwarven economy is re-developed.

Two billon bars can be made at a smelter from 1 silver bar and 1 copper bar, which does not create an increase in value. However, eight billon bars can be created by smelting 1 silver-bearing ore and 1 copper-bearing ore. Since tetrahedrite counts as both types of ore, two tetrahedrite nuggets can yield eight bars of billon for a roughly 70% increase in value over smelting the tetrahedrite nuggets separately. This recipe will only be used when no other silver-bearing ores are available to the smelter, otherwise silver nuggets or galena ore will be used as the silver-bearing ore, though tetrahedrite can still serve as the copper-bearing ore.

## Notes

Unlike both of its constituent metals, billon cannot be used to forge weapons or ammunition. Billon can be used to make moderately valuable furniture and other objects at a Metalsmith's forge. Be aware, however, that it is not magma-safe.

Billon coin.

    temperature values unknown, used copper
    [INORGANIC:BILLON]
        [USE_MATERIAL_TEMPLATE:METAL_TEMPLATE]
        [STATE_NAME_ADJ:ALL_SOLID:billon]
        [STATE_NAME_ADJ:LIQUID:molten billon]
        [STATE_NAME_ADJ:GAS:boiling billon]
        [DISPLAY_COLOR:7:3:0]
        [BUILD_COLOR:7:3:0]
        [MATERIAL_VALUE:6]
        [SPEC_HEAT:385]
        [MELTING_POINT:11952]
        [BOILING_POINT:14611]
        [SOLID_DENSITY:8930] used copper
        [LIQUID_DENSITY:8020]
        [MOLAR_MASS:63546]
        [IMPACT_YIELD:245000]
        [IMPACT_FRACTURE:770000]
        [IMPACT_STRAIN_AT_YIELD:175]
        [COMPRESSIVE_YIELD:245000]
        [COMPRESSIVE_FRACTURE:770000]
        [COMPRESSIVE_STRAIN_AT_YIELD:175] 140
        [TENSILE_YIELD:70000]
        [TENSILE_FRACTURE:220000]
        [TENSILE_STRAIN_AT_YIELD:58] 120
        [TORSION_YIELD:70000]
        [TORSION_FRACTURE:220000]
        [TORSION_STRAIN_AT_YIELD:145]
        [SHEAR_YIELD:70000]
        [SHEAR_FRACTURE:220000]
        [SHEAR_STRAIN_AT_YIELD:145] 48
        [BENDING_YIELD:70000]
        [BENDING_FRACTURE:220000]
        [BENDING_STRAIN_AT_YIELD:58]
        [MAX_EDGE:10000]
        [ITEMS_HARD]
        [ITEMS_METAL]
        [ITEMS_BARRED]
        [ITEMS_SCALED]
        [STATE_COLOR:ALL_SOLID:PALE_BROWN]
