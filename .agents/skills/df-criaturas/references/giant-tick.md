# Giant tick

> Fonte: [Giant tick](https://dwarffortresswiki.org/index.php/Giant_tick) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant ticks for their ability to expand.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Variations**
- **Tick - Tick man - Giant tick**
- **Attributes**
- **Alignment:** Savage
- **Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Max:** 200,007 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 2-2
- **Butchering returns**
- **Food items**
- **Meat:** 25
- **Fat:** 22
- **Brain:** 2
- **Heart:** 1
- **Intestines:** 8
- **Eyes:** 2
- **Raw materials**
- **Skin:** Chitin

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A large monster taking the shape of a tick.*

**Giant ticks** are the non-vermin variety of ticks. They carry the [`[MOUTH_SUCK_ATTACK]`](/index.php/Creature_token#MOUTH_SUCK_ATTACK "Creature token") creature variation tag, and can in fact suck blood from a dwarf. In form and capability they are essentially a toothless, webless giant spider, and as such are relatively no danger to your dwarves; however, if cornered and attacked, they can make quick work of a single, untrained and unarmored dwarf. Having an additional pair of legs gives them more resilience compared to giant insects, and less chance to get a fatal brain injury, but they are easily taken out by a military squad or hunter. It is highly recommended to either take it down by bolt, or have an armored soldier take care of it, as even a single bite can incapacitate an unarmored dwarf. They are ubiquitous, living for only two years, so they are better utilized as roasts than pets.

    [CREATURE:GIANT_TICK]
        [COPY_TAGS_FROM:TICK]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:20000700]
        [GO_TO_START]
        [NAME:giant tick:giant ticks:giant tick]
        [CASTE_NAME:giant tick:giant ticks:giant tick]
        [DESCRIPTION:A large monster taking the shape of a tick.]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'T']
        [COLOR:6:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:ability to expand]
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:9000:8900:8825:8775:9500:9900]
