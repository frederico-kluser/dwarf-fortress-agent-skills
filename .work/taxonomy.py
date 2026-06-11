#!/usr/bin/env python3
"""Taxonomy config: map raw wiki {{category}} names to high-level skill categories,
and assign each skill category to fortress-mode, adventure-mode, or both (shared)."""

# High-level skill categories. Each: which modes it belongs to + the raw wiki
# categories that feed into it + title/keyword hints for uncategorized pages.
# modes: "both" | "fortress" | "adventure"
SKILL_CATEGORIES = {
    "combate": {
        "modes": "both",
        "desc": "Combate no Dwarf Fortress — armas, armaduras, escudos, ferimentos, "
                "partes do corpo, síndromes, venenos e mecânica de luta. Use quando o "
                "jogador perguntar sobre lutar, equipar armas/armaduras, sangramento, "
                "dor, partes do corpo atingidas, ou comparar materiais de combate.",
        "raw_cats": ["Weapons", "Armor", "Ammo", "Military", "Military Ranks",
                     "Fortress defense", "Body parts", "Syndrome", "No Stun",
                     "No Pain", "No Exert", "Traps", "Trapavoid"],
        "kw": ["weapon", "armor", "armour", "axe", "sword", "shield", "wound",
               "syndrome", "attack", "combat", "fighting", "blood", "poison"],
    },
    "criaturas": {
        "modes": "both",
        "desc": "Criaturas do Dwarf Fortress — animais, humanoides, megabestas, "
                "semi-megabestas, mortos-vivos, vermes, raças jogáveis e bestiário. "
                "Use quando o jogador perguntar sobre um bicho específico, monstros, "
                "inimigos, montarias, animais domésticos ou criaturas selvagens.",
        "raw_cats": ["Animals", "Creatures", "Humanoids", "humanoids", "Megabeasts",
                     "Semi-megabeasts", "Races", "Non-player characters", "Vermin",
                     "Creature attributes", "Amphibious", "Flying", "Fire immune",
                     "Fanciful", "Exotic mount", "Learns", "Building destroyer",
                     "Shearable", "Beaching", "Webs", "HFS", "Bestiary"],
        "kw": ["creature", "animal", "beast", "monster", "dragon", "goblin",
               "elf", "human", "dwarf", "kobold", "titan", "forgotten"],
    },
    "materiais": {
        "modes": "both",
        "desc": "Materiais e substâncias — metais, pedras, minérios, gemas, madeira, "
                "tecidos, couro, conchas, extratos e propriedades de material "
                "(magma-safe, valor). Use para comparar/escolher materiais, saber "
                "do que algo é feito, ou propriedades físicas de uma substância.",
        "raw_cats": ["Materials", "Metals", "Ore", "Stone", "Economic Stone", "Gems",
                     "Diamond", "Extracts", "Shell", "Magma safe materials",
                     "Clothing", "Wood", "Symbol"],
        "kw": ["metal", "stone", "ore", "gem", "material", "steel", "iron", "bronze",
               "leather", "cloth", "silk", "bone", "shell"],
    },
    "geologia-mundo": {
        "modes": "both",
        "desc": "Geologia, biomas e geração de mundo — camadas de pedra/solo, biomas, "
                "oceanos, florestas, lugares, mitologia e worldgen. Use para perguntas "
                "sobre terreno, onde encontrar coisas, tipos de bioma, ou lore do mundo.",
        "raw_cats": ["World", "Biomes", "Stone Layers", "stone Layers", "Soil Layers",
                     "Ocean", "Surface trees", "Subterranean trees", "Trees", "Grass",
                     "Plants", "plants", "Map tiles", "map tiles", "Locations",
                     "Places", "Myth", "Lore"],
        "kw": ["biome", "world", "geology", "layer", "ocean", "forest", "cavern",
               "tree", "plant", "worldgen", "mountain", "river"],
    },
    "saude-alimentacao": {
        "modes": "both",
        "desc": "Saúde e alimentação — comida, bebida, hospital, doenças, cura, "
                "necessidades fisiológicas. Use para perguntas sobre comer, beber, "
                "ferimentos tratados em hospital, infecção, fome, sede ou cansaço.",
        "raw_cats": ["Food", "Healthcare", "Agriculture", "Brewable"],
        "kw": ["food", "drink", "eat", "hospital", "disease", "wound", "heal",
               "hunger", "thirst", "meal", "alcohol", "farm"],
    },
    "modding": {
        "modes": "both",
        "desc": "Modding e raws — tokens, arquivos raw, init, tilesets, gráficos e "
                "edição de definições do jogo. Use quando o jogador quiser modificar "
                "o jogo, entender tokens, criaturas custom, ou estrutura de raws.",
        "raw_cats": ["Modding", "modding", "Tokens", "Raws", "Modding_Examples",
                     "Modding Examples", "Misc raw pages", "Languages raws",
                     "Graphics", "Tileset", "Mods"],
        "kw": ["token", "raw", "modding", "tileset", "init", "graphics"],
    },
    "interface-controles": {
        "modes": "both",
        "desc": "Interface e controles (v50) — teclas, menus, designações, símbolos e "
                "ícones da interface. Use quando o jogador perguntar como fazer algo na "
                "tela, qual tecla apertar, ou como navegar os menus.",
        "raw_cats": ["Interface", "Controls", "Designations", "designations",
                     "Menu icon"],
        "kw": ["interface", "control", "keybind", "menu", "designation", "hotkey"],
    },
    # ---- FORTRESS-ONLY ----
    "industria": {
        "modes": "fortress",
        "desc": "Indústria da fortaleza — forja, fundição, agricultura, cerveja, "
                "artesanato, têxtil e cadeias de produção. Use para perguntas sobre "
                "produzir bens, oficinas de produção, smelting ou economia de produção.",
        "raw_cats": ["Industry", "Furnaces", "Jobs", "Occupation"],
        "kw": ["smelt", "forge", "craft", "industry", "production", "smith"],
    },
    "construcao": {
        "modes": "fortress",
        "desc": "Construção da fortaleza — oficinas, móveis, mecanismos, traps, "
                "stockpiles, salas, zonas, construções e componentes de máquina. Use "
                "para perguntas sobre construir, oficinas, armazenamento ou engenharia.",
        "raw_cats": ["Buildings", "Workshops", "Furniture", "Constructions",
                     "Machine components", "Stockpiles", "Rooms", "Zones",
                     "Computing", "Logic"],
        "kw": ["building", "workshop", "furniture", "mechanism", "stockpile",
               "construction", "wall", "floor", "pump", "lever"],
    },
    "dwarves-gestao": {
        "modes": "fortress",
        "desc": "Gestão de dwarves — labores, habilidades, atributos, humores, "
                "necessidades, pensamentos, nobres, profissões, justiça e relações. "
                "Use para perguntar sobre gerenciar dwarves, trabalho, moods, nobres "
                "ou felicidade/infelicidade do forte.",
        "raw_cats": ["Dwarves", "Skills", "skills", "Labors", "Professions",
                     "Nobles", "Appointed Nobles", "Elected Nobles", "Aristocrats",
                     "Noble Skills", "Thoughts", "Religion", "Justice",
                     "Relationships", "Occupation"],
        "kw": ["labor", "skill", "attribute", "mood", "noble", "profession",
               "happiness", "thought", "need", "justice"],
    },
    "comercio-economia": {
        "modes": "fortress",
        "desc": "Comércio e economia do forte — comércio, caravanas, depósito, "
                "riqueza, mandatos e economia. Use para perguntas sobre negociar, "
                "caravanas, depot, valor do forte ou dinheiro.",
        "raw_cats": ["Trade", "Economy", "Items"],
        "kw": ["trade", "caravan", "depot", "merchant", "wealth", "economy", "coin"],
    },
    "fortress-geral": {
        "modes": "fortress",
        "desc": "Mecânicas gerais do modo fortaleza — defesa, eventos, jobs e visão "
                "geral do Fortress mode. Use para perguntas amplas sobre tocar uma "
                "fortaleza que não caem em uma categoria mais específica.",
        "raw_cats": ["Fortress mode", "Game mechanics", "Game_mechanics", "Events",
                     "Getting started", "Quickstart guide", "Guides", "Design"],
        "kw": ["fortress", "embark", "siege", "mandate", "event"],
    },
    # ---- ADVENTURE-ONLY ----
    "adventure-geral": {
        "modes": "adventure",
        "desc": "Mecânicas gerais do modo aventura — criação de personagem, viagem, "
                "fast travel, conversas, acampamento, exploração de sítios, retire/"
                "reclaim e visão geral do Adventure mode. Use para perguntas amplas "
                "sobre jogar como aventureiro.",
        "raw_cats": ["Adventurer mode", "adventurer mode", "Legends mode",
                     "Locations", "Occupation"],
        "kw": ["adventure", "adventurer", "travel", "camp", "quest", "conversation",
               "retire", "reclaim", "fast travel", "site"],
    },
}

# Categories that should NOT become skills (meta/noise) — pages only in these get
# routed by keyword fallback or dropped.
DROP_CATS = {
    "Humor and stories", "Humor and stories\u200f", "Game development",
    "Game_development", "Community", "community", "Wiki", "Errors", "Bugs",
    "Stubs", "Files", "Images", "Templates", "Spoilers", "Arcs",
    "Release information", "FAQ", "FAQ - Wood", "Bloodline games", "Current",
    "Hacking", "Utilities", "Ahk scripts", "ahk scripts", "D for Dwarf",
    "Stories", "Computing", "Language", "Papers", "Objects", "game", "Game",
}
