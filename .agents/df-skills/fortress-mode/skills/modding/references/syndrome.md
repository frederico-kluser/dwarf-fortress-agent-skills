# Syndrome

> Fonte: [Syndrome](https://dwarffortresswiki.org/index.php/Syndrome) — Dwarf Fortress Wiki (GFDL/MIT)

In *Dwarf Fortress*, a **syndrome** can be thought of as a condition which applies a collection of effects to creatures who contract it. Syndromes give rise to several of the game's more interesting medical predicaments, such as alcohol inebriation, venomous snake bites, and the brain-rotting secretions of certain uninvited guests. That said, the syndrome system isn't functionally restricted to the simulation of disease - many of the game's supernatural features, such as werewolves, vampires, necromancers, mummy curses and the undead, are in fact produced by applying various special effects to creatures via syndromes.

*"Yeah, I know this. I was looking for examples..."*

## List of syndromes

In unmodded games, syndromes are generally named after the animal, substance or effect that delivers them. They can cause unpleasant and sometimes fatal symptoms over a short to long duration, but some will clear up over time or with the assistance of a doctor. A hospital is required to diagnose and potentially treat those that can be helped by treatment. Note that in a world with dragons and giant elephants, dwarves (and elves and humans) fall into the "small creatures" category for purposes of this discussion.

[TABLE]

1\. For small creatures such as humans and dwarves, paralysis tends to result in suffocation.

2\. Necrosis of the brain will eventually result in death once the brain rots away completely.

3\. Evil rain typically only causes minor symptoms such as blisters, bruising, coughing blood, dizziness, fever, nausea, oozing, and pain.

4\. Evil clouds either cause major symptoms (as with beast/titan/demon sicknesses) or permanently transform creatures into zombie-like forms.

5\. Titans, forgotten beasts, nightmares, experiments, demons and angels have a chance to have a randomized syndrome. These range from mildly hazardous (mild blisters from inhaling boiling blood) to instantly fatal (severe necrosis from a contact poison attached to a breath weapon/creature made of blood).

## The anatomy of a syndrome

To recap, syndromes are "diseases" which inflict effects upon creatures who acquire them. Mechanically, they're composed of a bunch of different syndrome tokens which detail how it works and what it does. Syndrome acquisition can be boiled down into two main routes: (1) via materials and (2) via interactions. Unlike most objects in the game, syndromes aren't defined in their own raw file; they're instead built up within the raw definition of the material or interaction effect to which they are tied, as described below.

**1) Transmission via Materials**

Any material (be it inorganic, creature-derived, or plant-derived) can have one or more syndromes added to it, simply by defining the syndrome within the material's own raw definition. The addition of certain tokens (detailed below) to the syndrome will determine what must be done to the material so as to transmit the syndrome to a creature; the current modes of transmission are as follows: bodily contact with the material, ingestion or inhalation of the material, or injection of the material into the bloodstream. Any combination of transmission modes can be specified per syndrome.

Here's the material definition of giant cave spider venom with its associated syndrome as an example:

*(See here for the complete creature raw.)*

`   [USE_MATERIAL_TEMPLATE:POISON:CREATURE_EXTRACT_TEMPLATE]`\
`       [STATE_NAME:ALL_SOLID:frozen giant cave spider venom]`\
`       [STATE_ADJ:ALL_SOLID:frozen giant cave spider venom]`\
`       [STATE_NAME:LIQUID:giant cave spider venom]`\
`       [STATE_ADJ:LIQUID:giant cave spider venom]`\
`       [STATE_NAME:GAS:boiling giant cave spider venom]`\
`       [STATE_ADJ:GAS:boiling giant cave spider venom]`\
`       [PREFIX:NONE]`\
`       [ENTERS_BLOOD]`\
`       `**`[SYNDROME]`**\
`           `**`[SYN_NAME:giant cave spider bite]`**\
`           `**`[SYN_AFFECTED_CLASS:GENERAL_POISON]`**\
`           `**`[SYN_IMMUNE_CREATURE:SPIDER_CAVE_GIANT:ALL]`**\
`           `**`[SYN_INJECTED]`**\
`           `**`[CE_PARALYSIS:SEV:100:PROB:100:RESISTABLE:SIZE_DILUTES:START:5:PEAK:10:END:20]`**

In the above, the non-bolded section consists of various material definition tokens used to define and customise the venom material. (USE_MATERIAL_TEMPLATE defines a material called 'POISON', and creates it using the template 'CREATURE_EXTRACT_TEMPLATE' as a basis, which is then altered by the other tokens placed below it. See STATE_NAME, STATE_ADJ, and PREFIX for more information about these tokens). The relevance of ENTERS_BLOOD in this context is explained below.

The bolded section consists of the syndrome definition, which is initiated using the [\SYNDROME\] token. The tokens placed after this (which are described in further detail below) flesh out the syndrome - in this case they name it "giant cave spider bite", make it work only against creatures belonging to the 'GENERAL_POISON' creature class, render giant cave spiders immune to it, and cause creatures to contract it if the venom is injected into them. The creature effect at the very bottom makes the syndrome inflict progressive complete paralysis upon the victim after a short delay, for what would be a relatively short-lived period were it not for the fact that most small creatures tend to suffocate before the effect wears off.

Great, so how do we get this lethal venom into a creature's bloodstream to transmit the syndrome? Giant cave spiders are able to do this via the SPECIALATTACK_INJECT_EXTRACT token appended to their bite attack as such:

`   [SPECIALATTACK_INJECT_EXTRACT:LOCAL_CREATURE_MAT:POISON:LIQUID:100:100]`

This makes their bites inject 100 units of the 'POISON' material in its liquid state. Note that 'LOCAL_CREATURE_MAT:POISON' indicates that the 'POISON' material is defined amidst the same creature raws where the attack was detailed i.e. within the SPIDER_CAVE_GIANT creature definition; we could have written 'CREATURE_MAT:SPIDER_CAVE_GIANT:POISON' instead for the same result. Also note that we can make the attack inject any material we want it to, not just creature-associated materials. (Want your spider to inject molten gold into its victims to melt them from the inside out instead of bothering with syndromes? Simply replace 'LOCAL_CREATURE_MAT:POISON:LIQUID' with 'INORGANIC:GOLD:LIQUID' and you're good to go).

Note that \[ENTERS_BLOOD\] must be added to the material definition for injection attacks making use of this material to function properly. Without this token, the material would simply splatter over the attacked bodypart instead of entering the bloodstream, so the above syndrome, which relies solely on the injectable transmission route, wouldn't be contracted. \[ENTERS_BLOOD\] can of course be left out intentionally, if the aim is to cover creatures with a material that transmits syndromes on contact. Keep in mind that splattering in lieu of injection also occurs with blunt attacks, on attacked body parts devoid of VASCULAR tissue, and on bloodless victims (including creatures who've had their blood removed via CE_REMOVE\_).

A fun variation on typical creature venoms is to add a contact-transmissible syndrome to the creature's blood material - this tends to end poorly for any predator that chooses to attack them.

**2) Transmission via Interactions**

The interaction system can be used to add syndromes to creatures directly via certain interaction effects, most notably I_EFFECT:ADD_SYNDROME. After placing this I_EFFECT in an interaction definition, the syndrome to be added is defined beneath it in exactly the same manner as that used for the material-bound syndromes described above. (Note that any IE\_ tokens used with this I_EFFECT can be placed before or after the syndrome definition; the order doesn’t really matter). The  ANIMATE and  RESURRECT interaction effects also allow syndromes to be tied to them in the same manner; in this case the syndrome is applied to the target creature after it is animated or resurrected respectively.

See below for an example of a syndrome-transmitting interaction.

## Basic syndrome tokens

[TABLE]

## Creature Effect Tokens

Each and every syndrome has a number of creature effect tokens, represented by CE_X - these lovely little beauties determine exactly how the poor creature suffering from the syndrome is affected. An example CE token is as follows:

` [CE_NECROSIS:SEV:100:PROB:100:LOCALIZED:VASCULAR_ONLY:RESISTABLE:START:50:PEAK:1000:END:2000]`

In this example, we have an effect that will always cause severe necrosis in whichever bodypart it touches, so long as that bodypart is vascular and that the creature is not able to resist it in some manner. The effect begins shortly after the syndrome is contracted, peaks 1000 time units afterwards, and finally ceases another 1000 time units later.

As a general rule of thumb, so long as CE_X starts the string and START/(PEAK/END) ends it, the order of the intervening tokens isn't important.

[TABLE]

A key point that needs to be understood with regards to damaging syndrome effects such as bruising is that they deal a quantity of damage (based on the effect's SEV and other modifiers) **every tick**, and this damage accumulates over time. Thus, even a bruising effect at the lowest possible severity value **will** eventually lead to destruction of the affected body part(s) if the effect has a long enough duration. Similarly, healing effects undo a specific amount of damage every tick whilst the effect lasts.

### Symptomatic Effects

The following table contains creature effect tokens which cause purely medical symptoms.

Non-targeted effects will ignore any BP tokens and LOCALIZED tokens.

The details of this table are still being thrashed out by modders, so if you have anything to add, please don't hesitate to hit the edit button!

[TABLE]

### Healing Effects

As of version 0.47.01, most of the above effects have counterparts to alleviate symptoms and heal physical damage:

[TABLE]

### Special Effects

Several special syndrome effects take different arguments than the above. These are used for generated interactions in unmodded games, but may be used as well for any custom substance or interaction.

[TABLE]

**All** creature effect tokens take START, END and PROB numbers, and can be followed by \[CE:PERIODIC\] and/or \[CE:COUNTER_TRIGGER\] to restrict when they actually take effect.

### Periodic Triggers

**\[CE::\:\:\\]**

When this token is placed after a syndrome effect, it will prevent that effect from working unless within the specified period range.

For example, generated werebeast syndromes have a body transformation effect with `[CE:PERIODIC:``MOON_PHASE``:27:0]`, which makes the transformation active only throughout moon phases 27 to 0 (the full moon period). Once the moon phase changes from 0 to 1, the transformation will end and remain inactive until phase 27 is reached again (unless of course the effect has an END time which is reached before this happens. On that note, keep in mind that the START time of the effect needs to have been reached for activation to have become possible).

Only one periodic trigger may currently be specified per effect. Counter triggers can also be specified for the same effect, in which case both the periodic trigger and at least one counter trigger will need to have its conditions met for the effect to be allowed to work.

MOON_PHASE is currently the only valid period type:

[TABLE]

### Counter Triggers

**\[CE::\:\:\:REQUIRED\]**

Creatures in *Dwarf Fortress* possess internal counters which keep track of their various activities and statuses. When this token is placed after a syndrome effect, it will prevent the effect from working unless the affected creature has the indicated counter, and its value lies within the specified range.

For example, generated vampire syndromes use `[CE:COUNTER_TRIGGER:``DRINKING_BLOOD``:1:NONE:REQUIRED]` with an appearance modifier to make the vampire's teeth temporarily lengthen whilst leeching blood.

Note that `NONE` can be used in place of \ to indicate that any value above \ is valid. `NONE` can also be used in place of \, which is equivalent to the lowest value attainable by a counter.

`REQUIRED` implies that the effect won't proceed if the counter exists but doesn't lie within the range provided. However, it's actually redunant as COUNTER_TRIGGER always checks for both of these conditions 5; replacing it with `NONE` doesn't alter the way the trigger functions, though it *will* fail to work if this slot is left empty instead.

As detailed below, most counters only exist temporarily, so their use as triggers is somewhat more restricted than intuition suggests. For example, specifying `0` or `NONE` as the \ for a CAVE_ADAPT trigger wouldn't permit the effect to work when the affected creature is outside, since this counter is removed from the unit as soon as its value decreases past 1. Similarly, MILK_COUNTER is only present for some time *after* a creature is milked.

Multiple counter triggers can be specified per effect, in which case the effect will be permitted to work if at least one of the trigger conditions is met. A periodic trigger can also be specified for the same effect, in which case both the periodic trigger and at least one counter trigger will need to have their conditions met for the effect to work.

The following is a list of valid counter types including a couple of notable values:

[TABLE]

## Inorganic syndromes and you!

It's perfectly possible - and quite simple - to add a nasty syndrome to a type of rock or metal - you simply add the syndrome tokens to the material definition in the same manner that you would add them to a creature material definition. The only catch is that since your hapless dwarves will only normally encounter the material in metal, gem or boulder form, a bit of creativity must be used to actually get them inside your citizens - that is, you need to make them 'explosively boil' as soon as they're mined or produced. This has the sad side effect of destroying the actual item - sorry, no highly radioactive uranium this release.

The easiest way to accomplish this is to assign the material a low boiling point, usually just under room temperature, and make sure its temperature is fixed to a point above it.

` [MELTING_POINT:NONE]`\
` [BOILING_POINT:10000]`\
` [MAT_FIXED_TEMP:10001]`

Now, as soon as this substance hits the open air - by being mined, smelted or reaction-produced at a custom workshop - it will EXPLOSIVELY BOIL, flooding a small area with delicious syndrome-rich gas. Creatures who inhale the gas will be immediately hit with the SYN_INHALED syndrome you thoughtfully attached to the material definition earlier!

There are a number of other tokens you can use to control the colour and naming conventions of your syndrome material, referred to as material definition tokens.

## Spreading diseases

It's fully possible to make a nasty disease capable of spreading itself from an infected dwarf to others, though it requires some skill in modding interactions as well. Here is an example of a plague-inflicting interaction:

` [INTERACTION:PLAGUE]`\
`   [I_TARGET:A:CREATURE]`\
`       [IT_LOCATION:CONTEXT_CREATURE]`\
`       [IT_FORBIDDEN:NOT_LIVING]`\
`       [IT_AFFECTED_CLASS:GENERAL_POISON]`\
`       [IT_MANUAL_INPUT:creatures]`\
`   [I_EFFECT:ADD_SYNDROME]`\
`       [IE_TARGET:A]`\
`       [IE_IMMEDIATE]`\
`       [SYNDROME]`\
`           [SYN_NAME:the plague]`\
`           [SYN_AFFECTED_CLASS:GENERAL_POISON]`\
`           [CE_FEVER:SEV:250:PROB:100:START:250:PEAK:1500:END:25000]`\
`           [CE_BLISTERS:SEV:325:PROB:100:BP:BY_CATEGORY:ALL:SKIN:START:250:PEAK:1500:END:25000]`\
`           [CE_NECROSIS:SEV:300:PROB:100:BP:BY_CATEGORY:ALL:ALL:VASCULAR_ONLY:START:22500:PEAK:23750:END:25000]`\
`           [CE_CAN_DO_INTERACTION:START:1500:END:25000]`\
`               [CDI:ADV_NAME:Spread the plague]`\
`               [CDI:INTERACTION:PLAGUE]`\
`               [CDI:TARGET:A:LINE_OF_SIGHT]`\
`               [CDI:TARGET_RANGE:A:10]`\
`               [CDI:WAIT_PERIOD:30]`

As you can see, the syndrome here inflicts blisters, fever and, after roughly a month, necrosis of the whole body - that's when the infected creatures will start dying out. But before that happens, CE_CAN_DO_INTERACTION makes them capable of spreading the plague further.

You also need a disease vector that will bring the plague straight to your fort. (hint: use various species of rats - they're perfect for that). The following code, added to a creature's raws, ensures the creature will infect anybody it encounters:

` [CAN_DO_INTERACTION:PLAGUE]`\
`   [CDI:ADV_NAME:Spread the plague]`\
`   [CDI:TARGET:A:LINE_OF_SIGHT]`\
`   [CDI:TARGET_RANGE:A:10]`\
`   [CDI:WAIT_PERIOD:30]`

As soon as the said creature is startled by your dwarves, the fun will begin.

### In 0.47.01

As of version 0.47.01, it may be possible to use a creature's established methods of attack for use in disease-spreading.

Let's use the borrowed example of the plague above. This time, the plague will spread through biting, using the following syndrome code:

` [INTERACTION:PLAGUE]`\
`   [I_TARGET:A:CREATURE]`\
`       [IT_LOCATION:CONTEXT_CREATURE]`\
`       [IT_FORBIDDEN:NOT_LIVING]`\
`       [IT_AFFECTED_CLASS:GENERAL_POISON]`\
`       [IT_MANUAL_INPUT:creatures]`\
`   [I_EFFECT:ADD_SYNDROME]`\
`       [IE_TARGET:A]`\
`       [IE_IMMEDIATE]`\
`       [SYNDROME]`\
`           [SYN_NAME:the plague]`\
`           [SYN_AFFECTED_CLASS:GENERAL_POISON]`\
`           [CE_FEVER:SEV:250:PROB:100:START:250:PEAK:1500:END:25000]`\
`           [CE_BLISTERS:SEV:325:PROB:100:BP:BY_CATEGORY:ALL:SKIN:START:250:PEAK:1500:END:25000]`\
`           [CE_NECROSIS:SEV:300:PROB:100:BP:BY_CATEGORY:ALL:ALL:VASCULAR_ONLY:START:22500:PEAK:23750:END:25000]`\
`           [CE_SPECIAL_ATTACK_INTERACTION:INTERACTION:PLAGUE:BP:BY_CATEGORY:TOOTH:START:0:ABRUPT]`

The line \[CE_SPECIAL_ATTACK_INTERACTION:INTERACTION:BITE_PLAGUE:BP:BY_CATEGORY:MOUTH:BP:BY_CATEGORY:TOOTH:START:0:ABRUPT\] allows any infected creature with an attack using mouth or tooth category body parts to immediately spread the disease using said attack. The victim of the attack may then spread the disease if they are able to attack with the needed body part/parts.

## Multi-caste/multi-creature body transformations

This is a way to get around the when using ANY or ALL castes for CE_BODY_TRANSFORMATION and not being limited to a single creature for transformations. It's an incredibly simple solution as you can see in this example code:

`[SYNDROME]`\
`[SYN_NAME:draconic curse]`\
`[SYN_CLASS:DRACONIC_CURSE]`\
`[CE_BODY_TRANSFORMATION:PROB:100:START:0]`\
`           [CE:CREATURE:HYDRA:MALE]`\
`[CE_BODY_TRANSFORMATION:PROB:100:START:0]`\
`           [CE:CREATURE:DRAGON:MALE]`\
`[CE_BODY_TRANSFORMATION:PROB:100:START:0]`\
`           [CE:CREATURE:HYDRA:FEMALE]`\
`[CE_BODY_TRANSFORMATION:PROB:100:START:0]`\
`           [CE:CREATURE:DRAGON:FEMALE]`

This code will transform a creature into either a female/male hydra or a female/male dragon. In conclusion, for every caste/creature you want a *victim* to transform into, you add a \[CE_BODY_TRANSFORMATION\] token with a \[PROB\] token attached to it.

## See also

- Syndrome examples
- Interaction token
- Modding
