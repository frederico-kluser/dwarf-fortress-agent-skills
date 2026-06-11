# Meat

> Fonte: [Meat](https://dwarffortresswiki.org/index.php/Meat) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Meat** is a collective term for all non-aquatic-vermin edible, animal butchery products, and a food staple which can make up a significant part of a fortress's diet. Although the status bar and stocks window categorize all edible butchery products as meat, the game names them variously: true "{creature type} meat", which is muscle, and prepared organs, both produced when the creature is butchered. The amount of meat products produced depends on the individual creature's absolute size, which is a combination of the species' average size and any creature-specific modifiers (height, broadness, etc.).

Dwarves (*and humans, of course*) are omnivores; having meat to eat is not compulsory, but does increase variety (munching on the same gruel day after day will eventually cause negative thoughts). If there is no meat in your stocks, carnivorous creatures (such as some species of animal people) will go hungry, and animal trainers will be unable to perform the initial training on any wild carnivores. Starving carnivorous citizens will auto-assign the job "hunt for small animal". Prepared meals containing meat apparently also qualify as meat, for the purpose of feeding carnivores.

Like most types of food, meat will rot if not stockpiled appropriately, becoming unfit for consumption and emitting miasma over time if left underground.

## List of meats

|  |  |  |
|----|----|----|
| Material | Meat name | Sprite |
| Muscle | Meat |  |
| Eye | Prepared eye |  |
| Brain | Prepared brain |  |
| Lung | Prepared lung |  |
| Heart | Prepared heart |  |
| Liver | Chopped liver |  |
| Gut | Prepared intestines |  |
| Stomach | Prepared tripe |  |
| Gizzard | Prepared gizzard |  |
| Pancreas | Sweetbread |  |
| Spleen | Prepared spleen |  |
| Kidney | Prepared kidney |  |

## See also

- Body parts
- Meat industry
- Fish

|  |
|----|
| "Meat" in other / Languages / Dwarven / : / igril / Elven / : / lethiro / Goblin / : / smozû / Human / : / átu |

    [MATERIAL_TEMPLATE:MUSCLE_TEMPLATE]
        [STATE_COLOR:ALL_SOLID:MAUVE]
        [STATE_NAME:ALL_SOLID:muscle]
        [STATE_ADJ:ALL_SOLID:muscle]
        [STATE_COLOR:LIQUID:MAUVE]
        [STATE_NAME:LIQUID:n/a]
        [STATE_ADJ:LIQUID:n/a]
        [STATE_COLOR:GAS:MAUVE]
        [STATE_NAME:GAS:n/a]
        [STATE_ADJ:GAS:n/a]
        [DISPLAY_COLOR:4:0:0]
        [MATERIAL_VALUE:1]
        [SPEC_HEAT:4181]
        [IGNITE_POINT:10508]
        [MELTING_POINT:NONE]
        [BOILING_POINT:NONE]
        [HEATDAM_POINT:10250]
        [COLDDAM_POINT:9900]
        [MAT_FIXED_TEMP:NONE]
        [SOLID_DENSITY:1060]
        [LIQUID_DENSITY:NONE]
        [MOLAR_MASS:NONE]
        [IMPACT_YIELD:10000]
        [IMPACT_FRACTURE:10000]
        [IMPACT_STRAIN_AT_YIELD:50000]
        [COMPRESSIVE_YIELD:10000]
        [COMPRESSIVE_FRACTURE:10000]
        [COMPRESSIVE_STRAIN_AT_YIELD:50000]
        [TENSILE_YIELD:10000]
        [TENSILE_FRACTURE:10000]
        [TENSILE_STRAIN_AT_YIELD:50000]
        [TORSION_YIELD:10000]
        [TORSION_FRACTURE:10000]
        [TORSION_STRAIN_AT_YIELD:50000]
        [SHEAR_YIELD:20000] used human skin
        [SHEAR_FRACTURE:20000]
        [SHEAR_STRAIN_AT_YIELD:50000]
        [BENDING_YIELD:10000]
        [BENDING_FRACTURE:10000]
        [BENDING_STRAIN_AT_YIELD:50000]
        [MAX_EDGE:0]
        [ABSORPTION:100]
        [IMPLIES_ANIMAL_KILL]
        [ROTS]
        [GENERATES_MIASMA]
        [MEAT]
        [BUTCHER_SPECIAL:MEAT:NONE]
        [MEAT_CATEGORY:STANDARD]
        [MEAT_NAME:NONE:meat:meat]
        This lets the game know that the item can be eaten in various ways.
        [EDIBLE_VERMIN]
        [EDIBLE_COOKED]
