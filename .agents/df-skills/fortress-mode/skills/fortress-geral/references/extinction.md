# Extinction

> Fonte: [Extinction](https://dwarffortresswiki.org/index.php/Extinction) — Dwarf Fortress Wiki (GFDL/MIT)

**Extinction** means one of two things in *Dwarf Fortress*.

## Sapient extinction

The first meaning of the word pertains to world generation: fighting between different sapient species may be so intense that a particular sapient species is wiped out entirely, going extinct in the process. Extinction events are exceedingly rare in larger worlds, but surprisingly common in pocket ones, where inter-species competition is at its fiercest. Sapient species that go extinct will obviously no longer trade with your dwarves, nor threaten them with ambushes or sieges. You can somehow still start a fortress mode game in a map vacated of any dwarves, but you will not receive any migrants beyond the first two (hard-coded) waves, nor any noble appointments (including the monarch). Conversely, if your fortress receives a third migrant wave, a dwarf trade caravan, or a monarch, then your civilization was not truly extinct, only "dying". Civilizations can remain "dying" for hundreds of years, and the game won't allow you to embark from an extinct civilization if any non-extinct civilizations are available, so a truly extinct civilization embark is fairly difficult to obtain, but not impossible.

On a smaller scale, landmass-specific extinctions can also occur, and although they are not nearly so dramatic as *mass* extinctions, and are in fact quite common, they can still affect your game. This usually happens on separated landmasses and islands inhabited by more than one sapient species below a certain area. Since civilizations cannot yet cross bodies of water that don't freeze over, such extinctions will affect your gameplay should you chose to settle on such a landmass. The effect of settling someplace inaccessible to dwarves is the same as starting a fortress when they are extinct: only two, hard-coded, migrant waves.

Calendar ages are greatly influenced by the relative lack or abundance of sapient life in your world, and so provide an at-a-glance view of the state of civilization on your lonely planet (if you know what they stand for, of course). Two calendar ages are more directly associated with extinction: the *Age of Death* and the *Age of Emptiness*, in which all civilizations have been wiped out. Actually getting these to happen can be difficult - the latter can only be achieved by killing every civilized creature in a world in Adventurer mode, then committing suicide, then embarking on the same map in fortress mode, then committing suicide with all of *those* dwarves. Once all of this is done, you will finally get an announcement telling you of the passing of the age. It's been done before.

## Site extinction

The second, more nuanced form of extinction has to do with the wildlife in your surroundings. Every site can have a certain number of creatures appear in it; *which* creatures depends on the site's biomes, *how often* depends on the `[FREQUENCY]` creature token in their raw files, *how many* depends on the number of biomes you abridge and on the creature's `[CLUSTER_NUMBER:#]`, and *how many before none will ever appear in the wild again* depends on a somewhat randomized token in specific creatures' definitions, the `[POPULATION_NUMBER:#:#]` tag. That is, if as many (wild, non-siege mount) creatures die or are captured and kept upon visiting your fortress as `[POPULATION_NUMBER]` is set to, they will be considered locally extinct, and will have their range clipped from your fortress surroundings.

This cap will not limit any breeding you do once you have captured the creature, and will obviously not affect any creatures visiting your site that are allowed to leave. It *will* affect the maximum number of non-breeding creatures that you can have at your fortress, however, and will not allow the appearance of creatures in clusters larger than are allowed by the cap. Note that the cap is biome-specific: even though sea serpents are capped at one serpent per site, it is possible to get multiples, and even start a breeding program, if your fortress abridges multiple valid biomes - note that such a breeding program wouldn't work in the current version, as sea serpents are now egg-laying and aquatic egg-layers don't breed due to a bug)

Every time a species becomes locally extinct it is (obviously) taken out of the wildlife visitation rotation. Rendering a policy of mass genocide on the countryside can thus eventually force the appearance of a sought-after species of wildlife, if you push hard enough. However, for the most part the number of creatures that can appear in the biome is so large, and the population caps are set so high, that it doesn't seriously affect gameplay. Aggressively hunting the local wildlife *will* eventually restrict its variety, however, and eventually you can prevent *any* wildlife from spawning at all on your map.

The cap does have important ramifications for a few specific species, however. Wildlife appearances on glaciers are heavily restricted, for instance, so the particularly aggressive yeti, which only appears five to ten times, is often made extinct very quickly. Because of a bug, aquatic vermin do not restock when fished, resulting in guaranteed eventual extinction. A certain nuance of the tag's implementation allows maintained hunting of certain species, with some micromanagement: if a cluster (or pack) of animals appears on the map, as long as at least one animal in that cluster is allowed to leave, the species will not have been considered depleted. This obviously does not work on solitary creatures. Another option is to capture a breeding pair and release their (untamed) young back into the wild; doing so can even raise the site population past its starting value.

### Natural regeneration

Supposedly, wildlife populations very slowly naturally repopulate due to continuous world-gen/world activities. Whether this can happen if they are locally extinct is unknown.

## Repopulating Site Extinction with DFHack

To fully bring back creatures from permanent extinction, the DFHack region-pops can help. The script is versatile, and when used correctly, can selectively weed out creatures a player does not want to bring back. This tool is not perfect, and with time, creatures you have weeded out may return. This may be due to a range limit, and does not take very long range migration into account.

To view which animals may spawn in your embark, use 'region-pops list-all'.

### Repopulation

To get started, first download the template here named 'region-pops.list' (credits to EldrickWT), and open it up with any text editor. The finished file should be structured like a .bat (all commands are stated before the options). By default, this scriptlet will remove every creature, which is not what we want. All we have to do is flip (or replace) the value into a positive number. Once done, save, copy and paste it in to the dfhack terminal. This script will restock all creatures with the value you inserted.

### Fine Tuning

With the basic repopulation done, you can fine-tune which creatures you don't want out with this part. Since a negative value removes creatures from the region, you can add below the last line, 'region-pops incr-all BIRD -X' to remove X from all creatures with 'BIRD' in its name. This also includes giant and animal person variants. Just remember to have the removing part at least larger than the repopulation part, to play it safe. Flying creatures often have a big impact on FPS, and removing them from your embark will definitely help. After saving the file, you can easily copy and paste your preferred region populations on every new playthrough.

There is (currently) no known script to repopulate civilizations.
