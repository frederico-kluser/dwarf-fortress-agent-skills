# Combat

> Fonte: [Combat](https://dwarffortresswiki.org/index.php/Combat) — Dwarf Fortress Wiki (GFDL/MIT)

*(This page*will'' cover the mechanics of combat - as they're all figured out. For now, you may want to refer to Combat skills, Armor and/or Weapons) for specific information on those aspects. The effects of many material properties on combat are somewhat understood (see the Material science page.

For a "How to", Military is the main article, or see Attack for the quick "right now!" version.)''

**Combat** in *Dwarf Fortress* is unlike that in most strategy and role-playing games. Rather than having hit points, units have a collection of body parts, such as limbs, head(s) and a torso. These have sub-parts: limbs have skin, fat, muscle, tendons, bones, nerves and arteries; heads have brains, eyes, noses, mouths, teeth and tongues; and torsos have internal organs. Damage to these parts and sub-parts causes various negative effects, such as fainting, vomiting, loss of mobility due to bone fractures or nerve damage, and eventually leading to death from organ failure or blood loss. The combat system tries to present a fairly realistic depiction of combat, with several important consequences.

Although creatures and players may direct and focus their attacks, combat is random in nature. A glancing blow can get lucky and damage a vital organ, or open an artery to cause massive blood loss. Weapons cause damage specific to their class, be they axes or swords or backpacks. You will often see creatures attacked with impaling weapons such as spears or crossbow bolts die of asphyxiation when their lungs are pierced, while slashing weapons are more likely to open an artery or lop off a limb, and blunt weapons will cause fractures. Some weapons may become stuck in the enemy: if the weapon wielder can maintain control he can continue to do damage and immobilize the enemy, but if the enemy gains control of the stuck weapon, the weapon's wielder will be disarmed.

Reading the combat eports will give you a gruesome blow-by-blow of the fighting, telling you exactly what each strike did. It is important to note that, while most natural creatures have the same sorts of vulnerabilities due to their similar collections of body parts, procedurally-generated creatures such as bogeymen, forgotten beasts and titans may lack these vulnerabilities entirely. Killing a shambling pile of refuse may prove to be a very, very long process due to the fact that it has no vital parts, and metallic creatures may prove to be nearly invulnerable. When all else fails, a cave-in or obsidian casting means certain death for anything caught in it.

As in real life, combat in *Dwarf Fortress* is chaotic, deadly, and gruesome. Numbers seem to matter, as defending against multiple opponents can be difficult, even for a decent fighter. Your warriors will not suffer loss of generic hit points, and cannot simply rest to regain them. Injuries must be dealt with in an appropriate fashion for healing to occur: broken bones must be set, wounds must be cleaned and stitched up, and for some things such as concussions, you can only wait and hope the victim eventually regains consciousness.

## General observations

- Blunt weapons use contact area, IMPACT_YIELD, IMPACT_FRACTURE and weapon mass to scale damage. As such, metal effective for blunt weapons are Adamantine 🡆 Copper 🡆 Iron 🡆 Bronze 🡆 Steel 🡆 Silver, from lowest to highest. It should be noted that steel is just about as effective as silver due to the impact values, as well as iron and copper. Higher contact area has higher potential damage but has a harder time getting through armor.
- Edge weapons use SHEAR_YIELD and SHEAR_FRACTURE for material strength. As such, metal effectiveness for edged weapons are Silver 🡆 Copper 🡆 Iron 🡆 Bronze 🡆 Steel 🡆 Adamantine, from lowest to highest.
- Edge weapons use contact area and penetration size to determine pressure. Lower contact area results in better ability to pierce armor, higher contact area increases the amount of tissue affected by an attack. Swords provide both, with slashing and stabbing; spears provide only low contact area, and axes only provide high.

### AI Behaviour

On seeing an enemy, military dwarves will rush towards their targets if they're able to path towards them.

#### Weapon attacks

During most fights, attacks are targeted at a specific body part with a specific weapon, based on a few factors.

In adventurer mode, during a fight, each turn generates an ease and squareness for each part on the target, based on relative positioning and current actions. If an auto-attack is made, the AI will take into account:

- A combination of the ease and squareness of the attack.
- Weapons at its disposal, including both held and natural weapons
- Body parts, such as the head, although this seems to be considered a low priority

The AI can also perform wrestling, including the use of locks, choke-holds, and even forcefully removing equipment, although wrestling attacks are usually uncommon when a weapon is equipped.

If the target is unconscious or immobilised, such as becoming exhausted or caught in webs, all strikes against that target will become perfectly accurate and perfectly squared, and the AI will always prioritise removing the helmet then striking the head.

Note that the AI does not seem to account for a body part's injuries - an already-disarmed hand or unusable leg can still be targeted, despite the presence of functional parts.

- Example: A goblin might suffer fatal upper spine injury from a blunt attack, rendering everything below their head useless - however, the dwarves will fail to recognise this and can continue to attack their body. This can result in dwarves becoming tired needlessly, increasing their own chances of death, especially in sieges.

The AI also sometimes forget to retrieve their weapon after it becomes lodged in a target's wound. While they can still block attacks with their weapon, they will stop using it to make an attack, unless they receive intervention, such as another dwarf killing their target or a tackle displacing them. This means even legendary weapon users can suddenly become useless mid-battle, and dispatching a small number of dwarves can be prone to reliability issues, especially if their weapon type becomes lodged often.

## General terms

**Stress** - Pressure = Force per area = F/A

**Strain** - Deformation of a solid due to stress = Stress/Elastic Modulus

**Yield Strength** is the amount of stress required to permanently deform (bend) a material (plastic deformation)

**Fracture Strength** is the amount of stress required to permanently break (rupture) a material

**Strain at yield** is the amount of deformation (bending) that occurs at the yield point

Implications to *Dwarf Fortress* Combat

## Armor properties

- Material Properties

:\* Blunt Protection

::\***Impact yield**

::\***Impact fracture**

::\***Impact strain at yield**

:\* Edge Protection

::\***Shear yield**

::\***Shear fracture**

::\***Shear strain at yield**

- Item Properties

:\***Armor Level**: Layer number in which armor is worn. Lower numbers will be equipped first, and later numbers equipped if space is available.

:\**'Coverage*: Some armor covers more of the body than others.

## Weapon properties

- Material Properties

:\*Common

::\***Contact Area**: Determines the surface area hit by the weapon. Likely in mm².

::\***Velocity Multiplier**: Effectively increases the velocity of the weapon swing.

:\*Blunt Weapons

::\*Blunt weapons are all about weapon mass, contact area, and velocity. Apply a large force to a small area for bone crushing goodness.

::\***Mass** is likely material **Density** times weapon **Size**

::\***Momentum** is **Mass** times **Velocity**

::\***Velocity** is based on the **Mass** of the weapon, the **Strength** of the wielder, and the **Velocity Multiplier** of the weapon

::\*Any impact must have a conservation of momentum, and thusly, impart the weapon's momentum to the target

::\***Stress** is the **Force** of the strike divided by the **Contact Area**

:::\*Material **Impact Yield** determines the **Stress** required to dent the armor (likely not used)

:\*Edged Weapons

::\*Edged weapons rely on a combination of size, mass, contact area, penetration depth, and velocity

## Attack speed

Attack speed is defined in the raws using the ATTACK_PREPARE_AND_RECOVER token. ATTACK_PREPARE_AND_RECOVER:3:3 means "3 ticks to prepare, 3 ticks to recover"; this is the usual, for most attacks. Some attacks, such as kicks, are slower, and some, such as many night creature attacks, are faster. These can also be affected by modifiers (see below).

## Other combat factors

- Both adventurer mode and fortress mode keeps track of which way a creature is facing, based on its last actions. Attacks from behind will have increased accuracy, especially if the target hasn't spotted the attacker yet.
- Movement speed plays an important role in melee combat, as it determines both dodging efficiency and opponent's accuracy. Creatures that are either prone or naturally slow (such as giant snails) will have a hard time dodging attacks, so breaking one of the opponent's legs is worth the effort.
- Creature size, especially relative to other combatants, has a considerable effect on combat. In addition to individual strength stats, larger targets hit with greater force, though whether this is absolute or relative to the target's size is uncertain. Charging and wrestling also favor the larger combatant.
- As of update 0.43.04 shakes and strong attacks will translate to other bodyparts. For example if you hit an enemy in the head with a blunt weapon, the force from that attack may also hurt the neck of the enemy. Even if the attack is blocked by armor, the force of the blow can still damage other bodyparts.
- Attacks can have modifiers that affect their speed and properties: heavy attacks increase the prepare and recover time, but have a higher velocity; precise attacks nearly double the prepare time, but have much higher accuracy; quick attacks reduce prepare and recover to about 2/3, but have lower velocity; wild attacks are slightly faster in preparation and have higher velocity, but lower accuracy and take significantly longer to recover.
- Only wild attacks are usable by berserk creatures.

## Arena test results

- See Material

## Adventurer mode

[TABLE]

Combat is the fine art of using physical force to cause injury and death, and it is particularly fun in *Dwarf Fortress*.

See Adventurer mode gameplay#Party members for information on switching characters and using tactical mode.

### Defense

Defense is very important in *Dwarf Fortress*. Lucky attacks can kill instantly, and the only way to heal is to pass time (which can be done with fast travel, sleeping, or actual waiting) and some damage can not be healed. The main methods of defense are armor, dodging, shields, and parrying attacks.

Defense can happen either automatically, or manually using the im attack menu. Manual defense is more likely to succeed, but prevents you from attacking (except for multi-attacks, but defense is tricky with those). The relative skill levels of attacker and target also affect the chances of success - a master swordsman is more likely to hit a novice dodger than a master dodger, for example. Also, see the Combat preferences section below for information on how those can affect defense.

Armor has a chance to automatically deflect an attack that targets a body part covered by it. So, getting as much coverage as possible is important, as is having more layers of protection. The armor user skill is also very important as otherwise worn armor will greatly slow the wearer down.

Each attack on you has a chance of being dodged automatically depending on your dodger skill level. You can also dodge manually in the im attack menu by selecting any creature and choosing dodge. You then pick a direction, and your character will move one tile in that direction, possibly avoiding any number of attacks. Tiles that have a creature standing in them or some other blocking object cannot be dodged into. It is not clear whether choosing a specific creature increases the chance to dodge their attack or if choosing any creature will result in the same chance to dodge all attacks.

Each held shield has a chance to block most attacks, including breath attacks, and each held weapon has a chance to parry other weapon attacks, including projectile attacks (very rarely). Blocking and parrying can also be attempted manually in the im attack menu. There you can see adjacent creatures and any attacks they are attempting. This may include how soon the attack will happen depending on observer skill level. You can then pick a creature and choose to attempt to parry or block their attack. If several attacks are incoming, you can either manually defend against the soonest attack hoping for time to defend against the others or against the most dangerous hoping the other attacks are defended automatically.

The defensive options in the im attack menu do not have fixed keys because their position can change if one or more is impossible. You can't block without a shield, parry without a free weapon, or dodge while in a wrestling hold.

Offense can also sometimes be used defensively. Using Wrestling grabs, incoming attacks can be interrupted and opponents disarmed.

Note that you can dodge even if you are not being attacked. Also, despite being in an attack menu the defensive options will not escalate the conflict level. So, you can dodge away from a friendly creature without it counting as an attack.

### Weapons

Weapons are divided into specific weapon skills. Also, any item held in a grasp (usually a hand) can be used as a weapon and will use the Miscellaneous object user skill. This includes shields. Mining picks are an exception in that they use the Miner skill.

Weapons can become stuck in wounds after an attack - this will make the weapon unavailable for aimed attacks. There are multiple ways to free them. The most reliable is by nteracting with the weapon in inventory, choosing the weapon, and choosing the option. Other ways include; doing a non-aimed attack can free up a stuck weapon (but if you're holding multiple weapons this isn't certain to work); moving from your current tile (exposing your back or flank to the enemy is not recommended); moving the enemy from their *own* tile by wrestling throw or charging attack; or jumping into the enemy.

Most creatures have body parts that can be used as weapons; hands, nails, feet, and mouths are common. These allow the creature to punch, scratch, kick, and bite, which use the Striker, Kicker, and Biter combat skills. Creatures with other body parts may have an added attack with those; horns or tusks add gore attacks, for example. Creatures may also have attacks as natural abilities or acquired powers which can be used with then or . is a common ability, but is not very effective.

The entire body can also be used as a weapon by umping into or through the tile a creature is in. Usually they will dodge, but that might be useful around dangerous terrain. If it does hit, they may be sent flying depending on your relative masses. This can be useful for crowd control or knocking enemies into pits. Having your weapon stuck in them seems to increase the chance of hitting them.

### Melee attacks

Hostile creatures can be attacked using a non-aimed attack by simply moving towards your enemy using the movement keys. A hostile creature in the same tile as you can be attacked with . The specific type of attack can be influenced by the combat preferences and may be influenced by the character's skill level for each type of attack.

Any visible creature can be attacked by standing next to it and pressing . Attacking some creatures will require a confirmation, given using +. This can be because they're friendly (which includes wild animals for elves), unconscious, or have yielded. This menu also has wrestling and defensive options.

The first option is to make an **aimed attack**. You first select the body part that you want to attack, then the type of attack. There are several options below the attack type menu. **Quick attacks** are faster than regular attacks but weaker. **Heavy attacks** are slower but hit harder. **Wild attacks** are faster and hit harder but are inaccurate. **Precise attacks** are very slow but are much more likely to hit. **Multi-attacks** allow you to attack several times in a row, at a great cost to the effectiveness of any one of the chosen attacks.

Some options may be marked with a , this indicates an attack of opportunity which has a greatly increased chance of effectiveness, but only applies to a specific attack type. Selecting a body part with one of these will then show which type of attack it is. A or indicates that there is a on another page. The keys to change the page are shown above the list, and by default. Even if one of these doesn't target an important body part or uses a weaker attack, if successful they can cause significant pain which may give you an advantage.

Some options may also be marked with one of , , , or , these indicate normal attacks that are better () or worse () than average.

Look at the difficulty rating for various possible attacks. Impossible attacks will be nearly impossible to land and Easier attacks will be very easy to land. The difficulty rating for an attack does not change depending on your weapon skill. Based on player experiences, a Grand Master weapon user can almost always land a "Tricky" strike, while a Novice generally cannot. Attacks on various locations will also have limits on how "squarely" they can land (due to being out of reach, for example). Square and very square attacks will deal more damage. Attacks which "can't land squarely" are generally still effective.

When your target is unconscious all attacks will be .

Attacks aimed at an unarmored head are the most effective; a single attack to the cranium with a weapon will usually put an end to the fight. Aimed attacks are especially useful for dismembering opponents. Opponents who are missing a foot will fall over, thereby greatly lowering their speed, and giving you an immediate edge in the fight. Cutting off both hands is also highly recommended for obvious reasons. After all, a field full of armless, one-legged enemies can be a big experience booster for your character and your companions. Damage to the lower body can cause nausea on most mundane creatures which is a major debuff for them. (They can also rarely geld male creatures, but that has no other combat effect.)

Aimed attacks are also especially helpful when fighting giant beasts. Some enemies like giant desert scorpions have lots of redundant body parts, and random attacks waste valuable time on low priority areas while the scorpion is busy injecting venom into the whole party. Lastly, aimed attacks allow you to grab trophies that are not available via butchering. For example, a minotaur's horns can be cut off during a fight, but since it's a humanoid, most adventurers will refuse to butcher its corpse after the fight. However, in DF2014, all butcherable corpses are able to be butchered, as long as the corpse isn't too mangled.

### Ranged attacks

To attack with a ranged weapon press the key with a ranged weapon (bow, crossbow, etc.) equipped on one hand and select the square where you want to attack. Note that you need to have some sort of ammo, corresponding to the type of ranged weapon you are using (for example, bows use arrows, crossbows use bolts). Otherwise, a message stating "You have nothing left to fire." is displayed in brown. Similarly use the key to throw any random object in the same manner. Random objects appear to make a random attack if they happen to have more than one possible type. For example, if you throw a sword it may hit with a blunt impact, a stabbing impact, or a slicing impact. Throwing crossbow bolts with sufficient throwing skill and strength seems to have an effect similar to firing them, although less powerful. On the plus side, you will never lose ammo if you throw it.

It is not possible to aim for specific body parts with ranged or thrown attacks.

hrowing is generally a good skill to have for any adventurer, as it allows you to slow down fleeing foes, both on the ground and in the air without the need of equipping a (cross)bow. Just like ooking, you can use throwing to view and hit enemies multiple Z levels away from you. If you're lucky, you can simply land a hit that causes the flying enemy to give in to pain, and then let gravity do the rest of the work. Even if the fall doesn't kill them, they will most likely be stunned long enough for you to run up and slaughter them.

### Wrestling

*Main article: Wrestling*

**Wrestling** (grappling) can be performed by selecting an enemy via followed by to wrestle. You can wrestle any enemy. Wrestling works somewhat like a targeted attack: Once you grab a creature by some body part, you may be able to make another wrestling attempt that will allow you to perform a throw or takedown. For a detailed list of moves, such as takedowns, throws, choke holds, etc., see Wrestling.

### Wounds

If you get wounded during combat, you can try to yield or flee - or both - before you get more wounded.

To yield, press . This will be less effective if you continue to hold a weapon, so drop any with . Putting them away with or may also work. You can also ask them to cease hostilities with . However, depending on the hostility level of the conflict and possibly the personality of your enemy, they may continue to attack you.

If you choose to flee, you can increase your movement speed with . Be aware that movement speed while stunned, nauseous or winded is reduced, and might leave you open to fatal blows. If you are next to a creature, manually dodging using the im attack menu may be faster than using the movement keys and will likely avoid more attacks.

Your wounds will heal over time, so just fast travel or sleep in a safe place. Some wounds may never heal, however, leaving you permanently crippled. Obtaining a crutch may help with this. Or, if you are not already a vampire, you can get bitten by a werebeast during full moon, which will heal all injuries once per month. Rolling divination dice can also result in a transformation or direct healing, though such magical healing seems to also have limits.

If you have some bolts or arrows stuck in your body, they can be removed by using the complex nteraction menu. Select the stuck bolt or arrow from the list and then pull it out with . You'll probably start bleeding after you pull it out, but the bleeding is rarely anything to worry about.

### Combat preferences

At any time during gameplay (except in fast travel mode), you can press to open the Combat Preferences menu. There are three different preferences you can set: Attack, Dodge and Charge Defense. These have a few different sub-preferences each:

- **ttack**
  - **According to Opponent** - The default setting. When set to this, charging happens more or less frequently, depending on the difference in size between you and the opponent. Bigger opponents get charged less, smaller more often. Can be very risky, since a random charge against a huge opponent is likely to get you knocked down and stunned. In the same vein, charging when close to obstacles or other environmental hazards is very dangerous, potentially fatal, if the enemy dodges you.
  - **Strike** - This setting ensures that you never charge an opponent, but rather just swing your weapon at them. This carries less risk than the above, but you're never going to knock anyone down without hitting their legs or spine. Very preferable against large opponents.
  - **Charge** - When set to this, you ALWAYS charge. When faced with numerous small enemies (Bogeymen in particular), this can be extremely useful, but remember to switch back when facing something bigger. Charging a large dragon is almost a certain death sentence.
  - **Close Combat** - With this setting, all your auto-attacks are grapples. Generally not very useful, since the random nature of it tends to prevent you from actually doing any damage with it, but if you continually auto-attack a harmless creature with it, your wrestling-skill will be legendary in no time.

- **odge**
  - **Move Around** - This means you can jump away from attacks, physically moving in a random direction. While this lets you dodge attacks more often, it can also result in you jumping into a wall or lake. If you're fighting in really tight spaces, or areas with large pits, you might want to switch to the other option.
  - **Stand Ground** - As can be expected, you stand your ground. No jumping around, which is useful in the above situation, but risky in the open. If you have room for jumping around, go with Move Around, but otherwise this could be a good idea.

- **harge Defense**
  - **According to Opponent** - Again, the default setting. You're more likely to stand still against small enemies charging, but will probably prefer moving away from larger ones. Somewhat risky, in that even a somewhat small enemy can stun you by charging.
  - **Dodge Away** - With this, you'll dodge away from charging enemies, if you can. It's not a sure bet, but it's very much worth it against enemies who like to charge. This is probably the most preferable mode, since you're not losing a whole lot by dodging a small foe charging, but dodging an angry night beast can save you from a world of pain.
  - **Stand Ground** - If you're certain of your physical superiority to the opponent, you can safely choose this. Standing your ground like a real man/woman might feel hardcore, but getting knocked down in a fight can be extremely dangerous. It probably has some use against bogeymen though, since they're quite small. If you really are much bigger than the enemy, you'll end up knocking THEM down. Most of the time though, charges heavily favor the attacker, so dodging away is probably preferable.

Using the Combat Preferences properly can actually save your hide, so they're worth fiddling with. Just don't forget that you've fiddled with them, since a misplaced charge or dodge could end up killing you.
