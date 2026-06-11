# System requirements

> Fonte: [System requirements](https://dwarffortresswiki.org/index.php/System_requirements) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

!!UNKNOWN!!  · xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*If you're looking for information on improving the performance of Dwarf Fortress on your computer, see Maximizing Framerate. For installation instructions, see Installation.*

*Dwarf Fortress* is a very complex game, but in ways that differ from most other complex games. This leads to the game having a somewhat unusual set of requirements.

Note that while the front page displays only the current builds, there also exist previous versions under the "All Versions" link.

## Premium version official requirements

From the Steam page

**Windows**

- Requires a 64-bit processor and operating system
- OS: minimum Windows 7 or later
- Processor: minimum Dual Core CPU - 2.4GHz+, recommended Dual Core CPU - 4GHz+
- Memory: 4 GB RAM
- Graphics: 1GB of VRAM: Intel HD 3000 GPU / AMD HD 5450 / Nvidia 9400 GT
- Storage: 500 MB available space

**SteamOS + Linux**

- None listed on the Steam page yet, but it should work on Ubuntu 22.04 LTS or later and other up to date Linux distributions.

## OS

- **64-bit Windows** can run the Premium and Classic releases natively. 32-bit and ARM versions of Windows will not be able to run DF. If you are unsure if you are using 64-bit Windows, check using the instructions here.
  - Windows Vista/7/8/8.1 are unsupported by Microsoft and may have issues -- be warned!
- **Linux on x86-64** (including **SteamOS**) can run the Premium version of Dwarf Fortress on Steam natively, though there may be issues that may or may not be fixed by using Proton.
- **Linux on x86-64** and **MacOS on Intel** may be able to run Dwarf Fortress via Wine, previous versions are rated Platinum on Wine's AppDB. Some find this to be more stable than the native Steam Linux version.
- **MacOS on Apple Silicon** (listed here) has worked for some people by running Dwarf Fortress via Wine in Rosetta 2's x86-64 emulation. Add your experiences below under Reports if you try! See the installation page for details.
- '*Linux ARM64* native builds, as of v50.13, are not yet published. The MacOS native build for v50+ has been cancelled for the time being (See the Kitfox FAQ).

## GPU

*Dwarf Fortress* is not particularly graphically intensive, even when using high-res tilesets and graphics sets. *Dwarf Fortress* also doesn't use technologies like OpenCL to make use of graphics cards anyway, so a top-of-the-line graphics card will generally not improve performance.

## CPU

*Dwarf Fortress* mostly operates on a single thread, so if you want to optimize for DF, you should probably optimize for single-core performance. This is especially true if you want to do more laggy things, such as mist generators. However, laggy circumstances are generally the exception, not the rule, and in those other circumstances, you generally don't need a *particularly* powerful CPU.

### Cache size

As *Dwarf Fortress'* bottlenecks are mostly due to cache misses, it has been speculated on the DF forums that "a CPU with a positively giant L3/L4 cache (and I mean \> 256 mb or GTFO)" would improve DF performance, as would using faster RAM with smaller transfer times—see the next section.

## RAM

During regular gameplay, *Dwarf Fortress* usually doesn't consume too much memory - 512MB is probably a bit tight, but 1GB is absolutely sufficient, though if you're short on RAM, you may want to quit other running processes. What's particularly important during regular gameplay is RAM *latency*—since the game uses the RAM *every single frame*, it's important that your RAM be fast, lest you experience FPS death.

However, world generation is known to eat up a lot more RAM than normal gameplay, especially if you generate worlds that are particularly large or have long histories - multiple gigabytes may be consumed. To be safe, you should shut down any background processes when generating a world, and if you're particularly tight on RAM, consider reducing the size or history of the worlds you generate—the game is rich enough with content that you'll still have plenty of things to do, and you can always tweak the other, less RAM-hungry advanced world generation parameters. (RAM latency is less of a problem here, since you'll only need to do this once every so often.)

## Experimental reports

### Report format

Please read the report template page before contributing any reports.

### Reports

Configuration type: RAM-upgraded MacBook Pro (13-inch, Late 2011)

Game info
Game version: v50.12-beta8

World size: Small

Embark size: 4x4

Age of fort: 8 years

Number of dwarves: 193

Average fps: 32 (18 graphical)

Default/nondefault raws: default

Tileset in use: Steam

Amount of stone dug: ~3000

Amount of water and state: inactive magma pump stack, no water

Approximate amount of z-levels: 30

RAM usage of game: 1622 MB

Draw mode in init.txt: Auto

PC info
CPU: Intel Core i7-2640M @ 2.8 GHz

RAM: 16 GB DDR3 @ 1333 MHz

GPU: Intel HD Graphics 3000

OS: Windows 10 under Boot Camp

------------------------------------------------------------------------

Configuration type: Self-build pc from 2024

Game info
Game version: v51.08

World size: Medium

Embark size: 4x4

Age of fort: 27 years

Number of dwarves: 204

Average fps: 47(47 graphical) with temperatures, 68 (49 graphic) without temperatures.

Default/nondefault raws: DFHack

Tileset in use: Steam

Amount of stone dug: ~10000

Amount of water and state: Non flowing ocean (75% of surface) + 2 flooded cavern layers (nearly entire cavern flooded). Light aquifer powered mist generator spanning ~100 Z levels.

Approximate amount of z-levels: ~130

RAM usage of game: 2978 MB

Draw mode in init.txt: Auto

PC info
CPU: AMD Ryzen 7 7700X

RAM: 32GB DDR5 @ 6000 MHz

GPU: RTX 3060 (slight overclock)

OS: Windows 10 Pro

|  |
|----|
| "System requirements" in other / Languages / Dwarven / : / idith inem / Elven / : / eritha enotho / Goblin / : / obsår eted / Human / : / histek tikes |
