# Animal person

> Fonte: [Animal person](https://dwarffortresswiki.org/index.php/Animal_person) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Animal people** are half-man, half-beast creatures with various animal-like traits, some beneficial (such as flying, and poisons), or detrimental (thievery), inherited from their base animal. They generally have significantly longer lifespans than the base animals, as well as the ability to learn. They can be legless, but get arms even if their base animal is limbless. Their body size is the average of their base animal's size and 70,000 (the size of a human), working out so that the smallest animal people are 35,000cm³, half the size of a human, but they can get very large. Most animal people can join civilizations and live in sites, or come to your fort as visitors.

Animal people are playable creatures in adventurer mode. If they became established members of a playable civ (dwarf, elf, human), they will appear listed in the creature selection screen alongside the main races. Otherwise, they are selectable under Intelligent Wilderness Creature. Some animal people may not be available due to having died out or being uncontacted (e.g. excluded to an isolated island).

Wild animal people wander on the surface in savage environments or dwell underground in the caverns; these two populations form distinct groups:

- Savage animal people behave mostly like common animals, wandering the wilderness and occasionally joining human, dwarven or elven society during world generation. When encountered in fortress mode gameplay, they are essentially animals who can't be butchered, incapable of any sort of non-violent interaction. In adventure mode gameplay, you can speak with them and possibly recruit them as followers - they may be neutral or, somewhat more commonly, hostile, though with rare exceptions capable of speech. Like their underground counterparts, they tend to have spears and blowguns, though they may also be unarmed.
- Subterranean animal people are a civilization in themselves, rarely encountered, in small groups or "tribes". They are equipped with primitive weaponry such as wooden spears and blowguns (they are the only known source of blowdarts). Subterranean animal people will be labelled as Hostile upon discovery. Despite this, they are non-aggressive and will generally ignore your dwarves unless provoked. Encountering them often comes as a surprise, since there is no way to know about their presence before embarking. They do not appear in the Y civilizations menu.

Subterranean animal people are also found in generated sewers, formed from collections of outcasts. Graphically, animal people are given their own sprites. Unlike dwarves, humans, elves, goblins and kobolds, where each of the body parts of the creature are assembled from separate smaller pieces to combine into one sprite, based on their physical traits and items in their possession, animal people will use the same exact sprite regardless of any differing qualities. Like almost every other creature in the game, animal people will have one standard sprite, and one undead sprite. Unlike most "man" creatures, Amphibian Man, Ant Man, Plump Helmet Man, Reptile Man, Rodent Man, and Serpent Man do not [`[COPY_TAGS_FROM]`](/index.php/Creature_token#COPY_TAGS_FROM "Creature token") their base species. Animal people will not inherit the [`[MEANDERER]`](/index.php/Creature_token#MEANDERER "Creature token") tag from their animal counterparts.

## Creature variation raws

For animal person definitions that do copy tags from the base creatures, one of the following in the c_variation_default.txt raw file is used to adjust them:

    Animal person
    creature variation
     raws

    Order of application:
    Remove tags are applied starting from the bottom, then convert tags from the bottom, then add tags from the top.

    Arguments:
    If APPLY_CREATURE_VARIATION in the creature raws sends in arguments, you can use them below as !ARG1, !ARG2, etc.  The GAIT variations below have some examples.  In the creature raws, if an argument is of the form "5|6", for example, it'll be converted to "5:6" in the creature variation, so you can handle variable-token arguments with the | character.

    Conditional tags:
    Change TAG to CTAG and add, for example, CV_REMOVE_CTAG:1:YES:
     to require !ARG1 to be YES to execute the changes.

    [CREATURE_VARIATION:ANIMAL_PERSON]
        [CV_REMOVE_TAG:NAME]
        [CV_REMOVE_TAG:GENERAL_CHILD_NAME]
        [CV_REMOVE_TAG:GENERAL_BABY_NAME]
        [CV_REMOVE_TAG:CASTE_NAME]
        [CV_REMOVE_TAG:CHILDNAME]
        [CV_REMOVE_TAG:BABYNAME]
        [CV_REMOVE_TAG:SMALL_REMAINS]
        [CV_REMOVE_TAG:DESCRIPTION]
        [CV_REMOVE_TAG:CREATURE_TILE]
        [CV_REMOVE_TAG:COLOR]
        [CV_REMOVE_TAG:MAXAGE]
        [CV_REMOVE_TAG:SOUND]
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
        [CV_REMOVE_TAG:IMMOBILE_LAND]
        [CV_REMOVE_TAG:TRIGGERABLE_GROUP]
        [CV_REMOVE_TAG:MOUNT]
        [CV_REMOVE_TAG:PET_EXOTIC]
        [CV_REMOVE_TAG:MOUNT_EXOTIC]
        [CV_REMOVE_TAG:NOT_BUTCHERABLE]
        [CV_REMOVE_TAG:SPEED]
        [CV_REMOVE_TAG:SWIM_SPEED]
        [CV_REMOVE_TAG:MUNDANE]
        [CV_REMOVE_TAG:POPULATION_NUMBER]
        [CV_REMOVE_TAG:CLUSTER_NUMBER]
        [CV_REMOVE_TAG:ATTACK]
        [CV_REMOVE_TAG:ATTACK_SKILL]
        [CV_REMOVE_TAG:ATTACK_VERB]
        [CV_REMOVE_TAG:ATTACK_CONTACT_PERC]
        [CV_REMOVE_TAG:ATTACK_PRIORITY]
        [CV_REMOVE_TAG:ATTACK_FLAG_WITH]
        [CV_REMOVE_TAG:ATTACK_PENETRATION_PERC]
        [CV_REMOVE_TAG:ATTACK_PREPARE_AND_RECOVER]
        [CV_REMOVE_TAG:ATTACK_FLAG_EDGE]
        [CV_REMOVE_TAG:ATTACK_FLAG_CANLATCH]
        [CV_REMOVE_TAG:SPECIALATTACK_INJECT_EXTRACT]
        [CV_REMOVE_TAG:SPECIALATTACK_SUCK_BLOOD]
        [CV_REMOVE_TAG:ATTACK_VELOCITY_MODIFIER]
        [CV_REMOVE_TAG:GAIT]
        [CV_REMOVE_TAG:UBIQUITOUS]
        [CV_REMOVE_TAG:MEANDERER]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:BODY]
            [CVCT_TARGET:QUADRUPED]
            [CVCT_REPLACEMENT:HUMANOID]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:BODY]
            [CVCT_TARGET:QUADRUPED_FRONT_GRASP]
            [CVCT_REPLACEMENT:HUMANOID]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:BODY]
            [CVCT_TARGET:QUADRUPED_NECK]
            [CVCT_REPLACEMENT:HUMANOID_NECK:3FINGERS]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:BODY]
            [CVCT_TARGET:QUADRUPED_NECK_FRONT_GRASP]
            [CVCT_REPLACEMENT:HUMANOID_NECK]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:BODY]
            [CVCT_TARGET:QUADRUPED_HOOF]
            [CVCT_REPLACEMENT:HUMANOID_HOOF:3FINGERS]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:BODY]
            [CVCT_TARGET:QUADRUPED_NECK_HOOF]
            [CVCT_REPLACEMENT:HUMANOID_NECK_HOOF:3FINGERS]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:BODY]
            [CVCT_TARGET:HUMANOID_ARMLESS]
            [CVCT_REPLACEMENT:HUMANOID:4FINGERS]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:BODY]
            [CVCT_TARGET:HUMANOID_ARMLESS_NECK]
            [CVCT_REPLACEMENT:HUMANOID_NECK:4FINGERS]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:BODY]
            [CVCT_TARGET:BODY_WITH_HEAD_FLAG]
            [CVCT_REPLACEMENT:HUMANOID:3FINGERS]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:BODY]
            [CVCT_TARGET:BASIC_1PARTBODY:BASIC_HEAD]
            [CVCT_REPLACEMENT:HUMANOID:3FINGERS]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:BODY]
            [CVCT_TARGET:BASIC_2PARTBODY:BASIC_HEAD]
            [CVCT_REPLACEMENT:HUMANOID:3FINGERS]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:BODY]
            [CVCT_TARGET:BASIC_1PARTBODY:BASIC_HEAD_NECK]
            [CVCT_REPLACEMENT:HUMANOID_NECK:3FINGERS]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:BODY]
            [CVCT_TARGET:BASIC_2PARTBODY:BASIC_HEAD_NECK]
            [CVCT_REPLACEMENT:HUMANOID_NECK:3FINGERS]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:BODY]
            [CVCT_TARGET:INSECT]
            [CVCT_REPLACEMENT:HUMANOID_4ARMS:3FINGERS]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:BODY]
            [CVCT_TARGET:INSECT_4LEGS_2ARMS]
            [CVCT_REPLACEMENT:HUMANOID:3FINGERS]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:BODY]
            [CVCT_TARGET:SPIDER]
            [CVCT_REPLACEMENT:HUMANOID_6ARMS:3FINGERS]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:BODY]
            [CVCT_TARGET:5TOES_FQ_FINGERS]
            [CVCT_REPLACEMENT:5FINGERS]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:BODY]
            [CVCT_TARGET:4TOES_FQ_FINGERS]
            [CVCT_REPLACEMENT:4FINGERS]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:BODY]
            [CVCT_TARGET:3TOES_FQ_FINGERS]
            [CVCT_REPLACEMENT:3FINGERS]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:BODY]
            [CVCT_TARGET:5TOES_FQ_REG]
            [CVCT_REPLACEMENT:5FINGERS]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:BODY]
            [CVCT_TARGET:4TOES_FQ_REG]
            [CVCT_REPLACEMENT:4FINGERS]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:BODY]
            [CVCT_TARGET:3TOES_FQ_REG]
            [CVCT_REPLACEMENT:3FINGERS]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:BODY]
            [CVCT_TARGET:5TOES_RQ_ANON]
            [CVCT_REPLACEMENT:5TOES]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:BODY]
            [CVCT_TARGET:4TOES_RQ_ANON]
            [CVCT_REPLACEMENT:4TOES]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:BODY]
            [CVCT_TARGET:3TOES_RQ_ANON]
            [CVCT_REPLACEMENT:3TOES]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:BODY]
            [CVCT_TARGET:5TOES_RQ_REG]
            [CVCT_REPLACEMENT:5TOES]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:BODY]
            [CVCT_TARGET:4TOES_RQ_REG]
            [CVCT_REPLACEMENT:4TOES]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:BODY]
            [CVCT_TARGET:3TOES_RQ_REG]
            [CVCT_REPLACEMENT:3TOES]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:BIOME]
            [CVCT_TARGET:ANY_POOL]
            [CVCT_REPLACEMENT:ANY_LAKE]
        [CV_NEW_TAG:LARGE_ROAMING]
        [CV_NEW_TAG:SAVAGE]
        [CV_NEW_TAG:SELECT_CASTE:ALL]
            [CV_NEW_TAG:GRAVITATE_BODY_SIZE:70000]
            [CV_NEW_TAG:CHANGE_FREQUENCY_PERC:10]
        [CV_NEW_TAG:CAN_LEARN]
        [CV_NEW_TAG:CAN_SPEAK]
        [CV_NEW_TAG:EQUIPS]
        [CV_NEW_TAG:CANOPENDOORS]
        [CV_NEW_TAG:LOCAL_POPS_CONTROLLABLE]
        [CV_NEW_TAG:LOCAL_POPS_PRODUCE_HEROES]
        [CV_NEW_TAG:CAN_DO_INTERACTION:PET_ANIMAL]
            [CV_NEW_TAG:CDI:ADV_NAME:Pet animal]
            [CV_NEW_TAG:CDI:USAGE_HINT:GREETING]
            [CV_NEW_TAG:CDI:BP_REQUIRED:BY_TYPE:GRASP]
            [CV_NEW_TAG:CDI:VERB:pet:pets:pets]
            [CV_NEW_TAG:CDI:TARGET:A:SELF_ONLY]
            [CV_NEW_TAG:CDI:TARGET:B:TOUCHABLE]
            [CV_NEW_TAG:CDI:TARGET_RANGE:B:1]
            [CV_NEW_TAG:CDI:MAX_TARGET_NUMBER:B:1]
            [CV_NEW_TAG:CDI:WAIT_PERIOD:20]

    Legless animal person creature variation raws

    [CREATURE_VARIATION:ANIMAL_PERSON_LEGLESS]
        [CV_REMOVE_TAG:NAME]
        [CV_REMOVE_TAG:GENERAL_CHILD_NAME]
        [CV_REMOVE_TAG:GENERAL_BABY_NAME]
        [CV_REMOVE_TAG:CASTE_NAME]
        [CV_REMOVE_TAG:CHILDNAME]
        [CV_REMOVE_TAG:BABYNAME]
        [CV_REMOVE_TAG:SMALL_REMAINS]
        [CV_REMOVE_TAG:DESCRIPTION]
        [CV_REMOVE_TAG:CREATURE_TILE]
        [CV_REMOVE_TAG:COLOR]
        [CV_REMOVE_TAG:MAXAGE]
        [CV_REMOVE_TAG:SOUND]
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
        [CV_REMOVE_TAG:IMMOBILE_LAND]
        [CV_REMOVE_TAG:TRIGGERABLE_GROUP]
        [CV_REMOVE_TAG:PET_EXOTIC]
        [CV_REMOVE_TAG:NOT_BUTCHERABLE]
        [CV_REMOVE_TAG:SPEED]
        [CV_REMOVE_TAG:SWIM_SPEED]
        [CV_REMOVE_TAG:MUNDANE]
        [CV_REMOVE_TAG:POPULATION_NUMBER]
        [CV_REMOVE_TAG:CLUSTER_NUMBER]
        [CV_REMOVE_TAG:ATTACK]
        [CV_REMOVE_TAG:ATTACK_SKILL]
        [CV_REMOVE_TAG:ATTACK_VERB]
        [CV_REMOVE_TAG:ATTACK_CONTACT_PERC]
        [CV_REMOVE_TAG:ATTACK_PRIORITY]
        [CV_REMOVE_TAG:ATTACK_FLAG_WITH]
        [CV_REMOVE_TAG:ATTACK_PENETRATION_PERC]
        [CV_REMOVE_TAG:ATTACK_PREPARE_AND_RECOVER]
        [CV_REMOVE_TAG:ATTACK_FLAG_EDGE]
        [CV_REMOVE_TAG:ATTACK_FLAG_CANLATCH]
        [CV_REMOVE_TAG:SPECIALATTACK_INJECT_EXTRACT]
        [CV_REMOVE_TAG:SPECIALATTACK_SUCK_BLOOD]
        [CV_REMOVE_TAG:ATTACK_VELOCITY_MODIFIER]
        [CV_REMOVE_TAG:GAIT]
        [CV_REMOVE_TAG:UBIQUITOUS]
        [CV_REMOVE_TAG:MEANDERER]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:BODY]
            [CVCT_TARGET:QUADRUPED]
            [CVCT_REPLACEMENT:HUMANOID_LEGLESS]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:BODY]
            [CVCT_TARGET:QUADRUPED_NECK]
            [CVCT_REPLACEMENT:HUMANOID_LEGLESS_NECK:3FINGERS]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:BODY]
            [CVCT_TARGET:QUADRUPED_HOOF]
            [CVCT_REPLACEMENT:HUMANOID_LEGLESS:3FINGERS]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:BODY]
            [CVCT_TARGET:QUADRUPED_NECK_HOOF]
            [CVCT_REPLACEMENT:HUMANOID_LEGLESS_NECK:3FINGERS]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:BODY]
            [CVCT_TARGET:HUMANOID_ARMLESS]
            [CVCT_REPLACEMENT:HUMANOID_LEGLESS:4FINGERS]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:BODY]
            [CVCT_TARGET:HUMANOID_ARMLESS_NECK]
            [CVCT_REPLACEMENT:HUMANOID_LEGLESS_NECK:4FINGERS]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:BODY]
            [CVCT_TARGET:BODY_WITH_HEAD_FLAG]
            [CVCT_REPLACEMENT:HUMANOID_LEGLESS:3FINGERS]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:BODY]
            [CVCT_TARGET:BASIC_1PARTBODY:BASIC_HEAD]
            [CVCT_REPLACEMENT:HUMANOID_LEGLESS:3FINGERS]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:BODY]
            [CVCT_TARGET:BASIC_2PARTBODY:BASIC_HEAD]
            [CVCT_REPLACEMENT:HUMANOID_LEGLESS:3FINGERS]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:BODY]
            [CVCT_TARGET:BASIC_1PARTBODY:BASIC_HEAD_NECK]
            [CVCT_REPLACEMENT:HUMANOID_LEGLESS_NECK:3FINGERS]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:BODY]
            [CVCT_TARGET:BASIC_2PARTBODY:BASIC_HEAD_NECK]
            [CVCT_REPLACEMENT:HUMANOID_LEGLESS_NECK:3FINGERS]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:BODY]
            [CVCT_TARGET:INSECT]
            [CVCT_REPLACEMENT:HUMANOID_LEGLESS_4ARMS:3FINGERS]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:BODY]
            [CVCT_TARGET:SPIDER]
            [CVCT_REPLACEMENT:HUMANOID_LEGLESS_6ARMS:3FINGERS]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:BODY]
            [CVCT_TARGET:5TOES_FQ_FINGERS]
            [CVCT_REPLACEMENT:5FINGERS]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:BODY]
            [CVCT_TARGET:4TOES_FQ_FINGERS]
            [CVCT_REPLACEMENT:4FINGERS]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:BODY]
            [CVCT_TARGET:3TOES_FQ_FINGERS]
            [CVCT_REPLACEMENT:3FINGERS]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:BODY]
            [CVCT_TARGET:5TOES_FQ_REG]
            [CVCT_REPLACEMENT:5FINGERS]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:BODY]
            [CVCT_TARGET:4TOES_FQ_REG]
            [CVCT_REPLACEMENT:4FINGERS]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:BODY]
            [CVCT_TARGET:3TOES_FQ_REG]
            [CVCT_REPLACEMENT:3FINGERS]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:BODY]
            [CVCT_TARGET:5TOES_RQ_ANON]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:BODY]
            [CVCT_TARGET:4TOES_RQ_ANON]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:BODY]
            [CVCT_TARGET:3TOES_RQ_ANON]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:BODY]
            [CVCT_TARGET:5TOES_RQ_REG]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:BODY]
            [CVCT_TARGET:4TOES_RQ_REG]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:BODY]
            [CVCT_TARGET:3TOES_RQ_REG]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:BIOME]
            [CVCT_TARGET:ANY_POOL]
            [CVCT_REPLACEMENT:ANY_LAKE]
        [CV_NEW_TAG:LARGE_ROAMING]
        [CV_NEW_TAG:SAVAGE]
        [CV_NEW_TAG:SELECT_CASTE:ALL]
            [CV_NEW_TAG:GRAVITATE_BODY_SIZE:70000]
            [CV_NEW_TAG:CHANGE_FREQUENCY_PERC:10]
        [CV_NEW_TAG:CAN_LEARN]
        [CV_NEW_TAG:CAN_SPEAK]
        [CV_NEW_TAG:EQUIPS]
        [CV_NEW_TAG:CANOPENDOORS]
        [CV_NEW_TAG:LOCAL_POPS_CONTROLLABLE]
        [CV_NEW_TAG:LOCAL_POPS_PRODUCE_HEROES]
        [CV_NEW_TAG:CAN_DO_INTERACTION:PET_ANIMAL]
            [CV_NEW_TAG:CDI:ADV_NAME:Pet animal]
            [CV_NEW_TAG:CDI:USAGE_HINT:GREETING]
            [CV_NEW_TAG:CDI:BP_REQUIRED:BY_TYPE:GRASP]
            [CV_NEW_TAG:CDI:VERB:pet:pets:pets]
            [CV_NEW_TAG:CDI:TARGET:A:SELF_ONLY]
            [CV_NEW_TAG:CDI:TARGET:B:TOUCHABLE]
            [CV_NEW_TAG:CDI:TARGET_RANGE:B:1]
            [CV_NEW_TAG:CDI:MAX_TARGET_NUMBER:B:1]
            [CV_NEW_TAG:CDI:WAIT_PERIOD:20]

## Subterranean animal people

-  / `a` Amphibian man
-  / `a` Antman
-  / `b` Bat man
-  / `f` Cave fish man
-  / `s` Cave swallow man
-  / `o` Olm man
-  / `r` Reptile man
-  / `r` Rodent man
-  / `s` Serpent man

### Ethics

Being an entity in their own right, subterranean animal people possess ethics, much like other civs. Those particular ethics are incomplete for now, being directly copied from kobolds and their cultural values all set to zero (neutral).

Like kobolds, subterranean animal people consider the killing of other living beings acceptable, but treason is unthinkable, and they'll respond to the murder of their own kind by exiling the offender from their tribe. They oppose torturing for information and the torture of animals, but consider torturing for fun appropriate. Assault is considered a personal matter, while slavery, the taking of animal trophies, and the consumption of sapient beings (which includes other animal people) are all unthinkable acts.

## Savage animal people

-  / `a` Aardvark man
-  / `a` Adder man
-  / `a` Albatross man
-  / `A` Alligator man
-  / `A` Anaconda man
-  / `a` Anole man
-  / `a` Armadillo man
-  / `a` Axolotl man
-  / `a` Aye-aye man
-  / `b` Badger man
-  / `s` Bark scorpion man
-  / `b` Barn owl man
-  / `b` Beaver man
-  / `b` Beetle man
-  / `B` Black bear man
-  / `s` Black mamba man
-  / `b` Bluejay man
-  / `b` Bobcat man
-  / `s` Brown recluse spider man
-  / `s` Bushmaster man
-  / `b` Bushtit man
-  / `b` Buzzard man
-  / `c` Capuchin man
-  / `c` Capybara man
-  / `c` Cardinal man
-  / `c` Cassowary man
-  / `c` Chameleon man
-  / `c` Cheetah man
-  / `c` Chinchilla man
-  / `c` Chipmunk man
-  / `c` Coati man
-  / `c` Cockatiel man
-  / `s` Copperhead snake man
-  / `c` Cougar man
-  / `c` Coyote man
-  / `c` Crab man
-  / `c` Crow man
-  / `c` Cuttlefish man
-  / `d` Damselfly man
-  / `d` Deer man
-  / `t` Desert tortoise man
-  / `d` Dingo man
-  / `d` Dragonfly man
-  / `e` Eagle man
-  / `e` Echidna man
-  / `E` Elephant man
-  / `S` Elephant seal man
-  / `E` Elk man
-  / `E` Emu man
-  / `f` Firefly man
-  / `f` Fly man
-  / `f` Flying squirrel man
-  / `f` Fox man
-  / `g` Gazelle man
-  / `T` Giant tortoise man
-  / `g` Gila monster man
-  / `G` Giraffe man
-  / `g` Grackle man
-  / `g` Grasshopper man
-  / `l` Gray langur man
-  / `s` Gray squirrel man
-  / `o` Great horned owl man
-  / `f` Green tree frog man
-  / `p` Grey parrot man
-  / `B` Grizzly bear man
-  / `g` Groundhog man
-  / `h` Hamster man
-  / `h` Hare man
-  / `h` Harp seal man
-  / `h` Hedgehog man
-  / `H` Hippo man
-  / `m` Hoary marmot man
-  / `b` Honey badger man
-  / `h` Hornbill man
-  / `h` Horseshoe crab man
-  / `h` Hyena man
-  / `i` Ibex man
-  / `i` Iguana man
-  / `i` Impala man
-  / `j` Jackal man
-  / `J` Jaguar man
-  / `s` Jumping spider man
-  / `k` Kakapo man
-  / `K` Kangaroo man
-  / `k` Kea man
-  / `k` Kestrel man
-  / `k` King cobra man
-  / `k` Kingsnake man
-  / `k` Kiwi man
-  / `k` Koala man
-  / `l` Leech man
-  / `g` Leopard gecko man
-  / `l` Leopard man
-  / `L` Leopard seal man
-  / `L` Lion man
-  / `l` Lion tamarin man
-  / `l` Lizard man
-  / `l` Loon man
-  / `l` Lorikeet man
-  / `l` Louse man
-  / `l` Lynx man
-  / `m` Magpie man
-  / `m` Mandrill man
-  / `m` Mantis man
-  / `l` Masked lovebird man
-  / `m` Mink man
-  / `b` Monarch butterfly man
-  / `m` Mongoose man
-  / `M` Monitor lizard man
-  / `s` Moon snail man
-  / `M` Moose man
-  / `m` Mosquito man
-  / `m` Moth man
-  / `g` Mountain goat man
-  / `M` Muskox man
-  / `N` Narwhal man
-  / `n` Nautilus man
-  / `o` Ocelot man
-  / `o` Octopus man
-  / `C` One-humped camel man
-  / `o` Opossum man
-  / `O` Orca man
-  / `o` Oriole man
-  / `o` Osprey man
-  / `O` Ostrich man
-  / `o` Otter man
-  / `P` Panda man
-  / `p` Pangolin man
-  / `p` Parakeet man
-  / `l` Peach-faced lovebird man
-  / `p` Penguin man
-  / `p` Peregrine falcon man
-  / `p` Platypus man
-  / `B` Polar bear man
-  / `t` Pond turtle man
-  / `p` Porcupine man
-  / `p` Puffin man
-  / `S` Python man
-  / `r` Raccoon man
-  / `r` Rat man
-  / `s` Rattlesnake man
-  / `r` Raven man
-  / `r` Red panda man
-  / `r` Red squirrel man
-  / `r` Red-winged blackbird man
-  / `m` Rhesus macaque man
-  / `R` Rhinoceros man
-  / `r` Roach man
-  / `C` Saltwater crocodile man
-  / `s` Skink man
-  / `s` Skunk man
-  / `B` Sloth bear man
-  / `s` Sloth man
-  / `s` Slug man
-  / `s` Snail man
-  / `t` Snapping turtle man
-  / `o` Snowy owl man
-  / `s` Sparrow man
-  / `W` Sperm whale man
-  / `m` Spider monkey man
-  / `s` Sponge man
-  / `s` Squid man
-  / `s` Stoat man
-  / `s` Swan man
-  / `T` Tapir man
-  / `t` Thrips man
-  / `t` Tick man
-  / `T` Tiger man
-  / `t` Toad man
-  / `C` Two-humped camel man
-  / `v` Vulture man
-  / `W` Walrus man
-  / `W` Warthog man
-  / `w` Weasel man
-  / `s` White stork man
-  / `B` Wild boar man
-  / `w` Wolf man
-  / `w` Wolverine man
-  / `w` Wombat man
-  / `w` Worm man
-  / `w` Wren man

## Body structure

While the standard description, *"A person with the head of a..."*, suggests a human-like body like a minotaur has, animal people use the same tissue types as their base animal. For example, insect people have a chitin exoskeleton, while mammalian people are covered in fur.

If the base creature does not normally have arms, then they get a single, three-fingered pair of arms by default. Insect bodies have four arms, and arachnids get six - mantis men are an exception, only having two (deadly) arms, as a mantis uses `[``BODY``:INSECT_4LEGS_2ARMS]` instead of `[``BODY``:INSECT]`. Bird men receive a pair of four-fingered arms in addition to their wings, whereas bat men have a single pair of arm-wings. Unlike other arthropods, crustacean people only have two arms, with no fingers.

Most, but not all, animal people have a pair of legs. Creatures with hooves or flippers will use those for locomotion, while species without toes do not gain any. A rule of thumb is that creatures that end in a tail remain legless as animal people. Due to graphical oversights, the sprite for some creatures (such as the snail man) may not match their body plan.

Animal people keep any additional body parts their species may have, including the head-arms of cephalopod people and the pincers of a bark scorpion man, as well as tails, shells, horns, or internal organs.

## Animal people organized by attributes

@ Probably only functions as a citizen in Fortress Mode\[Verify\]

\+ Probably only functions in Adventure Mode\[Verify\]

\(#\) Probably only functions for procedurally generated "mob spawns" and not for adventurers\[Verify\]

|  |  |  |
|----|----|----|
| Attribute | Effect | Species of animal person |
| **Amphibious** | Move and breathe normally on water AND dry land | Alligator man \| Amphibian man \| Axolotl man \| Capybara man \| Cave fish man \| Crab man \| Elephant seal man \| Gila monster man \| Green tree frog man \| Harp seal man \| Hippo man \| Horseshoe crab man \| Leopard seal man \| Olm man \| Otter man \| Platypus man \| Pond turtle man \| Reptile man \| Saltwater crocodile man \| Serpent man \| Snapping turtle man \| Toad man \| Walrus man |
| **Aquatic** | Move and breathe normally in water, but drown in less than 4/7 units of water. | Cuttlefish man \| Moon snail man \| Narwhal man \| Nautilus man \| Octopus man \| Orca man \| Sperm whale man \| Sponge man \| Squid man |
| **Ectothermic** | Does not have internal body temperature | Assumedly all species of reptiles, amphibians, arthropods, etc. |
| **Egglaying@** | Females will lay (sterile) eggs if given a nest box to claim | Assumedly all species of egglaying birds, reptiles, etc. |
| **Flying+(bugged)** | Can fly through the air | Antman (only Drone caste) \| Albatross man \| Barn owl man \| Bat man \| Bluejay man \| Bushtit man \| Buzzard man \| Cardinal man \| Cave swallow man \| Crow man \| Damselfly man \| Dragonfly man \| Eagle man \| Firefly man \| Fly man \| Grackle man \| Great horned owl man \| Grey parrot man \| Hornbill man \| Kea man \| Kestrel man \| Loon man \| Lorikeet man \| Magpie man \| Mantis man \| Masked lovebird man \| Monarch butterfly man \| Mosquito man \| Moth man \| Oriole man \| Osprey man \| Parakeet man \| Peach-faced lovebird man \| Peregrine falcon man \| Puffin man \| Raven man \| Red-winged blackbird man \| Roach man \| Snowy owl man \| Sparrow man \| Swan man \| Thrips man \| Vulture man \| Wren man |
| **Genderless** | Cannot breed in normal gameplay | Leech man \| Slug man \| Snail man \| Sponge man \| Worm man |
| **No Pain** | Feels no pain | Bark scorpion man \| Brown recluse spider man \| Jumping spider man |
| **No Stun** | Cannot be stunned | Bark scorpion man \| Brown recluse spider man \| Jumping spider man |
| **Shell** | Has a shell that can be yielded if butchered, however, dwarves won't butcher animal people in non-modded DF. | Armadillo man \| Desert tortoise man \| Giant tortoise man \| Moon snail man \| Nautilus man \| Pond turtle man \| Snail man \| Snapping turtle man |
| **Steals drink(#)** | Approaches any available drink and steals it, guzzling entire barrels at once, on the spot. | Black bear man \| Grizzly bear man \| Polar bear man \| Sloth bear man |
| **Steals food(#)** | Approaches any available food and steals it, carrying a stack of food off-map. | Black bear man \| Buzzard man \| Capuchin man \| Coati man \| Gray langur man \| Grizzly bear man \| Honey badger man \| Kea man \| Mandrill man \| Polar bear man \| Raccoon man \| Rhesus macaque man \| Sloth bear man \| Vulture man |
| **Steals items(#)** | Approaches an item and steals it, carrying it off-map. | Capuchin man \| Coati man \| Gray langur man \| Kea man \| Mandrill man \| Raccoon man \| Rhesus macaque man |
| **Syndrome** | Venoms that cause various symptoms, usually applied by bite or a special sting attack | Adder man \| Bark scorpion man \| Black mamba man \| Brown recluse spider man \| Bushmaster man \| Copperhead snake man \| Gila monster man \| King cobra man \| Platypus man \| Rattlesnake man |
| **Webs** | Can move through webbing and collect it in adventure mode with g. No web spray attack included. | Brown recluse spider man |

**(All animal people have the Learning and Humanoid Attributes)**

## Animal people organized by taxonomy

|  |  |  |  |  |
|----|----|----|----|----|
| Phylum | Class | Order | Family | Species |
| Annelida |  |  |  | Worm man |
| Annelida | Clitellata |  |  | Leech man |
| Arthropoda | Arachnida | Araneae | Salticidae | Jumping spider man |
| Arthropoda | Arachnida | Araneae | Sicariidae | Brown recluse spider man |
| Arthropoda | Arachnida | Ixodida |  | Tick man |
| Arthropoda | Arachnida | Scorpiones | Buthidae | Bark scorpion man |
| Arthropoda | Insecta | Odonatoptera: Odonata |  | Damselfly man |
| Arthropoda | Insecta | Odonatoptera: Odonata |  | Dragonfly man |
| Arthropoda | Insecta: Eumetabola | Holometabola: Coleoptera |  | Beetle man |
| Arthropoda | Insecta: Eumetabola | Holometabola: Coleoptera | Lampyridae | Firefly man |
| Arthropoda | Insecta: Eumetabola | Holometabola: Hymenoptera | Formicidae | Ant man |
| Arthropoda | Insecta: Eumetabola | Panorpida: Diptera |  | Fly man |
| Arthropoda | Insecta: Eumetabola | Panorpida: Diptera | Culicidae | Mosquito man |
| Arthropoda | Insecta: Eumetabola | Panorpida: Lepidoptera |  | Moth man |
| Arthropoda | Insecta: Eumetabola | Panorpida: Lepidoptera | Nymphalidae | Monarch butterfly man |
| Arthropoda | Insecta: Eumetabola | Paraneoptera: Psocodea |  | Louse man |
| Arthropoda | Insecta: Eumetabola | Paraneoptera: Thysanoptera |  | Thrips man |
| Arthropoda | Insecta: Polyneoptera | Dictyoptera: Blattodea |  | Roach man |
| Arthropoda | Insecta: Polyneoptera | Dictyoptera: Mantodea |  | Mantis man |
| Arthropoda | Insecta: Polyneoptera | Orthopteroidea: Orthoptera |  | Grasshopper man |
| Arthropoda | Malacostraca | Decapoda |  | Crab man |
| Arthropoda | Merostomata\* | Xiphosura | Limulidae | Horseshoe crab man |
| Chordata | Actinopterygii | \*\* |  | Cave fish man |
| Chordata | Amphibia |  |  | Amphibian man |
| Chordata | Amphibia | Anura |  | Green tree frog man |
| Chordata | Amphibia | Anura |  | Toad man |
| Chordata | Amphibia | Urodela | Ambystomatidae | Axolotl man |
| Chordata | Amphibia | Urodela | Proteidae | Olm man |
| Chordata | Aves: Elementaves:Gruimorphae | Charadriiformes | Alcidae | Puffin man |
| Chordata | Aves: Elementaves:Aequornithes | Gaviiformes | Gaviidae | Loon man |
| Chordata | Aves: Elementaves:Aequornithes | Procellariiformes | Diomedeidae | Albatross man |
| Chordata | Aves: Elementaves:Aequornithes | Sphenisciformes | Spheniscidae | Penguin man |
| Chordata | Aves: Elementaves:Aequornithes | Ciconiiformes | Ciconiidae | White stork man |
| Chordata | Aves: Galloanserae | Anseriformes | Anatidae | Swan man |
| Chordata | Aves: Palaeognathae | Apterygiformes | Apterygidae | Kiwi man |
| Chordata | Aves: Palaeognathae | Casuariiformes | Casuariidae | Cassowary man |
| Chordata | Aves: Palaeognathae | Casuariiformes | Casuariidae | Emu man |
| Chordata | Aves: Palaeognathae | Struthioniformes | Struthionidae | Ostrich man |
| Chordata | Aves: Palaeognathae or Telluraves:Afroaves | Casuariidae or Accipitriformes | Cathartidae or Accipitridae | Vulture man |
| Chordata | Aves: Telluraves:Afroaves | Accipitriformes | Accipitridae or Cathartidae | Buzzard man |
| Chordata | Aves: Telluraves:Afroaves | Accipitriformes | Accipitridae | Eagle man |
| Chordata | Aves: Telluraves:Afroaves | Accipitriformes | Pandionidae | Osprey man |
| Chordata | Aves: Telluraves:Afroaves | Bucerotiformes | Bucerotidae | Hornbill man |
| Chordata | Aves: Telluraves:Afroaves | Strigiformes | Strigidae | Great horned owl man |
| Chordata | Aves: Telluraves:Afroaves | Strigiformes | Strigidae | Snowy owl man |
| Chordata | Aves: Telluraves:Afroaves | Strigiformes | Tytonidae | Barn owl man |
| Chordata | Aves: Telluraves:Australaves | Falconiformes | Falconidae | Kestrel man |
| Chordata | Aves: Telluraves:Australaves | Falconiformes | Falconidae | Peregrine falcon man |
| Chordata | Aves: Telluraves:Australaves | Passeriformes: Corvides | Corvidae | Bluejay man |
| Chordata | Aves: Telluraves:Australaves | Passeriformes: Corvides | Corvidae | Crow man |
| Chordata | Aves: Telluraves:Australaves | Passeriformes: Corvides | Corvidae | Magpie man |
| Chordata | Aves: Telluraves:Australaves | Passeriformes: Corvides | Corvidae | Raven man |
| Chordata | Aves: Telluraves:Australaves | Passeriformes: Corvides or Passerida | Icteridae or Oriolidae | Oriole man |
| Chordata | Aves: Telluraves:Australaves | Passeriformes: Passerida | Aegithalidae | Bushtit man |
| Chordata | Aves: Telluraves:Australaves | Passeriformes: Passerida | Cardinalidae | Cardinal man |
| Chordata | Aves: Telluraves:Australaves | Passeriformes: Passerida | Icteridae | Grackle man |
| Chordata | Aves: Telluraves:Australaves | Passeriformes: Passerida | Icteridae | Red-winged blackbird man |
| Chordata | Aves: Telluraves:Australaves | Passeriformes: Passerida | Passerellidae or Passeridae | Sparrow man |
| Chordata | Aves: Telluraves:Australaves | Passeriformes: Passerida | Troglodytidae | Wren man |
| Chordata | Aves: Telluraves:Australaves | Psittaciformes | Cacatuoidea: Cacatuidae | Cockatiel man |
| Chordata | Aves: Telluraves:Australaves | Psittaciformes | Psittacoidea: Psittacidae | Grey parrot man |
| Chordata | Aves: Telluraves:Australaves | Psittaciformes | Psittacoidea: Psittaculidae | Lorikeet man |
| Chordata | Aves: Telluraves:Australaves | Psittaciformes | Psittacoidea: Psittaculidae | Masked lovebird man |
| Chordata | Aves: Telluraves:Australaves | Psittaciformes | Psittacoidea: Psittaculidae | Peach-faced lovebird man |
| Chordata | Aves: Telluraves:Australaves | Psittaciformes | Psittacoidea: Psittaculidae or Psittacidae | Parakeet man |
| Chordata | Aves: Telluraves:Australaves | Psittaciformes | Strigopoidea: Strigopidae | Kakapo man |
| Chordata | Aves: Telluraves:Australaves | Psittaciformes | Strigopoidea: Strigopidae | Kea man |
| Chordata | Mammalia: Atlantogenata | Afrotheria: Tubulidentata | Orycteropodidae | Aardvark man |
| Chordata | Mammalia: Atlantogenata | Afrotheria: Proboscidea | Elephantidae | Elephant man |
| Chordata | Mammalia: Atlantogenata | Xenarthra: Cingulata |  | Armadillo man |
| Chordata | Mammalia: Atlantogenata | Xenarthra: Pilosa |  | Sloth man |
| Chordata | Mammalia: Euarchontoglires | Lagomorpha | Leporidae | Hare man |
| Chordata | Mammalia: Euarchontoglires | Primates: Platyrrhini | Atelidae | Spider monkey man |
| Chordata | Mammalia: Euarchontoglires | Primates: Platyrrhini | Callitrichidae | Lion tamarin man |
| Chordata | Mammalia: Euarchontoglires | Primates: Platyrrhini | Cebidae | Capuchin man |
| Chordata | Mammalia: Euarchontoglires | Primates: Catarrhini | Cercopithecidae | Gray langur man |
| Chordata | Mammalia: Euarchontoglires | Primates: Catarrhini | Cercopithecidae | Mandrill man |
| Chordata | Mammalia: Euarchontoglires | Primates: Catarrhini | Cercopithecidae | Rhesus macaque man |
| Chordata | Mammalia: Euarchontoglires | Primates: Lemuriformes | Daubentoniidae | Aye-aye man |
| Chordata | Mammalia: Euarchontoglires | Rodentia: Castorimorpha | Castoridae | Beaver man |
| Chordata | Mammalia: Euarchontoglires | Rodentia: Caviomorpha | Caviidae | Capybara man |
| Chordata | Mammalia: Euarchontoglires | Rodentia: Caviomorpha | Chinchillidae | Chinchilla man |
| Chordata | Mammalia: Euarchontoglires | Rodentia: Caviomorpha | Erethizontidae | Porcupine man |
| Chordata | Mammalia: Euarchontoglires | Rodentia: Myomorpha (probably) |  | Rodent man |
| Chordata | Mammalia: Euarchontoglires | Rodentia: Myomorpha | Cricetidae | Hamster man |
| Chordata | Mammalia: Euarchontoglires | Rodentia: Myomorpha | Muridae (possibly Cricetidae or Heteromyidae) | Rat man |
| Chordata | Mammalia: Euarchontoglires | Rodentia: Sciuromorpha | Sciuridae: Sciurinae | Flying squirrel man |
| Chordata | Mammalia: Euarchontoglires | Rodentia: Sciuromorpha | Sciuridae: Sciurinae | Gray squirrel man |
| Chordata | Mammalia: Euarchontoglires | Rodentia: Sciuromorpha | Sciuridae: Sciurinae | Red squirrel man |
| Chordata | Mammalia: Euarchontoglires | Rodentia: Sciuromorpha | Sciuridae: Xerinae | Chipmunk man |
| Chordata | Mammalia: Euarchontoglires | Rodentia: Sciuromorpha | Sciuridae: Xerinae | Groundhog man |
| Chordata | Mammalia: Euarchontoglires | Rodentia: Sciuromorpha | Sciuridae: Xerinae | Hoary marmot man |
| Chordata | Mammalia: Laurasiatheria | Artiodactyla: Odontoceti | Delphinidae | Orca man |
| Chordata | Mammalia: Laurasiatheria | Artiodactyla: Odontoceti | Monodontidae | Narwhal man |
| Chordata | Mammalia: Laurasiatheria | Artiodactyla: Odontoceti | Physeteridae | Sperm whale man |
| Chordata | Mammalia: Laurasiatheria | Artiodactyla: Pecora | Bovidae | Gazelle man |
| Chordata | Mammalia: Laurasiatheria | Artiodactyla: Pecora | Bovidae | Ibex man |
| Chordata | Mammalia: Laurasiatheria | Artiodactyla: Pecora | Bovidae | Impala man |
| Chordata | Mammalia: Laurasiatheria | Artiodactyla: Pecora | Bovidae | Mountain goat man |
| Chordata | Mammalia: Laurasiatheria | Artiodactyla: Pecora | Bovidae | Muskox man |
| Chordata | Mammalia: Laurasiatheria | Artiodactyla: Pecora | Cervidae | Deer man |
| Chordata | Mammalia: Laurasiatheria | Artiodactyla: Pecora | Cervidae | Elk man |
| Chordata | Mammalia: Laurasiatheria | Artiodactyla: Pecora | Cervidae | Moose man |
| Chordata | Mammalia: Laurasiatheria | Artiodactyla: Pecora | Giraffidae | Giraffe man |
| Chordata | Mammalia: Laurasiatheria | Artiodactyla: Suina | Suidae | Warthog man |
| Chordata | Mammalia: Laurasiatheria | Artiodactyla: Suina | Suidae | Wild boar man |
| Chordata | Mammalia: Laurasiatheria | Artiodactyla: Tylopoda | Camelidae | One-humped camel man |
| Chordata | Mammalia: Laurasiatheria | Artiodactyla: Tylopoda | Camelidae | Two-humped camel man |
| Chordata | Mammalia: Laurasiatheria | Artiodactyla: Whippomorpha | Hippopotamidae | Hippo man |
| Chordata | Mammalia: Laurasiatheria | Chiroptera |  | Bat man |
| Chordata | Mammalia: Laurasiatheria | Eulipotyphla | Erinaceidae | Hedgehog man |
| Chordata | Mammalia: Laurasiatheria | Ferae: Carnivora: Arctoidea | Musteloidea: Ailuridae | Red panda man |
| Chordata | Mammalia: Laurasiatheria | Ferae: Carnivora: Arctoidea | Musteloidea: Mephitidae | Skunk man |
| Chordata | Mammalia: Laurasiatheria | Ferae: Carnivora: Arctoidea | Musteloidea: Mephitidae or Mustelidae | Badger man |
| Chordata | Mammalia: Laurasiatheria | Ferae: Carnivora: Arctoidea | Musteloidea: Mustelidae | Honey badger man |
| Chordata | Mammalia: Laurasiatheria | Ferae: Carnivora: Arctoidea | Musteloidea: Mustelidae | Mink man |
| Chordata | Mammalia: Laurasiatheria | Ferae: Carnivora: Arctoidea | Musteloidea: Mustelidae | Otter man |
| Chordata | Mammalia: Laurasiatheria | Ferae: Carnivora: Arctoidea | Musteloidea: Mustelidae | Stoat man |
| Chordata | Mammalia: Laurasiatheria | Ferae: Carnivora: Arctoidea | Musteloidea: Mustelidae | Weasel man |
| Chordata | Mammalia: Laurasiatheria | Ferae: Carnivora: Arctoidea | Musteloidea: Mustelidae | Wolverine man |
| Chordata | Mammalia: Laurasiatheria | Ferae: Carnivora: Arctoidea | Musteloidea: Procyonidae | Coati man |
| Chordata | Mammalia: Laurasiatheria | Ferae: Carnivora: Arctoidea | Musteloidea: Procyonidae | Raccoon man |
| Chordata | Mammalia: Laurasiatheria | Ferae: Carnivora: Arctoidea | Otarioidea: Odobenidae | Walrus man |
| Chordata | Mammalia: Laurasiatheria | Ferae: Carnivora: Arctoidea | Phocoidea: Phocidae | Elephant seal man |
| Chordata | Mammalia: Laurasiatheria | Ferae: Carnivora: Arctoidea | Phocoidea: Phocidae | Harp seal man |
| Chordata | Mammalia: Laurasiatheria | Ferae: Carnivora: Arctoidea | Phocoidea: Phocidae | Leopard seal man |
| Chordata | Mammalia: Laurasiatheria | Ferae: Carnivora: Arctoidea | Ursoidea: Ursidae | Black bear man |
| Chordata | Mammalia: Laurasiatheria | Ferae: Carnivora: Arctoidea | Ursoidea: Ursidae | Grizzly bear man |
| Chordata | Mammalia: Laurasiatheria | Ferae: Carnivora: Arctoidea | Ursoidea: Ursidae | Panda man |
| Chordata | Mammalia: Laurasiatheria | Ferae: Carnivora: Arctoidea | Ursoidea: Ursidae | Polar bear man |
| Chordata | Mammalia: Laurasiatheria | Ferae: Carnivora: Arctoidea | Ursoidea: Ursidae | Sloth bear man |
| Chordata | Mammalia: Laurasiatheria | Ferae: Carnivora: Cynoidea | Canidae | Coyote man |
| Chordata | Mammalia: Laurasiatheria | Ferae: Carnivora: Cynoidea | Canidae | Dingo man |
| Chordata | Mammalia: Laurasiatheria | Ferae: Carnivora: Cynoidea | Canidae | Fox man |
| Chordata | Mammalia: Laurasiatheria | Ferae: Carnivora: Cynoidea | Canidae | Jackal man |
| Chordata | Mammalia: Laurasiatheria | Ferae: Carnivora: Cynoidea | Canidae | Wolf man |
| Chordata | Mammalia: Laurasiatheria | Ferae: Carnivora: Feliformia | Felidae | Bobcat man |
| Chordata | Mammalia: Laurasiatheria | Ferae: Carnivora: Feliformia | Felidae | Cheetah man |
| Chordata | Mammalia: Laurasiatheria | Ferae: Carnivora: Feliformia | Felidae | Cougar man |
| Chordata | Mammalia: Laurasiatheria | Ferae: Carnivora: Feliformia | Felidae | Jaguar man |
| Chordata | Mammalia: Laurasiatheria | Ferae: Carnivora: Feliformia | Felidae | Leopard man |
| Chordata | Mammalia: Laurasiatheria | Ferae: Carnivora: Feliformia | Felidae | Lion man |
| Chordata | Mammalia: Laurasiatheria | Ferae: Carnivora: Feliformia | Felidae | Lynx man |
| Chordata | Mammalia: Laurasiatheria | Ferae: Carnivora: Feliformia | Felidae | Ocelot man |
| Chordata | Mammalia: Laurasiatheria | Ferae: Carnivora: Feliformia | Felidae | Tiger man |
| Chordata | Mammalia: Laurasiatheria | Ferae: Carnivora: Feliformia | Herpestoidea: Herpestidae | Mongoose man |
| Chordata | Mammalia: Laurasiatheria | Ferae: Carnivora: Feliformia | Herpestoidea: Hyaenidae | Hyena man |
| Chordata | Mammalia: Laurasiatheria | Ferae: Pholidota |  | Pangolin man |
| Chordata | Mammalia: Laurasiatheria | Perissodactyla | Rhinocerotidae | Rhinoceros man |
| Chordata | Mammalia: Laurasiatheria | Perissodactyla | Tapiridae | Tapir man |
| Chordata | Mammalia: Marsupialia | Didelphimorphia | Didelphidae | Opossum man |
| Chordata | Mammalia: Marsupialia | Diprotodontia | Macropodidae | Kangaroo man |
| Chordata | Mammalia: Marsupialia | Diprotodontia | Phascolarctidae | Koala man |
| Chordata | Mammalia: Marsupialia | Diprotodontia | Vombatidae | Wombat man |
| Chordata | Mammalia | Monotremata | Ornithorhynchidae | Platypus man |
| Chordata | Mammalia | Monotremata | Tachyglossidae | Echidna man |
| Chordata | Reptilia |  |  | Reptile man |
| Chordata | Reptilia | Crocodilia | Alligatoridae | Alligator man |
| Chordata | Reptilia | Crocodilia | Crocodylidae | Saltwater crocodile man |
| Chordata | Reptilia | Squamata: Gekkota:Gekkomorpha | Eublepharidae | Leopard gecko man |
| Chordata | Reptilia | Squamata: Scinciformata | Scincidae | Skink man |
| Chordata | Reptilia | Squamata: Laterata | Lacertoidea: Lacertidae | Lizard man |
| Chordata | Reptilia | Squamata: Toxicofera:Anguimorpha | Helodermatidae | Gila monster man |
| Chordata | Reptilia | Squamata: Toxicofera:Anguimorpha | Varanidae | Monitor lizard man |
| Chordata | Reptilia | Squamata: Toxicofera:Iguania | Chamaeleonidae | Chameleon man |
| Chordata | Reptilia | Squamata: Toxicofera:Iguania | Dactyloidae | Anole man |
| Chordata | Reptilia | Squamata: Toxicofera:Iguania | Iguanidae | Iguana man |
| Chordata | Reptilia | Squamata: Toxicofera:Serpentes |  | Serpent man |
| Chordata | Reptilia | Squamata: Toxicofera:Serpentes | Boidae | Anaconda man |
| Chordata | Reptilia | Squamata: Toxicofera:Serpentes | Colubridae | Kingsnake man |
| Chordata | Reptilia | Squamata: Toxicofera:Serpentes | Elapidae | Black mamba man |
| Chordata | Reptilia | Squamata: Toxicofera:Serpentes | Elapidae | King cobra man |
| Chordata | Reptilia | Squamata: Toxicofera:Serpentes | Pythonidae | Python man |
| Chordata | Reptilia | Squamata: Toxicofera:Serpentes | Viperidae | Adder man |
| Chordata | Reptilia | Squamata: Toxicofera:Serpentes | Viperidae | Bushmaster man |
| Chordata | Reptilia | Squamata: Toxicofera:Serpentes | Viperidae | Rattlesnake man |
| Chordata | Reptilia | Squamata: Toxicofera:Serpentes | Viperidae (or Elapidae or Colubridae) | Copperhead snake man |
| Chordata | Reptilia | Testudines | Chelydridae | Snapping turtle man |
| Chordata | Reptilia | Testudines | Emydidae or Geoemydidae | Pond turtle man |
| Chordata | Reptilia | Testudines | Testudinidae | Desert tortoise man |
| Chordata | Reptilia | Testudines | Testudinidae | Giant tortoise man |
| Mollusca | Cephalopoda: Coleoids | Octopodiformes: Octopoda |  | Octopus man |
| Mollusca | Cephalopoda: Coleoids | Decapodiformes: Sepiida |  | Cuttlefish man |
| Mollusca | Cephalopoda: Coleoids | Decapodiformes: |  | Squid man |
| Mollusca | Cephalopoda: Nautiloids | Nautilida | Nautilidae | Nautilus man |
| Mollusca | Gastropoda | Littorinimorpha | Naticidae | Moon snail man |
| Mollusca | Gastropoda |  |  | Slug man |
| Mollusca | Gastropoda |  |  | Snail man |
| Porifera |  |  |  | Sponge man |

The Animal Man Subkingdom

\* Merostomata is the historical order containing the Horseshoe crab man

\*\* Cave fish man is likely in one of these orders: Characiformes, Cypriniformes, Siluriformes, Gymnotiformes, Percopsiformes, Ophidiiformes, Cyprinodontiformes, Synbranchiformes, Scorpaeniformes, Gobiiformes, Anabantiformes

## History

Present from the first official release of the game, the animal people did not exist as a class but were instead part of a small group of subterranean creatures that harassed your dwarves. Frogmen, lizardmen, and snakemen emerged from cave rivers, and antmen, batmen, and ratmen would come out from chasms to attack.

v0.27.169.32a released three-dimensional worlds, and subterranean creatures were moved to flock near generated chasms, underground rivers, and underground pools. Cave swallowmen and olmmen were introduced. The first set of above-ground savage animal people were also introduced: leechmen, snailmen, slugmen, and tigermen.

In v0.31, every creature was renamed and/or had their properties revamped (for example, "frogman" was changed to "amphibian man" and "batman" was changed to "bat man"). Not all animal people were redefined in this version, and some continued to use old codes for many releases. The version also introduced "creature variation" templates, which made converting existing animals to humanoid (and giant) variations much more efficient. Underground features were expanded to the current caverns, and subterranean animal people formed civilizations. More anthropomorphic variations of animals present at the time were added.

More animal people were added to the game in v0.34.

v0.42.01 allowed animal people to join civilizations, live in sites, and visit forts. Animal people became playable as adventurers. (A grizzly bear hammerman, for example, has much to offer a dwarven society.) v0.42.04 added more animal people to the game.

## Bugs

- Animal people can't learn swimming. Bug:9853
