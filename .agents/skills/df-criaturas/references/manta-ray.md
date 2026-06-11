# Manta ray

> Fonte: [Manta ray](https://dwarffortresswiki.org/index.php/Manta_ray) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes manta rays for their majesty.**
- **Biome**
- **Tropical Ocean**
- **Attributes**
- **Aquatic**
- **Cannot be tamed**
- **Size**
- **Birth:** 100,000 cm 3
- **Mid:** 500,000 cm 3
- **Max:** 2,300,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 20-30
- **Butchering returns**
- **Food items**
- **Meat:** 37-153
- **Fat:** 7-29
- **Brain:** 5-7
- **Heart:** 2-3
- **Intestines:** 17-24
- **Liver:** 5-7
- **Kidneys:** 4-6
- **Tripe:** 5-7
- **Sweetbread:** 2-3
- **Eyes:** 2
- **Spleen:** 2-3
- **Raw materials**
- **Skull:** 1
- **Teeth:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A huge filter-feeding fish with great wings. They travel the oceans and are curious and friendly.*

**Manta rays** are massive cartilaginous fish that can be found in tropical oceans. At over two tons, adult manta rays are huge creatures, and as such will provide a great amount of returns if butchered. As fully-sized creatures, they can't be fished by fisherdwarves, but can be caught with a drowning chamber. An infant manta ray is called a *manta ray pup*.

Being cartilaginous, manta rays won't give bones if butchered (though they'll still provide a skull).

Some dwarves like manta rays for their *majesty*.

Admired for its *majesty*.

    [CREATURE:FISH_RAY_MANTA]
        [DESCRIPTION:A huge filter-feeding fish with great wings.  They travel the oceans and are curious and friendly.]
        [NAME:manta ray:manta rays:manta ray]
        [CASTE_NAME:manta ray:manta rays:manta ray]
        [CHILD:1][GENERAL_CHILD_NAME:manta ray pup:manta ray pups]
        [CREATURE_TILE:16][COLOR:7:0:0]
        [LARGE_ROAMING]
        [AQUATIC][UNDERSWIM][IMMOBILE_LAND]
        [BENIGN][MEANDERER][NATURAL]
        [PETVALUE:500]
        [BIOME:OCEAN_TROPICAL]
        [POPULATION_NUMBER:15:30]
        [PREFSTRING:majesty]
        [BODY:BASIC_2PARTBODY:BASIC_HEAD:SIDE_FINS:TAIL:2EYES:HEART:GUTS:ORGANS:SPINE:BRAIN:SKULL:MOUTH:RIBCAGE:GENERIC_TEETH]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
            [REMOVE_MATERIAL:HAIR]
            [REMOVE_MATERIAL:BONE]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
            [REMOVE_TISSUE:HAIR]
            [REMOVE_TISSUE:BONE]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:CARTILAGE:CARTILAGE]
        [SELECT_TISSUE_LAYER:HEART:BY_CATEGORY:HEART]
         [PLUS_TISSUE_LAYER:SKIN:BY_CATEGORY:THROAT]
            [TL_MAJOR_ARTERIES]
        [BODY_DETAIL_PLAN:STANDARD_HEAD_POSITIONS]
        [BODY_DETAIL_PLAN:HUMANOID_RIBCAGE_POSITIONS]
        [USE_MATERIAL_TEMPLATE:SINEW:SINEW_TEMPLATE]
        [TENDONS:LOCAL_CREATURE_MAT:SINEW:200]
        [LIGAMENTS:LOCAL_CREATURE_MAT:SINEW:200]
        [HAS_NERVES]
        [USE_MATERIAL_TEMPLATE:BLOOD:BLOOD_TEMPLATE]
        [BLOOD:LOCAL_CREATURE_MAT:BLOOD:LIQUID]
        [CREATURE_CLASS:GENERAL_POISON]
        [GETS_WOUND_INFECTIONS]
        [GETS_INFECTIONS_FROM_ROT]
        [USE_MATERIAL_TEMPLATE:PUS:PUS_TEMPLATE]
        [PUS:LOCAL_CREATURE_MAT:PUS:LIQUID]
        [BODY_SIZE:0:0:100000]
        [BODY_SIZE:1:0:500000]
        [BODY_SIZE:5:0:2300000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:20:30]
        [ALL_ACTIVE]
        [NO_DRINK]
        [HOMEOTHERM:10067]
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:900:691:482:251:1900:2900] 35 kph, NO DATA
        [SWIMS_INNATE]
        [CANNOT_JUMP]
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
                [TL_COLOR_MODIFIER:GRAY:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:eyes:PLURAL]
