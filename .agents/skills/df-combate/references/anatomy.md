# Anatomy

> Fonte: [Anatomy](https://dwarffortresswiki.org/index.php/Anatomy) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

!!UNKNOWN!!  · xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

This page details the constituent limbs and **organs** one can expect to find in a dwarf's (or other humanoid's) body, based on data from `\raw\objects\body_default.txt` and `\raw\objects\creature_standard.txt`.

# Head Structure

### Hair

Hair is common to many creatures, not the least of which are dwarves. Dwarves can exhibit facial hair from birth, though female dwarves do not grow any by default (this ~~mistake~~ can be ~~corrected~~ changed in `creature_standard.txt` under the token `[CASTE:FEMALE]`).

### Eyes

Eyes allow dwarves to use their sight to view the world around them, and make decisions based on visual information. Losing both eyes can render a dwarf blind, resulting in a dramatic decrease in situational awareness and crafting quality.

### Nose

Noses *would* allow dwarves to smell things that emit odors, but currently serve no real purpose\[Verify\]. A dwarf without a nose will still get unhappy thoughts from miasma.

### Mouth

Mouths are used for biting by certain creatures who lack teeth. Interestingly, they are only considered in combat; even if a dwarf somehow loses their mouth, they can still eat meals and talk to other dwarves.

An interesting point to note is that both the mouth and nose can be removed, and the dwarf will still be able to breathe.

### Ears

Ears are used to hear noises. To a dwarf, the only noises that matter are those from tasks that modify tiles, such as mining, carving/smoothing, and woodcutting. Losing both ears can render dwarves deaf, and thus unable to hear noises.

## Head Organs

### Brain

Brains allow dwarves to think and are critical to survival. If the brain experiences any damage beyond bruising, it may result in loss of consciousness, or even death.

# Upper Body Structure

### Neck

Necks contain part of the upper spine and connect the head to the torso. They contain nervous pathways that are critical to life. Damage to the neck may result in full body paralysis, followed by death.

### Throat

Throats are the forward-facing portion of the neck. They can be strangled to induce unconsciousness, and contain major arteries that can cause rapid death when opened by attacks.

### Upper Torso

The upper torso contains critical organs used for sustained life functions. Damage to the chest often results in damage to these critical organs, which can quickly result in death. The upper torso connects the neck and the lower torso, and attaches both arms to the body.

### Arms

Arms are used for general physical interaction with the world, including lifting and carrying objects, wrestling with combatants, and grasping items. They may also be used for mobility if the dwarf does not have the ability to stand, which may arise from loss or impairment of the legs.

- Upper arm
  - The upper arm connects the torso and the lower arm.

- Lower arm
  - The lower arm connects the upper arm and the hand.

- Hand
  - Hands are used for attacks and grasping, and are typically populated with five fingers, including the thumb. A dwarf may experience difficulty grasping if one or more fingers are missing from the hand, and will, obviously, completely lose their ability to grasp if all fingers are lost.

## Upper Body Organs

### Heart

Hearts *would* be necessary to circulate a dwarf's blood around their body, but in reality, they do not serve any real function, and are theoretically not required for a creature to stay alive. However, the high [\[VASCULAR\]](/index.php/Tissue_definition_token#VASCULAR "Tissue definition token") value of the tissue which the heart is made from, as well as the [\[MAJOR_ARTERIES\]](/index.php/Tissue_definition_token#MAJOR_ARTERIES "Tissue definition token") token attributed to said tissue, ensure that any puncture to the heart will result in severe blood loss and eventual death.

### Lungs

Lungs allow dwarves to breathe. Loss of one can impair a dwarf's stamina, and can cause the dwarf to become Winded when doing basic tasks; but loss of both causes death by suffocation.

### Stomach

Stomachs *would* be used to digest food, but their presence is mostly decorative - a dwarf with a missing stomach can still eat. Strikes to the stomach can cause nausea and vomiting.

### Liver

Livers *would* be used to determine how well a given creature can hold its liquor, but currently have no function and are mostly cosmetic in nature. Dwarven livers are 50% larger than normal, perhaps to reflect their innate resistance to inebriation. This is in reality caused by their syndrome dilution factor token, and damage to their livers will have no effect on it.

### Pancreas

Pancreases would be used to regulate digestion and blood sugars, but dwarven diabetes does not exist, therefore their presence is entirely decorative. They can be damaged, but this is unlikely compared to the stomach, liver, lungs and heart due to their small size.

### Spleen

Spleens would be used to filter the blood, like the kidneys, but they are entirely decorative, like the pancreas, stomach and liver.

# Lower Body Structure

### Lower Torso

The lower torso contains non-critical organs that are not immediately important to continued survival. It connects the upper torso and the legs.

### Legs

Legs are used for standing, walking, running, and jumping. When missing one or even two, dwarves can use crutches to walk, and may even become skilled enough to return to their standard walking speed.

- Upper Leg
  - The upper leg connects the lower torso and lower leg.

- Lower Leg
  - The lower leg connects the upper leg and foot.

- Foot
  - Feet are used to maintain a stance, and are required for walking. Loss of just one foot may impair a dwarf's mobility severely, especially without a crutch.

## Lower Body Organs

### Guts

Guts are considered to be one cohesive unit by the game, and are simulated as such; they represent the small and large intestinal tracts that fill the abdominal cavity. They are considered to be 'under pressure', and thus may be ejected if the lower torso is opened by an attack. Guts being ejected usually results in death.

### Kidneys

Kidneys would be important in cleaning the blood and creating urine, but the game treats them decoratively. The kidneys are not life-critical, and one or both can be disabled or removed without much incident.

# Limb Components

Limbs and other components of the body are layered in material that helps protect the vital organs and nervous connections that keep the body functioning.

## Skin

Skin is a protective layer that surrounds most external body parts; the first line of defense from infection and disease, and protects dwarves from contaminants such as blood or vomit. Dwarves with healthy skin will usually wash contaminants off of their skin with water, using soap if it is available.

## Fat

Subcutaneous fat is held under the skin, where it forms an additional layer of protection against blunt-force and slashing injuries. As Dwarf Fortress' layering system is somewhat abstracted, when a dwarf is set on fire, their fat usually catches alight first, destroying the skin in the process.

Some dwarves can survive burning, even when all of their skin and fat is burned off, forming sinewy "supersoldiers" that do not experience pain. They are, however, very likely to die of blood loss before this can be achieved.

## Muscle

Muscles are critical in moving parts of the body, and are the core component in the motoric capability of a limb. Torn muscles can heal over time, but will temporarily reduce or negate the ability of a limb to function.

### Sinews

Sinews connect the muscles and bones together, and include the tendons (muscle-to-bone) and ligaments (bone-to-bone). Sinew tearing will disable limbs until they heal on their own.

## Nerves

Nerves carry impulses to and from a creature's brain. Nerves are connected between body parts up to the brain; if a nerve is severed, all nerves downstream of it will be paralysed or numb. Nerves cannot heal, and once severed, will never reconnect.

### Sensory

Sensory nerves are used to experience tactile sensations in limbs, such as bumps, scratches and touches. Loss of sensory nerves can arise from skin damage and deep cuts, which can render the limb numb.

### Motor

Motor nerves are used to actuate muscles that move limbs. If an attack severs a motor nerve, the limb and any others connected to it will be paralysed.

## Arteries

Arteries carry blood around the body, typically under moderate pressure. If an attack opens an artery, the blood may spray and spatter walls and floors, and puts the creature in imminent danger of bleeding out if untreated.

A doctor's cheat sheet.
