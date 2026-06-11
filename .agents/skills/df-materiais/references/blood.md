# Blood

> Fonte: [Blood](https://dwarffortresswiki.org/index.php/Blood) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Blood** is a fluid and contaminant found in the bodies of most living creatures. The preferred fluid of Armok, it serves as a vital part of those who possess it; losing it tends to be invariably fatal to most things which have it.

Blood men are creatures made out of blood, and vampires require it to satiate their thirst needs. Creatures have different types of blood depending on their species, or how they are procedurally generated.

## Dealing with blood

Troll blood. Known to vampires as "off brand".

Ground smeared in blood, coming straight from the source. ASCII mode.

Much like other contaminants, blood tends to spread *everywhere* Bug:296. Dwarves walking on tiles with a blood smear will spread it to the next tile, where it will form a spattering of blood, then a smear, which is why bloody areas tend to grow quickly above ground when heavily trafficked.

Blood smears located indoors will automatically be cleaned by passing dwarves, while those located outdoors will remain there until cleaned by some external factor like rain. Allocating bloody indoor underground areas as a meeting area seems to increase their cleaning priority, and they will get cleaned pretty quickly if you have enough idle workers. It is possible to remove blood from a soil floor by building a dirt road on it.

Brooks and similar sources of water replicate any blood that falls on their tiles, resulting in an endlessly-growing carpet of blood. This can be dealt with by covering the offending brook tiles with walls or floors. It is better to forbid an area with blood in above ground areas as rain will randomly clear tiles where it touches it. To be rid of blood splatters on a rough wall, designating the splattered area to be smoothed will make it disappear.

An option in the game settings permits disabling the spreading of contaminants, including blood.

## Obtaining blood

A playable vampire sensing blood.

Beyond the obvious method of injuring creatures, barrels full of blood can be brought with a dwarven expedition upon embark, and bought from dwarven and human civilizations during trading. Barrels of blood possess no use beyond being trade goods (making buying them redundant at best and a waste of dwarfbucks at worst, unless you are using it as a currency). Player-controlled dwarves are not able to create blood barrels.

Selecting blood inside a barrel for dumping does not empty the barrel. Using the workaround for dumping liquids from lye buckets works - view the contents of the barrel, select the blood and forbid or dump it. Alternatively, forbid/dump the blood from the stocks screen in 'liquids' then order the barrel to be brought for trading at the depot.

As with all other contaminants, blood created from injured creatures can't be used for anything, beyond morbid decoration (except smeared blood from a vampire, as drinking vampiric blood will turn the person into a vampire themselves).

## Assorted blood types

Not all creatures have the same dark red blood that most do:

- Most intelligent and most land creatures will have standard red blood, containing hemoglobin. ()
- Most invertebrates (ants, honey bees, creeping eyes, giant cave spiders, etc.) possess white-colored **ichor**, which is functionally identical to blood. ()
- Trolls possess cyan-colored blood. ()
- Crabs, cuttlefish, nautiluses, octopuses and squids possess copper-based dark blue blood (though in Graphics mode it appears the same as cyan). ()
- Fire imps, demon rats, and some procedurally generated creatures possess gray-colored goo instead of normal blood. ()
- The game files contain magenta-colored blood, procedural generated bogeymen and nightmares can have it. ()

Inorganic creatures such as the bronze colossus, the magma man and the amethyst man don't have blood, including particular organics, such as sponges and their variants, similarly for some types of undead (skeletons or animated skin).

Some creatures, when injured, may leave residue like a normal creature would bleed, but not actual blood. For example, a titan made out of salt may leave piles of salt where it was injured.

## Blood in combat

|  |
|----|
| "Blood" in other / Languages / Dwarven / : / nazush / Elven / : / cameda / Goblin / : / ogom / Human / : / cadem |

Blood makes a significant impact during combat. A strike which causes damage to major arteries can open them, leading the creature to begin bleeding out rapidly. Without any treatment, the wound may eventually cause the creature to die of blood loss, even if it isn't struck down by any other means. This is especially important in adventurer mode, where the impact of blood loss is more noticeable on an individual level. This type of death is common with creatures who get their limbs severed from their bodies.

Most syndromes are contracted when the poison enters the victim's blood. Certain sicknesses (such as iron man cough) include coughing or vomiting blood as symptoms, which may lead to bleeding damage on the afflicted individual. These are usually not fatal, but may lead to the person being left vulnerable in the face of danger. Certain creatures will suck the blood out of their victims upon landing a bite attack (such as female mosquitos, leeches and nightwings). This is largely irrelevant with vermin (who can't interact with other creatures anyway), but may be a problem when dealing with their savage humanoid/giant counterparts.

Creatures with no blood pose a greater challenge to kill, as they can't die of blood loss, and they will continue to fight no matter how much damage they suffer to whatever it is they're made of. Giant sponges were particularly famous for this.

Blood loss can be observed in the Overview tab of a creature's character sheet, along with other status effects, listed as either "Faint" (less than 50% of their maximum blood volume) or "Pale" (less than 25%). At zero blood, the creature dies from blood loss. However, the specific announcement "Urist McBloodless was found dead, completely drained of blood!" will only trigger if a dwarf was victim to a vampire attack.

## Adventure Mode

An adventurer surrounded by blood in a catacomb.

According to testing, drinking blood from a pool of blood (without an adjective on it like "Coating" or "Smattering") can relieve thirst even for non-vampires.[1] Additionally, you can fill your waterskin from it; that is, if you are desperate enough and have no easy access to water, such as when exploring a catacomb.

Thirsty Enough?

A pool of blood without an adjective.

Fill that waterskin with blood.

\

    [MATERIAL_TEMPLATE:BLOOD_TEMPLATE]
        [STATE_COLOR:ALL_SOLID:CARMINE]
        [STATE_NAME:ALL_SOLID:frozen blood]
        [STATE_ADJ:ALL_SOLID:frozen blood]
        [STATE_COLOR:LIQUID:CARMINE]
        [STATE_NAME:LIQUID:blood]
        [STATE_ADJ:LIQUID:blood]
        [STATE_COLOR:GAS:CARMINE]
        [STATE_NAME:GAS:boiling blood]
        [STATE_ADJ:GAS:boiling blood]
        [DISPLAY_COLOR:4:0:0]
        [MATERIAL_VALUE:1]
        [SPEC_HEAT:4181]
        [IGNITE_POINT:10508]
        [MELTING_POINT:10000]
        [BOILING_POINT:10180]
        [HEATDAM_POINT:10250]
        [COLDDAM_POINT:9900]
        [MAT_FIXED_TEMP:NONE]
        [SOLID_DENSITY:500]
        [LIQUID_DENSITY:NONE]
        [MOLAR_MASS:NONE]
        [IMPACT_YIELD:10000]
        [IMPACT_FRACTURE:10000]
        [IMPACT_STRAIN_AT_YIELD:100]
        [COMPRESSIVE_YIELD:10000]
        [COMPRESSIVE_FRACTURE:10000]
        [COMPRESSIVE_STRAIN_AT_YIELD:100]
        [TENSILE_YIELD:10000]
        [TENSILE_FRACTURE:10000]
        [TENSILE_STRAIN_AT_YIELD:100]
        [TORSION_YIELD:10000]
        [TORSION_FRACTURE:10000]
        [TORSION_STRAIN_AT_YIELD:100]
        [SHEAR_YIELD:6600] used high salinity ice
        [SHEAR_FRACTURE:6600]
        [SHEAR_STRAIN_AT_YIELD:100]
        [BENDING_YIELD:10000]
        [BENDING_FRACTURE:10000]
        [BENDING_STRAIN_AT_YIELD:100]
        [MAX_EDGE:500]
        [ABSORPTION:100]
        [IMPLIES_ANIMAL_KILL]
        [ROTS]
        [BLOOD_MAP_DESCRIPTOR]
