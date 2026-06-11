# Trifle pewter

> Fonte: [Trifle pewter](https://dwarffortresswiki.org/index.php/Trifle_pewter) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Uses**
- **Metal crafting Construction**
- **Recipe**
- **2 Tin bars 1 Copper bar - or - 2 Cassiterite 1 Copper ore**
- **Properties**
- **Material value 4☼ Impact strength 350 MPa Shear strength 100 MPa Not fire-safe Not magma-safe Melting point 10417 °U Boiling point 14648 °U Ignition point none Solid density 7280 kg/m³ Liquid density 6990 kg/m³ Specific heat 210 J/kg·K Color taupe gray**
- **Not fire-safe:** Not magma-safe

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Trifle pewter** is an alloy of tin and copper.

Trifle pewter can be made using one of the following recipes:

- 2 Tin bars + 1 Copper bar = 3 Trifle pewter bars
- 2 Cassiterite + 1 Native copper, Malachite, or Tetrahedrite = 12 Trifle pewter bars

Trifle pewter has a base value of 4, making it better for objects of wealth than its ingredients, whose base values are merely 2. Using tin and copper in this way is, however, still not advisable because fine pewter and bronze use the same ingredients (with different formulae), but have base values of 5.

Trifle pewter flask.

    [INORGANIC:PEWTER_TRIFLE]
        [USE_MATERIAL_TEMPLATE:METAL_TEMPLATE]
        [STATE_NAME_ADJ:ALL_SOLID:trifle pewter]
        [STATE_NAME_ADJ:LIQUID:molten trifle pewter]
        [STATE_NAME_ADJ:GAS:boiling trifle pewter]
        [DISPLAY_COLOR:7:3:0]
        [BUILD_COLOR:7:3:0]
        [MATERIAL_VALUE:4]
        [SPEC_HEAT:210]
        [MELTING_POINT:10417]
        [BOILING_POINT:14684]
        [SOLID_DENSITY:7280]
        [LIQUID_DENSITY:6990]
        [MOLAR_MASS:118710]
        [IMPACT_YIELD:42000]
        [IMPACT_FRACTURE:350000]
        [IMPACT_STRAIN_AT_YIELD:724]
        [COMPRESSIVE_YIELD:42000]
        [COMPRESSIVE_FRACTURE:350000]
        [COMPRESSIVE_STRAIN_AT_YIELD:724] 58
        [TENSILE_YIELD:12000]
        [TENSILE_FRACTURE:100000]
        [TENSILE_STRAIN_AT_YIELD:24] 50
        [TORSION_YIELD:12000]
        [TORSION_FRACTURE:100000]
        [TORSION_STRAIN_AT_YIELD:66]
        [SHEAR_YIELD:12000]
        [SHEAR_FRACTURE:100000]
        [SHEAR_STRAIN_AT_YIELD:66] 18
        [BENDING_YIELD:12000]
        [BENDING_FRACTURE:100000]
        [BENDING_STRAIN_AT_YIELD:24]
        [MAX_EDGE:10000]
        [ITEMS_HARD]
        [ITEMS_METAL]
        [ITEMS_BARRED]
        [ITEMS_SCALED]
        [STATE_COLOR:ALL_SOLID:TAUPE_GRAY]
