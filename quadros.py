# -*- coding: utf-8 -*-
"""Extrai quadros (PNG) de uma Scene renderizada, para conferir o que está
na tela em vez de confiar só no código.

Renderiza em -ql — ou reaproveita o mp4 se ele já existe e é mais novo que
todos os .py do filme — e tira um PNG por instante com o ffmpeg, em
media/quadros/<Scene>/.

Um instante pode ser:
    12.5            segundos desde o começo do vídeo
    V1N01+3.2       segundos depois de a fala V1N01 começar (o narra()
                    daquela tag); V1N01 sozinho = o começo dela
    fecha=V1N01+9   qualquer um dos dois com um nome, que vai no arquivo

O começo de cada tag sai do próprio render: quadros.py roda o Manim com o
narra() instrumentado (só aqui, em memória — ferramentas.py não muda) e
grava media/quadros/<Scene>/marcas.json. Instantes por tag sobrevivem a
mudanças de duração em outras falas; segundos absolutos, não.

Uso:
    python quadros.py VideoIntro 3.5 V1N01+9.1 fecha=V1N01+9.4
    python quadros.py VideoIntro --marcas          # só lista o começo das tags
    python quadros.py Teste 0.5 --arquivo outro.py # Scene de outro arquivo
    python quadros.py VideoIntro 12 --forcar       # renderiza mesmo se fresco
"""

import argparse
import json
import re
import subprocess
import sys
from contextlib import contextmanager
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
QUALIDADE = "480p15"                 # a pasta que o -ql gera

INSTANTE = re.compile(r"^(?:(?P<nome>[\w-]+)=)?"
                      r"(?:(?P<tag>[A-Z]+\d*N?\d+)(?P<desl>[+-]\d+(?:\.\d+)?)?"
                      r"|(?P<seg>\d+(?:\.\d+)?))$")


def _instrumenta(destino):
    """Troca o narra() por um que anota o instante em que cada tag começa.
    Tem de rodar ANTES de o arquivo da Scene ser importado: capítulos e
    vídeos fazem `from ..ferramentas import narra`, que copia o nome."""
    import shor.ferramentas as f
    original = f.narra
    marcas = {}

    @contextmanager
    def narra(cena, tag, est=3.0):
        marcas.setdefault(tag, round(f._agora(cena), 3))
        with original(cena, tag, est) as dur:
            yield dur

    f.narra = narra
    return marcas


def _roda_manim(destino, arquivo, cena):
    """Modo interno (quadros.py --_manim): o Manim de verdade, pela mesma
    linha de comando do `manim -ql`, com o narra() instrumentado."""
    marcas = _instrumenta(destino)
    from manim.__main__ import main
    main(args=["render", "-ql", arquivo, cena], standalone_mode=False)
    Path(destino).write_text(json.dumps(marcas, indent=1), encoding="utf-8")


def _mp4(arquivo, cena):
    return RAIZ / "media" / "videos" / Path(arquivo).stem / QUALIDADE / f"{cena}.mp4"


def _fresco(mp4, arquivo):
    """O mp4 existe e é mais novo que o arquivo da Scene e que todo .py de
    shor/ (inclusive duracoes.py, que muda os tempos)."""
    if not mp4.exists():
        return False
    fontes = [Path(arquivo), *RAIZ.glob("shor/**/*.py")]
    return mp4.stat().st_mtime > max(f.stat().st_mtime for f in fontes)


def _duracao(mp4):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                        "format=duration", "-of", "csv=p=0", str(mp4)],
                       capture_output=True, text=True, check=True)
    return float(r.stdout.strip())


def _le_marcas(pasta, mp4):
    """As marcas só valem para o mp4 de que saíram."""
    arq = pasta / "marcas.json"
    if not arq.exists():
        return None
    dados = json.loads(arq.read_text(encoding="utf-8"))
    if dados.get("_mp4_mtime") != mp4.stat().st_mtime:
        return None
    return dados["marcas"]


def _renderiza(arquivo, cena, pasta, mp4):
    pasta.mkdir(parents=True, exist_ok=True)
    tmp = pasta / "marcas.tmp.json"
    print(f">> renderizando {cena} em -ql …")
    subprocess.run([sys.executable, str(Path(__file__).resolve()), "--_manim",
                    str(tmp), arquivo, cena], cwd=RAIZ, check=True)
    if not mp4.exists():
        sys.exit(f"!! o render terminou mas não achei {mp4}")
    marcas = json.loads(tmp.read_text(encoding="utf-8"))
    tmp.unlink()
    (pasta / "marcas.json").write_text(
        json.dumps({"_mp4_mtime": mp4.stat().st_mtime, "marcas": marcas},
                   indent=1), encoding="utf-8")
    return marcas


def _resolve(spec, marcas):
    """'12.5' | 'V1N01+3.2' | 'nome=…' → (segundos, nome do arquivo)."""
    m = INSTANTE.match(spec)
    if not m:
        sys.exit(f"!! instante não entendido: {spec!r}")
    if m["seg"] is not None:
        t = float(m["seg"])
        rotulo = m["nome"]
    else:
        if m["tag"] not in marcas:
            sys.exit(f"!! a tag {m['tag']} não passou por nenhum narra() "
                     f"desta Scene (tem: {', '.join(marcas)})")
        t = marcas[m["tag"]] + float(m["desl"] or 0)
        rotulo = m["nome"] or m["tag"] + (m["desl"] or "")
    nome = f"t{t:07.2f}.png" if rotulo is None else f"{rotulo}_t{t:07.2f}.png"
    return t, nome


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--_manim":
        _roda_manim(*sys.argv[2:5])
        return

    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("cena", help="nome da Scene (ex.: VideoIntro)")
    ap.add_argument("instantes", nargs="*",
                    help="12.5 | V1N01+3.2 | nome=V1N01+3.2")
    ap.add_argument("--arquivo", default="filme_shor.py",
                    help="arquivo da Scene (padrão: filme_shor.py)")
    ap.add_argument("--forcar", action="store_true",
                    help="renderiza mesmo que o mp4 esteja fresco")
    ap.add_argument("--marcas", action="store_true",
                    help="lista o instante em que cada tag começa")
    a = ap.parse_args()

    arquivo = str(Path(a.arquivo).resolve())
    mp4 = _mp4(arquivo, a.cena)
    pasta = RAIZ / "media" / "quadros" / a.cena

    precisa_tag = a.marcas or any(INSTANTE.match(s) and INSTANTE.match(s)["tag"]
                                  for s in a.instantes)
    marcas = None
    if a.forcar or not _fresco(mp4, arquivo):
        marcas = _renderiza(arquivo, a.cena, pasta, mp4)
    else:
        print(f">> reaproveitando {mp4.relative_to(RAIZ)}")
        marcas = _le_marcas(pasta, mp4)
        if marcas is None and precisa_tag:
            print(">> o mp4 não tem marcas.json correspondente; renderizando")
            marcas = _renderiza(arquivo, a.cena, pasta, mp4)
    marcas = marcas or {}

    total = _duracao(mp4)
    if a.marcas:
        for tag, t in marcas.items():
            print(f"   {tag:8s} {t:8.2f} s")
        print(f"   {'(fim)':8s} {total:8.2f} s")

    pasta.mkdir(parents=True, exist_ok=True)
    for spec in a.instantes:
        t, nome = _resolve(spec, marcas)
        if not 0 <= t < total:
            print(f"!! {spec} = {t:.2f} s está fora do vídeo (0–{total:.2f} s)")
            continue
        png = pasta / nome
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{t:.3f}",
                        "-i", str(mp4), "-frames:v", "1", str(png)], check=True)
        print(f"   {spec:>20s}  {t:8.2f} s  →  {png.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()
