# Fire imp

> Fonte: [Fire imp](https://dwarffortresswiki.org/index.php/Fire_imp) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes fire imps for their terrifying features.**
- **Biome**
- **Underground Depth: 0-4**
- **Attributes**
- **Genderless · Fire immune · Humanoid**
- **Cannot be tamed**
- **Size**
- **Max:** 6,000 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** Immortal
- **Butchering returns ( Value multiplier ×3)**
- **Food items**
- **Meat:** 7
- **Fat:** 7
- **Intestines:** 1
- **Raw materials**
- **Bones:** 4
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A small humanoid surrounded by fire which they can hurl at their enemies.*

**Fire imps** are small, hostile creatures straight from the magma sea, emerging in groups of 3-4 mayhem-minded individuals. Only a little bigger than a cat, the threat they pose comes in the form of their special attacks; they are able to throw large fireballs and launch jets of flame from their hands, which can ignite whole landscapes and immediately turn your dwarves into ‼dwarves‼. All fire imps are born with Legendary skill in climbing.

If breaching the magma sea to use its magma, one should expect to face fire imps sooner or later. Take measures when you spot some in a nearby magma pipe, and equip your military with shields in hopes they won't be ignited when facing them. Attempting to drown fire imps is futile, as like all other magma-dwellers, they don't need to breathe. They are also able to open unforbidden doors, meaning these can't be used to block them. To avoid unwanted fun when dealing with fire imps and other nasty magma-dwelling creatures, you can have a narrow channel leading between your source and the point you want to send it to, then put in a magma-safe grate or set of bars (fortifications are useless when submerged, as creatures can swim through them). Beware, though, that magma men and fire men can and will destroy such barriers.

A safer, but more complicated way to do this is having a floor grate cover the magma intake point and getting magma from it through a pump. Due to building-destroying mechanics, floor grates can't be destroyed from below. Pumps can take magma from a grated source. The pump and grate should obviously be magma-safe. Also, the pump should be powered, not manually operated - a dwarf operating the pump would be in line of fire should an imp find itself under the grate.

Fire imps are glass cannons (a dog can take care of them, provided they're not ignited), but resist heat much more than most creatures, only taking damage at 15000 °U . This makes them immune to fire and magma (obviously), but not dragonfire. It is possible for fire imps and other magma-resident creatures to travel to the surface via a volcano; if you are building near a volcano, and your dwarves get set on fire for no apparent reason, look around for a fire imp in the volcano. You can try channeling to the surface of the magma and baiting it or just dump water on it from above. They are one of the few renewable sources of fire-proof leather, aside from spoilers.

Fireball sprite.

In an amusing example of the intricacies of *Dwarf Fortress*, fire imps cannot get fevers. It makes sense when you know what a fever is (higher body temperature, by a few degrees), and the fact that fire imps are extremely resistant to high temperatures. This is not likely to affect gameplay unless you expose them to an appropriate evil weather or if modding is involved. Despite their humanoid anatomy, fire imps are not intelligent creatures and therefore your dwarves will be more than eager to butcher them for a small quantity of returns; their fire resistance is inherited by their returns, and the tanned hide of a fire imp can be used to create fireproof leather items. Curiously, fire imps are all genderless and biologically immortal, and rather than blood, they have gray-colored goo as their bodily fluids. Adventurers are able to smell fire imps with o, with them being described as smelling like "smoke".

Some dwarves like fire imps for their *terrifying features*.

Admired for its *terrifying features*.\
*Art by Fault*

## Trivia

-

  Initially, the premium version had a sprite for a child fire imp. It was later removed from the game, because fire imps are adults at birth.

    [CREATURE:IMP_FIRE]
        [DESCRIPTION:A small humanoid surrounded by fire which they can hurl at their enemies.]
        [NAME:fire imp:fire imps:fire imp]
        [CASTE_NAME:fire imp:fire imps:fire imp]
        [CREATURE_TILE:'i'][COLOR:6:0:1]
        [LARGE_ROAMING][FREQUENCY:20]
        [BIOME:SUBTERRANEAN_LAVA]
        [UNDERGROUND_DEPTH:0:4]
        [POPULATION_NUMBER:15:30]
        [CLUSTER_NUMBER:3:4]
        [LARGE_PREDATOR]
        [CAN_DO_INTERACTION:MATERIAL_EMISSION]
            [CDI:TOKEN:HURL_FIREBALL]
            [CDI:ADV_NAME:Hurl fireball]
            [CDI:USAGE_HINT:ATTACK]
            [CDI:BP_REQUIRED:BY_CATEGORY:HAND]
            [CDI:FLOW:FIREBALL]
            [CDI:TARGET:C:LINE_OF_SIGHT]
            [CDI:TARGET_RANGE:C:15]
            [CDI:MAX_TARGET_NUMBER:C:1]
            [CDI:WAIT_PERIOD:30]
        [CAN_DO_INTERACTION:MATERIAL_EMISSION]
            [CDI:TOKEN:SPRAY_FIRE_JET]
            [CDI:ADV_NAME:Spray jet of fire]
            [CDI:USAGE_HINT:ATTACK]
            [CDI:BP_REQUIRED:BY_CATEGORY:HAND]
            [CDI:FLOW:FIREJET]
            [CDI:TARGET:C:LINE_OF_SIGHT]
            [CDI:TARGET_RANGE:C:5]
            [CDI:MAX_TARGET_NUMBER:C:1]
            [CDI:WAIT_PERIOD:30]
        [FIREIMMUNE][MAGMA_VISION]
        [NOBREATHE]
        [CANOPENDOORS]
        [BONECARN]
        [PREFSTRING:terrifying features]
        [ODOR_STRING:smoke]
        [ODOR_LEVEL:90]
        [BODY:HUMANOID_NECK:TAIL:2EYES:2EARS:NOSE:HEART:GUTS:ORGANS:HUMANOID_JOINTS:THROAT:NECK:SPINE:BRAIN:SKULL:MOUTH:TONGUE:4FINGERS:4TOES:FACIAL_FEATURES:GENERIC_TEETH_WITH_LARGE_EYE_TEETH:RIBCAGE]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:BONE:CARTILAGE]
        [USE_MATERIAL_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:FINGER:NAIL:FRONT]
        [TISSUE_LAYER:BY_CATEGORY:TOE:NAIL:FRONT]
        [SELECT_TISSUE_LAYER:HEART:BY_CATEGORY:HEART]
         [PLUS_TISSUE_LAYER:SKIN:BY_CATEGORY:THROAT]
            [TL_MAJOR_ARTERIES]
        [BODY_DETAIL_PLAN:STANDARD_HEAD_POSITIONS]
        [BODY_DETAIL_PLAN:HUMANOID_HEAD_POSITIONS]
        [BODY_DETAIL_PLAN:HUMANOID_RIBCAGE_POSITIONS]
        [BODY_DETAIL_PLAN:HUMANOID_RELSIZES]
        [USE_MATERIAL_TEMPLATE:SINEW:SINEW_TEMPLATE]
        [TENDONS:LOCAL_CREATURE_MAT:SINEW:200]
        [LIGAMENTS:LOCAL_CREATURE_MAT:SINEW:200]
        [HAS_NERVES]
        [NO_DRINK][NO_EAT][NO_SLEEP]
        [USE_MATERIAL_TEMPLATE:GOO:GOO_TEMPLATE]
        [BLOOD:LOCAL_CREATURE_MAT:GOO:LIQUID]
        [BODY_SIZE:0:0:6000]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [ATTACK:BITE:CHILD_BODYPART_GROUP:BY_CATEGORY:HEAD:BY_CATEGORY:TOOTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
        [ATTACK:PUNCH:BODYPART:BY_TYPE:GRASP]
            [ATTACK_SKILL:GRASP_STRIKE]
            [ATTACK_VERB:punch:punches]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_FLAG_WITH]
            [ATTACK_PRIORITY:MAIN]
        [ATTACK:KICK:BODYPART:BY_TYPE:STANCE]
            [ATTACK_SKILL:STANCE_STRIKE]
            [ATTACK_VERB:kick:kicks]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PREPARE_AND_RECOVER:4:4]
            [ATTACK_FLAG_WITH]
            [ATTACK_PRIORITY:SECOND]
            [ATTACK_FLAG_BAD_MULTIATTACK]
        [ATTACK:SCRATCH:CHILD_TISSUE_LAYER_GROUP:BY_TYPE:GRASP:BY_CATEGORY:FINGER:NAIL]
            [ATTACK_SKILL:GRASP_STRIKE]
            [ATTACK_VERB:scratch:scratches]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:SECOND]
        [EQUIPS]
        [ALL_ACTIVE]
        [NO_FEVERS]
        [HOMEOTHERM:10095]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:730:561:351:1900:2900] 25 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [NATURAL_SKILL:CLIMBING:15]
        [SWIMS_INNATE]
        [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
            [TL_COLOR_MODIFIER:RED:1]
                [TLCM_NOUN:skin:SINGULAR]
        [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
            [TL_COLOR_MODIFIER:BLACK:1]
                [TLCM_NOUN:eyes:PLURAL]
        [SELECT_MATERIAL:ALL]
            [MULTIPLY_VALUE:3]
            [COLDDAM_POINT:NONE]
            [HEATDAM_POINT:NONE]
            [IGNITE_POINT:NONE]
            [IF_EXISTS_SET_MELTING_POINT:15000]
            [IF_EXISTS_SET_BOILING_POINT:20000]
        Need to make sure goo isn't solid at regular temperatures.
        [SELECT_MATERIAL:GOO]
            [MELTING_POINT:10000]
