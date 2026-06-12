---
name: df-live-bridge
description: >-
  Ponte ao vivo com o Dwarf Fortress rodando, via DFHack: lê e traduz os eventos
  novos do jogo (gamelog.txt), verifica o estado da sessão e envia comandos de
  controle ao console (pausar, despausar, designar mineração via quickfort,
  prospect) por dfhack-run ou socket TCP local (porta 5000). Use quando o usuário
  pedir (inclusive em português) para monitorar a fortaleza em tempo real, ler ou
  traduzir os últimos eventos e anúncios, pausar/despausar o jogo, executar um
  comando DFHack, ou instalar o DFHack no Linux/Steam. Termos EN: DFHack, live
  bridge, real-time, gamelog, announcement, remote control, console command,
  pause, unpause, dig designation, quickfort, RPC port 5000. Fortress e Adventure
  Mode; requer o jogo aberto no Linux para enviar comandos.
metadata:
  source: DFHack 53.x (docs.dfhack.org) — artigos manuais, não-wiki
  snapshot: "2026-06"
  license: MIT
  mode: both
---

# DF Live Bridge (Dwarf Fortress + DFHack)

Esta skill **opera um jogo aberto** (não é uma skill de wiki): lê os eventos novos do
`gamelog.txt` e envia comandos ao console do DFHack. Os artigos em `references/` e os
anúncios do gamelog estão em **inglês** — **traduza os eventos ao reportar** e responda
no idioma do usuário (glossário: `.agents/skills/scripts/glossary-pt-en.tsv`).

## Uso ao vivo (faça isto primeiro)

Estado da sessão (o jogo está aberto? dá para ler/escrever?):

    python3 .agents/skills/scripts/df_bridge.py status --json

Ler eventos (anúncios do jogo, em inglês — traduza ao responder):

    python3 .agents/skills/scripts/df_bridge.py log --new --json        # só o que aconteceu desde a última checagem
    python3 .agents/skills/scripts/df_bridge.py log --lines 30          # últimas 30 linhas
    python3 .agents/skills/scripts/df_bridge.py watch --seconds 15      # acompanha por 15s (sempre termina sozinho)

Controlar o jogo (o DFHack precisa estar rodando — o `status` mostra):

    python3 .agents/skills/scripts/df_bridge.py pause                   # pausa (seguro)
    python3 .agents/skills/scripts/df_bridge.py unpause                 # despausa
    python3 .agents/skills/scripts/df_bridge.py run prospect all        # qualquer comando do console
    python3 .agents/skills/scripts/df_bridge.py run quickfort run library/dreamfort.csv -n /surface1

Regras para o agente:
1. Se algo falhar, rode `status` primeiro e reporte o diagnóstico. Exit codes:
   `10` DF não encontrado · `11` gamelog ausente (jogo nunca rodou) ·
   `12` jogo/DFHack fechado (RPC inalcançável) · `13` o comando falhou dentro do jogo.
2. **Nunca** envie comandos que alteram o jogo (dig, quickfort, autodump, cleanowned…)
   sem o usuário pedir — `pause`/`unpause` e leituras (`log`, `watch`, `prospect`) são seguros.
3. Flags (`--json`, `--df-path`, `--port`, `--via`) vêm logo após o subcomando, **antes**
   do comando do jogo: `run --json prospect all`.

Comandos disponíveis e exemplos prontos: `references/dfhack-commands.md`.

## Instalar o DFHack (Linux/Steam)

Se o `status` disser que o DFHack não está instalado:

    bash .agents/skills/scripts/install_dfhack_linux.sh --dry-run   # mostra o plano, sem escrever nada
    bash .agents/skills/scripts/install_dfhack_linux.sh             # instala (rota Steam ou tarball)

Passo a passo, lançamento e troubleshooting: `references/live-bridge-setup.md`.

## Como buscar (referências desta skill)

Busca full-text rankeada (BM25, com stemming e tradução PT→EN automática):

    python3 .agents/skills/scripts/search.py --skill df-live-bridge "pause"     # use --json para saída estruturada

Em 0 resultados o script afrouxa sozinho (AND → OR → prefixo). Sem o índice:

    grep -ril "TERMO" references/ | head

## Índice (2 artigos)
- DFHack live bridge — setup & troubleshooting (Linux) → `references/live-bridge-setup.md`
- DFHack command cheatsheet for live control → `references/dfhack-commands.md`
