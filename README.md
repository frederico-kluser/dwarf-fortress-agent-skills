# Guia Técnico Completo: RAG da Wiki do Dwarf Fortress com um Copilot de IA

## TL;DR
- **Não faça scraping bruto.** O dwarffortresswiki.org é um MediaWiki 1.35.11 com API pública (`api.php`) e dumps XML prontos. Baixe com `wikiteam3` (crawl-delay padrão de 1,5s) ou pegue o dump pronto de novembro de 2023 no Internet Archive (`-history.xml.zst`, 31,5 MB). A wiki tem **9.832 artigos atualizados para v50** (mais 8 parcialmente migrados e 275 restantes) e **10.128 artigos no total**; licença **GFDL & MIT** (texto livre para reuso com atribuição).
- **Stack recomendada:** Python + **LlamaIndex** (melhor para RAG puro de documentação), embeddings locais **BGE-M3** (1024 dims, até 8192 tokens, MIT, grátis), vector store **ChromaDB** (persistência automática, ideal para o volume de ~15-40k chunks), e LLM via **OpenRouter** com o pacote dedicado `llama-index-llms-openrouter`. Modelo recomendado: **Gemini 2.5 Flash Lite** ($0,10/M input, $0,40/M output) ou **DeepSeek V4 Flash** ($0,0983/M input).
- **Pipeline:** dump XML → parse wikitext com `mwparserfromhell` (`strip_code()`) → chunk por seção (512-1024 tokens, ~15% overlap) com metadados (título/categoria/URL) → embeddings BGE-M3 → ChromaDB → query/chat engine LlamaIndex + OpenRouter → interface **Gradio** (`gr.ChatInterface`).

## Key Findings

### A wiki já tem dumps prontos — esse é o caminho mais rápido
O dwarffortresswiki.org documenta oficialmente um método de download na própria página `Dwarf_Fortress_Wiki:Offline_wiki`. O wiki roda **MediaWiki 1.35.11** (confirmado pela meta-tag generator), tem **API pública funcional** em `http://dwarffortresswiki.org/api.php` (responde a `action=query&meta=siteinfo`, o endpoint que o wikiteam3 usa), e o conteúdo é licenciado sob **GFDL & MIT**. Há **dumps prontos no Internet Archive na coleção WikiTeam**:

| Data | Item / arquivo XML | Tamanho XML | Imagens |
|------|--------------------|-------------|---------|
| **2023-11-07** (mais recente) | `wiki-dwarffortresswiki.org-20231107` / `-history.xml.zst` | **31,5 MB** | `images.7z` 583,3 MB |
| 2020-02-10 | `wiki-dwarffortresswikiorg` / `-history.xml.7z` | 399,3 KB | `wikidump.7z` 358,8 MB |
| 2018-05-05 | (mesmo item) `-history.xml.7z` | 27,1 MB | `wikidump.7z` 298,3 MB |
| 2016-02-29 | `wiki-dwarffortresswikiorg-20160229` | 9,5 MB | 259,6 MB |
| 2014-03-25 | `wiki-dwarffortresswikiorg` | 25,3 MB | `wikidump.7z` 257,7 MB |

**Não foi localizado dump de 2024/2025/2026** na coleção WikiTeam (verificado em junho de 2026). Para conteúdo v50 atual, gere um dump novo com wikiteam3. O dump de 2023 contém `-history.xml.zst` (com históricos); para RAG você quer só a revisão atual — gere com `--curonly`.

### Tamanho do corpus
**9.832 artigos atualizados para v50** ("9832 articles up-to-date for v50; 8 partially migrated; 275 remaining", per Main_Page) e **10.128 artigos no total** contando todos os namespaces de versão (DF2014, v0.34, etc. — "It launched on October 29, 2007, and has 10,128 articles"). É um corpus pequeno-médio: o XML comprimido tem só ~31 MB, gerando estimadamente 15.000-40.000 chunks após processamento. Isso é importante porque define toda a escolha de infraestrutura (cabe trivialmente em memória, embeddings locais rodam em minutos numa CPU/GPU modesta).

### LlamaIndex vence para este caso de uso
Para RAG focado em recuperação de documentação (exatamente este caso), **LlamaIndex** tem vantagem: query engines, routers e rerankers prontos, curva de aprendizado mais suave e API de alto nível ("ingerir e consultar em 5 linhas"). LangChain é mais flexível para orquestração complexa multi-ferramenta/multi-agente, mas é overkill aqui. Recomendação: **LlamaIndex** para o núcleo RAG; adicione LangChain só se evoluir para um agente com ferramentas depois. Os dois também podem ser combinados (LlamaIndex como retriever, LangChain como camada de agente).

### ChromaDB vence FAISS para este volume
Para ~15-40k chunks, **ChromaDB** é a melhor escolha: persistência automática (SQLite + DuckDB/Parquet), armazena vetores + documentos + metadados juntos, filtragem por metadados, índice HNSW com busca O(log n), e integração nativa com LlamaIndex/LangChain. FAISS é mais rápido em escala de milhões (e tem GPU/IVF) mas é só uma biblioteca de busca — sem armazenamento de documentos, sem metadados, exige save/load manual. Neste volume a diferença de velocidade é irrelevante; a simplicidade e persistência do Chroma vencem. Ambos são open-source (MIT/Apache).

### Não existe um projeto RAG pronto para a wiki do DF
Há projetos relacionados mas nenhum é um RAG aberto da wiki: `Ramblurr/Dwarf-Fortress-Portable-Wiki` (servidor offline com renderizador de wikitext do dump XML), `DF-Wiki/DFRawFunctions` (extensões MediaWiki da própria wiki). Copilots fechados existem — o GPT "Dwarf Fortress Dwarf" (requer ChatGPT Plus) e "Fortress Buddy" (ai4chat.co) — mas sem RAG aberto. Projetos de IA *jogando* DF (Ben Lubar `df-ai`, agente LLM via DFHack/TCP porta 5050) são outra categoria (controle do jogo, não Q&A sobre a wiki). **Há espaço para construir o que você quer do zero.**

## Details

### FASE 1 — Download da documentação

**Opção A (mais rápida para prototipar): dump pronto do Internet Archive**
```bash
wget https://archive.org/download/wiki-dwarffortresswiki.org-20231107/dwarffortresswiki.org-20231107-history.xml.zst
zstd -d dwarffortresswiki.org-20231107-history.xml.zst
```

**Opção B (recomendada para conteúdo v50 atual): gerar dump novo com wikiteam3**
`wikiteam3` é o porte Python 3 mantido do WikiTeam (instalável via PyPI, GPLv3). Por padrão "We crawl sites with 1.5s crawl-delay by default, and we respect Retry-After header":
```bash
pip install wikiteam3
wikiteam3dumpgenerator \
  --api http://dwarffortresswiki.org/api.php \
  --index http://dwarffortresswiki.org/index.php \
  --xml --curonly \
  --delay 1.5 \
  --path dfwiki
# --curonly  = só revisão atual (pula históricos; menor e mais rápido)
# --namespaces 0  ou  --exnamespaces para excluir Talk/File/User
```
Verificação de integridade do XML (os três primeiros números devem ser iguais entre si):
```bash
grep -E '<title(.*?)>' *.xml -c; grep -E '<page(.*?)>' *.xml -c; grep "</page>" *.xml -c
```

**Rate limiting / robots.txt:** wikiteam3 usa 1,5s de crawl-delay e respeita `Retry-After`. O opt-out de um wiki seria adicionar `User-agent: wikiteam3` / `Disallow: /` ao `robots.txt`; como dumps foram gerados com sucesso e a API é totalmente aberta a consultas anônimas, o crawling **não está bloqueado**. Use `--curonly` para reduzir drasticamente carga e volume. **Evite httrack/wget recursivo** na renderização HTML — é mais pesado para o servidor e o HTML é muito mais difícil de limpar do que o wikitext do dump.

### FASE 2 — Processamento do conteúdo

Parse **wikitext** (não HTML): o XML do dump já vem em wikitext, e `mwparserfromhell` é o parser maduro padrão (`pip install mwparserfromhell`). Use `mwxml` para iterar o dump.

```python
import mwxml, mwparserfromhell  # pip install mwxml mwparserfromhell

def wikitext_to_text(wikitext):
    code = mwparserfromhell.parse(wikitext)
    # remove templates {{...}} e tags; links [[bar]] -> "bar"; headings -> título
    return code.strip_code(normalize=True, collapse=True)

def extract_categories(wikitext):
    code = mwparserfromhell.parse(wikitext)
    return [str(l.title).split(":",1)[1] for l in code.filter_wikilinks()
            if str(l.title).lower().startswith("category:")]

dump = mwxml.Dump.from_file(open("dfwiki.xml"))
docs = []
for page in dump:
    if page.namespace != 0:          # só namespace principal (artigos v50)
        continue
    for revision in page:
        raw = revision.text or ""
        docs.append({
            "title": page.title,
            "url": f"https://dwarffortresswiki.org/index.php/{page.title.replace(' ', '_')}",
            "categories": extract_categories(raw),
            "text": wikitext_to_text(raw),
        })
```

`strip_code()` remove templates e tags, transforma `[[bar]]` em "bar" e reduz headings ao título. **Limpeza adicional:** remover linhas de navegação/`Category:` órfãs e templates de infobox que viram ruído; aplicar regex para resíduos de `[[File:...]]` (limitação conhecida do `strip_code`, que pode deixar texto como "135px"). Alternativa: `wikitextparser` (`remove_markup()` / `plain_text()`).

**Chunking inteligente por seção:** divida por headings (`==Seção==`) preservando **título da página + seção** como contexto em cada chunk. Metadados por chunk: `title`, `section`, `categories`, `url`, `version_namespace` (v50/DF2014).

### FASE 3 — Embeddings e Vector Store

**Modelo de embedding recomendado: BGE-M3** (BAAI) — licença **MIT** (grátis, self-hosted), **1024 dimensões**, processa "inputs... spanning from short sentences to long documents of up to 8192 tokens", e suporta dense/sparse/multi-vetor (ColBERT-style) numa única arquitetura, com forte desempenho no MTEB para retrieval e contexto longo. Para protótipo rápido/leve: `all-MiniLM-L6-v2` (384 dims, ~14ms/1K tokens, mas ~5-8% menos preciso). Para qualidade self-hosted alternativa, a família E5.

```python
# LlamaIndex + BGE-M3 local + ChromaDB
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import VectorStoreIndex, StorageContext, Settings
from llama_index.core.node_parser import SentenceSplitter
import chromadb

Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-m3")
Settings.node_parser = SentenceSplitter(chunk_size=512, chunk_overlap=75)

db = chromadb.PersistentClient(path="./df_chroma")
collection = db.get_or_create_collection("dwarf_fortress")
vector_store = ChromaVectorStore(chroma_collection=collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)

# nodes = lista de TextNode com metadados (gerados na fase 2)
index = VectorStoreIndex(nodes, storage_context=storage_context)
# Recarregar depois sem re-embedar:
# index = VectorStoreIndex.from_vector_store(vector_store)
```

**Chunking:** tamanho ideal **512-1024 tokens**, overlap **~15% (75-150 tokens)**. Para documentação técnica como wiki de jogo, **512 tokens** é o baseline (consultas factuais "como faço X"); use chunks maiores (1024) se as perguntas forem mais analíticas/estratégicas. Respeite limites de seção ao dividir.

### FASE 4 — Integração com OpenRouter

OpenRouter é um gateway OpenAI-compatível para centenas de modelos com uma única chave. LlamaIndex tem pacote dedicado `llama-index-llms-openrouter` (subclasse de `OpenAILike`):

```python
# pip install llama-index-llms-openrouter
from llama_index.llms.openrouter import OpenRouter
from llama_index.core import Settings
import os

Settings.llm = OpenRouter(
    api_key=os.environ["OPENROUTER_API_KEY"],
    model="google/gemini-2.5-flash-lite",
    max_tokens=1024,
    context_window=1048576,
)

query_engine = index.as_query_engine(similarity_top_k=5)
print(query_engine.query("Como começo uma fortaleza e evito inundações?"))
```

Alternativa LangChain (sem classe dedicada — use `ChatOpenAI` com `base_url`):
```python
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(
    model="google/gemini-2.5-flash-lite",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"],
)
```

**Modelo recomendado:** para um copilot de jogo (Q&A factual, barato), **Gemini 2.5 Flash Lite** — "$0.10 per million input tokens, $0.40 per million output tokens. 1,048,576 token context window" — ou **DeepSeek V4 Flash** — "$0.0983 per million input tokens, $0.1966 per million output tokens" (MoE de 284B params totais / 13B ativados, contexto de 1M). Para **prototipar de graça**, OpenRouter oferece modelos `:free` (variantes de DeepSeek/Llama/Gemma): limite de **20 requisições/minuto**; com menos de 10 créditos comprados, **50 requisições/dia** a modelos `:free`; com ≥10 créditos, o limite sobe para **1000/dia**.

### FASE 5 — Interface do copilot

**Recomendação: Gradio** para o chatbot — tem `gr.ChatInterface` pronto (estilo ChatGPT), gerencia histórico automaticamente e não recarrega o estado a cada interação (ao contrário do Streamlit, que recarrega o script inteiro e exige gerenciar `session_state`). Streamlit é superior para dashboards; Gradio é superior para chatbots LLM. Ambos rodam em Python puro e dockerizam.

```python
import gradio as gr

SYSTEM_PROMPT = """Você é Urist, um copilot especialista em Dwarf Fortress.
Use SOMENTE o contexto recuperado da wiki oficial para responder.
Cite o título da página da wiki usada. Se não houver contexto suficiente, diga que não sabe.
Seja prático e direto, focando em mecânicas de jogo acionáveis (versão v50/Premium)."""

chat_engine = index.as_chat_engine(
    chat_mode="context",
    system_prompt=SYSTEM_PROMPT,
    similarity_top_k=5,
)

def respond(message, history):
    return str(chat_engine.chat(message))

gr.ChatInterface(respond, title="Urist — Dwarf Fortress Copilot").launch()
```

Para um MVP de linha de comando, basta o loop `query_engine.query()` em um `while True`.

## Recommendations

1. **Comece pelo dump pronto** (Internet Archive, nov/2023) para ter um protótipo funcionando hoje. Migre para um dump fresco via `wikiteam3 --curonly --delay 1.5` quando precisar do conteúdo v50 mais recente.
2. **Stack inicial:** LlamaIndex + BGE-M3 (local) + ChromaDB + OpenRouter (Gemini 2.5 Flash Lite ou um modelo `:free` para testes) + Gradio. Tudo grátis exceto os tokens do LLM (centavos por dia neste volume).
3. **Chunking:** comece com 512 tokens / ~15% overlap por seção, com metadados de título + categoria + URL + namespace de versão. **Avalie com um conjunto fixo de ~20 perguntas reais** (taxa de acerto de recuperação, qualidade da resposta) e ajuste se a recuperação falhar.
4. **Adicione reranking** (BGE-reranker-v2) se a precisão de recuperação for insuficiente: recupere top-20, reranqueie para top-5. O fluxo recomendado pelo próprio BGE é "hybrid retrieval + re-ranking".
5. **Benchmarks/limiares que mudam a decisão:**
   - Corpus cresce >1M vetores ou latência de busca vira gargalo → migrar para **FAISS IVF** (com GPU se necessário).
   - Precisa de ações/ferramentas além de Q&A (ex.: consultar estado do jogo via DFHack) → adicionar **LangChain/agente**.
   - Respostas factuais ruins mesmo com bom contexto → subir para **Gemini 2.5 Flash** ou **Claude Sonnet**.
   - Recuperação traz chunks da versão errada → reforçar **filtro de metadados por namespace v50**.

## Caveats
- **Licença:** o texto da wiki é GFDL & MIT ("All editors publish their contributions under GNU Free Documentation License and the MIT License"), reutilizável com atribuição; imagens têm licenças individuais; conteúdo derivado dos arquivos do jogo é "Copyright (c) 2002-2026. All rights are retained by Tarn Adams" (Bay 12 Games). **Atribua a wiki nas respostas** do copilot.
- **Namespaces de versão duplicam conteúdo:** v50 fica no namespace principal, v0.47 em DF2014, etc. **Filtre o namespace principal (0)** para v50 ou marque a versão como metadado — caso contrário o RAG pode retornar mecânicas desatualizadas/conflitantes.
- **Não existe dump oficial de 2024-2026** no WikiTeam (verificado jun/2026); o dump mais recente é de 2023-11-07. Gere um novo se precisar de atualidade v50.
- **`strip_code()` tem limitações conhecidas** com `[[File:...]]` e interwiki links (pode deixar resíduos como "135px"); faça limpeza extra com regex.
- **`mwparserfromhell` é parser offline** — não expande templates (não conhece o conteúdo de `{{...}}`), então dados em infoboxes/templates podem se perder. Para páginas críticas com muitos templates, considere usar a API `action=parse` para obter o HTML renderizado e parsear com `mwparserfromhtml` ou BeautifulSoup.
- **Preços do OpenRouter flutuam** e variam por provider/roteamento (Balanced/Nitro/Exacto); confirme no momento do uso. Modelos `:free` têm rate limits que inviabilizam produção.
- A página oficial `Offline_wiki` que documenta o método de dump foi editada pela última vez em 2015 e referencia o WikiTeam antigo (Python 2); use o **wikiteam3** (Python 3, PyPI) no lugar dos comandos legados.