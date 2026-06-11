---
name: df-fortress-mode
description: Guia de conhecimento do Dwarf Fortress para o Fortress Mode. Foco em gerenciar uma fortaleza: dwarves, indústria, construção, comércio e defesa. Roteia a pergunta do jogador para a skill de categoria certa (combate, criaturas, materiais, etc.), carrega o SKILL.md dela e lê o artigo específico em references/.
---

# Dwarf Fortress — Fortress Mode (Roteador)

Você está no **Fortress Mode**. **Não responda de memória** sobre mecânicas — roteie para a categoria certa, carregue o `SKILL.md` dela e leia o arquivo de referência específico (progressive disclosure).

## Roteamento (situação do jogador → skill de categoria)
| Se o jogador fala sobre... | Carregue a skill |
|---|---|
| tokens, arquivos raw, init, tilesets, criaturas custom, editar definições | `skills/modding` (1453 artigos) |
| um bicho específico, monstros, inimigos, megabestas, animais, raças, montarias | `skills/criaturas` (504 artigos) |
| biomas, camadas de pedra, oceanos, florestas, worldgen, lugares, lore do mundo | `skills/geologia-mundo` (195 artigos) |
| defesa, siege, eventos, visão geral do modo fortaleza | `skills/fortress-geral` (168 artigos) |
| metais, pedras, minérios, gemas, do que algo é feito, magma-safe, valor de material | `skills/materiais` (161 artigos) |
| labores, habilidades, humores, nobres, profissões, justiça, felicidade | `skills/dwarves-gestao` (126 artigos) |
| lutar, armas, armaduras, ferimentos, sangramento, partes do corpo, síndromes/venenos | `skills/combate` (109 artigos) |
| oficinas, móveis, mecanismos, traps, stockpiles, salas, máquinas | `skills/construcao` (96 artigos) |
| teclas, menus, designações, como fazer algo na tela (v50) | `skills/interface-controles` (71 artigos) |
| comer, beber, hospital, doenças, cura, fome, sede, cansaço | `skills/saude-alimentacao` (71 artigos) |
| comércio, caravanas, depot, riqueza, mandatos | `skills/comercio-economia` (50 artigos) |
| forja, fundição, agricultura, cerveja, artesanato, produção | `skills/industria` (48 artigos) |

## Procedimento
1. Identifique a categoria pela tabela acima.
2. Leia o `SKILL.md` da categoria (Nível 2).
3. Use o índice dela (ou `scripts/search.sh`) para achar o artigo.
4. Leia **apenas** o(s) arquivo(s) de `references/` necessário(s) (Nível 3).
5. Responda citando a mecânica exata e a página-fonte.

## Busca local
Não sabe o arquivo? Rode:
`bash scripts/search.sh fortress-mode "termo de busca"`
ou restrinja a uma categoria:
`bash scripts/search.sh fortress-mode/combate "termo"`

## Regras
- Carregue uma categoria por vez (orçamento de contexto).
- Se a pergunta cruzar categorias (ex.: "armadura de aço"), carregue `materiais` E `combate`.
- O conteúdo cobre v50/v0.47; se houver ambiguidade de versão, assuma **v50** e avise.
