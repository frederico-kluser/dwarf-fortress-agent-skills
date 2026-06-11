# Cheating

> Fonte: [Cheating](https://dwarffortresswiki.org/index.php/Cheating) — Dwarf Fortress Wiki (GFDL/MIT)

**Cheating** is altering the game to make *Dwarf Fortress* conceptually easier — this is distinct from exploits, which take advantage of existing bugs or design oversights. There are two main ways to alter the game: changing the game's raw source files (which are really just text files), and directly altering the game's memory (which requires special tools). As with using exploits, whether or not to cheat is down to personal taste — after all, the game is *designed* to be readily moddable. Too much cheating can spoil your experience of *Dwarf Fortress*, but there are no other players to cheat — only yourself.

## Raw Editing

For making modifications to a newly-generated world, edit the raw files located in the **dwarffortress/raw/objects** folder *before* generating the game. For making modifications to an existing world, edit the raw files located in the **raw/objects** sub-folder of the saved game folder for that world.

The most common use of editing raw files is to get free items, such as gems, adamantine, or flux.

When changing the raw files, you may or may not need to create a new world in order for your changes to be reflected.

Generally speaking, *modifications* to an existing entry in a raw file don't require a new world gen, altering existing reactions or creatures being one example. However, when adding or deleting entries, you need to create a new world for the changes to take place, and when deleting, it can and probably will render your old world unplayable, as attempting to play worlds generated before the deletion will cause an error.

Shaostoul's Guide contains several cut & paste examples for editing raw files specifically for the purpose of cheating.

## Creature Token Modifications

Modifying creature files does not require the creation of a new world. You can modify the physical attributes of a creature, make animals tamable and trainable, make your dwarves into short little bearded terminators, and much more.

### Instructions for use:

1.  Open creature_standard.txt
2.  Find dwarven (or other creature) stats, which ought to resemble the sets below.
3.  Delete those stats and replace with the new set.
4.  Done.

- Notepad++ is recommended for altering raw files on Windows.

### Speedy Dwarves

Getting bored with slow dwarves? Open raw/objects/creature_standard.txt, look for `APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS`, and change the six numbers after it (0 is fastest). This can impact framerate in some cases - using 3 instead of 0 has been known to help.

        [APPLY_CREATURE_VARIATION:STANDARD_BIPED_GAITS:0:0:0:0:0:0]
        [APPLY_CREATURE_VARIATION:STANDARD_CLIMBING_GAITS:0:0:0:0:0:0]
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:0:0:0:0:0:0]
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:0:0:0:0:0:0]

### Immune Dwarves

Don't want to care for your dwarves? Simply add \[NO_EAT\] \[NO_SLEEP\] and \[NO_DRINK\] to your dwarves' raws and never care for them again. (Warning when editing \[NO_SLEEP\], because sometimes dwarves will rest and just never wake up)

As an added bonus, try adding \[NOFEAR\] (may take on an unwinnable fight) \[NOBREATHE\] \[AMPHIBIOUS\] (just in case) \[PARALYZEIMMUNE\] \[NOSTUN\] \[NONAUSEA\] \[NOPAIN\] \[NO_DIZZINESS\] \[NO_FEVERS\] \[WEBIMMUNE\] \[EXTRAVISION\] (won't suffer from blindness) \[FIREIMMUNE_SUPER\] \[MAGMA_VISION\] and \[NOEXERT\] as well.

(Warning, editing this may cause the game to crash.)

Other potential problems include, but are not limited to; unhappiness due to never drinking any booze, and insane dwarves with no viable avenues for suicide; not that they can't be assisted in such endeavors.

Also remove: \[CREATURE_CLASS:GENERAL_POISON\], \[GETS_WOUND_INFECTIONS\] and \[GETS_INFECTIONS_FROM_ROT\]

- Removing \[MAXAGE\] will prevent necromancer slabs from spawning.
- Removing the \[ALCOHOL_DEPENDENT\] tag should alleviate the problem of unhappiness due to never drinking booze.
- Removing the \[CAVE_ADAPT\] tag will eliminate cave adaptation but will also remove bonuses for dwarves in caves.

NOTE\* When generating a new world with the \[no_eat\] variable the world will crash, you can remove the \[no_eat\] variable while the world is being created and add it back before you 'accept' and save the new world.

### Pets for everyone

Ever want cave dragons, giant cave spiders, or even helmet snakes for pets?

Simply add \[PET\] and \[COMMON_DOMESTIC\] to the creature of your choice; then generate a new world-enjoy killing the local elephant population with your army of giant cave spiders. Also, if you want them to not be caged, cut out their raw file and transfer it to the bottom part of the creature_domestic.txt file and change the \[FANCIFUL\] token into the \[NATURAL\] token.

Alternatively, you can gain access to all in-game creatures as pets. Just add to mountain entity \[ANIMAL\] definition with only \[ANIMALS_ALWAYS_PRESENT\]. You can embark even with demons, humans, angels, night trolls and bronze colossi as pets. Intelligent creatures will be citizens, others will be pets and can change labors only with DFhack, but all will be tame. Don't embark with griffon, centaur, chimera and nothing, they will produce crash (have no body in raws)!

*Note: Pets may be **expensive**.* Which is why you set \[PETVALUE:1\]

### Non-Threatening Webs

Web-firing enemies (giant cave spiders, some forgotten beasts, titans and other super-fun things) are some of the most overpowered creatures in the game, able to easily tear an entire steel-clad militia apart no matter how well trained they might be. If you think that's not fair, add the \[WEBIMMUNE\] token to the dwarf creature's raws, which will make them unaffected by web attacks.

### Tinkering with the Dwarven Soul

By messing with the soul of a dwarf, you can drastically increase attributes and learning rates. Below are notes and a copy-paste section of text that you can use in the creature_standard.txt file, in which you replace the existing dwarf attributes. Some of these tags *must* be placed in the section where castes are defined (ex: to speed learning rates, place the tags under the \[CASTE:MALE\] and \[CASTE:FEMALE\] tags) Using the castes, it is very possible to specify what parts of your society get what (ex: adding a 'prodigy' caste of dwarves that learn 5 times faster than regular dwarves). The most easily adjustable portion of the castes is with the males and females.

ATT_RANGE dictates the level of effectiveness a being receives in an ability: 5,000 is the max. Please note that the elves get "5,000" in the memory stat, for the entire range. Humans get a default of 1,000, and presumably the same goes for any other creature that doesn't have a specified range.

Below, the ATT_RATES tag basically determines how quickly you gain and lose an attribute. The first value indicates cost - the lower it is, the better. The other values are for dictating the rate of decay, so keeping them at "NONE" basically nullifies that aspect. Don't use "0" for the first value, it crashes the game. Default for the first value is 500. If there is no number, the default will be used. It is believed that you can use negative numbers (negative numbers DO NOT increase the speed of rate, tested for Splinterz Dwarf Therapist that uses CTI, set CTI to -5000, -300, -100, the count kept increasing well past 1500, but no increase in attribute), which further increases the gain of attributes, since the ceiling to the next attribute level is lowered by the negative percentage you use.

ATT_RATES (Default is 500:2:3:2\]

- ATTRIBUTE Token
- cost to improve
- unused counter rate
- rust counter rate
- demotion counter rate

\[PHYS_ATT_RATES:STRENGTH:-5000:NONE:NONE:NONE\]

The game comes pre-stocked with several sets of attribute ranges, some better than others. The signs that come after the numeral ranges indicate what level that range represents, but have no effect in and of themselves.

`0:0:0:0:0:0:0                       unattainable`\
`0:100:200:300:400:450:500           ---`\
`0:400:600:750:800:900:1100           --`\
`150:600:800:900:1000:1100:1500        -`\
`450:950:1150:1250:1350:1550:2250      +`\
`700:1200:1400:1500:1600:1800:2500    ++`\
`1250:1500:1750:2000:2500:3000:5000  +++`\
`5000:5000:5000:5000:5000:5000:5000  max`

SKILL_RATE is a tag that grants you a % of skill improvement. The first number is the percentage, while the last three slots indicate decay. Skill rate increase is capped at 500%. Default is 100%, but creatures with the SLOW_LEARNER tag will get half of that.

SKILL_RATE (Default is 100:8:16:16\]

- % of improvement points you get
- unused counter rate
- rust counter rate
- demotion counter rate

Add this line under whichever castes you wish to receive the benefits.

`[SKILL_RATES:500:NONE:NONE:NONE]`

PHYS_ATT_CAP_PERC MENT_ATT_CAP_PERC

The default value is 200% of a dwarf's median+starting stats. This tag caps the amount of improvement to be had in an attribute. Below, I have cranked it up to 5,000%, hoping that it would let all dwarves achieve maximum attributes.

e.g.

`[PHYS_ATT_CAP_PERC:STRENGTH:5000]`\
`[MENT_ATT_CAP_PERC:FOCUS:5000]`

`     [SKILL_RATES:5000:NONE:NONE:NONE]`\
`     [PHYS_ATT_RANGE:STRENGTH:1250:1500:1750:2000:2500:3000:5000]           +++     `\
`     [PHYS_ATT_RATES:STRENGTH:-5000:NONE:NONE:NONE]`\
`     [PHYS_ATT_CAP_PERC:STRENGTH:5000:NONE:NONE:NONE]`\
`     [PHYS_ATT_RANGE:TOUGHNESS:1250:1500:1750:2000:2500:3000:5000]           +++`\
`     [PHYS_ATT_RATES:TOUGHNESS:-5000:NONE:NONE:NONE]`\
`     [PHYS_ATT_CAP_PERC:TOUGHNESS:5000:NONE:NONE:NONE]`\
`     [PHYS_ATT_RANGE:AGILITY:1250:1500:1750:2000:2500:3000:5000]           +++`\
`     [PHYS_ATT_RATES:AGILITY:-5000:NONE:NONE:NONE]`\
`     [PHYS_ATT_CAP_PERC:AGILITY:5000:NONE:NONE:NONE]`\
`     [PHYS_ATT_RANGE:ENDURANCE:1250:1500:1750:2000:2500:3000:5000]           +++`\
`     [PHYS_ATT_RATES:ENDURANCE:-5000:NONE:NONE:NONE]`\
`     [PHYS_ATT_CAP_PERC:ENDURANCE:5000]`\
`     [PHYS_ATT_RANGE:RECUPERATION:1250:1500:1750:2000:2500:3000:5000]        +++       `\
`     [PHYS_ATT_RATES:RECUPERATION:-5000:NONE:NONE:NONE]`\
`     [PHYS_ATT_CAP_PERC:RECUPERATION:5000]`\
`     [PHYS_ATT_RANGE:DISEASE_RESISTANCE:1250:1500:1750:2000:2500:3000:5000]  +++`\
`     [PHYS_ATT_RATES:DISEASE_RESISTANCE:-5000:NONE:NONE:NONE]`\
`     [PHYS_ATT_CAP_PERC:DISEASE_RESISTANCE:5000]`\
`     [MENT_ATT_RANGE:FOCUS:1250:1500:1750:2000:2500:3000:5000]              +++             `\
`     [MENT_ATT_RATES:FOCUS:-5000:NONE:NONE:NONE]`\
`     [MENT_ATT_CAP_PERC:FOCUS:5000]`\
`     [MENT_ATT_RANGE:CREATIVITY:1250:1500:1750:2000:2500:3000:5000]        +++         `\
`     [MENT_ATT_RATES:CREATIVITY:-5000:NONE:NONE:NONE]`\
`     [MENT_ATT_CAP_PERC:CREATIVITY:5000]`\
`     [MENT_ATT_RANGE:PATIENCE:1250:1500:1750:2000:2500:3000:5000]           +++     `\
`     [MENT_ATT_RATES:PATIENCE:-5000:NONE:NONE:NONE]`\
`     [MENT_ATT_CAP_PERC:PATIENCE:5000]`\
`     [MENT_ATT_RANGE:MEMORY:1250:1500:1750:2000:2500:3000:5000]           +++             `\
`     [MENT_ATT_RATES:MEMORY:-5000:NONE:NONE:NONE]`\
`     [MENT_ATT_CAP_PERC:MEMORY:5000]`\
`     [MENT_ATT_RANGE:SPATIAL_SENSE:1250:1500:1750:2000:2500:3000:5000]        +++`\
`     [MENT_ATT_RATES:SPATIAL_SENSE:-5000:NONE:NONE:NONE]`\
`     [MENT_ATT_CAP_PERC:SPATIAL_SENSE:5000]`\
`     [MENT_ATT_RANGE:EMPATHY:1250:1500:1750:2000:2500:3000:5000]           +++`\
`     [MENT_ATT_RATES:EMPATHY:-5000:NONE:NONE:NONE]`\
`     [MENT_ATT_CAP_PERC:EMPATHY:5000]`\
`     [MENT_ATT_RANGE:MUSICALITY:1250:1500:1750:2000:2500:3000:5000]        +++`\
`     [MENT_ATT_RATES:MUSICALITY:-5000:NONE:NONE:NONE]`\
`     [MENT_ATT_CAP_PERC:MUSICALITY:5000]`\
`     [MENT_ATT_RANGE:ANALYTICAL_ABILITY:1250:1500:1750:2000:2500:3000:5000]  +++`\
`     [MENT_ATT_RATES:ANALYTICAL_ABILITY:-5000:NONE:NONE:NONE]`\
`     [MENT_ATT_CAP_PERC:ANALYTICAL_ABILITY:5000]`\
`     [MENT_ATT_RANGE:LINGUISTIC_ABILITY:1250:1500:1750:2000:2500:3000:5000]  +++`\
`     [MENT_ATT_RATES:LINGUISTIC_ABILITY:-5000:NONE:NONE:NONE]`\
`     [MENT_ATT_CAP_PERC:LINGUISTIC_ABILITY:5000]`\
`     [MENT_ATT_RANGE:INTUITION:1250:1500:1750:2000:2500:3000:5000]           +++`\
`     [MENT_ATT_RATES:INTUITION:-5000:NONE:NONE:NONE]`\
`     [MENT_ATT_CAP_PERC:INTUITION:5000]`\
`     [MENT_ATT_RANGE:WILLPOWER:1250:1500:1750:2000:2500:3000:5000]           +++`\
`     [MENT_ATT_RATES:WILLPOWER:-5000:NONE:NONE:NONE]`\
`     [MENT_ATT_CAP_PERC:WILLPOWER:5000]`\
`     [MENT_ATT_RANGE:SOCIAL_AWARENESS:1250:1500:1750:2000:2500:3000:5000]     +++`\
`     [MENT_ATT_RATES:SOCIAL_AWARENESS:-5000:NONE:NONE:NONE]`\
`     [MENT_ATT_CAP_PERC:SOCIAL_AWARENESS:5000]`\
`     [MENT_ATT_RANGE:KINESTHETIC_SENSE:1250:1500:1750:2000:2500:3000:5000]     +++`\
`     [MENT_ATT_RATES:KINESTHETIC_SENSE:-5000:NONE:NONE:NONE]`\
`     [MENT_ATT_CAP_PERC:KINESTHETIC_SENSE:5000]`

### No more skill loss

Are you tired of your dwarves having red stats after a few years? If so, try adding this mod by LordSnow to df_folder/data/save/region/raw/objects/creature_standard.txt in the "dwarf" section.

Phys/Ment rate default: 500

`  [PHYS_ATT_RATES:STRENGTH:50:NONE:NONE:NONE]`\
`  [PHYS_ATT_RATES:AGILITY:50:NONE:NONE:NONE]`\
`  [PHYS_ATT_RATES:TOUGHNESS:50:NONE:NONE:NONE]`\
`  [PHYS_ATT_RATES:ENDURANCE:50:NONE:NONE:NONE]`\
`  [PHYS_ATT_RATES:DISEASE_RESISTANCE:50:NONE:NONE:NONE]`\
`  [PHYS_ATT_RATES:RECUPERATION:50:NONE:NONE:NONE]`

`  [MENT_ATT_RATES:ANALYTICAL_ABILITY:50:NONE:NONE:NONE]`\
`  [MENT_ATT_RATES:CREATIVITY:50:NONE:NONE:NONE]`\
`  [MENT_ATT_RATES:EMPATHY:50:NONE:NONE:NONE]`\
`  [MENT_ATT_RATES:FOCUS:50:NONE:NONE:NONE]`\
`  [MENT_ATT_RATES:INTUITION:50:NONE:NONE:NONE]`\
`  [MENT_ATT_RATES:KINESTHETIC_SENSE:50:NONE:NONE:NONE]`\
`  [MENT_ATT_RATES:LINGUISTIC_ABILITY:50:NONE:NONE:NONE]`\
`  [MENT_ATT_RATES:MUSICALITY:50:NONE:NONE:NONE]`\
`  [MENT_ATT_RATES:PATIENCE:50:NONE:NONE:NONE]`\
`  [MENT_ATT_RATES:SOCIAL_AWARENESS:50:NONE:NONE:NONE]`\
`  [MENT_ATT_RATES:MEMORY:50:NONE:NONE:NONE]`\
`  [MENT_ATT_RATES:SPATIAL_SENSE:50:NONE:NONE:NONE]`\
`  [MENT_ATT_RATES:WILLPOWER:50:NONE:NONE:NONE]`

### Enemy race dies in a pink cloud

Causes all creatures of a type to go \*poof\* in a little pink cloud. Put this under the creature you want to never appear again. Goodbye invasions!

`[SELECT_MATERIAL:ALL]`\
`     [BOILING_POINT:0]`\
`     [STATE_COLOR:ALL:PINK]`\
`     [STATE_NAME_ADJ:GAS:poof!]`

Warning: As with all cheats that involve the words "\[BOILING_POINT:0\]", the mist created when the creature boils will be very cold. Such cold temperatures will rapidly degrade weak items like cloth and leather, and may pose a danger to dwarves caught in the cloud without adequate cold weather clothing. You might have to experiment to find a temperature that will guarantee boiling without posing a danger to your dwarves.

Note: You must add this text after all the material you want to boil is defined. To be safe, just place it at the very end.

### All Skills Legendary

Put this under CREATURE:DWARF in creature_standard.txt

        [NATURAL_SKILL:MINING:16]
        [NATURAL_SKILL:WOODCUTTING:16]
        [NATURAL_SKILL:CARPENTRY:16]
        [NATURAL_SKILL:DETAILSTONE:16]
        [NATURAL_SKILL:MASONRY:16]
        [NATURAL_SKILL:ANIMALTRAIN:16]
        [NATURAL_SKILL:ANIMALCARE:16]
        [NATURAL_SKILL:DISSECT_FISH:16]
        [NATURAL_SKILL:DISSECT_VERMIN:16]
        [NATURAL_SKILL:PROCESSFISH:16]
        [NATURAL_SKILL:BUTCHER:16]
        [NATURAL_SKILL:TRAPPING:16]
        [NATURAL_SKILL:TANNER:16]
        [NATURAL_SKILL:WEAVING:16]
        [NATURAL_SKILL:BREWING:16]
        [NATURAL_SKILL:ALCHEMY:16]
        [NATURAL_SKILL:CLOTHESMAKING:16]
        [NATURAL_SKILL:MILLING:16]
        [NATURAL_SKILL:PROCESSPLANTS:16]
        [NATURAL_SKILL:CHEESEMAKING:16]
        [NATURAL_SKILL:MILK:16]
        [NATURAL_SKILL:COOK:16]
        [NATURAL_SKILL:PLANT:16]
        [NATURAL_SKILL:HERBALISM:16]
        [NATURAL_SKILL:FISH:16]
        [NATURAL_SKILL:SMELT:16]
        [NATURAL_SKILL:EXTRACT_STRAND:16]
        [NATURAL_SKILL:FORGE_WEAPON:16]
        [NATURAL_SKILL:FORGE_ARMOR:16]
        [NATURAL_SKILL:FORGE_FURNITURE:16]
        [NATURAL_SKILL:CUTGEM:16]
        [NATURAL_SKILL:ENCRUSTGEM:16]
        [NATURAL_SKILL:WOODCRAFT:16]
        [NATURAL_SKILL:STONECRAFT:16]
        [NATURAL_SKILL:METALCRAFT:16]
        [NATURAL_SKILL:GLASSMAKER:16]
        [NATURAL_SKILL:LEATHERWORK:16]
        [NATURAL_SKILL:BONECARVE:16]
        [NATURAL_SKILL:AXE:16]
        [NATURAL_SKILL:SWORD:16]
        [NATURAL_SKILL:DAGGER:16]
        [NATURAL_SKILL:MACE:16]
        [NATURAL_SKILL:HAMMER:16]
        [NATURAL_SKILL:SPEAR:16]
        [NATURAL_SKILL:CROSSBOW:16]
        [NATURAL_SKILL:SHIELD:16]
        [NATURAL_SKILL:ARMOR:16]
        [NATURAL_SKILL:SIEGECRAFT:16]
        [NATURAL_SKILL:SIEGEOPERATE:16]
        [NATURAL_SKILL:BOWYER:16]
        [NATURAL_SKILL:PIKE:16]
        [NATURAL_SKILL:WHIP:16]
        [NATURAL_SKILL:BOW:16]
        [NATURAL_SKILL:BLOWGUN:16]
        [NATURAL_SKILL:THROW:16]
        [NATURAL_SKILL:MECHANICS:16]
        [NATURAL_SKILL:MAGIC_NATURE:16]
        [NATURAL_SKILL:SNEAK:16]
        [NATURAL_SKILL:DESIGNBUILDING:16]
        [NATURAL_SKILL:DRESS_WOUNDS:16]
        [NATURAL_SKILL:DIAGNOSE:16]
        [NATURAL_SKILL:SURGERY:16]
        [NATURAL_SKILL:SET_BONE:16]
        [NATURAL_SKILL:SUTURE:16]
        [NATURAL_SKILL:CRUTCH_WALK:16]
        [NATURAL_SKILL:WOOD_BURNING:16]
        [NATURAL_SKILL:LYE_MAKING:16]
        [NATURAL_SKILL:SOAP_MAKING:16]
        [NATURAL_SKILL:POTASH_MAKING:16]
        [NATURAL_SKILL:DYER:16]
        [NATURAL_SKILL:OPERATE_PUMP:16]
        [NATURAL_SKILL:SWIMMING:16]
        [NATURAL_SKILL:PERSUASION:16]
        [NATURAL_SKILL:NEGOTIATION:16]
        [NATURAL_SKILL:JUDGING_INTENT:16]
        [NATURAL_SKILL:APPRAISAL:16]
        [NATURAL_SKILL:ORGANIZATION:16]
        [NATURAL_SKILL:RECORD_KEEPING:16]
        [NATURAL_SKILL:LYING:16]
        [NATURAL_SKILL:INTIMIDATION:16]
        [NATURAL_SKILL:CONVERSATION:16]
        [NATURAL_SKILL:COMEDY:16]
        [NATURAL_SKILL:FLATTERY:16]
        [NATURAL_SKILL:CONSOLE:16]
        [NATURAL_SKILL:PACIFY:16]
        [NATURAL_SKILL:TRACKING:16]
        [NATURAL_SKILL:KNOWLEDGE_ACQUISITION:16]
        [NATURAL_SKILL:CONCENTRATION:16]
        [NATURAL_SKILL:DISCIPLINE:16]
        [NATURAL_SKILL:SITUATIONAL_AWARENESS:16]
        [NATURAL_SKILL:WRITING:16]
        [NATURAL_SKILL:PROSE:16]
        [NATURAL_SKILL:POETRY:16]
        [NATURAL_SKILL:READING:16]
        [NATURAL_SKILL:SPEAKING:16]
        [NATURAL_SKILL:COORDINATION:16]
        [NATURAL_SKILL:BALANCE:16]
        [NATURAL_SKILL:LEADERSHIP:16]
        [NATURAL_SKILL:TEACHING:16]
        [NATURAL_SKILL:MELEE_COMBAT:16]
        [NATURAL_SKILL:RANGED_COMBAT:16]
        [NATURAL_SKILL:WRESTLING:16]
        [NATURAL_SKILL:BITE:16]
        [NATURAL_SKILL:GRASP_STRIKE:16]
        [NATURAL_SKILL:STANCE_STRIKE:16]
        [NATURAL_SKILL:DODGING:16]
        [NATURAL_SKILL:MISC_WEAPON:16]
        [NATURAL_SKILL:KNAPPING:16]
        [NATURAL_SKILL:MILITARY_TACTICS:16]
        [NATURAL_SKILL:SHEARING:16]
        [NATURAL_SKILL:SPINNING:16]
        [NATURAL_SKILL:POTTERY:16]
        [NATURAL_SKILL:GLAZING:16]
        [NATURAL_SKILL:PRESSING:16]
        [NATURAL_SKILL:BEEKEEPING:16]
        [NATURAL_SKILL:WAX_WORKING:16]

### Syndrome Immunity

Generated syndromes act on creatures with the token \[CREATURE_CLASS:GENERAL_POISON\]. If this token is not in a creature's entry, then it is not a valid target for generated syndromes.

To make a creature immune, remove \[CREATURE_CLASS:GENERAL_POISON\].

### Child Labor

Tired of having children spend 12 years drinking your booze and eating your food without performing any work? Simply open creature_standard.txt, and under the dwarf entry replace \[CHILD:12\] with \[CHILD:6\], or whatever age you consider it appropriate for children to start working at.

## Reaction Additions

There are now two reaction files: reaction_smelter and reaction_other. Additions to these lists will not take effect until you generate a new world. Note that if you edit an existing reaction entry (leaving the \[REACTION:NAME\] line unchanged) rather than add a new one, you will not need to generate a new world. Don't forget to add \[PERMITTED_REACTION:(reaction)\] under \[ENTITY:MOUNTAIN\] in entity_default raw.

### Skill Practice Workshops

A useful application of the new workshop/reaction setup is the Practice Workshop: loaded with no-reagent no-product reactions tied to every quality-based skill, it's an excellent way to get the most out of scarce resources and to train workers who utilize said resources (Jewelers, Craftsdwarves, etc.).

Create a new raw called building_practice_workshop in \raw\objects, and within it paste the following (ripped nigh-straight out of Lazureus' Crematorium package):

    building_practice_workshop

    [OBJECT:BUILDING]

    [BUILDING_WORKSHOP:PRACTICE_WORKSHOP]
        [NAME:Practice Workshop]
        [NAME_COLOR:7:0:1]
        [DIM:3:3]
        [WORK_LOCATION:2:3]
        [BUILD_LABOR:MASON]
        [BUILD_KEY:CUSTOM_SHIFT_P]
        [BLOCK:1:0:0:0]
        [BLOCK:2:0:0:0]
        [BLOCK:3:0:0:0]
        [TILE:0:1:' ':' ':236]
        [TILE:0:2:' ':236:'/']
        [TILE:0:3:'|':' ':' ']
        [COLOR:0:1:0:0:0:0:0:0:0:0:1]
        [COLOR:0:2:0:0:0:0:0:1:6:0:0]
        [COLOR:0:3:6:0:0:0:0:0:0:0:0]
        [TILE:1:1:236:' ':227]
        [TILE:1:2:'|':' ':8]
        [TILE:1:3:' ':' ':236]
        [COLOR:1:1:0:0:1:0:0:0:0:0:1]
        [COLOR:1:2:6:0:0:0:0:0:0:0:1]
        [COLOR:1:3:0:0:0:0:0:0:0:0:1]
        [TILE:2:1:201:227:187]
        [TILE:2:2:200:8:188]
        [TILE:2:3:' ':' ':' ']
        [COLOR:2:1:0:0:1:0:0:1:0:0:1]
        [COLOR:2:2:0:0:1:0:0:1:0:0:1]
        [COLOR:2:3:0:0:0:0:0:0:0:0:0]
        [TILE:3:1:201:227:187]
        [TILE:3:2:200:8:188]
        [TILE:3:3:150:210:253]
        [COLOR:3:1:0:0:1:0:0:1:0:0:1]
        [COLOR:3:2:0:0:1:0:4:1:0:0:1]
        [COLOR:3:3:0:0:1:6:0:0:7:0:1]
        [BUILD_ITEM:1:NONE:NONE:NONE:NONE][BUILDMAT][WORTHLESS_STONE_ONLY][CAN_USE_ARTIFACT]

Create a new raw called reaction_practice_workshop, and within it paste the following: (Fixed the process to only accept bars of coke instead of just ANY bar. Enjoy. -Anonymous)

    reaction_practice_workshop

    [OBJECT:REACTION]

    [REACTION:PRACTICE_ARMORSMITHING]
    [NAME:practice armorsmithing]
    [BUILDING:PRACTICE_WORKSHOP:NONE]
    [REAGENT:A:150:BAR:NO_SUBTYPE:COAL:COKE]
    [PRODUCT:100:1:BAR:NO_SUBTYPE:COAL:COKE][PRODUCT_DIMENSION:150]
    [SKILL:FORGE_ARMOR]

    [REACTION:PRACTICE_BEEKEEPING]
    [NAME:practice beekeeping]
    [BUILDING:PRACTICE_WORKSHOP:NONE]
    [REAGENT:A:150:BAR:NO_SUBTYPE:COAL:COKE]
    [PRODUCT:100:1:BAR:NO_SUBTYPE:COAL:COKE][PRODUCT_DIMENSION:150]
    [SKILL:BEEKEEPING]

    [REACTION:PRACTICE_BONECARVING]
    [NAME:practice bonecarving]
    [BUILDING:PRACTICE_WORKSHOP:NONE]
    [REAGENT:A:150:BAR:NO_SUBTYPE:COAL:COKE]
    [PRODUCT:100:1:BAR:NO_SUBTYPE:COAL:COKE][PRODUCT_DIMENSION:150]
    [SKILL:BONECARVE]

    [REACTION:PRACTICE_BONESETTING]
    [NAME:practice bonesetting]
    [BUILDING:PRACTICE_WORKSHOP:NONE]
    [REAGENT:A:150:BAR:NO_SUBTYPE:COAL:COKE]
    [PRODUCT:100:1:BAR:NO_SUBTYPE:COAL:COKE][PRODUCT_DIMENSION:150]
    [SKILL:SET_BONE]

    [REACTION:PRACTICE_BOWMAKING]
    [NAME:practice bowmaking]
    [BUILDING:PRACTICE_WORKSHOP:NONE]
    [REAGENT:A:150:BAR:NO_SUBTYPE:COAL:COKE]
    [PRODUCT:100:1:BAR:NO_SUBTYPE:COAL:COKE][PRODUCT_DIMENSION:150]
    [SKILL:BOWYER]

    [REACTION:PRACTICE_BREWING]
    [NAME:practice brewing]
    [BUILDING:PRACTICE_WORKSHOP:NONE]
    [REAGENT:A:150:BAR:NO_SUBTYPE:COAL:COKE]
    [PRODUCT:100:1:BAR:NO_SUBTYPE:COAL:COKE][PRODUCT_DIMENSION:150]
    [SKILL:BREWING]

    [REACTION:PRACTICE_CARPENTRY]
    [NAME:practice carpentry]
    [BUILDING:PRACTICE_WORKSHOP:NONE]
    [REAGENT:A:150:BAR:NO_SUBTYPE:COAL:COKE]
    [PRODUCT:100:1:BAR:NO_SUBTYPE:COAL:COKE][PRODUCT_DIMENSION:150]
    [SKILL:CARPENTRY]

    [REACTION:PRACTICE_CLOTHESMAKING]
    [NAME:practice clothesmaking]
    [BUILDING:PRACTICE_WORKSHOP:NONE]
    [REAGENT:A:150:BAR:NO_SUBTYPE:COAL:COKE]
    [PRODUCT:100:1:BAR:NO_SUBTYPE:COAL:COKE][PRODUCT_DIMENSION:150]
    [SKILL:CLOTHESMAKING]

    [REACTION:PRACTICE_COOKING]
    [NAME:practice cooking]
    [BUILDING:PRACTICE_WORKSHOP:NONE]
    [REAGENT:A:150:BAR:NO_SUBTYPE:COAL:COKE]
    [PRODUCT:100:1:BAR:NO_SUBTYPE:COAL:COKE][PRODUCT_DIMENSION:150]
    [SKILL:COOK]

    [REACTION:PRACTICE_DESIGNBUILDING]
    [NAME:practice architecture]
    [BUILDING:PRACTICE_WORKSHOP:NONE]
    [REAGENT:A:150:BAR:NO_SUBTYPE:COAL:COKE]
    [PRODUCT:100:1:BAR:NO_SUBTYPE:COAL:COKE][PRODUCT_DIMENSION:150]
    [SKILL:DESIGNBUILDING]

    [REACTION:PRACTICE_DIAGNOSIS]
    [NAME:practice diagnosis]
    [BUILDING:PRACTICE_WORKSHOP:NONE]
    [REAGENT:A:150:BAR:NO_SUBTYPE:COAL:COKE]
    [PRODUCT:100:1:BAR:NO_SUBTYPE:COAL:COKE][PRODUCT_DIMENSION:150]
    [SKILL:DIAGNOSE]

    [REACTION:PRACTICE_DYEING]
    [NAME:practice dyeing]
    [BUILDING:PRACTICE_WORKSHOP:NONE]
    [REAGENT:A:150:BAR:NO_SUBTYPE:COAL:COKE]
    [PRODUCT:100:1:BAR:NO_SUBTYPE:COAL:COKE][PRODUCT_DIMENSION:150]
    [SKILL:DYER]

    [REACTION:PRACTICE_ENGRAVING]
    [NAME:practice engraving]
    [BUILDING:PRACTICE_WORKSHOP:NONE]
    [REAGENT:A:150:BAR:NO_SUBTYPE:COAL:COKE]
    [PRODUCT:100:1:BAR:NO_SUBTYPE:COAL:COKE][PRODUCT_DIMENSION:150]
    [SKILL:DETAILSTONE]

    [REACTION:PRACTICE_GEM_CUTTING]
    [NAME:practice gem cutting]
    [BUILDING:PRACTICE_WORKSHOP:NONE]
    [REAGENT:A:150:BAR:NO_SUBTYPE:COAL:COKE]
    [PRODUCT:100:1:BAR:NO_SUBTYPE:COAL:COKE][PRODUCT_DIMENSION:150]
    [SKILL:CUTGEM]

    [REACTION:PRACTICE_GEM_SETTING]
    [NAME:practice gem setting]
    [BUILDING:PRACTICE_WORKSHOP:NONE]
    [REAGENT:A:150:BAR:NO_SUBTYPE:COAL:COKE]
    [PRODUCT:100:1:BAR:NO_SUBTYPE:COAL:COKE][PRODUCT_DIMENSION:150]
    [SKILL:ENCRUSTGEM]

    [REACTION:PRACTICE_GLASSMAKING]
    [NAME:practice glassmaking]
    [BUILDING:PRACTICE_WORKSHOP:NONE]
    [REAGENT:A:150:BAR:NO_SUBTYPE:COAL:COKE]
    [PRODUCT:100:1:BAR:NO_SUBTYPE:COAL:COKE][PRODUCT_DIMENSION:150]
    [SKILL:GLASSMAKER]

    [REACTION:PRACTICE_GLAZING]
    [NAME:practice glazing]
    [BUILDING:PRACTICE_WORKSHOP:NONE]
    [REAGENT:A:150:BAR:NO_SUBTYPE:COAL:COKE]
    [PRODUCT:100:1:BAR:NO_SUBTYPE:COAL:COKE][PRODUCT_DIMENSION:150]
    [SKILL:GLAZING]

    [REACTION:PRACTICE_GROWING]
    [NAME:practice growing]
    [BUILDING:PRACTICE_WORKSHOP:NONE]
    [REAGENT:A:150:BAR:NO_SUBTYPE:COAL:COKE]
    [PRODUCT:100:1:BAR:NO_SUBTYPE:COAL:COKE][PRODUCT_DIMENSION:150]
    [SKILL:PLANT]

    [REACTION:PRACTICE_HERBALISM]
    [NAME:practice herbalism]
    [BUILDING:PRACTICE_WORKSHOP:NONE]
    [REAGENT:A:150:BAR:NO_SUBTYPE:COAL:COKE]
    [PRODUCT:100:1:BAR:NO_SUBTYPE:COAL:COKE][PRODUCT_DIMENSION:150]
    [SKILL:HERBALISM]

    [REACTION:PRACTICE_LEATHERWORKING]
    [NAME:practice leatherworking]
    [BUILDING:PRACTICE_WORKSHOP:NONE]
    [REAGENT:A:150:BAR:NO_SUBTYPE:COAL:COKE]
    [PRODUCT:100:1:BAR:NO_SUBTYPE:COAL:COKE][PRODUCT_DIMENSION:150]
    [SKILL:LEATHERWORK]

    [REACTION:PRACTICE_MASONRY]
    [NAME:practice masonry]
    [BUILDING:PRACTICE_WORKSHOP:NONE]
    [REAGENT:A:150:BAR:NO_SUBTYPE:COAL:COKE]
    [PRODUCT:100:1:BAR:NO_SUBTYPE:COAL:COKE][PRODUCT_DIMENSION:150]
    [SKILL:MASONRY]

    [REACTION:PRACTICE_MECHANICS]
    [NAME:practice mechanics]
    [BUILDING:PRACTICE_WORKSHOP:NONE]
    [REAGENT:A:150:BAR:NO_SUBTYPE:COAL:COKE]
    [PRODUCT:100:1:BAR:NO_SUBTYPE:COAL:COKE][PRODUCT_DIMENSION:150]
    [SKILL:MECHANICS]

    [REACTION:PRACTICE_METALCRAFTING]
    [NAME:practice metalcrafting]
    [BUILDING:PRACTICE_WORKSHOP:NONE]
    [REAGENT:A:150:BAR:NO_SUBTYPE:COAL:COKE]
    [PRODUCT:100:1:BAR:NO_SUBTYPE:COAL:COKE][PRODUCT_DIMENSION:150]
    [SKILL:METALCRAFT]

    [REACTION:PRACTICE_METALSMITHING]
    [NAME:practice metalsmithing]
    [BUILDING:PRACTICE_WORKSHOP:NONE]
    [REAGENT:A:150:BAR:NO_SUBTYPE:COAL:COKE]
    [PRODUCT:100:1:BAR:NO_SUBTYPE:COAL:COKE][PRODUCT_DIMENSION:150]
    [SKILL:FORGE_FURNITURE]

    [REACTION:PRACTICE_MINING]
    [NAME:practice mining]
    [BUILDING:PRACTICE_WORKSHOP:NONE]
    [REAGENT:A:150:BAR:NO_SUBTYPE:COAL:COKE]
    [PRODUCT:100:1:BAR:NO_SUBTYPE:COAL:COKE][PRODUCT_DIMENSION:150]
    [SKILL:MINING]

    [REACTION:PRACTICE_POTTERY]
    [NAME:practice pottery]
    [BUILDING:PRACTICE_WORKSHOP:NONE]
    [REAGENT:A:150:BAR:NO_SUBTYPE:COAL:COKE]
    [PRODUCT:100:1:BAR:NO_SUBTYPE:COAL:COKE][PRODUCT_DIMENSION:150]
    [SKILL:POTTERY]

    [REACTION:PRACTICE_SIEGE_ENGINEERING]
    [NAME:practice siege engineering]
    [BUILDING:PRACTICE_WORKSHOP:NONE]
    [REAGENT:A:150:BAR:NO_SUBTYPE:COAL:COKE]
    [PRODUCT:100:1:BAR:NO_SUBTYPE:COAL:COKE][PRODUCT_DIMENSION:150]
    [SKILL:SIEGECRAFT]

    [REACTION:PRACTICE_STONECRAFTING]
    [NAME:practice stonecrafting]
    [BUILDING:PRACTICE_WORKSHOP:NONE]
    [REAGENT:A:150:BAR:NO_SUBTYPE:COAL:COKE]
    [PRODUCT:100:1:BAR:NO_SUBTYPE:COAL:COKE][PRODUCT_DIMENSION:150]
    [SKILL:STONECRAFT]

    [REACTION:PRACTICE_SURGERY]
    [NAME:practice surgery]
    [BUILDING:PRACTICE_WORKSHOP:NONE]
    [REAGENT:A:150:BAR:NO_SUBTYPE:COAL:COKE]
    [PRODUCT:100:1:BAR:NO_SUBTYPE:COAL:COKE][PRODUCT_DIMENSION:150]
    [SKILL:SURGERY]

    [REACTION:PRACTICE_SUTURING]
    [NAME:practice suturing]
    [BUILDING:PRACTICE_WORKSHOP:NONE]
    [REAGENT:A:150:BAR:NO_SUBTYPE:COAL:COKE]
    [PRODUCT:100:1:BAR:NO_SUBTYPE:COAL:COKE][PRODUCT_DIMENSION:150]
    [SKILL:SUTURE]

    [REACTION:PRACTICE_WAX_WORKING]
    [NAME:practice wax working]
    [BUILDING:PRACTICE_WORKSHOP:NONE]
    [REAGENT:A:150:BAR:NO_SUBTYPE:COAL:COKE]
    [PRODUCT:100:1:BAR:NO_SUBTYPE:COAL:COKE][PRODUCT_DIMENSION:150]
    [SKILL:WAX_WORKING]

    [REACTION:PRACTICE_WEAPONSMITHING]
    [NAME:practice weaponsmithing]
    [BUILDING:PRACTICE_WORKSHOP:NONE]
    [REAGENT:A:150:BAR:NO_SUBTYPE:COAL:COKE]
    [PRODUCT:100:1:BAR:NO_SUBTYPE:COAL:COKE][PRODUCT_DIMENSION:150]
    [SKILL:FORGE_WEAPON]

    [REACTION:PRACTICE_WEAVING]
    [NAME:practice weaving]
    [BUILDING:PRACTICE_WORKSHOP:NONE]
    [REAGENT:A:150:BAR:NO_SUBTYPE:COAL:COKE]
    [PRODUCT:100:1:BAR:NO_SUBTYPE:COAL:COKE][PRODUCT_DIMENSION:150]
    [SKILL:WEAVING]

    [REACTION:PRACTICE_WOODCRAFTING]
    [NAME:practice woodcrafting]
    [BUILDING:PRACTICE_WORKSHOP:NONE]
    [REAGENT:A:150:BAR:NO_SUBTYPE:COAL:COKE]
    [PRODUCT:100:1:BAR:NO_SUBTYPE:COAL:COKE][PRODUCT_DIMENSION:150]
    [SKILL:WOODCRAFT]

    [REACTION:PRACTICE_WOUND_DRESSING]
    [NAME:practice wound dressing]
    [BUILDING:PRACTICE_WORKSHOP:NONE]
    [REAGENT:A:150:BAR:NO_SUBTYPE:COAL:COKE]
    [PRODUCT:100:1:BAR:NO_SUBTYPE:COAL:COKE][PRODUCT_DIMENSION:150]
    [SKILL:DRESS_WOUNDS]

Lastly, paste the following to their respective spots in the dwarf section of entity_default, and you're done:

        [PERMITTED_BUILDING:PRACTICE_WORKSHOP]
        [PERMITTED_REACTION:PRACTICE_ARMORSMITHING]
        [PERMITTED_REACTION:PRACTICE_BEEKEEPING]
        [PERMITTED_REACTION:PRACTICE_BONECARVING]
        [PERMITTED_REACTION:PRACTICE_BONESETTING]
        [PERMITTED_REACTION:PRACTICE_BOWMAKING]
        [PERMITTED_REACTION:PRACTICE_BREWING]
        [PERMITTED_REACTION:PRACTICE_CARPENTRY]
        [PERMITTED_REACTION:PRACTICE_CLOTHESMAKING]
        [PERMITTED_REACTION:PRACTICE_DESIGNBUILDING]
        [PERMITTED_REACTION:PRACTICE_DIAGNOSIS]
        [PERMITTED_REACTION:PRACTICE_DYEING]
        [PERMITTED_REACTION:PRACTICE_ENGRAVING]
        [PERMITTED_REACTION:PRACTICE_GEM_CUTTING]
        [PERMITTED_REACTION:PRACTICE_GEM_SETTING]
        [PERMITTED_REACTION:PRACTICE_GLASSMAKING]
        [PERMITTED_REACTION:PRACTICE_GLAZING]
        [PERMITTED_REACTION:PRACTICE_GROWING]
        [PERMITTED_REACTION:PRACTICE_HERBALISM]
        [PERMITTED_REACTION:PRACTICE_LEATHERWORKING]
        [PERMITTED_REACTION:PRACTICE_MASONRY]
        [PERMITTED_REACTION:PRACTICE_MECHANICS]
        [PERMITTED_REACTION:PRACTICE_METALCRAFTING]
        [PERMITTED_REACTION:PRACTICE_METALSMITHING]
        [PERMITTED_REACTION:PRACTICE_MINING]
        [PERMITTED_REACTION:PRACTICE_POTTERY]
        [PERMITTED_REACTION:PRACTICE_SIEGE_ENGINEERING]
        [PERMITTED_REACTION:PRACTICE_SIEGE_OPERATION]
        [PERMITTED_REACTION:PRACTICE_STONECRAFTING]
        [PERMITTED_REACTION:PRACTICE_SURGERY]
        [PERMITTED_REACTION:PRACTICE_SUTURING]
        [PERMITTED_REACTION:PRACTICE_WAX_WORKING]
        [PERMITTED_REACTION:PRACTICE_WEAPONSMITHING]
        [PERMITTED_REACTION:PRACTICE_WEAVING]
        [PERMITTED_REACTION:PRACTICE_WOODCRAFTING]
        [PERMITTED_REACTION:PRACTICE_WOUND_DRESSING]

### Easy Vermin Disposal

Tired of vermin corpses lying around for months? Use this reaction to put them to a useful purpose:

    [REACTION:BUGS_TO_COKE]
       [NAME:Cremate Vermin Corpses]
       [BUILDING:SMELTER:NONE]
       [REAGENT:A:5:REMAINS:NONE:NONE:NONE]
       [PRODUCT:20:1:BAR:NO_SUBTYPE:COAL:COKE][PRODUCT_DIMENSION:150]
       [SKILL:SMELT]

Remember to add this to the appropriate entity files before generating a new world.

## Easy Entity Editing

Here is the edited entity_default raw entry. Just copy and paste everything underneath the existing entries. You may add more by using the format: \[PERMITTED_REACTION:(reaction)\]

            [PERMITTED_REACTION:FREE_DIAMOND_LY]
        [PERMITTED_REACTION:FREE_DIAMOND_FY]
        [PERMITTED_REACTION:FREE_EMERALD]
            [PERMITTED_REACTION:FREE_RUBY]
        [PERMITTED_REACTION:FREE_SAPPHIRE]
        [PERMITTED_REACTION:FREE_DIAMOND_CLEAR]
        [PERMITTED_REACTION:FREE_DIAMOND_RED]
        [PERMITTED_REACTION:FREE_DIAMOND_GREEN]
        [PERMITTED_REACTION:FREE_DIAMOND_BLUE]
        [PERMITTED_REACTION:FREE_DIAMOND_YELLOW]
        [PERMITTED_REACTION:FREE_DIAMOND_BLACK]
        [PERMITTED_REACTION:FREE_RUBY_STAR]
            [PERMITTED_REACTION:FREE_SAPPHIRE_STAR]
        [PERMITTED_REACTION:FREE_ADAMANTINE_THREAD]
        [PERMITTED_REACTION:FREE_ADAMANTINE_WAFERS]
        [PERMITTED_REACTION:FREE_WOOD]

### Free Gems

Fill in the name of a gem from the inorganic_stone_gem file and paste this in the reaction_smelter file to make your smelter spew out gems.

    [REACTION:FREE_(gem name here)]
    [NAME:make (gem name here)]
    [BUILDING:SMELTER:NONE]
    [PRODUCT:100:10:ROUGH:NO_SUBTYPE:INORGANIC:(gem name {from raws})]
    [SKILL:SMELT]

Note: You can change the skill used and the workshop, but make sure to keep it in the correct reaction file. For convenience, here are all the precious gems in the game.

    [REACTION:FREE_DIAMOND_LY]
    [NAME: make light yellow diamonds]
    [BUILDING:SMELTER:NONE]
    [PRODUCT:100:10:ROUGH:NO_SUBTYPE:INORGANIC:DIAMOND_LY]
    [SKILL:SMELT]

    [REACTION:FREE_DIAMOND_FY]
    [NAME: make faint yellow diamonds]
    [BUILDING:SMELTER:NONE]
    [PRODUCT:100:10:ROUGH:NO_SUBTYPE:INORGANIC:DIAMOND_FY]
    [SKILL:SMELT]

    [REACTION:FREE_EMERALD]
    [NAME: make emeralds]
    [BUILDING:SMELTER:NONE]
    [PRODUCT:100:10:ROUGH:NO_SUBTYPE:INORGANIC:EMERALD]
    [SKILL:SMELT]

    [REACTION:FREE_RUBY]
    [NAME: make rubies]
    [BUILDING:SMELTER:NONE]
    [PRODUCT:100:10:ROUGH:NO_SUBTYPE:INORGANIC:RUBY]
    [SKILL:SMELT]

    [REACTION:FREE_SAPPHIRE]
    [NAME: make sapphires]
    [BUILDING:SMELTER:NONE]
    [PRODUCT:100:10:ROUGH:NO_SUBTYPE:INORGANIC:SAPPHIRE]
    [SKILL:SMELT]

    [REACTION:FREE_DIAMOND_CLEAR]
    [NAME: make clear diamonds]
    [BUILDING:SMELTER:NONE]
    [PRODUCT:100:10:ROUGH:NO_SUBTYPE:INORGANIC:DIAMOND_CLEAR]
    [SKILL:SMELT]

    [REACTION:FREE_DIAMOND_RED]
    [NAME: make red diamonds]
    [BUILDING:SMELTER:NONE]
    [PRODUCT:100:10:ROUGH:NO_SUBTYPE:INORGANIC:DIAMOND_RED]
    [SKILL:SMELT]

    [REACTION:FREE_DIAMOND_GREEN]
    [NAME: make green diamond]
    [BUILDING:SMELTER:NONE]
    [PRODUCT:100:10:ROUGH:NO_SUBTYPE:INORGANIC:DIAMOND_GREEN]
    [SKILL:SMELT]

    [REACTION:FREE_DIAMOND_BLUE]
    [NAME: make blue diamonds]
    [BUILDING:SMELTER:NONE]
    [PRODUCT:100:10:ROUGH:NO_SUBTYPE:INORGANIC:DIAMOND_BLUE]
    [SKILL:SMELT]

    [REACTION:FREE_DIAMOND_YELLOW]
    [NAME: make yellow diamonds]
    [BUILDING:SMELTER:NONE]
    [PRODUCT:100:10:ROUGH:NO_SUBTYPE:INORGANIC:DIAMOND_YELLOW]
    [SKILL:SMELT]

    [REACTION:FREE_DIAMOND_BLACK]
    [NAME: make black diamonds]
    [BUILDING:SMELTER:NONE]
    [PRODUCT:100:10:ROUGH:NO_SUBTYPE:INORGANIC:DIAMOND_BLACK]
    [SKILL:SMELT]

    [REACTION:FREE_RUBY_STAR]
    [NAME: make star rubies]
    [BUILDING:SMELTER:NONE]
    [PRODUCT:100:10:ROUGH:NO_SUBTYPE:INORGANIC:RUBY_STAR]
    [SKILL:SMELT]

    [REACTION:FREE_SAPPHIRE_STAR]
    [NAME: make star sapphires]
    [BUILDING:SMELTER:NONE]
    [PRODUCT:100:10:ROUGH:NO_SUBTYPE:INORGANIC:SAPPHIRE_STAR]
    [SKILL:SMELT]

### Easy Adamantine

To get free adamantine wafers, add this to your reaction_smelter.

    [REACTION:FREE_ADAMANTINE_WAFERS]
    [NAME:create adamantine wafers]
    [BUILDING:SMELTER:NONE]
    [PRODUCT:100:10:BAR:NO_SUBTYPE:INORGANIC:ADAMANTINE][PRODUCT_DIMENSION:150]
    [SKILL:SMELT]

For adamantine thread it would be:

    [REACTION:FREE_ADAMANTINE_THREAD]
    [NAME:create adamantine thread]
    [BUILDING:SMELTER:NONE]
    [PRODUCT:100:1:THREAD:NO_SUBTYPE:INORGANIC:ADAMANTINE][PRODUCT_DIMENSION:15000]
    [SKILL:SMELT]

If you want to use a different skill and workshop to make free thread:

    [REACTION:MAKE_COTTON_CANDY]
    [NAME:make some cotton candy]
    [BUILDING:KITCHEN:NONE]
    [PRODUCT:100:1:THREAD:NO_SUBTYPE:INORGANIC:ADAMANTINE][PRODUCT_DIMENSION:15000]
    [SKILL:COOK]

Alternatively, simply remove the inputs from the existing smelter reaction (accessible in Reaction_Smelter) and cheekily put a “10” in front of the output.

### Easy Flux, Sand, and Ore

Add \[REACTION_CLASS:FLUX\] to any stone you have to turn it into a flux. This is in inorganic_stone_mineral, or inorganic_stone_layer Or, add \[METAL_ORE:{metal name}:100\] to turn it into an ore. It also bears noting that the metal can easily be an alloy, like steel or brass. Likewise, open inorganic_stone_soil and add \[SOIL_SAND\] to any soil to turn it into sand suitable for making glass with.

None of these cheats require creating a new world (if you modify the **save** raws, not the world generation file). Turn peat into glass, basalt into platinum, and combine iron, diorite, and coal to make steel.

### Easy Metal

Open reaction_smelter and change any reactions you like. Remove the \[FUEL\] tag. to make them require no fuel. Remove the line(s) headed with \[REAGENT:whatever\] to make them require no reagents. You can pick any metal that exists in the game, as long as you pick the right raw name. (For example: IRON, PEWTER_LAY, and NICKEL_SILVER makes iron, lay pewter, and nickel silver respectively.)

    [REACTION:FREE_(metal name here)]
    [NAME:create (metal name here)]
    [BUILDING:SMELTER:NONE]
    [PRODUCT:100:1:BAR:NO_SUBTYPE:INORGANIC:(metal name {from raws})][PRODUCT_DIMENSION:150]
    [SKILL:SMELT]

These cheats do not require a new world (because they only modify existing reactions), and allow smelters to create steel and adamantine from nothing.

### Create Wood

To create wood for free, add this to reaction_smelter. (don't forget the wood type, like OAK, PINE, TOWER_CAP, or FUNGIWOOD.)

    [REACTION:FREE_WOOD]
    [NAME:create wood]
    [BUILDING:SMELTER:NONE]
    [PRODUCT:100:5:WOOD:NO_SUBTYPE:PLANT_MAT:(wood name {from raws}):WOOD]
    [SKILL:SMELT]

Some examples with very light wood, perfect for buckets, and a frozen wood.

    [REACTION:FREE_FROZEN_WOOD]
    [NAME:create frozen wood]
    [BUILDING:SMELTER:NONE]
    [PRODUCT:100:5:WOOD:NO_SUBTYPE:PLANT_MAT:NETHER_CAP:WOOD]
    [SKILL:SMELT]

    [REACTION:FREE_FEATHER_WOOD]
    [NAME:create light wood]
    [BUILDING:SMELTER:NONE]
    [PRODUCT:100:5:WOOD:NO_SUBTYPE:PLANT_MAT:FEATHER:WOOD]
    [SKILL:SMELT]

### Thread

    [REACTION:FREE_SILK_THREAD]
    [NAME:create silk thread]
    [BUILDING:SMELTER:NONE]
    [PRODUCT:100:10:THREAD:NONE:CREATURE_MAT:SPIDER_CAVE_GIANT:SILK]
    [PRODUCT_DIMENSION:15000]

Don't forget to add the PERMITTED_REACTION to entity_default too. Also works for yarn and plant thread if you change the materials.

### Produce Food

To create food for free, add this to **reaction_smelter**. Fair warning, this will NOT allow you to grow these plants if you have not already discovered/obtained them. If you cannot get sun berries or similar through trade or gathering, you won't be able to plant the seeds and grow crops from them.

    [REACTION:FREE_PLUMP_HELMET]
    [NAME:create plump helmets]
    [BUILDING:SMELTER:NONE]
    [PRODUCT:100:10:PLANT:NO_SUBTYPE:PLANT_MAT:MUSHROOM_HELMET_PLUMP:STRUCTURAL]
    [SKILL:SMELT]

    [REACTION:FREE_CAVE_WHEAT]
    [NAME:create cave wheat]
    [BUILDING:SMELTER:NONE]
    [PRODUCT:100:10:PLANT:NO_SUBTYPE:PLANT_MAT:GRASS_WHEAT_CAVE:STRUCTURAL]
    [SKILL:SMELT]

    [REACTION:FREE_WILD_STRAWBERRIES]
    [NAME:create wild strawberries]
    [BUILDING:SMELTER:NONE]
    [PRODUCT:100:10:PLANT:NO_SUBTYPE:PLANT_MAT:BERRIES_STRAW_WILD:STRUCTURAL]
    [SKILL:SMELT]

    [REACTION:FREE_PRICKLE_BERRIES]
    [NAME:create prickle berries]
    [BUILDING:SMELTER:NONE]
    [PRODUCT:100:10:PLANT:NO_SUBTYPE:PLANT_MAT:BERRIES_PRICKLE:STRUCTURAL]
    [SKILL:SMELT]

    [REACTION:FREE_SWEET_PODS]
    [NAME:create sweet pods]
    [BUILDING:SMELTER:NONE]
    [PRODUCT:100:10:PLANT:NO_SUBTYPE:PLANT_MAT:POD_SWEET:STRUCTURAL]
    [SKILL:SMELT]

    [REACTION:FREE_GRASS_TAIL_PIG]
    [NAME:create pig tail grass]
    [BUILDING:SMELTER:NONE]
    [PRODUCT:100:10:PLANT:NO_SUBTYPE:PLANT_MAT:GRASS_TAIL_PIG:STRUCTURAL]
    [SKILL:SMELT]

... and this to **entity_default**

        [PERMITTED_REACTION:FREE_PLUMP_HELMET]
        [PERMITTED_REACTION:FREE_CAVE_WHEAT]
        [PERMITTED_REACTION:FREE_WILD_STRAWBERRIES]
        [PERMITTED_REACTION:FREE_PRICKLE_BERRIES]
        [PERMITTED_REACTION:FREE_SWEET_PODS]
        [PERMITTED_REACTION:FREE_GRASS_TAIL_PIG]

### Produce Water/Magma

This reaction will allow your dwarves to draw water from the rock. Unfortunately, it will not allow them to part the Red Sea - for that, you'll need lots of screw pumps, but that's another story...

    [REACTION:CHEAT_WATER]
            [NAME:make water]
            [BUILDING:SMELTER:NONE]
            [REAGENT:rock:1:BOULDER:NONE:NONE:NONE][WORTHLESS_STONE_ONLY]
            [REAGENT:bucket:1:BUCKET:NONE:NONE:NONE][EMPTY][DOES_NOT_ABSORB][PRESERVE_REAGENT][DOES_NOT_DETERMINE_PRODUCT_AMOUNT]
            [PRODUCT:100:1:LIQUID_MISC:NONE:WATER:NONE][PRODUCT_DIMENSION:150][PRODUCT_TO_CONTAINER:bucket]

Slightly less cheaty, this reaction allows you to convert drinks to water at the brewery:

    [REACTION:PURIFY_WATER]
        [NAME:purify water from booze]
        [BUILDING:STILL:CUSTOM_P]

        [REAGENT:booze:150:DRINK:NONE:NONE:NONE]
        [REAGENT:container1:1:NONE:NONE:NONE:NONE]
            [CONTAINS:booze]
            [PRESERVE_REAGENT]
            [DOES_NOT_DETERMINE_PRODUCT_AMOUNT]

            [REAGENT:bucket:1:BUCKET:NONE:NONE:NONE]
            [EMPTY]
            [DOES_NOT_ABSORB]
            [PRESERVE_REAGENT]
            [DOES_NOT_DETERMINE_PRODUCT_AMOUNT]

            [PRODUCT:100:1:LIQUID_MISC:NONE:WATER:NONE]
            [PRODUCT_DIMENSION:150]
            [PRODUCT_TO_CONTAINER:bucket]
       [SKILL:BREW]

Heres a reaction to fill minecarts up with 2 levels of magma. Paste the reaction over any preexisting reaction you want (the example is MAKE_WAX_CRAFTS) leaving the original REACTION, NAME, and BUILDING lines.

        [REAGENT:minecart:1:TOOL:ITEM_TOOL_MINECART:NONE:NONE
            [PRESERVE_REAGENT]
            [DOES_NOT_DETERMINE_PRODUCT_AMOUNT]
        [PRODUCT:100:833:LIQUID_MISC:NONE:INORGANIC:NONE]
            [PRODUCT_TO_CONTAINER:minecart]
            [PRODUCT_DIMENSION:150]
        [SKILL:SMELT]

NOTE: use stockpile links to restrict this to Iron/Steel/Nickel/Candy carts, or risk spontaneous combustion in the workshop.

This is what it should look like when you are finished.

    [REACTION:MAKE_WAX_CRAFTS]                                        | THIS WAS HERE
        [NAME:make wax crafts]                                    | BEFORE.
        [BUILDING:CRAFTSMAN:CUSTOM_SHIFT_W]                       |
        [REAGENT:minecart:1:TOOL:ITEM_TOOL_MINECART:NONE:NONE]
            [PRESERVE_REAGENT]
            [DOES_NOT_DETERMINE_PRODUCT_AMOUNT]
        [PRODUCT:100:833:LIQUID_MISC:NONE:INORGANIC:NONE]
            [PRODUCT_TO_CONTAINER:minecart]
            [PRODUCT_DIMENSION:150]
        [SKILL:SMELT]

### More cheats (Ore and Seeds)

Here are some not-so cheaty cheats that can be used to create vital ores and seeds. They are good for the conscience, and do not ruin the game experience.

Don't forget to include the entity_default tags

    [REACTION:HEMATITE_SONATA]
    [NAME:The Hematite Sonata]
    [BUILDING:SMELTER:NONE]
    [PRODUCT:100:1:BOULDER:NONE:INORGANIC:HEMATITE]
    [FUEL]
    [SKILL:SMELT]

    [REACTION:CALCITE_CACOPHONY]
    [NAME:The Calcite Cacophony]
    [BUILDING:SMELTER:NONE]
    [PRODUCT:100:1:BOULDER:NONE:INORGANIC:CALCITE]
    [FUEL]
    [SKILL:SMELT]

    [REACTION:MICROCLINE_MELODY]
    [NAME:The Microcline Melody]
    [BUILDING:SMELTER:NONE]
    [PRODUCT:100:1:BOULDER:NONE:INORGANIC:MICROCLINE]
    [FUEL]
    [SKILL:SMELT]

    [REACTION:MALACHITE_MUSE]
    [NAME:The Malachite Muse]
    [BUILDING:SMELTER:NONE]
    [PRODUCT:100:1:BOULDER:NONE:INORGANIC:MALACHITE]
    [FUEL]
    [SKILL:SMELT]

    [REACTION:CASSITERITE_CAROL]
    [NAME:The Cassiterite Carol]
    [BUILDING:SMELTER:NONE]
    [PRODUCT:100:1:BOULDER:NONE:INORGANIC:CASSITERITE]
    [FUEL]
    [SKILL:SMELT]

    [REACTION:SEED_STEW]
    [NAME:The Stew of Seeds]
    [BUILDING:STILL:NONE]
    [PRODUCT:40:1:SEEDS:NONE:PLANT_MAT:MUSHROOM_HELMET_PLUMP:SEED]
    [PRODUCT:40:1:SEEDS:NONE:PLANT_MAT:GRASS_TAIL_PIG:SEED]
    [PRODUCT:40:1:SEEDS:NONE:PLANT_MAT:GRASS_WHEAT_CAVE:SEED]
    [PRODUCT:40:1:SEEDS:NONE:PLANT_MAT:POD_SWEET:SEED]
    [PRODUCT:40:1:SEEDS:NONE:PLANT_MAT:BUSH_QUARRY:SEED]
    [PRODUCT:40:1:SEEDS:NONE:PLANT_MAT:TUBER_BLOATED:SEED]
    [FUEL]
    [SKILL:BREWING]

The entity_default tags:

    [PERMITTED_REACTION:HEMATITE_SONATA]
    [PERMITTED_REACTION:CALCITE_CACOPHONY]
    [PERMITTED_REACTION:MICROCLINE_MELODY]
    [PERMITTED_REACTION:SEED_STEW]
    [PERMITTED_REACTION:MALACHITE_MUSE]
    [PERMITTED_REACTION:CASSITERITE_CAROL]

**Free leather reaction:**

    [REACTION:MAKE_LEATHER]
    [NAME:create leather]
    [BUILDING:SMELTER:NONE]
    [PRODUCT:100:20:SKIN_TANNED:NO_SUBTYPE:CREATURE_MAT:FISH_CAVE:LEATHER]
    [SKILL:SMELT]

### Free Soap from the practice workshop

This reaction changes the "practice_bonecarving" reaction into a create soap reaction which creates elf soap. And it uses the crossbow skill for some reason.

    [REACTION:PRACTICE_BONECARVING]
    [NAME:create soap]
    [BUILDING:PRACTICE_WORKSHOP:NONE]
    [PRODUCT:100:1:BAR:NONE:CREATURE_MAT:ELF:SOAP][PRODUCT_DIMENSION:150]
    [SKILL:CROSSBOW]

# Memory Hacking

---
⚠️ Conteúdo truncado (48043 bytes = ~12010 tokens). Para o artigo completo, visite [Cheating](https://dwarffortresswiki.org/index.php/Cheating).