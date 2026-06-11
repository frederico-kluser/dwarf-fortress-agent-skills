# Graphite

> Fonte: [Graphite](https://dwarffortresswiki.org/index.php/Graphite) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Uses**
- **Masonry Stone crafting Construction**
- **Location**
- **Found within gneiss as small clusters Found within quartzite as small clusters Found within marble as small clusters Found within schist as small clusters**
- **Properties**
- **Material value 1☼ Fire-safe Not magma-safe Melting point none ( m ) Boiling point 16708 °U ( m ) Ignition point 11440 °U ( x ) Solid density 2160 kg/m³ Specific heat 409 J/kg·K Color charcoal**
- **Fire-safe:** Not magma-safe

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Graphite** is a stone found within certain metamorphic layers. Graphite is flammable on contact with magma, but will never *melt*, meaning burning graphite makes an excellent long-burning flame - a single boulder will burn for about nine and a half months before being consumed. This quality has applications in some fire-based traps.

## In real life

Graphite is the most common form of carbon under standard Earth temperatures and pressures. It sits around 1.5 on the Mohs scale, making it a very soft substance. Synthetic Graphite is relatively easy to produce via compression.

Graphite's applications include steelmaking, lubricants, batteries, and of course, pencil "lead."

-

  Some graphite

    [INORGANIC:GRAPHITE]
    [USE_MATERIAL_TEMPLATE:STONE_TEMPLATE]
    [STATE_NAME_ADJ:ALL_SOLID:graphite][DISPLAY_COLOR:0:7:1][TILE:'o']
    comes from metamorphism of sedimentary rocks
    [ENVIRONMENT_SPEC:GNEISS:CLUSTER_SMALL:100]gneiss can come from shale (sed.) or granite (ign.)
    [ENVIRONMENT_SPEC:QUARTZITE:CLUSTER_SMALL:100]
    [ENVIRONMENT_SPEC:MARBLE:CLUSTER_SMALL:100]
    [ENVIRONMENT_SPEC:SCHIST:CLUSTER_SMALL:100]
    [SPEC_HEAT:409]
    [IGNITE_POINT:11440]
    [MELTING_POINT:NONE]
    [BOILING_POINT:16708]
    [SOLID_DENSITY:2160]
    [IS_STONE]
    [STATE_COLOR:ALL_SOLID:CHARCOAL]
