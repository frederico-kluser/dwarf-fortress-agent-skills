# Giant jumping spider

> Fonte: [Giant jumping spider](https://dwarffortresswiki.org/index.php/Giant_jumping_spider) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant jumping spiders for their striking appearance.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Variations**
- **Jumping spider - Jumping spider man - Giant jumping spider**
- **Attributes**
- **Alignment:** Savage
- **No Stun · No Pain · Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Max:** 200,007 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 2-3
- **Butchering returns**
- **Food items**
- **Meat:** 23-65
- **Fat:** 21-34
- **Brain:** 2
- **Heart:** 1
- **Intestines:** 8
- **Eyes:** 2
- **Raw materials**
- **Skin:** Chitin

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster in the form of a jumping spider.*

**Giant jumping spiders** do not share the web-spitting ability or poisonous fangs of other spider species. They may be considered the least dangerous kind of giant spider, but they are still more than a match for an untrained, weaponless dwarf. Like other spiders, they are immune to stunning and pain, so your dwarves should focus on killing blows, not disabling attacks.

Like all the other new giant bugs introduced in 0.34.01, giant jumping spiders are *not* large predators and will generally leave your dwarves alone. They only live a maximum of 3 years, making them a poor choice for training and display.

Dwarves may admire them for their *ability to leap* (or their *striking appearance*).

Breeding attempts have been successful, observed to breed rapidly, although despite being spiders they breed much like mammals do, with the females becoming pregnant and then giving birth to generally one or two young. Given the lack of any maintenance requirement such as pastures or nest boxes, they make good meat animals and have the added bonus of being able to effectively defend themselves from attackers. As such, they can be pastured with more defenseless creatures that require pastures for protection.

    [CREATURE:GIANT_JUMPING_SPIDER]
        [COPY_TAGS_FROM:SPIDER_JUMPING]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:20000700]
        [APPLY_CREATURE_VARIATION:MOUTH_BITE_EDGE_ATTACK]
        [GO_TO_START]
        [NAME:giant jumping spider:giant jumping spiders:giant jumping spider]
        [CASTE_NAME:giant jumping spider:giant jumping spiders:giant jumping spider]
        [DESCRIPTION:A huge monster in the form of a jumping spider.]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'J']
        [COLOR:0:0:1]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:striking appearance]
        [PREFSTRING:ability to leap]
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900]
