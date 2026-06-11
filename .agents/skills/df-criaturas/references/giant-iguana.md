# Giant iguana

> Fonte: [Giant iguana](https://dwarffortresswiki.org/index.php/Giant_iguana) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant iguanas for their head bobs.**
- **Biome**
- **Any Tropical Forest**
- **Variations**
- **Iguana - Iguana man - Giant iguana**
- **Attributes**
- **Alignment:** Savage
- **Exotic mount · Egglaying**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 855.15 cm 3
- **Mid:** 28,505 cm 3
- **Max:** 228,040 cm 3
- **Food products**
- **Eggs:** 40-50
- **Age**
- **Adult at:** 1
- **Max age:** 10-20
- **Butchering returns ( Value multiplier ×2)**
- **Food items**
- **Meat:** 15
- **Fat:** 13
- **Brain:** 1
- **Heart:** 1
- **Lungs:** 2
- **Intestines:** 1
- **Liver:** 1
- **Kidneys:** 2
- **Tripe:** 1
- **Sweetbread:** 1
- **Spleen:** 1
- **Raw materials**
- **Bones:** 18
- **Skull:** 1
- **Skin:** Scales

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster in the shape of an iguana.*

**Giant iguanas** are the much-larger cousins of the iguanas who live in all savage tropical forests. Like their regular counterparts, they are relatively uncommon and only spawn one at a time, but stand 57 times larger than a normal iguana, which makes them far more formidable in combat. However, despite their enlarged bodies, giant iguanas are not predatory and are inclined to leave your dwarves alone unless you actively attack them, and even then they should stand no chance against a well-equipped military squad. Unlike their normal cousins, giant iguanas are considered exotic mounts, so you might see elves riding them in the event of a siege.

As normal iguanas already possess a pet value of 400, the gain from domesticating giant iguanas over normal ones is fairly small and may come down to availability and/or player preference. However, giant iguanas do retain the trait of laying 40 to 50 eggs at a time, making them excellent targets for egg production, either to feed the fortress or to fulfill the player's fantasies of unleashing an army of 50+ giant spiked reptiles at the unaware goblin intruders.

Some dwarves like giant iguanas for their *dewlaps* and their *head bobs*.

\

    [CREATURE:GIANT_IGUANA]
        [COPY_TAGS_FROM:IGUANA]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:5701]
        [GO_TO_START]
        [NAME:giant iguana:giant iguanas:giant iguana]
        [CASTE_NAME:giant iguana:giant iguanas:giant iguana]
        [GENERAL_CHILD_NAME:giant iguana hatchling:giant iguana hatchlings]
        [DESCRIPTION:A huge monster in the shape of an iguana.]
        [POPULATION_NUMBER:5:10]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'I']
        [COLOR:2:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:head bobs]
        [PREFSTRING:dewlaps]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:900:657:438:219:1900:2900] 40 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900]
