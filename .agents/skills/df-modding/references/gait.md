# Gait

> Fonte: [Gait](https://dwarffortresswiki.org/index.php/Gait) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

A **gait** is a mode of movement which a creature can use. In real life, the word only applies to movement on land; but in *Dwarf Fortress*, the term describes any mode of movement by a creature, including swimming, flying, and climbing.

In Adventurer mode, you can choose your preferred gait in the m movement menu, determining your speed.

## Gait Types

There are 5 different types of gaits: walking, crawling, climbing, swimming, and flying.

- Walking gaits are land-based gaits which require the creature to be standing up, and have more than half of their [`[STANCE]`](/index.php/Body_token#STANCE "Body token") body parts, e.g. legs, intact and working. They can be used to move across flat ground, and go up and down ramps and stairs.

- Crawling gaits are like walking gaits, except that they require neither standing up nor [`[STANCE]`](/index.php/Body_token#STANCE "Body token") body parts. They are much slower than walking gaits. Please note that an uninjured, slithering snake is considered to be using a walking gait, not a crawling gait: its body is its [`[STANCE]`](/index.php/Body_token#STANCE "Body token") body part. If a snake is injured in the body, it will revert to a crawling gait.

- Climbing gaits are used for moving up and down vertical surfaces, such as trees or walls, as well as for moving horizontally while supporting oneself against a vertical surface. In order to climb, a creature needs intact body parts to climb with: [`[GRASP]`](/index.php/Body_token#GRASP "Body token") body parts by default, or \[STANCE\] body parts if the creature has the [`[STANCE_CLIMBER]`](/index.php/Creature_token#STANCE_CLIMBER "Creature token") token. Stance climbers include cats and giant cave spiders.

- Swimming gaits are used for moving in the water. In order to swim, a creature needs either the [`[SWIMS_INNATE]`](/index.php/Creature_token#SWIMS_INNATE "Creature token") tag, or [`[SWIMS_LEARNED]`](/index.php/Creature_token#SWIMS_LEARNED "Creature token"), [`[CAN_LEARN]`](/index.php/Creature_token#CAN_LEARN "Creature token") and skill in swimming.

- Flying gaits are used for moving in the air. In order to fly, a creature needs the [`[FLIER]`](/index.php/Creature_token#FLIER "Creature token") tag, and for enough of its body parts tagged [`[FLIER]`](/index.php/Body_token#FLIER "Body token") (e.g. wings) to be intact, if applicable. Flying does not require a minimum speed to stay airborne, and turning while flying is no more difficult than turning while walking.

## Speed

Gait speeds are expressed in ticks/100 tiles. This means that "larger" speeds are **slower** than "smaller" speeds. Currently, the maximum allowed speed is 100 ticks/100 tiles, or 1 tick per tile.

The speeds of each gait are only a baseline for how fast a creature of that species will move. In practice, speed can also be affected by factors such as what a creature is wearing or carrying, as well as its skills, attributes, and even its personality\[Verify\].

Here are some speeds for reference.

|  |  |  |  |
|----|----|----|----|
| Gait Speed | kph | mph | Example |
| 8775 | 1 | 0.6 | average giant earthworm's top speed |
| 6561 | 1.3 | 0.8 | normal human/goblin climbing speed |
| 5951 | 1.5 | 0.9 | normal dwarven climbing speed |
| 3512 | 2.5 | 1.5 | normal kobold climbing speed |
| 2206 | 4 | 2.5 | normal elven climbing speed |
| 1422 | 6.2 | 3.9 | normal ogre walking speed |
| 900 | 9.6 | 6 | normal walking speed |
| 488 | 18 | 11 | average ogre's top speed |
| 439 | 20 | 12 | average troll's top speed |
| 351 | 25 | 16 | average dragon's top speed |
| 293 | 30 | 19 | average dwarf's top speed |
| 293 | 30 | 19 | average giant cave spider's top running **and climbing** speed |
| 251 | 35 | 22 | average kobold's top speed |
| 225 | 39 | 24 | average human's/goblin's top speed |
| 219 | 40 | 25 | average bronze colossus's top speed |
| 214 | 41 | 25 | average elf's top speed |
| 195 | 45 | 28 | average beak dog's top speed |
| 183 | 48 | 30 | average cat's top speed |
| 176 | 50 | 31 | average roc's top speed |
| 157 | 56 | 35 | average gibbon's top climbing speed |
| 149 | 59 | 37 | average dog's top speed |
| 125 | 70 | 43 | average horse's top speed |
| 109 | 80 | 50 | average gazelle's top speed |
| 100 | 87 | 54 | maximum allowed gait speed, average peregrine falcon's top speed |

## Standard Gaits

The vast majority of standard DF creatures use predefined gait patterns. While their gaits vary in speed from type to type and from creature to creature, the gaits' relations to each other are mostly uniform.

|  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|
| Relative Gait | Gait Names | Gait Types | Build-up | Turning | Speed Affected by Physique | Slowed by Stealth | Energy Drain |
| Fastest | Sprint / Gallop / Fastest Walk / Scramble / Maximum Swim Speed / Scramble / Maximum Flight Speed / Scramble | WALK (biped) / WALK (quadruped) / WALK (general) / CLIMB / SWIM / CRAWL / FLY / WALK (no legs) | 10, from a start speed of Fast | No | Yes | 50 | 50 |
| Faster | Run / Canter / Faster Walk / Faster Climb / Faster Swim / Faster Crawl / Faster Flight / Faster Crawl | WALK (biped) / WALK (quadruped) / WALK (general) / CLIMB / SWIM / CRAWL / FLY / WALK (no legs) | 5, from a start speed of Fast | No | Yes | 20 | 10 |
| Fast | Jog / Trot / Fast Walk / Fast Climb / Fast Swim / Fast Crawl / Fast Flight / Fast Crawl | WALK (biped) / WALK (quadruped) / WALK (general) / CLIMB / SWIM / CRAWL / FLY / WALK (no legs) | No | Yes | Yes | 10 | 5 |
| Normal | Walk / Walk / Walk / Climb / Swim / Crawl / Fly / Crawl | WALK (biped) / WALK (quadruped) / WALK (general) / CLIMB / SWIM / CRAWL / FLY / WALK (no legs) | No | Yes | No | No | 0 |
| Slow | Stroll / Stroll / Slow Walk / Slow Climb / Slow Swim / Slow Crawl / Slow Fly / Slow Crawl | WALK (biped) / WALK (quadruped) / WALK (general) / CLIMB / SWIM / CRAWL / FLY / WALK (no legs) | No | Yes | No | No | 0 |
| Slowest | Creep / Creep / Slowest Walk / Creep / Creeping Swim / Creep / Hover / Creep | WALK (biped) / WALK (quadruped) / WALK (general) / CLIMB / SWIM / CRAWL / FLY / WALK (no legs) | No | Yes | No | No | 0 |

## Gaits and Modding

In the vanilla game, gait templates are specified as creature variations in the c_variation_default.txt raw file. These standard templates, each pertaining to a specific gait type, contain 6 individual gaits which detail the different movement speeds available for that gait type, and are shown below.

To specify one of these predefined gaits, the token [`[APPLY_CREATURE_VARIATION]`](/index.php/Creature_token#APPLY_CREATURE_VARIATION "Creature token") should be used. Within this token, specify the desired gait template, and include maximum speed values (which will be inserted into the template in place of its !ARG1, !ARG2, etc. tokens, where the first value specified replaces !ARG1) in this order:\
normal:fast:faster:fastest:slow:slower

Example, taken from the dwarf: `[APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900]` where the speeds are: "walk:jog:run:sprint:stroll:creep". Sprint and run start at jog's max speed and gradually build up to their own, whereas the rest start off at max immediately.

Of course, it's entirely possible to write your own custom gait templates. Note that it isn't necessary to strictly mimic the predefined gaits; your templates can contain any number and mixture of individual gaits (including those of different gait types), and you can place argument tags (!ARG1, !ARG2, etc.) wherever you want to. It's also possible to do away with templates altogether and build up gaits from scratch within an individual creature's raw definition, if you're so inclined. See [`[GAIT]`](/index.php/Creature_token#GAIT "Creature token") for more information.

    Biped walking gaits raws

    [CREATURE_VARIATION:STANDARD_BIPED_GAITS]
        GAIT:type:name:full speed:build up time:turning max:start speed:energy use
            use NO_BUILD_UP if you jump immediately to full speed
            these optional flags go at the end:
                LAYERS_SLOW - fat/muscle layers slow the movement (muscle-slowing counter-acted by strength bonus)
                STRENGTH - strength attribute can speed/slow movement
                AGILITY - agility attribute can speed/slow movement
                STEALTH_SLOWS:
     - n is percentage slowed
                it would be interesting to allow quirky attributes (like mental stats), but they aren't supported yet
        [CV_NEW_TAG:GAIT:WALK:Sprint:!ARG4:10:3:!ARG2:50:LAYERS_SLOW:STRENGTH:AGILITY:STEALTH_SLOWS:50]
        [CV_NEW_TAG:GAIT:WALK:Run:!ARG3:5:3:!ARG2:10:LAYERS_SLOW:STRENGTH:AGILITY:STEALTH_SLOWS:20]
        [CV_NEW_TAG:GAIT:WALK:Jog:!ARG2:NO_BUILD_UP:5:LAYERS_SLOW:STRENGTH:AGILITY:STEALTH_SLOWS:10]
        [CV_NEW_TAG:GAIT:WALK:Walk:!ARG1:NO_BUILD_UP:0]
        [CV_NEW_TAG:GAIT:WALK:Stroll:!ARG5:NO_BUILD_UP:0]
        [CV_NEW_TAG:GAIT:WALK:Creep:!ARG6:NO_BUILD_UP:0]

    Quadruped walking gaits raws

    [CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS]
        [CV_NEW_TAG:GAIT:WALK:Gallop:!ARG4:10:3:!ARG2:5:LAYERS_SLOW:STRENGTH:AGILITY:STEALTH_SLOWS:50]
        [CV_NEW_TAG:GAIT:WALK:Canter:!ARG3:5:3:!ARG2:3:LAYERS_SLOW:STRENGTH:AGILITY:STEALTH_SLOWS:20]
        [CV_NEW_TAG:GAIT:WALK:Trot:!ARG2:NO_BUILD_UP:0:LAYERS_SLOW:STRENGTH:AGILITY:STEALTH_SLOWS:10]
        [CV_NEW_TAG:GAIT:WALK:Walk:!ARG1:NO_BUILD_UP:0]
        [CV_NEW_TAG:GAIT:WALK:Stroll:!ARG5:NO_BUILD_UP:0]
        [CV_NEW_TAG:GAIT:WALK:Creep:!ARG6:NO_BUILD_UP:0]

    Walking gaits raws

    [CREATURE_VARIATION:STANDARD_WALKING_GAITS]
        [CV_NEW_TAG:GAIT:WALK:Fastest Walk:!ARG4:10:3:!ARG2:50:LAYERS_SLOW:STRENGTH:AGILITY:STEALTH_SLOWS:50]
        [CV_NEW_TAG:GAIT:WALK:Faster Walk:!ARG3:5:3:!ARG2:10:LAYERS_SLOW:STRENGTH:AGILITY:STEALTH_SLOWS:20]
        [CV_NEW_TAG:GAIT:WALK:Fast Walk:!ARG2:NO_BUILD_UP:5:LAYERS_SLOW:STRENGTH:AGILITY:STEALTH_SLOWS:10]
        [CV_NEW_TAG:GAIT:WALK:Walk:!ARG1:NO_BUILD_UP:0]
        [CV_NEW_TAG:GAIT:WALK:Slow Walk:!ARG5:NO_BUILD_UP:0]
        [CV_NEW_TAG:GAIT:WALK:Slowest Walk:!ARG6:NO_BUILD_UP:0]

    Climbing gaits raws

    [CREATURE_VARIATION:STANDARD_CLIMBING_GAITS]
        [CV_NEW_TAG:GAIT:CLIMB:Scramble:!ARG4:10:3:!ARG2:50:LAYERS_SLOW:STRENGTH:AGILITY:STEALTH_SLOWS:50]
        [CV_NEW_TAG:GAIT:CLIMB:Faster Climb:!ARG3:5:3:!ARG2:10:LAYERS_SLOW:STRENGTH:AGILITY:STEALTH_SLOWS:20]
        [CV_NEW_TAG:GAIT:CLIMB:Fast Climb:!ARG2:NO_BUILD_UP:5:LAYERS_SLOW:STRENGTH:AGILITY:STEALTH_SLOWS:10]
        [CV_NEW_TAG:GAIT:CLIMB:Climb:!ARG1:NO_BUILD_UP:0]
        [CV_NEW_TAG:GAIT:CLIMB:Slow Climb:!ARG5:NO_BUILD_UP:0]
        [CV_NEW_TAG:GAIT:CLIMB:Creep:!ARG6:NO_BUILD_UP:0]

    Swimming gaits raws

    [CREATURE_VARIATION:STANDARD_SWIMMING_GAITS]
        [CV_NEW_TAG:GAIT:SWIM:Maximum Swim Speed:!ARG4:10:3:!ARG2:50:LAYERS_SLOW:STRENGTH:AGILITY:STEALTH_SLOWS:50]
        [CV_NEW_TAG:GAIT:SWIM:Faster Swim:!ARG3:5:3:!ARG2:10:LAYERS_SLOW:STRENGTH:AGILITY:STEALTH_SLOWS:20]
        [CV_NEW_TAG:GAIT:SWIM:Fast Swim:!ARG2:NO_BUILD_UP:5:LAYERS_SLOW:STRENGTH:AGILITY:STEALTH_SLOWS:10]
        [CV_NEW_TAG:GAIT:SWIM:Swim:!ARG1:NO_BUILD_UP:0]
        [CV_NEW_TAG:GAIT:SWIM:Slow Swim:!ARG5:NO_BUILD_UP:0]
        [CV_NEW_TAG:GAIT:SWIM:Creeping Swim:!ARG6:NO_BUILD_UP:0]

    Crawling gaits raws

    [CREATURE_VARIATION:STANDARD_CRAWLING_GAITS]
        [CV_NEW_TAG:GAIT:CRAWL:Scramble:!ARG4:10:3:!ARG2:50:LAYERS_SLOW:STRENGTH:AGILITY:STEALTH_SLOWS:50]
        [CV_NEW_TAG:GAIT:CRAWL:Faster Crawl:!ARG3:5:3:!ARG2:10:LAYERS_SLOW:STRENGTH:AGILITY:STEALTH_SLOWS:20]
        [CV_NEW_TAG:GAIT:CRAWL:Fast Crawl:!ARG2:NO_BUILD_UP:5:LAYERS_SLOW:STRENGTH:AGILITY:STEALTH_SLOWS:10]
        [CV_NEW_TAG:GAIT:CRAWL:Crawl:!ARG1:NO_BUILD_UP:0]
        [CV_NEW_TAG:GAIT:CRAWL:Slow Crawl:!ARG5:NO_BUILD_UP:0]
        [CV_NEW_TAG:GAIT:CRAWL:Creep:!ARG6:NO_BUILD_UP:0]

    Flying gaits raws

    [CREATURE_VARIATION:STANDARD_FLYING_GAITS]
        [CV_NEW_TAG:GAIT:FLY:Maximum Flight Speed:!ARG4:10:3:!ARG2:50:LAYERS_SLOW:STRENGTH:AGILITY:STEALTH_SLOWS:50]
        [CV_NEW_TAG:GAIT:FLY:Faster Flight:!ARG3:5:3:!ARG2:10:LAYERS_SLOW:STRENGTH:AGILITY:STEALTH_SLOWS:20]
        [CV_NEW_TAG:GAIT:FLY:Fast Flight:!ARG2:NO_BUILD_UP:5:LAYERS_SLOW:STRENGTH:AGILITY:STEALTH_SLOWS:10]
        [CV_NEW_TAG:GAIT:FLY:Fly:!ARG1:NO_BUILD_UP:0]
        [CV_NEW_TAG:GAIT:FLY:Slow Flight:!ARG5:NO_BUILD_UP:0]
        [CV_NEW_TAG:GAIT:FLY:Hover:!ARG6:NO_BUILD_UP:0]

    Walk Crawl gaits raws

    [CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS]
        [CV_NEW_TAG:GAIT:WALK:Scramble:!ARG4:10:3:!ARG2:50:LAYERS_SLOW:STRENGTH:AGILITY:STEALTH_SLOWS:50]
        [CV_NEW_TAG:GAIT:WALK:Faster Crawl:!ARG3:5:3:!ARG2:10:LAYERS_SLOW:STRENGTH:AGILITY:STEALTH_SLOWS:20]
        [CV_NEW_TAG:GAIT:WALK:Fast Crawl:!ARG2:NO_BUILD_UP:5:LAYERS_SLOW:STRENGTH:AGILITY:STEALTH_SLOWS:10]
        [CV_NEW_TAG:GAIT:WALK:Crawl:!ARG1:NO_BUILD_UP:0]
        [CV_NEW_TAG:GAIT:WALK:Slow Crawl:!ARG5:NO_BUILD_UP:0]
        [CV_NEW_TAG:GAIT:WALK:Creep:!ARG6:NO_BUILD_UP:0]

The "Walk Crawl" gait is used for various creatures including worms, slugs, snakes, lizards, etc, that normally crawl (or slither).
