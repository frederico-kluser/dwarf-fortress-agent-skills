# Calcite

> Fonte: [Calcite](https://dwarffortresswiki.org/index.php/Calcite) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Uses**
- **Masonry Stone crafting Construction Flux Make quicklime**
- **Location**
- **Found within limestone as small clusters Found within marble as small clusters**
- **Properties**
- **Material value 2☼ Fire-safe Magma-safe Melting point 12902 °U ( m ) Boiling point 14000 °U ( m ) Ignition point none ( m ) Solid density 2930 kg/m³ Specific heat 800 J/kg·K Color flax**
- **Fire-safe:** Magma-safe

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Calcite** is a flux stone; however, it's not particularly special, as it is found solely within limestone and marble, both of which are *also* flux. Its only distinguishing characteristic is that it is a magma-safe rock.

## In real life

Calcite is a crystalline form of calcium carbonate (CaCO3). Calcite is extremely common, forming multiple types of rocks, such as limestone, marble, and chalk, it is also known to form as a concrete in some sandstones and siltstones. Calcite, along with other crystalline forms of calcium carbonate such as Aragonite (which is not present in *Dwarf Fortress*) is readily edible (although not easily chewed, and not very palatable), and can be used as a supplementary source of calcium in an otherwise calcium-poor diet.

-

  A sample of Calcite

    main constituent of limestone, but can be found as crystal
    [INORGANIC:CALCITE]
    [USE_MATERIAL_TEMPLATE:STONE_TEMPLATE]
    [STATE_NAME_ADJ:ALL_SOLID:calcite][DISPLAY_COLOR:7:7:1][TILE:'"']
    [REACTION_CLASS:FLUX]
    [REACTION_CLASS:CALCIUM_CARBONATE]
    [ENVIRONMENT_SPEC:LIMESTONE:CLUSTER_SMALL:100]
    [ENVIRONMENT_SPEC:MARBLE:CLUSTER_SMALL:100]
    [MATERIAL_VALUE:2]
    [IS_STONE]
    [MELTING_POINT:12902]
    [SOLID_DENSITY:2930]
    [STATE_COLOR:ALL_SOLID:FLAX]
