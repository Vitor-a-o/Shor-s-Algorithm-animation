# -*- coding: utf-8 -*-
"""Lista os textos de tela de shor/textos.py numa tabela markdown.

Só leitura: não mexe em nada, imprime na saída padrão.

    python listar_textos.py                                         # na tela
    python listar_textos.py > roteiros/textos_para_traduzir.md   # para traduzir

Colunas: chave | pt | en | observação. A observação junta os comentários
que estão acima da chave em textos.py (token de formula, glifos, modelo) e
os lugares do código onde ela é usada. As chaves que são token de uma
fórmula ou de um VGroup indexado saem marcadas com ⚠ — nelas a tradução
tem de manter um token por chave. As de "glifos" também levam ⚠: a
animação conta as letras delas.
"""

import ast
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
TEXTOS_PY = RAIZ / "shor" / "textos.py"


def le_textos():
    """{chave: {"pt": ..., "en": ...}} lido do fonte, sem importar o pacote."""
    arvore = ast.parse(TEXTOS_PY.read_text(encoding="utf-8"))
    for no in arvore.body:
        if (isinstance(no, ast.Assign) and isinstance(no.targets[0], ast.Name)
                and no.targets[0].id == "TEXTOS"):
            return ast.literal_eval(no.value)
    raise SystemExit("TEXTOS não encontrado em shor/textos.py")


def le_comentarios():
    """{chave: [comentários logo acima dela em textos.py]} — cada comentário
    começa por uma das marcas abaixo; as linhas seguintes emendam nele."""
    marcas = ("token de", "glifos", "modelo", "também é", "em ")
    notas, pendentes = {}, []
    for linha in TEXTOS_PY.read_text(encoding="utf-8").splitlines():
        s = linha.strip()
        m = re.match(r'"([^"]+)": \{"pt"', s)
        if m:
            notas[m.group(1)] = pendentes
            pendentes = []
        elif s.startswith("# ") and not s.startswith("# ---"):
            s = s[2:].strip()
            if pendentes and not s.startswith(marcas):
                pendentes[-1] += " " + s
            else:
                pendentes.append(s)
        else:
            pendentes = []
    return notas


def le_usos():
    """{chave: ["arquivo.py:linha", ...]} — onde cada tx("chave") aparece."""
    usos = {}
    for py in sorted((RAIZ / "shor").rglob("*.py")):
        if py.name == "textos.py":
            continue
        for n, linha in enumerate(py.read_text(encoding="utf-8").splitlines(), 1):
            for m in re.finditer(r'tx\("([^"]+)"\)', linha):
                usos.setdefault(m.group(1), []).append(f"{py.name}:{n}")
    return usos


def celula(s):
    s = "" if s is None else str(s)
    return s.replace("|", "\\|").replace("\n", " ")


def main():
    textos, notas, usos = le_textos(), le_comentarios(), le_usos()
    def tem(chave, marca):
        return any(c.startswith(marca) for c in notas.get(chave, []))
    n_tok = sum(1 for k in textos if tem(k, "token de"))
    n_gli = sum(1 for k in textos if tem(k, "glifos"))
    print("# Textos de tela para traduzir")
    print()
    print("Gerado por `python listar_textos.py` a partir de `shor/textos.py` — "
          "não editar à mão; a tradução vai no campo `\"en\"` de lá.")
    print()
    print(f"{len(textos)} chaves · {n_tok} marcadas com ⚠ token indexado "
          "(token de fórmula ou de VGroup indexado: manter um token por chave, "
          f"sem juntar nem quebrar) · {n_gli} com ⚠ glifos indexados (contagem "
          "de letras amarrada à animação) · en vazio = cai no português.")
    print()
    print("| chave | pt | en | observação |")
    print("|---|---|---|---|")
    for chave, valores in textos.items():
        obs = list(notas.get(chave, []))
        if tem(chave, "token de"):
            obs.insert(0, "⚠ token indexado")
        if tem(chave, "glifos"):
            obs.insert(0, "⚠ glifos indexados")
        if chave in usos:
            obs.append("usado em " + ", ".join(usos[chave]))
        else:
            obs.append("SEM USO no código")
        print(f"| `{chave}` | {celula(valores['pt'])} | "
              f"{celula(valores.get('en'))} | {celula(' · '.join(obs))} |")


if __name__ == "__main__":
    main()
