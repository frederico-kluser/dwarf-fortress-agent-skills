# Giant mandrill

> Fonte: [Giant mandrill](https://dwarffortresswiki.org/index.php/Giant_mandrill) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant mandrills for their colorful faces.**
- **Biome**
- **Tropical Moist Broadleaf Forest**
- **Variations**
- **Mandrill - Mandrill man - Giant mandrill**
- **Attributes**
- **Alignment:** Savage
- **Steals food · Steals items · War animals · Hunting animals · Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Trainable : Hunting War**
- **Size**
- **Birth:** 34,180 cm 3
- **Mid:** 170,900 cm 3
- **Max:** 341,800 cm 3
- **Age**
- **Adult at:** 3
- **Max age:** 15-25
- **Butchering returns**
- **Food items**
- **Meat:** 17-21
- **Fat:** 15-19
- **Brain:** 1
- **Heart:** 1
- **Lungs:** 2
- **Intestines:** 1
- **Liver:** 1
- **Kidneys:** 2
- **Tripe:** 1
- **Sweetbread:** 1
- **Eyes:** 0-2
- **Spleen:** 1
- **Raw materials**
- **Bones:** 18-22
- **Skull:** 1
- **Teeth:** 2
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large monster in the form of a mandrill.*

More than 50% larger than a grizzly bear and lacking the [\[MEANDERER\]](/index.php/Creature_token#MEANDERER "Creature token") token, the giant mandrill also shares its smaller cousin's ability to be trained for war and hunting. They are the largest MUNDANE creature with the STEALS_ITEMS creature token.

    [CREATURE:GIANT_MANDRILL]
        [COPY_TAGS_FROM:MANDRILL]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:1709]
        [GO_TO_START]
        [NAME:giant mandrill:giant mandrills:giant mandrill]
        [CASTE_NAME:giant mandrill:giant mandrills:giant mandrill]
        [DESCRIPTION:A large monster in the form of a mandrill.]
        [POPULATION_NUMBER:20:50]
        [CLUSTER_NUMBER:5:10]
        [CREATURE_TILE:'M']
        [COLOR:1:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:colorful faces]
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:900:657:438:219:1900:2900] 40 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900]
