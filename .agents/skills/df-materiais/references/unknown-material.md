# Unknown material

> Fonte: [Unknown material](https://dwarffortresswiki.org/index.php/Unknown_material) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Properties**
- **Material value 1 Fire-safe Magma-safe Melting point None Boiling point None Ignition point None Solid density 2000 [ Verify ] Specific heat None Color gray**
- **Fire-safe:** Magma-safe

!!UNKNOWN!!  · xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*Not to be confused with the unknown substance.*

**Unknown materials** can appear as a placeholder as the result of bugs - specifically, missing material tokens. They have minimal material properties, typically appearing as a light gray solid unaffected by temperature.

## Generic

An "Unknown material", as it is listed in building descriptions, normally has no name. It has an internal ID of -1 or [`[NONE]`](/index.php/Material_token#NONE "Material token"), the same as used in tasks that require items of any or an unspecified material.

Doors and hatch covers in dark pitsBug:6776 and dead civilizationsBug:3478 have been known to generate as unknown material.

Since the material ID of -1 is used as a placeholder value for any material, items made of the unknown material cannot be specifically requested as an ingredient, even in modded reactions.

## Organic substances

[`[CREATURE_MAT]`](/index.php/Material_token#CREATURE_MAT "Material token") and [`[PLANT_MAT]`](/index.php/Material_token#PLANT_MAT "Material token") fall back to "unknown creature/plant substance" if they do not have a proper subtype. If solid, they will additionally be listed as "frozen".

## Other forms

Other material categories have fallbacks in addition to their subtypes. Unlike unknown materials, they are functional when obtained.

Inorganic materials without a subtype become magma (`[``INORGANIC``:NONE]`), or generic "rock" if solid.

The generic form of charcoal and coke (`[``COAL``:NO_MATGLOSS]`) is known as refined coal, which cannot be legitimately obtained.

## See also

- Unknown (tile)
- Glitchstuff
