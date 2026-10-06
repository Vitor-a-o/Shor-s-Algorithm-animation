# -*- coding: utf-8 -*-
"""Confere a largura dos textos em inglês de shor/textos.py contra o pt.

Não renderiza nada — só instancia Text do Manim para medir largura. Para
cada chave com "en" preenchido, monta o texto em pt e em en no MESMO
tamanho de fonte que o código usa naquela chave: procura no fonte a
chamada `T(tx("<chave>"), <tamanho>)`, `formula(..., tamanho=<tamanho>)`
ou qualquer chamada com `tamanho=` envolvendo a tx(); sem uso detectável
cai em 30, marcado "presumido". Havendo mais de um uso com tamanhos
diferentes, usa o maior (pior caso para estourar o quadro).

    python checar_textos.py              # tabela no terminal
    python checar_textos.py --salvar     # idem, e grava roteiros/larguras.md

Sai com código 1 se algum texto em inglês passar de 90% da largura do
quadro (config.frame_width) — rodar antes de cada render em inglês.
"""

import argparse
import ast
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
TEXTOS_PY = RAIZ / "shor" / "textos.py"
SHOR_DIR = RAIZ / "shor"
SAIDA = RAIZ / "roteiros" / "larguras.md"
LIMIAR = 0.90


def le_textos():
    """{chave: {"pt": ..., "en": ...}} lido do fonte, sem importar o pacote."""
    arvore = ast.parse(TEXTOS_PY.read_text(encoding="utf-8"))
    for no in arvore.body:
        if (isinstance(no, ast.Assign) and isinstance(no.targets[0], ast.Name)
                and no.targets[0].id == "TEXTOS"):
            return ast.literal_eval(no.value)
    raise SystemExit("TEXTOS não encontrado em shor/textos.py")


def _const(node):
    try:
        v = ast.literal_eval(node)
    except Exception:
        return None
    return v if isinstance(v, (int, float)) else None


def _resolve_tamanho(pilha):
    """Tamanho de fonte da chamada que envolve um tx(...), olhando a pilha
    de Call ancestrais do mais próximo ao mais distante."""
    for anc in reversed(pilha):
        if not isinstance(anc.func, ast.Name):
            continue
        nome = anc.func.id
        if nome == "T":
            if len(anc.args) >= 2:
                v = _const(anc.args[1])
                if v is not None:
                    return v, "T() direto"
            for kw in anc.keywords:
                if kw.arg == "tamanho":
                    v = _const(kw.value)
                    if v is not None:
                        return v, "T() tamanho="
            return 30, "T() padrão"
        if nome == "formula":
            for kw in anc.keywords:
                if kw.arg == "tamanho":
                    v = _const(kw.value)
                    if v is not None:
                        return v, "formula() tamanho="
            return 32, "formula() padrão"
        for kw in anc.keywords:
            if kw.arg == "tamanho":
                v = _const(kw.value)
                if v is not None:
                    return v, f"{nome}(tamanho=)"
    return None, None


class _Buscador(ast.NodeVisitor):
    """Coleta toda chamada tx("chave") de um arquivo com o tamanho de fonte
    resolvido a partir da chamada que a envolve (T(), formula(), ...)."""

    def __init__(self):
        self.achados = []  # (chave, lineno, tamanho|None, metodo|None)
        self.pilha = []

    def visit_Call(self, node):
        if (isinstance(node.func, ast.Name) and node.func.id == "tx"
                and node.args and isinstance(node.args[0], ast.Constant)
                and isinstance(node.args[0].value, str)):
            tamanho, metodo = _resolve_tamanho(self.pilha)
            self.achados.append((node.args[0].value, node.lineno, tamanho, metodo))
        self.pilha.append(node)
        self.generic_visit(node)
        self.pilha.pop()


def mapeia_usos():
    """{chave: [(arquivo, linha, tamanho|None, metodo|None), ...]}"""
    usos = {}
    for py in sorted(SHOR_DIR.rglob("*.py")):
        if py.name == "textos.py" or "__pycache__" in py.parts:
            continue
        arvore = ast.parse(py.read_text(encoding="utf-8"), filename=str(py))
        b = _Buscador()
        b.visit(arvore)
        for chave, linha, tamanho, metodo in b.achados:
            usos.setdefault(chave, []).append((py.name, linha, tamanho, metodo))
    return usos


def tamanho_da_chave(chave, usos):
    achados = [u for u in usos.get(chave, []) if u[2] is not None]
    if not achados:
        return 30, True, "nenhum uso com tamanho detectável"
    tamanho = max(t for _, _, t, _ in achados)
    detalhe = "; ".join(f"{f}:{l} tam={t} ({m})" for f, l, t, m in achados)
    return tamanho, False, detalhe


def mede(texto, tamanho):
    from manim import Text
    return Text(texto, font_size=tamanho).width


def confere(textos=None, usos=None):
    """Lista de linhas (dict), maior razão en/pt primeiro."""
    from manim import config
    textos = le_textos() if textos is None else textos
    usos = mapeia_usos() if usos is None else usos
    quadro = config.frame_width
    linhas = []
    for chave, valores in textos.items():
        en = valores.get("en")
        if not en:
            continue
        tamanho, presumido, detalhe = tamanho_da_chave(chave, usos)
        larg_pt = mede(valores["pt"], tamanho)
        larg_en = mede(en, tamanho)
        linhas.append({
            "chave": chave, "pt": valores["pt"], "en": en,
            "tamanho": tamanho, "presumido": presumido, "detalhe": detalhe,
            "largura_pt": larg_pt, "largura_en": larg_en,
            "razao": larg_en / larg_pt if larg_pt else float("inf"),
            "estoura": larg_en > LIMIAR * quadro,
        })
    linhas.sort(key=lambda l: l["razao"], reverse=True)
    return linhas, quadro


def tabela_markdown(linhas, quadro):
    out = [f"Quadro: {quadro:.2f} (limiar {LIMIAR:.0%} = {LIMIAR * quadro:.2f})", ""]
    out.append("| chave | tamanho | largura pt | largura en | razão en/pt | estoura? |")
    out.append("|---|---|---|---|---|---|")
    for l in linhas:
        tam = f"{l['tamanho']}" + (" (presumido)" if l["presumido"] else "")
        out.append(
            f"| `{l['chave']}` | {tam} | {l['largura_pt']:.2f} | "
            f"{l['largura_en']:.2f} | {l['razao']:.2f} | "
            f"{'⚠ SIM' if l['estoura'] else 'não'} |"
        )
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                  formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--salvar", action="store_true",
                     help=f"grava a tabela em {SAIDA.relative_to(RAIZ)}")
    args = ap.parse_args()

    linhas, quadro = confere()
    md = tabela_markdown(linhas, quadro)
    print(md)
    if not linhas:
        print('\n(nenhuma chave com "en" preenchido ainda)')

    if args.salvar:
        SAIDA.parent.mkdir(parents=True, exist_ok=True)
        SAIDA.write_text(md + "\n", encoding="utf-8")
        print(f"\nGravado em {SAIDA.relative_to(RAIZ)}")

    if any(l["estoura"] for l in linhas):
        sys.exit(1)


if __name__ == "__main__":
    main()
