# Zinc

> Fonte: [Zinc](https://dwarffortresswiki.org/index.php/Zinc) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Uses**
- **Make nickel silver at smelter Make brass at smelter Metal crafting Construction**
- **Ore**
- **Sphalerite**
- **Properties**
- **Material value 2☼ Impact strength 525 MPa Shear strength 150 MPa Not fire-safe Not magma-safe Melting point 10755 °U Boiling point 11633 °U Ignition point none Solid density 7135 kg/m³ Liquid density 6570 kg/m³ Specific heat 390 J/kg·K Color silver**
- **Not fire-safe:** Not magma-safe

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Zinc** is an uncommon, low-value metal primarily useful in the creation of alloys. It is smelted from sphalerite. Note that, unlike sphalerite itself, refined zinc is **not** magma-safe, or even fire-safe, and will melt in a grass fire. Zinc is the lightest of the low value metals, slightly lighter than tin, but still much heavier than rare aluminum.

Zinc may be combined with other metals at a smelter to form the following alloys:

- Brass = Zinc + Copper
- Nickel silver = Zinc + Copper + 2x Nickel

    [INORGANIC:ZINC]
        [USE_MATERIAL_TEMPLATE:METAL_TEMPLATE]
        [STATE_NAME_ADJ:ALL_SOLID:zinc]
        [STATE_NAME_ADJ:LIQUID:molten zinc]
        [STATE_NAME_ADJ:GAS:boiling zinc]
        [DISPLAY_COLOR:7:3:0]
        [BUILD_COLOR:7:3:0]
        [MATERIAL_VALUE:2]
        [SPEC_HEAT:390]
        [MELTING_POINT:10755]
        [BOILING_POINT:11633]
        [SOLID_DENSITY:7135]
        [LIQUID_DENSITY:6570]
        [MOLAR_MASS:65380]
        [IMPACT_YIELD:175000]
        [IMPACT_FRACTURE:525000]
        [IMPACT_STRAIN_AT_YIELD:250]
        [COMPRESSIVE_YIELD:175000]
        [COMPRESSIVE_FRACTURE:525000]
        [COMPRESSIVE_STRAIN_AT_YIELD:250] 70
        [TENSILE_YIELD:50000]
        [TENSILE_FRACTURE:150000]
        [TENSILE_STRAIN_AT_YIELD:46] 108
        [TORSION_YIELD:50000]
        [TORSION_FRACTURE:150000]
        [TORSION_STRAIN_AT_YIELD:116]
        [SHEAR_YIELD:50000]
        [SHEAR_FRACTURE:150000]
        [SHEAR_STRAIN_AT_YIELD:116] 43
        [BENDING_YIELD:50000]
        [BENDING_FRACTURE:150000]
        [BENDING_STRAIN_AT_YIELD:46]
        [MAX_EDGE:10000]
        [ITEMS_HARD]
        [ITEMS_METAL]
        [ITEMS_BARRED]
        [ITEMS_SCALED]
        [STATE_COLOR:ALL_SOLID:SILVER]
