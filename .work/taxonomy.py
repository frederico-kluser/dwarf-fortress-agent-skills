#!/usr/bin/env python3
"""Taxonomy V2 — flat skill names, YAML-safe descriptions (no ":"), no cross-mode
duplication. Pi/Claude Code discovery is RECURSIVE and FLAT — all SKILL.md files
found under .agents/skills/ become peers in the system prompt. No hierarchy, no
routers. Each skill name must be unique; descriptions must not contain unquoted ":".

Shared content (creatures, combat, materials, geology, health, modding, interface)
goes into ONE skill with its description noting both modes.
Mode-specific content has its own skill.
"""

# Each entry: skill name, mode hint for description, list of raw {{category}} tags
# All descriptions are YAML-safe — no ":" characters, no "#" at line start.

SKILL_CATEGORIES = {
    # ── shared (both modes) ──
    "df-combate": {
        "modes": "both",
        "desc": (
            "Armas, armaduras, escudos, ferimentos, partes do corpo, síndromes, "
            "venenos e mecânica de luta. Use quando o jogador perguntar sobre lutar, "
            "equipar armas ou armaduras, sangramento, dor, comparar materiais de "
            "combate, treinar soldados ou montar squads. "
            "Funciona para Adventure Mode e Fortress Mode."
        ),
        "raw_cats": [
            "Weapons", "Armor", "Ammo", "Military", "Military Ranks",
            "Fortress defense", "Body parts", "Syndrome", "No Stun",
            "No Pain", "No Exert", "Traps", "Trapavoid",
        ],
        "kw": ["weapon", "armor", "armour", "axe", "sword", "shield", "wound",
               "syndrome", "attack", "combat", "bleeding", "blood", "poison"],
    },
    "df-criaturas": {
        "modes": "both",
        "desc": (
            "Animais, humanoides, megabestas, semi-megabestas, mortos-vivos, "
            "vermes, raças jogáveis e bestiário do Dwarf Fortress. "
            "Use quando o jogador perguntar sobre um bicho específico, monstros, "
            "inimigos, montarias, animais domésticos ou criaturas selvagens. "
            "Funciona para Adventure Mode e Fortress Mode."
        ),
        "raw_cats": [
            "Animals", "Creatures", "Humanoids", "humanoids", "Megabeasts",
            "Semi-megabeasts", "Races", "Non-player characters", "Vermin",
            "Creature attributes", "Amphibious", "Flying", "Fire immune",
            "Fanciful", "Exotic mount", "Learns", "Building destroyer",
            "Shearable", "Beaching", "Webs", "HFS", "Bestiary",
        ],
        "kw": ["creature", "animal", "beast", "monster", "dragon", "goblin",
               "elf", "human", "dwarf", "kobold", "titan", "forgotten"],
    },
    "df-materiais": {
        "modes": "both",
        "desc": (
            "Metais, pedras, minérios, gemas, madeira, tecidos, couro, conchas, "
            "extratos e propriedades físicas de material — magma-safe, valor, peso. "
            "Use para comparar ou escolher materiais, saber do que algo é feito, "
            "ou propriedades de uma substância. "
            "Funciona para Adventure Mode e Fortress Mode."
        ),
        "raw_cats": [
            "Materials", "Metals", "Ore", "Stone", "Economic Stone", "Gems",
            "Diamond", "Extracts", "Shell", "Magma safe materials",
            "Clothing", "Wood", "Symbol",
        ],
        "kw": ["metal", "stone", "ore", "gem", "material", "steel", "iron",
               "bronze", "leather", "cloth", "silk", "bone", "shell"],
    },
    "df-geologia": {
        "modes": "both",
        "desc": (
            "Biomas, camadas de pedra e solo, oceanos, florestas, geração de mundo "
            "(worldgen), lugares e lore do mundo. "
            "Use para perguntas sobre terreno, onde encontrar recursos, tipos de "
            "bioma ou história do mundo gerado. "
            "Funciona para Adventure Mode e Fortress Mode."
        ),
        "raw_cats": [
            "World", "Biomes", "Stone Layers", "stone Layers", "Soil Layers",
            "Ocean", "Surface trees", "Subterranean trees", "Trees", "Grass",
            "Plants", "plants", "Map tiles", "map tiles", "Locations",
            "Places", "Myth", "Lore",
        ],
        "kw": ["biome", "world", "geology", "layer", "ocean", "forest", "cavern",
               "tree", "plant", "worldgen", "mountain", "river"],
    },
    "df-saude": {
        "modes": "both",
        "desc": (
            "Comida, bebida, hospital, doenças, cura e necessidades fisiológicas. "
            "Use para perguntas sobre comer, beber, tratar ferimentos em hospital, "
            "infecção, fome, sede ou cansaço. "
            "Funciona para Adventure Mode e Fortress Mode."
        ),
        "raw_cats": ["Food", "Healthcare", "Agriculture", "Brewable",
                     "Shearable"],
        "kw": ["food", "drink", "eat", "hospital", "disease", "wound",
               "heal", "hunger", "thirst", "meal", "alcohol", "farm"],
    },
    "df-modding": {
        "modes": "both",
        "desc": (
            "Tokens, arquivos raw, init, tilesets, gráficos e edição de definições "
            "do jogo. Use quando o jogador quiser modificar o Dwarf Fortress, "
            "entender tokens de criatura, criar raças custom ou editar raws. "
            "Funciona para Adventure Mode e Fortress Mode."
        ),
        "raw_cats": [
            "Modding", "modding", "Tokens", "Raws", "Modding_Examples",
            "Modding Examples", "Misc raw pages", "Languages raws",
            "Graphics", "Tileset", "Mods",
        ],
        "kw": ["token", "raw", "modding", "tileset", "init", "graphics"],
    },
    "df-interface": {
        "modes": "both",
        "desc": (
            "Teclas, menus, designações e ícones da interface v50/Premium. "
            "Use quando o jogador perguntar como fazer algo na tela, qual tecla "
            "apertar ou como navegar os menus do jogo. "
            "Funciona para Adventure Mode e Fortress Mode."
        ),
        "raw_cats": ["Interface", "Controls", "Designations", "designations",
                     "Menu icon"],
        "kw": ["interface", "control", "keybind", "menu", "designation", "hotkey"],
    },

    # ── adventure mode only ──
    "df-adventure": {
        "modes": "adventure",
        "desc": (
            "Mecânicas do Adventure Mode — criação de personagem, viagem no mapa, "
            "fast travel, conversas com NPCs, acampamento, exploração de sítios e "
            "masmorras, retire/reclaim de personagem. "
            "Use quando o jogador estiver no modo Aventureiro ou perguntar sobre "
            "exploração, quests, diálogos com NPCs ou mecânicas específicas de "
            "aventura. Exclusivo do Adventure Mode."
        ),
        "raw_cats": [
            "Adventurer mode", "adventurer mode", "Legends mode", "Occupation",
        ],
        "kw": ["adventure", "adventurer", "travel", "camp", "quest",
               "conversation", "retire", "reclaim", "fast travel", "site",
               "dungeon", "hearthperson", "character creation", "dialogue"],
    },

    # ── fortress mode only ──
    "df-fortress-industria": {
        "modes": "fortress",
        "desc": (
            "Indústria da fortaleza — forja, fundição, agricultura, cerveja, "
            "artesanato, têxtil e cadeias de produção. "
            "Use para perguntas sobre produzir bens, oficinas de produção, "
            "smelting, farming, brewing ou economia de produção. "
            "Exclusivo do Fortress Mode."
        ),
        "raw_cats": ["Industry", "Furnaces", "Jobs"],
        "kw": ["smelt", "forge", "craft", "industry", "production", "smith"],
    },
    "df-fortress-construcao": {
        "modes": "fortress",
        "desc": (
            "Construção da fortaleza — oficinas, móveis, mecanismos, traps, pontes, "
            "alavancas, stockpiles, salas, zonas, construções e componentes de "
            "máquina. Use para perguntas sobre construir, design de fortaleza, "
            "armazenamento ou engenharia de fortaleza. Exclusivo do Fortress Mode."
        ),
        "raw_cats": [
            "Buildings", "Workshops", "Furniture", "Constructions",
            "Machine components", "Stockpiles", "Rooms", "Zones",
            "Computing", "Logic",
        ],
        "kw": ["building", "workshop", "furniture", "mechanism", "stockpile",
               "construction", "wall", "floor", "pump", "lever", "bridge"],
    },
    "df-dwarves": {
        "modes": "fortress",
        "desc": (
            "Gestão de dwarves — labores, habilidades, atributos, humores, "
            "necessidades, pensamentos, nobres, profissões, justiça, relações "
            "e psicologia dos dwarves. Use para perguntas sobre gerenciar "
            "dwarves, trabalho, strange moods, nobres, mandatos ou felicidade "
            "do forte. Exclusivo do Fortress Mode."
        ),
        "raw_cats": [
            "Dwarves", "Skills", "skills", "Labors", "Professions",
            "Nobles", "Appointed Nobles", "Elected Nobles", "Aristocrats",
            "Noble Skills", "Thoughts", "Religion", "Justice",
            "Relationships",
        ],
        "kw": ["labor", "skill", "attribute", "mood", "noble", "profession",
               "happiness", "thought", "need", "justice", "dwarf"],
    },
    "df-comercio": {
        "modes": "fortress",
        "desc": (
            "Comércio e economia do forte — negociação, caravanas, trade depot, "
            "riqueza, mandatos e moeda. Use para perguntas sobre negociar com "
            "caravanas, montar depot, valor do forte ou economia. "
            "Exclusivo do Fortress Mode."
        ),
        "raw_cats": ["Trade", "Economy", "Items"],
        "kw": ["trade", "caravan", "depot", "merchant", "wealth", "economy", "coin"],
    },
    "df-fortress-geral": {
        "modes": "fortress",
        "desc": (
            "Mecânicas gerais do Fortress Mode — defesa, eventos, embarks, "
            "guias de iniciante, quickstart e visão geral. "
            "Use para perguntas amplas sobre tocar uma fortaleza que não caem "
            "em uma categoria mais específica. Exclusivo do Fortress Mode."
        ),
        "raw_cats": [
            "Fortress mode", "Game mechanics", "Game_mechanics", "Events",
            "Getting started", "Quickstart guide", "Guides", "Design",
        ],
        "kw": ["fortress", "embark", "siege", "mandate", "event", "quickstart", "guide"],
    },
}

# Categories that should not route to any skill (meta/noise)
DROP_CATS = {
    "Humor and stories", "Humor and stories\u200f", "Game development",
    "Game_development", "Community", "community", "Wiki", "Errors", "Bugs",
    "Stubs", "Files", "Images", "Templates", "Spoilers", "Arcs",
    "Release information", "FAQ", "FAQ - Wood", "Bloodline games", "Current",
    "Hacking", "Utilities", "Ahk scripts", "ahk scripts", "D for Dwarf",
    "Stories", "Computing", "Language", "Papers", "Objects", "game", "Game",
}