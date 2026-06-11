# Health care

> Fonte: [Health care](https://dwarffortresswiki.org/index.php/Health_care) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

A **hospital** location allows wounded dwarves to rest and receive care and treatment. Hospitals use any beds, Tables, traction benches, and chests that have been built within the zone. The hospital will requisition thread, cloth, splints, crutches, plaster powder (for casts), buckets, and soap for medical use. These will be stored within the hospital's containers; you may adjust the desired quantities.

**Doctors** are dwarves assigned to any of the four doctoring occupations: diagnosis, surgery, setting bones, and doctor, which does all of the above. All doctors in the fortress operate under the instruction of the chief medical dwarf, an appointed noble. Doctors perform their medical procedures on a dwarf only after treatment has been prescribed by a diagnostician. Doctors do not (yet; one must use DFHack in the interim) perform any healthcare on animals. Suturing and wound dressing are done by orderlies, but their quality is not impacted by any skills, so having all dwarves assigned to it has no negative effect.

Dwarves assigned roles via the hospital zone will only begin doing them once the labors for all dwarves have been updated. To quickly achieve this, go to the labor menu and set 'only selected dwarves mine' to 'no dwarves mine' and then set back to 'only selected dwarves mine', or do anything else in work details.

All beds within a hospital location are automatically hospital beds, where injured dwarves will go (or be brought) to recuperate. Tired, healthy dwarves will occasionally camp there too if the hospital is close, even if they have their own bed.

## Setting up a hospital

Hospitals are designated as locations. Designate a Meeting Area zone in the usual way, then select the Add Location button (plus sign) and select Hospital. Any amount of zones can be added to the hospital in the same way, selecting the existing hospital name instead of clicking "new hospital" at the top of the menu. Select the view location button () allows you to check the equipment and medical supplies missing/available to your hospital.

- Place enough beds in that zone to ensure you can keep all wounded dwarves in the hospital. Dwarves can lie on the ground instead of in beds if none are available, but this is not ideal.
- Place at least one table (b-f-t) for surgeons to perform surgery on. Adjacency to beds makes it easier to move a patient for surgery. You may perform surgery without tables; it will be messier.
  - Multiple dwarves may undergo simultaneous surgeries on the same table.
- Place one or more traction benches (b-f-T) to handle compound fractures when the dwarf requires "immobilization."
  - Each traction bench can only accommodate one dwarf at a time, and the dwarf may be there for quite some time, so plan accordingly.
- Place chests (b-f-h) to store medical supplies reserved for hospital use. Once placed, dwarves will start stocking the hospital with medical supplies, you can track their progress and change storage limits in the zone's 'Set Hospital Information' menu. A small hospital can manage with two containers, while a fully-fledged fortress with an adventurous military may need as many as eight. (Containers are not strictly necessary; doctors can and will use supplies from anywhere, but dedicated hospital containers allow you to earmark some supplies for medical use - for example, to prevent the auto-looming of *every* last thread.)

Medical Staff:

- Assign dwarves to one of the doctoring occupations and they will do them once work details have been updated. You might want to set several dwarves to be dedicated doctors, with diagnosis labor well-covered - without a diagnosis, patients cannot be treated, if they cannot be treated, they will occupy the hospital area until they die, performing no function. Any dwarf who is assigned as a doctor or diagnoser can diagnose dwarves. Once a patient is diagnosed, you can see on the individual health screen what procedures are needed, for example, washing or suturing. Low-skilled diagnosers may miss syndromes, so if you're having an epidemic of flesh melting extract, it may be best to only have your best diagnosers on duty.
- If you use a burrow to keep doctors near the hospital zone, ensure that this burrow covers all needed materials or you could get job cancellations because of a lack of material. Thread/cloth stockpiles, and items bought from caravans (e.g. plaster early in the game) are often the most troubling.

## Skills and injuries

There are four skilled doctoring labors and two unskilled supporting hauling labors involved in healthcare.

|  |  |
|----|----|
| Labor | Use |
| Diagnostician | Determines what procedures (of the other four) are necessary. Bad diagnosers might miss syndromes others won't. |
| Surgeon | Repair internal organ damage, excise necrotic tissue or serious injuries to muscle, bones. Good surgeons cause less bleeding in their operations. |
| Bone doctor | Sets simple breaks for healing |
| Suturer | Stops serious bleeding. Part of the default **orderly** work detail. |
| Wound dresser | Finalizes closed wounds for healing. Part of the default **orderly** work detail. |
| Recovering wounded | Hauls wounded units to the hospital. Part of the default **orderly** work detail. |
| Feed patients/prisoners | Gives food/water to patients/prisoners. Part of the default **orderly** work detail. |

Those with the **recover wounded** labor will attempt to carry an injured dwarf to a hospital zone, or, lacking one, to the nearest unoccupied bed. Dwarves are not light, especially ones in full armor, so these laborers should not have low strength attributes. Note that recovering wounded appears to be an extremely low priority task, and since immobile patients will need to be carried to a hospital before diagnosis, it may be necessary to temporarily disable all other labors on dwarves with this labor to get the wounded moved quickly.

Once in the hospital, a **diagnoser** will then evaluate the patient and prescribe a treatment, which any doctor who have the appropriate medical labors enabled (including themselves) may carry out – dwarves cannot be treated without a diagnosis. Depending on the injury, a treatment job will occur. Diagnosis is often required between procedures as well.

After diagnosis, injuries to various body parts will be revealed. The color of the text will indicate the severity of the wound, from least to most serious, as follows:

NONE: No recorded active wounds on the part.

MINOR: Any damage that doesn't have functional/structural consequences (might be heavy bleeding, though).

INHIBITED: Any muscular, structural, or functional damage, without total loss.

FUNCTION LOSS: An important function of the part is completely lost, but the part is structurally sound (or at least partially intact).

BROKEN: The part has lost all structural integrity or muscular ability.

MISSING: The part is completely gone.

- **Internal Organs** can be treated or removed by a surgeon using tables and traction benches, and are typically caused by piercing injuries.

Surgery also covers the repair of infected or rotten wounds, which are typically caused by lack of soap, poor water access for cleaning, delayed medical care, or just bad luck.

- **Bones** can be set and treated by bone doctors using thread and cloth (for minor fractures), splints and casts, or traction benches, depending on severity. Grasping is often impaired during healing. The Immobilization Request status tag is an indication that a splint or plaster cast is required. Multiple overlapping and compound fractures require a surgeon. Typically caused by blunt trauma.

- **Skin and muscle** can be treated by a suturer using thread and cloth. The wound will continue to bleed until sutured. Severe wounds to the hands can impair grasping during healing. Typically caused by slashing injuries.

- Closed wounds will be dressed by a wound dresser.

Any dwarves with the feed patients/prisoners labor will attempt to give food or a bucket of water to a hungry or thirsty patient. By default, all dwarves start with the non-doctoring, supporting labors enabled; these have no corresponding skills, do not cause experience gain, and merely are activities that can be performed by any dwarf, but can be disabled for those with more important labors.

## Infection

Every open wound can become infected. Infections may heal over time; however, many dwarves will die due to infection, often months after the actual wounding. The creature that caused the infection will be credited for the kill.

Causes of infection include:

- No cleaning of the wounds.
- Cleaning with water from a stagnant water source, or cleaning with water laced with mud.\[Verify\]
- Cleaning without soap.
- Bad luck

An infection effectively causes constant internal bleeding, and if the infected dwarf is healthy enough, they can naturally replenish their blood quickly enough to outpace the infection.

It's worth noting however that necromancy effectively cures infections, as the intelligent undead it can create cannot die of bleeding.

## Equipment and medical supplies

In-game hospital information summary

### Traction benches

A traction bench is used by a bone doctor in a hospital zone to immobilize a dwarf that has sustained complex or overlapping fractures.

It is constructed in the mechanic's workshop, and requires a table, a mechanism, and a rope or a chain to construct. The quality of each component is not reflected in the quality of the traction bench, and only the material of the table is used as the material for the bench. "Recycling" low-quality, low-value components into high-quality traction benches can provide a modest increase in value. Note that if any stockpiles have been linked to "Give" to the workshop, all of the resources needed to construct the traction bench must be found in the linked piles (e.g., linking only a stone stockpile may prevent access to the necessary tables/ropes/chains).

### Gypsum plaster

Orthopedic casts are made out of plaster powder and are used to keep bones in their proper place until healed. To store them in a hospital, place a chest or other container inside the hospital zone. Applying a cast also requires a bucket, cloth, and a water source.

Plaster powder is produced at a kiln or magma kiln from gypsum, alabaster, selenite, or satinspar and an empty bag by a dwarf with the furnace operator skill enabled. They can also be bought at embark for 3 points per unit; each unit comes with a free bag.

Gypsum powder is superior to a splint in that it allows the dwarf to leave the hospital and resume their duties, which is not possible with a splint. If(!) gypsum powder is available, use that rather than splints.

### Splints

Splints, applied by a bone doctor, immobilize limbs that have sustained bone fractures, allowing them to heal. Dwarves will **not** be able to leave the hospital and resume their normal duties until the broken limb is fully healed.\[Verify\]

They can be made out of one wood at the carpenter's workshop or one metal bar at the metalsmith's forge or the magma forge. Splints are categorized as finished goods.

Splints are inferior to plaster casts, as while they are easier to obtain and prepare, they do not allow movement while healing (which can take months). If plaster powder is available, it is by far the better option vs. splints.

### Other equipment

- Tables are used to conduct operations on. *(Bug: One table can hold multiple simultaneous diagnostic/surgical patients.)*
- Beds are used by patients to rest. Placing beds at the corners of a hospital will help ensure the wounded are brought to a tile that has a bed.
- Soap is used to clean wounds, sterilizing and preventing infection.
- Water is used to clean wounds, bathe patients and give drink, as patients do not drink alcohol. Make sure a designated source is safe, nearby and clean, either a well, cistern or running water.
- Buckets are used to gather and hold water for its uses.
- Thread is used to suture closed wounds.
- Cloth is used to clean wounds, wash patients and dress wounds.
- Chests are used to store hospital supplies.
- Crutches ┬ help a crippled dwarf walk again.

## Tips for an effective hospital

- Regularly use (i-H) to examine your hospital stockpile. Ensure your hospital is well-stocked. If you run out of materials regularly, increase the limits.
  - Note that the quantities listed in the "Set Hospital Information" screen are different than those used in stockpiles.
    - 1 stockpile unit of thread = 15000 in the hospital
    - 1 cloth = 10000
    - 1 soap = 150
    - 1 gypsum powder = 150
- It is possible to do without soap in the hospital stockpile. Choosing to do so, however, increases the risk of infection, which will most likely kill the patient. Consult the soap page to understand that industry. Bring 1 lye on embark for one bar of soap, which translates to 150 units.
- Put a well inside (or near) the hospital for maximum efficiency. Doctors need to wash patients regularly, and clean water reduces infection.
- Do not place chairs next to your surgery tables. A chair is an invitation for rat-roast-eating freeloaders to block the medical process.
- You may wish to consider individual rooms for each bed if you find your doctors are choosing to treat Urist McPaperCut over Urist McBloodFountainTheGushing. A locked door minimizes the mess, and thereby infection and allows you to prioritize. Plus, necrotizing flesh can generate lots of miasma, which a closed door will stop.
- You can select nurses who enjoy helping people to give them good thoughts. This also prevents dwarves that hate bringing others food from receiving unhappy thoughts.
- If you use Dwarf Therapist, try to select strong or large-sized dwarves to recover wounded. Weak dwarves slowly inching back to the hospital from a hostile area with a dying patient can result in fun.
- When a serious injury happens, don't exit (or save) the game until the injured are in the hospital zone, especially if a dwarf is immobile. "Bring crutch" and "Recover Wounded" jobs will be lost, keeping the patient away from the hospital, and doctors will NOT go to patients, even if burrowed with them, because a diagnose job hasn't been created. Sometimes a second "crutch required" or "recover wounded" request will be generated, but often too late for the patient's full recovery. Your best bet is to ensure someone (not burrowed) has "recover wounded" enabled at all times; burrow doctors doing non-medical tasks immediately; hope the patient makes it to the hospital.\[Verify\]
- Long-term residents will seek medical care if injured. This includes non-dwarves. Doctors will treat them the same as dwarves and the different physiology doesn't seem to be an issue.
- To prevent the usage of adamantine thread, store no thread in hospital settings and instead have a stockpile of non-metal thread in the hospital while additionally having a manager order to make 1 wafer when you have 1 adamantine thread.

Dwarves will prefer to store and use the most expensive thread and cloth – yes, that includes special "exotic" strands, which you may want to forbid during medical emergencies.

## Bugs

- Occupations assigned at a hospital will not take immediate effect due to the healthcare labors bug.
- For a variety of reasons, an injured dwarf may leave the hospital and/or refuse to go to the hospital. Bug:309
- Wounded dwarves are not always recovered properly. Bug:94 Re-injuring the dwarf (with a minecart collision, dropped item, etc.) may trigger proper recovery.
- Adamantine thread used for suturing. Bug:1346
- The quality and value of a finished traction bench does not account for all of the inputs used to make it.\[Verify\]
- Dwarves resting in bed may be starving/dehydrated and not being taken care of, deconstructing the bed to generate a new Recover Wounded task and force them to rest properly fixes this.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Soap is the only item dwarves will use to sterilize a wound. While dwarves are of course aware that humans will pour perfectly quaffable alcohol over their bloody wounds and onto the filthy ground to get the same effect, dwarves understand that some things are more precious than a single life, and face oblivion with a bit more dignity. The application of extreme heat is also well known to prevent infections and seal a wound, but dwarves consider magma the only legitimate heat source, and the non-lethal application of magma is sacrilege.

A human doctor attempting to help.\
*Art by Luke Fildes (October 3, 1843 – February 28, 1927)*
