# Giant capybara

> Fonte: [Giant capybara](https://dwarffortresswiki.org/index.php/Giant_capybara) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant capybaras for their resonant barking.**
- **Biome**
- **Any Wetland**
- **Variations**
- **Capybara - Capybara man - Giant capybara**
- **Attributes**
- **Alignment:** Savage
- **Amphibious · Grazer · Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Birth:** 52,335 cm 3
- **Mid:** 261,675 cm 3
- **Max:** 523,350 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 10-12
- **Butchering returns ( Value multiplier ×2)**
- **Food items**
- **Meat:** 19-31
- **Fat:** 15-25
- **Brain:** 1
- **Intestines:** 1-2
- **Liver:** 1
- **Kidneys:** 2
- **Tripe:** 1
- **Sweetbread:** 1
- **Eyes:** 2
- **Spleen:** 1
- **Raw materials**
- **Bones:** 21-31
- **Skull:** 1
- **Teeth:** 4
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge rodent that walks on tall legs. Its bark can be heard at large distances. It is fond of swimming.*

**Giant capybaras** are giant animal versions of common capybaras who can be found in savage wetlands. They are roughly ten times larger than a standard capybara, about the size of a full-grown moose, or almost nine times heavier than a dwarf. Giant capybaras attack when attacked and can be very dangerous: they have been known to drag their quarry into the water and drown them.

Giant capybaras are especially dangerous around unarmed dwarves – they can kill a dwarf with a single blow to the head, rip off limbs until they bleed to death, or even damage multiple internal organs until the dwarf dies. Even worse, they have an ability to resist attacks (similar to the bronze colossus) – their heads are extremely durable (more than those of dwarves), and they can usually manage to break a dwarf's grip on their throat, even when barely conscious. In the arena, giant capybaras are capable of resisting over 50 dwarves in groups of 1-3 without any additional assistance (as in defeating dwarves single-handedly, without being controlled). They do suffer minor injuries (bruises, minor scars) and occasionally lose consciousness, but are extremely good at survival. They may also appear as mounts during a siege, easily crossing water-filled moats and potentially sneaking into your fortress via wells or irrigation systems.

As with most dangerous wild animals, players attempting to train these creatures in a fortress should use an experienced animal trainer. While dragons are arguably more dangerous, giant capybaras rampaging through a fortress are generally not desirable (along with most other giant creatures). Unlike most other amphibious creatures, giant capybaras are grazers; when tamed, they require a pasture for food.

Some dwarves appreciate giant capybaras for their *graceful swimming*, *resonant barking*, and *beyond enormous rodentness*.

## Trivia

- The name of these creatures in the raws is `CAPYBARA, GIANT` - most other similar creatures would use `GIANT_CAPYBARA`.

    [CREATURE:CAPYBARA, GIANT]
        [COPY_TAGS_FROM:CAPYBARA]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:1163]
        [GO_TO_START]
        [NAME:giant capybara:giant capybaras:giant capybara]
        [CASTE_NAME:giant capybara:giant capybaras:giant capybara]
        [GENERAL_CHILD_NAME:giant capybara pup:giant capybara pups]
        [DESCRIPTION:A huge rodent that walks on tall legs.  Its bark can be heard at large distances.  It is fond of swimming.]
        [POPULATION_NUMBER:20:30]
        [CLUSTER_NUMBER:5:10]
        [CREATURE_TILE:'C']
        [COLOR:6:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [SOUND:ALERT:200:1000:VOCALIZATION:bark:barks:a resounding bark]
        [SOUND:PEACEFUL_INTERMITTENT:200:10000:VOCALIZATION:whistle:whistles:deep whistling]
        [SOUND:PEACEFUL_INTERMITTENT:50:10000:VOCALIZATION:grunt:grunts:a loud grunt]
        [SOUND:PEACEFUL_INTERMITTENT:5:10000:VOCALIZATION:purr:purrs:a deep purr]
        [SOUND:PEACEFUL_INTERMITTENT:50:10000:NONE:click:clicks:a loud click]
        [PREFSTRING:beyond enormous rodentness]
        [PREFSTRING:graceful swimming]
        [PREFSTRING:resonant barking]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:734:568:366:1900:2900] 24 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:6561:6115:5683:1755:7456:8567]
