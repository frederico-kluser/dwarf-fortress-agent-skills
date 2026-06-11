# Blowgun

> Fonte: [Blowgun](https://dwarffortresswiki.org/index.php/Blowgun) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*For a comparison of different weapons, see Weapon.*

A **blowgun** is a ranged weapon that fires projectiles called blowdarts. Blowguns can be fired incredibly quickly, though they are not very accurate and darts are lightweight. Blowgunners with higher skill and endurance can shoot at higher velocities. Blowguns are relatively rare, being used primarily by subterranean animal people.

As ranged weapons, blowguns use and train the blowgunner skill; as melee weapons, blowguns use and train the swordsdwarf skill, instead. Dwarves cannot normally forge blowguns nor darts, limiting supply to whatever low-quality specimens can be wrested from indigenous populations. During a strange mood, however, an aspiring yet misguided bowyer may create an artifact blowgun at a bowyer's workshop. Even if you do manage to get your hands on a blowgun, the severe lack of ammunition will make it nearly impossible to field an effective blowgun-dwarf. All dwarves can equip blowguns.

Units from other civilizations spawned as blowgunners are hardcoded to special behaviour. Unlike other ranged weapon users, they lack quivers, but their ammunition will be covered in any animal extract that is available to the civilization and causes an injected or contact syndrome. Currently, it is not possible for your dwarves to add a poison or toxin to a weapon without significant workarounds (and a bit of luck), making blowguns even more underwhelming.

## Bugs

- If a squad is assigned multiple ammo types, dwarves with "individual choice ranged" may carry the wrong ammoBug:1374.

    [ITEM_WEAPON:ITEM_WEAPON_BLOWGUN]
    [NAME:blowgun:blowguns]
    [SIZE:150]
    [SKILL:SWORD]
    [RANGED:BLOWGUN:BLOWDART]
    [AIM_DIFFICULTY:5]
    [LOADED:10:5]
    [INITIATE_SHOT_TIME:5]
    [SHOT_RECOVERY_TIME:0]
    [SHOOT_FORCE:100]
    [SHOT_FORCE_REQUIRES:ENDURANCE:1500]
    [SHOT_FORCE_REQUIRES:BLOWGUN:15]
    [SHOOT_MAXVEL:1000] I suppose you could blow harder and harder, but the force prevents it from getting out of hand.
    [TWO_HANDED:0]
    [MINIMUM_SIZE:5000]
    [MATERIAL_SIZE:2]
    [ATTACK:BLUNT:10000:4000:bash:bashes:NO_SUB:1250]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
