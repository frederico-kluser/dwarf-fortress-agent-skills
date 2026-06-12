# DFHack live bridge — setup & troubleshooting (Linux)

> Fonte: docs.dfhack.org (DFHack 53.x) e github.com/DFHack/dfhack — artigo manual desta
> skill (não é extrato da wiki). License: MIT. Snapshot: 2026-06.

## What the bridge is

Two independent channels into a running Dwarf Fortress on Linux:

- **Read** — the game appends every announcement to `gamelog.txt` in the DF root
  directory. Tailing that file works even without DFHack installed.
- **Write** — DFHack embeds an RPC server (localhost TCP, port 5000 by default) that
  accepts console commands from outside the game. That is exactly what the bundled
  `dfhack-run` binary does, and what the `df_bridge.py` script (in the `scripts/`
  directory shipped with these skills) speaks natively as a fallback.

## Requirements

- **Native Linux build** of Dwarf Fortress (Steam app `975370`). If the install only
  contains `Dwarf Fortress.exe` (no `dwarfort` binary), the game is running through
  Proton and the Linux DFHack build does not apply — see Troubleshooting.
- **Matching versions.** DFHack releases only support the DF version they are named
  after (DFHack `53.14-r2` ↔ DF `53.14`). After Steam updates the game, update DFHack.

## Install — route A: Steam (recommended)

1. In Steam, search for **"DFHack - Dwarf Fortress Modding Engine"** (free, app id
   `2346660`) and install it.
2. Launch the **DFHack** entry in your library instead of Dwarf Fortress — it starts
   the game with DFHack loaded.
3. Steam keeps DF and DFHack version-matched automatically.

## Install — route B: manual tarball

1. Download `dfhack-<tag>-Linux-64bit.tar.bz2` from
   `https://github.com/DFHack/dfhack/releases` (pick the tag matching your DF version).
2. Extract it into the DF root directory so that `hack/` ends up **next to** `data/`:

       tar -xf dfhack-<tag>-Linux-64bit.tar.bz2 -C "~/.steam/steam/steamapps/common/Dwarf Fortress"

3. The `install_dfhack_linux.sh` script in the bundled `scripts/` directory automates
   all of this (detection, download, validation, extraction) — run it with `--dry-run`
   first to see the plan.

Default Steam locations on Linux: `~/.steam/steam/steamapps/common/Dwarf Fortress`,
`~/.local/share/Steam/steamapps/common/Dwarf Fortress`, or (flatpak Steam)
`~/.var/app/com.valvesoftware.Steam/.local/share/Steam/steamapps/common/Dwarf Fortress`.
Extra library folders are listed in `steamapps/libraryfolders.vdf`.

## Launching DF with DFHack

- From a terminal: `cd "<DF dir>" && ./dfhack` — the terminal becomes the DFHack
  console (close the game to end the session).
- Startup commands: arguments beginning with `+` run as console commands, e.g.
  `./dfhack +unpause +"prospect all"`.
- Disable for one session: `./dfhack --disable-dfhack`.
- Steam route: just press Play on the DFHack library entry.

## The remote protocol (write channel)

- The RPC server listens on **localhost, TCP port 5000** as soon as DFHack starts —
  no game-side configuration needed for local clients.
- Config file: `dfhack-config/remote-server.json` in the DF directory:
  `"port"` (default `5000`) and `"allow_remote"` (default `false` = localhost only;
  leave it that way unless you know what you are doing).
- The `DFHACK_PORT` environment variable overrides the configured port for both the
  server and the `dfhack-run` client.
- `dfhack-run <command> [args…]` (binary in the DF root) sends one console command
  and prints the console's reply. The bridge script uses it when available and falls
  back to speaking the protocol directly over TCP.

## gamelog.txt (read channel)

- Plain text, append-only, one announcement per line, English, in the DF root.
- Created the first time the game runs; it grows forever (players sometimes delete it
  to trim — the bridge detects truncation/rotation and restarts cleanly).
- Works in both Fortress and Adventure mode, with or without DFHack.

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `connection refused` on port 5000 | game not running, or started without DFHack | launch via `./dfhack` (or the Steam DFHack entry), then retry |
| port answers but handshake fails | another service is squatting on the port | set `"port"` in `remote-server.json` or `DFHACK_PORT`, retry with the new port |
| game crashes on launch after manual install | DFHack tag does not match the DF version | install the release named after your DF version |
| only `Dwarf Fortress.exe` in the DF dir | Windows build via Proton | switch DF to the native Linux build (Steam → Properties → Compatibility, untick Proton), or use the Steam DFHack app which handles the Windows build |
| `gamelog.txt` missing | game never ran on this install | run the game once |
| `permission denied` extracting the tarball | DF directory owned by another user/readonly | fix ownership or rerun with appropriate permissions |
| commands hang / time out | game is frozen or busy (worldgen, saving) | wait and retry; check the game window |

## Links

- Installing DFHack: https://docs.dfhack.org/en/stable/docs/Installing.html
- Remote interface internals: https://docs.dfhack.org/en/stable/docs/dev/Remote.html
- Releases: https://github.com/DFHack/dfhack/releases
- Steam app: https://store.steampowered.com/app/2346660
