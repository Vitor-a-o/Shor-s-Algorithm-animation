# -*- coding: utf-8 -*-
"""Confere os roteiros (.md) contra o código dos capítulos (.py).

O contrato da série é a TAG: cada linha da tabela de um roteiro tem que
virar exatamente uma chamada de narra()/so_fala() no capítulo correspondente,
na mesma ordem e com a mesma estimativa.

Uso:
    python conferir.py                 # confere tudo o que encontrar
    python conferir.py 6 7 8           # só esses capítulos
    python conferir.py --quiet         # só os problemas

Sai com código 1 se houver qualquer ERRO (avisos não derrubam).
Só leitura: este script nunca escreve nada.
"""

import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent

# pastas que não são código do filme
IGNORAR = {".venv", "venv", "media", "__pycache__", ".git", "node_modules",
           "site-packages", ".mypy_cache", ".pytest_cache"}


def varre(padrao):
    """glob recursivo pulando .venv, media, __pycache__ e afins."""
    return sorted(f for f in RAIZ.glob(padrao)
                  if not (IGNORAR & set(f.parts)))

# --------------------------------------------------------------------------
# leitura dos roteiros
# --------------------------------------------------------------------------

TAG = re.compile(r"^(?:C(\d+)N(\d+)|V(\d+)N(\d+)|CAP(\d+))$")
EST = re.compile(r"^\d+,\d$")


def le_roteiros():
    """{tag: (est, arquivo, ordem_global)} a partir das tabelas dos .md."""
    fala = {}
    arquivos = varre("**/roteiro_video*.md")
    if not arquivos:
        print("!! nenhum roteiro_video*.md encontrado a partir de", RAIZ)
    for md in arquivos:
        i = 0
        for linha in md.read_text(encoding="utf-8").splitlines():
            col = [c.strip() for c in linha.split("|")]
            if len(col) < 5:
                continue
            tag, est = col[1], col[3]
            if not TAG.match(tag) or not EST.match(est):
                continue
            if tag in fala:
                print(f"ERRO  tag {tag} aparece em dois roteiros "
                      f"({fala[tag][1].name} e {md.name})")
            fala[tag] = (float(est.replace(",", ".")), md, i)
            i += 1
    return fala, arquivos


# --------------------------------------------------------------------------
# leitura do código
# --------------------------------------------------------------------------

CHAMADA = re.compile(
    r"""\b(?:narra|so_fala)\s*\(\s*cena\s*,\s*["']([A-Za-z0-9_]+)["']\s*"""
    r"""(?:,\s*(?:est\s*=\s*)?([0-9]+(?:\.[0-9]+)?))?""",
    re.VERBOSE)


def le_codigo():
    """{tag: [(est|None, arquivo, linha, ordem)]} — lista para pegar duplicata."""
    uso = {}
    # todo .py do projeto, menos as ferramentas de linha de comando
    arquivos = [f for f in varre("**/*.py")
                if f.name not in ("conferir.py", "medir.py", "duracoes.py")]
    for py in arquivos:
        for n, linha in enumerate(py.read_text(encoding="utf-8").splitlines(), 1):
            for m in CHAMADA.finditer(linha):
                tag, est = m.group(1), m.group(2)
                uso.setdefault(tag, []).append(
                    (float(est) if est else None, py, n, len(uso)))
    return uso, arquivos


def cartoes_de_montagem():
    """CARTOES = {6: 4.6, ...} do montagem.py — os CAP são gerados por f-string."""
    for py in varre("**/montagem.py"):
        txt = py.read_text(encoding="utf-8")
        m = re.search(r"CARTOES\s*=\s*\{(.*?)\}", txt, re.S)
        if m:
            return {int(k): float(v) for k, v in
                    re.findall(r"(\d+)\s*:\s*([0-9.]+)", m.group(1))}, py
    return {}, None


# --------------------------------------------------------------------------
# checagens
# --------------------------------------------------------------------------

def capitulo_da_tag(tag):
    m = TAG.match(tag)
    if not m:
        return None
    return int(m.group(1) or m.group(5) or 0)


def main():
    alvo = {int(a) for a in sys.argv[1:] if a.isdigit()}
    quieto = "--quiet" in sys.argv

    fala, mds = le_roteiros()
    uso, pys = le_codigo()
    cartoes, mont = cartoes_de_montagem()

    if not quieto:
        print(f"roteiros: {', '.join(m.name for m in mds) or '(nenhum)'}")
        print(f"código:   {len(pys)} arquivos\n")

    erros = avisos = 0

    def erro(msg):
        nonlocal erros
        erros += 1
        print("ERRO  " + msg)

    def aviso(msg):
        nonlocal avisos
        avisos += 1
        print("aviso " + msg)

    # 1) tags contíguas dentro de cada capítulo do roteiro
    porcap = {}
    for tag, (est, md, i) in fala.items():
        m = TAG.match(tag)
        if m.group(1):                       # CxxNyy
            porcap.setdefault(int(m.group(1)), []).append((int(m.group(2)), tag))
    for cap, lista in sorted(porcap.items()):
        if alvo and cap not in alvo:
            continue
        nums = sorted(n for n, _ in lista)
        esperado = list(range(1, len(nums) + 1))
        if nums != esperado:
            faltando = sorted(set(esperado) - set(nums))
            repetido = sorted({n for n in nums if nums.count(n) > 1})
            if faltando:
                erro(f"capítulo {cap}: buraco na numeração — falta "
                     + ", ".join(f"C{cap}N{n:02d}" for n in faltando))
            if repetido:
                erro(f"capítulo {cap}: tag repetida no roteiro — "
                     + ", ".join(f"C{cap}N{n:02d}" for n in repetido))

    # 2) roteiro -> código
    for tag, (est, md, i) in sorted(fala.items(), key=lambda kv: kv[1][2]):
        cap = capitulo_da_tag(tag)
        if alvo and cap not in alvo:
            continue
        if tag.startswith("CAP"):
            n = int(tag[3:])
            if tag in uso:
                # alguns cartões são chamados com a tag literal (ex.: video2.py)
                if len(uso[tag]) > 1:
                    onde = ", ".join(f"{p.name}:{ln}" for _, p, ln, _ in uso[tag])
                    erro(f"{tag}: chamado {len(uso[tag])} vezes ({onde})")
                e = uso[tag][0][0]
                if e is not None and abs(e - est) > 0.051:
                    erro(f"{tag}: est={e} no código e {est:.1f} no roteiro")
            elif n not in cartoes:
                erro(f"{tag}: sem entrada em CARTOES do montagem.py "
                     f"(roteiro pede {est:.1f} s, o código vai usar o padrão 3.0)")
            elif abs(cartoes[n] - est) > 0.051:
                erro(f"{tag}: CARTOES[{n}] = {cartoes[n]:.1f} mas o roteiro diz {est:.1f}")
            continue
        if tag not in uso:
            erro(f"{tag}: está no roteiro e não existe no código")
            continue
        if len(uso[tag]) > 1:
            onde = ", ".join(f"{p.name}:{n}" for _, p, n, _ in uso[tag])
            erro(f"{tag}: chamada {len(uso[tag])} vezes ({onde})")
        est_cod = uso[tag][0][0]
        if est_cod is None:
            aviso(f"{tag}: narra() sem est= — vai cair no padrão 3.0 se faltar áudio")
        elif abs(est_cod - est) > 0.051:
            p, n = uso[tag][0][1], uso[tag][0][2]
            erro(f"{tag}: est={est_cod} no código ({p.name}:{n}) "
                 f"e {est:.1f} no roteiro")

    # 3) código -> roteiro
    for tag, ocorrencias in sorted(uso.items()):
        cap = capitulo_da_tag(tag)
        if alvo and cap not in alvo:
            continue
        if not TAG.match(tag):
            continue          # tags do filme completo (ABN01, FIM01, …)
        if tag not in fala and not tag.startswith("CAP"):
            p, n = ocorrencias[0][1], ocorrencias[0][2]
            erro(f"{tag}: está no código ({p.name}:{n}) e não existe em roteiro nenhum")

    # 4) ordem: as tags de um capítulo têm que aparecer no código na ordem do roteiro
    for cap, lista in sorted(porcap.items()):
        if alvo and cap not in alvo:
            continue
        ordem_cod = [(uso[t][0][2], t) for _, t in sorted(lista)
                     if t in uso and len(uso[t]) == 1]
        linhas = [l for l, _ in ordem_cod]
        if linhas != sorted(linhas):
            fora = [t for (l, t), (l2, _) in zip(ordem_cod, sorted(ordem_cod))
                    if l != l2]
            erro(f"capítulo {cap}: tags fora de ordem no código — {', '.join(fora[:6])}")

    # 5) higiene: wait() solto e cor fora da paleta
    for py in pys:
        cap = None
        m = re.search(r"capitulo(\d+)", py.name)
        if m:
            cap = int(m.group(1))
        if alvo and cap not in alvo:
            continue
        txt = py.read_text(encoding="utf-8")
        n_wait = len(re.findall(r"cena\.wait\(", txt))
        if n_wait:
            aviso(f"{py.name}: {n_wait} cena.wait() solto — quem dá o respiro é o PAD")
        hex_cor = set(re.findall(r'"#[0-9A-Fa-f]{6}"', txt))
        if hex_cor:
            aviso(f"{py.name}: cor fora da paleta — {', '.join(sorted(hex_cor))}")

    # --------------------------------------------------------------------
    total = sum(est for tag, (est, _, _) in fala.items()
                if not alvo or capitulo_da_tag(tag) in alvo)
    print()
    print(f"{len(fala)} tags no roteiro · {sum(len(v) for v in uso.values())} "
          f"chamadas no código · {total:.1f} s de fala estimada")
    print(f"{erros} erro(s), {avisos} aviso(s)")
    return 1 if erros else 0


if __name__ == "__main__":
    sys.exit(main())
