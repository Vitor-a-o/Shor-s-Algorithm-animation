# -*- coding: utf-8 -*-
from manim import *
import numpy as np

from ..paleta import *
from ..ferramentas import *

# ============================================================================
# CAPÍTULO 3 — Multiplicação modular (slides 23–28): 5 × 4, Double and Add
#   Narração: C3N01 … C3N14 (roteiro_video2_aritmetica_modular.md)
#   Os agrupamentos nascem EM VOLTA dos próprios "4" sobre a reta — nada
#   desce para uma segunda linha.
# ============================================================================
def parte3(cena):
    def eq_mult(m):
        return formula(("c", VERDE), ("≡", PRETO), (str(m), VERMELHO),
                       ("×", PRETO), ("4", AZUL), *MOD("7"),
                       tamanho=38).to_edge(UP, buff=0.5)

    eq = eq_mult(5)

    # cinco blocos "4" quase encostados (a folga vem só do próprio traço)
    y1 = 1.55

    def fila_cima(m, W):
        """m blocos "4" azuis ocupando a largura W, rótulos na escala."""
        xs = np.linspace(-W / 2, W / 2, m + 1)
        tam = max(int(28 * (xs[1] - xs[0]) / 2.2), 6)
        blocos = VGroup(*[traco([xs[i], y1, 0], [xs[i + 1], y1, 0],
                                AZUL, gap=0.09, w=6) for i in range(m)])
        rotulos = VGroup(*[T("4", tam, AZUL)
                           .move_to([(xs[i] + xs[i + 1]) / 2, 1.95, 0])
                           for i in range(m)])
        return VGroup(blocos, rotulos)

    def fila_baixo(m, W):
        """c + setes na MESMA unidade da fila de cima (4·m unidades)."""
        u_ = W / (4 * m)
        x_ = -W / 2
        blocos = VGroup(traco([x_, 0.8, 0], [x_ + 6 * u_, 0.8, 0],
                              VERDE, gap=0.09, w=6))
        k = int(np.ceil((4 * m - 6) / 7))
        for i in range(k):
            blocos.add(traco([x_ + (6 + 7 * i) * u_, 0.8, 0],
                             [x_ + (6 + 7 * (i + 1)) * u_, 0.8, 0],
                             LARANJA, gap=0.09, w=6))
        return blocos

    base = fila_cima(5, 11.0)
    segs, rots = base[0], base[1]
    with narra(cena, "C3N01", 3.8):
        cena.play(Write(eq), run_time=1.0 * VEL)
        cena.play(LaggedStart(*[AnimationGroup(Create(s),
                                               TransformFromCopy(eq[4], r))
                                for s, r in zip(segs, rots)],
                              lag_ratio=0.15), run_time=2.0 * VEL)

    # linha de baixo: c + 7 + 7 (20 unidades, slide 24)
    u = 11.0 / 20.0
    x0 = -5.5
    baixo = VGroup(
        traco([x0, 0.8, 0], [x0 + 6 * u, 0.8, 0], VERDE, gap=0.09, w=6),
        traco([x0 + 6 * u, 0.8, 0], [x0 + 13 * u, 0.8, 0], LARANJA,
              gap=0.09, w=6),
        traco([x0 + 13 * u, 0.8, 0], [x0 + 20 * u, 0.8, 0], LARANJA,
              gap=0.09, w=6))
    rb = VGroup(T("c", 24, VERDE).move_to([x0 + 3 * u, 0.45, 0]),
                T("7", 24, LARANJA).move_to([x0 + 9.5 * u, 0.45, 0]),
                T("7", 24, LARANJA).move_to([x0 + 16.5 * u, 0.45, 0]))
    with narra(cena, "C3N02", 7.1):
        cena.play(*[Create(s) for s in baixo], FadeIn(rb), run_time=1.1 * VEL)

    # ---- o CUSTO é proporcional ao multiplicador (eco do laço do cap. 2):
    # o multiplicador cresce, a fila de "4" se multiplica junto e os setes
    # de baixo acompanham, encolhendo de escala até escapar do quadro
    with narra(cena, "C3N03", 10.4):
        cena.play(Indicate(eq[2], color=VERMELHO, scale_factor=1.6),
                  run_time=0.9 * VEL)
        # cópias intactas ANTES do crescimento: o ReplacementTransform
        # deforma os originais, e o restauro precisa da geometria de partida
        baixo0, rb0 = baixo.copy(), rb.copy()
        cima_v, baixo_v, eq_v = base, VGroup(baixo, rb), eq
        for m, W in ((10, 12.5), (20, 14.5), (40, 18.0)):
            cima_n = fila_cima(m, W)
            baixo_n = fila_baixo(m, W)
            eq_n = eq_mult(m)
            cena.play(ReplacementTransform(cima_v, cima_n),
                      ReplacementTransform(baixo_v, baixo_n),
                      ReplacementTransform(eq_v, eq_n),
                      run_time=1.1 * VEL)
            cima_v, baixo_v, eq_v = cima_n, baixo_n, eq_n
        # a fila volta ao caso pequeno: 5 × 4 de novo
        base = fila_cima(5, 11.0)
        segs, rots = base[0], base[1]
        baixo_r = VGroup(baixo0, rb0)
        eq = eq_mult(5)
        cena.play(ReplacementTransform(cima_v, base),
                  ReplacementTransform(baixo_v, baixo_r),
                  ReplacementTransform(eq_v, eq), run_time=1.2 * VEL)
        baixo, rb = baixo_r[0], baixo_r[1]

    # ---- reagrupar em duplas e duplas de duplas, EM VOLTA dos próprios
    # "4" (mesma manobra do capítulo 4): a fila abre espaço e desliza
    # para o layout-alvo [ ( 4 + 4 ) + ( 4 + 4 ) ] + 4
    alvo = formula(("[", PRETO), ("(", PRETO), ("4", AZUL), ("+", PRETO),
                   ("4", AZUL), (")", PRETO), ("+", PRETO), ("(", PRETO),
                   ("4", AZUL), ("+", PRETO), ("4", AZUL), (")", PRETO),
                   ("]", PRETO), ("+", PRETO), ("4", AZUL),
                   tamanho=30, buff=0.13).move_to([0, 1.95, 0])
    mapa = {0: 2, 1: 4, 2: 8, 3: 10, 4: 14}
    pe = VGroup(alvo[1], alvo[5], alvo[7], alvo[11])
    mais = VGroup(alvo[3], alvo[6], alvo[9], alvo[13])
    br = VGroup(alvo[0], alvo[12])
    with narra(cena, "C3N04", 9.2):
        # a linha c + 7 + 7 e a reta saem primeiro: o palco é da expressão
        cena.play(FadeOut(baixo), FadeOut(rb), FadeOut(segs),
                  run_time=0.5 * VEL)
        # "duplas": os parênteses abraçam o 1º com o 2º e o 3º com o 4º
        cena.play(*[rots[i].animate.move_to(alvo[mapa[i]]) for i in mapa],
                  *[GrowFromCenter(p) for p in pe],
                  *[FadeIn(m) for m in mais], run_time=1.0 * VEL)
        # "duplas de duplas": os colchetes fecham os dois parênteses;
        # o quinto "4" fica sozinho, sem nada em volta
        cena.play(*[GrowFromCenter(b) for b in br], run_time=0.9 * VEL)

    # ---- dentro de cada agrupamento: 4 + 4 vira 2·4; o quinto vira 1·4
    d1 = VGroup(T("2", 32, CIANO), T("· 4", 30, AZUL)).arrange(
        RIGHT, buff=0.08).move_to(alvo[3])
    d2 = VGroup(T("2", 32, CIANO), T("· 4", 30, AZUL)).arrange(
        RIGHT, buff=0.08).move_to(alvo[9])
    d3 = VGroup(T("1", 32, CIANO), T("· 4", 30, AZUL)).arrange(
        RIGHT, buff=0.08).move_to(alvo[14].get_center() + 0.3 * RIGHT)
    pe2 = VGroup(T("(", 34, PRETO).next_to(d1, LEFT, buff=0.08),
                 T(")", 34, PRETO).next_to(d1, RIGHT, buff=0.08),
                 T("(", 34, PRETO).next_to(d2, LEFT, buff=0.08),
                 T(")", 34, PRETO).next_to(d2, RIGHT, buff=0.08))
    with narra(cena, "C3N05", 8.3):
        cena.play(ReplacementTransform(VGroup(rots[0], alvo[3], rots[1]), d1),
                  ReplacementTransform(VGroup(rots[2], alvo[9], rots[3]), d2),
                  ReplacementTransform(pe, pe2), run_time=1.2 * VEL)
        cena.play(ReplacementTransform(rots[4], d3), run_time=0.8 * VEL)

    # ---- um nível acima: [2·4 + 2·4] vira 2²·4 e 1·4 vira 2⁰·4
    p1 = VGroup(pot("2", "2", CIANO, CIANO), T("· 4", 30, AZUL))
    p2 = VGroup(pot("2", "1", CIANO, CIANO), T("· 4", 30, AZUL))
    p3 = VGroup(pot("2", "0", CIANO, CIANO), T("· 4", 30, AZUL))
    for p in (p1, p2, p3):
        p.arrange(RIGHT, buff=0.10)
    linha = VGroup(p1, T("+", 30, PRETO), p2, T("+", 30, PRETO), p3)
    linha.arrange(RIGHT, buff=0.28).move_to([0, 0.85, 0])
    grupoA = VGroup(br[0], pe2[0], d1, pe2[1], alvo[6], pe2[2], d2, pe2[3],
                    br[1])
    with narra(cena, "C3N06", 1.7):
        # só p1 e p3 ficam em cena — o 2¹·4 ainda não existe; o "+" do
        # avulso vira o "+" da linha final, como o × faz no capítulo 4
        cena.play(ReplacementTransform(grupoA, p1),
                  ReplacementTransform(d3, p3),
                  ReplacementTransform(alvo[13], linha[3]),
                  run_time=1.2 * VEL)

    # ---- o 5 dá à luz "1 0 1" (originação, slide 26) — DEPOIS das potências
    with narra(cena, "C3N07", 5.0):
        digs = origina_binario(cena, eq[2], ["1", "0", "1"], y=2.05)

    # ---- o bit do meio está desligado: o termo dele NASCE apagado
    p2.set_opacity(0.25)
    with narra(cena, "C3N08", 4.6):
        cena.play(TransformFromCopy(digs[1], p2), FadeIn(linha[1]),
                  run_time=1.2 * VEL)

    # ---- cada parcela reduzida (mod 7) em paralelo: caixas cinzas do
    # slide 27 (a do bit 0, escura), bits em caixas e setas — emendados
    e1 = caixa_cinza(VGroup(pot("2", "2", CIANO, CIANO, 26),
                            T("· 4", 26, AZUL),
                            fmod("7", 24))
                     .arrange(RIGHT, buff=0.12)).move_to([-3.9, 0.35, 0])
    e2_int = VGroup(pot("2", "1", CIANO, CIANO, 26),
                    T("· 4", 26, AZUL),
                    fmod("7", 24)).arrange(RIGHT, buff=0.12)
    e2_int.set_opacity(0.25)
    e2 = caixa_cinza(e2_int, fundo=CAIXA2).move_to([0, 0.35, 0])
    e3 = caixa_cinza(VGroup(pot("2", "0", CIANO, CIANO, 26),
                            T("· 4", 26, AZUL),
                            fmod("7", 24))
                     .arrange(RIGHT, buff=0.12)).move_to([3.9, 0.35, 0])
    bits_cx = VGroup(
        caixa_cinza(T("1", 26, CIANO), pad=0.16).move_to([-3.9, 1.95, 0]),
        caixa_cinza(T("0", 26, AMARELO), pad=0.16,
                    fundo=CAIXA2).move_to([0, 1.95, 0]),
        caixa_cinza(T("1", 26, CIANO), pad=0.16).move_to([3.9, 1.95, 0]))
    setas_b = VGroup(*[Arrow(b.get_bottom() + 0.05 * DOWN,
                             e[0].get_top() + 0.05 * UP,
                             buff=0, color=PRETO, stroke_width=2.5,
                             max_tip_length_to_length_ratio=0.3)
                       for b, e in zip(bits_cx, (e1, e2, e3))])
    with narra(cena, "C3N09", 7.1):
        cena.play(ReplacementTransform(p1, e1), ReplacementTransform(p2, e2),
                  ReplacementTransform(p3, e3),
                  FadeOut(linha[1]), FadeOut(linha[3]), run_time=1.4 * VEL)
        cena.play(*[ReplacementTransform(d, b)
                    for d, b in zip(digs, bits_cx)], run_time=1.0 * VEL)
        cena.play(LaggedStart(*[GrowArrow(s) for s in setas_b], lag_ratio=0.2),
                  run_time=1.2 * VEL)

    # ---- árvore do slide 27: resultados verdes convergem para a soma
    res = VGroup(T("2", 34, VERDE).move_to([-3.9, -0.9, 0]),
                 T("0", 34, VERDE).move_to([0, -0.9, 0]),
                 T("4", 34, VERDE).move_to([3.9, -0.9, 0]))
    setas = VGroup(*[Arrow(e[0].get_bottom() + 0.05 * DOWN,
                           r.get_top() + 0.05 * UP,
                           buff=0, color=PRETO, stroke_width=2.5,
                           max_tip_length_to_length_ratio=0.3)
                     for e, r in zip((e1, e2, e3), res)])
    with narra(cena, "C3N10", 6.7):
        cena.play(LaggedStart(*[AnimationGroup(GrowArrow(s), FadeIn(r))
                                for s, r in zip(setas, res)], lag_ratio=0.2),
                  run_time=1.5 * VEL)
    so_fala(cena, "C3N11", 2.1)

    soma_f = formula(("(", PRETO), ("2", VERDE), ("+", PRETO), ("0", VERDE),
                     ("+", PRETO), ("4", VERDE), (")", PRETO),
                     *MOD("7"), tamanho=30, buff=0.10)
    soma = caixa_cinza(soma_f).move_to([0, -2.1, 0])
    setas2 = VGroup(*[Arrow(r.get_bottom() + 0.05 * DOWN,
                            soma[0].get_top() + np.array([dx, 0.05, 0]),
                            buff=0, color=PRETO, stroke_width=2.5,
                            max_tip_length_to_length_ratio=0.25)
                      for r, dx in zip(res, (-1.6, 0.0, 1.6))])
    with narra(cena, "C3N12", 3.8):
        cena.play(*[GrowArrow(s) for s in setas2], FadeIn(soma),
                  run_time=1.2 * VEL)

    seis = T("6", 42, VERDE).move_to([0, -3.25, 0])
    eq2 = formula(("6", VERDE), ("≡", PRETO), ("5", VERMELHO), ("×", PRETO),
                  ("4", AZUL), *MOD("7"), tamanho=38).move_to(eq)
    with narra(cena, "C3N13", 1.7):
        cena.play(TransformFromCopy(soma_f, seis), run_time=0.9 * VEL)
        cena.play(ReplacementTransform(eq, eq2),
                  TransformFromCopy(seis, eq2[0]), run_time=1.0 * VEL)
    so_fala(cena, "C3N14", 11.3)
