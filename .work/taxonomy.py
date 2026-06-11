#!/usr/bin/env python3
"""Taxonomy V3 — descriptions BILÍNGUES (gatilho PT + keywords EN), categorias v50
frescas da API, e roteamento de páginas /raw por ASSUNTO (não mais tudo p/ modding).

Discovery do pi/Claude Code é FLAT e RECURSIVO: cada SKILL.md vira peer no system
prompt, descoberto só pela `description`. Nomes únicos; descriptions ≤1024 chars.

Ordem do dict = PRIORIDADE de desempate no first-match (criaturas ganha de leather,
combate ganha de materiais, etc.). Categorias de qualidade/manutenção/versão são
filtradas em build_skills (não roteiam).
"""

# Ordem importa: a primeira skill cuja categoria casar vence (first-match determinístico).
SKILL_CATEGORIES = {
    "df-criaturas": {
        "modes": "both",
        "desc": (
            "Criaturas, animais e bestiário do Dwarf Fortress: bichos, monstros, "
            "inimigos, montarias, animais domésticos, megabestas, humanoides, vermes "
            "e raças jogáveis, incluindo os dados de raw (tokens) de cada criatura. "
            "Use quando o usuário perguntar (em qualquer idioma, inclusive português) "
            "sobre uma criatura, bicho, animal, monstro, dragão, goblin, troll, gato, "
            "cão, ou sobre stats de criatura como tamanho, pet value, ataques. "
            "Termos EN: creature, animal, beast, monster, megabeast, vermin, mount, "
            "pet, dragon, goblin, titan, forgotten beast. Adventure e Fortress Mode."
        ),
        "raw_cats": [
            "Creatures", "Creature raw pages", "Animals", "Humanoids", "Vermin",
            "Megabeasts", "Semi-megabeasts", "Races", "Non-player characters",
            "Creature attributes", "Creatures by attribute", "Amphibious", "Flying",
            "Aquatic", "Grazer", "Fire immune", "Fanciful", "Exotic mount",
            "Exotic pet", "Learns", "Building destroyer", "Egglaying", "Webs",
            "Genderless", "Hateable", "Pet", "Bestiary",
        ],
        "kw": ["creature", "beast", "megabeast", "titan", "forgotten-beast"],
    },
    "df-combate": {
        "modes": "both",
        "desc": (
            "Combate no Dwarf Fortress: armas, armaduras, escudos, ferimentos, partes "
            "do corpo, síndromes, venenos, mecânica de luta e militar (squads, treino, "
            "defesa). Use quando o usuário perguntar (inclusive em português) sobre "
            "lutar, equipar arma ou armadura, sangramento, dor, treinar soldados, "
            "montar esquadrão, ou defender a fortaleza. Termos EN: weapon, armor, "
            "shield, wound, syndrome, poison, military, squad, training, siege defense. "
            "Funciona para Adventure Mode e Fortress Mode."
        ),
        "raw_cats": [
            "Weapons", "Weapon raw pages", "Armor", "Ammo", "Military",
            "Military Ranks", "Fortress defense", "Body parts", "Syndrome",
            "No Stun", "No Pain", "No Exert", "Traps", "Trapavoid",
        ],
        "kw": ["weapon", "armor", "armour", "syndrome"],
    },
    "df-materiais": {
        "modes": "both",
        "desc": (
            "Materiais do Dwarf Fortress: metais, pedras, minérios, gemas, ligas, aço, "
            "adamantine, madeira, couro, conchas, extratos e propriedades físicas "
            "(magma-safe, valor, peso, densidade). Use quando o usuário perguntar "
            "(inclusive em português) sobre material, metal, pedra, minério, gema, aço, "
            "liga, do que algo é feito, ou \"how to make steel\". Termos EN: metal, "
            "stone, ore, gem, alloy, steel, iron, bronze, adamantine, leather, magma "
            "safe. Funciona para Adventure Mode e Fortress Mode."
        ),
        "raw_cats": [
            "Materials", "Material properties", "Metals", "Ore", "Stone",
            "Economic Stone", "Stone Layers", "Sedimentary Stone Layers",
            "Soil Layers", "Inorganic raw pages", "Gems", "Diamond", "Extracts",
            "Shell", "Magma safe materials", "Wood", "Leather", "Tooth", "Horn",
            "Hoof", "Scales", "Chitin", "Ivory", "Symbol", "Symbol raw pages",
        ],
        "kw": ["adamantine", "alloy"],
    },
    "df-saude": {
        "modes": "both",
        "desc": (
            "Saúde, comida e agricultura no Dwarf Fortress: comer, beber, hospital, "
            "doenças, cura, plantio, cervejaria e necessidades fisiológicas. Use quando "
            "o usuário perguntar (inclusive em português) sobre comida, bebida, lavoura, "
            "tratar ferimentos, infecção, fome, sede ou cansaço. Termos EN: food, drink, "
            "hospital, disease, heal, farming, crops, brewing, agriculture, hunger, "
            "thirst. Funciona para Adventure Mode e Fortress Mode."
        ),
        "raw_cats": [
            "Food", "Healthcare", "Agriculture", "Brewable", "Crops", "Fruit",
            "Millable", "Milkable", "Dye sources", "Fishable", "Steals food",
            "Devours food", "Steals drink",
        ],
        "kw": ["hospital", "brewing"],
    },
    "df-geologia": {
        "modes": "both",
        "desc": (
            "Geologia e mundo do Dwarf Fortress: biomas, camadas de pedra e solo, "
            "oceanos, florestas, plantas, árvores, geração de mundo (worldgen), lugares "
            "e lore. Use quando o usuário perguntar (inclusive em português) sobre "
            "terreno, onde achar recursos, bioma, caverna, planta, árvore, worldgen ou "
            "história do mundo. Termos EN: biome, world, geology, layer, cavern, tree, "
            "plant, worldgen, ocean, forest, river. Adventure e Fortress Mode."
        ),
        "raw_cats": [
            "World", "Biomes", "Ocean", "Surface trees", "Subterranean trees",
            "Trees", "Grass", "Plants", "Plant raw pages", "Surface plants",
            "Summer plants", "Autumn plants", "Spring plants", "Winter plants",
            "Leaves", "Map tiles", "Locations", "Places", "Myth", "Lore", "Soil",
        ],
        "kw": ["biome", "worldgen", "aquifer", "cavern"],
    },
    "df-modding": {
        "modes": "both",
        "desc": (
            "Modding do Dwarf Fortress: tokens, arquivos raw, init, tilesets, gráficos "
            "e edição de definições do jogo. Use quando o usuário quiser modificar o "
            "jogo, entender referência de tokens (creature token, weapon token), criar "
            "raças custom ou editar raws. Termos EN: token, raw, modding, tileset, init, "
            "graphics, reaction, mod. Funciona para Adventure Mode e Fortress Mode."
        ),
        "raw_cats": [
            "Modding", "Tokens", "Raws", "Mods", "Graphics", "Tileset",
            "Material template raw pages",
        ],
        "kw": ["token", "raw-file", "modding", "tileset"],
    },
    "df-interface": {
        "modes": "both",
        "desc": (
            "Interface do Dwarf Fortress v50/Premium: teclas, menus, designações, "
            "ícones e atalhos. Use quando o usuário perguntar (inclusive em português) "
            "como fazer algo na tela, qual tecla apertar, ou como navegar os menus. "
            "Termos EN: interface, control, keybinding, menu, designation, hotkey, UI "
            "shortcut. Funciona para Adventure Mode e Fortress Mode."
        ),
        "raw_cats": [
            "Interface", "Controls", "Designations", "Menu icon", "UI shortcuts",
            "Building icons", "Item sprites",
        ],
        "kw": ["keybind", "hotkey", "designation"],
    },
    "df-adventure": {
        "modes": "adventure",
        "desc": (
            "Adventure Mode do Dwarf Fortress: criação de personagem, viagem, fast "
            "travel, conversas com NPCs, acampamento, exploração de sítios e masmorras, "
            "retire/reclaim. Use quando o usuário estiver no modo Aventureiro ou "
            "perguntar (inclusive em português) sobre aventura, exploração, quests, "
            "diálogos ou viagem. Termos EN: adventurer, travel, camp, quest, "
            "conversation, retire, site, dungeon. Exclusivo do Adventure Mode."
        ),
        "raw_cats": [
            "Adventurer mode", "Legends mode", "Occupation",
        ],
        "kw": ["adventurer", "fast-travel"],
    },
    "df-fortress-industria": {
        "modes": "fortress",
        "desc": (
            "Indústria da fortaleza no Dwarf Fortress: forja, fundição, oficinas de "
            "produção, artesanato, têxtil e cadeias de produção. Use quando o usuário "
            "perguntar (inclusive em português) sobre produzir bens, fundir metal, "
            "forjar, ou economia de produção. Termos EN: smelt, forge, craft, industry, "
            "production, smith, workshop, magma forge. Exclusivo do Fortress Mode."
        ),
        "raw_cats": ["Industry", "Furnaces", "Jobs", "Farming Workshops"],
        "kw": ["smelt", "forge", "smith"],
    },
    "df-fortress-construcao": {
        "modes": "fortress",
        "desc": (
            "Construção da fortaleza no Dwarf Fortress: oficinas, móveis, mecanismos, "
            "pontes, alavancas, stockpiles, salas, zonas, construções e componentes de "
            "máquina. Use quando o usuário perguntar (inclusive em português) sobre "
            "construir, design de fortaleza, armazenamento ou engenharia. Termos EN: "
            "building, workshop, furniture, mechanism, stockpile, bridge, lever, pump. "
            "Exclusivo do Fortress Mode."
        ),
        "raw_cats": [
            "Buildings", "Workshops", "Furniture", "Constructions",
            "Machine components", "Stockpiles", "Rooms", "Zones", "Computing",
        ],
        "kw": ["stockpile", "mechanism"],
    },
    "df-dwarves": {
        "modes": "fortress",
        "desc": (
            "Gestão de dwarves no Dwarf Fortress: labores, habilidades, atributos, "
            "humores (strange mood), necessidades, pensamentos, nobres, profissões, "
            "justiça e psicologia. Use quando o usuário perguntar (inclusive em "
            "português) sobre gerenciar anões, trabalho, labor, humor estranho, nobres, "
            "mandatos ou felicidade. Termos EN: labor, skill, attribute, strange mood, "
            "noble, profession, happiness, thought, need, justice. Exclusivo do "
            "Fortress Mode."
        ),
        "raw_cats": [
            "Dwarves", "Skills", "Labors", "Professions", "Nobles", "Thoughts",
            "Religion", "Justice", "Relationships", "Scholarship",
        ],
        "kw": ["labor", "strange-mood", "noble"],
    },
    "df-comercio": {
        "modes": "fortress",
        "desc": (
            "Comércio e economia da fortaleza no Dwarf Fortress: negociação, caravanas, "
            "trade depot, riqueza, mercadorias, mandatos e moeda. Use quando o usuário "
            "perguntar (inclusive em português) sobre negociar, caravana, depot, valor "
            "do forte ou economia. Termos EN: trade, caravan, depot, merchant, wealth, "
            "economy, coin, item. Exclusivo do Fortress Mode."
        ),
        "raw_cats": ["Trade", "Economy", "Items"],
        "kw": ["caravan", "trade-depot"],
    },
    "df-fortress-geral": {
        "modes": "fortress",
        "desc": (
            "Mecânicas gerais do Fortress Mode no Dwarf Fortress: defesa, eventos, "
            "embarks, física (água, magma, pressão, desabamento), guias de iniciante, "
            "FAQs, quickstart e visão geral. Use para perguntas amplas (inclusive em "
            "português) sobre tocar uma fortaleza, embark, cerco, magma, água, ou que "
            "não caiam numa categoria específica. Termos EN: fortress, embark, siege, "
            "magma, water, pressure, cave-in, guide, FAQ, getting started. Exclusivo "
            "do Fortress Mode."
        ),
        "raw_cats": [
            "Fortress mode", "Game mechanics", "Game", "Events", "Getting started",
            "Physics", "Entities",
            "Quickstart guide", "Guides", "Design", "FAQ", "FAQ - Farming",
            "FAQ - Military", "FAQ - Water", "FAQ - Magma", "FAQ - Mining",
            "FAQ - Buildings", "FAQ - Starting", "FAQ - Interface",
            "FAQ - Error messages",
        ],
        "kw": ["embark", "siege", "magma", "quickstart"],
    },
}

# Categorias que NÃO devem rotear (meta/wiki/manutenção). Filtradas em build_skills.
DROP_CATS = {
    "Current", "D for Dwarf", "Bugs", "Verify", "Deletion", "Templates",
    "Template Documentation", "Navigation templates", "Raw templates",
    "Picture Templates", "Floor Plan Templates", "Formatting Templates",
    "Infobox templates", "Materials templates", "Version templates",
    "Message box templates", "Flowchart templates", "Inline formatting templates",
    "FAQ templates", "Hidden categories", "Disambiguation", "Release information",
    "Version", "Empty version pages", "Unversioned", "License tags", "Wiki",
    "Game development", "Community", "Humor and stories", "Stories",
    "Bloodline games", "Utilities", "Hacking", "New pages", "New talk pages",
    "New user pages", "Errors", "Spoilers", "Obsolete features", "Needs update",
    "Missing current version", "Lua script pages", "Language", "Masterwork",
    "Pages that break Community Portal rules", "Interface images",
    "Potential copyright", "Scholarship templates",
}

# Resgate por título para páginas v50 sem categoria útil (rede de segurança).
TITLE_RESCUE = {
    "mining": "df-fortress-geral",
    "fishing": "df-saude",
    "well": "df-fortress-construcao",
    "tunnel": "df-fortress-construcao",
    "butcher": "df-fortress-industria",
    "anatomy": "df-saude",
    "water": "df-fortress-geral",
    "magma": "df-fortress-geral",
}
