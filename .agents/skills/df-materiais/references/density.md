# Density

> Fonte: [Density](https://dwarffortresswiki.org/index.php/Density) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Density** is a material property that, along with volume, affects the weight/mass of an object made from the material.

Density influences weight, which influences how easily dwarves can carry things. Density affects the momentum of weapon attacks, but only so much; 600 density has 80% the momentum of something of infinite density, and all normal metals have significantly greater densities than this, meaning that you can usually ignore it for deciding which weapons are stronger. Density also affects fall damage. DF simulates falling by shooting the ground at you, so denser floors do more damage. Density in *Dwarf Fortress* is in units of kg/m3\*.

*(\* For example, in the real world, the density of pure gold is 19.32 grams/cm3, which works out to be 19,320 kg/m3, the same numeric value as the density of DF gold (see table below).)*

## Density of some materials

Note that not all forms of items are the same size, and so are not comparable when considering actual weight for practical applications, such as a door prize. A stone (including raw ore) has a size of 100,000 cm3 and a log of wood 50,000 cm3, while a bar of metal *(or a block of stone or wood)* have a size of only 6,000 cm3, a difference of ~16.67:1 for stone vs. metals, or ~8.33:1 for wood vs. metals.

Note that, as of v.50, "density" is no longer the primary factor for blunt (and other) damage. Heavier weapons are (often\*) swung more slowly, creating "momentum" (mass x velocity), which is a large part of what now is used in determining damage.

(\* depending on the strength of the creature swinging the weapon, and other factors, including a coded hard "cap" on that momentum. See Density vs. weapon momentum sub-section, below)

\

|  |  |  |  |
|----|----|----|----|
| Name | Type | Density | Notes |
| Feather tree | Wood | 100 | Least dense wood, found only in good biomes |
| Papaya | Wood | 130 | Second least dense wood, found only in tropical biomes |
| Candlenut | Wood | 140 | Third least dense wood, found only in tropical biomes |
| Adamantine | Metal | 200 | Least dense metal, light enough that it has much lower momentum\* in weapon attacks than others (about 57% for a normal dwarf) |
| Raw adamantine | Stone | 200 | Least dense stone |
| Kapok | Wood | 260 | Fourth least dense wood, found only in tropical biomes |
| Willow | Wood | 390 | Fifth least dense wood, found near water, most widespread of "light" wood |
| Bone | Organics | 500 |  |
| Leather | Organics | 500 |  |
| Silk | Organics | 500 |  |
| Yarn | Organics | 500 |  |
| Tunnel tube | Wood | 500 | Least dense underground wood, found only in caverns |
| "typical" wood | Wood | 600 | There are nearly about twenty varieties of wood at 600+ / -20, about twenty (unlisted here) that weigh less, / and about twenty (unlisted here) that weigh more. See / Wood / for a full list and discussion. |
| Persimmon | Wood | 835 | Densest wood found in temperate biomes |
| Olive | Wood | 990 | Densest "normal" wood, found only in tropical biomes |
| Divine metal | Metal | 1000 | Second least dense metal, about 86.6% momentum on attacks\* |
| Glumprong | Wood | 1200 | Densest above-ground wood *(by far)*, found only in evil biomes |
| Blood thorn | Wood | 1250 | Densest wood, underground, found only in caverns |
| Lignite | Stone | 1250 |  |
| Jet | Stone | 1320 | Least dense non-economic stone |
| Earthenware | Ceramic | 1360 |  |
| Plant cloth | Organics | 1520 |  |
| Stoneware | Ceramic | 2000 |  |
| Saltpeter | Stone | 2105 |  |
| Petrified wood | Stone | 2200 | Least dense "magma-safe" stone |
| Gypsum relatives | Stone | 2300 |  |
| Gypsum | Stone | 2320 |  |
| Porcelain | Ceramic | 2403 |  |
| Glass | Gem | 2600 |  |
| (General) stone | Stone | 2670 |  |
| Ordinary gem | Gem | 2670 |  |
| Aluminum | Metal | 2700 | Least dense "normal" metal |
| Limestone | Stone | 2710 |  |
| Marble | Stone | 2780 |  |
| Calcite | Stone | 2930 |  |
| Diamond (any) | Gem | 3520 |  |
| Cobaltite | Stone | 6295 |  |
| Zinc | Metal | 7135 |  |
| Tin | Metal | 7280 |  |
| Lay pewter | Metal | 7280 |  |
| Galena | Stone | 7500 | Ore of lead |
| Pitchblende | Stone | 7600 | Most dense "magma-safe" non-economic stone, excepting Slade |
| Iron | Metal | 7850 | standard weapons-grade metal, 98.125% max momentum\* |
| Steel | Metal | 7850 | standard weapons-grade metal, 98.125% max momentum\* |
| Cinnabar | Stone | 8100 | Densest non-economic stone, excepting Slade |
| Bronze | Metal | 8250 | standard weapons-grade metal, 98.2% max momentum\* |
| Nickel | Metal | 8800 |  |
| Copper | Metal | 8930 | standard weapons-grade metal, 98.35% max momentum\* |
| Silver | Metal | 10490 | standard weapons-grade metal, 98.59% max momentum\* |
| Lead | Metal | 11340 |  |
| Gold | Metal | 19320 |  |
| Platinum | Metal | 21400 | Densest metal, 99.3% max momentum\* |
| Native platinum | Stone | 21400 | Densest economic stone (and ore) |
| Slade | Stone | 200,000 | Densest stone, cannot normally be mined. |

(\* re "momentum" in determining damage for a weapon or collision, see next sub-section)

### Density vs. weapon momentum

In previous versions, the denser the material the heavier a weapon was, and the more damage that weapon would do in combat, especially blunt weapons - simple. However, that difference has been largely limited in the current combat system by determining "momentum", which is {weight x velocity}. Heavier weapons *tend* to be swung less quickly, so the old "heavier = more" rule is no longer that simple. There are many variables, significantly including size and strength of the combatant, but "momentum" is now the go-to value for determining "best" metal for blunt attacks.

And with a variation for maximum (based on strength/etc) momentum of between 98.125 (iron/steel) to 98.59 (silver), that's a difference of \moody holy grail of blunt weaponry, is now capped at a max 99.3%, only a 1.2% increase over steel. Meanwhile, the significant increased weight of such weapons *does* count directly toward tiring a combatant, making "heavier" weapons even less attractive for all but the strongest, most indefatigable dwarves.

Bottom line, against unarmored opponents (i.e. most animals, kobold thieves, simple undead, etc.), any metal bludgeoning weapon is overkill and will merrily break bones and crush skulls with ease. Against armored targets, all metals now work *about* the same. You can safely save your steel (and even iron and bronze) and use whatever metal(s) you have in surplus, and you're not hurting your hammer-/mace-dwarves by any amount that anyone would notice in game play; and weaker warriors don't have to lug around silver weapons, fatiguing themselves half-way through an encounter.

Note that it's been reported that these "maximums" are *not* capped in weapons traps which, presumably, have no variable "strength", and so heavier weapon materials, certainly for blunt but also for slashing/piercing attacks, do perform better (accounting for the superior metal rule for the latter).

- See also Material science#Attack Momentum for more technical details

## See also

- Size
- Weight
- Material science
