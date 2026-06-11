# Dog

> Fonte: [Dog](https://dwarffortresswiki.org/index.php/Dog) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes dogs for their loyalty.**
- **Biome**
- **Domesticated**
- **Attributes**
- **War animals · Hunting animals**
- **Tamed Attributes**
- **Pet value:** 30
- **Trainable : Hunting War**
- **Size**
- **Birth:** 1,000 cm 3
- **Mid:** 12,500 cm 3
- **Max:** 30,000 cm 3
- **Age**
- **Adult at:** 1
- **Max age:** 10-20
- **Butchering returns**
- **Food items**
- **Meat:** 6-13
- **Fat:** 6-13
- **Brain:** 1
- **Heart:** 0-1
- **Lungs:** 2
- **Intestines:** 1
- **Liver:** 0-1
- **Kidneys:** 0-2
- **Tripe:** 0-1
- **Sweetbread:** 0-1
- **Spleen:** 0-1
- **Raw materials**
- **Bones:** 4-11
- **Skull:** 1
- **Skin:** Raw hide

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*A medium-sized highly social mammalian carnivore. It has a keen sense of smell. It can be trained to obey commands.*

**Dogs** are common domestic animals that can be trained to assist your dwarves in combat or hunting as either war dogs or hunting dogs. Like all tame animals, they can serve as an emergency food supply and provide you with bones, leather, and skulls. Dogs do not require any food.

Some dwarves like dogs for their *loyalty*.

## Using dogs

Dogs left to their own devices will wander around, spending most of their time in meeting areas, and attacking any hostiles they see.

Newborn dogs will reach a size of 12,500 cm³ after one year, and 30,000 cm³ after two years. Cats have a similar growth curve, and also require no food, however fully-grown dogs are six times larger than cats and will not adopt dwarves on their own, making them more suitable as livestock.

As with any friendly creature, dogs can spot ambushers and thieves. You can assign dogs to restraints to act as guard dogs. Guard dogs work particularly well when placed behind a hall of traps or other siege-breaking devices. The traps will prevent aggressive invaders from harming the dogs, while the dogs prevent thieves from sneaking past the traps into the base. (Ideally, the dogs should be out of view of the trap corridor to prevent injury from ranged weapons.) Hunting dogs may be particularly well-suited to guard duty because of their improved observer skills.

You can assign a war or hunting dog to a dwarf via their preferences menu (v, select dwarf, p, a) to help them in combat. It will follow the dwarf like a pet.

Once a dog is assigned to a dwarf, it cannot be unassigned nor placed in a cage. A workaround for this is to train the dog with the dwarf you want the dog to follow. Unassigned war dogs and hunting dogs follow the dwarf who trained them, but can still be caged. If you use one or two dedicated animal trainers to train dogs, you may notice they will be followed by a large pack of them, along with their puppies. Assigned dogs **can** be pastured; this is another option for keeping them away from danger if you have some advance warning. It's also a good idea if you decide to train the owner in a danger room. War dogs can still be slaughtered for food, even if they have sustained serious injuries.

**Note:** *Using a civilian alert to keep civilians away from fighting affects war dogs as well, stopping them from following your soldiers into combat.*Bug:1058

## Hunting dogs

*"A hunting animal will target the creature its owner is targeting if the owner is hunting, and it will be sneaking without a movement penalty if it is reasonably close to its hunting owner. A hunting animal notices creatures from farther away, although this isn't exactly effective if it decides to target what its owner is targeting. It all needs a bit of work, but that is true of hunting in general."* -Toady One, long ago

## War dogs

Because of their training, war dogs do more damage in combat than untrained dogs.

Against heavily armored and armed opponents, dogs (war or hunting) can die quite easily, but that doesn't mean they are *useless*. Also, although a war dog is not nearly as dangerous against an armored opponent as an axe lord, they occasionally get lucky, and a pack of war dogs can be very dangerous indeed. They can also be used as walking meatshields, taking hits that would have otherwise injured your dwarves.

For this reason, some players attach them to any permanent close-combat military, and/or to any dwarf that regularly steps outside. However, the down side to assigning them to military dwarves is that they are very likely to die, since dogs move much faster than fully-armored dwarves and thus frequently charge in unassisted. A dead pet causes a serious unhappiness spike, and tantrums with legendary weapon skills mixed in can really maximize the fun. Fortunately they're not cats so you can make them unavailable as pets.

For breeding purposes, female war dogs are no worse than any other animal: they can give birth to, in this case, puppies as well. Male war dogs also can play the role of their civil counterparts. You probably don't want to train the female dogs though, so you can keep them as breeding stock along with a few studs, just like you do with any other animal.

## In real life

In real life, the dog (*Canis lupus familiaris*) is recognized as a subspecies of the wolf (*Canis lupus lupus*), having undergone gradual genetic divergence from wild wolves due to domestication by humans. Human-dog companionship has existed as far back as 20,000 BC. In *Dwarf Fortress*, taming wolves will not, no matter how much time passes, result in dogs.

## Bugs

- Dogs sometimes won't bite, but only scratch, greatly reducing their combat effectiveness. This seems to happen against wildlife.Bug:7541

|  |
|----|
| "Dog" in other / Languages / Dwarven / : / idar / Elven / : / macetha / Goblin / : / anot / Human / : / sheka |

\

Admired for its *loyalty*.

    [CREATURE:DOG]
        [DESCRIPTION:A medium-sized highly social mammalian carnivore.  It has a keen sense of smell.  It can be trained to obey commands.]
        [NAME:dog:dogs:canine]
        [CASTE_NAME:dog:dogs:canine]
        [CREATURE_TILE:'d'][COLOR:6:0:0]
        [CREATURE_CLASS:MAMMAL]
        [PETVALUE:30][NATURAL]
        [LARGE_ROAMING]
        [COMMON_DOMESTIC][TRAINABLE][PET]
        [BONECARN]
        [PREFSTRING:loyalty]
        [BODY:QUADRUPED_NECK:TAIL:2EYES:2EARS:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:NECK:SPINE:BRAIN:SKULL:4TOES_FQ_REG:4TOES_RQ_REG:MOUTH:TONGUE:GENERIC_TEETH_WITH_LARGE_EYE_TEETH:RIBCAGE]
        [BODYGLOSS:PAW]
        [BODY_DETAIL_PLAN:STANDARD_MATERIALS]
        [BODY_DETAIL_PLAN:STANDARD_TISSUES]
        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:BONE:CARTILAGE]
        [BODY_DETAIL_PLAN:BODY_HAIR_TISSUE_LAYERS:HAIR]
        [USE_MATERIAL_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]
        [TISSUE_LAYER:BY_CATEGORY:TOE:NAIL:FRONT]
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
        [BODY_SIZE:0:0:1000]
        [BODY_SIZE:1:0:12500]
        [BODY_SIZE:2:0:30000]
        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110]
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110]
        [MAXAGE:10:20]
        [ATTACK:BITE:CHILD_BODYPART_GROUP:BY_CATEGORY:HEAD:BY_CATEGORY:TOOTH]
            [ATTACK_SKILL:BITE]
            [ATTACK_VERB:bite:bites]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:MAIN]
            [ATTACK_FLAG_CANLATCH]
        [ATTACK:SCRATCH:CHILD_TISSUE_LAYER_GROUP:BY_TYPE:STANCE:BY_CATEGORY:ALL:NAIL]
            [ATTACK_SKILL:STANCE_STRIKE]
            [ATTACK_VERB:scratch:scratches]
            [ATTACK_CONTACT_PERC:100]
            [ATTACK_PENETRATION_PERC:100]
            [ATTACK_FLAG_EDGE]
            [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:SECOND]
            [ATTACK_FLAG_BAD_MULTIATTACK]
        [CHILD:1]
        [GENERAL_CHILD_NAME:puppy:puppies]
        [DIURNAL]
        [HOMEOTHERM:10070]
        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:447:298:149:1900:2900] 59 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:9000:8900:8825:8775:9500:9900] 1 kph, NO DATA
        [SWIMS_INNATE]
        [MUNDANE]
        [CASTE:FEMALE]
            [FEMALE]
        [CASTE:MALE]
            [MALE]
            [SET_BP_GROUP:BY_TYPE:LOWERBODY][BP_ADD_TYPE:GELDABLE]
        [SELECT_CASTE:ALL]
            [SET_TL_GROUP:BY_CATEGORY:BODY_UPPER:HAIR]
             [PLUS_TL_GROUP:BY_CATEGORY:BODY_LOWER:HAIR]
             [PLUS_TL_GROUP:BY_CATEGORY:LEG_FRONT:HAIR]
             [PLUS_TL_GROUP:BY_CATEGORY:LEG_REAR:HAIR]
        [TL_COLOR_MODIFIER:BLACK:1:BROWN:1:WHITE:1:GRAY:1:LIGHT_BROWN:1:DARK_BROWN:1:TAN:1:AUBURN:1:CHESTNUT:1:SLATE_GRAY:1:CREAM:1:CINNAMON:1:BUFF:1:BEIGE:1:CHOCOLATE:1:CHARCOAL:1:ASH_GRAY:1:RUSSET:1:IVORY:1:FLAX:1:PUMPKIN:1:GOLD:1:GOLDEN_YELLOW:1:GOLDENROD:1:COPPER:1:SAFFRON:1:AMBER:1:MAHOGANY:1:OCHRE:1:PALE_BROWN:1:RAW_UMBER:1:BURNT_SIENNA:1:BURNT_UMBER:1:SEPIA:1:DARK_TAN:1:PALE_CHESTNUT:1:DARK_CHESTNUT:1:TAUPE_PALE:1:TAUPE_DARK:1:TAUPE_SANDY:1:TAUPE_GRAY:1:TAUPE_MEDIUM:1:ECRU:1]
                    [TLCM_NOUN:hair:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EAR:HAIR]
        [TL_COLOR_MODIFIER:BLACK:1:BROWN:1:WHITE:1:GRAY:1:LIGHT_BROWN:1:DARK_BROWN:1:TAN:1:AUBURN:1:CHESTNUT:1:SLATE_GRAY:1:CREAM:1:CINNAMON:1:BUFF:1:BEIGE:1:CHOCOLATE:1:CHARCOAL:1:ASH_GRAY:1:RUSSET:1:IVORY:1:FLAX:1:PUMPKIN:1:GOLD:1:GOLDEN_YELLOW:1:GOLDENROD:1:COPPER:1:SAFFRON:1:AMBER:1:MAHOGANY:1:OCHRE:1:PALE_BROWN:1:RAW_UMBER:1:BURNT_SIENNA:1:BURNT_UMBER:1:SEPIA:1:DARK_TAN:1:PALE_CHESTNUT:1:DARK_CHESTNUT:1:TAUPE_PALE:1:TAUPE_DARK:1:TAUPE_SANDY:1:TAUPE_GRAY:1:TAUPE_MEDIUM:1:ECRU:1]
                    [TLCM_NOUN:ears:PLURAL]
            [SET_TL_GROUP:BY_CATEGORY:TAIL:HAIR]
        [TL_COLOR_MODIFIER:BLACK:1:BROWN:1:WHITE:1:GRAY:1:LIGHT_BROWN:1:DARK_BROWN:1:TAN:1:AUBURN:1:CHESTNUT:1:SLATE_GRAY:1:CREAM:1:CINNAMON:1:BUFF:1:BEIGE:1:CHOCOLATE:1:CHARCOAL:1:ASH_GRAY:1:RUSSET:1:IVORY:1:FLAX:1:PUMPKIN:1:GOLD:1:GOLDEN_YELLOW:1:GOLDENROD:1:COPPER:1:SAFFRON:1:AMBER:1:MAHOGANY:1:OCHRE:1:PALE_BROWN:1:RAW_UMBER:1:BURNT_SIENNA:1:BURNT_UMBER:1:SEPIA:1:DARK_TAN:1:PALE_CHESTNUT:1:DARK_CHESTNUT:1:TAUPE_PALE:1:TAUPE_DARK:1:TAUPE_SANDY:1:TAUPE_GRAY:1:TAUPE_MEDIUM:1:ECRU:1]
                    [TLCM_NOUN:tail:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:HEAD:HAIR]
        [TL_COLOR_MODIFIER:BLACK:1:BROWN:1:WHITE:1:GRAY:1:LIGHT_BROWN:1:DARK_BROWN:1:TAN:1:AUBURN:1:CHESTNUT:1:SLATE_GRAY:1:CREAM:1:CINNAMON:1:BUFF:1:BEIGE:1:CHOCOLATE:1:CHARCOAL:1:ASH_GRAY:1:RUSSET:1:IVORY:1:FLAX:1:PUMPKIN:1:GOLD:1:GOLDEN_YELLOW:1:GOLDENROD:1:COPPER:1:SAFFRON:1:AMBER:1:MAHOGANY:1:OCHRE:1:PALE_BROWN:1:RAW_UMBER:1:BURNT_SIENNA:1:BURNT_UMBER:1:SEPIA:1:DARK_TAN:1:PALE_CHESTNUT:1:DARK_CHESTNUT:1:TAUPE_PALE:1:TAUPE_DARK:1:TAUPE_SANDY:1:TAUPE_GRAY:1:TAUPE_MEDIUM:1:ECRU:1]
                    [TLCM_NOUN:head:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:FOOT_FRONT:HAIR]
             [PLUS_TL_GROUP:BY_TOKEN:RFTOE1:HAIR]
             [PLUS_TL_GROUP:BY_TOKEN:RFTOE2:HAIR]
             [PLUS_TL_GROUP:BY_TOKEN:RFTOE3:HAIR]
             [PLUS_TL_GROUP:BY_TOKEN:RFTOE4:HAIR]
             [PLUS_TL_GROUP:BY_TOKEN:LFTOE1:HAIR]
             [PLUS_TL_GROUP:BY_TOKEN:LFTOE2:HAIR]
             [PLUS_TL_GROUP:BY_TOKEN:LFTOE3:HAIR]
             [PLUS_TL_GROUP:BY_TOKEN:LFTOE4:HAIR]
        [TL_COLOR_MODIFIER:BLACK:1:BROWN:1:WHITE:1:GRAY:1:LIGHT_BROWN:1:DARK_BROWN:1:TAN:1:AUBURN:1:CHESTNUT:1:SLATE_GRAY:1:CREAM:1:CINNAMON:1:BUFF:1:BEIGE:1:CHOCOLATE:1:CHARCOAL:1:ASH_GRAY:1:RUSSET:1:IVORY:1:FLAX:1:PUMPKIN:1:GOLD:1:GOLDEN_YELLOW:1:GOLDENROD:1:COPPER:1:SAFFRON:1:AMBER:1:MAHOGANY:1:OCHRE:1:PALE_BROWN:1:RAW_UMBER:1:BURNT_SIENNA:1:BURNT_UMBER:1:SEPIA:1:DARK_TAN:1:PALE_CHESTNUT:1:DARK_CHESTNUT:1:TAUPE_PALE:1:TAUPE_DARK:1:TAUPE_SANDY:1:TAUPE_GRAY:1:TAUPE_MEDIUM:1:ECRU:1]
                    [TLCM_NOUN:front paws:PLURAL]
            [SET_TL_GROUP:BY_CATEGORY:FOOT_REAR:HAIR]
             [PLUS_TL_GROUP:BY_TOKEN:RRTOE1:HAIR]
             [PLUS_TL_GROUP:BY_TOKEN:RRTOE2:HAIR]
             [PLUS_TL_GROUP:BY_TOKEN:RRTOE3:HAIR]
             [PLUS_TL_GROUP:BY_TOKEN:RRTOE4:HAIR]
             [PLUS_TL_GROUP:BY_TOKEN:LRTOE1:HAIR]
             [PLUS_TL_GROUP:BY_TOKEN:LRTOE2:HAIR]
             [PLUS_TL_GROUP:BY_TOKEN:LRTOE3:HAIR]
             [PLUS_TL_GROUP:BY_TOKEN:LRTOE4:HAIR]
        [TL_COLOR_MODIFIER:BLACK:1:BROWN:1:WHITE:1:GRAY:1:LIGHT_BROWN:1:DARK_BROWN:1:TAN:1:AUBURN:1:CHESTNUT:1:SLATE_GRAY:1:CREAM:1:CINNAMON:1:BUFF:1:BEIGE:1:CHOCOLATE:1:CHARCOAL:1:ASH_GRAY:1:RUSSET:1:IVORY:1:FLAX:1:PUMPKIN:1:GOLD:1:GOLDEN_YELLOW:1:GOLDENROD:1:COPPER:1:SAFFRON:1:AMBER:1:MAHOGANY:1:OCHRE:1:PALE_BROWN:1:RAW_UMBER:1:BURNT_SIENNA:1:BURNT_UMBER:1:SEPIA:1:DARK_TAN:1:PALE_CHESTNUT:1:DARK_CHESTNUT:1:TAUPE_PALE:1:TAUPE_DARK:1:TAUPE_SANDY:1:TAUPE_GRAY:1:TAUPE_MEDIUM:1:ECRU:1]
                    [TLCM_NOUN:rear paws:PLURAL]
            [SET_TL_GROUP:BY_CATEGORY:ALL:SKIN]
        [TL_COLOR_MODIFIER:BROWN:1:BURNT_UMBER:1:CINNAMON:1:COPPER:1:DARK_BROWN:1:DARK_PEACH:1:DARK_TAN:1:ECRU:1:PALE_BROWN:1:PALE_CHESTNUT:1:PALE_PINK:1:PEACH:1:PINK:1:RAW_UMBER:1:SEPIA:1:TAN:1:TAUPE_PALE:1:TAUPE_SANDY:1]
                    [TLCM_NOUN:skin:SINGULAR]
            [SET_TL_GROUP:BY_CATEGORY:EYE:EYE]
                [TL_COLOR_MODIFIER:IRIS_EYE_AMBER:1:IRIS_EYE_AQUA:1:IRIS_EYE_AQUAMARINE:1:IRIS_EYE_ASH_GRAY:1:IRIS_EYE_AUBURN:1:IRIS_EYE_AZURE:1:IRIS_EYE_BLUE:1:IRIS_EYE_BRASS:1:IRIS_EYE_BRONZE:1:IRIS_EYE_BROWN:1:IRIS_EYE_CERULEAN:1:IRIS_EYE_CHESTNUT:1:IRIS_EYE_CHOCOLATE:1:IRIS_EYE_CINNAMON:1:IRIS_EYE_COPPER:1:IRIS_EYE_DARK_BLUE:1:IRIS_EYE_DARK_BROWN:1:IRIS_EYE_DARK_CHESTNUT:1:IRIS_EYE_DARK_GREEN:1:IRIS_EYE_DARK_OLIVE:1:IRIS_EYE_DARK_TAN:1:IRIS_EYE_ECRU:1:IRIS_EYE_EMERALD:1:IRIS_EYE_FERN_GREEN:1:IRIS_EYE_GRAY:1:IRIS_EYE_GREEN:1:IRIS_EYE_JADE:1:IRIS_EYE_LIGHT_BLUE:1:IRIS_EYE_LIGHT_BROWN:1:IRIS_EYE_MAHOGANY:1:IRIS_EYE_MIDNIGHT_BLUE:1:IRIS_EYE_OCHRE:1:IRIS_EYE_OLIVE:1:IRIS_EYE_PALE_BLUE:1:IRIS_EYE_PALE_BROWN:1:IRIS_EYE_PALE_CHESTNUT:1:IRIS_EYE_PERIWINKLE:1:IRIS_EYE_PINE_GREEN:1:IRIS_EYE_RAW_UMBER:1:IRIS_EYE_RUSSET:1:IRIS_EYE_SEA_GREEN:1:IRIS_EYE_SEPIA:1:IRIS_EYE_SKY_BLUE:1:IRIS_EYE_SLATE_GRAY:1:IRIS_EYE_SPRING_GREEN:1:IRIS_EYE_TAN:1:IRIS_EYE_TAUPE_DARK:1:IRIS_EYE_TAUPE_GRAY:1:IRIS_EYE_TAUPE_MEDIUM:1:IRIS_EYE_TAUPE_PALE:1:IRIS_EYE_TAUPE_SANDY:1:IRIS_EYE_TEAL:1:IRIS_EYE_TURQUOISE:1]
                    [TLCM_NOUN:eyes:PLURAL]
