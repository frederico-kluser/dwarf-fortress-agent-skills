---
name: dwarf-fortress-guide
description: Assistente-mestre de conhecimento do Dwarf Fortress. Use SEMPRE que o usuário fizer QUALQUER pergunta sobre jogar Dwarf Fortress — fortaleza, aventureiro, dwarves, combate, criaturas, indústria, construção, geologia, comércio, interface ou modding. Esta é a skill roteadora de topo: primeiro confirma se o jogador está no Adventure Mode ou no Fortress Mode, depois carrega o roteador daquele modo.
---

# Guia-Mestre do Dwarf Fortress (Roteador de Topo)

Há dois modos de jogo, cada um com sua própria árvore de skills. **Antes de responder, determine o modo do jogador.**

## Passo 1 — Escolha do modo
Pergunte (ou infira da conversa):

> **Você está jogando Adventure Mode (aventureiro) ou Fortress Mode (fortaleza)?**

| Modo | Carregue | Cobre |
|---|---|---|
| 🗺️ **Adventure Mode** (aventureiro, exploração, roguelike em 1ª pessoa) | `adventure-mode/SKILL.md` | 2642 artigos |
| 🏰 **Fortress Mode** (gerenciar fortaleza, dwarves, indústria) | `fortress-mode/SKILL.md` | 3052 artigos |

- Se o jogador disser "aventureiro", "viagem", "explorar", "minha personagem" → **Adventure Mode**.
- Se disser "meu forte", "meus dwarves", "construir oficina", "caravana" → **Fortress Mode**.
- Na dúvida, **pergunte** explicitamente antes de prosseguir.

## Passo 2 — Roteamento dentro do modo
Depois de carregar o `SKILL.md` do modo, use a tabela de roteamento dele para
achar a categoria (combate, criaturas, materiais, etc.), carregue o `SKILL.md`
da categoria e leia **apenas** o artigo relevante em `references/`.

## Regras
- **Não responda de memória** sobre mecânicas — baseie-se nos arquivos de referência.
- Carregue uma categoria por vez (orçamento de contexto).
- Conteúdo compartilhado (criaturas, armas, materiais, geologia, saúde, modding)
  existe em **ambos** os modos — use a árvore do modo atual.
- Conteúdo é v50/v0.47; em caso de ambiguidade de versão, assuma **v50** e avise.

## Busca local (ripgrep, sem embeddings)
`bash scripts/search.sh all "termo"`            # nos dois modos
`bash scripts/search.sh adventure-mode "termo"`  # só aventura
`bash scripts/search.sh fortress-mode/industria "termo"`  # categoria específica
