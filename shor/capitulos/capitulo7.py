# -*- coding: utf-8 -*-
from manim import *
import numpy as np
from functools import partial

from ..paleta import *
from ..ferramentas import *
from ..ferramentas import _agora
from ..sincronias import na_palavra

# ============================================================================
# CAPÍTULO 7 — Euler NA TABELA mod 9 (slides 67–81): o cancelamento proibido
#   Narração: C7N01 … C7N14 (roteiro_video3_do_teorema_ao_rsa.md)
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
    linhas_cel = [VGroup(*[T(str((i * j) % 9), 22, PRETO).move_to(ponto(i, j))
                           for j in range(1, 9)]) for i in range(1, 9)]
    with narra(cena, "C7N01", 7.5):
        cena.play(FadeIn(head_c, run_time=0.9 * VEL),
                  FadeIn(head_l, run_time=0.9 * VEL),
                  Create(lin_h, run_time=0.9 * VEL),
                  Create(lin_v, run_time=0.9 * VEL),
                  LaggedStart(*[FadeIn(l) for l in linhas_cel], lag_ratio=0.1,
                              run_time=1.8 * VEL))

    # elipse vermelha na linha 2 (slide 68): tentamos o truque de Fermat
    el2 = Ellipse(width=8 * tam + 0.5, height=0.5, color=VERMELHO,
                  stroke_width=2.5).move_to(canto + [4.5 * tam, -2 * tam, 0])

    # a equação da tentativa — com 3 e 6 em ROXO (slide 70)
    esq = formula(("2⁸", VERMELHO), ("· (1·2·", PRETO), ("3", ROXO),
                  ("·4·5·", PRETO), ("6", ROXO), ("·7·8)", PRETO),
                  tamanho=24, buff=0.06)
    dir_ = formula(("(1·2·", PRETO), ("3", ROXO), ("·4·5·", PRETO),
                   ("6", ROXO), ("·7·8)", PRETO), *MOD("9"),
                   tamanho=24, buff=0.06)
    eq = VGroup(esq, T("≡", 26, PRETO), dir_)
    eq.arrange(RIGHT, buff=0.2).move_to([0, -2.35, 0])
    with narra(cena, "C7N02", 3.3):
        na = partial(na_palavra, cena, _agora(cena), "C7N02", 3.3)
        cena.play(Create(el2), Write(eq), run_time=1.4 * VEL)
        # "multiplicador": a linha 2 e o 2⁸, depois do Write(eq) (não dá para
        # pulsar o que ainda está sendo escrito); "lista de restos": as listas
        # 1·…·8 dos dois lados, cada token na própria cor
        cena.play(na("multiplicador", realce(head_l[1], esq[0])),
                  na("lista de restos", realce(*esq[1:], *dir_[0:5])))

    # tentativa: DIVIDIR os dois lados pela mesma multiplicação
    ge = VGroup(*esq[1:])
    gd = VGroup(*dir_[:5])
    div_e = formula(("÷", VERMELHO), ("(1·2·", PRETO), ("3", ROXO),
                    ("·4·5·", PRETO), ("6", ROXO), ("·7·8)", PRETO),
                    tamanho=20, buff=0.05).next_to(ge, DOWN, buff=0.2)
    div_d = formula(("÷", VERMELHO), ("(1·2·", PRETO), ("3", ROXO),
                    ("·4·5·", PRETO), ("6", ROXO), ("·7·8)", PRETO),
                    tamanho=20, buff=0.05).next_to(gd, DOWN, buff=0.2)
    with narra(cena, "C7N03", 6.2):
        na = partial(na_palavra, cena, _agora(cena), "C7N03", 6.2)
        cena.play(na("cancelar a lista",
                     Write(div_e, run_time=1.0 * VEL),
                     Write(div_d, run_time=1.0 * VEL)))

    # POR QUE a divisão é proibida: dividir por um fator é MULTIPLICAR
    # pelo inverso dele — e 1/3 e 1/6 NÃO EXISTEM módulo 9
    exp1 = T(tx("c7.dividir_e_multiplicar"), 22,
             PRETO).move_to([3.7, 1.75, 0])
    exp2 = formula(("1/", PRETO), ("3", ROXO), (tx("geral.e"), PRETO), ("1/", PRETO),
                   ("6", ROXO), (tx("c7.nao_existem"), VERMELHO), *MOD("9"),
                   tamanho=22, buff=0.08).move_to([3.7, 1.2, 0])
    with narra(cena, "C7N04", 8.3):
        na = partial(na_palavra, cena, _agora(cena), "C7N04", 8.3)
        cena.play(FadeIn(exp1), Write(exp2), run_time=1.0 * VEL)
        # "dois desses fatores": os 3 e 6 roxos de todas as cópias; "módulo":
        # o 9 do exp2 e o de dir_
        cena.play(na("dois desses fatores",
                     realce(esq[2], esq[4], dir_[1], dir_[3],
                            div_e[2], div_e[4], div_d[2], div_d[4])))
        cena.play(na("módulo", realce(exp2[7], dir_[6])))

    # RESSALTA os inversos que não existem: os 3 e 6 roxos pulsam,
    # as linhas 3 e 6 da tabela apagam — a divisão é NEGADA
    neq = T("≢", 30, VERMELHO).move_to(eq[1])
    with narra(cena, "C7N05", 10.0):
        na = partial(na_palavra, cena, _agora(cena), "C7N05", 10.0)
        # o primeiro play começa em "linhas"; cada peça leva o run_time que
        # o play lhe dava (o do play sobrescreveria o do Wait)
        apaga = [linhas_cel[i].animate.set_opacity(0.2).build()
                 for i in (2, 5)]
        apaga += [head_l[i].animate.set_opacity(0.3).build()
                  for i in (2, 5)]
        for a in apaga:
            a.set_run_time(1.4 * VEL)
        cena.play(na("linhas", *apaga,
                     Indicate(div_e[2], color=ROXO, run_time=1.4 * VEL),
                     Indicate(div_e[4], color=ROXO, run_time=1.4 * VEL),
                     Indicate(div_d[2], color=ROXO, run_time=1.4 * VEL),
                     Indicate(div_d[4], color=ROXO, run_time=1.4 * VEL),
                     Indicate(exp2[5], color=VERMELHO, run_time=1.4 * VEL)))
        cena.play(Wiggle(div_e), Wiggle(div_d), run_time=0.9 * VEL)
        cena.play(FadeOut(div_e), FadeOut(div_d), Transform(eq[1], neq),
                  run_time=0.8 * VEL)

    # Euler: RETIRA os inversos que não existem — cruzes riscam o 3 e o 6
    # na equação e no topo da tabela → φ(9) = 6 sobreviventes
    cruzes = VGroup(Cross(head_c[2], stroke_color=VERMELHO, stroke_width=4),
                    Cross(head_c[5], stroke_color=VERMELHO, stroke_width=4))
    cruzes_eq = VGroup(*[Cross(m, stroke_color=VERMELHO, stroke_width=3.5)
                         for m in (esq[2], esq[4], dir_[1], dir_[3])])
    with narra(cena, "C7N06", 5.8):
        na = partial(na_palavra, cena, _agora(cena), "C7N06", 5.8)
        cena.play(FadeOut(exp1), FadeOut(exp2), run_time=1.0 * VEL)
        cena.play(na("números que não têm inverso",
                     Create(cruzes, run_time=1.0 * VEL),
                     Create(cruzes_eq, run_time=1.0 * VEL)))

    sobr = T("{1, 2, 4, 5, 7, 8}", 26, VERDE).move_to([3.6, 1.5, 0])
    with narra(cena, "C7N07", 5.0):
        na = partial(na_palavra, cena, _agora(cena), "C7N07", 5.0)
        cena.play(na("números", FadeIn(sobr, run_time=0.7 * VEL)))
        cena.play(na("módulo", realce(dir_[6])))

    phi = formula(("φ(", PRETO), ("9", LARANJA), (") = 6", PRETO),
                  tamanho=28, buff=0.06).move_to([3.6, 0.9, 0])
    with narra(cena, "C7N08", 7.1):
        na = partial(na_palavra, cena, _agora(cena), "C7N08", 7.1)
        cena.play(na("contagem", Write(phi, run_time=1.0 * VEL)))
        # cada token do φ(9) = 6 pulsa na própria cor (o 9 é laranja)
        cena.play(na("fi de ene", realce(*phi)))

    # a equação REFEITA só com inversíveis — agora a divisão é permitida
    esq2 = formula(("2⁶", VERMELHO), ("· (1·2·4·5·7·8)", PRETO),
                   tamanho=24, buff=0.10)
    dir2 = formula(("(1·2·4·5·7·8)", PRETO), *MOD("9"),
                   tamanho=24, buff=0.10)
    eq2 = VGroup(esq2, T("≡", 26, PRETO), dir2)
    eq2.arrange(RIGHT, buff=0.2).move_to(eq)
    with narra(cena, "C7N09", 4.2):
        cena.play(ReplacementTransform(eq, eq2), FadeOut(cruzes_eq),
                  run_time=1.1 * VEL)

    div2_e = formula(("÷", VERDE), ("(1·2·4·5·7·8)", PRETO),
                     tamanho=20, buff=0.05).next_to(esq2[1], DOWN, buff=0.2)
    div2_d = formula(("÷", VERDE), ("(1·2·4·5·7·8)", PRETO),
                     tamanho=20, buff=0.05).next_to(dir2[0], DOWN, buff=0.2)
    with narra(cena, "C7N10", 4.2):
        cena.play(Write(div2_e), Write(div2_d), run_time=0.8 * VEL)

    res = formula(("2⁶", VERMELHO), ("≡", PRETO), ("1", VERDE),
                  *MOD("9"), tamanho=32).move_to(eq2)
    with narra(cena, "C7N11", 5.0):
        na = partial(na_palavra, cena, _agora(cena), "C7N11", 5.0)
        cena.play(ReplacementTransform(VGroup(eq2, div2_e, div2_d), res),
                  run_time=1.1 * VEL)
        cena.play(na("potência", realce(res[0])))
        cena.play(na("a um", realce(res[2])))
        cena.play(na("nove", realce(res[4])))

    geral = VGroup(pot("a", expoente(("φ(", PRETO), ("n", LARANJA),
                                     (")", PRETO), tam=28), ROXO, tam=28),
                   T("≡", 28, PRETO), T("1", 28, VERDE), fmod("n", 26))
    geral.arrange(RIGHT, buff=0.16).move_to([0, -3.35, 0])
    with narra(cena, "C7N12", 8.3):
        na = partial(na_palavra, cena, _agora(cena), "C7N12", 8.3)
        cena.play(Write(geral), run_time=1.2 * VEL)
        # o n do módulo e o n do expoente (geral[0][1][1]) pulsam juntos; o
        # φ(n) do expoente pulsa token a token, cada um na própria cor
        cena.play(na("qualquer módulo",
                     realce(geral[3][1], geral[0][1][1])))
        cena.play(na("o expoente", realce(*geral[0][1])))
        cena.play(na("totiente", realce(*geral[0][1])))

    # A VIRADA, espelhando o C6N14: a tabela inteira e o aparato de exemplo
    # saem, e no mesmo bloco o geral sobe e cresce — sobrevivendo à limpeza,
    # o mesmo mobject viajando, sem ser redesenhado — enquanto o título
    # nasce. res é a última coisa a sumir, debaixo do geral que o generaliza.
    titulo = T(tx("c7.teorema_euler"), 40).move_to([0, 0.9, 0])
    saida = AnimationGroup(
        FadeOut(head_c), FadeOut(head_l), FadeOut(lin_h), FadeOut(lin_v),
        *[FadeOut(l) for l in linhas_cel],
        FadeOut(el2), FadeOut(cruzes), FadeOut(sobr), FadeOut(phi),
        FadeOut(eq2), FadeOut(div2_e), FadeOut(div2_d),
        geral.animate.move_to([0, -0.5, 0]).scale(40 / 28),
        Write(titulo), run_time=1.0 * VEL,
    )
    with narra(cena, "C7N13", 2.5):
        cena.play(LaggedStart(saida, FadeOut(res, run_time=0.6 * VEL),
                              lag_ratio=0.4))

    with narra(cena, "C7N14", 3.8):
        cena.play(Indicate(geral[0][1], color=ROXO), run_time=1.0 * VEL)
