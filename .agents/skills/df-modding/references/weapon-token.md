# Weapon token

> Fonte: [Weapon token](https://dwarffortresswiki.org/index.php/Weapon_token) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

\
**Weapon tokens** define weapons. These tokens can only be placed within an ITEM_WEAPON object definition, and most do not function in armor objects.

## Tokens

|  |  |  |
|----|----|----|
| Token | Arguments | Description |
|  NAME | singular / plural | Name of the weapon. Required. |
|  ADJECTIVE | adjective | Adjective of the weapon, e.g. the "large" in "large copper dagger". |
|  SIZE /  WEIGHT | size | Volume of weapon in mL or cubic cm. Defaults to 100. |
|  SHOOT_FORCE | value | The amount of force used when firing projectiles - velocity is presumably determined by the projectile's mass. Defaults to 0. |
|  SHOT_FORCE_REQUIRES | Attribute / or / skill token / value | Limits the force of fired projectiles based on the user's stats. For example, crossbows omit this token, while bows have `[``SHOT_FORCE_REQUIRES``:STRENGTH:1500]` and `[``SHOT_FORCE_REQUIRES``:BOW:15]`. |
|  SHOOT_MAXVEL | value | The maximum speed a fired projectile can have. |
|  AIM_DIFFICULTY | value | Higher values cause fired projectiles to be less accurate. |
|  LOADED/ NOCKED | maximum ticks / minimum ticks | Determines how long it takes to load ammunition into this weapon. An unskilled ranged weapon user takes the maximum / time / and a user with legendary skill in that ranged weapon takes the minimum time. Each level in the weapon's ranged skill reduces the loading time proportionally until the minimum time is reached. / LOADED ammo is / stored / inside the weapon, while NOCKED ammo stays inside the same inventory and remembers that it is nocked to the weapon. |
|  INITIATE_SHOT_TIME | value | Shooting this weapon takes this many ticks before the projectile is fired. |
|  SHOT_RECOVERY_TIME | value | After shooting this weapon, wait this many ticks to recover. |
|  SKILL | Skill token | The skill to determine effectiveness in melee with this weapon. Defaults to MACE. AXE skill will allow it to be used to chop down trees. MINING skill will allow it to be used for mining. Outsider adventurers (or regular ones with no points in offensive skills) will receive a weapon with the SPEAR skill, selected at random if multiple ones have been modded in. All adventurers will also start with a weapon using the DAGGER skill, again selected at random if multiple such weapons exist. |
|  RANGED | Skill token / Ammo class | Makes this a ranged weapon that uses the specified ammo. The specified skill determines accuracy in ranged combat. |
|  TWO_HANDED | size | Creatures under this size (in cm³, not including tissue layers) must use the weapon two-handed (or more if the creature has extra \[GRASP\] parts)\[Verify\]. Defaults to 50000. Below this size, one-handed use of a weapon will cause a penalty to hit. |
|  MINIMUM_SIZE | size | Minimum body size (in cm³, not including tissue layers) to use the weapon at all (multigrasp required until TWO_HANDED value). Defaults to 40000. |
|  CAN_STONE |  | Allows the weapon to be made at a craftsdwarf's workshop from a sharp (\[MAX_EDGE:10000\] or higher) stone (i.e. obsidian) plus a wood log. |
|  TRAINING |  | Restricts this weapon to being made of wood. |
|  MATERIAL_SIZE | value | Number of bar units needed for forging, as well as the amount gained from melting. Required. |
|  ATTACK_PREPARE_AND_RECOVER | Preparation time / Recovery time | Determines the length of time to prepare this attack and until one can perform this attack again. Values appear to be calculated in adventure mode ticks. |
|  ATTACK_FLAG_BAD_MULTIATTACK |  | Multiple strikes with this attack cannot be performed effectively. |
|  ATTACK_FLAG_INDEPENDENT_MULTIATTACK |  | Multiple strikes with this attack can be performed with no penalty. |
|  ATTACK | attacktype:BLUNT or EDGE / contact_area:value / penetration_size:value / verb2nd:string / verb3rd:string / noun:string / velocity_multiplier:value | You can have many ATTACK tags and one will be randomly selected for each attack, with EDGE attacks 100 times more common than BLUNT attacks. Contact area is usually high for slashing and low for bludgeoning, piercing, and poking. Penetration value tends to be low for slashing and high for stabbing, and is ignored if attack is BLUNT. Verbs are for the 2nd and 3rd person action verbs used to describe the attack. Noun describes what part of the weapon is being used in the attack, or NO_SUB for none. Velocity_multiplier is a multiplier for the attack momentum, increasing effectiveness; stab attacks use 1000 while the lash of a whip uses 5000. Required. |
