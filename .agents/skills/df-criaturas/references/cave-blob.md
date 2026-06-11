# Cave blob

> Fonte: [Cave blob](https://dwarffortresswiki.org/index.php/Cave_blob) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes cave blobs for their bright orange color.**
- **Biome**
- **Underground Depth: 3**
- **Attributes**
- **Genderless · No Stun · Syndrome**
- **Tamed Attributes**
- **Pet value:** 50
- **Not hunting/war trainable**
- **Size**
- **Max:** 20,000 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** Immortal
- **Butchering returns**
- **Food items**
- **Raw materials**
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A strange shapeless life form with an orange leathery skin containing a liquid interior. It can secrete its internal fluid.*

**Cave blobs** are small rare creatures who inhabit the third layer of the caverns. They lack bones or any kind of internal organs, and instead are filled with orange fluid which causes mild, short-term harm in the form of painful blisters on other creatures when ingested or made contact with. Undead cave blobs will appear pink. The blob's skin is covered in this fluid as well; touching it is enough to potentially contract its syndrome. This fluid leaks if the creature’s skin is pierced, spilling out over the surrounding tiles. They are genderless, emotionless, have no need to breathe and are immune to stunning or nausea, but due to their small size and fragile composition, an unarmed dwarf should be able to dispatch one without breaking a sweat. Cave blobs have no attacks other than a default push, which will glance away from just about anything.

Cave blobs may be captured in cage traps and trained into low-value pets. The only products gained by the butchering of a cave blob are a skin for your leatherworkers and a few pools of cave blob fluid, which can be drunk in adventurer mode to satiate thirst. Cave blobs are biologically immortal and only die from violence, so in case one of your dwarves is weird enough to adopt them, they'll potentially last forever.

Unlike most creatures, they can't be spawned in the object testing arena.

Some dwarves like cave blobs for their *bright orange color*.

## Adventure Mode Training

A way to improve adventurers who can start with cave blobs as tamed pets to become (mostly) safely and more easily highly potent in conventional combat has been found http://www.bay12forums.com/smf/index.php?topic=164906.msg8296757#msg8296757 (look for reply No.8).

As orange, cavey and blobby as possible.\
*Art by Zippy*

    [CREATURE:CAVE_BLOB]
        [ARENA_RESTRICTED]
        [DESCRIPTION:A strange shapeless life form with an orange leathery skin containing a liquid interior.  It can secrete its internal fluid.]
        [NAME:cave blob:cave blobs:cave blob]
        [CASTE_NAME:cave blob:cave blobs:cave blob]
        [CREATURE_TILE:'o'][COLOR:6:0:1]
        [CREATURE_CLASS:POISONOUS]
        [PETVALUE:50]
        [PET_EXOTIC]
        [FREQUENCY:10]
        [BIOME:SUBTERRANEAN_CHASM]
        [BIOME:SUBTERRANEAN_WATER]
        [LARGE_ROAMING]
        [UNDERGROUND_DEPTH:3:3]
        [EXTRAVISION][NOBREATHE][NOSTUN][NONAUSEA][NOEMOTION]
        [NOBONES]
        [NATURAL]
        [POPULATION_NUMBER:250:500]
        [CLUSTER_NUMBER:2:5]
        [PREFSTRING:bright orange color]
        [BODY:BASIC_1PARTBODY_THOUGHT]
        [USE_MATERIAL_TEMPLATE:SKIN:SKIN_TEMPLATE]
        [USE_MATERIAL_TEMPLATE:LEATHER:LEATHER_TEMPLATE]
        [USE_MATERIAL_TEMPLATE:PARCHMENT:PARCHMENT_TEMPLATE]
        [USE_MATERIAL_TEMPLATE:FLUID:CREATURE_EXTRACT_TEMPLATE]
            [STATE_NAME:ALL_SOLID:frozen cave blob fluid]
            [STATE_NAME_ADJ:ALL_SOLID:frozen cave blob fluid]
            [STATE_NAME:LIQUID:cave blob fluid]
            [STATE_NAME_ADJ:LIQUID:cave blob fluid]
            [STATE_NAME:GAS:boiling cave blob fluid]
            [STATE_NAME_ADJ:GAS:boiling cave blob fluid]
            [STATE_COLOR:ALL:ORANGE]
            [PREFIX:NONE]
            [SYNDROME]
                [SYN_NAME:blob blisters]
                [SYN_AFFECTED_CLASS:GENERAL_POISON]
                [SYN_IMMUNE_CREATURE:CAVE_BLOB:ALL]
                [SYN_CONTACT][SYN_INGESTED]
                [CE_PAIN:SEV:15:PROB:100:LOCALIZED:VASCULAR_ONLY:RESISTABLE:START:50:PEAK:1000:END:2000]
                [CE_BLISTERS:SEV:25:PROB:100:LOCALIZED:VASCULAR_ONLY:RESISTABLE:START:50:PEAK:1000:END:2000]
        [TISSUE:SKIN]
            [TISSUE_NAME:skin:NP]
            [TISSUE_MATERIAL:LOCAL_CREATURE_MAT:SKIN]
            [TISSUE_MAT_STATE:SOLID]
            [STRUCTURAL]
            [RELATIVE_THICKNESS:1]
            [CONNECTS]
            [TISSUE_SHAPE:LAYER]
        [TISSUE:FLUID]
            [TISSUE_NAME:fluid:NP]
            [TISSUE_MATERIAL:LOCAL_CREATURE_MAT:FLUID]
            [TISSUE_MAT_STATE:LIQUID]
            [MUSCULAR]
            [FUNCTIONAL]
            [STRUCTURAL]
            [RELATIVE_THICKNESS:100]
            [CONNECTS]
            [TISSUE_LEAKS]
            [TISSUE_SHAPE:LAYER]
        [TISSUE_LAYER:BY_CATEGORY:ALL:SKIN]
        [TISSUE_LAYER_UNDER:BY_CATEGORY:ALL:FLUID]
        [SECRETION:LOCAL_CREATURE_MAT:FLUID:LIQUID:BY_CATEGORY:ALL:SKIN]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [BODY_SIZE:0:0:20000]
        [ALL_ACTIVE]
        [NO_SLEEP]
        [NO_DIZZINESS]
        [NO_FEVERS]
        [CANNOT_JUMP]
        [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
            [TL_COLOR_MODIFIER:ORANGE:1]
                [TLCM_NOUN:skin:SINGULAR]
