# Duplicated raws

> Fonte: [Duplicated raws](https://dwarffortresswiki.org/index.php/Duplicated_raws) — Dwarf Fortress Wiki (GFDL/MIT)

**Duplication of raw file entries** is a type of game bug, widely known in the community, due to the bizarre effects this particular bug has on world generation. It is usually caused by a modding accident, though some players duplicate raws on purpose to create a crazy glitched world.

The exact effects of the bug happen at the end of worldgen, and vary depending on type and amount of duplicated raw entries.

## Overview

The term refers to the duplication of game object definitions present in the game's raw files. The presence of raw entries (such as `[CREATURE:DWARF]`) being defined more than once causes internal numeric IDs of the target type to be misattributed during the initial save, resulting in each pointer after the point of duplication being shifted one entry forward. Definitions before the point of duplication are unaffected. The effects are cumulative when more than one duplicated entry is present.

If the game finds any duplicated raws when loading a save, it writes an appropriate message in errorlog.txt per each duplicated entry.

## Duplicated creatures

Duplication of creature raws results in the wrong creatures appearing in the wrong places and assuming the wrong roles during gameplay, with many messy and/or hilarious results. It has been known to cause cave crocodiles to live in houses, civilizations of elephants to form, camels to wear clothes, fluffy wamblers to pull wagons, and so on. It also causes creature materials to glitch, which likely results in civilians wearing clothing made out of liver tissue, chicken teeth, soap, or "unknown frozen creature substance", to name a few, and other weirdnesses, such as llama eggs being available on embark.

This type of raw file duplication is very prone to spontaneous crashing, and duplicating all creatures will almost certainly result in a crash during worldgen, so it's not advised to do this during regular play.

## Duplicated plants

One of the most visible results of duplicated plant raws is a complete lack of trees. Other vegetation will likely be replaced by uniform dark green grass composed of non-grass plants, or generic grass like that from before the v0.31.19 release.

Plant materials, notably wood, will be screwed up the same way creature materials are in creature raws duplication - that is, your would-be wooden items will be composed of plump helmets, frozen booze, dye, or "unknown frozen plant substance". Other plant-derived items will be affected as well.

## Duplicated materials

Duplication of inorganic material raws results in wrong materials forming geological layers and inclusions, some of which normally don't appear within the world's crust. These can produce unusual resources when mined, such as metal boulders. Below is the list of what materials you can encounter, and how you can put them to use.

n.b. Although duplication of "default" (rather than 'inorganic') materials have been a feature of a few mods for quite some time, and there have been no verified bugs directly related to this, the developers of the game have assured the community that these definitely will be causing errors, even if they are not immediately apparent to players.

### Displaced minerals, soils, and metal layers

The amount of displaced minerals will depend on the place in which raw file duplication has occurred - sometimes, you can even find entire layers composed of usable ore.

Soil, sand, and clay tiles can also be displaced, which will likely result in aquifers being generated in unexpected places, such as in mineral deposits. The tiles themselves will be unusable in sand/clay production, however, unless they happen to form the entire layer.

Contrary to what you might think, metal layers produce metal *boulders* when mined, which can either be melted into a meager amount of metal bars, or directly made into short swords, the same way obsidian swords are made.

### Evil weather materials

Evil weather materials have no melting or boiling point, and, thus, will always be mined as solids. These can be used either as basic construction material, or in jewelry, but not stoneworking. Note that mining them and working with created 'boulders' is perfectly safe, but cave-in dust **will** transfer any syndromes of the material, likely turning the majority of your population into undead husks.

### Divine fabric

While not fire-safe, divine fabric has an astonishingly-high base value of 300, making it perfect for decoration. Unfortunately, 'boulders' composed of it cannot be processed into thread, being workable only at a jeweler's workshop.

### Divine metal

This metal of the gods is completely impervious to heat, and superior to anything other than adamantine. Mined boulders of it can be processed the same way as boulders of other metals, discussed above.

### Undefined materials

If a given region's list of geological layers ends up not containing any Stone or Soil materials, the corresponding terrain tiles will rapidly flicker between **all** possible inorganic materials. Attempting to designate such Wall tiles will randomly fail whenever the game picks an undiggable material such as slade (and successfully-designated tiles may randomly fail to mine with "Inappropriate dig square" for the same reason), and successfully mining one will produce a completely random result, with gem materials yielding rough gems and everything else yielding boulders.

## Gallery

 ground.gif\|Flickering tiles are one of the effects of material duplication.  embark screen can be used to inspect material weirdnesses.  vegetation in a world with duplicated plants.  stone layer composition, characteristic to worlds with duplicated minerals.  artifact created in a world with duplicated raws.
