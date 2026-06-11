# Giant animal

> Fonte: [Giant animal](https://dwarffortresswiki.org/index.php/Giant_animal) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

**Giant animals** are variants of normal animals, characterized by simply being much larger. Giant animals appear in caverns, or on the surface-level of savage biomes. Giant animals are based on all kinds of animals, ranging from the smallest of vermin to the largest of beasts, from peaceful grazers to ferocious predators. The main exception to this are the domestic animals – there is no giant turkey, for example. Creatures with no basis in reality are also exempt from becoming giant animals.

Both the largest creature in the game, the giant sperm whale, and the largest land creature, the giant elephant, are giant animals. Other giant animals, such as the giant orca, giant rhinoceros, giant elephant seal and giant walrus, are still larger than the fort-threatening monsters that are megabeasts, titans and forgotten beasts.

The rule in *Dwarf Fortress* is that a giant creature should be at least as large as a grizzly bear, even if it's a giant version of a small insect. As the real-world creatures approach grizzly bear size, and then beyond, a curve is applied, so that the largest ones are only roughly twice as large in every dimension as their counterpart. Giant whales are very, very large, but they are just eight times as massive as a normal whale, rather than the kind of scaling you see when you go from a spider to a giant spider.

Many variants are only found on the surface of savage biomes. However, some giant animals are practically universal across caverns, regardless of savagery level. Giant rats, Giant olms, Giant moles, Giant cave spiders, Giant cave swallows, Giant earthworms and Giant cave toads are readily found even in non-savage biomes, as long as you dig down to at least the first cavern level.

Three giant animals are called "gigantic" instead of "giant" to avoid confusion with real-life creatures - they are the gigantic panda, gigantic squid and gigantic tortoise. The giant tortoise and giant grouper are not technically giant animals, despite having "giant" in their names. Unlike most other giant creatures, the Giant, Giant bat, Giant cave swallow, Giant Grouper Fish, Giant Tortoise, Giant earthworm, Giant mole, Giant olm, Giant rat, Giant cave spider, and Giant cave toad do not [`[COPY_TAGS_FROM]`](/index.php/Creature_token#COPY_TAGS_FROM "Creature token") their base creatures. For those that do copy tags, the following is used to adjust them:

    Giant
    creature variation
     raws

    [CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:NAME]
        [CV_REMOVE_TAG:GENERAL_CHILD_NAME]
        [CV_REMOVE_TAG:GENERAL_BABY_NAME]
        [CV_REMOVE_TAG:CASTE_NAME]
        [CV_REMOVE_TAG:CHILDNAME]
        [CV_REMOVE_TAG:BABYNAME]
        [CV_REMOVE_TAG:POPULATION_NUMBER]
        [CV_REMOVE_TAG:CLUSTER_NUMBER]
        [CV_REMOVE_TAG:COLOR]
        [CV_REMOVE_TAG:MOUNT]
        [CV_REMOVE_TAG:MOUNT_EXOTIC]
        [CV_REMOVE_TAG:SOUND]
        [CV_REMOVE_TAG:SMALL_REMAINS]
        [CV_REMOVE_TAG:DESCRIPTION]
        [CV_REMOVE_TAG:CREATURE_TILE]
        [CV_REMOVE_TAG:PET]
        [CV_REMOVE_TAG:PETVALUE]
        [CV_REMOVE_TAG:PENETRATEPOWER]
        [CV_REMOVE_TAG:VERMIN_EATER]
        [CV_REMOVE_TAG:VERMIN_HATEABLE]
        [CV_REMOVE_TAG:VERMIN_GROUNDER]
        [CV_REMOVE_TAG:VERMIN_FISH]
        [CV_REMOVE_TAG:VERMIN_SOIL]
        [CV_REMOVE_TAG:VERMIN_SOIL_COLONY]
        [CV_REMOVE_TAG:VERMIN_ROTTER]
        [CV_REMOVE_TAG:VERMIN_NOTRAP]
        [CV_REMOVE_TAG:FISHITEM]
        [CV_REMOVE_TAG:TRIGGERABLE_GROUP]
        [CV_REMOVE_TAG:PET_EXOTIC]
        [CV_REMOVE_TAG:NOT_BUTCHERABLE]
        [CV_REMOVE_TAG:PREFSTRING]
        [CV_REMOVE_TAG:SPEED]
        [CV_REMOVE_TAG:SWIM_SPEED]
        [CV_REMOVE_TAG:MUNDANE]
        [CV_REMOVE_TAG:GAIT]
        [CV_REMOVE_TAG:UBIQUITOUS]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:BIOME]
            [CVCT_TARGET:ANY_POOL]
            [CVCT_REPLACEMENT:ANY_LAKE]
        [CV_NEW_TAG:LARGE_ROAMING]
        [CV_NEW_TAG:SAVAGE]
        [CV_NEW_TAG:SELECT_CASTE:ALL]
            [CV_NEW_TAG:CHANGE_BODY_SIZE_PERC:200]
            [CV_NEW_TAG:CHANGE_FREQUENCY_PERC:50]

## List of giant animals

|  |  |  |
|----|----|----|
|  / `A` Giant aardvark |  / `A` Giant adder |  / `A` Giant albatross |
|  / `A` Giant alligator |  / `A` Giant anaconda |  / `A` Giant anole |
|  / `A` Giant armadillo |  / `A` Giant axolotl |  / `A` Giant aye-aye |
|  / `B` Giant bat |  / `B` Giant badger |  / `S` Giant bark scorpion |
|  / `B` Giant barn owl |  / `B` Giant beaver |  / `B` Giant beetle |
|  / `B` Giant black bear |  / `S` Giant black mamba |  / `B` Giant bluejay |
|  / `B` Giant bobcat |  / `S` Giant brown recluse spider |  / `S` Giant bushmaster |
|  / `B` Giant bushtit |  / `B` Giant buzzard |  / `C` Giant capuchin |
|  / `C` Giant capybara |  / `C` Giant cardinal |  / `S` Giant cave spider |
|  / `C` Giant cave swallow |  / `T` Giant cave toad |  / `C` Giant cassowary |
|  / `C` Giant chameleon |  / `C` Giant cheetah |  / `C` Giant chinchilla |
|  / `C` Giant chipmunk |  / `C` Giant coati |  / `C` Giant cockatiel |
|  / `S` Giant copperhead snake |  / `C` Giant cougar |  / `C` Giant coyote |
|  / `C` Giant crab |  / `C` Giant crow |  / `C` Giant cuttlefish |
|  / `D` Giant damselfly |  / `D` Giant deer |  / `S` Giant desert scorpionUntil v0.42.04 |
|  / `T` Giant desert tortoise |  / `D` Giant dingo |  / `D` Giant dragonfly |
|  / `E` Giant eagle |  / `W` Giant earthworm |  / `E` Giant echidna |
|  / `E` Giant elephant |  / `S` Giant elephant seal |  / `E` Giant elk |
|  / `E` Giant emu |  / `F` Giant firefly |  / `F` Giant fly |
|  / `F` Giant flying squirrel |  / `F` Giant fox |  / `G` Giant gazelle |
|  / `T` Gigantic tortoise |  / `G` Giant gila monster |  / `G` Giant giraffe |
|  / `G` Giant grackle |  / `G` Giant grasshopper |  / `L` Giant gray langur |
|  / `S` Giant gray squirrel |  / `O` Giant great horned owl |  / `F` Giant green tree frog |
|  / `P` Giant grey parrot |  / `B` Giant grizzly bear |  / `G` Giant groundhog |
|  / `H` Giant hamster |  / `H` Giant hare |  / `H` Giant harp seal |
|  / `H` Giant hedgehog |  / `H` Giant hippo |  / `M` Giant hoary marmot |
|  / `B` Giant honey badger |  / `H` Giant hornbill |  / `H` Giant horseshoe crab |
|  / `H` Giant hyena |  / `I` Giant ibex |  / `I` Giant iguana |
|  / `I` Giant impala |  / `J` Giant jackal |  / `J` Giant jaguar |
|  / `S` Giant jumping spider |  / `K` Giant kakapo |  / `K` Giant kangaroo |
|  / `K` Giant kea |  / `K` Giant kestrel |  / `K` Giant king cobra |
|  / `K` Giant kingsnake |  / `K` Giant kiwi |  / `K` Giant koala |
|  / `L` Giant leech |  / `G` Giant leopard gecko |  / `L` Giant leopard |
|  / `L` Giant leopard seal |  / `L` Giant lion |  / `L` Giant lion tamarin |
|  / `L` Giant lizard |  / `L` Giant loon |  / `L` Giant lorikeet |
|  / `L` Giant louse |  / `L` Giant lynx |  / `M` Giant magpie |
|  / `M` Giant mandrill |  / `M` Giant mantis |  / `L` Giant masked lovebird |
|  / `M` Giant mink |  / `m` Giant mole |  / `B` Giant monarch butterfly |
|  / `M` Giant mongoose |  / `M` Giant monitor lizard |  / `S` Giant moon snail |
|  / `M` Giant moose |  / `M` Giant mosquito |  / `M` Giant moth |
|  / `G` Giant mountain goat |  / `M` Giant muskox |  / `N` Giant narwhal |
|  / `N` Giant nautilus |  / `O` Giant ocelot |  / `O` Giant octopus |
|  / `C` Giant one-humped camel |  / `O` Giant opossum |  / `O` Giant orca |
|  / `O` Giant oriole |  / `O` Giant osprey |  / `O` Giant ostrich |
|  / `O` Giant otter |  / `O` Giant olm |  / `P` Gigantic panda |
|  / `P` Giant pangolin |  / `P` Giant parakeet |  / `L` Giant peach-faced lovebird |
|  / `P` Giant penguin |  / `P` Giant peregrine falcon |  / `P` Giant platypus |
|  / `B` Giant polar bear |  / `T` Giant pond turtle |  / `P` Giant porcupine |
|  / `P` Giant puffin |  / `S` Giant python |  / `R` Giant raccoon |
|  / `R` Giant rat |  / `S` Giant rattlesnake |  / `R` Giant raven |
|  / `R` Giant red panda |  / `R` Giant red squirrel |  / `R` Giant red-winged blackbird |
|  / `M` Giant rhesus macaque |  / `R` Giant rhinoceros |  / `R` Giant roach |
|  / `C` Giant saltwater crocodile |  / `S` Giant skink |  / `S` Giant skunk |
|  / `B` Giant sloth bear |  / `S` Giant sloth |  / `S` Giant slug |
|  / `S` Giant snail |  / `T` Giant snapping turtle |  / `O` Giant snowy owl |
|  / `S` Giant sparrow |  / `W` Giant sperm whale |  / `M` Giant spider monkey |
|  / `S` Giant sponge |  / `S` Gigantic squid |  / `S` Giant stoat |
|  / `S` Giant swan |  / `T` Giant tapir |  / `T` Giant thrips |
|  / `T` Giant tick |  / `T` Giant tiger |  / `T` Giant toad |
|  / `C` Giant two-humped camel |  / `V` Giant vulture |  / `W` Giant walrus |
|  / `W` Giant warthog |  / `W` Giant weasel |  / `S` Giant white stork |
|  / `B` Giant wild boar |  / `W` Giant wolf |  / `W` Giant wolverine |
|  / `W` Giant wombat |  / `W` Giant wren |  |

## History

Giant animals have existed since the 2D days of Dwarf Fortress. Initially, the only giant animals were giant bats, giant cave spiders, giant cheetahs, giant leopards, giant lions, giant moles, giant rats, giant tigers, and giant toads. The giant desert scorpion was also one of these.

More giant animals were added up until sometime during 0.31, when creature variations were added. After this, any new giant animal was added as a creature variant. Several new giant animals came with 0.34.01, due to the animals of the animal sponsorship drive receiving giant variants.

Sometime during DF2014, the original giant animals were refactored to be creature variants, instead of being defined separately from their common versions. The giant cave spider was an exception from this.

0.42.04 added many giant animals as variants of existing creatures, including the giant elephant. The giant desert scorpion was removed, as there existed no normal ”desert scorpion”.
