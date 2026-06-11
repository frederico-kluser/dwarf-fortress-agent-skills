# Fire man

> Fonte: [Fire man](https://dwarffortresswiki.org/index.php/Fire_man) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes fire men for their licks of fire.**
- **Biome**
- **Underground Depth: 3-4**
- **Attributes**
- **Building destroyer : Level 2**
- **Genderless · No Stun · No Pain · No Exert · Fire immune · Humanoid**
- **Cannot be tamed**
- **Size**
- **Max:** 70,000 cm 3
- **Age**
- **Adult at:** Birth
- **Max age:** Immortal
- **Becomes after death**
- **Ash**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*Fire in the shape of a human that can hurl fireballs.*

**Fire men** are exceptionally rare construct creatures made of fire, found in the magma sea. They stand at the size of a human, feel no emotion, no exertion, don't need to breathe, are immune to pain and cannot be stunned. When a fire man is killed, it leaves behind a bar of ash which can be made into lye or potash. Because they live in the magma sea and are building destroyers, one should be cautious when setting up magma forges in the event one of them actually shows up. Despite being made of fire, they can be safely captured and stored in wooden cages and are unharmed by touching water. Fire men are immortal and only die from violence.

Fire men are only dangerous because of their natural heat and fire attacks (a fireball throw and a fire jet throw.) Their punches and kicks are harmless on their own, and their flame body is extremely fragile, so don't be surprised if a baby punches a fire man to death. However, actually killing a fire man can be quite fun, as the resulting burst of flame tends to set nearby creatures on fire.

Some dwarves like fire men for their *licks of fire*.

Admired for their *licks of fire*.

|  |
|----|
| "Fire man" in other / Languages / Dwarven / : / ziril udos / Elven / : / inira onino / Goblin / : / zedan ngorûg / Human / : / usmok abo |

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

Make sure you remove any books from your possession when facing a Fire Man in adventure mode. Sighting a book will send the Fire Man into a murderous rage!

Fire men tend to be obsessed with a distorted view of justice, mercilessly attacking those they view as evildoers.

Very rarely, unconscious humans have been known to transform into special types of fire men. These are indestructible, blindly aggressive and can only be controlled by outside sources.

Some fire men are known for their heroic deeds, joining teams of up to four members in order to protect innocents from outworldly threats.

## In real life

"Fire man", also spelled "fireman", is an archaic English term for a firefighter. In real life, they are not made of fire\[Verify\], and in fact tend to quell it rather than spread it.

    [CREATURE:ELEMENTMAN_FIRE]
        [DESCRIPTION:Fire in the shape of a human that can hurl fireballs.]
        [NAME:fire man:fire men:fire man]
        [CASTE_NAME:fire man:fire men:fire man]
        [CREATURE_TILE:'M'][COLOR:4:0:1]
        [CAN_DO_INTERACTION:MATERIAL_EMISSION]
            [CDI:TOKEN:HURL_FIREBALL]
            [CDI:ADV_NAME:Hurl fireball]
            [CDI:USAGE_HINT:ATTACK]
            [CDI:FLOW:FIREBALL]
            [CDI:TARGET:C:LINE_OF_SIGHT]
            [CDI:TARGET_RANGE:C:15]
            [CDI:MAX_TARGET_NUMBER:C:2]
            [CDI:WAIT_PERIOD:30]
        [CAN_DO_INTERACTION:MATERIAL_EMISSION]
            [CDI:TOKEN:SPRAY_FIRE_JET]
            [CDI:ADV_NAME:Spray jet of fire]
            [CDI:USAGE_HINT:ATTACK]
            [CDI:FLOW:FIREJET]
            [CDI:TARGET:C:LINE_OF_SIGHT]
            [CDI:TARGET_RANGE:C:5]
            [CDI:MAX_TARGET_NUMBER:C:1]
            [CDI:WAIT_PERIOD:30]
        [FIREIMMUNE][MAGMA_VISION]
        [LARGE_ROAMING]
        [BIOME:SUBTERRANEAN_LAVA]
        [UNDERGROUND_DEPTH:3:4]
        [FREQUENCY:1][DIFFICULTY:2]
        [POPULATION_NUMBER:15:30]
        [NOPAIN][EXTRAVISION][NOBREATHE][NOSTUN][NONAUSEA][NOEMOTION]
            [NOTHOUGHT][NOEXERT]
        [NO_DIZZINESS]
        [NO_FEVERS]
        [FIXED_TEMP:10800]
        [BUILDINGDESTROYER:2]
        [LARGE_PREDATOR]
        [NO_DRINK][NO_EAT][NO_SLEEP]
        [NOT_LIVING]
        [CANOPENDOORS]
        [NOT_BUTCHERABLE]
        [NOFEAR]
        [PREFSTRING:licks of fire]
        [NOBONES]
        [ODOR_STRING:smoke]
        [ODOR_LEVEL:50]
        [SMELL_TRIGGER:10000] cannot smell
        [BODY:HUMANOID_SIMPLE]
        [NO_THOUGHT_CENTER_FOR_MOVEMENT]
        [USE_MATERIAL_TEMPLATE:FLAME:FLAME_TEMPLATE]
            [MAT_FIXED_TEMP:10800]
        [USE_TISSUE_TEMPLATE:FLAME:FLAME_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:ALL:FLAME]
        [BODY_SIZE:0:0:70000]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
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
        [ITEMCORPSE:BAR:NO_SUBTYPE:ASH:NO_MATGLOSS]
        [ALL_ACTIVE]
        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:900:711:521:293:1900:2900] 30 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:2990:2257:1525:731:4300:6100] 12 kph
        [SWIMS_INNATE]
