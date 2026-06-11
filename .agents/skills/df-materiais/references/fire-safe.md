# Fire-safe

> Fonte: [Fire-safe](https://dwarffortresswiki.org/index.php/Fire-safe) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Fire-safe materials** are those that are not damaged by fire. These materials include glass, *most* (but not all!) stone, and *most* metal (everything *but* bismuth, lead, tin, zinc, and all three pewters). Nether-cap is the only wood that can withstand fire (and even magma) thanks to its fixed temperature, but the game does not recognize it as a fire-safe building material. Counterintuitively, Bituminous coal, lignite, charcoal, and coke **are** considered fire-safe, since they only catch fire when they're hot enough (see below).

For the purpose of job item requirements (e.g. in custom reactions or when constructing certain buildings), only bars, blocks, stone, logs, and anvils can be classified as "fire-safe materials" - all other item types are rejected outright. Fire-safe materials are only required when the object is going to come into contact with extreme heat, such as all conventional furnaces and the forge. For the magma-powered versions of these buildings, as well as anything that will be in direct contact with magma (such as floodgates, grates or pumps, but not constructed walls, floors, fortifications, etc.), fire-safe is not enough: it has to be magma-safe.

As far as the game is concerned, only materials which are stable at the temperature 11000 °U (i.e. MELTING_POINT/BOILING_POINT/IGNITE_POINT/HEATDAM_POINT greater than 11000 and COLDDAM_POINT less than 11000) are considered fire-safe. Despite this temperature being considered fire-safe, actual fire can generate temperatures significantly higher - in particular, all burning items generate temperatures up to 200 degrees *above* their material's ignite point, so once a "fire-safe" item manages to get ignited (e.g. by exposure to magma), it can easily spread further. For practical purposes, anything which has an IGNITE_POINT should be treated as not fire-safe.
