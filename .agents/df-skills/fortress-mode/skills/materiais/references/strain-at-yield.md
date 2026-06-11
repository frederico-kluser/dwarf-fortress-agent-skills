# Strain at yield

> Fonte: [Strain at yield](https://dwarffortresswiki.org/index.php/Strain_at_yield) — Dwarf Fortress Wiki (GFDL/MIT)

**Strain at yield** is a property of materials. As with yield and fracture, there are six types of strain at yield, one for each of the six forces: impact, compressive, tensile, torsion, shear, and bending. Although in real life it represents the level of strain when forced by one of the forces, it is simplified greatly. Only impact strain at yield has been verified to have an effect.

A higher number means more strain (more flexible). A lower number means less strain (more rigid).

## Strain at yield of materials

Strain at yield of materials is defined by the following tokens:

- \[IMPACT_STRAIN_AT_YIELD\]
- \[COMPRESSIVE_STRAIN_AT_YIELD\]
- \[TENSILE_STRAIN_AT_YIELD\]
- \[TORSION_STRAIN_AT_YIELD\]
- \[SHEAR_STRAIN_AT_YIELD\]
- \[BENDING_STRAIN_AT_YIELD\]

As stated above, only \[IMPACT_STRAIN_AT_YIELD\] has been observed to affect the material. Lower strain at yield materials will shatter when hit by an impact, even if the impact is an edge weapon.

| Material | Strain at yield |
|----|----|
| Stone, Bone, Tooth, Horn, Hoof, Pearl, Shell, Soap, Tallow, Chitin, Most frozen liquids | 100 |
| Metal template, Wood template, Plant template, Seed template, most powders | 1000 |
| Nail | 5000 |
| Cartilage | 25000 |
| Skin, Fat, Muscle, Sinew, Nerve, Organ template, Leather, Cheese, Leaf | 50000 |
| Hair, Feather, Scale, Silk, Thread | 100000 |
