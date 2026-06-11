# Gait

> Fonte: [Gait](https://dwarffortresswiki.org/index.php/Gait) — Dwarf Fortress Wiki (GFDL/MIT)

A **gait** is a mode of movement which a creature can use. In real life, the word only applies to movement on land; but in *Dwarf Fortress*, the term describes any mode of movement by a creature, including swimming, flying, and climbing.

## Gait Types

There are 5 different types of gaits: walking, crawling, climbing, swimming, and flying.

- Walking gaits are land-based gaits which require the creature to be standing up, and have more than half of their body parts, e.g. legs, intact and working. They can be used to move across flat ground, and go up and down ramps and stairs.

- Crawling gaits are like walking gaits, except that they require neither standing up nor body parts. They are much slower than walking gaits. Please note that an uninjured, slithering snake is considered to be using a walking gait, not a crawling gait: its body is its body part. If a snake is injured in the body, it will revert to a crawling gait.

- Climbing gaits are used for moving up and down vertical surfaces, such as trees or walls, as well as for moving horizontally while supporting oneself against a vertical surface. In order to climb, a creature needs intact body parts to climb with: body parts by default, or \[STANCE\] body parts if the creature has the token. Stance climbers include cats and giant cave spiders.

- Swimming gaits are used for moving in the water. In order to swim, a creature needs either the tag, or , and skill in swimming.

- Flying gaits are used for moving in the air. In order to fly, a creature needs the tag, and for enough of its body parts tagged (e.g. wings) to be intact, if applicable. Flying does not require a minimum speed to stay airborne, and turning while flying is no more difficult than turning while walking.

## Speed

Gait speeds are expressed in ticks/100 tiles. This means that "larger" speeds are **slower** than "smaller" speeds. Currently, the maximum allowed speed is 100 ticks/100 tiles, or 1 tick per tile.

The speeds of each gait are only a baseline for how fast a creature of that species will move. In practice, speed can also be affected by factors such as what a creature is wearing or carrying, as well as its skills, attributes, and even its personality.

Here are some speeds for reference.

| Gait Speed | kph | mph | Example |
|----|----|----|----|
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

[TABLE]

## Gaits and Modding

In the vanilla game, gait templates are specified as creature variations in the c_variation_default.txt raw file. These standard templates, each pertaining to a specific gait type, contain 6 individual gaits which detail the different movement speeds available for that gait type.

To specify one of these predefined gaits, the token should be used. Within this token, specify the desired gait template, and include maximum speed values (which will be inserted into the template in place of its !ARG1, !ARG2, etc. tokens, where the first value specified replaces !ARG1) in this order:\
normal:fast:faster:fastest:slow:slower

Example, taken from the dwarf: `[APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900]` where the speeds are: "walk:jog:run:sprint:stroll:creep". Sprint and run start at jog's max speed and gradually build up to their own, whereas the rest start off at max immediately.

Of course, it's entirely possible to write your own custom gait templates. Note that it isn't necessary to strictly mimic the predefined gaits; your templates can contain any number and mixture of individual gaits (including those of different gait types), and you can place argument tags (!ARG1, !ARG2, etc.) wherever you want to. It's also possible to do away with templates altogether and build up gaits from scratch within an individual creature's raw definition, if you're so inclined. See for more information.
