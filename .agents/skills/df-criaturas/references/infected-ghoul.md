# Infected ghoul

> Fonte: [Infected ghoul](https://dwarffortresswiki.org/index.php/Infected_ghoul) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Infected ghouls** `Ñ` are a type of undead night creature created by necromancers who can spread their condition through their bites. Like victims of werebeasts, a creature bitten by a ghoul will become infected with their contagion - should the initial bite break the skin - turning them against their allies almost instantly.

Ghouls are essentially artificially created husks/thralls, being extremely physically strong and tough, fearless, and immune to a number of status effects, such as stunning or becoming winded due to injuries. Pulping/mangling and blood loss seem to be the only reliable ways to put them down without resorting to atom smashers or cages, and are sometimes a part of assaults launched by necromancers. Additionally, some experiments may sometimes be turned into ghouls, magnifying their already often-formidable forms further. Some intelligent undead may be given the ghoul nomenclature, such as "cursed ghoul" or "doomed ghoul", but will have no connection to infected ghouls.

Additionally, historical figures infected by ghouls may arrive as visitors. They may proceed to either attack, or stand and glare menacingly at your livestock, should they happen upon it while going to whatever location attracted them (these behaviors are presumably bugs.) Visiting ghouls may also behave entirely normally, even participating in the intrigue system.

Graphically, ghouls will appear as humanoids with crimson red skin.

    Example raws (as extracted from world.sav in version
    0.47.04
    )

    [INTERACTION:SECRET_GHOUL_8]
        [GENERATED]
        [EXPERIMENT_ONLY]
        [I_SOURCE:EXPERIMENT]
            [IS_HIST_STRING_1: infected ]
            [IS_HIST_STRING_2: with a contagious ghoulish condition]
            [IS_TRIGGER_STRING_SECOND:have]
            [IS_TRIGGER_STRING_THIRD:has]
            [IS_TRIGGER_STRING:been infected with a contagious ghoulish condition]
        [I_SOURCE:ATTACK]
            [IS_HIST_STRING_1: bit ]
            [IS_HIST_STRING_2:, passing on the ghoulish condition]
        [I_TARGET:A:CREATURE]
            [IT_LOCATION:CONTEXT_CREATURE]
            [IT_AFFECTED_CLASS:GENERAL_POISON]
            [IT_FORBIDDEN:NOT_LIVING]
            [IT_CANNOT_HAVE_SYNDROME_CLASS:WERECURSE]
            [IT_CANNOT_HAVE_SYNDROME_CLASS:VAMPCURSE]
            [IT_CANNOT_HAVE_SYNDROME_CLASS:DISTURBANCE_CURSE]
            [IT_CANNOT_HAVE_SYNDROME_CLASS:RAISED_UNDEAD]
            [IT_CANNOT_HAVE_SYNDROME_CLASS:RAISED_GHOST]
            [IT_CANNOT_HAVE_SYNDROME_CLASS:GHOUL]
            [IT_MANUAL_INPUT:victim]
        [I_EFFECT:ADD_SYNDROME]
            [IE_TARGET:A]
            [SYNDROME]
                [SYN_CONCENTRATION_ADDED:1000:0]
                [SYN_CLASS:GHOUL]
                [CE_FLASH_TILE:TILE:165:4:0:1:FREQUENCY:2000:1000:START:0:ABRUPT]
                [CE_DISPLAY_NAME:NAME:plague thrall:plague thralls:plague thrall:START:0:ABRUPT]
                [CE_ADD_TAG:NO_AGING:NOT_LIVING:OPPOSED_TO_LIFE:EXTRAVISION:NOEXERT:NOPAIN:NOBREATHE:NOSTUN:NONAUSEA:NO_DIZZINESS:NO_FEVERS:NOEMOTION:PARALYZEIMMUNE:NOFEAR:NO_EAT:NO_DRINK:NO_SLEEP:NO_PHYS_ATT_GAIN:NO_PHYS_ATT_RUST:NOTHOUGHT:NO_THOUGHT_CENTER_FOR_MOVEMENT:NO_CONNECTIONS_FOR_MOVEMENT:START:0:ABRUPT]
                [CE_REMOVE_TAG:TRANCES:MISCHIEVOUS:START:0:ABRUPT]
                [CE_SPECIAL_ATTACK_INTERACTION:INTERACTION:SECRET_GHOUL_8:BP:BY_CATEGORY:MOUTH:BP:BY_CATEGORY:TOOTH:START:0:ABRUPT]

    [INTERACTION:SECRET_GHOUL_10]
        [GENERATED]
        [EXPERIMENT_ONLY]
        [I_SOURCE:EXPERIMENT]
            [IS_HIST_STRING_1: infected ]
            [IS_HIST_STRING_2: with a contagious ghoulish condition]
            [IS_TRIGGER_STRING_SECOND:have]
            [IS_TRIGGER_STRING_THIRD:has]
            [IS_TRIGGER_STRING:been infected with a contagious ghoulish condition]
        [I_SOURCE:ATTACK]
            [IS_HIST_STRING_1: bit ]
            [IS_HIST_STRING_2:, passing on the ghoulish condition]
        [I_TARGET:A:CREATURE]
            [IT_LOCATION:CONTEXT_CREATURE]
            [IT_AFFECTED_CLASS:GENERAL_POISON]
            [IT_FORBIDDEN:NOT_LIVING]
            [IT_CANNOT_HAVE_SYNDROME_CLASS:WERECURSE]
            [IT_CANNOT_HAVE_SYNDROME_CLASS:VAMPCURSE]
            [IT_CANNOT_HAVE_SYNDROME_CLASS:DISTURBANCE_CURSE]
            [IT_CANNOT_HAVE_SYNDROME_CLASS:RAISED_UNDEAD]
            [IT_CANNOT_HAVE_SYNDROME_CLASS:RAISED_GHOST]
            [IT_CANNOT_HAVE_SYNDROME_CLASS:GHOUL]
            [IT_MANUAL_INPUT:victim]
        [I_EFFECT:ADD_SYNDROME]
            [IE_TARGET:A]
            [SYNDROME]
                [SYN_CONCENTRATION_ADDED:1000:0]
                [SYN_CLASS:GHOUL]
                [CE_FLASH_TILE:TILE:165:4:0:1:FREQUENCY:2000:1000:START:0:ABRUPT]
                [CE_DISPLAY_NAME:NAME:diseased ghoul:diseased ghouls:diseased ghoul:START:0:ABRUPT]
                [CE_ADD_TAG:NO_AGING:NOT_LIVING:OPPOSED_TO_LIFE:EXTRAVISION:NOEXERT:NOPAIN:NOBREATHE:NOSTUN:NONAUSEA:NO_DIZZINESS:NO_FEVERS:NOEMOTION:PARALYZEIMMUNE:NOFEAR:NO_EAT:NO_DRINK:NO_SLEEP:NO_PHYS_ATT_GAIN:NO_PHYS_ATT_RUST:NOTHOUGHT:NO_THOUGHT_CENTER_FOR_MOVEMENT:NO_CONNECTIONS_FOR_MOVEMENT:START:0:ABRUPT]
                [CE_REMOVE_TAG:TRANCES:MISCHIEVOUS:START:0:ABRUPT]
                [CE_SPECIAL_ATTACK_INTERACTION:INTERACTION:SECRET_GHOUL_10:BP:BY_CATEGORY:MOUTH:BP:BY_CATEGORY:TOOTH:START:0:ABRUPT]
