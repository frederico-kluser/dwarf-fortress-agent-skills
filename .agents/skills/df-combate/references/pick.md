# Pick

> Fonte: [Pick](https://dwarffortresswiki.org/index.php/Pick) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

A **pick** is a digging implement / weapon that can be forged (using the weaponsmithing labor) from most weapon-grade metals, such as copper, iron, bronze, bismuth bronze, steel, and adamantine, but not silver, (although other weapons can be forged from silver). Picks are essential for a properly-functioning fortress: miners require picks to strike the earth, dig tunnels, carve staircases and everything else related to the removal of rock and soil tiles. You will need to purchase or create picks on embark, as miners won't bring their own. Without picks, your dwarves will be stranded on the surface, forced to live like elves. As of version 53.07, digging speed is affected by both the miner's skill and the material of the pickaxe itself; quality of the tool is a 20% boost per level up to double (100% boost)[1].

Picks can also be used as weapons. They inflict EDGE type damage, tend to impale or dismember enemies, and gain damage bonuses dependent on the user's Mining skill level. Picks combine a velocity bonus with a narrow attack surface, making them on par with spears for penetration while inflicting broader wounds. The effectiveness of picks is often overestimated by newer players who tend to fall short on proper military training. When they then see the effects of skill by the single miner they've been ordering to mine stone day and night compared to their late start militaries on part-time schedules, they are amazed and imagine that the pick must be a superweapon. Another source of such beliefs is that the Pick seems to be a "superweapon" *on paper* - as it has Edge attack type, pretty small contact area (100), average penetration (4000) and 2.0x velocity - what, to the inexperienced eye, seems to be a mashup of the best qualities of the War hammer and Spear (which is close to truth, but novice players tend to overestimate the power of such a combination). Extensive testing that examines weapons *ceteris paribus* has revealed that it is very effective, but not in itself the best in every category.

While other weapons, given equal skills, are more effective against siegers and huge enemies, picks excel at killing undead, in particular armored undead. The main advantage and key thing that sets picks apart is that players can utilize mining quarries to increase the weapon skill of potential military dwarves faster than they can ascend to sparring status, although this comes at the opportunity cost of putting off the other skills you would in a sparring session, especially defensive, blocking and armor skills. An additional point in their favor is that it also results in a large number of miners in case you have a mega project in mind and need FPS-crushing amounts of stone quarried.

The quality and material are both important when using a pick as a weapon. Since a steel pick, just like every bladed dwarven weapon, can penetrate most armor, picks are effective against any foe, armored, forgotten elemental, bronze, or otherwise. Picks are slightly below average in terms of how many dwarves can wield them along with a shield. Some dwarves must use two hands, which makes them more similar to real-life (modern human) ice axes than actual pickaxes.

Note that military dwarves will never select a pick as a weapon if allowed "individual choice" - they must be specifically assigned picks as part of their uniform or on their equip screen.

## Forging and melting

- Metal picks cost **one** metal bar to forge, or **four** adamantine wafers.
- When a non-adamantine metal pick is melted down, it will return **1.2** metal bars, for an **efficiency of 120%**.
- When an adamantine pick is melted down, it will produce **1.2** wafers, for an **efficiency of 30%**.

|  |
|----|
| "Pick" in other / Languages / Dwarven / : / tekkud / Elven / : / mubara / Goblin / : / otez / Human / : / tekud |

    [ITEM_WEAPON:ITEM_WEAPON_PICK]
    [NAME:pick:picks]
    [SIZE:500]
    [SKILL:MINING]
    [TWO_HANDED:47500]
    [MINIMUM_SIZE:42500]
    [MATERIAL_SIZE:4]
    [ATTACK:EDGE:100:4000:strike:strikes:NO_SUB:2000]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
