# Fuel

> Fonte: [Fuel](https://dwarffortresswiki.org/index.php/Fuel) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Uses**
- **Fuel Make pig iron and steel**
- **Properties**
- **Material value 2 Fire-safe Not magma-safe Ignition point 11440 °U Melting point None Boiling point None Solid density 1346 Specific heat 409**
- **Fire-safe:** Not magma-safe

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*In Dwarf Fortress, bituminous coal is not the same as "coal" – see that article if desired.*

**Fuel**, **coal**, and **refined coal** are three in-game terms that refer to the same thing, any unit of charcoal or coke, the two fuels used to power high-temperature industries, namely metalworking, glassworking, and pottery. One unit of either of these fuels is required for every task at a conventional (non-magma) smelter, forge, kiln, or glass furnace. Magma versions of these facilities do not need fuel, and in fact *cannot* use conventional fuel to power them, if their magma sources fail. Fuel is also used as a reactant in the pig iron and steel creation process *(see below)*.

Both "charcoal" and "coke" are considered bars; they are found under the "bars" section of the k-stocks menu and are stored in Bar/Block stockpiles. To place bars of fuel in a stockpile, create a Bars/Blocks stockpile, or a custom stockpile with "coal" (found in the "Bars" sub-category) enabled and permitted. To allow *only* coal in a stockpile, enable "Bars/Blocks", block everything, and enable "Bars: Other Materials → Coal" (with Enter). There is currently no way to distinguish between "charcoal" and "coke" when designating stockpiles. But you can sort the coal in stockpiles by origin: if plant-based ones are allowed, there will be charcoal, and if non-plant-based ones are allowed, there will be coal.

## Fuel: charcoal and coke

The two types of fuel are ***charcoal*** and ***coke*** – both are "fuel". These are *nearly identical* for in-game purposes, even though they come from different sources and have different in-game names. Whenever you see "fuel", "refined coal" or "coal" in-game, those refer to *either* charcoal or coke – they are interchangeable, and either one will serve as fuel for any workshop activity. Since some understandable confusion can arise over the usage of the various terms for fuel, the simple umbrella term "fuel" will be used in the explanations in this article.

To be perfectly clear – *despite the different names, there is no distinction between charcoal and coke for any workshop-related activities.* Both are "refined coal" or "coal", or just "fuel". **The only actual difference** between charcoal and coke has to do with Elven traders – trading them charcoal will offend them, but coke will not.

## Creating fuel

Wood does not burn hot enough for use as fuel, and (in *Dwarf Fortress*) raw bituminous coal and lignite, though flammable, are not directly usable as fuel. Both can, however, be converted to fuel using different processes:

### Charcoal, from wood

Charcoal is created at a wood furnace from wood logs by a dwarf with the Wood burning labor enabled. One log produces one bar of charcoal; skill levels in Wood burner reduce the time required for this activity, but do not affect the results.

- Required Building – Wood furnace
- Required Labor enabled – Wood burning
- Required Material – Wood

### Coke, from bituminous coal or lignite

Coke is a type of refined coal created at a smelter from either bituminous coal or lignite (producing either 9 or 5 coke, respectively) by a dwarf with the Furnace operating labor enabled. Skill levels in furnace operator reduce the time required for this activity, but do not affect the result.

At a conventional smelter, one bar of fuel is required to perform this reaction, effectively reducing the net yield by one bar.

- Required Building – Smelter or Magma smelter
- Required Labor enabled – Furnace operating
- Required Material – Bituminous coal or lignite
- Required Fuel – one unit of fuel per job at a conventional smelter

Blocks of bituminous coal and lignite (sometimes offered by traders) can neither be used as fuel nor converted into fuel in any way. They can only be used for standard block purposes – though they are, of course, *not* fire-safe!

Because you need fuel in order to refine coke at a standard smelter, you may need to create at least one unit of charcoal at a Wood Burner first, import a bar of fuel, or skip directly to magma power.

## Error messages

At a conventional (non-magma) smelter, if you try to add a smelting task and have no fuel, you will see the message:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| N | o |   | t | a | s | k | s |   | a | v | a | i | l | a | b | l | e |   |   |   |   |   |   |   |   |   |   |   |
| C | h | e | c | k |   | f | o | r |   | r | a | w |   | m | a | t | e | r | i | a | l |   | a | c | c | e | s | s |
| a | n | d |   | f | u | e | l |   | i | f |   | n | e | c | e | s | s | a | r | y |   |   |   |   |   |   |   |   |

*(Note that this message will also be seen if there is no path to your workshop or needed materials, including fuel, or if the necessary materials aren't in any linked stockpiles.)*

You will not be allowed to add any tasks to any conventional smelter until that workshop has access to at least one unit of either charcoal or coke. (However, if you have just one bar of un-used fuel, you can queue up as many jobs as you want – see next.)

If you have queued up multiple tasks and then run out of fuel, you will get an announcement similar to:

> "**Urist McFuelUser cancels job: needs refined coal.**"

Note that a forge or glass furnace *will* let you add tasks if you have no fuel, and only once a dwarf arrives and finds they cannot complete that task will you get the announcement to that effect. You will get one announcement for each un-fueled task that is unable to be completed. Jobs are canceled when there is no fuel.

When you get either of these messages, you need more fuel – either charcoal or coke will serve equally well.

## Magma facilities

Magma replaces conventional fuel for magma smelters, magma forges, magma kilns and magma glass furnaces. No fuel is needed, nor can it be used, for activities at these facilities. Note that you will still need charcoal or coke as a reactant for smelting bars of pig iron and steel. (And see next section.)

## Pig iron and steel production

When smelting pig iron or steel at any location, one unit of either charcoal or coke is required in the reaction as a source of carbon. Again, there is no distinction – both charcoal and coke serve equally well in the production of bars of either. This is in addition to the unit of fuel that is needed to power the furnace at conventional (non-magma) smelters.

## See also

- Smelting
- Fuel industry

    [MATERIAL:COAL] - reconstructed from data extracted from memory
        [STATE_COLOR:ALL:BLACK]
        [STATE_NAME_ADJ:SOLID:coal]
        [STATE_NAME_ADJ:SOLID_POWDER:coal powder]
        [STATE_NAME_ADJ:SOLID_PASTE:coal slush]
        [STATE_NAME_ADJ:SOLID_PRESSED:pressed coal]
        [BASIC_COLOR:0:1]
        [BUILD_COLOR:0:0:1]
        [TILE_COLOR:7:7:1]
        [MATERIAL_VALUE:2]
        [SPEC_HEAT:409]
        [IGNITE_POINT:11440]
        [SOLID_DENSITY:1346]
