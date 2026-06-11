# Random creature profile

> Fonte: [Random creature profile](https://dwarffortresswiki.org/index.php/Random_creature_profile) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

|  |
|:--:|
|   This article or section contains **minor spoilers**. You may want to avoid reading it. |

A **random creature profile** (**rcp**) is a template used by procedurally-generated creatures. rcps typically use body parts from `body_rcp.txt` instead of `body_default.txt`.

## Overview

**rcp** stands for "random creature profile". rcp is a scripted raw template that defines the basic body, tissues and body attacks of a random creature before it receives further randomness (three-eyed, wings of stretched skin, external ribs, uniform elemental composition, etc). Most amphibian, mammalian and reptilian rcps have humanoid variations of themselves, described as "in humanoid form" or "twisted into humanoid form". There are 243 standard rcps and 81 humanoid variations, which brings the known total to 324.

The rcp of a randomly generated creature can be identified by its description. Many rcps have identical names with normal creatures (e.g. albatross), although they are entirely unrelated; other rcps feature animals that don't exist anywhere else, such as zebras. Some rcps have inherent abilities like flight or webbing.

Night trolls and bogeymen only use the generic "humanoid" rcp, and werebeasts use the humanoid animal forms. Primates, hexapods, octopods and decapods are unique to beast-like experiments, while armless bipeds, wyrms, and the generic "snake" and "worm" rcps are unique to failed experiments.

## Technical details

Random creature profiles can be found in `vanilla_procedural/scripts/`. By adding data to the corresponding tables, it is possible to mod in new random creature profiles.

This explanation from Toady, shared by Meph, goes into more detail on how procedural creature generation works:

> The `body_rcp.txt` file has the definitions it expects for bodyparts. (rcp stands for "random creature profile") The main thing is that the base "animal" word is doing most of the heavy lifting in terms of making the descriptions evocative, so the rcp's don't end up mattering that much. There are little internal definitions for each animal word, about 230 of them. If we ignore that, then we're more just working with "feathered quadruped" and so forth.
>
> Example of a random creature profile (for the elephant type):
>
>
>
>     random_creature_types.MAMMAL_ELEPHANT={
>         name_string="elephant",
>         tile='E',
>         body_base="QUADRUPED",
>         c_class="MAMMAL",
>         must_have_tail=true,
>         must_have_elephant_trunk=true,
>         min_size=500000,
>         weight=14
>     }
>
>
>
> So, hmm, perhaps the base and class lists are relevant here...
>
> - classes (`random_creature_class`): mammal, chitin exo, fleshy, amphibian, reptile, feathered reptile, avian, uniform (like 'composed of iron')
>
>
>
> - bases (`body_base_fun`): amorphous, insect, insect larva, spider, scorpion, ten legged, eight legged, worm, no limbs, quadruped, snake, humanoid, two legs + no arms, quadruped with front graspers (like a monkey)
>
> The flags just force certain rcp additions, and prevent others from happening. For instance, the "slug" profile has "cannot have shell" because a slug with a shell is confusing.
>
> Ah, here we go. The rcp are used via the "body tweak" system. A body can have a tweak from category one, a tweak from category two, and an attack tweak, respecting its profile flags.
>
> - Category one tweaks (`options.btc`): wings, flightless wings, tail, proboscis, trunk, shell, antennae, head horns, large mandibles, twisted into humanoid form, six legged, eight legged
>
>
>
> - Category two tweaks (`options.btc2`): hair, feathers, scales, exoskeleton, skin, skin/bones, no eyes, one eye, three eyes, beak missing, nose missing, external ribs, lidless eyes, skinless
>
>
>
> - Attack tweaks (`options.attack_tweak`): tail stinger, insect stinger, blood proboscis, fire, webs, breath (trailing flow), breath (glob), breath (undirected), secretion, poisonous blood, poisonous bite
>
> That material list (`random_creature_material`) looks almost right - here's the official list of variables: ash, mud, vomit, salt (powder), grime, snow, water, steam, flame, amber, coral, green glass, clear glass, crystal glass, charcoal, coke, salt (solid), ice, mineral (any), soil (any), gem (any), metal (any)
>
> The "any" materials can't be "special", but there don't appear to be other restrictions. There are various other implicit flags on these things when it comes to werebeasts etc. "humanoidable" and "beast", for example. So all night creatures require "humanoidable" and werebeasts require "beast" on top of that. Which is why we don't have wereblobs or even wereserpents.

## List

In ASCII mode, nearly all rcps use specific uppercase or lowercase letters if the monster type does not use a fixed tile, such as '&' for demons. Lobsters uniquely use the '¥' sign instead. rcps with humanoid versions are **bolded**. Humanoid forms use the same tile as their standard counterparts.

Capitalization denotes body size. In most cases, anything larger than a dwarf (60,000) uses an uppercase letter. Only uppercase letters are shown here.

In-game, the tile color is determined by the creature's external color modifier. If it does not have a color modifier and is not skinless, it uses the outermost tissue layer's default material color. If it is skinless, it is displayed in dark red (4:0:0).

- `A` Albatross
- `A` **Alligator**
- `A` Anaconda
- `A` Ankylosaurid
- `I` Ant
- `A` **Anteater**
- `A` **Antelope**
- `I` Antlion larva
- `A` **Ape**
- `I` Aphid
- `A` **Armadillo**
- `B` Armless biped
- `I` Assassin bug
- `B` **Badger**
- `B` Bat
- `B` **Bear**
- `B` **Beaver**
- `I` Bee
- `B` **Bison**
- `B` Blob
- `W` Bristleworm
- `B` **Buffalo**
- `B` **Bull**
- `B` Bunting
- `B` Bushtit
- `I` Butterfly
- `B` Buzzard
- `I` Caddisfly
- `C` **Camel**
- `C` **Capybara**
- `C` Cardinal
- `C` **Cat**
- `I` Caterpillar
- `C` **Cavy**
- `C` Ceratopsid
- `C` **Chameleon**
- `C` Chickadee
- `C` Chicken
- `C` **Chinchilla**
- `I` Cicada
- `C` **Civet**
- `I` Click beetle
- `C` **Coati**
- `C` Cobra
- `C` Cockatoo
- `I` Cockroach
- `C` Condor
- `C` **Coyote**
- `C` Crab
- `C` Crane
- `I` Cricket
- `C` **Crocodile**
- `C` Crow
- `C` Cuckoo
- `I` Damselfly
- `I` Darkling beetle
- `D` Decapod
- `D` **Deer**
- `D` Dimetrodon
- `D` **Donkey**
- `D` Dove
- `I` Dragonfly
- `D` Duck
- `I` Dung beetle
- `E` Eagle
- `W` Earthworm
- `I` Earwig
- `E` **Elephant**
- `E` **Elk**
- `F` Falcon
- `F` Fantail
- `F` Finch
- `I` Firefly
- `F` Flamingo
- `W` Flat worm
- `I` Flea
- `I` Fly
- `F` Flycatcher
- `F` **Fox**
- `F` **Frog**
- `F` Fruit bat
- `G` **Gecko**
- `G` **Gila monster**
- `G` **Giraffe**
- `G` **Goat**
- `G` Goose
- `G` **Gopher**
- `I` Grasshopper
- `G` Grebe
- `G` Grouse
- `G` Gull
- `H` Hadrosaurid
- `H` **Hare**
- `H` Harrier
- `H` Hawk
- `H` **Hedgehog**
- `H` Hexapod
- `H` **Hippopotamus**
- `H` Honeyeater
- `H` Hornbill
- `I` Hornet
- `H` **Horse**
- `H` Humanoid
- `H` Hummingbird
- `H` **Hyena**
- `I` **Iguana**
- `I` Iguanodont
- `J` **Jackal**
- `J` Jay
- `K` **Kangaroo**
- `K` Kestrel
- `K` Kingfisher
- `K` Kinglet
- `K` Kite
- `K` **Koala**
- `I` Lacewing
- `I` Ladybug
- `L` Lark
- `L` Leech
- `L` **Lemur**
- `L` **Lizard**
- `L` **Llama**
- `¥` Lobster
- `L` Loon
- `L` **Loris**
- `I` Louse
- `L` Lyrebird
- `I` Maggot
- `M` Magpie
- `M` **Mammoth**
- `I` Mantis
- `M` **Marmot**
- `M` Martin
- `I` Mayfly
- `M` Mite
- `M` Mockingbird
- `M` **Mole**
- `M` **Mongoose**
- `M` **Monitor**
- `M` **Monkey**
- `M` **Moose**
- `I` Mosquito
- `I` Moth
- `M` **Mouse**
- `N` Nematode
- `N` **Newt**
- `N` Nightjar
- `N` Nuthatch
- `O` Octopod
- `O` **Opossum**
- `O` Oriole
- `O` Osprey
- `O` **Otter**
- `O` Owl
- `O` Oxpecker
- `P` **Panda**
- `P` **Pangolin**
- `P` **Panther**
- `P` Parrot
- `P` Pelican
- `P` Penguin
- `P` Petrel
- `P` Pheasant
- `P` **Pig**
- `P` Pigeon
- `P` **Porcupine**
- `P` Primate
- `P` Pterosaur
- `P` Python
- `Q` Quadruped
- `Q` Quail
- `Q` Quetzal
- `R` **Rabbit**
- `R` **Raccoon**
- `R` **Rat**
- `R` Rattlesnake
- `R` Raven
- `R` **Rhinoceros**
- `I` Rhinoceros beetle
- `W` Ribbon worm
- `I` Rove beetle
- `S` **Salamander**
- `S` Sauropod
- `I` Scarab beetle
- `S` Scorpion
- `I` Scorpionfly
- `S` Serpent
- `S` **Sheep**
- `S` **Shrew**
- `S` Shrike
- `S` Shrimp
- `I` Silverfish
- `S` **Skink**
- `S` **Skunk**
- `S` **Sloth**
- `S` Slug
- `S` Snail
- `S` Snake
- `I` Snakefly
- `S` Sparrow
- `S` Spider
- `S` **Squirrel**
- `I` Stag beetle
- `S` Starling
- `S` Stegosaurid
- `I` Stick insect
- `I` Stonefly
- `S` Stork
- `S` Swallow
- `S` Swan
- `S` Swift
- `T` Tanager
- `T` **Tapir**
- `S` Tarantula
- `I` Termite
- `T` Theropod
- `T` Thornbill
- `I` Thrips
- `T` Thrush
- `T` Tick
- `I` Tiger beetle
- `T` Titmouse
- `T` **Toad**
- `T` **Tortoise**
- `T` Toucan
- `T` Turkey
- `T` **Turtle**
- `V` Viper
- `V` Vulture
- `W` Walrus
- `W` Warbler
- `W` **Warthog**
- `I` Wasp
- `W` Waxwing
- `W` **Weasel**
- `I` Weevil
- `W` **Wolf**
- `W` **Wombat**
- `W` Woodpecker
- `W` Worm
- `W` Wren
- `W` Wyrm
- `Z` **Zebra**

## Graphics

All random creatures except werebeasts use graphic sprites found in `beasts.png` and `beasts_small.png`. There are 19 primary body sprites (6 are alternate-legged variations) with additional sprite layers representing secondary body parts. Several rcps have one or more secondary sprite layers by default. A few rcps, like quadrupeds, have more than one body sprite to randomly select from.

rcp sprites, ignoring random body modifications, large sprites only

rcps
Sprite
Secondary graphic token(s)
Primary graphic token

albatross, armless biped, bat, blob, bunting, bushtit, buzzard, cardinal, chickadee, chicken, cockatoo, condor, crane, crow, cuckoo, dove, duck, eagle, falcon, fantail, finch, flamingo, flycatcher, fruit bat, goose, grebe, grouse, gull, harrier, hawk, honeyeater, hornbill, hummingbird, jay, kestrel, kingfisher, kinglet, kite, lark, loon, lyrebird, magpie, martin, mockingbird, nightjar, nuthatch, oriole, osprey, owl, oxpecker, parrot, pelican, penguin, petrel, pheasant, pigeon, pterosaur, quail, quetzal, raven, shrike, sparrow, starling, stork, swallow, swan, swift, tanager, thornbill, thrush, titmouse, toucan, turkey, vulture, warbler, waxwing, woodpecker, wren

none
BEAST_AMORPHOUS

snake

none
BEAST_SNAKE

anaconda, cobra, python, rattlesnake, serpent, viper

BEAST_SNAKE_EYE_TWO

bristleworm, earthworm, flat worm, leech, nematode, ribbon worm, slug, worm

none
BEAST_WORM_LONG

snail

BEAST_WORM_LONG_SHELL_BACK

caterpillar, maggot

BEAST_WORM_SHORT_EYE_TWO
BEAST_WORM_SHORT

hexapod

none
BEAST_INSECT

antlion larva, flea, louse

BEAST_INSECT_EYE_TWO

ant, aphid, assassin bug, click beetle, cockroach, cricket, darkling beetle, dung beetle, earwig, grasshopper, ladybug, mantis, rove beetle, scarab beetle, silverfish, stick insect, stonefly, termite, thrips, tiger beetle, weevil

BEAST_INSECT_EYE_TWO, BEAST_INSECT_ANTENNAE

stag beetle

BEAST_INSECT_MANDIBLES, BEAST_INSECT_EYE_TWO, BEAST_INSECT_ANTENNAE

rhinoceros beetle

BEAST_INSECT_HORNS, BEAST_INSECT_EYE_TWO, BEAST_INSECT_ANTENNAE

cicada, damselfly, dragonfly, fly

BEAST_INSECT_WINGS_LACY_BACK, BEAST_INSECT_EYE_TWO

bee, butterfly, caddisfly, firefly, hornet, lacewing, mayfly, moth, scorpionfly, snakefly, wasp

BEAST_INSECT_WINGS_LACY_BACK, BEAST_INSECT_EYE_TWO, BEAST_INSECT_ANTENNAE

mosquito

BEAST_INSECT_WINGS_LACY_BACK, BEAST_INSECT_EYE_TWO, BEAST_INSECT_PROBOSCIS, BEAST_INSECT_ANTENNAE

decapod, octopod

none
BEAST_SPIDER

crab, lobster, mite, spider, tarantula, tick

BEAST_SPIDER_EYE_TWO

shrimp

BEAST_SPIDER_EYE_TWO, BEAST_SPIDER_EYE_ANTENNAE

scorpion

BEAST_SCORPION_EYE_TWO, BEAST_SCORPION_TAIL_ONE
BEAST_SCORPION

wyrm

none
BEAST_BIPEDAL_DINOSAUR

humanoid*

none
BEAST_HUMANOID

humanoid* / (humanoid forms) / : ape, capybara, cavy, frog, koala, toad, wombat

BEAST_HUMANOID_EYE_TWO

iguanodont, theropod / (humanoid forms) / : alligator, anteater, antelope, armadillo, badger, bear, beaver, bison, buffalo, bull, camel, cat, chameleon, chinchilla, civet, coati, coyote, crocodile, deer, donkey, elk, fox, gecko, gila monster, giraffe, goat, gopher, hare, hedgehog, hippopotamus, horse, hyena, iguana, jackal, kangaroo, lemur, lizard, llama, loris, marmot, mole, mongoose, monitor, monkey, moose, mouse, newt, opossum, otter, panda, pangolin, panther, pig, porcupine, rabbit, raccoon, rat, rhinoceros, salamander, sheep, shrew, skink, skunk, sloth, squirrel, tapir, warthog, weasel, wolf, zebra

BEAST_HUMANOID_EYE_TWO, BEAST_HUMANOID_TAIL_ONE

(humanoid forms): elephant, mammoth

BEAST_HUMANOID_EYE_TWO, BEAST_HUMANOID_TAIL_ONE, BEAST_HUMANOID_TRUNK

(humanoid forms): tortoise, turtle

BEAST_HUMANOID_EYE_TWO, BEAST_HUMANOID_SHELL_BACK

ape

BEAST_FRONT_GRASP_EYE_TWO
BEAST_FRONT_GRASP

monkey

BEAST_FRONT_GRASP_EYE_TWO, BEAST_FRONT_GRASP_TAIL_ONE

primate, quadruped

none
BEAST_QUADRUPED_BULKY

capybara, cavy, koala, toad, wombat

BEAST_QUADRUPED_BULKY_EYE_TWO

ankylosaurid, armadillo, bear, beaver, bison, buffalo, bull, camel, ceratopsid, chinchilla, goat, gopher, hadrosaurid, hedgehog, hippopotamus, llama, loris, marmot, mole, panda, pig, porcupine, rhinoceros, sauropod, sheep, sloth, stegosaurid, tapir, warthog

BEAST_QUADRUPED_BULKY_EYE_TWO, BEAST_QUADRUPED_BULKY_TAIL_ONE

elephant, mammoth

BEAST_QUADRUPED_BULKY_EYE_TWO, BEAST_QUADRUPED_BULKY_TAIL_ONE, BEAST_QUADRUPED_BULKY_TRUNK

tortoise, turtle

BEAST_QUADRUPED_BULKY_EYE_TWO, BEAST_QUADRUPED_BULKY_SHELL_FRONT

primate, quadruped

none
BEAST_QUADRUPED_SLINKY

frog

BEAST_QUADRUPED_SLINKY_EYE_TWO

alligator, anteater, antelope, badger, cat, chameleon, civet, coati, coyote, crocodile, deer, dimetrodon, donkey, elk, fox, gecko, gila monster, giraffe, hare, horse, hyena, iguana, jackal, kangaroo, lemur, lizard, mongoose, monitor, moose, mouse, newt, opossum, otter, pangolin, panther, rabbit, raccoon, rat, salamander, shrew, skink, skunk, squirrel, weasel, wolf, zebra

BEAST_QUADRUPED_SLINKY_EYE_TWO, BEAST_QUADRUPED_SLINKY_TAIL_ONE

walrus

BEAST_WALRUS_EYE_TWO
BEAST_WALRUS

**\*** The (generic) humanoid rcp has two or no eyes (by default) depending on the type of beast/monster:

2 eyes: bogeymen, experiments (intelligent humanoids), night trolls

0 eyes: experiments (amalgamations), nightmares, everything else (which are elementals)

## Gallery

- Large sprites

-

  Amorphous sprite

-

  Snake sprite

-

  Long worm sprite

-

  Short worm sprite

-

  Insect sprite

-

  Spider sprite

-

  Scorpion sprite

-

  Scorpion sprite (with one tail)

-

  Bipedal dinosaur sprite

-

  Humanoid sprite

-

  Front grasp sprite

-

  Front grasp sprite (six-legged)

-

  Front grasp sprite (eight-legged)

-

  Bulky quadruped sprite

-

  Bulky quadruped sprite (six-legged)

-

  Bulky quadruped sprite (eight-legged)

-

  Slinky quadruped sprite

-

  Slinky quadruped sprite (six-legged)

-

  Slinky quadruped sprite (eight-legged)

-

  Walrus sprite

- Small sprites

-

  Small amorphous sprite

-

  Small snake sprite

-

  Small long worm sprite

-

  Small short worm sprite

-

  Small insect sprite

-

  Small spider sprite

-

  Small scorpion sprite

-

  Small scorpion sprite (with one tail)

-

  Small bipedal dinosaur sprite

-

  Small humanoid sprite

-

  Small front grasp sprite

-

  Small front grasp sprite (six-legged)

-

  Small front grasp sprite (eight-legged)

-

  Small bulky quadruped sprite

-

  Small bulky quadruped sprite (six-legged)

-

  Small bulky quadruped sprite (eight-legged)

-

  Small slinky quadruped sprite

-

  Small slinky quadruped sprite (six-legged)

-

  Small slinky quadruped sprite (eight-legged)

-

  Small walrus sprite

\
