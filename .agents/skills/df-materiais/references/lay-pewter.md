# Lay pewter

> Fonte: [Lay pewter](https://dwarffortresswiki.org/index.php/Lay_pewter) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Uses**
- **Metal crafting Construction**
- **Recipe**
- **2 Tin bars 1 Copper bar 1 Lead bar**
- **Properties**
- **Material value 3☼ Impact strength 350 MPa Shear strength 100 MPa Not fire-safe Not magma-safe Melting point 10417 °U Boiling point 14684 °U Ignition point none Solid density 7280 kg/m³ Liquid density 6990 kg/m³ Specific heat 210 J/kg·K Color white**
- **Not fire-safe:** Not magma-safe

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Lay pewter** is an alloy that can created from bars of metal, at a smelter, using the following recipe:

- 2 Tin bars + 1 Copper bar + 1 Lead bar

Unlike trifle pewter and fine pewter, lay pewter *cannot* be smelted directly from ore.

Lay pewter has a base value of 3, which would make it preferable over its ingredient metals for creating objects of value, since all of its ingredients have a value of only 2. However, with the same ingredients (in a different formula) you get more value from making trifle pewter or, better still, bronze or fine pewter, and using lead as-is (separately).

When using classic ASCII graphics, lay pewter is notable for producing bars, furniture and crafts that appear in-game as teal-colored, a color shared only by clear glass and spore tree wood.

Technically *(i.e. "in real life")*, lay pewter is trifle pewter that has been cut with lead; it is less valuable, but you get more of it.

Lay pewter

    [INORGANIC:PEWTER_LAY]
        [USE_MATERIAL_TEMPLATE:METAL_TEMPLATE]
        [STATE_NAME_ADJ:ALL_SOLID:lay pewter]
        [STATE_NAME_ADJ:LIQUID:molten lay pewter]
        [STATE_NAME_ADJ:GAS:boiling lay pewter]
        [DISPLAY_COLOR:3:7:0]
        [BUILD_COLOR:3:7:0]
        [MATERIAL_VALUE:3]
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
        [STATE_COLOR:ALL_SOLID:WHITE]
