"""Gera os arquivos da identidade visual Search.CRT / Search.CFT.

Uso: python tools/gerar_identidade.py assets/identidade
Dependências: pip install cairosvg fonttools pillow
Fonte: baixe a Inter (rsms.me/inter) e aponte INTER_DIR para a pasta com Inter-Medium.otf e Inter-ExtraBold.otf.
Textos viram curvas (paths) para renderizar igual em qualquer lugar (GitHub, navegador).
"""
import os
import sys

import cairosvg
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from PIL import Image

FONTES = os.environ.get("INTER_DIR", "/usr/share/fonts/opentype/inter")
REG = TTFont(os.path.join(FONTES, "Inter-Medium.otf"))
BOLD = TTFont(os.path.join(FONTES, "Inter-ExtraBold.otf"))

# ---------- Paleta oficial ----------
AZUL_INST = "#0B2545"   # Azul Institucional
AZUL_PROF = "#13315C"   # Azul Profundo
AZUL_MEDIO = "#1F4E8C"  # Azul Médio
CIANO = "#22B8CF"       # Ciano Busca (destaque / cruzamento)
CIANO_CLARO = "#8FD8E6"
VERDE = "#2BB673"       # Verde Confere
BRANCO = "#FFFFFF"
NEVOA = "#F4F7FB"


def texto_em_curvas(texto, fonte, tamanho, x, y, cor, espaco=0.0):
    """Converte texto em <path>. Retorna (svg, largura)."""
    gs = fonte.getGlyphSet()
    cmap = fonte.getBestCmap()
    upm = fonte["head"].unitsPerEm
    esc = tamanho / upm
    hmtx = fonte["hmtx"]
    caminhos = []
    cursor = 0.0
    for ch in texto:
        nome = cmap.get(ord(ch))
        if nome is None:
            continue
        pen = SVGPathPen(gs)
        tpen = TransformPen(pen, (esc, 0, 0, -esc, x + cursor, y))
        gs[nome].draw(tpen)
        d = pen.getCommands()
        if d:
            caminhos.append(d)
        cursor += hmtx[nome][0] * esc + espaco * tamanho
    return f'<path fill="{cor}" d="{" ".join(caminhos)}"/>', cursor - espaco * tamanho


def simbolo(x, y, s, anel, cabo, aros, miolo, fundo=None, raio_fundo=0.22):
    """Lupa com dois aros sobrepostos; a interseção (o 'cruzamento') fica preenchida.
    Desenhado em grade de 64 unidades, escalado para s px."""
    k = s / 64
    cid = f"c{abs(hash((x, y, s, anel))) % 10**8}"
    partes = []
    if fundo:
        partes.append(f'<rect x="0" y="0" width="64" height="64" rx="{64*raio_fundo}" fill="{fundo}"/>')
    partes.append(f"""
      <defs><clipPath id="{cid}"><circle cx="22.5" cy="26" r="7.5"/></clipPath></defs>
      <line x1="37.5" y1="37.5" x2="51" y2="51" stroke="{cabo}" stroke-width="7.5" stroke-linecap="round"/>
      <circle cx="27" cy="26" r="16" fill="none" stroke="{anel}" stroke-width="5"/>
      <circle cx="31.5" cy="26" r="7.5" fill="{miolo}" clip-path="url(#{cid})"/>
      <circle cx="22.5" cy="26" r="7.5" fill="none" stroke="{aros}" stroke-width="2.2"/>
      <circle cx="31.5" cy="26" r="7.5" fill="none" stroke="{aros}" stroke-width="2.2"/>""")
    return f'<g transform="translate({x} {y}) scale({k})">{"".join(partes)}</g>'


def svg(w, h, corpo, fundo=None):
    bg = f'<rect width="{w}" height="{h}" fill="{fundo}"/>' if fundo else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">'
            f"{bg}{corpo}</svg>")


def logo_horizontal(sufixo, negativo=False, assinatura=None):
    cor_txt = BRANCO if negativo else AZUL_INST
    anel = BRANCO if negativo else AZUL_INST
    aros = CIANO_CLARO if negativo else AZUL_MEDIO
    s = 96
    corpo = simbolo(0, 12, s, anel=anel, cabo=CIANO, aros=aros, miolo=CIANO)
    x0 = s + 22
    t1, w1 = texto_em_curvas("Search", REG, 62, x0, 84, cor_txt, espaco=-0.02)
    t2, w2 = texto_em_curvas(f".{sufixo}", BOLD, 62, x0 + w1 + 2, 84, CIANO, espaco=-0.01)
    corpo += t1 + t2
    largura = x0 + w1 + 2 + w2 + 8
    altura = 120
    if assinatura:
        t3, w3 = texto_em_curvas(assinatura, REG, 15.5, x0 + 2, 110,
                                 CIANO_CLARO if negativo else "#4A5668", espaco=0.06)
        corpo += t3
        largura = max(largura, x0 + w3 + 8)
    return svg(round(largura), altura, corpo)


def main(dest):
    os.makedirs(dest, exist_ok=True)
    arquivos = {}

    # Símbolo solto (fundo transparente) e ícone de app (fundo azul)
    arquivos["simbolo.svg"] = svg(64, 64, simbolo(0, 0, 64, AZUL_INST, CIANO, AZUL_MEDIO, CIANO))
    arquivos["simbolo-negativo.svg"] = svg(64, 64, simbolo(0, 0, 64, BRANCO, CIANO, CIANO_CLARO, CIANO))
    arquivos["icone-app.svg"] = svg(64, 64, simbolo(0, 0, 64, BRANCO, CIANO, CIANO_CLARO, CIANO, fundo=AZUL_INST))

    # Logos da família
    for suf in ("CRT", "CFT"):
        base = suf.lower()
        arquivos[f"logo-search-{base}.svg"] = logo_horizontal(suf)
        arquivos[f"logo-search-{base}-negativo.svg"] = logo_horizontal(suf, negativo=True)
    arquivos["logo-search-crt-es.svg"] = logo_horizontal(
        "CRT", assinatura="ES  ·  SISTEMA CFT/CRTs")
    arquivos["logo-search-crt-es-negativo.svg"] = logo_horizontal(
        "CRT", negativo=True, assinatura="ES  ·  SISTEMA CFT/CRTs")

    for nome, conteudo in arquivos.items():
        with open(os.path.join(dest, nome), "w", encoding="utf-8") as f:
            f.write(conteudo)

    # PNGs e ICO do ícone do app
    pngs = []
    for tam in (16, 24, 32, 48, 64, 128, 256, 512):
        p = os.path.join(dest, f"icone-{tam}.png")
        cairosvg.svg2png(bytestring=arquivos["icone-app.svg"].encode(), write_to=p,
                         output_width=tam, output_height=tam)
        pngs.append(p)
    img = Image.open(os.path.join(dest, "icone-256.png"))
    img.save(os.path.join(dest, "searchcrt.ico"),
             sizes=[(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])
    # Mantém só os tamanhos úteis no repositório
    for tam in (16, 24, 48, 128):
        os.remove(os.path.join(dest, f"icone-{tam}.png"))

    # Versões PNG dos logos (para documentos e apresentações)
    for nome in list(arquivos):
        if nome.startswith("logo-"):
            cairosvg.svg2png(bytestring=arquivos[nome].encode(),
                             write_to=os.path.join(dest, nome.replace(".svg", ".png")), scale=3)
    print("Gerados:", sorted(os.listdir(dest)))


if __name__ == "__main__":
    main(sys.argv[1])
