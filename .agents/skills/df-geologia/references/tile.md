# Tile

> Fonte: [Tile](https://dwarffortresswiki.org/index.php/Tile) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*For a list of all tile characters used in DF, see Tilesets.*

**Tiles** are the square rectangular cuboids that form a map. They are *approximately* two meters long, two meters wide, and three meters high.[1] However, the physics calculations assume a tile size of 2.8 meters high and a tick rate of 10 ticks per second, and from the listed speeds (in km/h) and gaits (ticks per 100 tiles) and the tick rate of 10 ticks per second, a tile would be about 8×8 feet (2.4×2.4 meters). The horizontal cross-section of a 1×1 embark is 48×48 tiles; this is also the scale of overland travel tiles in adventure mode. 16×16 local tiles, the maximum embark size, covers a region map tile. A single region map tile (the maximum embark size) would have a cross-section of 768×768 embark tiles (approx. 6144 feet or 1873 meters across). As worlds can have between 17 and 257 region map tiles, a world in *Dwarf Fortress* is between 20 and 300 miles (32 and 481 kilometers) across with a maximum area of 89,434 square miles (231,632 kilometers squared)– which is about 4% smaller than the United Kingdom.

A tile consists of two sections—a wall section and a floor section, shown in cross-section like this:

    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒ -|
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒  |
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒  |--> Wall Section
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒  |
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒  |
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒ -|
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ----> Floor Section

When digging and building, this is important, since some designations and constructions will only be done in wall tiles and others will only be done in floor tiles.

## Stairs

Building a stairway consists of two elements: an up stair and a down stair, each element is built only in the matching tile section, across two z-levels, like this:

    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒ -|                                  -|
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒  |                                   |
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒  |--> Wall Section                   |--> Open Space
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒  |                                   |
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒  |                                   |
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒ -|                                  -|
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ----> Floor          ▓      ▓▓▓▓▓▓▓ ----> Down Stair
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒ -|                   ▒▒▒            -|
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒  |                     ▒▒▒           |
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒  |--> Wall Section       ▒▒▒         |--> Up Stair
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒  |                         ▒▒▒       |
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒  |                           ▒▒▒     |
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒ -|                             ▒▒▒  -|
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ----> Floor          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ----> Floor

An up-down stair, or building both up and down stairs in the same tile, works like this:

    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒ -|                   ▒▒▒            -|               -|
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒  |                     ▒▒▒           |                |
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒  |--> Wall Section       ▒▒▒         |--> Up Stair    | Up/Down
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒  |                         ▒▒▒       |                |  Stair
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒  |                           ▒▒▒     |                |
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒ -|                             ▒▒▒  -|                |
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ----> Floor          ▓      ▓▓▓▓▓▓▓ ----> Down Stair -|

## Walls

Both naturally-occurring and constructed walls span across two z-levels, the bottom wall section and floor and the top floor section:

                   -|
                    |
                    |--> Open Space Wall
                    |
                    |
                   -|
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ----> Floor       -|
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒ -|                 |
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒  |                 |
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒  |--> Wall Section |-->  Wall
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒  |                 |
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒  |                 |
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒ -|                 |
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ----> Floor       -|

Smoothed and engraved walls span across only one z-level, the bottom wall section and floor. The floor above the wall can become "open space" by two methods: felling a tree above the wall, and digging a down stair above the wall, which is technically "open" (by exposing the tile below).

                   -|                                                       -|
                    |                                                        |
                    |--> Open Space Wall                                     |--> Open Space Wall
                    |                                                        |
                    |                                                        |
                   -|                                                       -|
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ----> Natural or Constructed Floor                       ----> Open Space Floor (or Down Stair)
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒ -|                -|                      ▒▒▒▒▒▒▒▒▒▒▒▒▒▒ -|                -|
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒  |                 |                      ▒▒▒▒▒▒▒▒▒▒▒▒▒▒  |                 |
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒  |--> Wall Section |-->  Wall   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒  |--> Wall Section |-->  Wall
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒  |                 |                      ▒▒▒▒▒▒▒▒▒▒▒▒▒▒  |                 |
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒  |                 |                      ▒▒▒▒▒▒▒▒▒▒▒▒▒▒  |                 |
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒ -|                 |                      ▒▒▒▒▒▒▒▒▒▒▒▒▒▒ -|                 |
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ----> Floor       -|                      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ----> Floor       -|

## Supports and Fortifications

Unlike walls, supports span only one z-level, allow liquids and movement, and don't create a floor on top. Constructed fortifications are basically the same, but block movement as well. Note, however, that fully submerged (depth of 7/7) fortifications no longer block creature movement.

          ▒▒       -|                 |                                     -|                 |
          ▒▒        |                 |                      ▒▒▒ ▒▒▒▒▒▒ ▒▒▒  |                 |
          ▒▒        |--> Wall Section |-->  Wall   ▒▒▒ ▒▒▒▒▒▒ ▒▒▒  |--> Wall Section |-->  Fortification
          ▒▒        |                 |                      ▒▒▒ ▒▒▒▒▒▒ ▒▒▒  |                 |
          ▒▒        |                 |                      ▒▒▒ ▒▒▒▒▒▒ ▒▒▒  |                 |
          ▒▒       -|                 |                      ▒▒▒▒▒▒▒▒▒▒▒▒▒▒ -|                 |
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ----> Floor       -|                      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ----> Floor       -|

## Furniture

### Statues

Statues block normal movement, but not unintended movement (dodging, being thrown, swept by current, etc) nor do they block fluids.

    ▒▒▒▒▒░░░░▒▒▒▒▒ -|                 |
    ▒▒▒▒▒▓░░▓▒▒▒▒▒  |                 |
    ▒▒░░░▓▓▓▓░░░▒▒  |--> Wall Section |-->  Statue
    ▒░░▒░░▓▓░░▒░░▒  |                 |
    ▒▒▒▒░░▒▒░░▒▒▒▒  |                 |
    ▒▒░░░░▒▒░░░░▒▒ -|                 |
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒ -|                 |
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ----> Floor       -|

### Doors and Windows

Windows and doors both block fluids (doors only when closed).

    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒ -|                 |                     ▒▒▒▒▒▒▒▒▒▒▒▒▒▒ -|                 |
    ▒░░░░░░░░░░░░▒  |                 |                     ▒░░░░░░░░░░░░▒  |                 |
    ▒░░░░░░░░░░░░▒  |--> Wall Section |-->  Door  ▒░░░░░░░░░░░░▒  |--> Wall Section |-->  Window
    ▒░░░░░░░░░░░░▒  |                 |                     ▒▒▒▒▒▒▒▒▒▒▒▒▒▒  |                 |
    ▒░░░░░░░░░▒▒░▒  |                 |                     ▒░░░░░░░░░░░░▒  |                 |
    ▒░░░░░░░░░░░░▒ -|                 |                     ▒░░░░░░░░░░░░▒ -|                 |
    ▒░░░░░░░░░░░░▒ -|                 |                     ▒▒▒▒▒▒▒▒▒▒▒▒▒▒ -|                 |
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ----> Floor       -|                     ▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ----> Floor       -|

...

## Special Tiles

There are some naturally-occurring special tiles, these can't be recreated\[Verify\]:

### Murky pool tile

Occur on at least\[Verify\] 2 z-levels, as an open space wall section with an open space floor section, and in the lowest z-level another open space wall section (filled with water) with a murky pool floor section, the lower open space wall section can fill with rain water and during winter with an ice wall\[Verify\]

    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒ -|                                  -|
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒  |                                   |
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒  |--> Wall Section                   |--> Open Space Wall
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒  |                                   |
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒  |                                   |
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒ -|                                  -|
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ----> Floor                         ----> Open Space Floor (an Ice wall creates an Ice floor here)
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒ -|                   ~~~~~~w7~~~~~~ -|
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒  |                   ~~~~~~w6~~~~~~  |
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒  |--> Wall Section   ~~~~~~w5~~~~~~  |--> Open Space Wall (can be filled with Water or Ice)
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒  |                   ~~~~~~w4~~~~~~  |
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒  |                   ~~~~~~w3~~~~~~  |
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒ -|                   ~~~~~~w2~~~~~~ -|
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ----> Floor          ▓▓▓▓▓▓w1▓▓▓▓▓▓ ----> Murky Pool ----> 1/1 Water or Ice floor{{verify}

                                              w# = water level

### River

\[Verify\] under construction...

River Source tiles: generate infinite flowing water for both rivers and brooks??\[Verify\]

### Brook tile

Brook tiles occur on at least\[Verify\] 2 z-levels, as an open space wall section with a brook floor section, and in the lowest z-level another open space wall section (filled with water) with another brook *(or river source)* floor section, the lower open space wall section can fill with rain water\[Verify\] and during winter with an ice wall\[Verify\]

    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒ -|                                  -|
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒  |                                   |
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒  |--> Wall Section                   |--> Open Space Wall
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒  |                                   |
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒  |                                   |
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒ -|                                  -|
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ----> Floor          ▓▓  ▓▓  ▓▓  ▓▓ ----> Brook (freezing effects?[Verify])
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒ -|                   ~~~~~~w7~~~~~~ -|
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒  |                   ~~~~~~w6~~~~~~  |
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒  |--> Wall Section   ~~~~~~w5~~~~~~  |--> Open Space Wall (can be filled with flowing[Verify] water or Ice)
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒  |                   ~~~~~~w4~~~~~~  |
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒  |                   ~~~~~~w3~~~~~~  |
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒ -|                   ~~~~~~w2~~~~~~ -|
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ----> Floor          ▓▓  ▓▓w1▓▓  ▓▓ ----> Brook / River Source ----> 1/1 Water or Ice floor[Verify]

Brook tiles work like floor grates, can be walked on, fished through, allow fluids and missiles through, etc...

|  |
|----|
| "Tile" in other / Languages / Dwarven / : / bot / Elven / : / çile / Goblin / : / garspo / Human / : / lir |
