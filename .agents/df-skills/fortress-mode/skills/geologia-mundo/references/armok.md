# Armok

> Fonte: [Armok](https://dwarffortresswiki.org/index.php/Armok) — Dwarf Fortress Wiki (GFDL/MIT)

**Armok**, God of Blood, is the name of the creator deity in the lore of the original *Slaves to Armok: God of Blood*, and the in-game explanation for that game's random world generation:

*"Armok, the God of Blood, is just about the only constant in these chaotic random universes. A general sense of conflict keeps Armok appeased - when the universe becomes too boring, it is set on the anvil of creation to be reforged."*

*"The destruction of the world by Armok will arise inevitably in most game worlds. As civilizations spread and the frontier closes, the world will start to look homogeneous. Armok, looking upon this decadence in disgust, will reform the world. Basically, when the universe has become too boring, it will be changed."*

''"But who or what is Armok? ARMOK is the God of Blood…The Supreme God, he gives name to the game, his powers are literally endless…He creates and destroys whole Universes just for pleasure and fun. He enjoys watching death, destruction and, of course, blood run on his Universe…In a Universe, he can have billions of worshippers, while in another his existence might be unknown...but HE EXISTS. This cannot be denied, and allows to play almost any type universe…from a standard fantasy-type world to a “primitive”, stone age world…and, why not a “future world” with star travel? In fact, when Armok creates a Universe, he likes putting more than one planet in it!

*Remember…Armok can control and destroy all other creatures, including the other, ”lesser” gods, but he usually enjoys watching civilizations grow, because he hopes that one day these civilizations will fight each other, and thus generate conflict and slaughter!"*

Despite the above description, Armok is not actually present in *Dwarf Fortress* proper; he does not appear as a deity available for worshipping, nor does Toady One intend to add him into the game. Not that it stops players from referencing him, especially when something extremely fun is ensuing. As implied by his role of reshaping reality for the sake of his own amusement, Armok is essentially an in-lore name for the player of the game.

## Name

The name of the Dwarven God comes from the variable "arm_ok", which is from Tarn Adams's fantasy game, *Dragslay*. The variable was used to count the number of arms left, for inventory purposes. (Source)

Armok was immediately after used by a Bay12 forums user as a name, and afterwards, it stuck.

## Playable Armok mod

Copy this into any creature file in the raws, and play with your very own avatar of the God of Blood! Shoots fireballs, smites heretics with dragonfire, and slays mortal creatures with a single touch!

    [CREATURE:ARMOK]
        [DESCRIPTION:The blood god is risen.]
        [NAME:avatar of armok:avatars of armok:avatar of armok]
        [CREATURE_TILE:'A'][COLOR:4:0:1]
        [BODY:HUMANOID:MOUTH:TONGUE]
        [EXTRAVISION]
        [NOBREATHE][NOSTUN][NONAUSEA][NOPAIN][NO_DIZZINESS]
        [NOEMOTION][NOSTUCKINS][NOTHOUGHT][NOEXERT][NO_DRINK][NO_EAT][NO_SLEEP]
        [NO_GENDER][CAN_SPEAK]
        [PARALYZEIMMUNE][WEBIMMUNE]
        [NOT_LIVING]
        [BUILDINGDESTROYER:2][NOT_BUTCHERABLE]
        [SWIMS_INNATE]
        [OUTSIDER_CONTROLLABLE]
        [CANOPENDOORS][CAN_LEARN]
        [NO_THOUGHT_CENTER_FOR_MOVEMENT]
        [NO_CONNECTIONS_FOR_MOVEMENT]
        [EQUIPS]
        [PREFSTRING:omnipotence]
        [FIREIMMUNE]
        [FLIER]
        [NATURAL_SKILL:MELEE_COMBAT:25]
        [NATURAL_SKILL:RANGED_COMBAT:25]
        [NATURAL_SKILL:WRESTLING:25]
        [NATURAL_SKILL:BITE:25]
        [NATURAL_SKILL:GRASP_STRIKE:25]
        [NATURAL_SKILL:STANCE_STRIKE:25]
        [NATURAL_SKILL:DODGING:25]
        [NATURAL_SKILL:MISC_WEAPON:25]
        [NATURAL_SKILL:AXE:25]
        [NATURAL_SKILL:SWORD:25]
        [NATURAL_SKILL:DAGGER:25]
        [NATURAL_SKILL:MACE:25]
        [NATURAL_SKILL:HAMMER:25]
        [NATURAL_SKILL:SPEAR:25]
        [NATURAL_SKILL:CROSSBOW:25]
        [NATURAL_SKILL:SHIELD:25]
        [NATURAL_SKILL:ARMOR:25]
        [NATURAL_SKILL:SIEGECRAFT:25]
        [NATURAL_SKILL:SIEGEOPERATE:25]
        [NATURAL_SKILL:BOWYER:25]
        [NATURAL_SKILL:PIKE:25]
        [NATURAL_SKILL:WHIP:25]
        [NATURAL_SKILL:BOW:25]
        [NATURAL_SKILL:BLOWGUN:25]
        [NATURAL_SKILL:THROW:25]
        [TISSUE:SLADE]
            [TISSUE_NAME:slade:NP]
            [TISSUE_MATERIAL:INORGANIC:SLADE]
            [MUSCULAR]
            [FUNCTIONAL]
            [STRUCTURAL]
            [RELATIVE_THICKNESS:1]
            [CONNECTS]
            [TISSUE_SHAPE:LAYER]
        [TISSUE_LAYER:BY_CATEGORY:ALL:SLADE]
        [USE_MATERIAL_TEMPLATE:POISON:CREATURE_EXTRACT_TEMPLATE]
            [STATE_NAME:ALL_SOLID:touch of death]
            [STATE_ADJ:ALL_SOLID:touch of death]
            [STATE_NAME:LIQUID:touch of death]
            [STATE_ADJ:LIQUID:touch of death]
            [STATE_NAME:GAS:touch of death]
            [STATE_ADJ:GAS:touch of death]
            [PREFIX:NONE]
            [ENTERS_BLOOD]
            [SYNDROME]
                [SYN_NAME:curse of the blood god]
                [SYN_AFFECTED_CLASS:GENERAL_POISON]
                [SYN_IMMUNE_CREATURE:ARMOK:ALL]
                [SYN_INJECTED]
                [CE_NECROSIS:SEV:1000:PROB:100:BP:BY_CATEGORY:ALL:ALL:START:30:PEAK:60:END:1200]
        [BODY_SIZE:10:0:200000000]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:100:100:100:100:100:100:100]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:100:100:100:100:100:100:100]
        [CAN_DO_INTERACTION:MATERIAL_EMISSION]
            [CDI:ADV_NAME:Hurl fireball]
            [CDI:USAGE_HINT:ATTACK]
            [CDI:BP_REQUIRED:BY_CATEGORY:HAND]
            [CDI:FLOW:FIREBALL]
            [CDI:TARGET:C:LINE_OF_SIGHT]
            [CDI:TARGET_RANGE:C:15]
            [CDI:MAX_TARGET_NUMBER:C:1]
            [CDI:WAIT_PERIOD:1]
        [CAN_DO_INTERACTION:MATERIAL_EMISSION]
            [CDI:ADV_NAME:Smite]
            [CDI:USAGE_HINT:ATTACK]
            [CDI:BP_REQUIRED:BY_CATEGORY:HAND]
            [CDI:FLOW:DRAGONFIRE]
            [CDI:TARGET:C:LINE_OF_SIGHT]
            [CDI:TARGET_RANGE:C:15]
            [CDI:MAX_TARGET_NUMBER:C:1]
            [CDI:WAIT_PERIOD:1]
        [ATTACK:PUNCH:BODYPART:BY_TYPE:GRASP]
            [ATTACK_SKILL:GRASP_STRIKE]
            [ATTACK_VERB:touch:touches]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_WITH]
            [ATTACK_PRIORITY:MAIN]
            [SPECIALATTACK_INJECT_EXTRACT:LOCAL_CREATURE_MAT:POISON:LIQUID:100:100]
        [ITEMCORPSE:STATUE:NO_SUBTYPE:INORGANIC:SLADE]
        [ITEMCORPSE_QUALITY:5]

then copy this into entity_default.txt to play as the Blood God Incarnate in adventure mode. Don't worry, they won't appear in fortress mode or worldgen... yet.

    [ENTITY:CHEATER]
        [ALL_MAIN_POPS_CONTROLLABLE]
        [CREATURE:ARMOK]

Updated for v0.42\
Original creature design taken from GenericOverusedName on the Bay12 Forums. ()

\]\] \]\]
