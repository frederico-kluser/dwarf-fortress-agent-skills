# Weight

> Fonte: [Weight](https://dwarffortresswiki.org/index.php/Weight) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Weight**, or sometimes more correctly termed **mass**, is an item property, and is measured in the unit *Γ*, also sometimes known as *urists*, or more commonly as the *kilogram*, its equivalent real-life unit.

Weight is largely used by the game to determine how fast someone or something should move, due to encumbrance effects and carry weight restrictions; to calculate damage, since object mass factors into impact momentum; and to some extent to make temperature calculations, as mass factors into heat capacity. Note that, for DF, weight and mass are currently indistinguishable because, as it stands, DF gravity is uniform both across the whole universe and from world to world and buoyancy isn't implemented.

Weight is displayed as a quantity associated with an item. Weight calculation is not entirely straightforward, since each item category — or sometimes even individual items — have their own formula for determining weight.

In adventure mode (where weight is referred to as "burden"), carrying too much weight in a character's inventory will cause them to move more slowly, the more they carry beyond their limits. When this happens, an icon appears above the inventory icon. Movement speed is reduced based on how much you exceed your carrying capacity, it will never reach zero, however, even if you are carrying hundreds of units above your carrying capacity. Characters can carry more the higher their strength attribute is - naturally, stronger, larger characters (such as an elephant man) are able to carry more.

## Weight Calculation

The general form for calculating weight in DF is to take the material density (as found in the raws) multiplied by the item's volume.

Weight (in Γ) = Density (in kg/m3) \* Volume (in cm3) / 1,000,000 (cm3/m3)

Internally, all custom volume/capacity numbers are rounded *down* to the nearest multiple of 10 - thus, if you define a tool with \[SIZE:15\], it will actually behave as if you had specified \[SIZE:10\].[1]

An item's volume is also used to determine workshop clutter as well as how many items can fit into a container.

## Assorted item weights

Weight displayed in-game is rounded down to a whole number.

|  |  |  |
|----|----|----|
| Item | Weight in Γ(kg) | Notes |
| Iron anvil | 78.5000 | Same as a steel anvil. |
| Aluminum bar | 16.2000 | Least dense normal metal. |
| Steel bar | 47.1000 | Same as an iron or pig iron bar. |
| Platinum bar | 128.4000 | Most dense metal. |
| 1 Copper coin | 0.0893 | Weight per coin varies with stack size, see Size for details. |
| 500 Copper coins | 2.7683 | This is 0.0055366 per coin, but that varies with stack size. |
| 500 Silver coins | 3.2519 | This is 0.0065038 per coin, but that varies with stack size. |
| 500 Gold coins | 5.9892 | This is 0.0119784 per coin, but that varies with stack size. |
| Feather (wood) barrel | 2.0000 | Least dense wood, found only in good biomes. |
| Willow barrel | 7.8000 | Least dense common wood, found near water in many biomes. |
| Tunnel tube barrel | 10.0000 | Least dense cavern wood, found only in lower caverns. |
| Tower cap barrel | 12.0000 | Same as a barrel of acacia, ash, fungiwood, goblin-cap, mahogany, pear, or spore wood. |
| Blood thorn barrel | 25.0000 | Most dense wood, found only in lowest caverns. |
| Jet block | 7.9200 | Least dense non-economic stone. |
| Shale block | 13.5000 |  |
| Cinnabar block | 48.6000 | Most dense non-economic stone. |
| Sheep cheese | 1.2000 | All cheeses seem to use the default density of 1200 kg/m3. |
| Willow large pot | 1.9500 | Least dense common wood, found near water in many biomes. |
| Tower cap large pot | 3.0000 | Same as a large pot of acacia, ash, fungiwood, goblin-cap, mahogany, pear, or spore wood. |
| Blood thorn large pot | 6.2500 | Most dense wood, found only in lowest caverns. |
| Jet large pot | 6.6000 | Least dense non-economic stone. |
| Earthenware large pot | 6.8000 | Must be glazed to hold liquids (or maybe any food). |
| Stoneware large pot | 10.0000 | Does not need glazing. |
| Shale large pot | 11.2500 |  |
| Porcelain large pot | 12.0150 | Not an unlimited resource like other ceramics. |
| Glass large pot | 13.0000 | All three types of glass have the same density. |
| Cinnabar large pot | 40.5000 | Most dense non-economic stone. |
| Feather log | 5.0000 | Least dense wood, found only in good biomes. |
| Willow log | 19.5000 | Least dense common wood, found near water in many biomes. |
| Tunnel tube log | 25.0000 | Least dense cavern wood, found only in lower caverns. |
| Tower cap log | 30.0000 | Same as a log of acacia, ash, fungiwood, goblin-cap, mahogany, pear, or spore wood. |
| Blood thorn log | 62.5000 | Most dense wood, found only in lowest caverns. |
| Jet stone | 132.0000 | Least dense non-economic stone. |
| Shale stone | 225.0000 |  |
| Cinnabar stone | 810.0000 | Most dense non-economic stone. |

## See also

- Density
- Size

|  |
|----|
| "Weight" in other / Languages / Dwarven / : / âl / Elven / : / eba / Goblin / : / deslo / Human / : / ketas |
