# -*- coding: utf-8 -*-
from manim import *
import numpy as np

from ..paleta import *
from ..ferramentas import *

# ============================================================================
# CAPÍTULO 9 — Ordem Modular NA TABELA multiplicativa (slides 107–119)
#   Tabela mod 9, base a = 4: o zigue-zague verde 1 → 4 → 7 → 1 mostra
#   que multiplicar por a é saltar para a linha 4 na coluna do valor
#   atual. 3 passos para voltar ao 1 ⇒ r = 3.
# ============================================================================
def parte9(cena):
    # slide 108: tabela multiplicativa + exponenciação modular
    eq = VGroup(T("c", 34, VERDE), T("≡", 34, PRETO),
                pot("4", "b", VERMELHO, AZUL, 34), fmod("9", 32))
    eq.arrange(RIGHT, buff=0.15).to_edge(UP, buff=0.4)
    with narra(cena, "C9N01", 8.3):
        cena.play(Write(eq), run_time=1.0 * VEL)
    escolha = formula(("n", LARANJA), ("=", PRETO), ("9", LARANJA),
                      ("e", CINZA), ("a", VERMELHO), ("=", PRETO),
                      ("4", VERMELHO), ("inversível", CINZA),
                      tamanho=22, buff=0.12).move_to([3.6, 2.55, 0])
    with narra(cena, "C9N02", 9.6):
        cena.play(FadeIn(escolha), run_time=0.7 * VEL)
        # "tem inverso": a condição do capítulo 5 já está escrita ali
        cena.play(Indicate(escolha[7], color=VERMELHO), run_time=0.8 * VEL)

    # a tabela mod 9 (slide 109), com a seta vermelha na linha do 4
    tam = 0.52
    canto = np.array([-6.0, 2.2, 0.0])

    def ponto(i, j):
        return canto + np.array([(j + 1) * tam, -(i + 1) * tam, 0.0])

    head_c = VGroup(*[T(str(j), 22, AZUL).move_to(canto + [(j + 1) * tam, 0, 0])
                      for j in range(9)])
    head_l = VGroup(*[T(str(i), 22, VERMELHO)
                      .move_to(canto + [0, -(i + 1) * tam, 0])
                      for i in range(9)])
    lin_h = Line(canto + [0.55 * tam, -0.5 * tam, 0],
                 canto + [9.5 * tam, -0.5 * tam, 0], color=PRETO,
                 stroke_width=1.5)
    lin_v = Line(canto + [0.55 * tam, -0.5 * tam, 0],
                 canto + [0.55 * tam, -9.5 * tam, 0], color=PRETO,
                 stroke_width=1.5)
    linhas_cel = [VGroup(*[T(str((i * j) % 9), 22, PRETO).move_to(ponto(i, j))
                           for j in range(9)]) for i in range(9)]
    # a grade e o miolo num movimento só: a tabela entra como UMA peça
    with narra(cena, "C9N03", 6.7):
        cena.play(LaggedStart(
            AnimationGroup(FadeIn(head_c), FadeIn(head_l), Create(lin_h),
                           Create(lin_v), run_time=0.9 * VEL),
            LaggedStart(*[FadeIn(l) for l in linhas_cel], lag_ratio=0.1,
                        run_time=1.8 * VEL),
            lag_ratio=0.6))
    seta4 = Arrow(canto + [-1.05, -5 * tam, 0], canto + [-0.35, -5 * tam, 0],
                  buff=0, color=VERMELHO, stroke_width=5,
                  max_tip_length_to_length_ratio=0.4)
    with narra(cena, "C9N04", 3.8):
        cena.play(GrowArrow(seta4), Indicate(head_l[4], color=VERMELHO),
                  run_time=0.8 * VEL)

    # slide 110: objetivo — todos os restos c possíveis, um b de cada vez
    def circ(i, j):
        return Circle(radius=0.22, color=VERDE,
                      stroke_width=2.5).move_to(ponto(i, j))

    # b = 0: c = 1 (slide 111)
    f0 = VGroup(pot("4", "0", VERMELHO, AZUL, 26), T("≡", 26, PRETO),
                T("1", 26, VERDE), fmod("9", 24))
    f0.arrange(RIGHT, buff=0.12).move_to([3.6, 1.75, 0])
    c00 = circ(1, 1)
    with narra(cena, "C9N05", 4.2):
        cena.play(Create(c00), Write(f0), run_time=0.9 * VEL)

    # slide 112: somar 1 em b = multiplicar o resultado anterior por 4
    nota = T("somar 1 em b = multiplicar por 4", 20,
             CINZA).move_to([3.6, 1.2, 0])
    with narra(cena, "C9N06", 8.3):
        cena.play(FadeIn(nota), run_time=0.7 * VEL)

    # o ZIGUE-ZAGUE dos slides 113–115: descer para a linha 4 multiplica;
    # o resultado vira a coluna do próximo salto
    passos = [(1, 1, 4), (4, 1, None), (1, 4, 4), (4, 4, None),
              (1, 7, 4), (4, 7, None)]
    fs = [VGroup(pot("4", "1", VERMELHO, AZUL, 26), T("≡", 26, PRETO),
                 T("4", 26, VERDE), fmod("9", 24)),
          VGroup(pot("4", "2", VERMELHO, AZUL, 26), T("≡", 26, PRETO),
                 T("7", 26, VERDE), fmod("9", 24)),
          VGroup(pot("4", "3", VERMELHO, AZUL, 26), T("≡", 26, PRETO),
                 T("1", 26, VERDE), fmod("9", 24), T("✓", 26, VERDE))]
    for k, f in enumerate(fs):
        f.arrange(RIGHT, buff=0.12).move_to([3.6, 0.55 - 0.62 * k, 0])
    zig = VGroup(c00)
    trilha = VGroup()           # o caminho do ciclo, para as voltas extras

    def _passo(k):
        """Um degrau do zigue-zague: desce até a linha da base, escreve a
        potência e sobe de volta na coluna do resultado."""
        j = (1, 4, 7)[k]
        desce = Arrow(ponto(1, j) + 0.22 * DOWN, ponto(4, j) + 0.24 * UP,
                      buff=0, color=VERDE, stroke_width=2.5,
                      max_tip_length_to_length_ratio=0.18)
        alvo = circ(4, j)
        cena.play(GrowArrow(desce), Create(alvo), run_time=0.7 * VEL)
        cena.play(Write(fs[k]), run_time=0.7 * VEL)
        zig.add(desce, alvo)
        trilha.add(Line(ponto(1, j) + 0.22 * DOWN, ponto(4, j) + 0.24 * UP))
        if k < 2:
            prox_j = (4, 7)[k]
            sobe = ArcBetweenPoints(ponto(4, j) + 0.24 * RIGHT,
                                    ponto(1, prox_j) + 0.24 * DOWN,
                                    angle=-0.55, color=VERDE,
                                    stroke_width=2.0)
            topo = circ(1, prox_j)
            cena.play(Create(sobe), Create(topo), run_time=0.7 * VEL)
            zig.add(sobe, topo)
            trilha.add(sobe.copy())

    # os dois primeiros degraus inteiros sob uma fala só: o with envolve o
    # laço, não cada iteração dele
    with narra(cena, "C9N07", 7.5):
        for k in range(2):
            _passo(k)

    # o terceiro degrau é o que devolve o 1 — o Flash pertence a ele
    with narra(cena, "C9N08", 4.6):
        _passo(2)
        cena.play(Flash(ponto(4, 7), color=VERDE, flash_radius=0.5),
                  run_time=0.7 * VEL)

    # o CICLO SE FECHA: do 1 reencontrado, de volta ao ponto de partida
    fecha = ArcBetweenPoints(ponto(4, 7) + 0.24 * DOWN,
                             ponto(1, 1) + 0.26 * LEFT, angle=-1.3,
                             color=VERDE, stroke_width=2.0)
    with narra(cena, "C9N09", 5.8):
        cena.play(Create(fecha), Indicate(c00, color=VERDE),
                  run_time=1.0 * VEL)
    trilha.add(fecha.copy())
    zig.add(fecha)

    # slide 118: cada VOLTA COMPLETA no ciclo soma 3 ao expoente —
    # surgem 4⁶, 4⁹, … todos congruentes a 1
    mult = VGroup(T("1", 26, VERDE), T("≡", 26, PRETO),
                  pot("4", "3", VERMELHO, AZUL, 26), T("≡", 26, PRETO),
                  pot("4", "6", VERMELHO, AZUL, 26), T("≡", 26, PRETO),
                  pot("4", "9", VERMELHO, AZUL, 26), fmod("9", 24))
    mult.arrange(RIGHT, buff=0.12).move_to([3.6, -1.65, 0])
    with narra(cena, "C9N10", 5.0):
        cena.play(Write(VGroup(mult[0], mult[1], mult[2])), run_time=0.8 * VEL)

    def volta_no_ciclo():
        return Succession(*[ShowPassingFlash(
            s.copy().set_stroke(AMARELO, width=6), time_width=0.7)
            for s in trilha])

    # as duas voltas extras correm sob uma fala só — o "e assim por diante"
    with narra(cena, "C9N11", 5.4):
        cena.play(volta_no_ciclo(), run_time=1.3 * VEL)
        cena.play(FadeIn(mult[3]), TransformFromCopy(mult[2], mult[4]),
                  run_time=0.8 * VEL)
        cena.play(volta_no_ciclo(), run_time=1.3 * VEL)
        cena.play(FadeIn(mult[5]), TransformFromCopy(mult[4], mult[6]),
                  FadeIn(mult[7]), run_time=0.8 * VEL)

    # slides 116–117: 3 passos para fechar o ciclo ⇒ o r NASCE do expoente 3
    rdef = VGroup(T("r", 38, AMARELO), T("=", 38, PRETO),
                  T("3", 38, AMARELO))
    rdef.arrange(RIGHT, buff=0.16).move_to([3.6, -2.5, 0])
    with narra(cena, "C9N12", 3.3):
        cena.play(Write(rdef[0]), Write(rdef[1]),
                  TransformFromCopy(mult[2][1], rdef[2]), run_time=0.9 * VEL)

    # slide 117 (definição) + slide 119 (pior caso r = φ(n))
    d1 = formula(("ordem modular de", PRETO), ("a", VERMELHO),
                 ("módulo", PRETO), ("n", LARANJA), (":", PRETO),
                 tamanho=26, buff=0.14)
    d2 = formula(("o menor", PRETO), ("r", AMARELO), ("tal que", PRETO),
                 tamanho=24, buff=0.14)
    d3 = VGroup(pot("a", "r", VERMELHO, AMARELO, 30), T("≡", 30, PRETO),
                T("1", 30, VERDE), fmod("n", 28))
    d3.arrange(RIGHT, buff=0.15)
    d4 = formula(("pior caso:", CINZA), ("r", AMARELO), ("=", CINZA),
                 ("φ(", CINZA), ("n", LARANJA), (")", CINZA),
                 tamanho=20, buff=0.08)
    caixa_d = VGroup(d1, d2, d3, d4).arrange(DOWN, buff=0.24)
    # sem a tabela e sem a coluna do exemplo, a definição não divide mais a
    # tela com ninguém: ela nasce no centro
    caixa_d.move_to(ORIGIN)
    # a borda já abraça o d4, que só entra no C9N14 — assim o layout não se
    # mexe quando o pior caso chegar
    borda = SurroundingRectangle(caixa_d, color=VERDE, buff=0.25,
                                 corner_radius=0.12)

    # A VIRADA, o mesmo pouso do C6N12 e do C7N13: a tabela e a coluna do
    # exemplo saem enquanto o geral nasce, num play único. O rdef é a última
    # coisa a sumir — e o r dele não morre: viaja por cópia para os dois
    # lugares onde a definição o usa, o d2 e o expoente do d3
    corpo = VGroup(d1, d2[0], d2[2], d3[0][0], d3[1], d3[2], d3[3])
    saida = AnimationGroup(
        FadeOut(head_c), FadeOut(head_l), FadeOut(lin_h), FadeOut(lin_v),
        *[FadeOut(l) for l in linhas_cel], FadeOut(seta4), FadeOut(zig),
        FadeOut(eq), FadeOut(escolha), FadeOut(f0), FadeOut(nota),
        *[FadeOut(f) for f in fs], FadeOut(mult),
        Write(corpo), Create(borda),
        TransformFromCopy(rdef[0], d2[1]),
        TransformFromCopy(rdef[0], d3[0][1]),
        run_time=1.2 * VEL,
    )
    with narra(cena, "C9N13", 3.3):
        cena.play(LaggedStart(saida, FadeOut(rdef, run_time=0.6 * VEL),
                              lag_ratio=0.4))

    # o pior caso tem tempo próprio: é a fala mais longa do capítulo
    with narra(cena, "C9N14", 12.6):
        cena.play(Write(d4), run_time=1.0 * VEL)
        # "a contagem de Euler": a peça que o capítulo 7 definiu e o 8 gastou
        cena.play(Indicate(VGroup(d4[3], d4[4], d4[5]), color=LARANJA),
                  run_time=0.9 * VEL)

    # a caixa fica parada em cena; só o r pisca, porque é o que o capítulo
    # seguinte vem cobrar
    with narra(cena, "C9N15", 9.6):
        cena.play(Indicate(d3[0][1], color=AMARELO), run_time=0.9 * VEL)
