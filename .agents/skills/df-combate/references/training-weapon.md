# Training weapon

> Fonte: [Training weapon](https://dwarffortresswiki.org/index.php/Training_weapon) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Training weapons** are edgeless wooden weapons created at a carpenter's workshop. There are three kinds available; axes, spears, and swords.

Dwarves won't harm each other (or themselves) during combat drills, or sparring while using metal weapons, so training weapons are only useful for actual "training" when you have no metal weapon of the kind you'd like your soldiers to train with, and in a few specific circumstances.

Training weapons are virtually useless in combat, so make sure that your soldiers have exchanged them for real weapons before sending them into battle, even if it means using a weapon they are totally unfamiliar with. Their utter uselessness can prove useful for live training, however.

Note that soldiers equipped with training weapons for extended periods of time can grow attached to their worthless wooden weapons. Congratulations - you now have a legendary stick.

Training weapons may also be used as non-lethal equipment for your fortress guard, to avoid them seriously wounding or killing criminals, including mandate violators. Though it is unclear how often this happens in *Dwarf Fortress* v50.

Training weapons can be useful in weapon traps if used creatively. Although they will only rarely even bruise a target, each weapon (max 10/trap) will trigger a "dodge" attempt, often inviting the target to step into a tile adjacent to the trap. If that tile, for example, has no floor for 10 z-levels, or is over magma, then the weapon has done its job.

Additionally, training spears can be used in upright spike traps, which is a useful design for a danger room. Use the least-dense wood available for extra safety (unless you want to train medical skills).

Training axes cannot be used for cutting down trees.

    Training axe raws

    [ITEM_WEAPON:ITEM_WEAPON_AXE_TRAINING]
    [NAME:training axe:training axes]
    [SIZE:800]
    [SKILL:AXE]
    [TWO_HANDED:47500]
    [MINIMUM_SIZE:42500]
    [MATERIAL_SIZE:4]
    [ATTACK:BLUNT:30000:6000:hack:hacks:NO_SUB:1250]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
    [ATTACK:BLUNT:30000:6000:slap:slaps:flat:1250]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
    [ATTACK:BLUNT:100:1000:strike:strikes:pommel:1000]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
    [TRAINING]

    Training spear raws

    [ITEM_WEAPON:ITEM_WEAPON_SPEAR_TRAINING]
    [NAME:training spear:training spears]
    [SIZE:400]
    [SKILL:SPEAR]
    [TWO_HANDED:47500]
    [MINIMUM_SIZE:42500]
    [MATERIAL_SIZE:3]
    [ATTACK:BLUNT:200:10000:stab:stabs:NO_SUB:1000]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
    [ATTACK:BLUNT:10000:6000:bash:bashes:shaft:1250]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
    [TRAINING]

    Training sword raws

    [ITEM_WEAPON:ITEM_WEAPON_SWORD_SHORT_TRAINING]
    [NAME:training sword:training swords]
    [SIZE:300]
    [SKILL:SWORD]
    [TWO_HANDED:37500]
    [MINIMUM_SIZE:32500]
    [MATERIAL_SIZE:3]
    [ATTACK:BLUNT:20000:4000:slash:slashes:NO_SUB:1250]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
    [ATTACK:BLUNT:50:2000:stab:stabs:NO_SUB:1000]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
    [ATTACK:BLUNT:20000:4000:slap:slaps:flat:1250]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
    [ATTACK:BLUNT:100:1000:strike:strikes:pommel:1000]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
    [TRAINING]
