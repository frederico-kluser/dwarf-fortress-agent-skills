# Electrum

> Fonte: [Electrum](https://dwarffortresswiki.org/index.php/Electrum) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Uses**
- **Metal crafting Construction**
- **Recipe**
- **1 Silver bar 1 Gold bar - or - 1 Silver ore 1 Native gold**
- **Properties**
- **Material value 20☼ Impact strength 350 MPa Shear strength 100 MPa Fire-safe Not magma-safe Melting point 11828 °U Boiling point 14968 °U Ignition point none Solid density 14905 kg/m³ Liquid density 13000 kg/m³ Specific heat 180 J/kg·K Color ochre**
- **Fire-safe:** Not magma-safe

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Electrum** is an alloy of equal parts gold and silver. Electrum bars can be made at a smelter by a dwarf with the furnace operating labor activated. Electrum is useful for high-value crafts, furniture, and decorations.

One gold bar and one silver bar will produce two electrum bars. One gold nugget and one silver-bearing ore will produce eight electrum bars.

Smelting bars together consumes a value 30 material and a value 10 material to produce two units of value 20, thus producing no net gain (or loss); you're taking a high-value item and a medium-value item and averaging their values. The value relative to density is improved greatly, however, and makes hauling jobs much more efficient. Smelting the ores directly saves you five units of fuel (if you don't have access to magma). Moreover, low-value galena or tetrahedrite can be substituted for native silver or horn silver, producing more value overall than would be generated from smelting the ores separately. Thus, if you have access to galena or tetrahedrite, producing electrum bars creates value.

This is an x+electrum goblet+x. On the item is an image of two forgotten beasts and two gazelles. The two forgotten beasts are raising the two gazelles. The two forgotten beasts are screaming. The two gazelles look terrified.

    [INORGANIC:ELECTRUM]
        [USE_MATERIAL_TEMPLATE:METAL_TEMPLATE]
        [STATE_NAME_ADJ:ALL_SOLID:electrum]
        [STATE_NAME_ADJ:LIQUID:molten electrum]
        [STATE_NAME_ADJ:GAS:boiling electrum]
        [DISPLAY_COLOR:6:6:1]
        [BUILD_COLOR:6:6:1]
        [MATERIAL_VALUE:20]
        [SPEC_HEAT:180]
        [MELTING_POINT:11828]
        [BOILING_POINT:14968]
    Density based on an alloy of 50% gold + 50% silver, per the recipe for creating it (1 gold + 1 silver = 2 electrum)
    Also found a more accurate source, which gives a range of 13000-16000 -- http://books.google.com/books?id=OuoV-o_Xf-EC&pg=PA21&lpg=PA21&dq=electrum+density&source=bl&ots=Ar0C0iCqq9&sig=hy58B_naO8sUQtmwdRUNfrmiwBI&hl=en&ei=9lisTqH9IIaHtweDx5T0Dg&sa=X&oi=book_result&ct=result&resnum=4&ved=0CDUQ6AEwAw
        [SOLID_DENSITY:14905]
        [LIQUID_DENSITY:13000]
        [MOLAR_MASS:150000]
        Used gold.
        [IMPACT_YIELD:175000]
        [IMPACT_FRACTURE:350000]
        [IMPACT_STRAIN_AT_YIELD:97]
        [COMPRESSIVE_YIELD:175000]
        [COMPRESSIVE_FRACTURE:350000]
        [COMPRESSIVE_STRAIN_AT_YIELD:97] bulk modulus 180 GPa
        [TENSILE_YIELD:50000]
        [TENSILE_FRACTURE:100000]
        [TENSILE_STRAIN_AT_YIELD:64] young's modulus 78 GPa
        [TORSION_YIELD:50000]
        [TORSION_FRACTURE:100000]
        [TORSION_STRAIN_AT_YIELD:185]
        [SHEAR_YIELD:50000]
        [SHEAR_FRACTURE:100000]
        [SHEAR_STRAIN_AT_YIELD:185] shear modulus 27 GPa
        [BENDING_YIELD:50000]
        [BENDING_FRACTURE:100000]
        [BENDING_STRAIN_AT_YIELD:64]
        [MAX_EDGE:10000]
        [ITEMS_HARD]
        [ITEMS_METAL]
        [ITEMS_BARRED]
        [ITEMS_SCALED]
        [STATE_COLOR:ALL_SOLID:OCHRE]
