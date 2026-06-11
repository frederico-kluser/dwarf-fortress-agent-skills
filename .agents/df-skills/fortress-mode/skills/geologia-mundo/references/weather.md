# Weather

> Fonte: [Weather](https://dwarffortresswiki.org/index.php/Weather) — Dwarf Fortress Wiki (GFDL/MIT)

**Weather** refers to any type of weather effect in *Dwarf Fortress*. It includes snow, rain, and special features in evil surroundings. Additionally, one can observe clouds, fog/mist and the stars in adventure mode, however, they have no gameplay impact in fortress mode.

Weather conditions and event text seem to depend on the embark location in the world, biome and climate. For example, some winters can see extremely low temperatures with large amounts of snowfall, whilst summers may be scorchers.

Normal (non-evil) weather can be disabled by changing \[WEATHER:YES\] to \[WEATHER:NO\] in d_init.txt. Disabling weather is a quick and largely harmless fix to improve framerate on older machines if required.

## Normal weather

### Clouds (adventure mode only)

*Dwarf Fortress* has three layers of clouds: cumulus, cirrus, and stratus. When using the key in adventure mode, any number of messages about the weather may appear, and corresponding symbols are shown when is enabled on the fast travel mode. The types of clouds that are possible are:

- **Clear sky (no clouds)** — The sky is clear above you.

- **Scattered cumulus** — There are scattered puffy clouds above you.

- **Many cumulus (causes rain)** — There are mounds of clouds above you, smooth on the bottom with prominent upward bulges.

- **Cumulonimbus (causes rain)** — A dark, menacing cloud towers above you, crowned by an anvil.

- **Cirrus** — The sky is striped with high, thin clouds.

- **Altostratus** — The sky above you is hazy and white.

- **Stratus (causes rain)** — The sky above you is gray.

- **Nimbostratus (causes rain)** — The sky above you is a uniform and dark gray.

Additionally, some unique messages occur when there are clouds in multiple layers:

- **Scattered cumulus and cirrus** — There are scattered clouds underneath a striped sky.
- **Many cumulus and cirrus** — Mounds of clouds are clustered through a striped sky.
- **Cumulonimbus and cirrus** — A dark, towering cloud rises into a striped sky.
- **Altostratus and cumulonimbus** — A towering gray cloud descends from the white sky above you.
- **Stratus cumulonimbus** — The sky above you is completely gray, with dark cloud pillars pressing through it.
- **Nimbostratus and cumulonimbus** — The sky above you is nearly black, ripped through with towering clouds.

Otherwise, stratus clouds prevent you from seeing if there are any cirrus or cumulus clouds.

### Fog / Mist (adventure mode only)

Fog is another aspect of the weather, described separately from the state of clouds when using . (However, thick fog prevents you from being able to tell what the clouds are like via .) There are three kinds of fog that may appear:

- **Thin Mist** — There is a thin mist here.

- **Fog** — Fog enshrouds the area.

- **Thick Fog** — There is a heavy blanket of fog enveloping everything.

The symbols shown on the fast travel map are shown regardless of whether you have enabled or not. If you have cloud viewing enabled, clouds in the same position as the fog will obscure that fog. When in the midst of fog on the fast travel map, a small circle around your adventurer will blink to show the surrounding area.

### Precipitation

#### Rain

Rainfall occurs occasionally. Normal rain cleans any tile it lands on, removing blood, vomit and other bodily fluids on contact. Any dwarf caught outside when it rains will receive a minor unhappy thought.

When rain hits a tile labeled as a murky pool, it will begin to fill it up with 1/7 water, and if that does not evaporate, the water will grow deeper, until the pool is full. Murky pools do not overflow from rain, but this extra water can be drained off and stored or used. (See the Well Guide.) While not much, it can really help maps without 'unlimited' water supplies such as rivers and brooks.

#### Snow and Cold

If the temperature is cold enough, snowfall rather than rainfall will occur, and outside water will freeze, including murky pools and rivers. This can happen in winter months in a moderate biome, or at any time in freezing biomes like a tundra or glacier.

Amid snowfall, the ground, trees and other surfaces will gradually become covered in snow. Dwarves caught outside during a snowstorm can have bad thoughts as well as freeze to death, so a very high priority when embarking on a glacier is to dig out some place warm for your idlers to rest.

In the freezing cold, outside water will freeze into a wall of ice if at least 4/7 deep, or a floor otherwise. Freezing ice acts much like obsidian, and will instantly kill anything caught inside of it -- including creatures otherwise extremely hard to kill. In moderate biomes after winter has passed, ice will melt back into ponds. Ice walls will always thaw back into a full 7 units of liquid, regardless of the original water level, but ice floors will produce the original water depth when thawed.

Magma running under snow-covered ground will melt it, but unlike ice, molten snow doesn't turn into water.

### Wind

In a given embark tile biome, there are three wind-related variables tracked: East-West Wind, North-South Wind, and Wind Strength. East-West and North-South can be positive or negative, and Wind Strength is equal to the sum of their absolute values; so if East-West is -10, and North-South wind speed is 4, then Wind Strength is 14. Moreover, wind is uniform across the entire embark at any given time; Wind Strength does NOT increase the higher up you go.

East-West Wind is primarily driven by the latitude of the embark tile biome, and is modeled loosely after atmospheric circulation. For a given world, one end (either top or bottom) is the "pole" and the other is the "equator". According to Toady One in a Future of the Fortress thread, "the directions alternate over the latitudes and depend on the pole settings, and yeah, a no-pole world is treated like a N+S pole world". The following table gives the base East-West Wind value for a given latitude, by counting tiles from the pole-most tile.1

| Cell   | Pocket     | Smaller    | Small      | Medium       | Large        | Wind |
|--------|------------|------------|------------|--------------|--------------|------|
| Polar  | 0          | 0 thru 1   | 0 thru 3   | 0 thru 7     | 0 thru 15    | -15  |
| Polar  | 1          | 2 thru 3   | 4 thru 7   | 8 thru 13    | 16 thru 27   | -14  |
| Polar  | 2          | 4          | 7 thru 9   | 14 thru 19   | 28 thru 38   | -13  |
| Polar  | \-         | 5          | 10 thru 11 | 20 thru 22   | 39 thru 45   | -12  |
| Polar  | 3          | 6          | 12         | 23 thru 25   | 46 thru 50   | -11  |
| Ferrel | \-         | \-         | 13         | 26           | 51 thru 52   | +11  |
| Ferrel | \-         | \-         | \-         | 27           | 53 thru 54   | +12  |
| Ferrel | \-         | 7          | 14         | 28           | 55 thru 56   | +13  |
| Ferrel | \-         | \-         | \-         | 29           | 57 thru 59   | +14  |
| Ferrel | \-         | \-         | 15         | 30 thru 31   | 60 thru 62   | +15  |
| Ferrel | 4          | 8          | 16         | 32           | 63 thru 65   | +16  |
| Ferrel | \-         | \-         | 17         | 33 thru 34   | 66 thru 69   | +17  |
| Ferrel | \-         | 9          | 18         | 35 thru 36   | 70 thru 73   | +18  |
| Ferrel | \-         | \-         | 19         | 37 thru 38   | 74 thru 77   | +19  |
| Ferrel | 5          | 10         | 20         | 39 thru 41   | 78 thru 82   | +20  |
| Ferrel | \-         | \-         | 21         | 42 thru 43   | 83 thru 87   | +21  |
| Ferrel | \-         | 11         | 22 thru 23 | 44 thru 46   | 88 thru 92   | +22  |
| Ferrel | 6          | 12         | 24         | 47 thru 49   | 93 thru 98   | +23  |
| Ferrel | \-         | 13 thru 13 | 25 thru 26 | 50 thru 52   | 99 thru 104  | +24  |
| Ferrel | 7          | 14         | 27 thru 29 | 53 thru 58   | 105 thru 116 | +25  |
| Ferrel | \-         | 15         | 30         | 59 thru 61   | 117 thru 122 | +24  |
| Ferrel | 8          | 16         | 31 thru 32 | 62 thru 64   | 123 thru 128 | +23  |
| Ferrel | \-         | \-         | 33         | 65 thru 66   | 129 thru 133 | +22  |
| Ferrel | \-         | 17         | 34         | 67 thru 69   | 134 thru 138 | +21  |
| Ferrel | \-         | \-         | 35         | 70 thru 71   | 139 thru 143 | +20  |
| Ferrel | 9          | 18         | 36         | 72 thru 73   | 144 thru 147 | +19  |
| Ferrel | \-         | \-         | 37         | 74 thru 75   | 148 thru 151 | +18  |
| Ferrel | \-         | 19         | 38         | 77           | 152 thru 155 | +17  |
| Ferrel | \-         | \-         | 39         | 78 thru 79   | 156 thru 158 | +16  |
| Ferrel | 10         | 20         | 40         | 80           | 159 thru 161 | +15  |
| Ferrel | \-         | \-         | 41         | 81 thru 82   | 162 thru 164 | +14  |
| Ferrel | \-         | \-         | \-         | 83           | 165 thru 166 | +13  |
| Ferrel | \-         | 21         | 42         | 84           | 167 thru 168 | +12  |
| Ferrel | \-         | \-         | \-         | 85           | 169 thru 170 | +11  |
| Hadley | \-         | \-         | 43         | 86           | 171 thru 172 | -13  |
| Hadley | \-         | \-         | \-         | 87           | 173 thru 175 | -14  |
| Hadley | 11         | 22         | 44         | 88 thru 89   | 176 thru 178 | -15  |
| Hadley | \-         | \-         | 45         | 90           | 179 thru 181 | -16  |
| Hadley | \-         | 23         | 46         | 91 thru 92   | 182 thru 184 | -17  |
| Hadley | \-         | \-         | 47         | 93 thru 94   | 185 thru 188 | -18  |
| Hadley | 12         | 24         | 48         | 95 thru 96   | 189 thru 192 | -19  |
| Hadley | \-         | \-         | 49         | 97 thru 99   | 193 thru 198 | -20  |
| Hadley | \-         | 25         | 50         | 100 thru 101 | 199 thru 202 | -19  |
| Hadley | \-         | \-         | 51         | 102 thru 103 | 203 thru 206 | -18  |
| Hadley | 13         | 26         | 52         | 104          | 207 thru 209 | -17  |
| Hadley | \-         | \-         | 53         | 105 thru 106 | 210 thru 212 | -16  |
| Hadley | \-         | \-         | \-         | 107          | 213 thru 215 | -15  |
| Hadley | \-         | 27         | 54         | 108 thru 109 | 216 thru 218 | -14  |
| Hadley | \-         | \-         | 55         | 110          | 219 thru 220 | -13  |
| Hadley | 14 thru 16 | 28 thru 32 | 56 thru 64 | 111 thru 128 | 221 thru 256 | 0    |

Note: negative values indicate east-to-west winds, while positive values indicate west-to-east winds.

In addition to east-west wind from latitude, certain parts of the world experience "mountain/valley winds and sea breezes"2. Such locations will receive additional wind each morning (corresponding to between 3:00 AM and 7:00 AM, and between 6:00 AM and 9:00 AM) and each afternoon (both corresponding to between 3:00 PM and 6:00 PM). A gust of wind affects both the east-west and north-south wind speeds, adding or subtracting 10 from each. The afternoon gust is always the opposite of the morning gust, so if the morning gust was +10 east-west and -10 north-south, the afternoon gust will be -10 east-west and +10 north-south.

Currently, wind primarily interacts with windmills to generate power. A total wind strength of between 1 and 14 generates 20 power, and between 15 and 29 generates 40 power. A total wind strength of 30+ generates 60 power, but this is currently only briefly achievable during gusts. In addition, wind affects the message you get when checking for the weather as an  adventurer.

## Evil weather

Certain evil surroundings feature freakish weather, such as fogs, clouds, and rains. They may afflict those caught in them with various kinds of syndromes or curses, such as poisonings or transformation into zombies. Names for evil weather are randomly generated, typically something along the lines of "abominable mist", "unholy gloom" (clouds) or "creeping murk", "horrid goo" (rain). Materials tainted by evil weather goo will appear as 'slimy'.

Evil weather does not count as true "weather" for all purposes: most notably, disabling weather in d_init.txt will not disable evil weather.

Two kinds of evil weather exist: evil rain and evil clouds. The types of weather effect and their associated syndromes (if any) are different and randomly chosen for every evil biome in a generated world. There will be at most one weather effect for a given evil biome, sometimes in conjunction with the effect of corpse animation.

### Evil clouds

Evil clouds are made of a generated inorganic gas or dust. They start in one tile and spread out in a similar manner to miasma vapor; when the game announces the cloud's presence, it will zoom in to this tile. Evil clouds cause more serious syndromes than evil rains, similar to those of forgotten beasts, titans and demons. Certain evil clouds transform living beings caught in them into dangerous zombie-like thralls, turning them against all life while significantly increasing their strength and toughness attributes.

Evil clouds inflict worse syndromes than evil rains; thralling clouds are especially dangerous in the extreme, as the zombies produced are much stronger than those produced via ambient effects. These undead are very hard to kill and are **much** stronger than their original forms. Evil clouds have a tendency to roll over your outdoor trade depot and convert traveling merchants into a band of dwarf-hungry savages, which can be quite fun to a fortress reliant on trade.

If you wish to embark to an evil biome that has thralling/husking clouds, a few options are available:

1.  You can inspect the world manually after it is created. In order to do this, you will need to turn off compressed saves in init.txt. Then enter advanced world generation, set the number of evil rain types to "none" and the number of evil cloud types to 1. Generate a world, quit, then open \`\`world.dat\`\` in the region folder. Locate \`\`\[INORGANIC:EVIL_CLOUD_1\]\`\`, then check the syndrome right after it. If this syndrome doesn't have Thralls, Husks, or Zombies, gen a new world and try again. This is much faster than embarking 20 times in a row, and you can make sure you will get dust if you prefer it over fog.
2.  DFHack's \`\`embark-assistant\`\` plugin can help find these types of biomes when run from the embark screen.
3.  You can change what evil weather a biome has with the DFHack script biomemanipulator, and/or use \`\`gui/gm-editor\`\` to change what evil weathers there are.

Thralling clouds are also dangerous in adventure mode: this particular form of undead status means inherent hostility from civilized beings, reduced speed and no regeneration. However, other undead will, as usual, ignore you.

### Evil rain

Evil rain can be made of either the blood of a civilized race (most famously elf blood, but it can rain dwarf blood and others) or a randomly generated inorganic substance. Blood rain typically causes no syndromes, only giving whoever is caught in it an unhappy thought. Generated substances are more dangerous, causing minor symptoms such as vomiting and fevers, as well as inspiring the aforementioned unhappy thought. Evil rain can also cause wounds and injure dwarves and other creatures caught in them, although the extent of injury depends on the substance. Some forms of evil rain, such as those that cause blisters, will lead to instant fun as a blistered brain means death. Cats, birds, and other livestock dying after being exposed to evil rain indicates that dwarves may be next. Dwarves spattered with evil rain will seek a bath after any outdoor work, wasting time and soap. There are rumors of rain composed of other substances, such as alcohol and vomit; however, these seem to be rare.

### Dangers of evil weather

One of the dangers of evil weather is that ponds will never refill. Store water into underground basins and plan accordingly. Another annoyance is the total lack of wild bees in an evil climate. Though evil rains (excluding rains of blood) usually cause the "milder" types of syndromes, these may still cause death as a secondary result of that syndrome: e.g. suffocation from blisters, dehydration from chronic nausea.

Some evil weather effects condense on creatures, making their effects semi-permanent - symptoms won't go away until the source is washed. Those effects also can spread like a disease. In most cases, it will just infect dwarves that carry contaminated bodies to caskets. Thralling dust clouds, however, can quickly lead to an unstoppable zombie apocalypse if the dust is not completely washed off somehow.

#### Movement of evil weather and safeguarding

Evil weather forms within about 30 tiles of the edge of the map (or edges of evil biomes within the map), and moves about the screen in one direction as the wind blows. Their structure is a series of miasma-like bursts of cloud that are spawned along the path of the cloud's invisible center. Because the clouds inflate similarly to miasma and because the direction they move in is random, they can very quickly dissipate, fly out of the map immediately, carry on at a steady pace, or spread rapidly to engulf very large areas. They will not, however, change direction.

Clouds pose a serious threat to dwarves (and from there, entire fortresses), even if your citizens seem to be inside safe structures. However, clouds' movement methods can be exploited, and buildings need not be limited to hermetically-sealed pillboxes if you're careful.

Although a cloud will glide uninterrupted along a single Z-level, it will teleport to the top of straight walls and pass over structures. As a result, a cloud will climb any hills and fortresses in its way with ease. Closed doors, raised drawbridges, and walls will keep the billowing parts out of buildings, but the movement of the cloud is mostly dependent on which tiles are marked "outside." Clouds will not propagate inside a roofed area, although already-started miasma-like bursts can billow under the edges of such places if there are no walls to stop them, or if there are open windows in those walls. Clouds can also teleport down from an open roof (it only takes one tile of open stairwell for a small segment of cloud to teleport down and burst upon the bottom floor of your tower.) They will pass through fortifications with ease, although they'll never spawn inside a roofed fortification; a cloud must billow in from somewhere else in that case. For this reason, do not make windows that are one the same z-level as the rooftops of adjacent buildings or natural features. It is safe, for instance, to make a tall, isolated tower and give its middle levels windows with no protection whatsoever, because the clouds teleport rather than climb, and will not teleport to any inside area. They would go directly to the roof without bothering the levels in between. This could be multiplied to make something like New York with complete impunity, so long as all the rooftops are at the same height.

If you choose to fortify outside, either be extremely careful with your designs, or be sure to have any open areas secured with floodgates, doors, or bridges to act as shutters to keep the clouds out. Adding doors throughout the structure to stop any accidentally-contained clouds from moving further inward does not hurt. It is important to emphasize that no rooftop will ever be safe.

An evil cloud will dissipate rapidly at the border of evil with non-evil biomes, but if there is more evil biome on the other side of the non-evil biome, the same cloud can and will eventually spring up over there; clouds do not necessarily die when they disappear, depending on the map. They can phase through non-evil biomes, and will move invisibly across the non-evil biome(s) at the same rate that they would across evil biomes.

It should be noted that attempting to make an open-roof barracks or tavern to prevent cave adaptation is extremely risky, even more so in a mixed-biome embark because the hazards of evil clouds are not immediately obvious. It would seem that the temporary disappearing effect of evil clouds when it attempts to cross a non-evil area is overwritten if it sweeps across constructed or otherwise modified floors (i.e. channeled out, roofed, or walls). This means erratic teleporting of the cloud depending on how much you've constructed but always means that any roofs are not safe. It also means the clouds will "appear" to linger on top of constructed surfaces, even if said surfaces are not in the evil part of the area.

The only part that the cloud will not reach when it interacts with constructed walls is that it cannot touch the natural surface tiles within the walls that are the courtyard if the area is non-evil. Constructed surfaces and possibly channeled out areas are fair game for the cloud to spread. It's unknown if clouds will originate within modified tiles that are within non-evil areas of the map.

For unknown reasons, clouds will not teleport up multi-tile trees, but will pass uninterrupted below their boughs. This will not be true for anything you build, implying that any "outside" tile is dangerous, as trees provide support and elevation without changing which tiles are exposed to the outside.

Undead created by evil weather gain immediate strength bonuses and acquire a status of . They will tirelessly seek out living things to kill until they are struck down, which can take considerable effort.

## Good Weather

It has been observed that in biomes where the alignment is "good", there exists a possibility that it may rain alcohol. However, this is not actually the case. When using a tavern, dwarves will sometimes spill alcohol. When a dwarf walks through the resulting spatter, it will contaminate their clothes. When a contaminated dwarf then walks outside during rain, the alcohol will wash off, forming pools on the ground that can also be tracked through and spread, giving the impression that it is “raining alcohol”.

Theoretically, this may be made by modding interactions, but wasn't verified by testing.

## Bugs

- Different biomes can exist in layers above the surface. This can lead to odd behavior like evil rain above a "good" biome.

Humans have attempted to predict the weather from time to time, to unusually bad results. Dwarven scholars absentmindedly noted that they could do it better, which caused a war from the completely unrelated cause of sock-making procedures. Dwarves *would* probably still do it better though, that is, if it rains tonight.
