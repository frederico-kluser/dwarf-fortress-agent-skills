# Strain at yield

> Fonte: [Strain at yield](https://dwarffortresswiki.org/index.php/Strain_at_yield) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Strain at yield** is a mechanical property that materials possess. As with yield and fracture, there are six types of strain at yield, one for each of the six forces: impact, compressive, tensile, torsion, shear, and bending. Although in real life it represents the level of strain when forced by one of the forces, it is simplified greatly. Only impact strain at yield has been verified to have an effect.

A higher number means more strain (more flexible). A lower number means less strain (more rigid).

## Elastic Modulus

The formula used by the raws to calculate strain at yield from a real-world elastic modulus value is the raw yield strength (in KPa) divided by the elastic modulus (in GPa/10 or Pa × 108). As it represents strain, this value is a dimensionless quantity.

For example, iron has an [`[IMPACT_YIELD]`](/index.php/Material_definition_token#IMPACT_YIELD "Material definition token") of 542,500 KPa and its bulk modulus is 170 GPa. (**542500**/\[10 × **170**\]) = 319.1…, thus its [`[IMPACT_STRAIN_AT_YIELD]`](/index.php/Material_definition_token#IMPACT_STRAIN_AT_YIELD "Material definition token") is 319.

An online material helper to simplify these calculations for modding can be found here: https://putnam3145.github.io/helper

Young's modulus is used for tensile and bending elasticity, the shear modulus is used for shear and torsion elasticity, and the bulk modulus is used for impact and compressive elasticity.

## Strain at yield of materials

The strain at yield of materials is defined by the following tokens:

- [`[IMPACT_STRAIN_AT_YIELD]`](/index.php/Material_definition_token#IMPACT_STRAIN_AT_YIELD "Material definition token")
- [`[COMPRESSIVE_STRAIN_AT_YIELD]`](/index.php/Material_definition_token#COMPRESSIVE_STRAIN_AT_YIELD "Material definition token")
- [`[TENSILE_STRAIN_AT_YIELD]`](/index.php/Material_definition_token#TENSILE_STRAIN_AT_YIELD "Material definition token")
- [`[TORSION_STRAIN_AT_YIELD]`](/index.php/Material_definition_token#TORSION_STRAIN_AT_YIELD "Material definition token")
- [`[SHEAR_STRAIN_AT_YIELD]`](/index.php/Material_definition_token#SHEAR_STRAIN_AT_YIELD "Material definition token")
- [`[BENDING_STRAIN_AT_YIELD]`](/index.php/Material_definition_token#BENDING_STRAIN_AT_YIELD "Material definition token")

As stated above, only [`[IMPACT_STRAIN_AT_YIELD]`](/index.php/Material_definition_token#IMPACT_STRAIN_AT_YIELD "Material definition token") has been observed to affect the material. Lower strain at yield materials will shatter when hit by an attack, even if the attack is with an edge weapon.

|  |  |
|----|----|
| Material | Strain at yield |
| Stone, Bone, Tooth, Horn, Hoof, Pearl, Shell, Soap, Tallow, Chitin, most frozen liquids | 100 |
| Metal template, Wood template, Plant template, Seed template, most powders | 1000 |
| Nail | 5000 |
| Cartilage | 25000 |
| Skin / , / Fat / , Muscle, Sinew, Nerve, / Organ / template, / Leather / , / Cheese / , / Leaf / Minimum for / structurally elastic / armor / ( / clothing / , mail) | 50000 |
| Hair, Feather, Scale, Silk, Thread | 100000 |
