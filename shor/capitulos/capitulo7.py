# -*- coding: utf-8 -*-
from manim import *
import numpy as np

from ..paleta import *
from ..ferramentas import *

# ============================================================================
# CAPÍTULO 7 — Euler NA TABELA mod 9 (slides 67–81): o cancelamento proibido
# ============================================================================
def parte7(cena):
    # tabela 8×8 dos resíduos de 9
    tam = 0.5
    canto = np.array([-6.1, 2.35, 0.0])

    def ponto(i, j):
        return canto + np.array([j * tam, -i * tam, 0.0])

    head_c = VGroup(*[T(str(j), 22, AZUL).move_to(ponto(0, j))
                      for j in range(1, 9)])
    head_l = VGroup(*[T(str(i), 22, VERMELHO).move_to(ponto(i, 0))
                      for i in range(1, 9)])
    lin_h = Line(canto + [0.5 * tam, -0.5 * tam, 0],
                 canto + [8.45 * tam, -0.5 * tam, 0], color=PRETO,
                 stroke_width=1.5)
    lin_v = Line(canto + [0.5 * tam, -0.5 * tam, 0],
                 canto + [0.5 * tam, -8.45 * tam, 0], color=PRETO,
                 stroke_width=1.5)
    cena.play(FadeIn(head_c), FadeIn(head_l), Create(lin_h), Create(lin_v),
              run_time=0.9 * VEL)
    linhas_cel = [VGroup(*[T(str((i * j) % 9), 22, PRETO).move_to(ponto(i, j))
                           for j in range(1, 9)]) for i in range(1, 9)]
    cena.play(LaggedStart(*[FadeIn(l) for l in linhas_cel], lag_ratio=0.1),
              run_time=1.8 * VEL)

    # elipse vermelha na linha 2 (slide 68): tentamos o truque de Fermat
    el2 = Ellipse(width=8 * tam + 0.5, height=0.5, color=VERMELHO,
                  stroke_width=2.5).move_to(canto + [4.5 * tam, -2 * tam, 0])
    cena.play(Create(el2), Indicate(head_l[1], color=VERMELHO),
              run_time=0.8 * VEL)

    # a equação da tentativa — com 3 e 6 em ROXO (slide 70)
    esq = formula(("2⁸", VERMELHO), ("· (1·2·", PRETO), ("3", ROXO),
                  ("·4·5·", PRETO), ("6", ROXO), ("·7·8)", PRETO),
                  tamanho=24, buff=0.06)
    dir_ = formula(("(1·2·", PRETO), ("3", ROXO), ("·4·5·", PRETO),
                   ("6", ROXO), ("·7·8)", PRETO), *MOD("9"),
                   tamanho=24, buff=0.06)
    eq = VGroup(esq, T("≡", 26, PRETO), dir_)
    eq.arrange(RIGHT, buff=0.2).move_to([0, -2.35, 0])
    cena.play(Write(eq), run_time=1.4 * VEL)

    # tentativa: DIVIDIR os dois lados pela mesma multiplicação
    ge = VGroup(*esq[1:])
    gd = VGroup(*dir_[:5])
    div_e = formula(("÷", VERMELHO), ("(1·2·", PRETO), ("3", ROXO),
                    ("·4·5·", PRETO), ("6", ROXO), ("·7·8)", PRETO),
                    tamanho=20, buff=0.05).next_to(ge, DOWN, buff=0.2)
    div_d = formula(("÷", VERMELHO), ("(1·2·", PRETO), ("3", ROXO),
                    ("·4·5·", PRETO), ("6", ROXO), ("·7·8)", PRETO),
                    tamanho=20, buff=0.05).next_to(gd, DOWN, buff=0.2)
    cena.play(Write(div_e), Write(div_d), run_time=1.0 * VEL)

    # POR QUE a divisão é proibida: dividir por um fator é MULTIPLICAR
    # pelo inverso dele — e 1/3 e 1/6 NÃO EXISTEM módulo 9
    exp1 = T("dividir = multiplicar pelo inverso", 22,
             PRETO).move_to([3.7, 1.75, 0])
    exp2 = formula(("1/", PRETO), ("3", ROXO), ("e", PRETO), ("1/", PRETO),
                   ("6", ROXO), ("não existem", VERMELHO), *MOD("9"),
                   tamanho=22, buff=0.08).move_to([3.7, 1.2, 0])
    cena.play(FadeIn(exp1), run_time=0.8 * VEL)
    cena.play(Write(exp2), run_time=1.0 * VEL)

    # RESSALTA os inversos que não existem: os 3 e 6 roxos pulsam,
    # as linhas 3 e 6 da tabela apagam — a divisão é NEGADA
    cena.play(*[linhas_cel[i].animate.set_opacity(0.2) for i in (2, 5)],
              *[head_l[i].animate.set_opacity(0.3) for i in (2, 5)],
              Indicate(div_e[2], color=ROXO), Indicate(div_e[4], color=ROXO),
              Indicate(div_d[2], color=ROXO), Indicate(div_d[4], color=ROXO),
              Indicate(exp2[5], color=VERMELHO),
              run_time=1.4 * VEL)
    neq = T("≢", 30, VERMELHO).move_to(eq[1])
    cena.play(Wiggle(div_e), Wiggle(div_d), run_time=0.9 * VEL)
    cena.play(FadeOut(div_e), FadeOut(div_d), Transform(eq[1], neq),
              run_time=0.8 * VEL)
    cena.wait(0.9 * VEL)

    # Euler: RETIRA os inversos que não existem — cruzes riscam o 3 e o 6
    # na equação e no topo da tabela → φ(9) = 6 sobreviventes
    cruzes = VGroup(Cross(head_c[2], stroke_color=VERMELHO, stroke_width=4),
                    Cross(head_c[5], stroke_color=VERMELHO, stroke_width=4))
    cruzes_eq = VGroup(*[Cross(m, stroke_color=VERMELHO, stroke_width=3.5)
                         for m in (esq[2], esq[4], dir_[1], dir_[3])])
    sobr = T("{1, 2, 4, 5, 7, 8}", 26, VERDE).move_to([3.6, 1.5, 0])
    phi = formula(("φ(", PRETO), ("9", LARANJA), (") = 6", PRETO),
                  tamanho=28, buff=0.06).move_to([3.6, 0.9, 0])
    cena.play(FadeOut(exp1), FadeOut(exp2),
              Create(cruzes), Create(cruzes_eq), FadeIn(sobr), Write(phi),
              run_time=1.2 * VEL)
    cena.wait(0.6 * VEL)

    # a equação REFEITA só com inversíveis — agora a divisão é permitida
    esq2 = formula(("2⁶", VERMELHO), ("· (1·2·4·5·7·8)", PRETO),
                   tamanho=24, buff=0.10)
    dir2 = formula(("(1·2·4·5·7·8)", PRETO), *MOD("9"),
                   tamanho=24, buff=0.10)
    eq2 = VGroup(esq2, T("≡", 26, PRETO), dir2)
    eq2.arrange(RIGHT, buff=0.2).move_to(eq)
    cena.play(ReplacementTransform(eq, eq2), FadeOut(cruzes_eq),
              run_time=1.1 * VEL)
    div2_e = formula(("÷", VERDE), ("(1·2·4·5·7·8)", PRETO),
                     tamanho=20, buff=0.05).next_to(esq2[1], DOWN, buff=0.2)
    div2_d = formula(("÷", VERDE), ("(1·2·4·5·7·8)", PRETO),
                     tamanho=20, buff=0.05).next_to(dir2[0], DOWN, buff=0.2)
    cena.play(Write(div2_e), Write(div2_d), run_time=0.8 * VEL)
    res = formula(("2⁶", VERMELHO), ("≡", PRETO), ("1", VERDE),
                  *MOD("9"), tamanho=32).move_to(eq2)
    cena.play(ReplacementTransform(VGroup(eq2, div2_e, div2_d), res),
              run_time=1.1 * VEL)

    geral = VGroup(pot("a", expoente(("φ(", PRETO), ("n", LARANJA),
                                     (")", PRETO), tam=28), ROXO, tam=28),
                   T("≡", 28, PRETO), T("1", 28, VERDE), fmod("n", 26))
    geral.arrange(RIGHT, buff=0.16).move_to([0, -3.35, 0])
    caixa = SurroundingRectangle(geral, color=VERDE, buff=0.16,
                                 corner_radius=0.12)
    cena.play(Write(geral), Create(caixa), run_time=1.2 * VEL)
    cena.wait(1.6 * VEL)


