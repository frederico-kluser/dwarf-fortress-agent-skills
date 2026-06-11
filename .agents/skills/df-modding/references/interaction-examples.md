# Interaction examples

> Fonte: [Interaction examples](https://dwarffortresswiki.org/index.php/Interaction_examples) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

This page was created to aid those curious about the interaction process by providing example interactions for them to use or study. Those familiar with interaction raws should feel free to add helpful/obscure information to the lists below to help members of the community less experienced with interactions.

## General Tips

### Synchronizing Adventure and Fort Mode syndrome timers

Fort mode runs 144 times faster than adventure mode - which means that a syndrome that lasts a single tick in Fort Mode will last 144 ticks in Adventure Mode. For short-term syndromes, this will cause very different behaviors between the two modes. In order to ensure that a syndrome operates the same way regardless of mode, add DWF_STRETCH:144 to the end of the CE effect tag.

It is not possible to make a syndrome that lasts shorter than 144 ticks in Adventure Mode

### Syndromes with no effect

There are times you will want to create a syndrome that has no actual effect - generally in order to add a SYN_CLASS that renders the target untargetable by a different interaction. Syndromes disappear once their effects have expired, so to do this you will need to add an effect that does nothing. Some examples:

    "Dummy" syndrome tags

    [CE_SPEED_CHANGE:SPEED_PERC:100:START:0:END:1:DWF_STRETCH:144] <-- Makes the target move at 100% of its current speed

    [CE_SKILL_ROLL_ADJUST:PERC:100:PERC_ON:0:START:0:END:1:DWF_STRETCH:144] <-- Multiplies the target's skill by 100%, 0% of the time

    [CE_MATERIAL_FORCE_MULTIPLIER:PROB:100:MAT_MULT:NONE:NONE:1:1:START:0:END:1:DWF_STRETCH:144] <-- Makes the target take 1/1 times its normal damage from attacks

So if you see tags like this in the examples below, this is what they are for.

## Material Emission Interactions

Following are several examples of material emission interactions.

### Multiple Projectile Emission

    Example [MATERIAL_EMISSION] interaction raws that fire three projectiles of the same material

     [INTERACTION:MATERIAL_EMISSION_3]
        [I_SOURCE:CREATURE_ACTION]
        [I_TARGET:A:MATERIAL]
            [IT_MATERIAL:CONTEXT_MATERIAL]
        [I_TARGET:B:LOCATION]
            [IT_LOCATION:CONTEXT_LOCATION] <-- this is always the emitter for now
        [I_TARGET:C:LOCATION]
            [IT_LOCATION:CONTEXT_CREATURE_OR_LOCATION] <-- lets projectiles be aimed at specific creatures
            [IT_MANUAL_INPUT:target]
        [I_EFFECT:MATERIAL_EMISSION]
            [IE_TARGET:A]
            [IE_TARGET:B]
            [IE_TARGET:C]
            [IE_IMMEDIATE]
        [I_EFFECT:MATERIAL_EMISSION]
            [IE_TARGET:A]
            [IE_TARGET:B]
            [IE_TARGET:C]
            [IE_IMMEDIATE]
        [I_EFFECT:MATERIAL_EMISSION]
            [IE_TARGET:A]
            [IE_TARGET:B]
            [IE_TARGET:C]
            [IE_IMMEDIATE]

\
By adding additional \[I_EFFECT:MATERIAL_EMISSION\] tags with their associated targets, you may stack additional projectiles.

### Predefined Material Emissions

    Example [MATERIAL_EMISSION] interaction raws that use a predefined material

     [INTERACTION:BASALT_EMISSION]
        [I_SOURCE:CREATURE_ACTION]
        [I_TARGET:A:MATERIAL]
            [IT_MATERIAL:MATERIAL:INORGANIC:BASALT:SOLID_GLOB] <-- the predefined material (INORGANIC), sub material (BASALT), and action type (SOLID_GLOB)
        [I_TARGET:B:LOCATION]
            [IT_LOCATION:CONTEXT_LOCATION]
        [I_TARGET:C:LOCATION]
            [IT_LOCATION:CONTEXT_CREATURE_OR_LOCATION]
            [IT_MANUAL_INPUT:target]
        [I_EFFECT:MATERIAL_EMISSION]
            [IE_TARGET:A]
            [IE_TARGET:B]
            [IE_TARGET:C]
            [IE_IMMEDIATE]

If a material is listed in this format, the creature will not need a \[CDI:MATERIAL\] tag in their creature raws in order to use it. This allows projectile attacks to be gained through substance ingestion, other interactions, etc.

### Predefined Emissions of Different Types

    Example [MATERIAL_EMISSION] interaction raws that use two predefined material types

     [INTERACTION:BASALT_GRANITE_EMISSION]
        [I_SOURCE:CREATURE_ACTION]
        [I_TARGET:A:MATERIAL]
            [IT_MATERIAL:MATERIAL:INORGANIC:BASALT:SOLID_GLOB] <-- the predefined material (INORGANIC), sub material (BASALT), and action type (SOLID_GLOB)
        [I_TARGET:A1:MATERIAL]
            [IT_MATERIAL:MATERIAL:INORGANIC:GRANITE:LIQUID_GLOB] <-- the second predefined material (INORGANIC), sub material (GRANITE), and action type (LIQUID_GLOB)
        [I_TARGET:B:LOCATION]
            [IT_LOCATION:CONTEXT_LOCATION]
        [I_TARGET:C:LOCATION]
            [IT_LOCATION:CONTEXT_CREATURE_OR_LOCATION]
            [IT_MANUAL_INPUT:target]
        [I_EFFECT:MATERIAL_EMISSION]
            [IE_TARGET:A]
            [IE_TARGET:B]
            [IE_TARGET:C]
            [IE_IMMEDIATE]
        [I_EFFECT:MATERIAL_EMISSION]
            [IE_TARGET:A1]
            [IE_TARGET:B]
            [IE_TARGET:C]
            [IE_IMMEDIATE]

This interaction fires both a solid glob of basalt and a liquid glob of granite magma.

### Material Emissions With Immunity

    Example interaction raws that may only target unprotected creatures, and the protection interaction

     [INTERACTION:CTARGET_BASALT_EMISSION] <-- The projectile itself
        [I_SOURCE:CREATURE_ACTION]
        [I_TARGET:A:MATERIAL]
            [IT_MATERIAL:MATERIAL:INORGANIC:BASALT:SOLID_GLOB] <-- the material tags used in the previous predefined material example.
        [I_TARGET:B:LOCATION]
            [IT_LOCATION:CONTEXT_LOCATION]
        [I_TARGET:C:CREATURE] <-- the may no longer be used on a location and must target a creature.
            [IT_CANNOT_HAVE_SYNDROME_CLASS:NO_EMISSION] <-- the syndrome class that makes targeting a creature with this interaction impossible.
            [IT_LOCATION:CONTEXT_CREATURE]
            [IT_MANUAL_INPUT:target]
        [I_EFFECT:MATERIAL_EMISSION]
            [IE_TARGET:A]
            [IE_TARGET:B]
            [IE_TARGET:C]
            [IE_IMMEDIATE]

     [INTERACTION:EMISSION_PROTECTION] <-- The ability that protects creatures from the above projectile
        [I_TARGET:A:CREATURE]
            [IT_LOCATION:CONTEXT_CREATURE]
            [IT_MANUAL_INPUT:target]
        [I_EFFECT:ADD_SYNDROME]
            [IE_TARGET:A]
            [IE_IMMEDIATE]
            [SYNDROME]
                [SYN_CLASS:NO_EMISSION]
                [SYN_NAME:protection from projectiles]
                [CE_FLASH_TILE:TILE:'O':7:0:1:FREQUENCY:2000:1000:START:0:END:2:ABRUPT:DWF_STRETCH:144]

Material emissions used in this format are affected by \[IT_CANNOT_HAVE_SYNDROME_CLASS:X\] tags (given above as the custom tag NO_EMISSION). This allows a modder to create immunity syndromes, disallowing a creature using the emission interaction from targeting the creature with immunity.

## Targeted Interactions

Interactions that are specifically intended to target particular types of creatures.

### Turn Undead

An attack that hits all procedurally-generated zombies and ghouls.

    Turn Undead

    [INTERACTION:TURN_UNDEAD] <- Should work against all zombies and ghouls
        [I_SOURCE:CREATURE_ACTION]
        [I_TARGET:A:CREATURE]
            [IT_LOCATION:CONTEXT_CREATURE]
            [IT_MANUAL_INPUT:zombies]
            [IT_CANNOT_HAVE_SYNDROME_CLASS:TURN_UNDEAD]
            [IT_AFFECTED_CLASS:GENERAL_POISON]
            [IT_REQUIRES:NO_AGING]
            [IT_REQUIRES:NO_THOUGHT_CENTER_FOR_MOVEMENT]
            [IT_REQUIRES:NO_CONNECTIONS_FOR_MOVEMENT]
            [IT_REQUIRES:OPPOSED_TO_LIFE]
        [I_EFFECT:ADD_SYNDROME]
            [IE_TARGET:A]
            [IE_IMMEDIATE]
            [SYNDROME]
                [SYN_NAME:turned]
                [SYN_CLASS:TURN_UNDEAD]
                [CE_REMOVE_TAG:NO_DIZZINESS:NONAUSEA:NOFEAR:NOPAIN:NOSTUN:START:0:END:8:DWF_STRETCH:144] <-- This removes the normal undead tags, rendering them vulnerable to the syndrome's other effects.
                [CE_SKILL_ROLL_ADJUST:PERC:50:PERC_ON:100:START:0:END:8:DWF_STRETCH:144]
                [CE_DIZZINESS:SEV:200:PROB:100:START:0:END:8:DWF_STRETCH:144]
                [CE_NAUSEA:SEV:200:PROB:100:START:0:END:8:DWF_STRETCH:144]
                [CE_PAIN:SEV:100:PROB:100:START:0:END:8:DWF_STRETCH:144]

### Smite Evil

An attack that hits all procedurally-generated bogeymen, night creatures, vampires, werebeasts, demons, and... angels. There does not currently appear to be a way of excluding angels. (Eh, it's DF angels, they probably count as evil anyway).

    Smite Evil

    [INTERACTION:SMITE_EVIL]
        [I_SOURCE:CREATURE_ACTION]
        [I_TARGET:A:CREATURE]
            [IT_LOCATION:CONTEXT_CREATURE]
            [IT_MANUAL_INPUT:night creatures]
            [IT_CANNOT_HAVE_SYNDROME_CLASS:SMITE_EVIL]
            [IT_IMMUNE_CLASS:NOT_EVIL] <-- used to specify custom creatures that have the normal night creature tags but will be immune to the spell.
            [IT_REQUIRES:NO_DRINK]
            [IT_REQUIRES:NO_EAT]
            [IT_REQUIRES:NO_SLEEP]
            [IT_REQUIRES:NOPAIN]
            [IT_REQUIRES:NOSTUN]
            [IT_REQUIRES:NONAUSEA]
            [IT_REQUIRES:NOFEAR]
            [IT_REQUIRES:NOEXERT]
            [IT_REQUIRES:NO_DIZZINESS]
            [IT_REQUIRES:NO_FEVERS]
            [IT_REQUIRES:NOBREATHE]
            [IT_REQUIRES:CAN_LEARN]
            [IT_REQUIRES:CAN_SPEAK]
        [I_EFFECT:ADD_SYNDROME]
            [IE_TARGET:A]
            [IE_IMMEDIATE]
            [SYNDROME]
                [SYN_NAME:smote]
                [SYN_CLASS:SMITE_EVIL]
                [CE_REMOVE_TAG:NO_DIZZINESS:NONAUSEA:NOFEAR:NOPAIN:NOSTUN:START:0:END:8:DWF_STRETCH:144]
                [CE_SKILL_ROLL_ADJUST:PERC:50:PERC_ON:100:START:0:END:8:DWF_STRETCH:144]
                [CE_DIZZINESS:SEV:200:PROB:100:START:0:END:8:DWF_STRETCH:144]
                [CE_NAUSEA:SEV:200:PROB:100:START:0:END:8:DWF_STRETCH:144]
                [CE_PAIN:SEV:100:PROB:100:START:0:END:8:DWF_STRETCH:144]

## Multi-Stage Interactions

These are more elaborate groups of interactions that allow you to create complex behaviors by using interactions to enable or disable other interactions.

### Timed Self-Destruct (or other powerful ability) with Override Ability

This will allow the user to explode after spending a certain amount of time in combat. A few ticks before exploding, it will flash with a "!" as a warning. You can also replace the explosion with any other powerful ability that you want it to use only after a countdown. It also comes with a syndrome that will disable the explosion. This is intended to be used by non-playable units, like animals or zombies.

    Example Timed Self-Destruct with Override Ability

    [INTERACTION:EXPLOSION_READY_1] <-- This is the ability you actually give the creature.  Use CDI:USAGE_HINT:DEFEND, and CDI:TARGET:A:SELF_ONLY.
        [I_SOURCE:CREATURE_ACTION]
        [I_TARGET:A:CREATURE]
            [IT_LOCATION:CONTEXT_CREATURE]
            [IT_CANNOT_HAVE_SYNDROME_CLASS:EXPLOSION_READY_1]
        [I_EFFECT:ADD_SYNDROME]
            [IE_TARGET:A]
            [IE_IMMEDIATE]
            [SYNDROME]
                [SYN_NAME:counting down]
                [SYN_CLASS:EXPLOSION_READY_1]
                [CE_CAN_DO_INTERACTION:START:10:END:11:DWF_STRETCH:144] <--The START affects the amount of time spent in combat before the explosion can occur.
                    [CDI:ADV_NAME:Draw Energy]
                    [CDI:USAGE_HINT:DEFEND]
                    [CDI:VERB:engage self-destruct sequence:engages self-destruct sequence:NA]
                    [CDI:INTERACTION:EXPLOSION_READY_2]
                    [CDI:TARGET:A:SELF_ONLY]
                    [CDI:WAIT_PERIOD:1500]

    [INTERACTION:EXPLOSION_READY_2]
        [I_SOURCE:CREATURE_ACTION]
        [I_TARGET:A:CREATURE]
            [IT_LOCATION:CONTEXT_CREATURE]
            [IT_CANNOT_HAVE_SYNDROME_CLASS:EXPLOSION_READY_2]
            [IT_CANNOT_HAVE_SYNDROME_CLASS:EXPLOSION_OVERRIDE]
        [I_EFFECT:ADD_SYNDROME]
            [IE_TARGET:A]
            [IE_IMMEDIATE]
            [SYNDROME]
                [SYN_NAME:ready to explode]
                [SYN_CLASS:EXPLOSION_READY_2]
                [CE_FLASH_TILE:TILE:33:4:0:0:FREQUENCY:32:16:START:0:END:2:DWF_STRETCH:144] <-- Flash as a warning
                [CE_SPEED_CHANGE:SPEED_PERC:50:START:0:END:2:DWF_STRETCH:144]
                [CE_CAN_DO_INTERACTION:START:1:END:2:DWF_STRETCH:144] <-- The AI will use this and then immediately explode, provided it is still in combat and not affected by EXPLOSION_OVERRIDE.
                    [CDI:ADV_NAME:Remove safeties]
                    [CDI:USAGE_HINT:DEFEND]
                    [CDI:INTERACTION:EXPLOSION_READY_3]
                    [CDI:TARGET:A:SELF_ONLY]
                    [CDI:WAIT_PERIOD:250]

    [INTERACTION:EXPLOSION_READY_3]
        [I_SOURCE:CREATURE_ACTION]
        [I_TARGET:A:CREATURE]
            [IT_LOCATION:CONTEXT_CREATURE]
            [IT_CANNOT_HAVE_SYNDROME_CLASS:EXPLOSION_READY_3]
            [IT_CANNOT_HAVE_SYNDROME_CLASS:EXPLOSION_OVERRIDE]
        [I_EFFECT:ADD_SYNDROME]
            [IE_TARGET:A]
            [IE_IMMEDIATE]
            [SYNDROME]
                [SYN_NAME:about to explode]
                [SYN_CLASS:EXPLOSION_READY_3]
                [CE_FLASH_TILE:TILE:33:4:0:0:FREQUENCY:32:16:START:0:END:2:DWF_STRETCH:144]
                [CE_CAN_DO_INTERACTION:START:0:END:1:DWF_STRETCH:144]
                    [CDI:ADV_NAME:Explode]
                    [CDI:USAGE_HINT:ATTACK]
                    [CDI:INTERACTION:MATERIAL_EMISSION]
                    [CDI:VERB:explode:explodes:NA]
                    [CDI:MATERIAL:CREATURE_MAT:BOMBER:EXPLOSION:UNDIRECTED_DUST] <-- This points to a creature called BOMBER that contains the EXPLOSION material. It is better to put unstable materials in dummy creatures rather than making them INORGANICs, to prevent titans or forgotten beasts from being made of them.
                    [CDI:TARGET:C:LINE_OF_SIGHT]
                    [CDI:TARGET_RANGE:C:1]
                    [CDI:MAX_TARGET_NUMBER:C:1]
                    [CDI:WAIT_PERIOD:250]

    [INTERACTION:EXPLOSION_OVERRIDE] <-- Give this to any creature you want to be able to override the explosion.  For example, a necromancer that creates kamikaze zombies may disable any zombies nearby, to prevent friendly fire.
        [I_SOURCE:CREATURE_ACTION]
        [I_TARGET:A:CREATURE]
            [IT_LOCATION:CONTEXT_CREATURE]
            [IT_CANNOT_HAVE_SYNDROME_CLASS:EXPLOSION_READY_3]
            [IT_CANNOT_HAVE_SYNDROME_CLASS:EXPLOSION_OVERRIDE]
        [I_EFFECT:ADD_SYNDROME]
            [IE_TARGET:A]
            [IE_IMMEDIATE]
            [SYNDROME]
                [SYN_NAME:unable to explode]
                [SYN_CLASS:EXPLOSION_OVERRIDE]
                [CE_SPEED_CHANGE:SPEED_PERC:100:START:0:END:2:DWF_STRETCH:144]

## Transformation Interactions

These are interactions that will cause a creature to transform into another creature.

### Demon Transformation

This is a fairly straightforward transformation, as it only relies on one caste token. This interaction will transform a creature into a random non-unique demon

    Demon transformation

    [INTERACTION:DEMON_POLYMORPH]
        [I_SOURCE:CREATURE_ACTION]
        [I_TARGET:A:CREATURE]
            [IT_LOCATION:CONTEXT_CREATURE]
        [I_EFFECT:ADD_SYNDROME]
            [IE_TARGET:A]
            [IE_IMMEDIATE]
            [SYNDROME]
                [SYN_CONCENTRATION_ADDED:1000:0]
                [CE_BODY_TRANSFORMATION:START:0:PEAK:0:END:5:ABRUPT:DWF_STRETCH:144]
                    [CE:CREATURE_CASTE_FLAG:DEMON]
                [CE_ADD_TAG:NO_AGING:START:0:PEAK:0:END:5:ABRUPT:DWF_STRETCH:144]

Note that this interaction will not work in arena mode due to the lack of generated creatures in that mode. However, it will work if a creature performs the interaction in a loaded world that contains generated demons.

\

### Vault Guardian Transformation

Transformation syndromes that turn a creature into a titan or demon only really rely on the \[DEMON\] and \[TITAN\] tokens, but how can the same be achieved with vault guardians? Below is an example of an interaction that will reliably transform a creature into a random angel.

    Angel transformation

    [INTERACTION:ANGEL_POLYMORPH]
        [I_SOURCE:CREATURE_ACTION]
        [I_TARGET:A:CREATURE]
            [IT_LOCATION:CONTEXT_CREATURE]
        [I_EFFECT:ADD_SYNDROME]
            [IE_TARGET:A]
            [IE_IMMEDIATE]
            [SYNDROME]
                [SYN_CONCENTRATION_ADDED:1000:0]
                [CE_BODY_TRANSFORMATION:START:0:PEAK:0:END:5:ABRUPT:DWF_STRETCH:144]
                    [CE:FORBIDDEN_CREATURE_FLAG:SMALL_RACE]
                    [CE:FORBIDDEN_CREATURE_FLAG:HAS_ANY_FEATURE_BEAST]
                    [CE:CREATURE_FLAG:GENERATED] this is key, as the generated token is one unique to vault guardians and other "secret" creatures
                    [CE:FORBIDDEN_CREATURE_CASTE_FLAG:DEMON] we have to forbid all types of night creatures and other generated creatures so the game may only choose angels
                    [CE:FORBIDDEN_CREATURE_FLAG:HAS_ANY_NIGHT_CREATURE]
                    [CE:FORBIDDEN_CREATURE_FLAG:HAS_ANY_NIGHT_CREATURE_BOGEYMAN]
                    [CE:FORBIDDEN_CREATURE_FLAG:HAS_ANY_NIGHT_CREATURE_EXPERIMENTER]
                    [CE:FORBIDDEN_CREATURE_FLAG:HAS_ANY_NIGHT_CREATURE_NIGHTMARE]
                    [CE:FORBIDDEN_CREATURE_FLAG:HAS_ANY_NIGHT_CREATURE_HUNTER]
                    [CE:FORBIDDEN_CREATURE_CASTE_FLAG:CANNOT_BREATHE_AIR]
                    [CE:FORBIDDEN_CREATURE_CASTE_FLAG:IMMOBILE_LAND]
                    [CE:FORBIDDEN_CREATURE_CASTE_FLAG:MEGABEAST]
                    [CE:FORBIDDEN_CREATURE_CASTE_FLAG:SEMIMEGABEAST]
                    [CE:FORBIDDEN_CREATURE_CASTE_FLAG:TITAN]
                    [CE:FORBIDDEN_CREATURE_CASTE_FLAG:UNIQUE_DEMON]
                [CE_ADD_TAG:NO_AGING:START:0:PEAK:0:END:5:ABRUPT:DWF_STRETCH:144]

Note that this interaction will not work in arena mode due to the lack of generated creatures in that mode. However, it will work if a creature performs the interaction in a loaded world that contains vault guardians.

## Item Powers

An item's magicv51.01-beta26 field can hold an interaction. This sample interaction allows the wielder to shoot an icicle.

    Ice bolt

    [INTERACTION:MYTHICAL_ITEM_POWER_1]
       [I_SOURCE:ITEM_POWER]
           [IS_DESCRIPTION:This item shimmers with frost.]
           [IS_CDI:ADV_NAME:Launch ice bolt]
           [IS_CDI:INTERACTION:MYTHICAL_ITEM_POWER_1]
           [IS_CDI:MATERIAL:WATER:SHARP_ROCK]
           [IS_CDI:TARGET:C:LINE_OF_SIGHT]
           [IS_CDI:TARGET_RANGE:C:25]
           [IS_CDI:USAGE_HINT:ATTACK]
           [IS_CDI:VERB:focus:focuses:NA]
           [IS_CDI:MAX_TARGET_NUMBER:C:1]
           [IS_CDI:WAIT_PERIOD:50]
           [IS_CDI:DEFAULT_ICON:ADVENTURE_INTERACTION_ICON_LAUNCH_ICE_BOLT]
       [I_TARGET:A:MATERIAL]
           [IT_MATERIAL:CONTEXT_MATERIAL]
       [I_TARGET:B:LOCATION]
           [IT_LOCATION:CONTEXT_LOCATION]
       [I_TARGET:C:LOCATION]
           [IT_LOCATION:CONTEXT_CREATURE_OR_LOCATION]
       [IT_MANUAL_INPUT:target]
           [I_EFFECT:MATERIAL_EMISSION]
           [IE_TARGET:A]
           [IE_TARGET:B]
           [IE_TARGET:C]
           [IE_IMMEDIATE]

## See Also

- Creature examples
- Reaction examples
