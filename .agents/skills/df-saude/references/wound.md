# Wound

> Fonte: [Wound](https://dwarffortresswiki.org/index.php/Wound) — Dwarf Fortress Wiki (GFDL/MIT)

**Injuries** can be sustained to limbs and organs via the environment or fighting. There are five different levels of injury in the game, ranging from none to complete part loss - shown using the default colors, they are as follows:

*(The color of wounds can be changed in d_init.txt.)*

For ways to diagnose and treat injuries, see health care.

## Wound effects

**Brain**: Any structural damage results in instant death. A bruise which doesn't cause can be survived, and the creature suffers no effect from the injured brain and lives as normal.

**Throat**: The throat has a major artery, much like the heart. Bruising damage to the throat has no special effect, however any structural damage can "open a major artery in the throat", producing the same bleeding as a torn heart.

**Eyes**: Eye damage causes loss of sight, limiting creature perception.

**Mouth/nose/ears/cheeks**: No special effect.

**Teeth**: Fewer teeth to use for biting attacks.

**Lungs**: Damage to one lung interferes with breathing. Creature toughness affects how well it can survive with impaired breathing. Damage to both lungs simultaneously almost always results in suffocation. Bruises to the lungs can cause so they impair breathing; though they heal much more quickly than a torn lung, two simultaneous bruised lungs with function loss can be fatal (in adventurer mode party members can heal them by raveling).

**Heart**: Any structural damage causes massive, fatal bleeding. The heart itself isn't required for life—it is the extreme bleeding that causes death when the heart is pierced. As such, a bruised heart causes no ill effects.

**Pancreas/liver**: No effect. While it is reasonable to assume that the dwarven liver has evolved to be completely indestructible, liver damage doesn't cripple anything else either. Dwarves have a larger liver than any other sapient species, causing them to suffer liver damage more often, as it is easier to hit.

**Guts**: Damage to the guts causes great pain and nausea. Creatures will vomit and then retch repeatedly, depending on how much damage was caused. This slows down the creature and can dehydrate them. When the guts are pierced, they may spill out of the wound. This is visible as a gray "~" trailing behind the creature. This causes a lot of bleeding and exposes the guts themselves as a target for aimed attacks. Slicing off the exposed guts causes heavy bleeding, and almost always death. The cut-off guts can then be picked up and used as a weapon.

**Spinal injuries**: Attacks to the spine that also tear nervous tissue are extremely serious. Lower spinal injuries permanently disable the creature's legs - they can no longer stand or kick. Upper and middle spinal injuries disable every limb in the body, rendering the creature unable to do anything except use the default "push" attack, bite if it still has teeth, and move very slowly. It also disables every organ in the body besides the brain. As this disables the lungs, upper spine injuries will generally cause suffocation within a few turns. However, a broken bone in the spine does **not** cause irreparable damage - only damage to the nervous tissue does. If a dwarf suffers a broken bone in the spine without any nerve damage, just get them a cast and it will eventually heal.

**Gelding**: Attacks to the lower body (or, theoretically, anywhere else where the 'geldables' may be kept) of a geldable creature (including male dwarves) can very rarely result in a "gelding strike." In addition to the expected effects of bleeding and pain, this renders the creature permanently incapable of reproducing, just like non-combat gelding.

## Pain

Injuries cause pain; and excessive pain will knock your dwarves unconscious from the shock.

How pain works:

- Bruising causes 1× the pain value from the raw files
- Partially damaged tissue causes 2× pain
- Broken tissue causes 3× pain
- Having 150+ pain causes unconsciousness.
- Pain is independent of body part size

Most tissue has \[PAIN_RECEPTORS:5\], except bone, which has \[PAIN_RECEPTORS:50\]. So being punched in the guts (bruising skin, fat, muscle, guts) causes 20 pain and some nausea. Having any bone broken causes 15+50×3=165 pain (presuming bruised skin, fat, muscle). Having good stats presumably causes the pain to recede quickly, but that won't cause your character to wake up sooner after they fall unconscious.

Missing body parts no longer produce pain, so a completely severed limb or digit will cause no pain. Without breaking a bone, a creature would have to have three layers bruised on about ten different body parts, or three layers broken on about four, to collapse from pain (and edged weapons often damage sensory nerves, reducing pain).

## Miscellaneous injuries

(Miscellaneous injuries include generic tears, cuts and breaks that don't target a specific organ.)

Attacks that shatter nail or horn generate a cosmetic injury report, but otherwise have no effect unless they become infected. Similarly, attacks that tear hair have no ill effects, but hair damage is common during chokeholds on animals, such as a lion's mane being damaged by a chokehold.

Injuries that only tear skin tend to cause little bleeding and light scarring, while injuries that tear fat layers cause worse bleeding and severe scarring but little pain. Injuries to muscle layers can sometimes cause the affected limb to become unusable. This happens when a tendon, ligament, or motor nerve is severed, or if the limb reaches . If the muscle is in an arm and loses function, items held in that hand will be dropped. Damaged leg or foot muscles may cause the creature to fall over and be unable to walk until the injury heals. Damage to sensory nerves eliminates pain in the body part, and may reduce attack strength using that part.

Bone damage causes extreme pain, especially if the bone is fractured or broken. Those are the most painful injuries in *Dwarf Fortress*, and will almost invariably cause unconsciousness from the pain. A bone that is broken in a limb will render that limb inoperative. Bones that are hit hard enough may shatter and be jammed into the muscles in their body part, or nearby bones and body parts, causing far more damage - this is most notable with the skull. A hard hit (or any hit) to the skull that causes a fracture can force the broken part into the brain, causing immediate death. A broken arm may be jammed into the shoulder as well, breaking it, and broken bones sometimes tear the muscles around them, causing bleeding.

In recent versions the neck is appended to the upper body, and the head is appended to the neck (which is why you have to press "d" now to target the head, and "c" is the neck - the neck must be defined first). You can't hurt the upper spine directly by attacking the head anymore, though very powerful attacks can damage adjacent body parts by "twisting" them, so an extremely strong attack to the head or one of its parts can damage the upper spine by twisting the neck.

- Having the upper spine (in the neck) torn in 0.40.xx disables everything and causes suffocation.
- Having the middle spine (in the upper body) torn disables everything and causes suffocation.
- Having the lower spine (in the lower body) torn paralyzes the legs, preventing kicks and negating pain in the legs and in the lower spine itself.

Note that the bones in the spine being fractured does not cause paralysis, which occurs only when the nerves in the spine are torn.

If the neck is destroyed (pulped, broken, or cleaved), the upper spine will be destroyed as well.

## Missing limb

As the name implies, this signals that a limb has been completely severed. Dwarves with severed limbs frequently either die of blood loss, or linger in the hospital permanently. Those who recover may find themselves unable to perform the same tasks that they had done in the past.

Dwarves without arms are unable to haul items, but are still able to gather crops or work in a workshop. Once created/gathered, the items simply remain where they are until another dwarf comes along to move them. They are also unable to equip armor/clothing, but this won't stop them from biting/kicking in combat. Armless dwarves are unable to operate screw pumps, and trying to dress or clean themselves often causes constant cancellation spam.

## Function loss

The cyan "Function loss" signals impairment of an organ for which "broken" or "bruised" would not make sense. Internal organs and eyes have been observed to turn cyan, indicating failures of sight, liver function, and other maladies.

A dwarf can also suffer nervous damage to sensory and/or motor nerves. For example, motor nerve damage to a leg means that the dwarf will never be able to stand up again, which will show as "Ability to stand lost" in the dwarf's personal health screen, in addition to nervous damage information. Sensory nerve damage causes pain to disappear and is thought to make a creatures' attacks weaker. With a crutch applied, dwarves with leg nerve damage can become mobile / useful again. Damage to spinal nervous tissue disconnects all nervous function below the damaged point. For the upper and middle spines this can include the lungs, so damage leads to suffocation.

Creatures can be set to heal spinal nerve damage by going into the raws, finding the tissue_template_default and setting a number like \[HEALING_RATE:100\] at the NERVE_TEMPLATE. A higher number translates to a slower healing rate, with bones for example having a healing rate of 1000. However, this setting does not affect non-spinal nerves, as they do not count as "nervous tissue".

## Scarring

Dwarves who sustain major injuries may never fully heal – the part will always remain listed in their Wounds section as "Minor" or "Inhibited", and the dwarf's description in their Thoughts and Preferences screen will note that they bear scars of varying degrees and types, e.g., (Tiny, very short, short, long, very long, massive, huge, etc.); (Jagged, Dent, Straight, etc.). While not all scars have an effect, this may result in notes in the Health screen such as "Ability to grasp somewhat impaired". This means that one of the creature's grasping parts (usually hands) has lost the ability to grasp. Military dwarves with inhibited ability to grasp will not hold a weapon or shield in the crippled arm. However, they will automatically grasp both weapon and shield in their good hand when they next come to equip themselves, assuming, of course, that they are set to use both such items.

## Permanent injury

There are several types of injuries that dwarves will never recover from - nerve damage is permanent, as is loss of limbs, while some types of syndromes are lifelong. As a result, you may end up with a dwarf who has lost function in one or more body parts, or who continually exhibits some kind of problematic symptom. But these dwarves, if they don't meet with an unfortunate accident, can still be very useful.

### Function loss: legs

Dwarves who have lost the use of one leg cannot walk (or kick enemies in battle, but that's a minor problem). If the dwarf in question has had a foot or leg amputated, or has nerve damage to the leg, they can be issued a crutch by doctors in your hospital. Thereafter, they will gain crutch-walking skill whenever they move with the crutch in their inventories. Eventually,their speed with the crutch can become faster than it was before, due to the Agility gained each step and reduction of the movement penalty to 0. A dwarf using a crutch can go back to military duty without any loss of effectiveness; in fact, it is quite possible for a one-armed dwarf to hold a shield, crossbow, and crutch (and occasionally bash their enemies with it - it is recommended to make metal crutches to issue to military dwarves).

### Lower body paralysis

A dwarf who has nerve damage to their lower spine, or to both of their legs, is unable to use them and cannot benefit from using a crutch. After their recovery (you may need to deconstruct their hospital bed to get them out of it), they can move—but only very slowly. Dwarves like this are obviously unfit for military duty (other than as a marksdwarf who sticks to fortifications)—they can still swing a battle axe, but they won't make it to the battle before the rest of the squad have finished their jobs and have moved on to claiming the enemies' socks. The best jobs for these dwarves are ones that don't require them to move around much-for best results, create a burrow containing the dwarf's workshop, stockpiles for food and booze, and bedroom. Turn off all labors but the one you want the dwarf to do; most importantly, turn off hauling. A paralyzed dwarf can also be kept idle in your lever room, where they will still move five steps more quickly than another dwarf can move fifty; or they can be appointed as the broker and burrowed in your depot. You could also make such a dwarf a hammerer, with exemplary results.

No one has yet done Science on the possibility of using minecarts to transport paralyzed dwarves. Will your fort be the first?

### Function loss: arms

The dwarf who has lost the use of an arm can go on with their life normally, and can even hold a shield and battle-axe at the same time. In the military, they are limited only in that they cannot wield weapons that are too large to be wielded one-handed, and outside the military, they can work as well as any other dwarf.

Losing both arms is a different story. Dwarves who have lost the use of both arms will be unable to do almost any task. Even managers, bookkeepers, and brokers must be able to use at least one arm. They cannot pick up weapons or shields and cannot haul items. Most irritatingly, they cannot clean themselves, or pick up clothing in order to put it on, and will probably spam cancellation messages at you (seriously, consider turning off job cancellation messages in the 'o'rders menu if this is the case). These dwarves are at risk of insanity from the lack of clothing once their current set wears out, though they may have been lucky enough to be wearing armor, which will not wear out. Military dwarves can still lead demonstrations in non-weapons skills, and could quite possibly become a good wrestler or biter. Dwarves without arms can also be used as sentries; burrow them in watchtowers to spot ambushes.

### Blindness

A dwarf with both eyes damaged cannot see - and what they can't see, they won't be afraid of. Therefore, a blind dwarf can do civilian labors *without* dropping everything and running when there's a wild animal nearby. They will suffer a severe drop in the quality of their work, but this won't affect jobs whose products don't have a quality level, such as wood burning.

### Long-term syndrome

The most common long-term syndrome is probably the bite of a cave spider, which causes long-term mild dizziness. The dwarf seems fine and works normally, except that the work tends to be low-quality because the dwarf is feeling under the weather. Even legendary dwarves will, if they're feeling dizzy enough, be unable to produce masterwork crafts—assign these dwarves to producing goods that don't have quality levels.

## Adventure Mode

A wounded character in adventurer mode may be unable to use wounded limbs, or perform actions with them - a mangled arm, for example, cannot wield a sword. Wounds heal over time, but moving even one cell in fast-ravel mode will vastly speed up recovery, instantly healing all injuries that could heal over time. An adventurer with higher recuperation will heal faster than others. Some wounds, however, will never heal.

As with dwarves in fortress mode, missing limbs and nonfunctional nerves, blindness, and similar permanent injuries do not heal, no matter how much time passes. Lower-body paralysis can be especially dangerous, as the affected character can only crawl on the ground.

### Advanced healing

There are some events that heal normally permanent injuries:

- Getting a lucky roll on a divination die will heal some wounds.
- Undergoing a werebeast transformation heals all wounds, including paralysis. This is the only way in the game to restore lost limbs.
