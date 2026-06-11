# Giant hyena

> Fonte: [Giant hyena](https://dwarffortresswiki.org/index.php/Giant_hyena) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant hyenas for their coordinated hunting.**
- **Biome**
- **Tropical Savanna Tropical Grassland Tropical Shrubland**
- **Variations**
- **Hyena - Hyena man - Giant hyena**
- **Attributes**
- **Alignment:** Savage
- **Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 63,360 cm 3
- **Mid:** 316,800 cm 3
- **Max:** 633,600 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 10-25
- **Butchering returns ( Value multiplier ×2)**
- **Food items**
- **Meat:** 33
- **Fat:** 28
- **Brain:** 1
- **Heart:** 1
- **Lungs:** 2
- **Intestines:** 2
- **Liver:** 1
- **Kidneys:** 2
- **Tripe:** 1
- **Sweetbread:** 1
- **Eyes:** 2
- **Spleen:** 1
- **Raw materials**
- **Bones:** 34
- **Skull:** 1
- **Teeth:** 2
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster the shape of a hyena.*

**Giant hyenas** are extremely large, six times the size of an average dwarf, close to as large as a yak. Thanks to the `[LARGE_PREDATOR]` token they inherit from their basal kin, they're also extremely aggressive. Combined with their pack behavior, appearing in groups of 5-15 individuals, giant hyenas are (unsurprisingly) *extremely* dangerous, and will rip apart an unfortunate dwarf faster than he can scream. Should not be approached without large and experienced military hunting parties in full armor; the proceeds of such a clash could feed the fortress for a while.

Some dwarves like giant hyenas for their *distinctive laugh* and their *coordinated hunting*.

A Lovecraftian view of giant hyenas. Their laughs are even more horrifying.

    [CREATURE:GIANT_HYENA]
        [COPY_TAGS_FROM:HYENA]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:1056]
        [GO_TO_START]
        [NAME:giant hyena:giant hyenas:giant hyena]
        [CASTE_NAME:giant hyena:giant hyenas:giant hyena]
        [GENERAL_CHILD_NAME:giant hyena cub:giant hyena cubs]
        [DESCRIPTION:A huge monster the shape of a hyena.]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:5:15]
        [CREATURE_TILE:'H']
        [COLOR:6:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:distinctive laugh]
        [PREFSTRING:coordinated hunting]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:549:366:183:1900:2900] 48 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900]
