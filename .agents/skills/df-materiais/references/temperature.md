# Temperature

> Fonte: [Temperature](https://dwarffortresswiki.org/index.php/Temperature) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*For temperature as it relates to choosing an embarkation site, see Climate.*

**Temperature** - by definition - is a measurable quantity that represents how hot or cold a given area or object is. Temperature is also a very large element in the climate of an area, or more specifically, a biome. In both *Dwarf Fortress* and real life, there are two units to measure temperature, although the game uses a made-up, unique additional unit. The real life units are Celsius (°C), and Kelvin (K); other units, such as Réaumur (°r, °Re, or °Ré), Fahrenheit (°F) or Rankine (°R or °Ra) have been proposed and occasionally used. While the unique unit used by the game has no definite name, the designation "Urist" (°U) is used throughout this wiki and the community to reduce confusion.

## Adventure mode

In adventure mode, the temperature of the player character's surroundings is always displayed in the top-right corner. Being near elements and creatures that affect temperature (for example, being near a fire man) will also alter the temperature reading:\

## Temperature scale

Temperatures in *Dwarf Fortress* are measured in the game's own, unnamed temperature scale, since termed "degrees Urist" by the community. Temperatures in *Dwarf Fortress* are stored as sixteen-bit unsigned integers, which translates into a minimum value of 0 °U and a technical maximum of 65535 °U (216-1), although this is internally limited to 60000 °U, as 60001 °U is used for temperatures which have been set to `NONE`. Floating point values are not considered, and when they appear, any decimals are either sheared off or rounded away by the game. For example, the number 2999.999, would be rounded to 3000. Urists are scaled logically against the Fahrenheit scale, so conversions are non-intuitive:

|             |                             |
|-------------|-----------------------------|
| `[URIST]` = | `[FAHRENHEIT]` + 9968       |
|             | `[RANKINE]` + 9508.33       |
|             | `[CELSIUS]` \* 9/5 + 10000  |
|             | `[KELVIN]` \* 9/5 + 9508.33 |

According to Toady One in a Future of the Fortress post, the temperature scale used in the advanced worldgen settings is related to regular degrees Urist by the equation "local temp = world temp \* 0.75 + 10000". This scale doesn't seem to be used anywhere else in the game.

Some reference numbers:

|  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|
| Significance | DF Scale | worldgen | Celsius (°C) | Kelvin | Fahrenheit (°F) | Rankine (°Ra) |
| Boiling point of water | 10180 | 240.0 | 100.00 °C | 373.150 K | 212.00 °F | 671.67 °Ra |
| Dwarven body temperature | 10067 | 89.3 | 37.22 °C | 310.372 K | 99.00 °F | 558.67 °Ra |
| Freezing point of water | 10000 | 0.0 | 0.00 °C | 273.150 K | 32.00 °F | 491.67 °Ra |
| Freezing point of ≈89% ABV | 9850 | -200.0 | −83.33 °C | 189.816 K | −118.00 °F | 341.67 °Ra |
| Absolute zero | \*9508 | -656.0 | −273.15 °C | 0 K | −459.67 °F | 0 °Ra |
| Zero degrees Urist | 0 | -13333.3 | −5555.55 °C | −5282.405 K | −9968.00 °F | −9508.33 °Ra |
| Highest possible temperature | 60000 | 66666.6 | 27777.77 °C | 28050.927 K | 50032.00 °F | 50491.67 °Ra |

＊Absolute Zero is rounded down internally to avoid decimals. If it was more-precisely converted, it would be 9508.33°U. Also interesting is the fact that temperatures in *Dwarf Fortress* can go *far, far* below absolute zero, which is physically impossible; considering *Dwarf Fortress* also allows perpetual motion, sometimes it's best not to ask questions.

Values with an overline are truncated values with ending numbers that go on indefinitely, so a value of 45.738 is technically 45.738888888888- with the 8's going on indefinitely.

Urist asks...
I'm a modder who needs to work with temperature conversions all the time. Is there any tool I can use to lessen the amount of work involved?

Temperature conversions are usually only useful when / modding / , and can be annoying to do manually; luckily a simple / temperature conversion utility / has been created for those who find themselves having to convert a lot of temperatures to and / or from degrees Urist often. / An online temperature conversion utility can be found at / https: / jose96xd.github.io / DF_Tools / Modules / TemperatureConverter.html

Examples of some temperatures encountered in *Dwarf Fortress*, the most important ones in bold:

|  |  |  |  |
|----|----|----|----|
| Event / location | Native °U | °C | °F |
| Alcohol freezes | 9850 | -83.3 °C | -118 °F |
| **Lowest survivable temperature** | **9900** | -55.5 °C | -68 °F |
| Outside, freezing climate (varies) | 9960 | -22.2 °C | -8 °F |
| Underground, glacier ice | 9990 | -5.5 °C | 22 °F |
| **Water freezes** | **10000** | 0 °C | 32 °F |
| Nether-cap | 10000 | 0 °C | 32 °F |
| **Underground** | **10015** | 8.3 °C | 47 °F |
| Dwarf/human homeotherm | 10067 | 37.2 °C | 99 °F |
| Tiles next to magma (warm stone) | 10075 | 41.6 °C | 107 °F |
| **Highest survivable temperature** | **10078** | 43.3 °C | 110 °F |
| Outside, scorching climate (varies) | 10080 | 44.4 °C | 112 °F |
| Water boils | 10180 | 100 °C | 212 °F |
| Ignition of organic materials | 10508 | 282.2 °C | 540 °F |
| Wood fire (max) | 10708 | 393.3 °C | 740 °F |
| Material is fire-safe | 11000 | 555.5 °C | 1,032 °F |
| Common stone melts (varies) | 11500 | 833.3 °C | 1,532 °F |
| Coal fire (max) | 11640 | 911.1 °C | 1,672 °F |
| **Magma** | **12000** | 1,111.1 °C | 2,032 °F |
| Material is magma-safe | 12000 | 1,111.1 °C | 2,032 °F |
| Creatures made of flame/fire | 14000 | 2,222.2 °C | 4,032 °F |
| Dragonfire | 50000 | 22,222.2 °C | 40,032 °F |

## Material values

Temperature has important constraints on the materials in the game, and dictates a number of material properties related to states of matter and heat/cold damage. These are defined by material definition tokens in the material raw files, most of which use temperature as an input field:

- [`[MELTING_POINT]`](/index.php/Material_definition_token#MELTING_POINT "Material definition token") — This is the temperature at which a liquid material will freeze, or a solid material will melt. In *Dwarf Fortress* the melting point and freezing point coincide exactly; this is contrary to many real-life materials, which can be supercooled.
- [`[BOILING_POINT]`](/index.php/Material_definition_token#BOILING_POINT "Material definition token") — This is the temperature at which the material will boil or condense. Water boils at 10180 °U .
- [`[IGNITE_POINT]`](/index.php/Material_definition_token#IGNITE_POINT "Material definition token") — This is the temperature at which the material will catch fire.
- [`[HEATDAM_POINT]`](/index.php/Material_definition_token#HEATDAM_POINT "Material definition token") — This is the temperature above which the material will begin to take heat damage. Burning items without a heat damage point (or with an exceptionally high one) will take damage very slowly, causing them to burn for a very long time (9 months and 16.8 days) before disappearing.
- [`[COLDDAM_POINT]`](/index.php/Material_definition_token#COLDDAM_POINT "Material definition token") — This is the temperature below which the material will begin to take frost damage.
- [`[SPEC_HEAT]`](/index.php/Material_definition_token#SPEC_HEAT "Material definition token") — This determines how long it takes the material to heat up or cool down. A material with a high specific heat capacity will hold more heat and affect its surroundings more before cooling down or heating up to equilibrium. The input for this token is not temperature, but rather the specific heat capacity of the material.
- [`[MAT_FIXED_TEMP]`](/index.php/Material_definition_token#MAT_FIXED_TEMP "Material definition token") — A material's temperature can be forced to always be a certain value via the MAT_FIXED_TEMP material definition token. The only standard material which uses this is nether-cap wood, whose temperature is always at the melting point of water. If a material's temperature is fixed to between its cold damage point and its heat damage point, then items made from that material will never suffer cold/heat damage. This makes nether-caps fire-safe and magma-safe despite being a type of wood.

An important thing to remember when testing mods: Due to the way fixed temperature is handled, giving a material a fixed temperature will not cause its actual temperature to change accordingly — instead, its temperature will simply be permanently locked at whatever it was previously. *Removing* a material's fixed temperature, however, will cause all items made of it to heat or cool until reaching equilibrium with their surroundings. The fixed temperature of a container does affect its contents, but you can't freeze water by putting it into a bucket made from nether-cap because water will not freeze until it cools *below* 10000 °U . The fixed temperature of an inorganic material has no effect on unmined walls made from that material, though boulders **will** take on that temperature as they are produced via mining.

## Temperature transfer

Temperature transfer in *Dwarf Fortress* is fairly simple - every tick, an item that is exposed to a hotter/colder environment (or another item) will adjust its temperature by the difference (in °U) divided by the item's specific heat. Fractions are retained, but not used in calculations. For example, a piece of lignite (which has `[``SPEC_HEAT``:409]`) at temperature 10015 (room temperature underground) exposed to magma (temperature 12000) will heat up by (12000-10015)/409 = 4.853 °U in the first tick, then gradually slower. In order to reach its ignition point of 11440, it would need to be in the magma for a total of 517 ticks, over 5 seconds at 100 FPS.

## Bugs

- Temperature calculations are a known cause of lag. If maximizing framerate is a concern, you can disable temperature calculations in the settings. With temperature calculations disabled, effects such as water freezing, melting, or evaporating, or creatures and items taking temperature-related damage will not occur.
- When temperature calculations are disabled, dwarves will refuse to set foot in a cast obsidian tile (or any other tiles previously occupied by magma).Bug:8391 Occasionally, this can also occur when temperature calculations are still enabled. Bug:1272
