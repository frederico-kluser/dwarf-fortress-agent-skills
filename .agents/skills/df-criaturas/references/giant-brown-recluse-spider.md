# Giant brown recluse spider

> Fonte: [Giant brown recluse spider](https://dwarffortresswiki.org/index.php/Giant_brown_recluse_spider) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes giant brown recluse spiders for their venomous bite.**
- **Biome**
- **Temperate Broadleaf Forest**
- **Variations**
- **Brown recluse spider - Brown recluse spider man - Giant brown recluse spider**
- **Attributes**
- **Alignment:** Savage
- **No Stun · No Pain · Exotic mount · Webs · Syndrome**
- **Tamed Attributes**
- **Pet value:** 500
- **Not hunting/war trainable**
- **Size**
- **Max:** 200,007 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 1-2
- **Butchering returns**
- **Food items**
- **Meat:** 51
- **Fat:** 21
- **Brain:** 2
- **Heart:** 1
- **Intestines:** 8
- **Eyes:** 2
- **Raw materials**
- **Skin:** Chitin

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge monster in the shape of a brown recluse spider.*

**Giant brown recluse spiders** are giant animal versions of the common brown recluse spider who inhabit savage temperate broadleaf forests. While their original counterparts are vermin, these creatures are over three times bigger than a dwarf, and as large as a giant cave spider. While they aren't particularly aggressive, giant brown recluses will attack if provoked, which can quickly lead to the death of dwarves due to the spider's venom and immunity to pain and stunning. Their existence in a biome is marked by the presence of their web on the surface. Unlike giant cave spiders, however, giant brown recluses are unable to spew web as a form of combat, making them considerably easier to kill.

Giant brown recluse spiders can be captured in cage traps and trained into pets, possessing the standard giant creature pet value. They are born adults and can't be turned fully tame. While farming silk out of them may come to mind, it's not as good an idea as it sounds; their silk possesses normal item value, they only produce web sporadically and don't shoot it in huge quantities like a giant cave spider does, and they are extremely short-lived creatures, only living from 1 to 2 years max. All of it makes them a very poor choice for silk production, though you can always butcher them instead. Like other giant beasts, they are exotic mounts.

Some dwarves like giant brown recluse spiders for their *venomous bite*.

    [CREATURE:GIANT_BROWN_RECLUSE_SPIDER]
        [COPY_TAGS_FROM:SPIDER_BROWN_RECLUSE]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_NAME]
            [CVCT_TARGET:brown recluse spider]
            [CVCT_REPLACEMENT:giant brown recluse spider]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:STATE_ADJ]
            [CVCT_TARGET:brown recluse spider]
            [CVCT_REPLACEMENT:giant brown recluse spider]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:SYN_NAME]
            [CVCT_TARGET:brown recluse spider]
            [CVCT_REPLACEMENT:giant brown recluse spider]
        [CV_CONVERT_TAG]
            [CVCT_MASTER:SYN_IMMUNE_CREATURE]
            [CVCT_TARGET:SPIDER_BROWN_RECLUSE]
            [CVCT_REPLACEMENT:GIANT_BROWN_RECLUSE_SPIDER]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [APPLY_CREATURE_VARIATION:GIANT]
        [CV_REMOVE_TAG:CHANGE_BODY_SIZE_PERC]
        [APPLY_CURRENT_CREATURE_VARIATION]
        [GO_TO_END]
        [SELECT_CASTE:ALL]
        [CHANGE_BODY_SIZE_PERC:20000700]
        [APPLY_CREATURE_VARIATION:MOUTH_BITE_VENOM_ATTACK]
        [GO_TO_START]
        [NAME:giant brown recluse spider:giant brown recluse spiders:giant brown recluse spider]
        [CASTE_NAME:giant brown recluse spider:giant brown recluse spiders:giant brown recluse spider]
        [DESCRIPTION:A huge monster in the shape of a brown recluse spider.]
        [POPULATION_NUMBER:10:20]
        [CLUSTER_NUMBER:1:1]
        [CREATURE_TILE:'S']
        [COLOR:6:0:0]
        [PET_EXOTIC]
        [PETVALUE:500]
        [MOUNT_EXOTIC]
        [GO_TO_END]
        [PREFSTRING:venomous bite]
        [APPLY_CREATURE_VARIATION:STANDARD_WALKING_GAITS:900:750:600:439:1900:2900] 20 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900]
