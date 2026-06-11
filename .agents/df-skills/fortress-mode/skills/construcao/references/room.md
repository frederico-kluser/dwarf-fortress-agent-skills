# Room

> Fonte: [Room](https://dwarffortresswiki.org/index.php/Room) — Dwarf Fortress Wiki (GFDL/MIT)

A functional **room** is a contiguous area extending out from a piece of furniture that defines the room, created when the room is *defined from* that piece of furniture. A room, as the game understands it, only exists when specifically defined from a specific piece of furniture. For example, a small chamber with a bed in it is not yet a bedroom; you have to select the bed and *define* a bedroom from it in order for it to be recognized as a "room" with a specific function, as opposed to just another hollowed-out area of your fortress, same as any tunnel or mined out vein of ore. Only one room can be defined from any one piece of furniture, and there are reasons why you don't want the area of designated rooms to overlap (see below).

When sizing a room, the game will display the tiles which are currently included in the room. Each of those tiles is considered part of the room, and will contribute to both the room's value and its effectiveness. The room does **not** have to be enclosed by walls, but surrounding walls do have an effect on room value. It is possible to define several such rooms in one actual enclosed space; they may even overlap, although this comes at a penalty to the room's value. The maximum size of a **room** is 60×60 tiles.

## Creating

To create a room, you must first have built something capable of supporting a room from the uild menu, such as a table or bed. Then you must select the completed item in question with the command and choose to create a room. The room's radius extends outward in a rectangle, but will stop when it hits walls or external doors. If you first build the door to create a closed space, then the game will define the room, so you won't need to resize it unless it is very big.

If you want a room definition to expand through a door and into the space beyond, you can set the door to "internal" in the door's menu. Rooms do not have to be blocked off on all sides, and can even overlap, but for various reasons you will usually want to avoid overlapping rooms and give them proper boundaries.

In general, you only need to define a room from *one* object in the room. For instance, a communal dining room is defined from one table -- just give the room a large enough radius to cover the whole space.

Rooms cannot span z-levels; when you define a room it can only be on a single level.

## Room types

| Room type | Designated from |
|----|----|
| Tomb | Coffin |
| Barracks | Bed, cabinet, containers, weapon rack, or armor stand |
| Dormitory | Bed |
| Dining hall | Table |
| Bedroom | Bed |
| Office | Chair |
| Meeting hall | Well |
| Zoo | Cage |
| Memorial hall | Memorial slab |
| Sculpture garden | Statue |
| Jail | Metal cage, Restraint |
| Museum | Pedestal |

## Assigning

Rooms can be assigned to specific dwarves. When dwarves have their own room, happy thoughts occur when they sleep in it (alternatively, unhappy thoughts can occur when they do not have their own room to sleep in). Also, most nobles require an assignment to a room.

If you assign two or more rooms of the same type to a dwarf, the value of the piece of furniture that defines the room determines which room the dwarf will prefer to use. For example, if you give a dwarf two bedrooms, the dwarf will prefer to use the room with the higher quality bed, regardless of the comparative quality values of each room.

You can assign rooms to dwarves manually or automatically. If a dwarf (who does not already have a room) is ready to sleep and there is an unassigned room available, it will be spontaneously claimed by that dwarf. Married couples will share a bedroom, with the exception of some nobles.

## Locations

Rooms can be assigned to a location—such as a bedroom being assigned to a tavern as a rented room—from the ocation menu when a room is selected with .

## Quality

Most dwarves don't have high expectations when it comes to rooms - a communal dining room and dormitory are enough for the general populace, though making that dining room high-quality and giving them individual quarters will give them happy thoughts, helping to avoid tantrums. Nobles, on the other hand, require rooms of a particular minimum quality that contain certain furniture. Not meeting these demands will make them stressed, and may prevent them from functioning at their full capacity.

Room quality is determined by the total value of the room's floor and walls, plus the value of any furniture or other constructions in the room. If the floor area of two or more rooms overlap, each such room is reduced in value by 75%, but a wall can be part of multiple rooms without causing a decrease in value. Doors not marked as internal are not counted towards the value of any room, though they can separate rooms without the 75% loss of value. Note that this penalty is only applied *once*. There is no difference in value between a piece of furniture shared by two rooms, or by forty.

A room that is not entirely enclosed by walls suffers a partial value penalty to the total value of the room tiles (including the item designating the room), but not to any other items placed in the room.\* Thus, if a room is not going to be fully enclosed by walls, it's best to use your low-value item (if you have one) to designate the room.

Room quality levels can be viewed in the **R**oom/Building List () screen.

| Bedroom name | Dining room name | Office Name | Grave Name | Numeric Value |
|----|----|----|----|----|
| Meager Quarters | Meager Dining Room | Meager Office | Grave | 1 |
| Modest Quarters | Modest Dining Room | Modest Office | Servant's Burial Chamber | 100 |
| Quarters | Dining Room | Office | Burial Chamber | 250 |
| Decent Quarters | Decent Dining Room | Decent Office | Tomb | 500 |
| Fine Quarters | Fine Dining Room | Splendid Office | Fine Tomb | 1000 |
| Great Bedroom | Great Dining Room | Throne Room | Mausoleum | 1500 |
| Grand Bedroom | Grand Dining Room | Opulent Throne Room | Grand Mausoleum | 2500 |
| Royal Bedroom | Royal Dining Room | Royal Throne Room | Royal Mausoleum | 10000 |

Note: unassigned (or communal) rooms may be referenced by other descriptors, such as the happy thought "... dined in a legendary dining room ...".

(\* See forum thread for full discussion)

## Increasing room value

Making a large room, so that it has more floor and wall space, is an easy way to start out a high-quality room, as is forming the room with natural walls of valuable stone like limestone or obsidian (to make a *really* valuable room, put it in a magnetite cluster) or keep an eye out for gem clusters. (Note that mined tiles now revert to the base layer material, but a ruby pillar in the middle of a room still adds substantial value.) Once a room has been mined out, its value can be increased by smoothing and engraving the floor and walls.

Afterwards, placing valuable furniture (Preferably encrusted with gems or artifact quality) is an option for increasing value, but not the only one. Constructions (including workshops) inside a room increase a room's value, so you can use non-furniture artifacts in a construction to increase room value:

| Type | Building |
|----|----|
| Weapon | Weapon trap |
| Barrel | Dyer's shop, Ashery |
| Bucket | Dyer's shop, Ashery, Well\* |
| Mechanism | Lever, Gear assembly, Trap, Well\* |
| Chain | Restraint, Well\* |
| Anvil | Forge |

*\* - gains additional quality from skilled architecture and construction*

Weapon traps are an excellent way to increase room value while being conservative with space: One trap can contain 10 valuable components plus a mechanism, and the mechanism can be encrusted with gems.

Also, Levers have the special property that they can be used to stack an unlimited number of mechanisms, all of which count towards room value, in one tile. To add mechanisms simply link the lever to a deconstructible building such as a cage and pull the lever — one of mechanisms used for the link will remain in the lever. You can repeat this process as many times as you want until you increase the room's value to the desired level.

## View Rooms/Buildings

The command will bring up a list of all rooms, activity zones, stockpiles, and built furniture. It can be a very long list!

Rooms which have overlap (reducing their value) will be highlighted in red.

## See also

- Forum thread: Room Values - !!SCIENCE!! - The mathematics to help calculate room value.
- FAQ: How do I increase the value of a room?
