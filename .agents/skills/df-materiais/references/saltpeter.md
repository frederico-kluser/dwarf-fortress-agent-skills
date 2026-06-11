# Saltpeter

> Fonte: [Saltpeter](https://dwarffortresswiki.org/index.php/Saltpeter) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Uses**
- **Masonry Stone crafting Construction**
- **Location**
- **Found in sedimentary layers as small clusters**
- **Properties**
- **Material value 1☼ Not fire-safe Not magma-safe Melting point 10601 °U ( x ) Boiling point 10720 °U ( x ) Ignition point none ( m ) Solid density 2105 kg/m³ Specific heat 800 J/kg·K Color ivory**
- **Not fire-safe:** Not magma-safe

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Saltpeter** is a non-economic and low-value yellow stone found in small clusters within sedimentary layers. With a melting point of 10601 °U and a boiling point of only 10720 °U , it is one of the few stones which will *boil* in magma. Saltpeter is also the second least dense non-economic stone\*, making it better than most stone for objects that must be hauled frequently.

*(\* Saltpeter is about 60% heavier than jet, more than 21% lighter than typical stone, but about 350% (3 1/2 times) the weight of typical wood items.)*

In real life, its best known use is as a primary ingredient of gunpowder, along with charcoal and sulfur. This process does not exist in *Dwarf Fortress* (yet; it seems Toady One has plans to include gunpowder later, but only for simple uses[1]), and therefore gunpowder is also non-existent. Saltpeter, as a source of both potassium (like potash) and nitrogen, is also a fertilizer, though it is not possible to use it as such in *Dwarf Fortress*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
It is rumored that if a dwarf ever discovers saltpeter's capabilities, dwarven "civilization" would come to an explosive, but Fun end.

Despite persistent myths to the contrary, adding saltpeter to your male dwarves' military rations will *not* help to control your fortress's population *or* reduce incidences of romantic infidelity.

Saltpeter mine.

    potassium nitrate, good for fertilizer and blowing things up with carbon and sulfur
    [INORGANIC:SALTPETER]
    [USE_MATERIAL_TEMPLATE:STONE_TEMPLATE]
    [STATE_NAME_ADJ:ALL_SOLID:saltpeter][DISPLAY_COLOR:6:7:1][TILE:'x']
    [ENVIRONMENT:SEDIMENTARY:CLUSTER_SMALL:100]
    [SOLID_DENSITY:2105]  Previous value was much too low
    [IS_STONE]
    [MELTING_POINT:10601]
    [BOILING_POINT:10720]
    [STATE_COLOR:ALL_SOLID:IVORY]
