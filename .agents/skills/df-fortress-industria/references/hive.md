# Hive

> Fonte: [Hive](https://dwarffortresswiki.org/index.php/Hive) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Construction**
- **Used for**
- **Beekeeping**
- **Browse other items**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

More honey than you'll ever care about. 🐝

A **hive** is a tool and building that stores honey bee colonies. It is used in the beekeeping industry for the production of honeycombs and royal jelly, which can be processed into usable items. Citizens with the beekeeping labor enabled handle the building, removal, and management of hives. By default, the beekeeping labor is enabled for every dwarf in the fortress, unless specified by a work detail.

In ASCII graphics, hives use the same character as logs. As an item, they have the color of their material, but built ones are displayed as yellow.

## Manufacturing

Hives can be made out of wood, stone, metal, glass, or ceramic. Each material is created from their respective workshops by their appropriate labors. Hives are categorized as "Tools" in finished goods stockpiles.

### Forging and melting

- Metal hives cost **one** metal bar to forge, or **one** adamantine wafer.
- When a hive is melted down, it will return **0.3** metal bars/adamantine wafers for an efficiency of **30%**.

## Building and removal

Hives can be built using b+o+f+h. For hives to produce honey, they must be built adjacent to (or on) an above ground tile. Subterranean hives can still store colonies but will not make products.

Removing a hive via its building interface returns the hive and any items inside it, including the colony, which is released as a single honey bee that eventually disappears if left outside. Removed honeycombs can be collected and hauled, but any royal jelly is spilled onto the ground and wasted.

## Settings

The hive's settings can be found by clicking on a constructed hive to open its interface. There are two options which control beekeepers from doing certain jobs with the hive:

**Install colony when ready.** This setting is enabled by default, and will cause a beekeeper to install a colony in this hive when one becomes available, either from a wild colony or a hive colony that is ready to split. Changing this setting to **Do not install colony** will not allow the hive to accept new colonies. Preexisting colonies in the hive are not affected.

**Gather any products.** This setting is enabled by default, and allows beekeepers to gather honeycombs and royal jelly from the hive, destroying the colony. Changing the settings to **Do not gather products** will prevent beekeepers from gathering the products inside the hive, leaving the colonies alive so they can be saved for splitting.

The settings also display additional information about the hive: whether it has outdoor access or not (relating to above ground and subterranean tile attributes, which affect honey production), if the colony is ready to be split, and if there are too many colonized hives on the map, which affects production speed.

## Function

*Further information: Beekeeping industry § Hive management*

ToggleA hive that has produced royal jelly and honeycomb

Items in the hive can be seen by clicking on it to open the hive interface. Each hive can store a colony, which is represented as a stack of live honey bees. Colonies are collected from the wild or by splitting colonies from other hives. Three months after installation, colonies become Ready to be split, which allows them to be used to install other hives. It produces one honeycomb and royal jelly after six months after installation, unless the colony count limit was exceeded. Once both items are produced, a beekeeper with an empty jug goes to gather the items, storing the royal jelly in the jug. Beekeepers leave both the freed honeycomb and jug of royal jelly in the hive, and food haulers carry them to a stockpile. When a hive's products are gathered, the colony is destroyed, and the hive requires a new colony in order to produce again.

Colonies used to install other hives are not destroyed after installing. They need another three months to become ready to split again.

Colony size typically ranges between 10,000 and 20,000. The size of a colony does not affect production or its readiness to split. The number of bees is static and does not change over time, even after splitting. When beekeepers "split" a colony, they do not actually separate a portion of it; instead, they duplicate the old colony and haul away a new stack of live bees. Both the old and new stack will contain the same number of bees, and the number of bees in the old hive remains unchanged in the process.

When the total number of colonized hives in a fortress reach over forty, the chance of production decreases as indicated by the warnings Too many hives and Output restricted seen in the building settings of colonized hives. When the number of colonies reach sixty, the warning turns red (Too many hives) and products stop appearing. The limits do not affect the duration it takes for colonies to become ready to split, and hives can still be installed with new colonies; just nothing more is produced by hives until the number of colonies is reduced back below 60. Flowers and other surrounding vegetation do not affect production. The surroundings, weather, and the seasons have no effect on the colony or honey production.

## Hazard

Honey bee workers spawn from colonized hives and will occasionally sting passersby. Honey bee workers die and leave remains after stinging. Placing a zone near colonized hives puts idle citizens, visitors, and animals at high risk of being stung. Honey bee stings are reported in the announcements under the icon  / ·! in yellow text.

Honey bee stings cause strong swelling and slight pain. They are relatively harmless and inconsequential for dwarves - they do not even produce a bad thought. Bee stings are not recorded as wounds, but the health screen will display "Slight pain" for the stung dwarf, which can trigger a "recover wounded" task. This can trigger good thoughts about being rescued and resting, even though the hospital stay is instantaneous.

    [ITEM_TOOL:ITEM_TOOL_HIVE]
    [NAME:hive:hives]
    [VALUE:10]
    [HARD_MAT]
    [TOOL_USE:HIVE]
    [TILE:22]
    [SIZE:2000]
    [MATERIAL_SIZE:1]
    [CONTAINER_CAPACITY:5000]
