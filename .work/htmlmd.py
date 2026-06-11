#!/usr/bin/env python3
"""HTML (renderizado pela API) → Markdown limpo para consumo por agentes LLM.

Substitui a antiga rota wikitext→pandoc, que apagava templates não-expandidos.
Aqui o HTML já vem com templates expandidos pela wiki; precisamos só:
  1. remover "chrome" (edit links, navboxes, version banners, TOC, imagens);
  2. extrair infoboxes como bloco chave:valor (pandoc estraga tabelas verticais);
  3. preservar blocos de raw/token como código cercado;
  4. deixar o pandoc converter o resto com `-t gfm` (tabelas viram pipe tables).

NOTA IMPORTANTE: usar `-t gfm`, NÃO `-t gfm-raw_html`. Com raw_html desabilitado
o pandoc emite o placeholder literal "[TABLE]" para tabelas que não viram pipe
table — era essa a causa de 124 arquivos com "[TABLE]". Com `gfm` puro elas viram
pipe tables corretas.
"""
import re
import subprocess
import html as _html

from bs4 import BeautifulSoup

# Classes/elementos de navegação a remover por completo.
DROP_SELECTORS = [
    ".mw-editsection", ".toc", "#toc", ".navbox", ".vertical-navbox",
    ".version-table", ".noprint", ".metadata", ".mw-empty-elt",
    "style", "script", "sup.reference", ".reference", ".error",
    ".mw-jump-link", ".printfooter", ".catlinks", "#catlinks",
    "table.ratingbox", ".ambox", ".dablink", ".hatnote",
]

# Chaves de infobox que são só ruído (imagem, toggle, sub-template vazado).
NOISE_KEYS = ("toggle", "portrait", "graphic", "wikipedia article",
              "template:", "v · t · e", "v t e")

# Detecta navbox "V · T · E ..." (rodapé de navegação classificado como infobox).
NAVBOX_RE = re.compile(r"\bv\b\s*[·•∙]\s*\bt\b\s*[·•∙]\s*\be\b", re.I)


def _is_navbox(table):
    txt = table.get_text(" ", strip=True)
    return bool(NAVBOX_RE.search(txt)) or txt.count("·") > 25


def _row_is_noise(key, val):
    klow = key.lower()
    if not re.sub(r"[^a-z0-9]", "", klow):      # chave só de símbolos (tile art)
        return True
    if any(n in klow for n in NOISE_KEYS):
        return True
    if "template:" in val.lower():
        return True
    # linha gigante de arte ASCII (poucas letras, muitos símbolos)
    letters = len(re.sub(r"[^a-zA-Z]", "", key))
    if len(key) > 40 and letters < len(key) * 0.4:
        return True
    return False


def _extract_infobox(table):
    rows = []
    for tr in table.find_all("tr"):
        cells = tr.find_all(["th", "td"], recursive=False)
        if len(cells) == 2:
            key = cells[0].get_text(" ", strip=True)
            val = cells[1].get_text(" ", strip=True)
        elif len(cells) == 1:
            key, val = cells[0].get_text(" ", strip=True), ""
        else:
            continue
        key = re.sub(r"\s+", " ", key).strip(" :·•")
        val = re.sub(r"\s+", " ", val).strip(" :·•")
        if not key or _row_is_noise(key, val):
            continue
        rows.append((key, val))
    return rows


def _infobox_to_md(rows):
    if not rows:
        return ""
    lines = ["## Dados (infobox)", ""]
    for key, val in rows:
        lines.append(f"- **{key}:** {val}" if val else f"- **{key}**")
    return "\n".join(lines) + "\n\n"


def _raw_blocks_to_code(soup):
    """Blocos gamedata (tokens [CREATURE:...]) → <pre> p/ virarem code fence."""
    for table in soup.select("table.gamedata"):
        txt = table.get_text("\n", strip=False)
        txt = re.sub(r"^\s*Raws\s*\n", "", txt)
        pre = soup.new_tag("pre")
        pre.string = txt.strip("\n")
        table.replace_with(pre)


def _strip_chrome(soup):
    for sel in DROP_SELECTORS:
        for el in soup.select(sel):
            el.decompose()
    for el in soup.find_all(["img", "figure", "figcaption"]):
        el.decompose()


def _flatten_table_cells(soup):
    """Achata conteúdo de bloco dentro de células (td/th) para inline, garantindo
    que toda tabela vire pipe table no pandoc (cells com <p>/<ul>/<dl> fariam o
    pandoc cair para HTML cru / texto empilhado, perdendo a grade)."""
    for cell in soup.find_all(["td", "th"]):
        if cell.find(["p", "ul", "ol", "dl", "div", "br", "table"]):
            text = cell.get_text(" / ", strip=True)
            text = re.sub(r"(\s*/\s*)+", " / ", text).strip(" /")
            text = re.sub(r"\s+", " ", text)
            cell.clear()
            cell.append(text)


def clean_html(html):
    """Retorna (infobox_md, soup_limpo) pronto p/ pandoc."""
    soup = BeautifulSoup(html, "lxml")
    _strip_chrome(soup)
    _raw_blocks_to_code(soup)

    # Infoboxes ANTES de achatar células (senão os separadores " / " vazam nelas).
    infobox_md = ""
    for table in soup.select("table.infobox"):
        if _is_navbox(table):
            table.decompose()
            continue
        infobox_md += _infobox_to_md(_extract_infobox(table))
        table.decompose()

    _flatten_table_cells(soup)      # só nas tabelas de dados restantes
    return infobox_md, soup


def pandoc_html_to_md(html_fragment):
    try:
        p = subprocess.run(
            ["pandoc", "-f", "html", "-t", "gfm", "--wrap=none"],
            input=html_fragment, capture_output=True, text=True, timeout=120)
        return p.stdout
    except Exception:
        return ""


def post_process(md):
    md = _html.unescape(md)                              # &nbsp; &#10; etc.
    for _ in range(3):                                   # links → texto puro
        md = re.sub(r"\[([^\[\]]+)\]\([^)]*\)", r"\1", md)
    md = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", md)         # imagens residuais
    md = re.sub(r"\{[.#][^{}\n]*\}", "", md)             # atributos {.class}/{#id}
    md = re.sub(r"<[^>\n]+>", "", md)                    # tags HTML residuais
    md = re.sub(r"[ \t]+\n", "\n", md)
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md.strip()


def _header(title, url):
    return (f"# {title}\n\n"
            f"> Fonte: [{title}]({url}) — Dwarf Fortress Wiki (GFDL & MIT). "
            f"Snapshot 2026-06.\n\n")


def to_markdown(html, title, url, categories=None):
    """HTML renderizado → markdown final com header."""
    # Páginas /raw são tokens puros: code fence direto, sem pandoc (evita escape).
    if title.endswith("/raw") or title.endswith(" raw"):
        soup = BeautifulSoup(html, "lxml")
        _strip_chrome(soup)
        body = soup.get_text("\n", strip=False).strip("\n")
        body = re.sub(r"\n{3,}", "\n\n", body)
        return _header(title, url) + "```\n" + body + "\n```\n"

    infobox_md, soup = clean_html(html)
    body = post_process(pandoc_html_to_md(str(soup)))
    parts = [_header(title, url)]
    if infobox_md:
        parts.append(infobox_md)
    parts.append(body)
    return "".join(parts).strip() + "\n"
