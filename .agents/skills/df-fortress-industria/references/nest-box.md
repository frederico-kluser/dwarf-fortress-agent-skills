# Nest box

> Fonte: [Nest box](https://dwarffortresswiki.org/index.php/Nest_box) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **b - o - f - n**
- **Job Requirement**
- **Food hauling**
- **Construction**
- **Materials:** Jobs
- **Wood Metal Stone Glass:** Woodcrafter Metalcrafter Stonecrafter Glassmaker
- **Purpose**
- **Producing eggs Producing poultry (with male present)**

!!UNKNOWN!!  · xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

A **nest box** is a 1×1 building that a tame egg-laying creature will claim and use to lay eggs in, once created and placed.

## Creation

A nest box is created using a single piece of wood or stone at a craftsdwarf's workshop, a single bag of sand (and optional rock crystal/pearlash) at a glass furnace or magma glass furnace, or a single bar of metal at a metalsmith's forge or magma forge. Unplaced nest boxes are stored in the tool section of a finished goods stockpile.

- To create one at a Craftdwarf's workshop, select wood products and choose "Make wooden Nest Box", or select rock products and choose "Make rock Nest Box".
- For a glass nest box, choose green/clear/crystal glass, then select "Make *type* glass Nest Box".
- For either forge, select "other objects", choose metal and then - "Make *metal* Nest Box".

## Construction and use

Once created, the nest box is then built as a Workshop of type farmer as a nest box (bofn), and will not block movement. The box will then be claimed by an egg-laying animal when it is ready to lay eggs. The animal that claims the nest box will periodically lay eggs into the nest. This process is very quick (\<1 day) and the eggs are ready to be collected immediately if they are to be cooked, but require time to hatch if you wish to start a breeding program.

If dwarves have access to the nest, a dwarf with the food hauling labor enabled will then remove the eggs and take them to a food stockpile and the animal will vacate the nest until it is ready to lay again. If a dwarf does not collect the eggs, the animal will remain on the nest box until the eggs hatch, after which it will also vacate the nest box until it is ready to lay again. In either situation, the nest box remains claimed by the animal. To free the nest for rapid turn around of eggs from a single box, deconstruct the nest after the eggs are collected or hatched and rebuild it - a different animal, ready to lay, will claim the nest box and immediately lay a clutch of eggs.

## Fertilized eggs

A nested female will lay eggs regardless of the presence of a male of the same species, however the eggs will not be fertilized unless a male is present. Hatching does not require a male to be around, once the eggs are fertilized and laid. If a male is present, the eggs may be fertilized and will hatch if the dwarves can be prevented from collecting them out of the nest box and hauling them to be eaten. To achieve this, eggs can be forbidden, or access to the nest box can be blocked with locked doors, or eggs can be forbidden as a cooking ingredient in the kitchen menu and disabled in all food stockpiles reachable from the nest. Nested females will stay in the nest box until a fertilized egg hatches, otherwise it will leave unfertilized eggs behind. Eggs do not appear to go rotten and can be collected and cooked after two or more seasons without generating miasma.

When the eggs are harvested from an occupied nest box, the female bird will leave the box, making it unoccupied once more. If you have a stockpile set to automatically receive eggs, then it is very likely that all your nest boxes will appear to be empty.

### Incubation Chamber

A simple way to make sure that eggs can hatch without having dwarves try to make omelettes out of them is to build incubation chambers for your female birds.

1.  Build 1×1 rooms, with lockable doors.
2.  Put one nest box in each room.
3.  Create a 1×1 pasture zone on top of the nest box, and assign one female egg-layer to it. She should claim the nest box when she is ready to lay eggs.
4.  Pasture or chain at least one male of the species somewhere that females can reach them. It needn't be close to the nest box.
5.  When you want the eggs to remain undisturbed, lock the door to the room.

If the eggs are fertile, you should eventually get a message about eggs having hatched. When you do, go to the nest box and unlock the door so the crowded chicks can get out (crowded animals will fight, and if they do, you may lose a chick or two in the melee; luckily they are always much smaller than their mother and unlikely to hurt her.)

It's a good idea to keep a cage nearby to assign newly hatched chicks to, so they won't get in the way and lower your FPS. When they are grown, they can be reassigned to pastures for breeding or egg-laying, or butchered.

## Forging and Melting

- Metal nest boxes cost **one** metal bar to forge, or **one** adamantine wafer.

- When a nest box is melted down, it will return **0.3** metal bars/adamantine wafers for an efficiency of **30%**

## Bugs

It should be noted that most domestic birds have tremendous reproductive potential, and a few species of breeding birds can cause a population explosion that rivals even the deadliest of catsplosions. Several species other than birds, such as cave crocodiles and crundles, are also prolific egg-layers, such that entire fortresses can be fed with egg production. It is unclear whether this behaviour is a bug or a feature, as the indicated clutch sizes in the raws are meant to match those of real life - and are sometimes *lower* in the case of reptiles.

Elk birds are both grazers and egg layers. Females left undisturbed near a nest box will probably starve themselves to death (certainly, if there are no males available). Bug:4637 A possible workaround is to assign the bird a pasture close to the nest, but not including it, so that dwarves with Animal hauling on would pasture the bird now and then, then she would return.\[Verify\] Eggs do not require continuous presence, only return before timeout (link).

Aquatic creatures (such as sea serpents) refuse to use a submerged nest box, which makes breeding impossible.Bug:4105

"Is *that* where all that damn chirping is coming from?!"

    [ITEM_TOOL:ITEM_TOOL_NEST_BOX]
    [NAME:nest box:nest boxes]
    [VALUE:10]
    [HARD_MAT]
    [TOOL_USE:NEST_BOX]
    [TILE:8]
    [SIZE:1000]
    [MATERIAL_SIZE:1]
    [CONTAINER_CAPACITY:2000]
