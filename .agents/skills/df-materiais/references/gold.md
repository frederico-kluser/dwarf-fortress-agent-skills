# Gold

> Fonte: [Gold](https://dwarffortresswiki.org/index.php/Gold) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Uses**
- **Make black bronze at smelter Make electrum at smelter Make rose gold at smelter Metal crafting Construction**
- **Ore**
- **Native gold**
- **Properties**
- **Material value 30☼ Impact strength 350 MPa Shear strength 100 MPa Fire-safe Not magma-safe Melting point 11915 °U Boiling point 15141 °U Ignition point none Solid density 19320 kg/m³ Liquid density 17310 kg/m³ Specific heat 129 J/kg·K Color gold**
- **Fire-safe:** Not magma-safe

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Gold** is a high-value, relatively common metal - the fourth highest value metal, in fact, tied with steel. The only ore of gold is native gold, which yields **gold nuggets** when mined. Each gold nugget can be turned into four gold bars at a smelter or magma smelter by a dwarf with the furnace operating labor enabled. Gold is fire-safe but *not* magma safe.

Gold may be combined with other metals at a smelter or magma smelter to form several alloys:

- Black bronze = Gold + Silver + 2× Copper
- Electrum = Gold + Silver
- Rose gold = 3× Gold + Copper

None of the gold alloys have a greater material value than gold itself, but may prove useful if gold is particularly scarce on a map. Further, if gold nuggets (material value 30) are smelted directly with a low-value silver ore such as galena (material value 5) or tetrahedrite (material value 3), it will produce eight bars of electrum (material value 20) for a net gain in total value.

Refining gold nuggets produces 4 bars, which can result in significantly increased value compared to the original nuggets. However, in some cases, it may be advantageous to make furniture directly from gold ore, since it requires no fuel and uses a labor, stone carving, that is more easily trained than blacksmithing. Native gold furniture may also be useful to satisfy a noble's needs for their own specific, high-value rooms. To use native gold for furniture and the like, you should place a stone stockpile allowing only native gold near your Mason's workshop (native gold furniture, blocks, etc.), Craftsdwarf's workshop (native gold crafts), or Mechanic's workshop (native gold mechanisms) and enable "gold nuggets" (**not** "gold") using the y: `Stone use` menu. To avoid wasting gold nuggets, assign your stockpile to 'give' only to one specific workshop, and disable non-economic use upon completion.

Note that a dwarf who has a preference for gold metal will not be particularly impressed by items crafted from native gold nuggets, and vice-versa.

Gold cannot be used to make weapons or armor directly, but can be used for artifacts. Gold armor will protect poorly; maybe half as well as bronze (due to lower impact fracture/yield ratio). For weapons, edged attacks will perform even worse than silver (due to lower shear fracture), while blunt attacks will have less than 1% more momentum than silver (despite having almost twice the density), and the extra weight will exhaust the wielder faster.

#### History

Gold used to be one of the three metals (with copper and silver) used to mint coins for the dwarven economy, and has the highest value of the three.

-

  A gold bar.

|  |
|----|
| "Gold" in other / Languages / Dwarven / : / limul / Elven / : / ithi / Goblin / : / ongong / Human / : / abli |

    [INORGANIC:GOLD]
        [USE_MATERIAL_TEMPLATE:METAL_TEMPLATE]
        [STATE_NAME:SOLID:gold]
        [STATE_NAME:SOLID_POWDER:gold dust]
        [STATE_ADJ:ALL_SOLID:gold]
        [STATE_NAME_ADJ:LIQUID:molten gold]
        [STATE_NAME_ADJ:GAS:boiling gold]
        [DISPLAY_COLOR:6:6:1]
        [BUILD_COLOR:6:6:1]
        [MATERIAL_VALUE:30]
        [SPEC_HEAT:129]
        [MELTING_POINT:11915]
        [BOILING_POINT:15141]
        [SOLID_DENSITY:19320]
        [LIQUID_DENSITY:17310]
        [MOLAR_MASS:196967]
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
        [STATE_COLOR:ALL_SOLID:GOLD]
