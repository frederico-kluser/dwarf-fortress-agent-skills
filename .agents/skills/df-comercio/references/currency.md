# Currency

> Fonte: [Currency](https://dwarffortresswiki.org/index.php/Currency) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

The game's **currency** is measured in "☼" (*White Sun With Rays*, unicode character U+263C, key combination Alt + NumPad-15), called "dwarfbucks" or "db's" by some players. Each item has a specific trade value in ☼, determined by what kind of object it is, what it is made of, and (sometimes) how well it was made. Dwarfbucks are an important measure in trade for bartering goods, allowing both the merchant and trader to judge whether the bartered trade goods are equivalent or not.

## Coins

This is a stack of 4 Scythe 2008 pewter coins. This is a pewter currency of Scythe from the year 2008. On the front of the coin is a well-designed image of a dwarf.

Metal crafters may strike physical coins out of any metal at the metalsmith's forge. This process requires one metal bar and one unit of fuel, and produces one stack of 500 coins. Each stack of coins has an effective item value of 10, meaning that the value of a stack is 10 × material value of the component metal, and a given coin is (10 × material value ÷ 500) of the value of the metal bar that produced it. For example, silver has a material value of 10, so a stack of 500 silver coins will be worth 10 × 10 = 100☼, and each silver coin in the stack will be worth 10 × 10 ÷ 500, or 0.2☼ (fractional ☼ values are never displayed).

Coins have their own stockpile, and a bin in such a stockpile can hold over 100 stacks of 500 coins each. Coins are named based on the year they are minted and the name of your civilization, and each coin in a given stack will be identical. For example, if the year is 1058 and the name of the civilization is Olon Ibesh, each coin in a stack of silver coins will be an "Olon Ibesh 1058 silver" coin. The coins also depict images and figures from the history of the civilization. The images replicated on the coin can be of quality, but this does not translate into a quality grade of the coin itself. Every material and every year will get its own pair of images.

Graphically, coins have different sprites for different amounts stacked in a tile.

### Coins and the Dwarven Economy

Coins were intended for use with the dwarven economy, until it was removed - in previous versions, copper, silver, and gold coins had monetary value in addition to their intrinsic value, and dwarves would keep personal stacks of coins as part of their personal accounts. Coins of other metals were widely known as "collector's coins." The CURRENCY entity token, which defines the value of coins, does still exist, but its effects can only be seen in Adventurer mode. Because of this, coins have no economic use in Fortress mode aside from trading.

### Coins and Combat Training

It is possible - although highly inadvisable in the current version - to construct danger rooms which train dwarves' armor user skills by flinging coins at them.

## Adventure Mode

Coins are commonly found in Adventure mode. Virtually any intelligent being (dwarf, human etc.) you find can have coins in their inventory - provided they have a suitable container on their person, typically a small pouch. Coins from dwarven civilizations are named after the civilization and the year they were minted as described above - other races name their coins after their civilization and the name of the reigning ruler. Each civilization maintains its own currency, and coins minted by one civilization will not retain their value if you travel to a town belonging to a different civilization. For this reason, it can be more practical to exchange excess coinage for other small and valuable (barter) objects like gems. Coins are also useful for throwing at enemies.

Coin values in Adventure Mode:

- Copper Coin = 1☼
- Silver Coin = 5☼
- Gold Coin = 15☼

Human and dwarven civilizations frequently utilize their coins in shops and markets. They seem to be the only civilizations to actually use currency. Elves do not appear to use coins in their trades, goblins do not appear to participate in commerce at all, and kobolds only barely grasp the concept of *communication*, so expecting them to understand the finer points of economics is a bit mean.

Due to the way the game code handles size, stacks of 1 to 31 coins (of the same material) will all weigh the same. In other words, carrying 10 "stacks" of 1 gold coin will weigh 10 times as much as a single stack of 10 gold coins.

As a curiosity, coins with quality levels can show up in adventurer mode. Bandit leaders receive quality equipment, which often results in them carrying coins with improved quality. They can also be seen on the skeletal remains of certain sites and shrines "Shrine (megabeast)").

## Bugs

- Coins can, unusually, be melted and return more metal than was used to create them. E.g: Make 10 stacks of coins using 10 bars of the same metal, then melt down those 10 stacks of coins, and you'll have 11 bars of that metal. You can create even more bars of metal by splitting the stacks of coins, somehow (typically through the trading interface). This even works with Adamantine, which only requires 1 wafer to forge and returns 1.1 wafers when melted. Bug:6026
