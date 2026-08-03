# -*- coding: utf-8 -*-
from manim import *
import numpy as np

from ..paleta import *
from ..ferramentas import *

# ============================================================================
# CAPÍTULO 6 — Fermat NA TABELA multiplicativa mod 7 (slides 59–66)
# ============================================================================
def parte6(cena):
    # tabela 6×6 dos resíduos de 7
    tam = 0.6
    canto = np.array([-6.0, 2.1, 0.0])

    def ponto(i, j):
        return canto + np.array([j * tam, -i * tam, 0.0])

    head_c = VGroup(*[T(str(j), 24, AZUL).move_to(ponto(0, j))
                      for j in range(1, 7)])
    head_l = VGroup(*[T(str(i), 24, VERMELHO).move_to(ponto(i, 0))
                      for i in range(1, 7)])
    lin_h = Line(canto + [0.5 * tam, -0.5 * tam, 0],
                 canto + [6.45 * tam, -0.5 * tam, 0], color=PRETO,
                 stroke_width=1.5)
    lin_v = Line(canto + [0.5 * tam, -0.5 * tam, 0],
                 canto + [0.5 * tam, -6.45 * tam, 0], color=PRETO,
                 stroke_width=1.5)
    titulo_tab = T("Tabela multiplicativa (mod 7)", 26).move_to([-4.2, 2.85, 0])
    cena.play(FadeIn(titulo_tab), FadeIn(head_c), FadeIn(head_l),
              Create(lin_h), Create(lin_v), run_time=0.9 * VEL)
    linhas_cel = [VGroup(*[T(str((i * j) % 7), 24, PRETO).move_to(ponto(i, j))
                           for j in range(1, 7)]) for i in range(1, 7)]
    cena.play(LaggedStart(*[FadeIn(l) for l in linhas_cel], lag_ratio=0.12),
              run_time=1.8 * VEL)

    # elipse verde na linha 1 (slide 59) e cópia da linha para fora da tabela
    el1 = Ellipse(width=6 * tam + 0.55, height=0.55, color=VERDE,
                  stroke_width=2.5).move_to(canto + [3.5 * tam, -1 * tam, 0])
    cena.play(Create(el1), run_time=0.7 * VEL)
    xsr = np.linspace(1.4, 6.4, 6)
    yA, yB = 2.05, 0.25
    A = VGroup(*[T(str(j + 1), 30, PRETO).move_to([xsr[j], yA, 0])
                 for j in range(6)])
    cena.play(LaggedStart(*[TransformFromCopy(linhas_cel[0][j], A[j])
                            for j in range(6)], lag_ratio=0.1),
              run_time=1.5 * VEL)

    # MULTIPLICAR CADA RESTO POR 3 (slide 61): sob cada valor da linha 1,
    # o produto 3·j nasce do 3 vermelho e do próprio resto
    Bv = [3, 6, 2, 5, 1, 4]
    B = VGroup(*[T(str(Bv[j]), 30, VERMELHO).move_to([xsr[j], yB, 0])
                 for j in range(6)])
    prods = VGroup(*[formula(("3", VERMELHO), ("·" + str(j + 1), PRETO),
                             tamanho=22, buff=0.03)
                     .next_to(B[j], UP, buff=0.18) for j in range(6)])
    cena.play(LaggedStart(*[AnimationGroup(
        TransformFromCopy(head_l[2], p[0]),
        TransformFromCopy(A[j], p[1]))
        for j, p in enumerate(prods)], lag_ratio=0.15), run_time=2.0 * VEL)
    cena.wait(0.5 * VEL)

    # TIRAR O MÓDULO de cada produto: nascem os restos da linha do × 3
    mod_rot = fmod("7", 24).next_to(B, LEFT, buff=0.3)
    cena.play(FadeIn(mod_rot),
              LaggedStart(*[TransformFromCopy(prods[j], B[j])
                            for j in range(6)], lag_ratio=0.1),
              run_time=1.6 * VEL)
    cena.wait(0.5 * VEL)

    # elipse na linha 3 (slide 63): a linha 3 sai da tabela e cai EXATAMENTE
    # sobre os restos que acabamos de calcular
    el3 = Ellipse(width=6 * tam + 0.55, height=0.55, color=VERDE,
                  stroke_width=2.5).move_to(canto + [3.5 * tam, -3 * tam, 0])
    cena.play(Create(el3), Indicate(head_l[2], color=VERMELHO),
              run_time=0.8 * VEL)
    copias = VGroup(*[linhas_cel[2][j].copy() for j in range(6)])
    cena.play(LaggedStart(*[copias[j].animate.move_to(B[j])
                            .set_color(VERMELHO).scale(30 / 24)
                            for j in range(6)], lag_ratio=0.1),
              run_time=1.5 * VEL)
    cena.play(FadeOut(copias),
              *[Indicate(b, color=VERMELHO) for b in B], run_time=0.8 * VEL)
    cena.wait(0.5 * VEL)

    # CURVAS ligando os valores iguais: as duas linhas têm os mesmos números
    arcos = VGroup()
    for j in range(6):
        idx = Bv.index(j + 1)
        arcos.add(ArcBetweenPoints(A[j].get_bottom() + 0.08 * DOWN,
                                   prods[idx].get_top() + 0.08 * UP,
                                   angle=(0.65 if idx > j else -0.65),
                                   color=VERDE, stroke_width=2.5))
    cena.play(LaggedStart(*[Create(a) for a in arcos], lag_ratio=0.12),
              run_time=1.8 * VEL)
    cena.wait(0.8 * VEL)

    # produto da linha 3 escrito como (3·1)·(3·2)·…·(3·6)  (slide 61)
    eq0 = formula(("(", PRETO), ("3", VERMELHO), ("·1", PRETO),
                  (")(", PRETO), ("3", VERMELHO), ("·2", PRETO),
                  (")(", PRETO), ("3", VERMELHO), ("·3", PRETO),
                  (")(", PRETO), ("3", VERMELHO), ("·4", PRETO),
                  (")(", PRETO), ("3", VERMELHO), ("·5", PRETO),
                  (")(", PRETO), ("3", VERMELHO), ("·6", PRETO),
                  (")", PRETO), tamanho=24, buff=0.04).move_to([0, -2.35, 0])
    cena.play(LaggedStart(*[TransformFromCopy(p, VGroup(eq0[3 * j + 1],
                                                        eq0[3 * j + 2]))
                            for j, p in enumerate(prods)], lag_ratio=0.12),
              *[Write(eq0[i]) for i in range(0, 19, 3)],
              run_time=1.8 * VEL)
    nota = T("multiplicação é comutativa", 20, CINZA).move_to([0, -1.75, 0])
    cena.play(FadeIn(nota), run_time=0.6 * VEL)

    # comutatividade: os seis 3 se juntam em 3⁶ (slide 62)
    tre = pot("3", "6", VERMELHO, AZUL, 26)
    eq = VGroup(tre, T("· (1·2·3·4·5·6)", 26, PRETO), T("≡", 26, PRETO),
                T("(1·2·3·4·5·6)", 26, PRETO), fmod("7", 24))
    eq.arrange(RIGHT, buff=0.15).move_to([0, -2.4, 0])
    cena.play(ReplacementTransform(eq0, VGroup(eq[0], eq[1])),
              FadeIn(eq[2]),
              TransformFromCopy(A, eq[3]), FadeIn(eq[4]),
              FadeOut(nota), run_time=1.5 * VEL)
    cena.wait(0.8 * VEL)

    # dividir os dois lados pela MESMA multiplicação (slides 64–65)
    nota2 = T("dividir os dois lados pela mesma multiplicação", 20,
              CINZA).move_to([0, -1.75, 0])
    div_e = formula(("÷", VERDE), ("(1·2·3·4·5·6)", PRETO),
                    tamanho=20, buff=0.05).next_to(eq[1], DOWN, buff=0.2)
    div_d = formula(("÷", VERDE), ("(1·2·3·4·5·6)", PRETO),
                    tamanho=20, buff=0.05).next_to(eq[3], DOWN, buff=0.2)
    cena.play(FadeIn(nota2), Write(div_e), Write(div_d), run_time=1.0 * VEL)
    cena.wait(0.5 * VEL)
    tre2 = pot("3", "6", VERMELHO, AZUL, 34)
    resultado = VGroup(tre2, T("≡", 34, PRETO), T("1", 34, VERDE),
                       fmod("7", 32))
    resultado.arrange(RIGHT, buff=0.16).move_to([0, -2.4, 0])
    cena.play(ReplacementTransform(VGroup(eq, div_e, div_d), resultado),
              FadeOut(nota2), run_time=1.1 * VEL)
    geral = VGroup(pot("a", expoente(("n", LARANJA), ("−1", PRETO), tam=28),
                       VERMELHO, tam=28),
                   T("≡", 28, PRETO), T("1", 28, VERDE), fmod("n", 26),
                   T("(n primo)", 22, CINZA))
    geral.arrange(RIGHT, buff=0.16).move_to([0, -3.35, 0])
    cena.play(Write(geral), run_time=1.2 * VEL)
    cena.wait(1.6 * VEL)
