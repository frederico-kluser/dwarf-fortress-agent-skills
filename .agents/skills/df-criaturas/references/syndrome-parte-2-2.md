# Syndrome (parte 2/2)

|  CE_BODY_MAT_INTERACTION | No | MAT_TOKEN: | This is used to tie an / interaction / to one of the creature’s body materials. Generated / vampire / syndromes use this effect to make vampire blood pass on the vampirism curse when consumed. / The target body material is specified by inserting its ID as defined in the creature raws. For example, when a syndrome with “CE_BODY_MAT_INTERACTION:MAT_TOKEN:SWEAT” is gained by a unit, the effect will apply to any material defined as “SWEAT” in the creature raws of that unit, if such a material is present. / RESERVED_BLOOD / is a special body material token which can be used to specify the / \[BLOOD\] / material of any creature, regardless of the material's actual ID. / The following tokens should be placed after this effect: / CE:SYNDROME_TAG: / is used to specify what must be done with the body material to trigger the interaction. Replace " / " with any of / SYN_INGESTED / , / SYN_INJECTED / , / SYN_CONTACT / , / SYN_INHALED / . Multiple instances of this tag may be used to specify different valid transmission routes. / However, SYN_INGESTED appears to be the only one that works at present. / CE:INTERACTION: / \ is used to specify which interaction is to be run (replace " / " with the name of the desired interaction). Appropriate interaction effects with a creature target (such as / ADD_SYNDROME / ) will be inflicted upon the unit who interacts with the body material as specified above. Note that the linked interaction must have an / \[I_SOURCE:INGESTION\] / token for this to work. / This currently only works on materials obtained from historical figures. That is to say, the material must bear the source unit's name, such as "Urist McVampire's dwarf blood" as opposed to mere "dwarf blood". |
|  CE_SENSE_CREATURE_CLASS | No | CLASS:\: / : / : / : | Provides the ability to sense creatures belonging to the specified creature class even when such creatures lie far beyond line of sight, including through walls and floors. It also appears to reduce or negate the combat penalty of blind units when fighting creatures they can sense. In adventure mode, the specified tile will be used to represent sensed creatures when they cannot be seen directly. |
|  CE_FEEL_EMOTION | No | EMOTION:\ | Makes the creature feel a specific emotion. The effect's SEV value determines how intense the emotion is. The creature also receives a thought in the following format: "\[creature\] feels \[emotion\] due to [\[syndrome name\]](/index.php/Syndrome#SYN_NAME "Syndrome")". See Emotion for the list of valid emotions. |
|  CE_CHANGE_PERSONALITY | No | FACET:\: | Changes a / personality facet / by the given amount. Multiple FACET: / : / sets may be used, and / can be negative. For example, generated / necromancer / syndromes come with the following effect: / \[CE_CHANGE_PERSONALITY:FACET:ANXIETY_PROPENSITY:50:FACET:TRUST:-50:START:0:ABRUPT\] / According to Toady, CE_CHANGE_PERSONALITY effects can cause creatures to re-evaluate their / goals / in worldgen; the boost to anxiety and distrust given to necromancers makes it more likely for them to develop the goal of / ruling the world / . / \[4\] |
|  CE_ERRATIC_BEHAVIOR | No |  | Causes erratic behavior, meaning "People that like to brawl have a chance of starting a brawl-level fight with any nearby adult." -Toady |

**All** creature effect tokens take START, END and PROB numbers, and can be followed by \[CE:PERIODIC\] and/or \[CE:COUNTER_TRIGGER\] to restrict when they actually take effect.

### Periodic Triggers

**\[CE: PERIODIC:::\]**

When this token is placed after a syndrome effect, it will prevent that effect from working unless within the specified period range.

For example, generated werebeast syndromes have a body transformation effect with `[CE:PERIODIC:``MOON_PHASE``:27:0]`, which makes the transformation active only throughout moon phases 27 to 0 (the full moon period). Once the moon phase changes from 0 to 1, the transformation will end and remain inactive until phase 27 is reached again (unless of course the effect has an END time which is reached before this happens. On that note, keep in mind that the START time of the effect needs to have been reached for activation to have become possible).

Only one periodic trigger may currently be specified per effect. Counter triggers can also be specified for the same effect, in which case both the periodic trigger and at least one counter trigger will need to have its conditions met for the effect to be allowed to work.

MOON_PHASE is currently the only valid period type:

|  |  |
|----|----|
| Period | Description |
|  MOON_PHASE | The lunar cycle in / Dwarf Fortress / is composed of 28 segments (each slightly shorter than a / day / in duration), with each segment represented by a value ranging from 0 to 27. These correspond to moon phases as follows: / 0 / = full moon / 1-4 / = waning gibbous / 5-8 / = waning half / 9-12 / = waning crescent / 13-14 / = new moon / 15-18 / = waxing crescent / 19-22 / = waxing half / 23-26 / = waxing gibbous / 27 / = full moon |

### Counter Triggers

**\[CE: COUNTER_TRIGGER::::REQUIRED\]**

Creatures in *Dwarf Fortress* possess internal counters which keep track of their various activities and statuses. When this token is placed after a syndrome effect, it will prevent the effect from working unless the affected creature has the indicated counter, and its value lies within the specified range.

For example, generated vampire syndromes use `[CE:COUNTER_TRIGGER:``DRINKING_BLOOD``:1:NONE:REQUIRED]` with an appearance modifier to make the vampire's teeth temporarily lengthen whilst leeching blood.

Note that `NONE` can be used in place of to indicate that any value above is valid. `NONE` can also be used in place of , which is equivalent to the lowest value attainable by a counter.

`REQUIRED` implies that the effect won't proceed if the counter exists but doesn't lie within the range provided. However, it's actually redunant as COUNTER_TRIGGER always checks for both of these conditions [5]; replacing it with `NONE` doesn't alter the way the trigger functions, though it *will* fail to work if this slot is left empty instead.

As detailed below, most counters only exist temporarily, so their use as triggers is somewhat more restricted than intuition suggests. For example, specifying `0` or `NONE` as the for a CAVE_ADAPT trigger wouldn't permit the effect to work when the affected creature is outside, since this counter is removed from the unit as soon as its value decreases past 1. Similarly, MILK_COUNTER is only present for some time *after* a creature is milked.

Multiple counter triggers can be specified per effect, in which case the effect will be permitted to work if at least one of the trigger conditions is met. A periodic trigger can also be specified for the same effect, in which case both the periodic trigger and at least one counter trigger will need to have their conditions met for the effect to work.

The following is a list of valid counter types including a couple of notable values:

|  |  |
|----|----|
| Counter | Description |
|  ALCOHOLIC | For / \[ALCOHOL_DEPENDENT\] / creatures, this counter increases by 1 each / tick / , and is reset to 0 when the creature drinks / alcohol / . The following messages are added after "needs alcohol to get through the working day" in the creature's description when the counter reaches the specified values: / 100800 (3 months) = and is starting to work slowly due to its scarcity / 201600 (6 months) = and really wants a drink / 302400 (9 months) = and has gone without a drink for far, far too long / 403200 (1 year) = and can't even remember the last time (s)he had some |
|  CAVE_ADAPT | For creatures with the / \[CAVE_ADAPT\] / token, this counter is created and increases by 1 each / tick / when the creature is in the / Dark / , and is deleted once the dwarf steps outside and / vomits / . See / cave adaptation / for more information. / 403200 (1 year) = going outside causes irritation / 604800 (1.5 years) = going outside causes nausea |
|  MILK_COUNTER | When a creature is milked, this counter is created and set to the frequency value specified in the creature's [`[MILKABLE]`](/index.php/Creature_token#MILKABLE "Creature token") token, and subsequently decreases by 1 each tick until it reaches 0, at which point it is immediately removed, making the creature available for milking again. |
|  EGG_SPENT | This counter is created and set to 100800 (3 months' worth of ticks in fortress mode) when a creature lays eggs, and thereafter decreases by 1 each tick until it reaches 0, at which point it is removed and the creature regains the ability to lay eggs. |
|  GROUNDED_ANIMAL_ANGER | This counter is added and increases by 200 whenever a unit is lying on the ground and does not have \[CAN_LEARN\]. It subsequently decreases by 1 each tick, with a 1% chance to increase by 200. The counter is removed if it decreases to 0. If the counter is greater than 45000 the unit will lash out at a random nearby unit and the counter will be reset to 40000. This is the counter's only effect. |
|  TIME_SINCE_SUCKED_BLOOD | This counter rises by 1 every / tick / for creatures with the / \[BLOODSUCKER\] / token. When it rises high enough (generally around 100800; 3 months in fortress mode time), the creature will seek an / unconscious / victim to leech off of. Blood-sucking causes the counter to decrease, and will continue until either the victim is dead or the counter reaches 0. Note that this counter isn't removed when 0 is reached. / When playing as a bloodsucker in / adventure mode / , the following bloodthirst indicators are displayed when this counter reaches the specified values: / 172800 (1 day in adventure mode time) = / Thirsty / 1209600 (1 week) = / Thirsty! / 2419200 (2 weeks) = / Thirsty! / Various penalties are applied as bloodthirst increases; see the / vampire / article for more information. |
|  DRINKING_BLOOD | This appears to be created and set to a fixed value of 20 whilst the creature is sucking blood, and begins to decrease by 1 each tick once blood-sucking ceases (as described above) until it reaches 0, at which point the counter is removed. |

## Inorganic syndromes and you!

It's perfectly possible - and quite simple - to add a nasty syndrome to a type of rock or metal - you simply add the syndrome tokens to the material definition in the same manner that you would add them to a creature material definition. The only catch is that since your hapless dwarves will only normally encounter the material in metal, gem or boulder form, a bit of creativity must be used to actually get them inside your citizens - that is, you need to make them 'explosively boil' as soon as they're mined or produced. This has the sad side effect of destroying the actual item - sorry, no highly radioactive uranium this release.

The easiest way to accomplish this is to assign the material a low boiling point, usually just under room temperature, and make sure its temperature is fixed to a point above it.

     [MELTING_POINT:NONE]
     [BOILING_POINT:10000]
     [MAT_FIXED_TEMP:10001]
     [SPEC_HEAT:1]

Now, as soon as this substance hits the open air - by being mined, smelted or reaction-produced at a custom workshop - it will EXPLOSIVELY BOIL, flooding a small area with delicious syndrome-rich gas. Creatures who inhale the gas will be immediately hit with the SYN_INHALED syndrome you thoughtfully attached to the material definition earlier! Note that creatures do not need to inhale every tick, so there is a chance that the gas will dissipate before it can infect any particular creature.

There are a number of other tokens you can use to control the colour and naming conventions of your syndrome material, referred to as material definition tokens.

## Spreading diseases

It's fully possible to make a nasty disease capable of spreading itself from an infected dwarf to others, though it requires some skill in modding interactions as well. Here is an example of a plague-inflicting interaction:

     [INTERACTION:PLAGUE]
        [I_TARGET:A:CREATURE]
            [IT_LOCATION:CONTEXT_CREATURE]
            [IT_FORBIDDEN:NOT_LIVING]
            [IT_AFFECTED_CLASS:GENERAL_POISON]
            [IT_MANUAL_INPUT:creatures]
        [I_EFFECT:ADD_SYNDROME]
            [IE_TARGET:A]
            [IE_IMMEDIATE]
            [SYNDROME]
                [SYN_NAME:the plague]
                [SYN_AFFECTED_CLASS:GENERAL_POISON]
                [CE_FEVER:SEV:250:PROB:100:START:250:PEAK:1500:END:25000]
                [CE_BLISTERS:SEV:325:PROB:100:BP:BY_CATEGORY:ALL:SKIN:START:250:PEAK:1500:END:25000]
                [CE_NECROSIS:SEV:300:PROB:100:BP:BY_CATEGORY:ALL:ALL:VASCULAR_ONLY:START:22500:PEAK:23750:END:25000]
                [CE_CAN_DO_INTERACTION:START:1500:END:25000]
                    [CDI:ADV_NAME:Spread the plague]
                    [CDI:INTERACTION:PLAGUE]
                    [CDI:TARGET:A:LINE_OF_SIGHT]
                    [CDI:TARGET_RANGE:A:10]
                    [CDI:WAIT_PERIOD:30]

As you can see, the syndrome here inflicts blisters, fever and, after roughly a month, necrosis of the whole body - that's when the infected creatures will start dying out. But before that happens, CE_CAN_DO_INTERACTION makes them capable of spreading the plague further.

You also need a disease vector that will bring the plague straight to your fort. (hint: use various species of rats - they're perfect for that). The following code, added to a creature's raws, ensures the creature will infect anybody it encounters:

     [CAN_DO_INTERACTION:PLAGUE]
        [CDI:ADV_NAME:Spread the plague]
        [CDI:TARGET:A:LINE_OF_SIGHT]
        [CDI:TARGET_RANGE:A:10]
        [CDI:WAIT_PERIOD:30]

As soon as the said creature is startled by your dwarves, the fun will begin.

It is also possible to use a creature's established methods of attack for use in disease-spreading.

Let's use the borrowed example of the plague above. This time, the plague will spread through biting, using the following syndrome code:

     [INTERACTION:PLAGUE]
        [I_TARGET:A:CREATURE]
            [IT_LOCATION:CONTEXT_CREATURE]
            [IT_FORBIDDEN:NOT_LIVING]
            [IT_AFFECTED_CLASS:GENERAL_POISON]
            [IT_MANUAL_INPUT:creatures]
        [I_EFFECT:ADD_SYNDROME]
            [IE_TARGET:A]
            [IE_IMMEDIATE]
            [SYNDROME]
                [SYN_NAME:the plague]
                [SYN_AFFECTED_CLASS:GENERAL_POISON]
                [CE_FEVER:SEV:250:PROB:100:START:250:PEAK:1500:END:25000]
                [CE_BLISTERS:SEV:325:PROB:100:BP:BY_CATEGORY:ALL:SKIN:START:250:PEAK:1500:END:25000]
                [CE_NECROSIS:SEV:300:PROB:100:BP:BY_CATEGORY:ALL:ALL:VASCULAR_ONLY:START:22500:PEAK:23750:END:25000]
                [CE_SPECIAL_ATTACK_INTERACTION:INTERACTION:PLAGUE:BP:BY_CATEGORY:TOOTH:START:0:ABRUPT]

\
The line \[CE_SPECIAL_ATTACK_INTERACTION:INTERACTION:BITE_PLAGUE:BP:BY_CATEGORY:MOUTH:BP:BY_CATEGORY:TOOTH:START:0:ABRUPT\] allows any infected creature with an attack using mouth or tooth category body parts to immediately spread the disease using said attack. The victim of the attack may then spread the disease if they are able to attack with the needed body part/parts.

## Multi-caste/multi-creature body transformations

This is a way to get around the  looping problem when using ANY or ALL castes for CE_BODY_TRANSFORMATION and not being limited to a single creature for transformations. It's an incredibly simple solution as you can see in this example code:

    [SYNDROME]
        [SYN_NAME:draconic curse]
        [SYN_CLASS:DRACONIC_CURSE]
        [CE_BODY_TRANSFORMATION:PROB:25:START:0]
                [CE:CREATURE:HYDRA:MALE]
        [CE_BODY_TRANSFORMATION:PROB:33:START:0]
                [CE:CREATURE:DRAGON:MALE]
        [CE_BODY_TRANSFORMATION:PROB:50:START:0]
                [CE:CREATURE:HYDRA:FEMALE]
        [CE_BODY_TRANSFORMATION:PROB:100:START:0]
                [CE:CREATURE:DRAGON:FEMALE]

This code will transform a creature into either a female/male hydra or a female/male dragon.

For every caste/creature you want a *victim* to transform into, you add a \[CE_BODY_TRANSFORMATION\] token with a \[PROB\] token attached to it. For each of the transformations, the PROB is set to `100 / number_of_remaining_transformations` (or different numbers if you want uneven odds), with the final transformation having a PROB of 100 to ensure there is always at least one transformation chosen. A creature can only have one active transformation at a time, so if any of the lower PROB transformations occurs then the PROB 100 transformation can not happen.

If you instead want a *sequence* of transformations to take place then you need make sure that one transformation ends on the same tick that the next one begins:

    [SYNDROME]
        [SYN_NAME:draconic sequence curse]
        [SYN_CLASS:DRACONIC_SEQUENCE_CURSE]
        [CE_BODY_TRANSFORMATION:PROB:100:START:0:END:10]
                [CE:CREATURE:HYDRA:MALE]
        [CE_BODY_TRANSFORMATION:PROB:100:START:10:END:20]
                [CE:CREATURE:DRAGON:MALE]
        [CE_BODY_TRANSFORMATION:PROB:100:START:20:END:30]
                [CE:CREATURE:HYDRA:FEMALE]
        [CE_BODY_TRANSFORMATION:PROB:100:START:30:END:40]
                [CE:CREATURE:DRAGON:FEMALE]

## See also

- Syndrome examples
- Interaction token
- Modding


---
*Parte 2 de 2 de «Syndrome». Demais partes em arquivos `...-part-{1..2}.md` na mesma pasta. Fonte: https://dwarffortresswiki.org/index.php/Syndrome*
