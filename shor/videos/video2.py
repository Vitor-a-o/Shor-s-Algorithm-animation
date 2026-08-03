# -*- coding: utf-8 -*-
"""Vídeo 2 — Aritmética modular, as quatro operações: abertura e
encerramento próprios (roteiro_video2_aritmetica_modular.md)."""

from manim import *

from ..paleta import CINZA, LARANJA, PRETO, VERDE, VERMELHO, VEL
from ..ferramentas import T, narra, pot
from ..montagem import TITULOS
from ..cadeado import cadeado


def abertura(cena):
    """Cartão silencioso de ~4 s que se EMENDA ao CAP01 num movimento só:
    o subtítulo sai primeiro e o título encolhe e some por último, já com
    o cartão do capítulo 1 entrando por baixo. Por isso esta função também
    toca o CAP01 — quem a chama NÃO deve chamar abre_capitulo(cena, 1)."""
    t1 = T("Do Zero ao Algoritmo de Shor Quântico", 42)
    t2 = T("Vídeo 2 de 4 — Aritmética modular", 28, CINZA)
    VGroup(t1, t2).arrange(DOWN, buff=0.5)
    cena.play(Write(t1), run_time=1.1 * VEL)
    cena.play(FadeIn(t2, shift=0.25 * UP), run_time=0.8 * VEL)
    cena.wait(1.3 * VEL)
    cena.play(FadeOut(t2), run_time=0.6 * VEL)

    # o cartão do capítulo 1 (mesma diagramação do cartao_capitulo)
    r = T("Capítulo 1", 26, LARANJA)
    t = T(TITULOS[0], 38)
    g = VGroup(r, t).arrange(DOWN, buff=0.35)
    linha = Line(3 * LEFT, 3 * RIGHT, color=CINZA, stroke_width=1.5)
    linha.next_to(g, DOWN, buff=0.45)
    with narra(cena, "CAP01", 4.6):
        cena.play(FadeOut(t1, scale=0.5),
                  FadeIn(r, shift=0.3 * DOWN), Write(t), Create(linha),
                  run_time=1.3 * VEL)
    cena.play(FadeOut(g), FadeOut(linha), run_time=0.5 * VEL)


def encerramento(cena):
    """As quatro operações em fila, o ÷ riscado (a divisão continua não
    existindo), o cadeado fechado do vídeo 1 e o cartão do vídeo 3."""
    fila = VGroup(T("+", 48, PRETO), T("×", 48, PRETO),
                  pot("x", "n", PRETO, PRETO, 44), T("÷", 48, PRETO))
    fila.arrange(RIGHT, buff=1.1)
    risco = Line(fila[3].get_corner(DL) + 0.14 * DL,
                 fila[3].get_corner(UR) + 0.14 * UR,
                 color=VERMELHO, stroke_width=6)
    ainv = pot("a", "−1", VERDE, VERDE, 44).next_to(fila[3], RIGHT, buff=0.65)
    with narra(cena, "V2N00", 11.3):
        # um símbolo a cada operação nomeada
        for s in fila:
            cena.play(FadeIn(s, scale=1.3), run_time=0.7 * VEL)
        # "sem nunca fazer uma divisão": o ÷ é riscado e o a⁻¹ nasce ao
        # lado — o risco NÃO sai, porque a divisão continua não existindo
        cena.play(Create(risco), run_time=0.5 * VEL)
        cena.play(FadeIn(ainv, shift=0.2 * UP), run_time=0.7 * VEL)

    cad = cadeado("fechado")
    with narra(cena, "V2N01", 8.3):
        cena.play(FadeOut(fila), FadeOut(risco), FadeOut(ainv),
                  run_time=0.6 * VEL)
        cena.play(FadeIn(cad, scale=1.15), run_time=1.0 * VEL)

    # cartão final silencioso (~3 s)
    fim = T("Vídeo 3 de 4 — Do teorema ao RSA", 32)
    cena.play(FadeOut(cad), FadeIn(fim), run_time=0.8 * VEL)
    cena.wait(1.6 * VEL)
    cena.play(FadeOut(fim), run_time=0.6 * VEL)
