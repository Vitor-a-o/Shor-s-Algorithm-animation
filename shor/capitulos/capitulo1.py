# -*- coding: utf-8 -*-
from manim import *
import numpy as np

from ..paleta import *
from ..ferramentas import *


def parte1(cena):
    reta = NumberLine(x_range=[0, 12, 1], length=10, color=CINZA,
                      include_ticks=True, tick_size=0.06).shift(1.9 * DOWN)
    n2 = reta.n2p
    with narra(cena, "C1N01", 4.2):
        cena.play(Create(reta), run_time=1.5 * VEL)

    b11 = traco(n2(0) + 2.35 * UP, n2(11) + 2.35 * UP, AZUL)
    r11 = T("11", 30, AZUL).next_to(b11, UP, buff=0.12)
    with narra(cena, "C1N02", 5.4):
        cena.play(Create(b11), FadeIn(r11), run_time=1.5 * VEL)

    # todo o encaixe corre debaixo do C1N03, sem pausa entre as etapas:
    # os três blocos laranja em cadeia, o quarto estourando o zero e o fecho
    tres, r3s = VGroup(), VGroup()
    for i in (2, 1, 0):
        s = traco(n2(5 + 3 * i) + 0.5 * UP, n2(2 + 3 * i) + 0.5 * UP, LARANJA)
        tres.add(s)
        r3s.add(T("3", 26, LARANJA).next_to(s, UP, buff=0.10))
    tenta = traco(n2(2) + 0.5 * UP, n2(-1) + 0.5 * UP, LARANJA)
    r3x = T("3", 26, LARANJA).next_to(tenta, UP, buff=0.10)
    xis = T("✗", 30, VERMELHO).move_to(n2(-0.5) + 0.95 * UP)
    with narra(cena, "C1N03", 4.2):
        cena.play(LaggedStart(*[AnimationGroup(Create(s), FadeIn(r))
                                for s, r in zip(tres, r3s)],
                              lag_ratio=0.35), run_time=1.6 * VEL)
        cena.play(Create(tenta), FadeIn(r3x), run_time=0.9 * VEL)
        cena.play(Flash(n2(0) + 0.5 * UP, color=VERMELHO, flash_radius=0.4),
                  FadeIn(xis, scale=1.4), Wiggle(tenta), run_time=1.0 * VEL)

    s2 = traco(n2(2) + 0.5 * UP, n2(0) + 0.5 * UP, VERDE)
    r2 = T("2", 26, VERDE).next_to(s2, UP, buff=0.10)
    with narra(cena, "C1N09", 2.1):
        cena.play(ReplacementTransform(tenta, s2),
                  ReplacementTransform(r3x, r2),
                  FadeOut(xis), run_time=1.2 * VEL)

    eq = formula(("2", VERDE), ("≡", PRETO), ("11", AZUL),
                 ("(mod ", PRETO), ("3", LARANJA), (")", PRETO),
                 tamanho=40).to_edge(UP, buff=0.55)
    with narra(cena, "C1N10", 11.3):
        cena.play(TransformFromCopy(r2, eq[0]), FadeIn(eq[1]), FadeIn(eq[3]),
                  FadeIn(eq[5]), TransformFromCopy(r11, eq[2]),
                  TransformFromCopy(r3s[0], eq[4]), run_time=2.0 * VEL)

    so_fala(cena, "C1N11", 3.8)
    b8 = traco(n2(0) + 1.9 * UP, n2(8) + 1.9 * UP, VERMELHO)
    r8 = T("8", 26, VERMELHO).next_to(b8, RIGHT, buff=0.15)
    b5 = traco(n2(0) + 1.45 * UP, n2(5) + 1.45 * UP, CIANO)
    r5 = T("5", 26, CIANO).next_to(b5, RIGHT, buff=0.15)
    b2 = traco(n2(0) + 1.0 * UP, n2(2) + 1.0 * UP, ROSA)
    r2b = T("2", 26, ROSA).next_to(b2, RIGHT, buff=0.15)
    for b, r, tag, est in ((b8, r8, "C1N12", 2.5), (b5, r5, "C1N13", 1.3),
                           (b2, r2b, "C1N14", 2.9)):
        with narra(cena, tag, est):
            cena.play(Create(b), FadeIn(r), run_time=0.8 * VEL)

    cadeia = formula(("11", AZUL), ("≡", PRETO), ("8", VERMELHO),
                     ("≡", PRETO), ("5", CIANO), ("≡", PRETO), ("2", ROSA),
                     ("(mod ", PRETO), ("3", LARANJA), (")", PRETO),
                     tamanho=36).to_edge(UP, buff=0.55)
    with narra(cena, "C1N15", 10.4):
        cena.play(FadeOut(eq[0]), FadeOut(eq[1]), run_time=0.4 * VEL)
        cena.play(ReplacementTransform(eq[2], cadeia[0]),
                  FadeIn(cadeia[1]), TransformFromCopy(r8, cadeia[2]),
                  FadeIn(cadeia[3]), TransformFromCopy(r5, cadeia[4]),
                  FadeIn(cadeia[5]), TransformFromCopy(r2b, cadeia[6]),
                  ReplacementTransform(eq[3], cadeia[7]),
                  ReplacementTransform(eq[4], cadeia[8]),
                  ReplacementTransform(eq[5], cadeia[9]), run_time=2.5 * VEL)

    so_fala(cena, "C1N16", 7.1)
