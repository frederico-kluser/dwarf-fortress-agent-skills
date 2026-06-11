# Dwarf Fortress Agent Skills

> A complete **Agent Skills** knowledge base for [Dwarf Fortress](https://www.bay12games.com/dwarves/), built from the official [Dwarf Fortress Wiki](https://dwarffortresswiki.org) — **no RAG, no embeddings, no vector database**. Just plain Markdown + progressive disclosure + `ripgrep`.

[![License: GFDL & MIT](https://img.shields.io/badge/content-GFDL%20%26%20MIT-blue)](#attribution--license)
[![Articles](https://img.shields.io/badge/articles-5694-green)](#whats-inside)
[![Modes](https://img.shields.io/badge/modes-adventure%20%2B%20fortress-orange)](#two-game-modes)

## What is this?

This repo turns the ~10k-article Dwarf Fortress Wiki into a set of **Agent Skills** that any LLM coding agent (Claude Code, Cursor, Codex, or a custom OpenRouter agent) can load to answer gameplay questions accurately — **without inventing mechanics from memory**.

Instead of a heavyweight RAG pipeline (chunking → embeddings → vector store → reranker), it uses the **progressive disclosure** pattern:

1. **Level 1 — Router metadata.** Tiny `SKILL.md` files (just `name` + `description`) tell the agent *when* a skill is relevant.
2. **Level 2 — Category instructions.** When a category is relevant, the agent loads its `SKILL.md`, which contains an index of articles.
3. **Level 3 — Reference articles.** The agent reads **only** the specific Markdown article(s) it needs.

Lexical search over the ~5.7k Markdown files is done with `ripgrep` — for this corpus size it's faster, simpler, and far more transparent than a vector store.

> **Why not RAG?** For a fixed, ~33 MB documentation corpus, `ripgrep` retrieval is instant, deterministic, and needs zero infrastructure. The agent sees exactly which file it's reading and can cite the source wiki page. See [`docs/why-not-rag.md`](#design-notes) below.

## Two game modes

Dwarf Fortress has two very different ways to play, so the knowledge base is split into **two self-contained skill trees**. A top-level router first asks the player which mode they're in:

| Mode | Description | Articles | Categories |
|---|---|---|---|
| 🗺️ **Adventure Mode** | First-person roguelike: create a character, travel, explore sites, talk to NPCs, fight | 2,642 | 8 |
| 🏰 **Fortress Mode** | Manage a dwarven fortress: labors, industry, construction, trade, defense | 3,052 | 12 |

**Shared content** (creatures, combat, materials, geology, health, modding, interface) is **duplicated into both trees**, so each mode is fully portable and self-sufficient.

## Structure

```
.agents/df-skills/
├── SKILL.md                 # 🧭 MASTER router — asks: Adventure or Fortress mode?
├── README.md                # detailed docs + rebuild instructions
├── scripts/
│   └── search.sh            # local lexical search (ripgrep) — the "retriever"
├── adventure-mode/
│   ├── SKILL.md             # mode router: situation → category
│   └── skills/<category>/
│       ├── SKILL.md         # category index: when to use + article list
│       └── references/*.md  # one wiki article per file
└── fortress-mode/
    ├── SKILL.md
    └── skills/<category>/...
```

### Categories

| Category | Modes | Covers |
|---|---|---|
| `combate` | both | weapons, armor, wounds, syndromes, military |
| `criaturas` | both | animals, megabeasts, races, bestiary |
| `materiais` | both | metals, stone, gems, material properties |
| `geologia-mundo` | both | biomes, stone layers, worldgen, locations |
| `saude-alimentacao` | both | food, drink, hospital, diseases |
| `modding` | both | raw tokens, tilesets, init files |
| `interface-controles` | both | keys, menus, designations (v50) |
| `industria` | fortress | smithing, farming, brewing, crafting |
| `construcao` | fortress | workshops, furniture, traps, mechanisms |
| `dwarves-gestao` | fortress | labors, moods, nobles, justice |
| `comercio-economia` | fortress | trade, caravans, wealth |
| `fortress-geral` | fortress | defense, events, overview |
| `adventure-geral` | adventure | character creation, travel, conversation |

> Category `SKILL.md` descriptions are in Portuguese (the project's working language); article content is the original English wiki text.

## How an agent uses it

```
1. Load  SKILL.md                                  → confirm Adventure vs Fortress mode
2. Load  <mode>/SKILL.md                            → route situation → category
3. Load  <mode>/skills/<category>/SKILL.md          → pick the article from the index
4. Read  <mode>/skills/<category>/references/*.md   → answer, citing the source page
```

When the agent doesn't know the exact file, it searches locally:

```bash
bash scripts/search.sh all "steel armor"               # both modes
bash scripts/search.sh adventure-mode "bleeding"        # one mode
bash scripts/search.sh fortress-mode/industria "magma"  # one category
```

## Installation

**Claude Code / Cursor / Codex (native skills):**

```bash
# personal (all projects)
cp -r .agents/df-skills/* ~/.claude/skills/
# or per-project, versioned in git:
mkdir -p .claude/skills && cp -r .agents/df-skills/* .claude/skills/
```

(Cursor → `.cursor/skills/`, Codex → `~/.codex/skills/`.)

**Custom OpenRouter agent:** implement the three disclosure levels yourself — inject the `name`+`description` catalog into the system prompt, expose `load_skill` / `read_skill_file` / `search_skills` tools, and let the model decide what to load. See `.work/` for the data layout the tools should read.

## How it was built

The whole pipeline lives in [`.work/`](.work) and is fully reproducible:

```bash
# 1. download the prebuilt dump (WikiTeam, 2023-11-07, ~31 MB compressed)
curl -L -o df-history.xml.zst \
  "https://archive.org/download/wiki-dwarffortresswiki.org-20231107/dwarffortresswiki.org-20231107-history.xml.zst"
zstd -d --long=31 df-history.xml.zst -o .work/df-history.xml

# 2. run the pipeline (Python venv with: mwparserfromhell mwxml pyyaml)
.venv/bin/python .work/parse_dump.py          # XML → pages.jsonl (dedupe Main/DF2014)
.venv/bin/python .work/extract_taxonomy.py     # mine 157 real {{category}} tags
.venv/bin/python .work/build_skills.py         # clean wikitext + pandoc → gfm → references/*.md
.venv/bin/python .work/build_dispatchers.py    # generate search.sh + routers
```

**Pipeline stages:**

1. **Collect** — prebuilt XML dump from the Internet Archive (WikiTeam scan, 2023-11-07).
2. **Parse** — `mwxml` over the all-revisions dump, deduplicating pages by `(namespace, title)` and keeping the latest revision. The `Main` (v50) and `DF2014` (v0.47) namespaces are merged per title, preferring the more complete version (the Nov-2023 dump caught the v50 migration mid-flight).
3. **Clean** — `mwparserfromhell` strips navigation/infobox templates; `[[File:]]`, interwiki links, and category tags are removed; HTML/entities are decoded.
4. **Convert** — `pandoc -f mediawiki -t gfm-raw_html` produces clean GitHub-Flavored Markdown (links flattened to plain text, images dropped).
5. **Classify** — 157 real `{{category|X}}` tags are mapped to 13 high-level skill categories, each assigned to fortress, adventure, or both.
6. **Generate** — per-category `SKILL.md` with navigable index, per-mode routers, the master router, and the `ripgrep` search script.

Dependencies: `pandoc`, `zstd`, `ripgrep`, and a Python venv with `mwparserfromhell mwxml pyyaml`.

> The 2.2 GB raw XML dump and large intermediate JSON files are **gitignored** — only the generated skills and the build scripts are versioned.

## Design notes

- **No embeddings on purpose.** ~5.7k Markdown files fit trivially in `ripgrep`'s wheelhouse; retrieval is sub-second and the agent can cite the exact source file. A vector store would add infrastructure and opacity for zero benefit at this scale.
- **Version targeting.** Content reflects **v50 / v0.47**. Where Main (v50) and DF2014 (v0.47) describe the same mechanic, the larger/more-complete page wins. Agents are instructed to assume **v50** on ambiguity and flag it.
- **"Pushy" descriptions.** Router `description` fields use assertive language ("Use SEMPRE que…") to combat under-triggering — the common failure mode for skills.

## Attribution & License

- **Wiki text** is licensed under **GFDL & MIT** ("All editors publish their contributions under the GNU Free Documentation License and the MIT License") — reusable with attribution. Every generated article links back to its source wiki page.
- **Game-derived data** (raw tokens, etc.) is © 2002–2026 **Tarn Adams / Bay 12 Games**.
- The **build scripts** in this repo are released under the **MIT License** (see `LICENSE`).

This is an unofficial, community resource and is not affiliated with Bay 12 Games.

## Contributing

Issues and PRs welcome — especially:
- improved taxonomy mappings (`.work/taxonomy.py`),
- cleaner wikitext→Markdown conversion edge cases,
- a refreshed dump from a newer wiki snapshot (v50 content keeps evolving).

To regenerate after changing the pipeline, re-run the four scripts above and commit the diff under `.agents/df-skills/`.
