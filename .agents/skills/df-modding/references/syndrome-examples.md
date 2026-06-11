# Syndrome examples

> Fonte: [Syndrome examples](https://dwarffortresswiki.org/index.php/Syndrome_examples) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

This page was created to aid those looking to create new syndromes. Those familiar with syndrome design (and certain complexities in particular) should feel free to add helpful/obscure information to the lists below to help less-experienced members of the community with their syndromes.

The syndromes on this page can be applied through interactions, as creature actions, curses, blessings, or secrets, or through substances, including injected venoms, contact effects, or ingested foods. Examples on this page should operate the same regardless of application method.

## General Tips

### Synchronizing Adventure and Fort Mode syndrome timers

Fort mode runs 144 times faster than adventure mode - which means that a syndrome that lasts a single tick in Fort Mode will last 144 ticks in Adventure Mode. For short-term syndromes, this will cause very different behaviors between the two modes. In order to ensure that a syndrome operates the same way regardless of mode, add `DWF_STRETCH:144` to the end of the CE effect tag.

It is not possible to make a syndrome that lasts shorter than 144 ticks in Adventure Mode.

### Making a creature with a syndrome always applied

Some syndromes have effects that you can't add to a creature's basic RAW. To fix this, you can make a material that applies the syndrome to the creature's own species on contact, and make it continuously secreted by one of the creature's internal organs. See below for an example of this concept in action.

Note that syndromes applied in this manner will only be added to creatures when they are loaded in fortress or adventure mode, as secretions aren't currently simulated in world generation or the like.

Of course, you can also add a `PROB` value to the syndrome's various effects to determine how likely they are to actually manifest, which could be useful if you want a particular type of creature to only occasionally appear with a special ability/curse/disease/immunity/etc (as an alternative to messing around with extra castes). Make sure to add at least one guaranteed permanent syndrome effect - such as one of the dummy examples shown here, but with no `END` specified - to prevent the syndrome from being reapplied undesirably (which can occur when the secreted coating is removed and replaced by a new secretion), as this would give creatures who initially failed the `PROB` check another chance to pass it. Having a permanent effect in place prevents this from happening as reinfection cannot occur before a syndrome has ended fully.

Expanding on the above, this one-off opportunity to develop a certain syndrome effect can be turned into a recurring event by adding an `END` duration of your choice to the guaranteed dummy effect (henceforth referred to as the 'inhibitor'). For example, you might want to give a particular creature species the opportunity to evolve into another creature once every month, with a 1/100 chance of the transformation manifesting: this could be implemented as a secretion-applied syndrome with a `PROB:1` transformation effect and an `END:33600` inhibitor.

This can also be used to impose delays between the active phase of particular syndrome effects. For example, say you want to give your creature an intermittently activating regenerative ability: you could give it a secretion-derived syndrome providing the requisite healing effects with their `END` set to X, alongside an 'inhibitor' effect with an `END` set to X+Y, where Y is the duration of the delay.

## Stat-modifying syndromes

Syndromes that affect the creature's stats, particularly in combat.

### Size Modification

`CE_BODY_APPEARANCE_MODIFIER` not only changes the way a creature is described on the unit viewing screen - it also changes the combat effectiveness of the creature. The square-cube law is respected, meaning that doubling a creature's length, height, and broadness will make them 8 times as massive - an extreme boost in combat effectiveness. This does not affect the clothing they can wear.

    Giant Growth

    [SYNDROME]
        [SYN_NAME:giant growth]
        [CE_BODY_APPEARANCE_MODIFIER:APPEARANCE_MODIFIER:HEIGHT:200:APPEARANCE_MODIFIER:LENGTH:200:APPEARANCE_MODIFIER:BROADNESS:200:START:0]

Also, you can change the size of particular body parts, with appropriate effects. The following syndrome, for example, will make the creature's punches more powerful (but it will not make their scratches any stronger, because their fingers are still the same size).

    Hulk Hands

    [SYNDROME]
        [SYN_NAME:freakishly big hands]
        [CE_BP_APPEARANCE_MODIFIER:BP:BY_CATEGORY:HAND:APPEARANCE_MODIFIER:HEIGHT:300:APPEARANCE_MODIFIER:LENGTH:300:APPEARANCE_MODIFIER:BROADNESS:300:START:0]

## Counter Trigger examples

`CE_COUNTER_TRIGGER` is a fun token that lets you make syndromes with effects that activate under certain circumstances. You can use these to undo a different syndrome effect, in order to make a syndrome operate differently in different circumstances. Each counter trigger only affects the tag directly above it.

### More curse-like vampires

There's no real reason *not* to become a vampire in vanilla DF, you don't even really need to drink blood to survive. Let's change that by making a syndrome that weakens you if you don't drink blood, but makes you even stronger than vanilla vampires if you do.

    Double-edged vampire curse

    [SYNDROME]
        [SYN_NAME:vampire curse]
        [CE_PHYS_ATT_CHANGE:STRENGTH:50:0:TOUGHNESS:50:0:AGILITY:50:0:ENDURANCE:50:0:DISEASE_RESISTANCE:50:0:START:0] <-- Weakens the target always
        [CE_PHYS_ATT_CHANGE:STRENGTH:800:0:TOUGHNESS:800:0:AGILITY:800:0:ENDURANCE:800:0:DISEASE_RESISTANCE:800:0:START:0] <-- Strengthens the target
            [CE:COUNTER_TRIGGER:TIME_SINCE_SUCKED_BOOD:NONE:172799:REQUIRED] <-- Prevents the above strengthening effect from working unless the target has recently sucked blood (vampires become Thirsty at 172800)

### Creatures that behave differently underground

This is nice if you want to make an above-ground fort mode race, but don't want to actually restrict them to the surface - instead, you can give them a mood penalty for staying underground for too long. Note that the creature must have the [`[CAVE_ADAPT]`](/index.php/Creature_token#CAVE_ADAPT "Creature token") tag in order for the CAVE_ADAPT counter-trigger to work, and you will also need a constant secretion in order to ensure the syndrome is applied (see above).

    Bad thoughts from spending more than a month underground example (Place this in creature raw)

    [CAVE_ADAPT]
    [USE_MATERIAL_TEMPLATE:THOUGHTS:CREATURE_EXTRACT_TEMPLATE]
        [SYNDROME]
            [SYN_CONTACT]
            [SYN_NAME:a lack of sunlight]
            [SYN_AFFECTED_CREATURE:MY_CREATURE:ALL]
            [CE_FEEL_EMOTION:EMOTION:GLUMNESS:SEV:50:START:0]
                [CE:COUNTER_TRIGGER:CAVE_ADAPT:33600:NONE:REQUIRED]
    [SECRETION:LOCAL_CREATURE_MAT:THOUGHTS:LIQUID:BY_CATEGORY:BRAIN:ALL:CONTINUOUS]

You can do other things with this, like make a creature that gets extra abilities underground, or is stronger aboveground (by making the syndrome increase their strength normally, but reduce it using the counter-trigger, similar to the vampire example).
