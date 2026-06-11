# Cave floater

> Fonte: [Cave floater](https://dwarffortresswiki.org/index.php/Cave_floater) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes cave floaters for their graceful drifting.**
- **Biome**
- **Underground Depth: 2-3**
- **Attributes**
- **Flying · Genderless · No Stun · Syndrome**
- **Cannot be tamed**
- **Size**
- **Max:** 40,000 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** 15-30
- **Butchering returns**
- **Food items**
- **Raw materials**
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A floating pod with eye-stalks. It can spray poison and it gives off poison gas when punctured.*

**Cave floaters** are small floating creatures full of noxious gas, rarely found in groups of 1-3 individuals in the deepest caverns. The good news is that inhaling the gas won't kill your dwarves, though it may knock them unconscious. The bad news is that it's nearly impossible to avoid contamination, since it's an inhaled projectile weapon. It isn't typically necessary to fight these creatures, but if you must, you'll want to shoot them from afar.

Cave floaters cannot attack normally, except for their default push attack - instead, they launch a stream of steaming cave floater gas juice at attackers. This juice, despite being described as hot, doesn't seem to cause burns or indeed do much of anything. If you manage to kill a cave floater without puncturing it, take care **not** to butcher the corpse, as it will detonate the gas right there in the butcher's shop. It's not generally worth it anyway, as the only thing produced will be a single cave floater skin.

If a cave floater is exposed to temperatures below 10000 °U (0 °C), such as by luring it out onto a glacier, it will die as a result of condensation. *(This is because cave floater gas, which constitutes the [`[FUNCTIONAL]`](/index.php/Tissue_definition_token#FUNCTIONAL "Tissue definition token") tissue material of its [`[THOUGHT]`](/index.php/Body_token#THOUGHT "Body token") body part, condenses at this temperature).*

Cave floaters possess a pet value of 50, but lack the necessary tokens to be trainable. Additionally, they may not be spawned in the object testing arena.

Some dwarves like cave floaters for their *graceful drifting*.

He who smelt it, died.\
*Crudely drawn by Zippy*

    [CREATURE:CAVE_FLOATER]
        [ARENA_RESTRICTED]
        [DESCRIPTION:A floating pod with eye-stalks.  It can spray poison and it gives off poison gas when punctured.]
        [NAME:cave floater:cave floaters:cave floater]
        [CASTE_NAME:cave floater:cave floaters:cave floater]
        [CREATURE_TILE:'f'][COLOR:6:0:1]
        [CREATURE_CLASS:POISONOUS]
        [PETVALUE:50]
        [BIOME:SUBTERRANEAN_CHASM]
        [UNDERGROUND_DEPTH:2:3]
        [LARGE_ROAMING]
        [FREQUENCY:10]
        [EXTRAVISION][NOBREATHE][NOSTUN][NONAUSEA][NOEMOTION]
        [FLIER]
        [NOBONES]
        [NATURAL]
        [POPULATION_NUMBER:30:50]
        [CLUSTER_NUMBER:1:3]
        [PREFSTRING:graceful drifting]
        [BODY:BASIC_1PARTBODY_FLYING_HEAD_FLAG_THOUGHT:2EYESTALKS]
        [USE_MATERIAL_TEMPLATE:POD_JUICE:CREATURE_EXTRACT_TEMPLATE]
            [STATE_NAME:ALL_SOLID:frozen cave floater juice]
            [STATE_ADJ:ALL_SOLID:frozen cave floater juice]
            [STATE_NAME:LIQUID:cave floater juice]
            [STATE_ADJ:LIQUID:cave floater juice]
            [STATE_NAME:GAS:cave floater gas]
            [STATE_ADJ:GAS:cave floater gas]
            [MELTING_POINT:9950]
            [BOILING_POINT:10000]
            [PREFIX:NONE]
            [SYNDROME]
                [SYN_NAME:cave floater sickness]
                [SYN_AFFECTED_CLASS:GENERAL_POISON]
                [SYN_IMMUNE_CREATURE:CAVE_FLOATER:ALL]
                [SYN_INHALED][SYN_INGESTED]
                [CE_FEVER:SEV:50:PROB:100:RESISTABLE:START:50:PEAK:500:END:1500]
                [CE_NAUSEA:SEV:35:PROB:100:RESISTABLE:START:50:PEAK:100:END:300]
                [CE_DROWSINESS:SEV:75:PROB:100:RESISTABLE:START:1000:PEAK:2000:END:4000]
                [CE_DIZZINESS:SEV:75:PROB:100:RESISTABLE:START:1000:PEAK:2000:END:3000]
        [USE_MATERIAL_TEMPLATE:SKIN:SKIN_TEMPLATE]
        [USE_MATERIAL_TEMPLATE:LEATHER:LEATHER_TEMPLATE]
        [USE_MATERIAL_TEMPLATE:PARCHMENT:PARCHMENT_TEMPLATE]
        [TISSUE:GAS]
            [TISSUE_NAME:interior gas:NP]
            [TISSUE_MATERIAL:LOCAL_CREATURE_MAT:POD_JUICE]
            [TISSUE_MAT_STATE:GAS]
            [MUSCULAR]
            [FUNCTIONAL]
            [STRUCTURAL]
            [RELATIVE_THICKNESS:10]
            [CONNECTS]
            [TISSUE_SHAPE:LAYER]
            [TISSUE_LEAKS]
        [TISSUE_LAYER:BY_CATEGORY:BODY:GAS]
        [TISSUE:POD]
            [TISSUE_NAME:pod:NP]
            [TISSUE_MATERIAL:LOCAL_CREATURE_MAT:SKIN]
            [TISSUE_MAT_STATE:SOLID]
            [STRUCTURAL]
            [RELATIVE_THICKNESS:1]
            [CONNECTS]
            [TISSUE_SHAPE:LAYER]
        [TISSUE_LAYER:BY_CATEGORY:ALL:POD]
        [CAN_DO_INTERACTION:MATERIAL_EMISSION]
            [CDI:TOKEN:SPRAY_JUICE]
            [CDI:ADV_NAME:Spray juice]
            [CDI:USAGE_HINT:ATTACK]
            [CDI:BP_REQUIRED:BY_CATEGORY:BODY]
            [CDI:MATERIAL:LOCAL_CREATURE_MAT:POD_JUICE:TRAILING_GAS_FLOW]
            [CDI:VERB:spray a stream of steaming juice:sprays a stream of steaming juice:NA]
            [CDI:TARGET:C:LINE_OF_SIGHT]
            [CDI:TARGET_RANGE:C:5]
            [CDI:MAX_TARGET_NUMBER:C:1]
            [CDI:WAIT_PERIOD:30]
        [APPLY_CREATURE_VARIATION:STANDARD_FLYING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_WALK_CRAWL_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph
        [BODY_SIZE:0:0:40000]
        [MAXAGE:15:30]
        [ALL_ACTIVE]
        [LOW_LIGHT_VISION:10000]
        [NO_SLEEP]
        [NO_DIZZINESS]
        [NO_FEVERS]
        [CANNOT_JUMP]
        [SET_TL_GROUP:BY_CATEGORY:ALL:POD]
            [TL_COLOR_MODIFIER:CLEAR:1]
                [TLCM_NOUN:exterior:SINGULAR]
