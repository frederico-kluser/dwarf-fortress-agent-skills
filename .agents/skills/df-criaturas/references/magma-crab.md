# Magma crab

> Fonte: [Magma crab](https://dwarffortresswiki.org/index.php/Magma_crab) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes magma crabs for their chittering.**
- **Biome**
- **Underground Depth: 3-5**
- **Attributes**
- **Fire immune**
- **Cannot be tamed**
- **Size**
- **Birth:** 1,000 cm 3
- **Mid:** 2,000 cm 3
- **Max:** 30,000 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 50-70
- **Cannot be butchered ( Value multiplier ×2)**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A small rock-eating creature that lives in molten rock. It scurries on little feet and swims through liquid rock with sharp wings. It uses magma to digest rock and spits out burning globs.*

A **magma crab** is a small magma-dwelling creature that has the unique ability to spit globs of liquid basalt in small quantities. It does so at a very fast rate when at range, but if confronted in close quarters, they can only defend themselves with a weak push attack. The basalt spit is a very small and incredibly hot glob of the stuff and as such only burns areas it hits, generally melting off the fat of that body part. It should be noted however that this can be exceptionally deadly, especially to smaller dwarves if they're struck multiple times, as they rapidly bleed until all the fat on the hit parts is melted away. Alternatively, the magma crab's spit may hit some cave moss and set it alight, causing a cavern-wide fire which is certainly deadly to dwarves.

Due to having few organs, magma crabs are quite resilient, but due to their small size they can be killed relatively easily by just about any conventional means, from cave-in traps and marksdwarves to having a mace- or hammerdwarf bash it enough times to crush its body. Using militia dwarves can potentially result in fatalities as dwarves are easily hit by the basalt spit, though soldiers with enough skill in shield use may come out unscathed. Overall, if you leave an open path from their home, magma crabs can be quite disrupting and dangerous, but any potential threat can be neutralized if you wall off any magma access before or after they appear, sealing them in and your dwarves out. Magma crabs cannot be butchered, so the only use of their corpses is filling your refuse stockpile. Magma crabs crawling out of a volcano onto a glacier will cause ice to melt.

Despite what their name and sprite indicate, magma crabs are not actually crab-like in terms of body structure; according to their raws, they are essentially crawling heads with a pair of flightless wings, being devoid of extremities like legs or pincers, making them closer to hungry heads than crabs.

Magma crabs possess a pet value of 200, but are not trainable. Additionally, they can't be spawned in the object testing arena.

Some dwarves like magma crabs for their *chittering*.

## Gallery

-

  Not handshake-friendly.\
  *Art by Piper.t*

-

  It's not much like a crab...\
  *Art by Rhynca-Rook*

-

  "Lithovore, uses magma to digest choice rocks. Little nub feet for scurrying. Sharp swimming fins. Spits burning rock globs."\
  *Concept art by Bay 12 Games.*

    [CREATURE:MAGMA_CRAB]
        [ARENA_RESTRICTED]
        [DESCRIPTION:A small rock-eating creature that lives in molten rock.  It scurries on little feet and swims through liquid rock with sharp wings.  It uses magma to digest rock and spits out burning globs.]
        [NAME:magma crab:magma crabs:magma crab]
        [CASTE_NAME:magma crab:magma crabs:magma crab]
        [CREATURE_TILE:'C'][COLOR:0:0:1]
        [PETVALUE:200]
        [NATURAL]
        [LARGE_ROAMING]
        [BIOME:SUBTERRANEAN_LAVA]
        [UNDERGROUND_DEPTH:3:5]
        [FREQUENCY:100]
        [POPULATION_NUMBER:25:50]
        [CLUSTER_NUMBER:1:5]
        [PREFSTRING:chittering]
        [ALL_ACTIVE]
        [NO_SLEEP]
        [HOMEOTHERM:12000]
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:6561:6115:5683:1755:7456:8567] 5 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:4732:4026:3327:1097:5922:7567] 8 kph
        [SWIMS_INNATE]
        [FIREIMMUNE]
        [NOT_BUTCHERABLE]
        [EXTRAVISION]
        [CANNOT_JUMP]
        [MAGMA_VISION]
        [NOBREATHE]
        [NOBONES]
        [BODY:BODY_WITH_HEAD_FLAG:BRAIN:MOUTH:2WINGS]
        [BODY_DETAIL_PLAN:CHITIN_MATERIALS]
        [BODY_DETAIL_PLAN:CHITIN_TISSUES]
        [BODY_DETAIL_PLAN:EXOSKELETON_TISSUE_LAYERS:CHITIN:FAT:MUSCLE]
        [BODY_DETAIL_PLAN:STANDARD_HEAD_POSITIONS]
        [CAN_DO_INTERACTION:MATERIAL_EMISSION]
            [CDI:TOKEN:SPIT_MOLTEN_ROCK]
            [CDI:ADV_NAME:Spit molten rock]
            [CDI:USAGE_HINT:ATTACK]
            [CDI:BP_REQUIRED:BY_CATEGORY:MOUTH]
            [CDI:MATERIAL:INORGANIC:BASALT:LIQUID_GLOB]
            [CDI:VERB:spit a glob of molten rock:spits a glob of molten rock:NA]
            [CDI:TARGET:C:LINE_OF_SIGHT]
            [CDI:TARGET_RANGE:C:15]
            [CDI:MAX_TARGET_NUMBER:C:1]
            [CDI:WAIT_PERIOD:30]
        [HAS_NERVES]
        [BODY_SIZE:0:0:1000]
        [BODY_SIZE:1:168:2000]
        [BODY_SIZE:5:0:30000]
        [MAXAGE:50:70]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:CHITIN]
                [TL_COLOR_MODIFIER:BLACK:1]
                    [TLCM_NOUN:exterior:SINGULAR]
        [SELECT_MATERIAL:ALL]
            [MULTIPLY_VALUE:2]
            [IF_EXISTS_SET_HEATDAM_POINT:13000]
            [IF_EXISTS_SET_IGNITE_POINT:13000]
            [IF_EXISTS_SET_MELTING_POINT:13000]
            [IF_EXISTS_SET_BOILING_POINT:15000]
