# -*- coding: utf-8 -*-
from manim import *
import numpy as np

from ..paleta import *
from ..ferramentas import *

# ============================================================================
# CAPÍTULO 4 — Exponenciação modular (slides 30–35): 3⁶, Square and Multiply
#   Narração: C4N01 … C4N16 (roteiro_video2_aritmetica_modular.md)
#   Os agrupamentos nascem EM VOLTA dos próprios "3" da corrente — nada
#   desce para uma segunda linha.
# ============================================================================
def parte4(cena):
    def eq_pot(m):
        t = pot("3", str(m), AZUL, VERMELHO, 38)
        g = VGroup(T("c", 38, VERDE), T("≡", 38, PRETO), t, fmod("7", 38))
        g.arrange(RIGHT, buff=0.16).to_edge(UP, buff=0.5)
        return g

    def corrente(k, W=None):
        """k trêses em corrente de multiplicações; W = largura imposta."""
        pares = []
        for i in range(k):
            pares.append(("3", AZUL))
            if i < k - 1:
                pares.append(("×", PRETO))
        f = formula(*pares, tamanho=30, buff=0.22)
        if W is not None:
            f.scale_to_fit_width(W)
        return f.move_to([0, 1.95, 0])

    def linha_resultado(x_max, com_ret=True):
        """A linha tracejada que só sugere o TAMANHO do resultado."""
        g = VGroup(*[traco([x, 1.5, 0], [x + 1.25, 1.5, 0], AZUL,
                           gap=0.09, w=6)
                     for x in np.arange(-x_max, x_max - 1.25, 1.25)])
        if com_ret:
            g.add(T("…", 30, AZUL).move_to([x_max - 0.45, 1.5, 0]))
        return g

    eq = eq_pot(6)
    tre = eq[2]

    # o produto 3 × 3 × 3 × 3 × 3 × 3 (slide 31): uma CORRENTE de
    # multiplicações — cada 3 NÃO é um comprimento somado, então os 3s
    # aparecem como fórmula, com os × entre eles
    prod = corrente(6)
    idx_3s = [0, 2, 4, 6, 8, 10]
    with narra(cena, "C4N01", 4.6):
        cena.play(Write(eq), run_time=1.0 * VEL)
        cena.play(LaggedStart(*[TransformFromCopy(tre[0], prod[i])
                                for i in idx_3s], lag_ratio=0.12),
                  *[FadeIn(prod[i]) for i in range(1, 11, 2)],
                  run_time=1.8 * VEL)

    # a linha tracejada embaixo e a linha c + 7 + 7 … correm emendadas
    segs = linha_resultado(5.5)
    baixo = VGroup(traco([-5.5, 0.8, 0], [-4.8, 0.8, 0], VERDE,
                         gap=0.09, w=6),
                   traco([-4.8, 0.8, 0], [-1.3, 0.8, 0], LARANJA,
                         gap=0.09, w=6),
                   traco([-1.3, 0.8, 0], [2.2, 0.8, 0], LARANJA,
                         gap=0.09, w=6),
                   T("…", 30, LARANJA).move_to([2.8, 0.8, 0]))
    rb = VGroup(T("c", 24, VERDE).move_to([-5.15, 0.45, 0]),
                T("7", 24, LARANJA).move_to([-3.05, 0.45, 0]),
                T("7", 24, LARANJA).move_to([0.45, 0.45, 0]))
    with narra(cena, "C4N02", 6.7):
        cena.play(LaggedStart(*[(Create(s) if isinstance(s, Line)
                                 else FadeIn(s)) for s in segs],
                              lag_ratio=0.08), run_time=1.2 * VEL)
        cena.play(*[Create(s) for s in baixo[:3]], FadeIn(baixo[3]),
                  FadeIn(rb), run_time=1.0 * VEL)

    # ---- o CUSTO aqui é de outra natureza (terceiro elo da corrente):
    # o expoente cresce, a corrente de trêses cresce DEVAGAR, e é a reta
    # tracejada do resultado que estoura para fora dos dois lados do
    # quadro, engolindo o "…"
    with narra(cena, "C4N03", 12.1):
        cena.play(Indicate(tre[1], color=VERMELHO, scale_factor=1.6),
                  run_time=0.9 * VEL)
        prod_v, segs_v, eq_v = prod, segs, eq
        for m, Wc, Wr in ((12, 11.5, 8.0), (24, 12.5, 10.0),
                          (48, 13.5, 12.5)):
            prod_n = corrente(m, Wc)
            segs_n = linha_resultado(Wr, com_ret=False)
            eq_n = eq_pot(m)
            cena.play(ReplacementTransform(prod_v, prod_n),
                      ReplacementTransform(segs_v, segs_n),
                      ReplacementTransform(eq_v, eq_n),
                      run_time=1.1 * VEL)
            prod_v, segs_v, eq_v = prod_n, segs_n, eq_n
        # a corrente volta ao caso pequeno: 3⁶ de novo
        prod = corrente(6)
        segs = linha_resultado(5.5)
        eq = eq_pot(6)
        tre = eq[2]
        cena.play(ReplacementTransform(prod_v, prod),
                  ReplacementTransform(segs_v, segs),
                  ReplacementTransform(eq_v, eq), run_time=1.2 * VEL)

    # ---- reagrupar em duplas e duplas de duplas, EM VOLTA dos "3" da
    # corrente: parênteses no 1º+2º, 3º+4º e 5º+6º; os colchetes fecham os
    # dois primeiros parênteses e o terceiro par fica sozinho no dele.
    # A corrente abre espaço enquanto é abraçada: os 3s deslizam para o
    # layout-alvo [ ( 3 × 3 ) × ( 3 × 3 ) ] × [ ( 3 × 3 ) ]
    alvo = formula(("[", PRETO), ("(", PRETO), ("3", AZUL), ("×", PRETO),
                   ("3", AZUL), (")", PRETO), ("×", PRETO), ("(", PRETO),
                   ("3", AZUL), ("×", PRETO), ("3", AZUL), (")", PRETO),
                   ("]", PRETO), ("×", PRETO), ("[", PRETO), ("(", PRETO),
                   ("3", AZUL), ("×", PRETO), ("3", AZUL), (")", PRETO),
                   ("]", PRETO),
                   tamanho=30, buff=0.13).move_to([0, 1.95, 0])
    mapa = {0: 2, 1: 3, 2: 4, 3: 6, 4: 8, 5: 9, 6: 10, 7: 13,
            8: 16, 9: 17, 10: 18}
    pe = VGroup(alvo[1], alvo[5], alvo[7], alvo[11], alvo[15], alvo[19])
    br = VGroup(alvo[0], alvo[12], alvo[14], alvo[20])
    with narra(cena, "C4N04", 7.1):
        # a reta do resultado e a linha c + 7 + 7 … saem primeiro
        cena.play(FadeOut(segs), FadeOut(baixo), FadeOut(rb),
                  run_time=0.5 * VEL)
        cena.play(*[prod[i].animate.move_to(alvo[mapa[i]]) for i in mapa],
                  *[GrowFromCenter(p) for p in pe], run_time=1.0 * VEL)
        cena.play(*[GrowFromCenter(b) for b in br], run_time=0.9 * VEL)

    # ---- dentro de cada agrupamento: 3 × 3 vira 3²
    q1 = pot("3", "2", AZUL, CIANO, 32).move_to(alvo[3])
    q2 = pot("3", "2", AZUL, CIANO, 32).move_to(alvo[9])
    q3 = pot("3", "2", AZUL, CIANO, 32).move_to(alvo[17])
    pe2 = VGroup(T("(", 34, PRETO).next_to(q1, LEFT, buff=0.08),
                 T(")", 34, PRETO).next_to(q1, RIGHT, buff=0.08),
                 T("(", 34, PRETO).next_to(q2, LEFT, buff=0.08),
                 T(")", 34, PRETO).next_to(q2, RIGHT, buff=0.08),
                 T("(", 34, PRETO).next_to(q3, LEFT, buff=0.08),
                 T(")", 34, PRETO).next_to(q3, RIGHT, buff=0.08))
    with narra(cena, "C4N05", 8.8):
        cena.play(ReplacementTransform(VGroup(prod[0], prod[1], prod[2]), q1),
                  ReplacementTransform(VGroup(prod[4], prod[5], prod[6]), q2),
                  ReplacementTransform(VGroup(prod[8], prod[9], prod[10]), q3),
                  ReplacementTransform(pe, pe2), run_time=1.4 * VEL)
    so_fala(cena, "C4N06", 6.2)

    # ---- um nível acima: [3² × 3²] vira 3^2² e [3²] vira 3^2¹ — e a
    # expressão desce para a faixa central, abrindo espaço aos bits
    p1 = pot("3", "2²", AZUL, CIANO, 32)
    p2 = pot("3", "2¹", AZUL, CIANO, 32)
    p3 = pot("3", "2⁰", AZUL, CIANO, 32)
    linha = VGroup(p1, T("×", 30, PRETO), p2, T("×", 30, PRETO), p3)
    linha.arrange(RIGHT, buff=0.30).move_to([0, 0.85, 0])
    grupoA = VGroup(br[0], pe2[0], q1, pe2[1], prod[3], pe2[2], q2, pe2[3],
                    br[1])
    grupoB = VGroup(br[2], pe2[4], q3, pe2[5], br[3])
    with narra(cena, "C4N07", 1.7):
        # só p1 e p2 ficam em cena — o 3^2⁰ ainda não existe
        cena.play(ReplacementTransform(grupoA, p1),
                  ReplacementTransform(grupoB, p2),
                  ReplacementTransform(prod[7], linha[1]),
                  run_time=1.2 * VEL)

    # ---- o expoente 6 dá à luz "1 1 0" (slide 33) — DEPOIS das potências
    with narra(cena, "C4N08", 5.0):
        digs = origina_binario(cena, tre[1], ["1", "1", "0"], y=2.05)

    # ---- o último bit está desligado: o termo dele NASCE apagado
    p3.set_opacity(0.25)
    with narra(cena, "C4N09", 5.0):
        cena.play(TransformFromCopy(digs[2], p3), FadeIn(linha[3]),
                  run_time=1.2 * VEL)

    # ---- cada fator reduzido (mod 7) em paralelo: caixas cinzas do
    # slide 34 (a do bit 0, escura), bits em caixas e setas — emendados
    e1 = caixa_cinza(VGroup(pot("3", "2²", AZUL, CIANO, 26),
                            fmod("7", 24))
                     .arrange(RIGHT, buff=0.14)).move_to([-3.9, 0.35, 0])
    e2 = caixa_cinza(VGroup(pot("3", "2¹", AZUL, CIANO, 26),
                            fmod("7", 24))
                     .arrange(RIGHT, buff=0.14)).move_to([0, 0.35, 0])
    e3_int = VGroup(pot("3", "2⁰", AZUL, CIANO, 26),
                    fmod("7", 24)).arrange(RIGHT, buff=0.14)
    e3_int.set_opacity(0.25)
    e3 = caixa_cinza(e3_int, fundo=CAIXA2).move_to([3.9, 0.35, 0])
    bits_cx = VGroup(
        caixa_cinza(T("1", 26, CIANO), pad=0.16).move_to([-3.9, 1.95, 0]),
        caixa_cinza(T("1", 26, CIANO), pad=0.16).move_to([0, 1.95, 0]),
        caixa_cinza(T("0", 26, AMARELO), pad=0.16,
                    fundo=CAIXA2).move_to([3.9, 1.95, 0]))
    setas_b = VGroup(*[Arrow(b.get_bottom() + 0.05 * DOWN,
                             e[0].get_top() + 0.05 * UP,
                             buff=0, color=PRETO, stroke_width=2.5,
                             max_tip_length_to_length_ratio=0.3)
                       for b, e in zip(bits_cx, (e1, e2, e3))])
    with narra(cena, "C4N10", 7.5):
        cena.play(ReplacementTransform(p1, e1), ReplacementTransform(p2, e2),
                  ReplacementTransform(p3, e3),
                  FadeOut(linha[1]), FadeOut(linha[3]), run_time=1.4 * VEL)
        cena.play(*[ReplacementTransform(d, b)
                    for d, b in zip(digs, bits_cx)], run_time=1.0 * VEL)
        cena.play(LaggedStart(*[GrowArrow(s) for s in setas_b], lag_ratio=0.2),
                  run_time=1.2 * VEL)

    # ---- árvore do slide 34: resultados verdes convergem para o produto
    res = VGroup(T("4", 34, VERDE).move_to([-3.9, -0.9, 0]),
                 T("2", 34, VERDE).move_to([0, -0.9, 0]),
                 T("1", 34, VERDE).move_to([3.9, -0.9, 0]))
    setas = VGroup(*[Arrow(e[0].get_bottom() + 0.05 * DOWN,
                           r.get_top() + 0.05 * UP,
                           buff=0, color=PRETO, stroke_width=2.5,
                           max_tip_length_to_length_ratio=0.3)
                     for e, r in zip((e1, e2, e3), res)])
    with narra(cena, "C4N11", 5.8):
        cena.play(LaggedStart(*[AnimationGroup(GrowArrow(s), FadeIn(r))
                                for s, r in zip(setas, res)], lag_ratio=0.2),
                  run_time=1.5 * VEL)
    so_fala(cena, "C4N12", 4.2)

    soma_f = formula(("(", PRETO), ("4", VERDE), ("×", PRETO), ("2", VERDE),
                     ("×", PRETO), ("1", VERDE), (")", PRETO),
                     *MOD("7"), tamanho=30, buff=0.10)
    soma = caixa_cinza(soma_f).move_to([0, -2.1, 0])
    setas2 = VGroup(*[Arrow(r.get_bottom() + 0.05 * DOWN,
                            soma[0].get_top() + np.array([dx, 0.05, 0]),
                            buff=0, color=PRETO, stroke_width=2.5,
                            max_tip_length_to_length_ratio=0.25)
                      for r, dx in zip(res, (-1.6, 0.0, 1.6))])
    with narra(cena, "C4N13", 3.8):
        cena.play(*[GrowArrow(s) for s in setas2], FadeIn(soma),
                  run_time=1.2 * VEL)

    um = T("1", 42, VERDE).move_to([0, -3.25, 0])
    tre2 = pot("3", "6", AZUL, VERMELHO, 38)
    eq2 = VGroup(T("1", 38, VERDE), T("≡", 38, PRETO), tre2, fmod("7", 38))
    eq2.arrange(RIGHT, buff=0.16).move_to(eq)
    with narra(cena, "C4N14", 1.7):
        cena.play(TransformFromCopy(soma_f, um), run_time=0.9 * VEL)
        cena.play(ReplacementTransform(eq, eq2),
                  TransformFromCopy(um, eq2[0]), run_time=1.0 * VEL)
    so_fala(cena, "C4N15", 12.9)
    so_fala(cena, "C4N16", 8.8)
