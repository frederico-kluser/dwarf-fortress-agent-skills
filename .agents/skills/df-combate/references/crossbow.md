# Crossbow

> Fonte: [Crossbow](https://dwarffortresswiki.org/index.php/Crossbow) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*See Weapon for a general overview of weapons and related information.*

**Crossbows** are the only native ranged weapon available to dwarves (although one can also acquire blowguns and bows through trading, or looting of failed sieges). While more difficult to set up than melee weapons, crossbows have the distinct advantage of allowing dwarves to fight at range, often killing enemies before they can enter melee distance. They are thus an excellent support weapon, especially if you have already filled out your ~~meat shields~~ melee squad(s).

## Production

Still has shaky aim.\
*Art by Kirill Nedorosol*

Crossbows can be made from a variety of materials, be they wood, bone or metal, which has no effect on accuracy or damage. The quality of a crossbow influences its accuracy (along with the skill of the marksdwarf), while the quality and material of the bolts influences the damage done on a successful hit.

|  |  |  |  |
|----|----|----|----|
| Material | Skill | Workshop | Consumed |
| metal1 | weaponsmith | metalsmith's forge | 1 bar |
| (ammo ×25) | weaponsmith | metalsmith's forge | 1 bar |
| wood2 | bowyer | bowyer's workshop | 1 log |
| (ammo ×25) | wood crafter | craftsdwarf's workshop | 1 log |
| bone | bowyer | bowyer's workshop | 1 / bone / off stack |
| (ammo ×5) | bone carver | craftsdwarf's workshop | 1 bone |

Notes:

1\) All materials perform equally well for a ranged weapon; a bone or wood crossbow shoots as straight and hard as a steel one (because once it hits, it's the bolt that does the damage!). However, if an enemy closes into melee range with a marksdwarf, then they will use their crossbow as a hammer, doing blunt damage (and using the Hammerdwarf skill). For this reason, you may want to make your military crossbows out of a metal\*, and leave any bone/wood crossbows for hunters or wall defenders, or as Trade items.

(\* For blunt-force weapons (including crossbows in melee): Steel seems to be *slightly* preferable for blunt weapon damage\*\*, but Iron, Bronze (including Bismuth Bronze), and Copper are all very close seconds. All are vastly superior to wood or bone for any melee purpose.)

(\*\* As is silver (due to its high density), but silver is not available as a choice for standard crossbow manufacture. Strange moods can produce any weapon of any metal.)

Similarly, metal bolts are far superior to wood/bone, with (in order) Steel, Iron or Bronze/Bismuth Bronze, and Copper being preferred, and Silver bolts a distant last against most any metal armor.

2\) For similar reasons, if you are going to use wooden crossbows, denser wood types are proportionally preferable to lighter ones for both crossbows and ammo, as a slight improvement over very bad.

## Ranged combat

Crossbows shoot bolts as their ammunition, and marksdwarves will engage targets up to 20 tiles distant, provided they have a clear line of sight to them. Z-levels up *or down* count equally *against* the distance when measuring this range, subtracting from the total x-/y-axis distance, so shooting from a high wall or tower effectively *reduces* that 20-tile maximum. Bolts may miss the target and fly a bit further than intended, potentially striking another foe, but **never** a friendly.

Unlike other ranged weapons, crossbows always fire at maximum force. They can fire accurate, high-power shots, though they take the longest to reload.

The material that the crossbows are made of is irrelevant to ranged combat (but see melee combat). Only the quality of the crossbow\[Verify\] and skill of the marksdwarf determine accuracy (i.e. whether a bolt hits the target or not), whereas the quality and material\* of the bolts determine the damage delivered to that target. If you have a skilled bowyer and are confident that your fortress design and/or your melee soldiers will keep your marksdwarves safe from enemy engagements, then you can arm your marskdwarves with high-quality wooden or bone crossbows, which will be just as accurate and deadly as metal crossbows (until melee proves necessary, that is).

(\* metal being better than bone being better than wood. See also superior metal for comments on different metal bolts vs. different metal armor.)

As can be expected, targets that are stationary are much easier to hit than those that are moving. Since marksdwarves can drop targets at range, they do a much better job taking down fleeing thieves and retreating goblin ambushes that your regular soldiers might not be able to catch.

## Melee combat

Nonetheless, marksdwarves that are approached by enemies will engage in melee combat with them, using the butt of their crossbows like hammers. Because of this it is useful to cross-train your dwarves with hammering skill, so that they will be better able to stand their ground in a fight, but a marksdwarf fighting a similarly armed and armored enemy with a melee weapon will usually lose either way. Focusing their training in defensive skills such as Blocking and Dodging is much more convenient, since it lets them at least hold off the enemy long enough to give a soldier more suited for melee combat a chance to surprise the enemy and dispatch them quickly.

In previous versions, the denser the material, the more damage a crossbow butt-strike would do in melee combat, simple. However, that difference has been largely limited in the current combat system. The different standard weapons-grade metals are now very closely equivalent for melee bashing attacks, but all metals are still far superior to the heaviest wood/bone. (See here for more discussion)

## Logistics

Crossbows require bolts and a quiver to fire, otherwise crossbows are used as hammers. Bolts are typically carried in quivers, which can be made of leather from leatherworking, obtained from caravans, or as goblinite.

When shot, one of two things will happen: either the bolt will shatter on impact with the ground or the target, or it will stay whole and, when all's said and done, be retrievable. This is a bit difficult, however, as shot bolts are automatically forbidden by default; in the orders screen, under \[F\]orbid, you can change it so that shot ammunition is automatically claimed. Otherwise, the easiest way to reclaim spent ammunition is to find them in the stocks screen and unforbid them.

Marksdwarves require an archery range with an archery target to be able to train.

## Hunting

Hunters use crossbows when hunting; migrant hunters automatically arrive with a free crossbow and a small number of bolts, and hunters will automatically pick one up from your ammunition stockpile when they go hunting, as well as the necessary quiver and bolts. Disabling the hunting labor will cause them to drop their weapon and equipment at the nearest applicable stockpile, and is absolutely necessary if you have embarked in a particularly fun location. Hunters usually give up on hunting if they run out of carried ammunition.

## Forging and melting

- Metal crossbows cost **one** metal bar to forge, or **three** adamantine wafers.
- When a non-adamantine metal crossbow is melted down, it will return **0.9** metal bars, for an **efficiency of 90%**.
- When an adamantine crossbow is melted down, it will produce **0.9** wafers, for an **efficiency of 30%**

## See also

- Crossbowman
- Archery
- Advanced marksdwarf training guide

|  |
|----|
| "Crossbow" in other / Languages / Dwarven / : / metul-egdoth / Elven / : / arifi-ramí / Goblin / : / sakor-uneg / Human / : / om-ethro |

    [ITEM_WEAPON:ITEM_WEAPON_CROSSBOW]
    [NAME:crossbow:crossbows]
    [SIZE:400]
    [SKILL:HAMMER]
    [RANGED:CROSSBOW:BOLT]
    [AIM_DIFFICULTY:2]
    [LOADED:30:7]
    [INITIATE_SHOT_TIME:1]
    [SHOT_RECOVERY_TIME:0]
    [SHOOT_FORCE:1000]
    no shot force requirements
    [SHOOT_MAXVEL:200]  This is just to make sure a near-weightless object doesn't go faster than the string could possibly go.
    [TWO_HANDED:0]
    [MINIMUM_SIZE:15000]
    [MATERIAL_SIZE:3]
    [ATTACK:BLUNT:10000:4000:bash:bashes:NO_SUB:1250]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
