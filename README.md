# Dwarf Fortress Agent Skills

> A **flat, YAML-safe** Agent Skills knowledge base for [Dwarf Fortress](https://www.bay12games.com/dwarves/) v50/v0.47, extracted from the official [wiki](https://dwarffortresswiki.org) — **no RAG, no embeddings, no vector database**. Just clean Markdown + progressive disclosure + `ripgrep`.

[![License: GFDL & MIT](https://img.shields.io/badge/wiki_license-GFDL%20%26%20MIT-blue)](#license)
[![Articles](https://img.shields.io/badge/articles-2852-green)](https://github.com/frederico-kluser/dwarf-fortress-agent-skills)
[![Skills](https://img.shields.io/badge/skills-13-orange)](#skill-categories)

## What is this?

13 flat Agent Skills (progressive disclosure pattern) that any LLM coding agent — pi, Claude Code, Cursor, Codex, or a custom OpenRouter agent — can load to answer Dwarf Fortress gameplay questions with **wiki-ground-truth accuracy**, instead of inventing mechanics from memory.

The agent discovers skills by their `description` field in the system prompt. When a task matches, it loads the skill's `SKILL.md` (a short index), then reads the specific Markdown article from `references/`. Lexical search via `ripgrep` replaces embeddings — instant, deterministic, zero infrastructure.

### Why flat? (The pi revelation)

Early designs had a 3-level hierarchy (master → mode → category). **Pi's discovery model is flat** — every directory with a `SKILL.md` becomes a **peer** in the system prompt, discovered only by its `description`. Key lessons from the [pi skills documentation](https://agentskills.io/specification):

- **Strict YAML.** `description` can NOT contain unquoted `:` — or the skill silently fails to load (`return { skill: null }`).
- **Unique names.** Collisions keep the first discovery; duplicates silently vanish.
- **Flat peers.** There's no built-in routing. The `description` IS the router.

This V2 addresses all of those. Every SKILL.md passes pi's YAML parser; all 13 names are unique; each description is a self-contained signal.

## Skill categories

| Skill | Mode | Covers |
|---|---|---|
| `df-combate` | both | weapons, armor, wounds, bleeding, syndromes, military |
| `df-criaturas` | both | animals, megabeasts, races, bestiary, NPCs |
| `df-materiais` | both | metals, stone, gems, material properties, magma-safe |
| `df-geologia` | both | biomes, stone layers, worldgen, locations, lore |
| `df-saude` | both | food, drink, hospital, diseases, hunger, thirst |
| `df-modding` | both | tokens, raws, tilesets, creature definitions |
| `df-interface` | both | keys, menus, designations (v50) |
| `df-adventure` | adventure | character creation, travel, conversation, sites, quests |
| `df-fortress-industria` | fortress | smelting, forging, farming, brewing, crafting |
| `df-fortress-construcao` | fortress | workshops, furniture, traps, bridges, stockpiles |
| `df-dwarves` | fortress | labors, skills, moods, nobles, justice, psychology |
| `df-comercio` | fortress | trade, caravans, depot, wealth, economy |
| `df-fortress-geral` | fortress | defense, quickstart, embarks, megaprojects |

All SKILL.md descriptions are in Portuguese (the project's working language); article content is the original English wiki text.

## How an agent uses it

```
1. System prompt includes 13 descriptions. Agent sees the user's question.
2. Agent picks the relevant skill by description match.
3. Agent loads the skill's SKILL.md (short index, < 700 tokens each).
4. Agent reads the specific references/*.md article — or searches first:
     bash scripts/search.sh df-combate "steel armor"
     bash scripts/search.sh all "bleeding"
5. Agent answers, citing the source wiki page.
```

## Installation

**pi / .agents/skills (automatic discovery):** Just clone — no config needed.

**Claude Code / Cursor / Codex:**
```bash
cp -r .agents/skills/* ~/.claude/skills/
# or per-project: mkdir -p .claude/skills && cp -r ...
```

## Search script

```bash
bash scripts/search.sh df-criaturas "goblin"   # one skill
bash scripts/search.sh all "magma forge"        # all skills
```

Returns the top-20 most relevant reference files by `ripgrep` occurrence count.

## Build pipeline (reproducible)

See [`.work/`](.work) for scripts:

```bash
# 1. Download (31 MB compressed, WikiTeam 2023-11-07)
curl -L -o .work/df-history.xml.zst \
  "https://archive.org/download/wiki-dwarffortresswiki.org-20231107/dwarffortresswiki.org-20231107-history.xml.zst"
zstd -d --long=31 .work/df-history.xml.zst -o .work/df-history.xml

# 2. Pipeline
.venv/bin/python .work/parse_dump.py          # XML → pages.jsonl
.venv/bin/python .work/extract_taxonomy.py     # 157 {{category}} tags
.venv/bin/python .work/build_skills.py         # wikitext → clean gfm → references/*.md
.venv/bin/python .work/build_dispatchers.py   # search.sh + dispatcher
```

Dependencies: `pandoc`, `zstd`, `ripgrep`, Python venv with `mwparserfromhell mwxml pyyaml`.

## Design decisions

- **No RAG.** `ripgrep` over ~2.8k Markdown files is sub-second and deterministic. A `vector_store` + embeddings pipeline would add infrastructure and opacity for zero benefit at this scale.
- **50 KB cap per article.** Files that exceed 48 KB are truncated with a source link — no `read` can overflow a context window.
- **Giant dumps split.** `string-dump-raw.md` (raw token reference) was 923 KB → split into alphabetical chunks + truncated.
- **Indexes capped at 30 entries.** SKILL.md indexes list the most substantial articles; the rest are found via `search.sh`.
- **Wiki cleanup.** `mwparserfromhell` strips navigation templates; `pandoc -f mediawiki -t gfm-raw_html` produces clean Markdown; HTML entities, `{{}}` residue, broken images and interwiki links are all removed.

## License

- **Wiki text** (under `.agents/skills/*/references/`) — GFDL & MIT by Dwarf Fortress Wiki contributors. Every article links to its source page.
- **Build scripts** (under `.work/`) — MIT License (see `LICENSE`).
- **Game-derived data** — © 2002–2026 Tarn Adams / Bay 12 Games.

This is an unofficial, community resource and is not affiliated with Bay 12 Games.