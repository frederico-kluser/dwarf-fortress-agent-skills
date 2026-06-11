# Giant slug

> Fonte: [Giant slug](https://dwarffortresswiki.org/index.php/Giant_slug) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant slugs for their slime trails.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Variations**
- **Slug - Slug man - Giant slug**
- **Attributes**
- **Alignment:** Savage
- **Genderless · Exotic mount**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Max:** 200,007 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 1-1
- **Butchering returns**
- **Food items**
- **Meat:** 55-74
- **Fat:** 20-27
- **Brain:** 6
- **Heart:** 3
- **Intestines:** 20
- **Raw materials**
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster in the form of a slug.*

**Giant slugs** are just that: really large slugs. They are quite nonthreatening, although you may want to armor your dwarves first to attack them safely. Their large size can make their push attacks somewhat dangerous. They may appear as mounts during a siege, though it's difficult to take an invader seriously when mounted upon a giant slug.

Giant slugs are largely harmless in combat. The head of a giant slug appears to not have any bone inside it, consisting of only fat, muscle, and a brain, along with its eyestalks. Therefore, a hit to the head is usually always lethal. Conversely, it can take a long time (and a lot of bolts) for a marksdwarf to take down a slug, as most of the bolts will hit the body of the slug, and do next to no damage (the body is almost exclusively muscle and fat). Giant slugs can also drown, and expire from old age after a single year.

Hunting giant slugs can provide a decent food source, but they are generally not worthwhile to tame – they do not breed and live for only a short time. Overall, they are pretty uninteresting creatures, unless you happen to have a fascination for giant slugs' *slime trails*.

Not as threatening as it looks here.

    [CREATURE:GIANT_SLUG]
        [COPY_TAGS_FROM:SLUG]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:20000700]
        [GO_TO_START]
        [NAME:giant slug:giant slugs:giant slug]
        [CASTE_NAME:giant slug:giant slugs:giant slug]
        [DESCRIPTION:A huge monster in the form of a slug.]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'S']
        [COLOR:6:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:slime trails]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900]
