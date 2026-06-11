# Melt item

> Fonte: [Melt item](https://dwarffortresswiki.org/index.php/Melt_item) — Dwarf Fortress Wiki (GFDL/MIT)

Metal items can be **melted** at a smelter using the furnace operator labor, to recover some of the metal they were made of. Decorations of a different metal are not recovered or considered; the metal recovered is the specific metal that the basic item was listed as being made from. The percentile return is fixed and known for each item type, and ranges from 10%-150% (or more), depending on the item. Higher skill levels in furnace operator speed up the process, but have no effect on the percentile return. \_\_ToC\_\_

## Return

Recovered metal is measured in tenths (0.1) of a full bar, and those fractions of a bar of each separate metal are saved at the smelter where the item was melted. Fractional bars are not "shared" between smelters, nor do they exist as usable objects as is. When 10/10ths of a type of metal are accumulated at the same smelter, 1 bar of that metal is produced. If the smelter is torn down or destroyed, all fractions are lost.

*Example:*

- If 2 items, worth .4 bars each, of the same metal are melted at the same smelter, that smelter now has .8 bars (2 x .4) of that specific metal waiting in it. Not enough to use - yet...
- If a similar item of a *different* metal is then melted there, that smelter would still have .8 bars of the first metal, and .4 bars of the second metal.
- If a similar item of the *first* metal is then melted at a *different* smelter, that other smelter will have .4 of that metal, and have no connection to the fractions in the first smelter.
- If *(finally!)* a 3rd, similar item of the first metal is melted at the first smelter, that adds another .4 bars to the .8 waiting there. This gives a total of 1.2 bars of that type of metal, meaning 1 bar of that metal is produced, ready for forging or other use, and .2 of a bar is waiting (plus the .4 of the second metal, also waiting).

It is most efficient to designate one smelter as a "melting" smelter (or for one metal type), to guarantee that fractions will add up effectively. This becomes less important as more bars of a particular metal are accumulated.

## Designating items to melt

To mark an item for melting when it is:

:\* On the **ground**: Click the tile the item is on, then if there is more than one item there, click the tab of the item on the right edge of the sheet window, and click the melt button.

:\* In a **workshop**: Click one of the tiles the workshop, find the item in the list of items in that workshop, and click the melt button.

:\* **Held** by a dwarf: View the dwarf's sheet, select the Items tab, find the item in the list, click the button to view the item's sheet, and click the melt button.

:\* Inside a **container**: Display the container's item sheet, find the item in the list of items in that container, and click the melt button.

:\* In the **stocks** menu: Type or click the Stocks button, then either:

:\*\* click the filter input at the top and enter text to match the item, then click the melt button for the desired item.

:\*\* select the item category, scroll to the item, and click the melt button.

If the item is designated for melting and forbidden then the item will **not** be melted.

This only marks which items will be melted - the job-order will still need to be made at a smelter.

## Melting the items

Items designated to be melted will be left alone until the "Melt a metal object" job is queued at a Smelter. Melting down an object requires the Furnace operator labor (and consumes a unit of fuel for a non-magma smelter).

The job gives the same experience to the furnace operator skill, regardless of % yield of the item melted.

If there are items in a container that is being melted, the items will be placed inside the smelter when the container is destroyed.

## Yield

Testing is incomplete, but preliminary results show a yield of 0.3 bars\*the object's material size for anything that has a material size, or 1 bar for most furniture (regardless of size).

Note that the Efficiency column is only accurate for ordinary metals - when using adamantine, the number of wafers required comes from the "Material size" column instead of "Bars to make", so if that number is larger, the efficiency will be reduced accordingly. For coins however, the number is accurate for adamantine, which only requires 1 wafers and returns 1.1 wafers when melted.

Note also that some items are always produced in twos (gauntlets, boots) or threes (flasks, goblets), or (in the case of ammo) stacks of 25 at a time, or (for coins) 500 at a time. In the case of crafts, from 1 to 3 are produced. These are shown as "1/x" below, although a single job will never use less than one bar, nor produce less than the pair/trio/etc. of items.

| Item | Material size | Bars to make | Bars returned | Efficiency |
|----|----|----|----|----|
| Armor (Armorsmith) |  |  |  |  |
| Cap | 1 | 1 | 0.3 | 30% |
| Helm | 2 | 1 | 0.6 | 60% |
| Gauntlet | 2 | 1/2 | 0.6 | **120%** |
| Leggings | 5 | 1 | 1.5 | ***150%*** |
| Greaves | 6 | 2 | 1.8 | 90% |
| Low boot | 1 | 1/2 | 0.3 | 60% |
| High boot | 2 | 1/2 | 0.6 | **120%** |
| Buckler | 2 | 1 | 0.6 | 60% |
| Shield | 4 | 1 | 1.2 | **120%** |
| Mail shirt | 6 | 2 | 1.8 | 90% |
| Breastplate | 9 | 3 | 2.7 | 90% |
| Weapons (made by Weaponsmith) |  |  |  |  |
| Crossbow | 3 | 1 | 0.9 | 90% |
| Mace | 3 | 1 | 0.9 | 90% |
| Spear | 3 | 1 | 0.9 | 90% |
| Short sword | 3 | 1 | 0.9 | 90% |
| War hammer | 3 | 1 | 0.9 | 90% |
| Battle axe | 4 | 1 | 1.2 | **120%** |
| Pick | 4 | 1 | 1.2 | **120%** |
| Ammo (full stack of 25) | \(1\) | 1 | 0.3 | 30% |
| Ammo (single bolt) | \(1\) | 1/25 | 0.1 | ***250%*** |
| Foreign Weapons |  |  |  |  |
| Blowgun | 2 | 1 | 0.6 | 60% |
| Bow | 3 | 1 | 0.9 | 90% |
| Dagger | 1 | 1 | 0.3 | 30% |
| Flail | 4 | 1 | 1.2 | 120% |
| Great axe | 5 | 1 | 1.5 | 150% |
| Halberd | 5 | 1 | 1.5 | 150% |
| Long sword | 4 | 1 | 1.2 | 120% |
| Maul | 5 | 1 | 1.5 | 150% |
| Morningstar | 4 | 1 | 0.9 | 90% |
| Pike | 4 | 1 | 1.2 | 120% |
| Scimitar | 3 | 1 | 0.9 | 90% |
| Scourge | 2 | 1 | 0.6 | 60% |
| Two-handed sword | 5 | 1 | 1.5 | 150% |
| Whip | 1 | 1 | 0.3 | 30% |
| Trap Components (Weaponsmith) |  |  |  |  |
| Giant Axe Blade | 5 | 1 | 1.5 | ***150%*** |
| Enormous Corkscrew | 5 | 1 | 1.5 | ***150%*** |
| Spiked Ball | 4 | 1 | 1.2 | **120%** |
| Large, Serrated Disc | 4 | 1 | 1.2 | **120%** |
| Menacing Spike | 5 | 1 | 1.5 | ***150%*** |
| Trap Components (Mechanic) |  |  |  |  |
| Mechanisms | \(3\) | 1 | 0.5 | 50% |
| Siege Equipment (Weaponsmith) |  |  |  |  |
| Ballista arrow | \(4\) | 3 | 0.5 | 17% |
| Ballista arrowhead | \(4\) | 3 | 0.5 | 17% |
| Tools (Metalcrafter) |  |  |  |  |
| Nest box | 1 | 1 | 0.3 | 30% |
| Jug | 1 | 1 | 0.3 | 30% |
| Pot | 1 | 1 | 0.3 | 30% |
| Hive | 1 | 1 | 0.3 | 30% |
| Minecart | 6 | 2 | 1.8 | 90% |
| Wheelbarrow | 6 | 2 | 1.8 | 90% |
| Furniture (Blacksmith / Metalsmith) |  |  |  |  |
| Anvil | \(9\) | 3 | 1 | 33% |
| Armor stand | \(9\) | 3 | 1 | 33% |
| Barrel | \(9\) | 3 | 1 | 33% |
| Bin | \(9\) | 3 | 1 | 33% |
| Blocks | \(4\) | 1 | 0.5 | 50% |
| Bucket | \(3\) | 1 | 1 | **100%** |
| Cabinet | \(9\) | 3 | 1 | 33% |
| Cage | \(6\) | 3 | 1 | 33% |
| Chair | \(9\) | 3 | 1 | 33% |
| Chest | \(9\) | 3 | 1 | 33% |
| Coffin | \(9\) | 3 | 1 | 33% |
| Crutch | \(3\) | 3 | 0.5 | 17% |
| Door | \(9\) | 3 | 1 | 33% |
| Floodgate | \(9\) | 3 | 1 | 33% |
| Grate | \(9\) | 3 | 1 | 33% |
| Hatch cover | \(9\) | 3 | 1 | 33% |
| Pipe section | \(9\) | 3 | 1 | 33% |
| Splint | \(2\) | 3 | 0.5 | 17% |
| Statue | \(9\) | 3 | 1 | 33% |
| Table | \(9\) | 3 | 1 | 33% |
| Traction bench | \(9\) | 3 | 1 | 33% |
| Weapon rack | \(9\) | 3 | 1 | 33% |
| Furniture (Metalcrafter) |  |  |  |  |
| Chain | \(4\) | 1 | 1 | **100%** |
| Furniture (Trapper) |  |  |  |  |
| Animal trap | \(3\) | 1 | 1 | **100%** |
| Other objects (Metalcrafter) |  |  |  |  |
| Amulet | (1/3 to 1) | 1/3 to 1 | 0.1 | 10% to 30% |
| Bracelet | (1/3 to 1) | 1/3 to 1 | 0.1 | 10% to 30% |
| Coins (stack of 500) | \(1\) | 1 | 1.1 | ***110%*** |
| Coins (stack of 1) | \(1\) | 1/500 | 0.1 | ***5000%*** |
| Crown | (1/3 to 1) | 1/3 to 1 | 0.1 | 10% to 30% |
| Earring | (1/3 to 1) | 1/3 to 1 | 0.1 | 10% to 30% |
| Flask | (1/3) | 1/3 | 0.2 | 60% |
| Figurine | (1/3 to 1) | 1/3 to 1 | 0.2 | 20% to 60% |
| Goblet | (1/3) | 1/3 | 0.2 | 60% |
| Instrument | \(1\) | 1 | 1 | **100%** |
| Toy | \(1\) | 1 | 0.2 | 20% |
| Ring | (1/3 to 1) | 1/3 to 1 | 0.1 | 10% to 30% |
| Scepter | (1/3 to 1) | 1/3 to 1 | 0.2 | 20% to 60% |

All melting yields for items *not* specified in the raws (weapons, armor, tools, etc.) are hardcoded.

Metal bars are able to be melted and remade into half a bar at a smelter. (Melt 1 tin bar, return as 0.5 tin bar + experience.)

### Exploit

Items that yield more than 100% can be used to increase the amount of a metal available by producing those items and then melting them down again, as many times as required. This is generally considered to be an exploit of an error in the game mechanics. However, using a dwarf with a high skill level to make the items will result in severe tantrums being thrown when all the ☼masterwork☼ creations start being melted, so it is best to utilize low-skill metalworkers and make sure their skill levels don't get too high to avoid masterwork items, or there will be tantrum spirals, fistfights, and/or lots of useless junk valuable trade goods lying around. (A workshop profile on the forge can be used to restrict production to dwarves below a certain skill level. Another option is to designate a nearby stockpile for meltable items that doesn't allow Legendary or Master items.) For multiplying weapons/armor-grade metals, forging and melting giant axe blades, large serrated discs, and leggings will yield a 50% gain per item; \*note that this does not work with adamantine, since adamantine goods require 3 times as many wafers, instead leading to a 70% loss per item.

## Bugs

- A number of items produce more metal when melted than they cost to produce.
- Designating items to be melted from the stocks screen can cause a crash.
