# -*- coding: utf-8 -*-
"""O cadeado da série — a criptografia que protege a internet.

Genérico de propósito: é usado fechado no encerramento do vídeo 2 (V2N01),
abre e fecha na abertura do vídeo 1, ganha rótulos gravados no corpo
(RSA no V1N03, "fatorar n" no V3N01) e uma rachadura parcial no V3N02.
É também a peça central da fase 0 do capítulo 8.
"""

from manim import *
import numpy as np

from .paleta import CINZA, LARANJA, PRETO, VEL
from .ferramentas import T

# ângulo entre o arco fechado (como construído) e aberto — usado tanto na
# construção (estado="aberto") quanto nas animações abrir()/fechar()
_ABERTURA = -60 * DEGREES


def _rotulo(corpo, texto, tamanho=26, cor=PRETO):
    """Texto centrado no corpo, encolhido se não couber (ex.: "fatorar n")."""
    r = T(texto, tamanho, cor)
    if r.width > corpo.width - 0.3:
        r.scale_to_fit_width(corpo.width - 0.3)
    return r.move_to(corpo)


def cadeado(estado="fechado", rotulo=None):
    """VGroup [arco, corpo, …] com o ARCO separado do corpo, para que o
    cadeado possa abrir e fechar: animar `cad[0]` move só o arco.

    estado: "fechado" (arco encaixado) ou "aberto" (arco girado para cima,
    apoiado na perna direita). rotulo: texto opcional no corpo (sem rótulo,
    o corpo ganha o buraco de fechadura)."""
    corpo = RoundedRectangle(width=1.9, height=1.5, corner_radius=0.18)
    corpo.set_fill(LARANJA, opacity=1).set_stroke(PRETO, width=3)

    raio = 0.62
    topo = corpo.get_top()[1]
    arco = VGroup(
        Arc(radius=raio, start_angle=PI, angle=-PI,
            arc_center=[0, topo + 0.28, 0]),
        Line([-raio, topo + 0.28, 0], [-raio, topo - 0.18, 0]),
        Line([raio, topo + 0.28, 0], [raio, topo - 0.18, 0]))
    arco.set_stroke(PRETO, width=8)
    if estado == "aberto":
        arco.rotate(_ABERTURA, about_point=[raio, topo - 0.18, 0])

    cad = VGroup(arco, corpo)
    if rotulo is None:
        buraco = VGroup(Dot(radius=0.10, color=PRETO),
                        Line(ORIGIN, 0.26 * DOWN, color=PRETO,
                             stroke_width=6))
        buraco.arrange(DOWN, buff=0).move_to(corpo).shift(0.05 * UP)
        cad.add(buraco)
    else:
        cad.add(_rotulo(corpo, rotulo))
    return cad


def gravar(cena, cad, texto, tamanho=26, cor=PRETO, run_time=0.9):
    """Grava `texto` no corpo de um `cad` já em cena, com o mesmo flash
    seco do travamento (V1N01) — usado para "RSA" (V1N03) e "fatorar n"
    (V3N01). Substitui o buraco de fechadura ou rótulo anterior."""
    corpo = cad[1]
    novo = _rotulo(corpo, texto, tamanho, cor)
    antigo = cad[2] if len(cad) > 2 else None
    anims = [Write(novo),
             Flash(corpo.get_center(), color=PRETO, flash_radius=0.9,
                   line_length=0.25)]
    if antigo is not None:
        anims.insert(0, FadeOut(antigo))
    cena.play(*anims, run_time=run_time * VEL)
    if antigo is not None:
        cad.remove(antigo)
    cad.add(novo)
    return novo


def rachar(cena, cad, run_time=1.0):
    """Racha o arco pela metade sem que o cadeado se abra (V3N02) — a
    quebra completa (arco estala, pedaços caem) fica para o vídeo 4.

    A fissura CORRE pelo arco: zigue-zagueia perpendicular à curva (não na
    vertical) e com amplitude proporcional ao raio, para continuar colada
    ao traço em qualquer escala do cadeado."""
    arco = cad[0][0]  # o Arc, não as pernas
    centro = arco.get_arc_center()
    raio = float(np.linalg.norm(arco.point_from_proportion(0.5) - centro))
    amp = 0.07 * raio          # ~ a espessura do traço: racha, não descola
    # perfil da fissura: (proporção ao longo do arco, desvio radial em
    # frações de amp). Irregular de propósito — serrilha regular lê como
    # enfeite —, mas fixo, para o render ser reproduzível. Começa e acaba
    # em cima do traço, então ela nasce e MORRE dentro do arco
    perfil = ((0.30, 0.0), (0.36, -0.9), (0.42, 0.5), (0.47, -0.35),
              (0.52, 1.0), (0.57, -0.5), (0.62, 0.0))
    pontos = []
    for t, d in perfil:
        p = arco.point_from_proportion(t)
        radial = (p - centro) / np.linalg.norm(p - centro)
        pontos.append(p + d * amp * radial)
    rachadura = VMobject(stroke_color=CINZA, stroke_width=3)
    rachadura.set_points_as_corners(pontos)
    cena.play(Create(rachadura), run_time=run_time * VEL)
    cad.add(rachadura)
    return rachadura


# a fissura inteira, de ponta a ponta do arco. Os pontos entre 0,30 e 0,62
# são os MESMOS do perfil do rachar(): a rachadura parcial não se mexe
# quando a quebra a alcança, ela só ganha continuação — no mesmo passo
# irregular — até as duas pontas
_PERFIL_CHEIO = ((0.00, 0.0), (0.05, 0.85), (0.11, -0.45), (0.17, 0.6),
                 (0.23, -0.8),
                 (0.30, 0.0), (0.36, -0.9), (0.42, 0.5), (0.47, -0.35),
                 (0.52, 1.0), (0.57, -0.5), (0.62, 0.0),
                 (0.68, 0.75), (0.74, -0.6), (0.80, 0.4), (0.87, -0.85),
                 (0.94, 0.55), (1.00, 0.0))


def _fissura(arco, centro, amp, perfil):
    """Pontos de uma fissura que CORRE pelo arco: cada (t, d) do perfil é um
    ponto a `d * amp` do traço, na direção radial (nunca na vertical)."""
    pontos = []
    for t, d in perfil:
        p = arco.point_from_proportion(t)
        radial = (p - centro) / np.linalg.norm(p - centro)
        pontos.append(p + d * amp * radial)
    return pontos


def quebrar(cena, cad, run_time=1.4):
    """A quebra que o `rachar()` promete (V4N01). Recebe um `cad` que JÁ
    passou pelo `rachar()` e carrega a rachadura parcial: a fissura termina
    de correr até as duas pontas do arco, o arco estala em dois pedaços na
    altura dela e os dois caem, girando e apagando.

    O corpo NÃO cai — fica em cena com o rótulo gravado, que é o ponto: a
    aposta é que quebra, não o número. Devolve VGroup(pedaço de fora, pedaço
    de dentro), porque o V4N03 os remonta; os dois ficam em cena, no fundo e
    invisíveis, onde caíram — para trazê-los de volta basta `set_opacity(1)`
    (e um `bring_to_front` se tiverem de passar por cima de alguma coisa).

    Depois desta chamada o cadeado não tem mais arco (`cad[0]` fica só com
    os dois cotos): `abrir()` e `fechar()` não valem mais para ele."""
    arco = cad[0][0]  # o Arc, não as pernas
    centro = arco.get_arc_center()
    raio = float(np.linalg.norm(arco.point_from_proportion(0.5) - centro))
    amp = 0.07 * raio          # a mesma do rachar(): proporcional ao raio,
                               # para colar no traço em qualquer escala
    rachadura = cad[3] if len(cad) > 3 else None

    # a fissura termina de correr: cada extensão nasce na ponta da rachadura
    # parada e vai até a ponta do arco (por isso a esquerda vai invertida —
    # o Create tem de partir de onde o vídeo 3 parou)
    esq = _fissura(arco, centro, amp,
                   tuple(reversed([p for p in _PERFIL_CHEIO if p[0] <= 0.30])))
    dta = _fissura(arco, centro, amp,
                   [p for p in _PERFIL_CHEIO if p[0] >= 0.62])
    corridas = VGroup()
    for pontos in (esq, dta):
        t = VMobject(stroke_color=CINZA, stroke_width=3)
        t.set_points_as_corners(pontos)
        corridas.add(t)
    cena.play(*[Create(t) for t in corridas], run_time=0.45 * run_time * VEL)

    # o arco estala: os dois pedaços são os dois lados da fissura, cada um
    # com metade da espessura do traço
    pecas = VGroup()
    for lado in (0.5, -0.5):       # meia amplitude para cada lado da fissura:
                                   # juntos, os dois cobrem o traço de origem
        pontos = _fissura(arco, centro, amp,
                          [(t, d + lado) for t, d in _PERFIL_CHEIO])
        peca = VMobject(stroke_color=PRETO, stroke_width=5)
        peca.set_points_as_corners(pontos)
        pecas.add(peca)
    # a rachadura e as corridas saem tanto do cad quanto da cena: o Create
    # as pendurou no topo da cena, tirar só do VGroup deixaria o rabisco lá
    cad[0].remove(arco)
    cena.remove(arco, *corridas)
    if rachadura is not None:
        cad.remove(rachadura)
        cena.remove(rachadura)
    cena.add(pecas)
    cena.bring_to_back(pecas)  # os cacos caem ATRÁS do corpo, senão passam
                               # riscando por cima do rótulo

    # o estalo: os dois lados se apartam um dedo, ainda inteiros e opacos
    fora, dentro = pecas
    cena.play(fora.animate.shift(0.22 * raio * UP),
              dentro.animate.shift(0.22 * raio * DOWN),
              run_time=0.15 * run_time * VEL)
    cena.play(
        fora.animate.shift(4.5 * raio * DOWN + 1.6 * raio * RIGHT)
            .rotate(-70 * DEGREES).set_opacity(0),
        dentro.animate.shift(4.5 * raio * DOWN + 1.6 * raio * LEFT)
            .rotate(55 * DEGREES).set_opacity(0),
        run_time=0.40 * run_time * VEL)
    return pecas


def rede(n=7, semente=0):
    """A rede de cadeados anônimos do V1N03, que volta intacta no V4N03:
    pontos e arestas cinzas com um `cadeado()` de corpo vazio pousado em
    cada aresta, tudo apagado em opacidade 0,3.

    Determinística — o jitter sai de um gerador com `semente` fixa, então
    dois renders dão exatamente a mesma rede. O miolo fica livre: é lá que
    mora o cadeado aceso. Devolve VGroup(arestas, pontos, cadeados)."""
    rng = np.random.default_rng(semente)
    pos = []
    for i in range(n):
        ang = 2 * PI * i / n + float(rng.uniform(-0.18, 0.18))
        r = 2.55 + float(rng.uniform(-0.35, 0.35))
        pos.append(np.array([1.5 * r * np.cos(ang), r * np.sin(ang), 0.0]))

    # o anel, mais cordas de dois em dois: nenhuma passa perto do centro
    ligacoes = [(i, (i + 1) % n) for i in range(n)]
    ligacoes += [(i, (i + 2) % n) for i in range(0, n, 3)]

    arestas = VGroup(*[Line(pos[i], pos[j], color=CINZA, stroke_width=2.5)
                       for i, j in ligacoes])
    pontos = VGroup(*[Dot(p, radius=0.07, color=CINZA) for p in pos])

    cads = VGroup()
    for a in arestas:
        c = cadeado()
        c.remove(c[2])                      # corpo vazio: sem buraco, sem letras
        c.scale(0.22).move_to(a.get_center())
        c.shift(0.30 * c.height * DOWN)     # pendurado pelo arco na aresta
        cads.add(c)

    grupo = VGroup(arestas, pontos, cads)
    grupo.set_opacity(0.3)
    return grupo


def abrir(cena, cad, run_time=0.7):
    """Abre o arco — inverso de `fechar`, sem flash (abrir é silencioso)."""
    pivot = cad[0][2].get_bottom()
    cena.play(Rotate(cad[0], _ABERTURA, about_point=pivot),
              run_time=run_time * VEL)


def fechar(cena, cad, run_time=0.6):
    """Fecha o arco com o flash seco do V1N01 — chamar quando `cad`
    estiver aberto (por `abrir()` ou por `cadeado("aberto")`)."""
    pivot = cad[0][2].get_bottom()
    cena.play(Rotate(cad[0], -_ABERTURA, about_point=pivot),
              Flash(cad[1].get_top(), color=PRETO, flash_radius=0.55,
                    line_length=0.22),
              run_time=run_time * VEL)
