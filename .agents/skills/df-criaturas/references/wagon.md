# Wagon

> Fonte: [Wagon](https://dwarffortresswiki.org/index.php/Wagon) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Biome**
- **Domesticated**
- **Attributes**
- **Genderless**
- **Cannot be tamed**
- **Size**
- **Max:** 12,000 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** Immortal
- **Becomes after death**
- **Wagon wood**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*This page is about the creature. For the structure, see Wagon (embark) "Wagon (embark)")*

*A rolling platform for carrying passengers or cargo.*

**Wagons** are special "creatures" used by human and dwarven caravans. Wagons have a much greater hauling capacity than pack animals, increasing the imported goods available to your fortress and the capacity for exported goods. Surprisingly, despite their capacity and being the only multi-tile creature, wagons are only 1/5th the size (volume) of a dwarf - no wonder they scuttle so easily.

Wagons require specific accommodations to reach your fortress: wagon-accessible paths must be three tiles wide, extend from natural-land tiles at the screen border to your trade depot, and cannot contain traps or pressure plates. If wagons are unable to find a path to your trade depot (or if you have not built a depot at all), they will bypass your site, and you will only be able to trade for what is available on the merchants' pack animals.

Wagons which are destroyed, abandoned, or scuttled will leave behind a unique type of wood: wagon wood. Since they count as creatures, dead wagons can be memorialized (though a ghostly wagon has not yet been observed).[1]

It is not possible for creatures to have a preference for wagons - even if they are given a [`[PREFSTRING]`](/index.php/Creature_token#PREFSTRING "Creature token"), their [`[EQUIPMENT_WAGON]`](/index.php/Creature_token#EQUIPMENT_WAGON "Creature token") status makes them exempt.

As stated by their raw files, they exist as creatures only temporarily, until moving siege engines are added to the game.

## Depot Accessibility

**There is not a tool to check wagon accessibility currentlyv50.11, the screenshots are from a previous version.**

Trade wagons will not visit your fort, unless you have a noble with a barony title or greater (count, duke, etc).

An accessible and an inaccessible wagon path. Below is how the paths are viewed with depot access turned on.

In order to appear alongside caravans, wagons must have an appropriate place on the map edge to spawn, and an unobstructed path to the trade depot.

Accessibility is calculated from your depot towards the map edges; even though you see a green area around your depot, it may not be accessible from outside. You need to make sure the path extends all the way to some edge of the map. The display is somewhat misleading, in that a one-tile wide green path is sufficient for the 3-tile wide wagons; the green Ws represent only the *center* of a wagon, although the whole 3×3 can fit around it - so a three-tile wide path, which can fit a wagon, will only show up as one-tile wide line of Ws. When the route they would take goes over hills (ramps), it's hard to eye whether it is continuous all the way to the edge of the map, so be sure you see the words "depot accessible" on the depot access screen.

As long as you have a 3-tile wide path to the depot that reaches *any* natural-land tiles at the edge of the map, wagons will be able to reach the depot. If there is only one path they can take, they will take that path. You can force them to enter and exit the map in an exact spot -- preferably very near your depot -- by erecting walls or digging channels so that all paths but the one you want them to take are blocked. Note that all caravans will prefer to enter the map at a wagon-accessible point, so this can also be used for elven caravans as well.

Wagons will not appear on non-natural surface tiles at a map edge (such as a "bridge to nowhere"), though they can sometimes be encouraged to leave the map edge in such a manner. Wagons will also delay appearing at the map edge if their intended location is currently blocked by any other creature, similar to migrants.

### Trade depots on different z-levels

If your trade depot is underground, there needs to be a ramp that is at least 3 tiles wide, so that the wagon can proceed to the next level. If this goes into your fortress, you may want to secure it somehow from attackers and unwanted critters, e.g. by using a bridge.

## Movement

Human merchants directing their wagons in a 3×3 channel.

When determining movement, a wagon has a 3×3 "footprint" (9 squares). However, for many purposes, only the center square is considered. Animals drawing the wagon are not considered for purposes of determining movement.

Wagons can move horizontally across/through:

- Ordinary open ground
- Small plants, e.g. grass, shrubs
- Constructed roads or floors
- Bridges
- Closed hatch covers, even if they are over open space
- Ramps (both "up" to the next z-level, and the empty hole over a ramp "down" to the next z-level below)
- Passable buildings (e.g. workshops or restraints)
- Creatures, apart from other wagons
- Gear assemblies and horizontal axles built on passable tiles

\
Wagons **cannot** move horizontally across/through:

- Open space below
- Boulders (can be smoothed to make them passable)
- Traps
- Pressure plates
- Any type of stair tile, apart from a down stair with a hatch cover on top
- Impassable buildings (e.g. statues)
- Doors, even if they are operated by lever and left open
- Drained murky pool or river tiles (constructing and, optionally, removing a floor or road on top will make them passable)
- Minecart Tracks

Wagons can move up or down z-levels via ramps, provided they do not have hatch covers on top. Wagons use different rules for movement on ramps - namely, they are able to ascend a ramp to a raised floor over empty space, but cannot cross the line of ramps while remaining at the same level. With some careful design it is possible to make bridges that control depot accessibility without actually allowing anything to cross them, or paths that can be traversed only by wagons but not dwarves or *vice versa*.

It may seem somewhat strange, but wagons \*\*are\*\* able to climb and descend 3×2 ramp tunnels (that is, a series of diagonally adjacent 1×3 up ramps going in the same direction). While climbing up and down these ramps, parts of the wagons can clip inside walls with apparently no ill effects. This is somewhat less strange when you consider that climbing down a (dwarf-usable) ramp always guarantees that the lower level cannot have at least 3×3 clearance, since at least one tile adjacent to the up ramp below must be a solid tile to allow the ramp to be climbed by normal units. This is likely the reason why wagons have more lenient ramp climbing rules and can climb such ramps even if the solid tile is missing (though this will cause non-wagons to be unable to use the ramps).

## Wagon-only entrances

Wagons are able to navigate through certain entrances which other (walking) creatures cannot. Specifically, wagons can climb ramps that walking creatures consider to be "unusable". By building a set of ramps which are exclusively unusable, you can send wagons on a direct route, while filtering all other traffic through your trap-covered route.

Note: Pack animals with caravans will not follow the "wagon only" route. However, that means your trapped route to your Trade Depot can be only 1 tile wide.

An example: [1]:

|     |     |     |     |     |     |     |     |     |     |     |     |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|     | Z   | =   | 0   |     |     |     |     | Z   | =   | \+  | 1   |
| ▓   | \+  | \+  | \+  | ▓   |     |     | ▓   | ▓   | ▓   | ▓   | ▓   |
| ▓   | \+  | ▲   | \+  | ▓   |     |     | ▓   | \+  | ▼   | \+  | ▓   |
| ▓   | \+  | \+  | \+  | ▓   |     |     | ▓   | \+  | \+  | \+  | ▓   |
| ▓   | ▓   | ▓   | ▓   | ▓   |     |     | ▓   | \+  | \+  | \+  | ▓   |
| ▓   | \+  | \+  | \+  | ▓   |     |     | ▓   | \+  | \+  | \+  | ▓   |
| ▓   | \+  | ▲   | \+  | ▓   |     |     | ▓   | \+  | ▼   | \+  | ▓   |
| ▓   | \+  | \+  | \+  | ▓   |     |     | ▓   | ▓   | ▓   | ▓   | ▓   |

Another example, which uses slightly less space (note: this particular entrance is *not* a wagon-only entrance and is usable by creatures able to jump).

|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|     | Z   | =   | \-  | 1   |     |     |     | Z   | =   | 0   |     |     |     |     |     |
| ▓   | ▓   | ▓   | ▓   | ▓   |     |     | ▓   | \+  | \+  | \+  | ▓   |     |     |     |     |
| ▓   | \+  | \+  | \+  | ▓   |     |     | ▓   | \+  | \+  | \+  | ▓   |     |     |     |     |
| ▓   | \+  | ▲   | \+  | ▓   |     |     | ▓   | ·   | ▼   | ·   | ▓   |     |     |     |     |
| ▓   | \+  | \+  | \+  | ▓   |     |     | ▓   | \+  | \+  | \+  | ▓   |     |     |     |     |
| ▓   | ▓   | ▓   | ▓   | ▓   |     |     | ▓   | \+  | \+  | \+  | ▓   |     |     |     |     |

Yet another example, which allow wagons to move between z-levels [2]:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
|  | Z | = | \- | 4 |  |  |  |  | Z | = | \- | 3 |  |  |  |  |  | Z | = | \- | 2 |  |  |  |  | Z | = | \- | 1 |  |  |  |  | Z | = | 0 |  |  |  |  |  |
| ▓ | ▓ | ▓ | ▓ | ▓ | ▓ |  |  | ▓ | ▓ | ▓ | ▓ | ▓ | ▓ |  |  | ▓ | ▓ | ▓ | ▓ | ▓ | ▓ |  |  | ▓ | ▓ | ▓ | ▓ | ▓ | ▓ |  |  | ▓ | ▓ | \+ | \+ | \+ | ▓ |  |  |  |  |
| ▓ | \+ | \+ | \+ | ▓ | ▓ |  |  | ▓ | ▓ | ▓ | ▓ | ▓ | ▓ |  |  | ▓ | ▓ | ▓ | ▓ | ▓ | ▓ |  |  | ▓ | ▓ | \+ | \+ | \+ | ▓ |  |  | ▓ | ▓ | \+ | \+ | \+ | ▓ |  |  |  |  |
| ▓ | \+ | ▲ | ▼ | ▓ | ▓ |  |  | ▓ | \+ | ▼ | \+ | ▓ | ▓ |  |  | ▓ | ▓ | \+ | \+ | \+ | ▓ |  |  | ▓ | ▓ | \+ | ▲ | \+ | ▓ |  |  | ▓ | ▓ | \+ | ▼ | \+ | ▓ |  |  |  |  |
| ▓ | \+ | \+ | \+ | ▓ | ▓ |  |  | ▓ | \+ | ▲ | \+ | ▓ | ▓ |  |  | ▓ | ▓ | ▼ | ▲ | \+ | ▓ |  |  | ▓ | ▓ | \+ | ▼ | \+ | ▓ |  |  | ▓ | ▓ | ▓ | ▓ | ▓ | ▓ |  |  |  |  |
| ▓ | ▓ | ▓ | ▓ | ▓ | ▓ |  |  | ▓ | \+ | \+ | \+ | ▓ | ▓ |  |  | ▓ | ▓ | \+ | \+ | \+ | ▓ |  |  | ▓ | ▓ | ▓ | ▓ | ▓ | ▓ |  |  | ▓ | ▓ | ▓ | ▓ | ▓ | ▓ |  |  |  |  |
| ▓ | ▓ | ▓ | ▓ | ▓ | ▓ |  |  | ▓ | ▓ | ▓ | ▓ | ▓ | ▓ |  |  | ▓ | ▓ | ▓ | ▓ | ▓ | ▓ |  |  | ▓ | ▓ | ▓ | ▓ | ▓ | ▓ |  |  | ▓ | ▓ | ▓ | ▓ | ▓ | ▓ |  |  |  |  |

## When do caravans bring wagons?

As of v50.05, there are two requirements for a caravan to bring wagons for their goods.

The first is that the civilization has access to wagons through their KILL_PLANT ethic response (which is why elves lack wagons), as well as wagon pullers through the COMMON_DOMESTIC_PULL token. Both of these tokens can easily be added to vanilla civs by modifying the game's raws, though the former will alter their behavior during trade.

The second is that the player's fort is either the current home of the monarch or that the site has been elevated to a landholding with an on-site living landholder such as a baron, count or duke. Currently, these landholder titles corresponding to player forts will never be inherited, so if the holder of the title dies and the player's fort is not the residence of the monarch, caravans will permanently stop bringing wagons.

Players using DFHack can work around the second issue by using the `gui/gm-editor` tool to edit the title assignment so that the title is reassigned to another (preferably less *dead*) historical figure.

Step by step instructions for fixing a corrupted or dead landholder position **as of v50.05 and DFHack 50.05-alpha3.1**:

1.  Backup your saves. The `gm-editor` tool can cause irreversible save file corruption.
2.  Select the unit you wish to make into a noble and run `gui/gm-editor` from the DFHack terminal or launcher. This will bring up a page where you can (s)earch for the unit's `hist_figure_id`. Write down this id, which from now on will be referred to as `desired_histfig_id` in this guide.
3.  Now that you have the required hist_fig_id, run `gui/gm-editor df.historical_entity.find(df.global.plotinfo.civ_id).positions.own`. This a list of **types** of titles your civilization can give out (e.g. monarch, duke). Find the entry with `code` equal to your desired position (e.g. `COUNT`, `DUKE`, `BARON`). Note the `id` for this entry, which from now on will be referred to as `desired_position_id` in this guide.
4.  Run `gui/gm-editor df.global.plotinfo`. (s)earch for both `civ_id` (write this down for later, we will call it `desired_civ_id`) and `site_id` (write down as well, we will call it `desired_site_id`).
5.  Run `gui/gm-editor df.world_site.find(df.global.plotinfo.site_id).entity_links`. Find the link here where `entity_id` is equal to `desired_civ_id`. This is the game's information for connections between your site and your civ. Write down the value in `position_profile_id`; we will refer this to `desired_position_assignment_id` in this guide.
6.  Run `gui/gm-editor df.historical_entity.find(df.global.plotinfo.civ_id).positions.assignments`. This is a list of **actual titles** given out by your civ. Find the entry where `id` is equal to `desired_position_assignment_id` (in these entries, confusingly, `id` is the position_assignment_id, and `position_id` is the id of the **type** of title in `positions.own` from step 3.) This entry is the actual created title for your site (e.g. "Count of Boatmurders"), while the entry from step 3 is essentially just the information for "A count". Here you can replace \`histfig\` and \`histfig2\` with `desired_histfig_id` from step 2. The game should immediately after this recognize the new noble and display them in the nobles screen, but the noble will **not** recognize this title in their `groups` tab until you follow the final steps.
7.  Run `gui/gm-editor df.historical_figure.find().entity_links`. This is essentially where civ-level information on the unit's `groups` tab is stored. Use Alt+i to insert a new value; enter the type name `histfig_entity_link_positionst` when prompted. Once the value is created, open it. Enter `desired_civ_id` from step 4 as `entity_id`, enter `100` for `link_strength`, enter `desired_position_assignment_id` for `assignment_id`. `start_year` is up to you; this is what legends will use to determine the date this character was elevated to a noble. The current year is the simplest option, though any year after the site's founding and where the desired noble is an adult will work fine.

Update **as of v51.10-beta and DFHACK v51.10-beta2**, I was able to figure out a VERY EXPERIMENTAL way to do this when the fortress has never had a baron(ness) before:

1.  For step five my site had a `position_profile_id` of `-1` likely due to the lack of a previous baron. Into this I put a `position_profile_id` I made up (in case it matters I used `8`). I made sure it wasn't in `df.historical_entity.find(df.global.plotinfo.civ_id).positions.assignments` because I don't believe a collision would be a good thing here.
2.  For step six I used alt+i and typed `entity_position_assignment` to add a new entry into the assignments list because my site did not have one. I filled in the `id` to be the `position_profile_id` I made up and the `position_id` to be the value retrieved in 3 for the `code` of the `BARON` position (`18` in my case). Finally, I filled in \`histfig\` and \`histfig2\` with my dwarf's `desired_histfig_id` from step 2.
3.  I used my new ID I made for `position_profile_id` as the `desired_position_assignment_id` for the rest of the instructions. After the final step my dwarf was indeed the baroness of the fort! I have not tested whether all the related things (like caravans) work or not yet.

"Now to get another wagon for NON-alcohol items."

## Bugs

- Wagons can become "stuck" in obstacles.Bug:5418
- Wagon pathing problems can result in caravan collisions.Bug:5687
- It's possible for a dwarf to have a preference for "wagon wood".Bug:3676
- Wagons are listed as "deceased" after being scuttled.
- Wagon despawns, becoming listed as "Missing" and causing the caravan to flee.

## Trivia

- If you happen to be playing *as* a wagon (presumably through some clever modding) in Adventurer mode, you can receive a message that you have been scuttled.

    [CREATURE:EQUIPMENT_WAGON]
        [DESCRIPTION:A rolling platform for carrying passengers or cargo.]
        [NAME:wagon:wagons:wagon]
        [CASTE_NAME:wagon:wagons:wagon]
        [CREATURE_TILE:'W'][COLOR:6:0:0]
        [EQUIPMENT_WAGON][COMMON_DOMESTIC]
        [NOT_BUTCHERABLE]
        [BODY:WAGON]
        [USE_MATERIAL_TEMPLATE:WOOD:WOOD_TEMPLATE]

        Wagons-as-creatures is most likely going to be replaced once moving siege engines are in, so we'll just use a generic "wood" material here instead of worrying about coding up race glosses again.

        [TISSUE:WOOD]
            [TISSUE_NAME:wood:wooden]
            [TISSUE_MATERIAL:LOCAL_CREATURE_MAT:WOOD]
        [TISSUE_LAYER:BY_CATEGORY:ALL:WOOD]
        [ITEMCORPSE:WOOD:NO_SUBTYPE:LOCAL_CREATURE_MAT:WOOD]
        [BODY_SIZE:0:0:12000]
        [ALL_ACTIVE]
        [TRADE_CAPACITY:15000]
        [MUNDANE]
        [ODOR_LEVEL:0]
