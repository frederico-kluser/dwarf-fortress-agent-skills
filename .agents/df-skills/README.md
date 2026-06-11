# Dwarf Fortress — Agent Skills

Sistema de **Agent Skills** (progressive disclosure, sem RAG/embeddings) gerado a
partir da [Dwarf Fortress Wiki](https://dwarffortresswiki.org) (dump WikiTeam de
2023-11-07, conteúdo v50/v0.47, licença GFDL & MIT).

## Estrutura (3 níveis)

```
df-skills/
├── SKILL.md                 # Roteador de TOPO: pergunta o modo (Adventure/Fortress)
├── scripts/search.sh        # busca lexical local (ripgrep) — sem embeddings
├── adventure-mode/          # árvore completa do Adventure Mode
│   ├── SKILL.md             # roteador do modo (situação → categoria)
│   └── skills/<categoria>/
│       ├── SKILL.md         # índice + quando usar
│       └── references/*.md  # 1 artigo da wiki por arquivo
└── fortress-mode/           # árvore completa do Fortress Mode
    ├── SKILL.md
    └── skills/<categoria>/...
```

**Conteúdo compartilhado** (criaturas, combate, materiais, geologia, saúde, modding,
interface) existe em **ambos** os modos — cada árvore é autossuficiente. O jogador
escolhe o modo no roteador de topo, e daí o roteamento desce para a categoria e o
artigo específico.

## Como usar (fluxo do agente)

1. Carregue `SKILL.md` (topo) → confirme **Adventure** ou **Fortress Mode**.
2. Carregue `<modo>/SKILL.md` → use a tabela situação→categoria.
3. Carregue `<modo>/skills/<categoria>/SKILL.md` → use o índice.
4. Leia **apenas** o(s) `references/*.md` necessário(s).

Busca quando não souber o arquivo:
```bash
bash scripts/search.sh all "steel armor"               # nos dois modos
bash scripts/search.sh adventure-mode "bleeding"        # só aventura
bash scripts/search.sh fortress-mode/industria "magma"  # categoria específica
```

## Categorias

| Categoria | Modos | Conteúdo |
|---|---|---|
| combate | ambos | armas, armaduras, ferimentos, síndromes |
| criaturas | ambos | animais, megabestas, raças, bestiário |
| materiais | ambos | metais, pedras, gemas, propriedades |
| geologia-mundo | ambos | biomas, camadas, worldgen, lugares |
| saude-alimentacao | ambos | comida, bebida, hospital, doenças |
| modding | ambos | tokens, raws, tilesets |
| interface-controles | ambos | teclas, menus, designações (v50) |
| industria | fortress | forja, agricultura, cerveja, artesanato |
| construcao | fortress | oficinas, móveis, traps, mecanismos |
| dwarves-gestao | fortress | labores, humores, nobres, justiça |
| comercio-economia | fortress | comércio, caravanas, riqueza |
| fortress-geral | fortress | defesa, eventos, visão geral |
| adventure-geral | adventure | criação de personagem, viagem, conversas |

## Reconstruir

Os scripts de geração estão em `../.work/` (não versionar o dump bruto):

```bash
# 1. baixar dump
curl -L -o df-history.xml.zst "https://archive.org/download/wiki-dwarffortresswiki.org-20231107/dwarffortresswiki.org-20231107-history.xml.zst"
zstd -d --long=31 df-history.xml.zst -o df-history.xml
# 2. pipeline
.venv/bin/python .work/parse_dump.py          # XML → pages.jsonl
.venv/bin/python .work/extract_taxonomy.py     # categorias
.venv/bin/python .work/build_skills.py         # references/*.md + SKILL.md por categoria
.venv/bin/python .work/build_dispatchers.py    # search.sh + roteadores
```

Dependências: `pandoc`, `zstd`, `ripgrep`, e venv Python com
`mwparserfromhell mwxml pyyaml`.

## Atribuição

Texto da wiki sob **GFDL & MIT** (reutilizável com atribuição). Cada artigo inclui
link para a página-fonte. Conteúdo derivado dos arquivos do jogo é
© 2002–2026 Tarn Adams / Bay 12 Games.
