# Learning

> Fonte: [Learning](https://dwarffortresswiki.org/index.php/Learning) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

**Learning** creatures (those with the [`[CAN_LEARN]`](/index.php/Creature_token#CAN_LEARN "Creature token") creature tag) may increase their skills through practice and use; conversely, creatures that cannot learn will never experience a skill increase. `[CAN_LEARN]` and [`[CAN_SPEAK]`](/index.php/Creature_token#CAN_SPEAK "Creature token") are implied by [`[INTELLIGENT]`](/index.php/Creature_token#INTELLIGENT "Creature token"). Creatures with `[CAN_LEARN]` will improve their social skills when standing near other members of their own species, but not when standing near `[CAN_LEARN]` members of other species.

Creatures which can learn are considered intelligent for the purpose of assigning ethics. In general, your dwarves will refuse to butcher the remains of any intelligent creature, though they can be assigned to slaughter a tame intelligent creature. The butchered remains will not be consumed, and can be assigned a casket. However, the eggs, milk and cheese of intelligent creatures can be eaten as normal. It should be noted that butchering creatures with the `[CAN_LEARN]` tag is currently forbidden, whatever ETHIC parameters are given to your adventurers or civilization. Bug:9171 (see butcher for precisions)

While enemy or unaffiliated intelligent creatures have no needs, tame intelligent creatures need to eat and drink, and are unable to drink booze or use wells or flasks. If they have tags for dietary requirements, such as [`[GRAZER]`](/index.php/Creature_token#GRAZER "Creature token"), [`[BONECARN]`](/index.php/Creature_token#BONECARN "Creature token"), [`[CARNIVORE]`](/index.php/Creature_token#CARNIVORE "Creature token"), [`[HUNTS_VERMIN]`](/index.php/Creature_token#HUNTS_VERMIN "Creature token"), or [`[DIVE_HUNTS_VERMIN]`](/index.php/Creature_token#DIVE_HUNTS_VERMIN "Creature token"), they will not eat any food which does not satisfy these requirements.

Although intelligent creatures belonging to other civilizations will not breed, wild, native, or tame intelligent creatures will. Intelligent creatures do not breed as much as other wild creatures and need to be married if they are residents of your fortress, and at least 'marriage-compatible' if they are not. Intelligent creatures born into your civilization as pets will receive a Dwarven name at their time of birth.

Capturing and training an intelligent creature can lead to all sorts of weirdness as it's considered both a resident of your fortress with needs and moods and feelings just like your other dwarves, and one of your pets that requires constant training. In vanilla DF, only gremlins are concerned, though.

Tame intelligent creatures with the [`[BABY]`](/index.php/Creature_token#BABY "Creature token") tag which give live birth will hold on to their offspring until the baby grows into a child; but egg-layers will not nurse their hatchlings. Since intelligent creatures require food and drink, and babies cannot see to their own needs, `[BABY]` tags are not recommended for intelligent egg-layers.

|  |
|----|
| "Learning" in other / Languages / Dwarven / : / turel / Elven / : / ridethe / Goblin / : / sobus / Human / : / cando |
