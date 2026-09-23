# -*- coding: utf-8 -*-
"""Vídeo 1 — Introdução: o vídeo inteiro mora aqui
(roteiro_video1_introducao.md). Não há capítulo por trás dele."""

from manim import *
import numpy as np

from ..paleta import CINZA, LARANJA, PRETO, VEL
from ..ferramentas import T, narra
from ..cadeado import cadeado, fechar
from .comum import VIDEOS

# o gancho do V1N00, já quebrado nas três linhas em que ele nasce
_GANCHO = ("Existe uma aposta que protege quase tudo",
           "que você faz na internet, e ela não é",
           "uma senha forte que você possa escolher.")

# a faixa da operação de mão única (V1N01), abaixo do cadeado
_FAIXA = -2.3

# para onde cada "?" do despedaçar se espalha, a partir do seu lugar na
# seta de volta — fixo, para dois renders darem o mesmo quadro (o V1N02
# e o V1N04 contam com as interrogações onde elas pararam)
_ESPALHA = ((-0.7, 0.95, 18), (-0.35, -0.85, -12), (0.15, 1.15, 8),
            (0.3, -0.7, 22), (-0.1, 0.8, -20), (0.55, -1.0, -6),
            (0.8, 0.9, 14))


def _frase(linhas, tamanho=40):
    """As linhas centradas, cada uma um Text inteiro (a tipografia não
    pula), e a lista das palavras recortadas dos glifos de cada linha — o
    Text não tem glifo para espaço, então cada palavra é uma fatia."""
    textos = VGroup(*[T(l, tamanho) for l in linhas]).arrange(DOWN, buff=0.35)
    palavras = []
    for txt, linha in zip(textos, linhas):
        i = 0
        for p in linha.split():
            palavras.append(txt[i:i + len(p)])
            i += len(p)
        assert i == len(txt), f"glifos não batem com as letras: {linha!r}"
    return textos, palavras


def _no_mesmo_play(cena, anims, fn, *args, **kw):
    """Roda `fn(cena, *args)` — uma função do cadeado.py que faz UM
    cena.play, como o fechar() — com `anims` somadas àquele mesmo play.

    É o "no mesmo instante" do V1N01: a fusão acontece no quadro do
    travamento, e o travamento continua sendo o fechar() de verdade, com o
    flash seco dele, sem copiar o Rotate para cá nem editar o cadeado.py.
    O play original volta no primeiro uso."""
    def junto(*a, **k):
        cena.__dict__.pop("play", None)
        cena.play(*a, *anims, **k)
    cena.play = junto
    try:
        fn(cena, *args, **kw)
    finally:
        cena.__dict__.pop("play", None)


def abertura(cena):
    """V1N00, o cartão silencioso e V1N01. O vídeo abre FALANDO: o gancho
    vem primeiro, a marca vem depois.

    Devolve (cad, bloco, interrogacoes), todos ainda em cena — o V1N02
    nasce em cima das interrogações e reabre o bloco, então nada disto
    sai aqui."""
    # --- V1N00: a frase nasce palavra por palavra; "aposta" pisca -------
    _, palavras = _frase(_GANCHO)
    aposta = palavras[2]
    with narra(cena, "V1N00", 9.6):
        cena.play(LaggedStart(*[Write(w) for w in palavras[:3]],
                              lag_ratio=0.6), run_time=1.2 * VEL)
        # a frase segue no mesmo ritmo enquanto "aposta" pisca uma vez
        cena.play(Indicate(aposta, color=LARANJA, scale_factor=1.08,
                           run_time=1.0 * VEL),
                  LaggedStart(*[Write(w) for w in palavras[3:]],
                              lag_ratio=0.5, run_time=6.8 * VEL))
        # o resto esmaece; "aposta" sobrevive como rótulo aceso no canto
        cena.play(*[FadeOut(w) for w in palavras if w is not aposta],
                  aposta.animate.scale(0.7).set_color(LARANJA)
                        .to_corner(UL, buff=0.5),
                  run_time=1.1 * VEL)
    rotulo = aposta

    # --- cartão silencioso: o rótulo continua aceso no canto ------------
    t1 = T("Do Zero ao Algoritmo de Shor Quântico", 42)
    t2 = T(f"Vídeo 1 de 4 — {VIDEOS[0]}", 28, CINZA)
    VGroup(t1, t2).arrange(DOWN, buff=0.5)
    cena.play(Write(t1), run_time=1.1 * VEL)
    cena.play(FadeIn(t2, shift=0.25 * UP), run_time=0.8 * VEL)
    cena.wait(1.0 * VEL)
    cena.play(FadeOut(t1), FadeOut(t2), run_time=0.6 * VEL)

    # --- V1N01 -----------------------------------------------------------
    # o cadeado aberto, só o contorno: o corpo se enche depois, com o que
    # ele protege
    cad = cadeado("aberto")
    cad.shift([0, 0.9, 0] - cad[1].get_center())
    cad[1].set_fill(opacity=0)

    itens = VGroup(T("contas bancárias", 30), T("compras online", 30),
                   T("mensagens privadas", 30))
    itens[0].next_to(cad[1], LEFT, buff=1.2)
    itens[1].next_to(cad[1], RIGHT, buff=1.2)
    itens[2].next_to(cad[1], DOWN, buff=0.5)

    # os dois fatores cinzas e o bloco laranja em que eles se fundem. O
    # bloco são duas metades encostadas, sem traço entre elas: lê como um
    # só, mas o V1N02 pode reabri-lo e mostrar do que era feito
    f1 = Square(0.55).set_fill(CINZA, opacity=1).set_stroke(width=0)
    f2 = Square(0.8).set_fill(CINZA, opacity=1).set_stroke(width=0)
    f1.move_to([-4.3, _FAIXA, 0])
    f2.move_to([-3.35, _FAIXA, 0])
    bloco = VGroup(Rectangle(width=0.62, height=0.8),
                   Rectangle(width=0.92, height=0.8))
    bloco.arrange(RIGHT, buff=0).move_to([3.4, _FAIXA, 0])
    bloco.set_fill(LARANJA, opacity=1).set_stroke(LARANJA, width=1)

    ida = Arrow([-2.55, _FAIXA, 0], [2.4, _FAIXA, 0], buff=0, color=PRETO,
                stroke_width=5)
    volta = Arrow([2.4, _FAIXA, 0], [-2.55, _FAIXA, 0], buff=0, color=PRETO,
                  stroke_width=5)
    interrogacoes = VGroup(*[T("?", 36, CINZA) for _ in _ESPALHA])
    for q, x in zip(interrogacoes, np.linspace(2.2, -2.35, len(_ESPALHA))):
        q.move_to([x, _FAIXA, 0])

    with narra(cena, "V1N01", 14.2):
        # o rótulo desce para o centro, já da largura do corpo, e se abre
        # no contorno do cadeado letra a letra, por posição: "a p s" viram
        # o corpo, o "o" vira o buraco e o "ta" da direita sobe no arco,
        # que no cadeado aberto também fica à direita
        cena.play(rotulo.animate.scale_to_fit_width(cad[1].width)
                        .move_to(cad[1]), run_time=1.0 * VEL)
        a, p, o, s, t, a2 = rotulo
        cena.play(ReplacementTransform(VGroup(a, p, s), cad[1]),
                  ReplacementTransform(o, cad[2]),
                  ReplacementTransform(VGroup(t, a2), cad[0]),
                  run_time=1.0 * VEL)
        # as três peças entraram soltas; o cadeado volta a ser um só
        cena.remove(*cad)
        cena.add(cad)
        # contas, compras, mensagens: uma a cada respiro
        for it, d in zip(itens, (RIGHT, LEFT, UP)):
            cena.play(FadeIn(it, shift=0.3 * d), run_time=0.8 * VEL)
        # e se condensam dentro dele, que se enche de laranja
        cena.play(*[it.animate.scale(0.05).move_to(cad[1]).set_opacity(0)
                    for it in itens],
                  cad[1].animate.set_fill(LARANJA, opacity=1),
                  run_time=1.2 * VEL)
        cena.remove(*itens)

        # "operações": os dois fatores cinzas na faixa de baixo
        cena.play(FadeIn(f1, shift=0.2 * UP), FadeIn(f2, shift=0.2 * UP),
                  run_time=1.2 * VEL)
        # "fáceis de fazer numa direção": a seta varre para a direita...
        cena.play(GrowArrow(ida), run_time=1.6 * VEL)
        # ...e os fatores se fundem no bloco no instante em que o cadeado
        # trava — o play é o do próprio fechar()
        _no_mesmo_play(cena, [ReplacementTransform(f1, bloco[0]),
                              ReplacementTransform(f2, bloco[1]),
                              FadeOut(ida)],
                       fechar, cad)

        # "impraticáveis de desfazer": a volta tenta e se despedaça
        cena.play(GrowArrow(volta), run_time=1.0 * VEL)
        cena.play(ReplacementTransform(volta, interrogacoes),
                  run_time=0.6 * VEL)
        # as interrogações se espalham e o cadeado chacoalha sem abrir
        cena.play(*[q.animate.shift([dx, dy, 0]).rotate(ang * DEGREES)
                    for q, (dx, dy, ang) in zip(interrogacoes, _ESPALHA)],
                  Wiggle(cad), run_time=1.2 * VEL)

    return cad, bloco, interrogacoes
