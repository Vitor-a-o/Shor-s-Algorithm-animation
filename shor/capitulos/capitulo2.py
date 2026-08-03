# -*- coding: utf-8 -*-
from manim import *
import numpy as np

from ..paleta import *
from ..ferramentas import *

# ============================================================================
# CAPÍTULO 2 — Adição modular (slides 10–17): 6 + 5 (mod 7), com o x amarelo
#   Fiel aos slides: a linha de baixo (c verde + n laranja) aparece LOGO,
#   com o rótulo "c" desconhecido; o algoritmo roda e só então c vira 4.
#   Narração: C2N01 … C2N11 (roteiro_video2_aritmetica_modular.md)
# ============================================================================
def parte2(cena):
    eq = formula(("c", VERDE), ("≡", PRETO), ("6", VERMELHO), ("+", PRETO),
             ("5", AZUL), *MOD("7"), tamanho=38).to_edge(UP, buff=0.55)
    reta = NumberLine(x_range=[0, 14, 1], length=11, color=CINZA,
                      include_ticks=True, tick_size=0.06).shift(2.45 * DOWN)
    n2 = reta.n2p
    with narra(cena, "C2N01", 9.6):
        cena.play(Write(eq), run_time=1.0 * VEL)
        cena.play(Create(reta), run_time=0.7 * VEL)

    def teste(xv, ok):
        """O teste dos slides 14–16 já resolvido: "2 > 6 ✗" (ou "7 > 6 ✓")."""
        return formula((xv, AMARELO), (">", PRETO), ("6", VERMELHO),
                       ("✓" if ok else "✗", VERDE if ok else VERMELHO),
                       tamanho=28).move_to([0, 0.62, 0])

    # linha de cima: b = 6 (vermelho) e a = 5 (azul), como no slide 11
    b6 = traco(n2(0) + 2.1 * UP, n2(6) + 2.1 * UP, VERMELHO)
    r6 = T("6", 26, VERMELHO).next_to(b6, UP, buff=0.10)
    a5 = traco(n2(6) + 2.1 * UP, n2(11) + 2.1 * UP, AZUL)
    r5 = T("5", 26, AZUL).next_to(a5, UP, buff=0.10)
    # a linha de BAIXO (slide 11): o bloco n = 7 cresce da DIREITA para a
    # ESQUERDA; quando a ponta alcança o início da reta vermelha (x = 6),
    # o x amarelo começa a crescer JUNTO — o x é o pedaço de n que passa de a
    cver = traco(n2(0) + 0.95 * UP, n2(4) + 0.95 * UP, VERDE)
    rc = T("c", 24, VERDE).next_to(cver, DOWN, buff=0.10)
    n7 = traco(n2(11) + 0.95 * UP, n2(4) + 0.95 * UP, LARANJA)
    rn = T("7", 24, LARANJA).next_to(n7, DOWN, buff=0.10)
    x2 = traco(n2(6) + 1.5 * UP, n2(4) + 1.5 * UP, AMARELO)
    # o rótulo do x fica à DIREITA: essa ponta nunca sai do lugar (x = 6),
    # então ele não persegue a barra nem escapa da tela quando o x cresce
    rx = T("x", 22, AMARELO).next_to(x2, RIGHT, buff=0.12)
    # tudo emendado, sem pausa: parcelas, módulo medido (com o x nascendo
    # quando a ponta cruza o x = 6 — razão 5/7 do Wait mantida), rótulos e c
    with narra(cena, "C2N02", 5.0):
        cena.play(Create(b6), FadeIn(r6), run_time=0.5 * VEL)
        cena.play(Create(a5), FadeIn(r5), run_time=0.5 * VEL)
        cena.play(AnimationGroup(
            Create(n7, run_time=2.1 * VEL, rate_func=linear),
            Succession(Wait(1.5 * VEL),
                       Create(x2, run_time=0.6 * VEL, rate_func=linear))))
        cena.play(FadeIn(rn), FadeIn(rx), run_time=0.5 * VEL)
        cena.play(Create(cver), FadeIn(rc), run_time=0.7 * VEL)

    # o algoritmo (slides 12–13): x = n − a; a conta vira 7 − 5 e o
    # resultado "= 2" é ADICIONADO, mantendo as duas igualdades à vista
    exf = formula(("x", AMARELO), ("=", PRETO), ("7", LARANJA), ("−", PRETO),
                  ("5", AZUL), ("=", PRETO), ("2", AMARELO),
                  tamanho=32).move_to([-3.0, 1.5, 0])
    ex0 = formula(("x", AMARELO), ("=", PRETO), ("n", LARANJA), ("−", PRETO),
                  ("a", AZUL), tamanho=32)
    for j in range(5):
        ex0[j].move_to(exf[j])
    rx2 = T("2", 22, AMARELO).move_to(rx)
    with narra(cena, "C2N03", 7.9):
        cena.play(Write(ex0), run_time=0.9 * VEL)
        cena.play(ReplacementTransform(VGroup(*ex0[2:]), VGroup(*exf[2:5])),
                  run_time=0.8 * VEL)
        cena.play(FadeIn(exf[5]), FadeIn(exf[6], scale=1.3),
                  run_time=0.7 * VEL)
        # o rótulo do traço amarelo revela o valor: x = 2
        cena.play(Flash(x2.get_center(), color=AMARELO, flash_radius=0.4),
                  ReplacementTransform(rx, rx2), run_time=0.8 * VEL)
    ex = VGroup(ex0[0], ex0[1], *exf[2:])   # x = 7 − 5 = 2 (visível)

    # o TESTE dos slides 14–16: "x > b ?" — enquanto o x não passa do b,
    # ainda sobra pedaço do b e o resto é c = b − x
    tst0 = formula(("x", AMARELO), (">", PRETO), ("b", VERMELHO),
                   ("?", PRETO), tamanho=28)
    tst = teste("2", False)
    for j in range(4):
        tst0[j].move_to(tst[j])
    with narra(cena, "C2N04", 9.6):
        cena.play(Write(tst0), run_time=0.7 * VEL)
        cena.play(ReplacementTransform(VGroup(*tst0[:3]), VGroup(*tst[:3])),
                  run_time=0.6 * VEL)
        cena.play(FadeOut(tst0[3], scale=0.5), FadeIn(tst[3], scale=1.4),
                  run_time=0.5 * VEL)

    # deu ✗  →  c = b − x, na mesma sequência do x
    t2f = formula(("c", VERDE), ("=", PRETO), ("6", VERMELHO), ("−", PRETO),
                  ("2", AMARELO), ("=", PRETO), ("4", VERDE),
                  tamanho=30).move_to([3.0, 1.5, 0])
    t2s = formula(("c", VERDE), ("=", PRETO), ("b", VERMELHO), ("−", PRETO),
                  ("x", AMARELO), tamanho=30)
    for j in range(5):
        t2s[j].move_to(t2f[j])
    rc4 = T("4", 24, VERDE).move_to(rc)
    with narra(cena, "C2N05", 5.0):
        cena.play(Write(t2s), run_time=0.8 * VEL)
        cena.play(ReplacementTransform(VGroup(*t2s[2:]), VGroup(*t2f[2:5])),
                  run_time=0.8 * VEL)
        cena.play(FadeIn(t2f[5]), FadeIn(t2f[6], scale=1.3),
                  run_time=0.7 * VEL)
        # o c foi DESCOBERTO: o rótulo "c" da reta vira "4" (slide 17)
        cena.play(Flash(cver.get_center(), color=VERDE, flash_radius=0.5),
                  ReplacementTransform(rc, rc4), run_time=0.9 * VEL)
    t2 = VGroup(t2s[0], t2s[1], *t2f[2:])   # c = 6 − 2 = 4 (visível)

    # a equação do topo se completa: c vira 4
    eq2 = formula(("4", VERDE), ("≡", PRETO), ("6", VERMELHO), ("+", PRETO),
                  ("5", AZUL), *MOD("7"), tamanho=38).move_to(eq)
    with narra(cena, "C2N06", 7.1):
        cena.play(ReplacementTransform(eq, eq2), run_time=1.0 * VEL)

    # ---------- e se n CRESCER? o x cresce junto, até passar do b ----------
    # (estado atual: barras b6/a5, x2 [4,6], n7 [4,11], cver [0,4])
    def estado(n):
        """Reconstrói barras, rótulos e fórmulas para o módulo n (n ≤ 11)."""
        xv, cv = n - 5, 11 - n
        bn = traco(n2(11) + 0.95 * UP, n2(11 - n) + 0.95 * UP, LARANJA)
        bx = traco(n2(6) + 1.5 * UP, n2(11 - n) + 1.5 * UP, AMARELO)
        # com n = 11 não sobra NADA: o traço vira um ponto em cima do zero
        bc = (Dot(n2(0) + 0.95 * UP, radius=0.06, color=VERDE) if cv == 0
              else traco(n2(0) + 0.95 * UP, n2(11 - n) + 0.95 * UP, VERDE))
        ln = T(str(n), 24, LARANJA).next_to(bn, DOWN, buff=0.10)
        lx = T(str(xv), 22, AMARELO).next_to(bx, RIGHT, buff=0.12)
        lc = T(str(cv), 24, VERDE).next_to(bc, DOWN, buff=0.10)
        fx = formula(("x", AMARELO), ("=", PRETO), (str(n), LARANJA),
                     ("−", PRETO), ("5", AZUL), ("=", PRETO),
                     (str(xv), AMARELO), tamanho=32).move_to(exf)
        f2 = formula(("c", VERDE), ("=", PRETO), ("6", VERMELHO),
                     ("−", PRETO), (str(xv), AMARELO), ("=", PRETO),
                     (str(cv), VERDE), tamanho=30).move_to(t2f)
        fq = formula((str(cv), VERDE), ("≡", PRETO), ("6", VERMELHO),
                     ("+", PRETO), ("5", AZUL), *MOD(str(n)),
                     tamanho=38).move_to(eq2)
        return VGroup(bn, bx, bc, ln, lx, lc, fx, f2, fq, teste(str(xv), False))

    #        0    1   2     3   4    5    6   7   8    9
    atual = VGroup(n7, x2, cver, rn, rx2, rc4, ex, t2, eq2, tst)
    # a narração nova cobre o laço inteiro com uma fala só: os quatro
    # ReplacementTransform correm num bloco só, sem pausa entre eles
    with narra(cena, "C2N07", 10.0):
        for n in (8, 9, 10, 11):
            novo = estado(n)
            cena.play(*[ReplacementTransform(a, b)
                        for a, b in zip(atual, novo)], run_time=1.0 * VEL)
            atual = novo

    # n = 12: o x PASSA do b — o teste finalmente dá ✓ e não sobra mais nada
    # do b para tirar, então a volta não acontece
    bn12 = traco(n2(11) + 0.95 * UP, n2(-1) + 0.95 * UP, LARANJA)
    bx12 = traco(n2(6) + 1.5 * UP, n2(-1) + 1.5 * UP, AMARELO)
    ln12 = T("12", 24, LARANJA).next_to(bn12, DOWN, buff=0.10)
    lx12 = T("7", 22, AMARELO).next_to(bx12, RIGHT, buff=0.12)
    fx12 = formula(("x", AMARELO), ("=", PRETO), ("12", LARANJA),
                   ("−", PRETO), ("5", AZUL), ("=", PRETO), ("7", AMARELO),
                   tamanho=32).move_to(exf)
    tst12 = teste("7", True)
    # o módulo mudou: o topo volta a ter o c DESCONHECIDO (mod 12)
    eqc = formula(("c", VERDE), ("≡", PRETO), ("6", VERMELHO), ("+", PRETO),
                  ("5", AZUL), *MOD("12"), tamanho=38).move_to(eq2)
    with narra(cena, "C2N08", 6.7):
        cena.play(ReplacementTransform(atual[0], bn12),
                  ReplacementTransform(atual[1], bx12),
                  ReplacementTransform(atual[3], ln12),
                  ReplacementTransform(atual[4], lx12),
                  ReplacementTransform(atual[6], fx12),
                  ReplacementTransform(atual[8], eqc),
                  ReplacementTransform(atual[9], tst12),
                  # o c antigo e a regra c = b − x deixam de valer: somem
                  FadeOut(atual[2]), FadeOut(atual[5]), FadeOut(atual[7]),
                  run_time=1.0 * VEL)
        cena.play(Flash(tst12[3].get_center(), color=VERDE, flash_radius=0.35),
                  Indicate(tst12[3], color=VERDE, scale_factor=1.4),
                  run_time=0.7 * VEL)

    # sem dar a volta, o resto é a própria soma: c = a + b — e a reta verde
    # NASCE do vermelho + azul, um degrau abaixo, para caber inteira
    f2ab = formula(("c", VERDE), ("=", PRETO), ("a", AZUL), ("+", PRETO),
                   ("b", VERMELHO), tamanho=30).move_to(t2f)
    bc12 = traco(n2(0) + 0.42 * UP, n2(11) + 0.42 * UP, VERDE)
    lc12 = T("c", 24, VERDE).next_to(bc12, RIGHT, buff=0.15)
    f2n = formula(("c", VERDE), ("=", PRETO), ("6", VERMELHO), ("+", PRETO),
                  ("5", AZUL), ("=", PRETO), ("11", VERDE),
                  tamanho=30).move_to(t2f)
    with narra(cena, "C2N09", 9.6):
        cena.play(Write(f2ab), run_time=0.8 * VEL)
        cena.play(TransformFromCopy(VGroup(b6, a5), bc12), FadeIn(lc12),
                  run_time=0.9 * VEL)
        cena.play(ReplacementTransform(f2ab, f2n), run_time=0.8 * VEL)

    # a reta e a equação confirmam: c = 11
    lc11 = T("11", 24, VERDE).move_to(lc12)
    eq12 = formula(("11", VERDE), ("≡", PRETO), ("6", VERMELHO), ("+", PRETO),
                   ("5", AZUL), *MOD("12"), tamanho=38).move_to(eq2)
    with narra(cena, "C2N10", 10.4):
        cena.play(Flash(bc12.get_center(), color=VERDE, flash_radius=0.5),
                  ReplacementTransform(lc12, lc11),
                  ReplacementTransform(eqc, eq12), run_time=1.0 * VEL)
    so_fala(cena, "C2N11", 4.2)
