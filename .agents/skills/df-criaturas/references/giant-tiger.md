# Giant tiger

> Fonte: [Giant tiger](https://dwarffortresswiki.org/index.php/Giant_tiger) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant tigers for their large stripes, of course.**
- **Biome**
- **Any Tropical Forest Tropical Shrubland Tropical Freshwater Swamp Tropical Saltwater Swamp Mangrove Swamp**
- **Variations**
- **Tiger - Tiger man - Giant tiger**
- **Attributes**
- **Alignment:** Savage
- **War animals · Hunting animals · Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Trainable : Hunting War**
- **Size**
- **Birth:** 189,450 cm 3
- **Mid:** 842,000 cm 3
- **Max:** 1,894,500 cm 3
- **Age**
- **Adult at:** 3
- **Max age:** 10-20
- **Butchering returns ( Value multiplier ×3)**
- **Food items**
- **Meat:** 20
- **Fat:** 17
- **Brain:** 1
- **Heart:** 1
- **Lungs:** 2
- **Intestines:** 1
- **Liver:** 1
- **Kidneys:** 2
- **Tripe:** 1
- **Sweetbread:** 1
- **Eyes:** 2
- **Spleen:** 1
- **Raw materials**
- **Bones:** 21
- **Skull:** 1
- **Teeth:** 2
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*The largest of the giant cats. It can be found hunting alone in the most savage countryside.*

**Giant tigers** are strong carnivorous animals, roaming savage tropical areas. Adult giant tigers are more than three times the size of a standard cow. Giant tigers may also appear as mounts during a siege.

Captured giant tigers may be tamed and kept as pets, trained for hunting or war, or bred as livestock for a meat industry. While they do not produce as much meat as some other "giant" creatures, giant tiger butchering returns are worth four times as much as those of common domestic animals.

Giant tigers are well-suited for military service, as they are by far the biggest of all the giant cats and breed relatively rapidly. Even untrained, giant tigers present a formidable defense for a fortress. As non-grazers, giant tigers don't require a pasture, and so need no special attention after taming.

Some dwarves prefer giant tigers for their *large stripes, of course*.

Not what they meant when they said, "Earn your stripes."

    [CREATURE:GIANT_TIGER]
        [COPY_TAGS_FROM:TIGER]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:842]
        [GO_TO_START]
        [NAME:giant tiger:giant tigers:giant tiger]
        [CASTE_NAME:giant tiger:giant tigers:giant tiger]
        [GENERAL_CHILD_NAME:giant tiger cub:giant tiger cubs]
        [DESCRIPTION:The largest of the giant cats.  It can be found hunting alone in the most savage countryside.]
        [POPULATION_NUMBER:2:3]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'T']
        [COLOR:6:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:large stripes, of course]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:471:314:157:1900:2900] 56 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900]
