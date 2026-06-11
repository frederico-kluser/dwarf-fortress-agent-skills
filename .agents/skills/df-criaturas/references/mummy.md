# Mummy

> Fonte: [Mummy](https://dwarffortresswiki.org/index.php/Mummy) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

"Who dares to enter my house? I curse you!"\
You feel horrible!

A **mummy** `Ñ` is an undead night creature, the preserved and magically animated body of a deceased ruler, placed in a tomb as a guardian of its contents. They are only encountered in adventure mode (unless you embark directly on the tomb), arising to attack interlopers who have disturbed their long slumber, afflicting intruders with horrible bad-luck curses for their crime. (A mummy's curse zeroes all skill rolls intermittently, using a skill adjust syndrome. Due to the way syndromes are timed in combination with dwarf mode, time is cut into segments about 7 walking steps long, and your luck is bad for 20% of those time segments. So if you are attacked during one of your unfortunate times, it will go as badly as it can possibly go. There are many random rolls that aren't skill-dependent, though.)

Graphically, all mummies will appear with dark yellow skin. They rest in every tomb and may be in catacombs beneath towns, fortresses and temples. Their coffin and slab will always be in a room together, surrounded by corpses they can command. Due to their preference of slumbering in their tombs, mummies are the only night creature that will never actively seek out their enemies from the start.

In world generation, mummies may be disturbed by thieves attempting to steal artifacts stored in their tomb. The mummy will form a grudge against the thief but will generally lash out at any nearby site, overrunning it with their undead minions. They will also revive important historical figures as intelligent undead. These will have procedurally generated names like "interred ghoul" designed to be more "cryptic" than other such names.

In tombs, mummies may be disturbed by bashing the door, taking items, or triggering traps. Approaching them without sneaking may alert them, and entering any tile adjacent to their coffin always will. Once awoken, they will unerringly home in on the intruder, even if unable to detect him or her. It should be noted that tombs are structured in such a way that the mummy's room is almost always in a location between the treasure rooms and the exit, almost inevitably leading to the player being intercepted by the mummy while trying to escape after looting. This could result in moderate to extreme amounts of fun, depending on if the corpses in the passageways have been cleared, ranging from the player getting away with a curse, to death.

Mummies are capable of raising the remains of others, much like necromancers, and calling these minions against their foes. Therefore, it is strongly recommended that any skeletons or bodies near the room containing the mummy are cleared out to the best possible extent prior to an encounter. Mummies can only be killed by decapitation or bisection. Because rulers lose their title upon death, the mummies will be identified by their other profession (such as a beekeeper mummy) or they can get the position of a bandit leader, if the bandits claim a tomb as their settlement before disturbing the mummy.

A safe way to approach mummies, talk to them, and even potentially recruit them as allies, is to become a night creature that undead are friendly with, such as a vampire or necromancer. If you do manage to get a mummy companion, use caution when passing through towns or forts – the mummy will begin to curse everyone in sight, and even attack if it has weapons. Despite what you may think, grabbing what you want and leaving before they can get to you is not a good idea, as they will follow you throughout the world.

Occasionally in world gen, mummies will be disturbed by AI adventurers and eventually create their own necromancer-style towers.[1]

Because the syndrome's effect multiplies rolls by zero, the blessing effect from divinations is negated.

    Example raws (as extracted from world.dat)

    [INTERACTION:DISTURBANCE_1]

    [GENERATED]

    [I_SOURCE:DISTURBANCE]

    [I_TARGET:A:CORPSE]
        [IT_LOCATION:CONTEXT_ITEM]
        [IT_FORBIDDEN:NOT_LIVING]
        [IT_REQUIRES:FIT_FOR_RESURRECTION]
        [IT_REQUIRES:CAN_LEARN]
        [IT_REQUIRES:CAN_SPEAK]
        [IT_CANNOT_HAVE_SYNDROME_CLASS:WERECURSE]
        [IT_CANNOT_HAVE_SYNDROME_CLASS:VAMPCURSE]
        [IT_CANNOT_HAVE_SYNDROME_CLASS:DISTURBANCE_CURSE]
        [IT_CANNOT_HAVE_SYNDROME_CLASS:RAISED_UNDEAD]
        [IT_CANNOT_HAVE_SYNDROME_CLASS:RAISED_GHOST]
        [IT_CANNOT_HAVE_SYNDROME_CLASS:GHOUL]

    [I_EFFECT:RESURRECT]
        [IE_TARGET:A]
        [IE_IMMEDIATE]
        [SYNDROME]
            [SYN_CONCENTRATION_ADDED:1000:0]
            [SYN_CLASS:DISTURBANCE_CURSE]
            [CE_DISPLAY_TILE:TILE:165:6:0:1:START:0:ABRUPT]
            [CE_DISPLAY_NAME:NAME:mummy:mummies:mummified:START:0:ABRUPT]
            [CE_PHYS_ATT_CHANGE:STRENGTH:300:1000:TOUGHNESS:300:1000:START:0:ABRUPT]
            [CE_ADD_TAG:NO_AGING:NOT_LIVING:STERILE:EXTRAVISION:NOEXERT:NOPAIN:NOBREATHE:NOSTUN:NONAUSEA:NO_DIZZINESS:NO_FEVERS:NOEMOTION:PARALYZEIMMUNE:NOFEAR:NO_EAT:NO_DRINK:NO_SLEEP:NO_PHYS_ATT_GAIN:NO_PHYS_ATT_RUST:NOTHOUGHT:NO_THOUGHT_CENTER_FOR_MOVEMENT:NO_CONNECTIONS_FOR_MOVEMENT:START:0:ABRUPT]
            [CE_REMOVE_TAG:HAS_BLOOD:TRANCES:MISCHIEVOUS:START:0:ABRUPT]
            [CE_CHANGE_PERSONALITY:FACET:ANXIETY_PROPENSITY:50:FACET:TRUST:-50:FACET:VENGEFUL:100:START:0:ABRUPT]
            [CE_CAN_DO_INTERACTION:START:0:ABRUPT]
                [CDI:ADV_NAME:Curse]
                [CDI:INTERACTION:DISTURBANCE_CURSE_1]
                [CDI:TARGET:A:LINE_OF_SIGHT:DISTURBER_ONLY]
                [CDI:TARGET_RANGE:A:25]
                [CDI:USAGE_HINT:MAJOR_CURSE]
                [CDI:VERBAL]
                [CDI:VERBAL_SPEECH:curse.txt]
                [CDI:TARGET_VERB:feel horrible:looks horrible]
                [CDI:MAX_TARGET_NUMBER:A:1]
                [CDI:WAIT_PERIOD:20]
            [CE_CAN_DO_INTERACTION:START:0:ABRUPT]
                [CDI:ADV_NAME:Animate corpse]
                [CDI:INTERACTION:DISTURBANCE_ANIMATE_1]
                [CDI:TARGET:A:LINE_OF_SIGHT]
                [CDI:TARGET_RANGE:A:25]
                [CDI:VERB:gesture:gestures:NA]
                [CDI:TARGET_VERB:shudder and begin to move:shudders and begins to move]
                [CDI:WAIT_PERIOD:10]
            [CE_CAN_DO_INTERACTION:START:0:ABRUPT]
                [CDI:ADV_NAME:Raise sacred stalker]
                [CDI:INTERACTION:DISTURBANCE_UNDEAD_RES_1]
                [CDI:TARGET:A:LINE_OF_SIGHT]
                [CDI:TARGET_RANGE:A:10]
                [CDI:VERB:gesture:gestures:NA]
                [CDI:TARGET_VERB:shudder and begin to move:shudders and begins to move]
                [CDI:WAIT_PERIOD:10]

    [INTERACTION:DISTURBANCE_CURSE_1]

    [GENERATED]

    [I_TARGET:A:CREATURE]
        [IT_LOCATION:CONTEXT_CREATURE]
        [IT_CANNOT_TARGET_IF_ALREADY_AFFECTED]
        [IT_MANUAL_INPUT:victim]

    [I_EFFECT:ADD_SYNDROME]
        [IE_TARGET:A]
        [IE_IMMEDIATE]
        [SYNDROME]
            [SYN_CONCENTRATION_ADDED:1000:0]
            [CE_SKILL_ROLL_ADJUST:PERC:0:PERC_ON:20:START:0:ABRUPT]

    [INTERACTION:DISTURBANCE_ANIMATE_1]

    [GENERATED]

    [I_TARGET:A:CORPSE]
        [IT_LOCATION:CONTEXT_ITEM]
        [IT_AFFECTED_CLASS:GENERAL_POISON]
        [IT_REQUIRES:FIT_FOR_ANIMATION]
        [IT_FORBIDDEN:NOT_LIVING]
        [IT_MANUAL_INPUT:corpses]

    [I_EFFECT:ANIMATE]
        [IE_TARGET:A]
        [IE_IMMEDIATE]
        [SYNDROME]
            [SYN_CONCENTRATION_ADDED:1000:0]
            [CE_FLASH_TILE:TILE:165:3:0:0:FREQUENCY:2000:1000:START:0:ABRUPT]
            [CE_PHYS_ATT_CHANGE:STRENGTH:130:0:TOUGHNESS:300:1000:START:0:ABRUPT]
            [CE_SPEED_CHANGE:SPEED_PERC:60:START:0:ABRUPT]
            [CE_ADD_TAG:NO_AGING:NOT_LIVING:OPPOSED_TO_LIFE:EXTRAVISION:NOEXERT:NOPAIN:NOBREATHE:NOSTUN:NONAUSEA:NO_DIZZINESS:NO_FEVERS:NOEMOTION:PARALYZEIMMUNE:NOFEAR:NO_EAT:NO_DRINK:NO_SLEEP:NO_PHYS_ATT_GAIN:NO_PHYS_ATT_RUST:NOTHOUGHT:NO_THOUGHT_CENTER_FOR_MOVEMENT:NO_CONNECTIONS_FOR_MOVEMENT:START:0:ABRUPT]
            [CE_REMOVE_TAG:HAS_BLOOD:TRANCES:MISCHIEVOUS:START:0:ABRUPT]

    [INTERACTION:DISTURBANCE_UNDEAD_RES_1]

    [GENERATED]

    [I_TARGET:A:CORPSE]
        [IT_LOCATION:CONTEXT_ITEM]
        [IT_AFFECTED_CLASS:GENERAL_POISON]
        [IT_REQUIRES:FIT_FOR_RESURRECTION]
        [IT_REQUIRES:CAN_LEARN]
        [IT_FORBIDDEN:NOT_LIVING]
        [IT_MANUAL_INPUT:corpses]
        [IT_CANNOT_HAVE_SYNDROME_CLASS:WERECURSE]
        [IT_CANNOT_HAVE_SYNDROME_CLASS:VAMPCURSE]
        [IT_CANNOT_HAVE_SYNDROME_CLASS:DISTURBANCE_CURSE]
        [IT_CANNOT_HAVE_SYNDROME_CLASS:RAISED_UNDEAD]
        [IT_CANNOT_HAVE_SYNDROME_CLASS:RAISED_GHOST]
        [IT_CANNOT_HAVE_SYNDROME_CLASS:GHOUL]

    [I_EFFECT:RESURRECT]
        [IE_TARGET:A]
        [IE_IMMEDIATE]
        [SYNDROME]
            [SYN_CONCENTRATION_ADDED:1000:0]
            [SYN_CLASS:RAISED_UNDEAD]
            [CE_DISPLAY_TILE:TILE:165:3:0:1:START:0:ABRUPT]
            [CE_DISPLAY_NAME:NAME:sacred stalker:sacred stalkers:sacred stalker:START:0:ABRUPT]
            [CE_PHYS_ATT_CHANGE:STRENGTH:200:1000:TOUGHNESS:200:1000:START:0:ABRUPT]
            [CE_ADD_TAG:NO_AGING:NOT_LIVING:STERILE:EXTRAVISION:NOEXERT:NOPAIN:NOBREATHE:NOSTUN:NONAUSEA:NO_DIZZINESS:NO_FEVERS:NOEMOTION:PARALYZEIMMUNE:NOFEAR:NO_EAT:NO_DRINK:NO_SLEEP:NO_PHYS_ATT_GAIN:NO_PHYS_ATT_RUST:NOTHOUGHT:NO_THOUGHT_CENTER_FOR_MOVEMENT:NO_CONNECTIONS_FOR_MOVEMENT:START:0:ABRUPT]
            [CE_REMOVE_TAG:HAS_BLOOD:TRANCES:MISCHIEVOUS:START:0:ABRUPT]
            [CE_CAN_DO_INTERACTION:START:0:ABRUPT]
                [CDI:ADV_NAME:Cause dizziness]
                [CDI:INTERACTION:DISTURBANCE_RES_POWER_1_1]
                [CDI:TARGET:A:LINE_OF_SIGHT]
                [CDI:TARGET_RANGE:A:25]
                [CDI:BP_REQUIRED:BY_TYPE:GRASP]
                [CDI:USAGE_HINT:ATTACK]
                [CDI:VERB:hold up hand:holds up hand:NA]
                [CDI:TARGET_VERB:feel dizzy:looks dizzy]
                [CDI:MAX_TARGET_NUMBER:A:1]
                [CDI:WAIT_PERIOD:50]
