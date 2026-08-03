# -*- coding: utf-8 -*-
"""Montagem do filme: ordem dos capítulos, títulos, abertura e encerramento."""

from pathlib import Path

from manim import *

from .paleta import CINZA, LARANJA, VERDE2, PRETO, ROSA, BRANCO, VEL
from .ferramentas import T, formula, cartao_capitulo, narra
from .capitulos.capitulo1 import parte1
from .capitulos.capitulo2 import parte2
from .capitulos.capitulo3 import parte3
from .capitulos.capitulo4 import parte4
from .capitulos.capitulo5 import parte5
from .capitulos.capitulo6 import parte6
from .capitulos.capitulo7 import parte7
from .capitulos.capitulo8 import parte8
from .capitulos.capitulo9 import parte9
from .capitulos.capitulo9b import parte9b
from .capitulos.capitulo10 import parte10

IMG_ABERTURA = (Path(__file__).resolve().parent.parent
                / "media" / "images" / "filme_shor" / "open_image.png")

CARTOES = {
    1: 4.6, 2: 4.6, 3: 4.6, 4: 5.0, 5: 4.2,
    6: 4.6, 7: 5.4, 8: 5.4,
}

TITULOS = [
    "Aritmética modular",
    "Adição modular",
    "Multiplicação modular — Double and Add",
    "Exponenciação modular — Square and Multiply",
    "Inverso multiplicativo modular",
    "Pequeno Teorema de Fermat",
    "A generalização de Euler: φ(n)",
    "O algoritmo RSA",
    "Ordem Modular",
    "Da Ordem Modular à fatoração",
    "Shor Quântico: a QFT encontra o período",
]
PARTES = [parte1, parte2, parte3, parte4, parte5,
          parte6, parte7, parte8, parte9, parte9b, parte10]

def abre_capitulo(cena, i):
    cartao_capitulo(cena, f"Capítulo {i}", TITULOS[i - 1],
                    tag=f"CAP{i:02d}", est=CARTOES.get(i, 3.0))

def abertura(cena):
    # Arte de abertura full-bleed: preenche a tela toda (a imagem é levemente
    # mais larga que o quadro, então as bordas laterais sangram — sem tarjas).
    arte = ImageMobject(str(IMG_ABERTURA))
    arte.height = config.frame_height

    # Faixa escura no rodapé — a região menos poluída da arte — para o título
    # respirar com contraste sobre o fundo.
    faixa = Rectangle(width=config.frame_width, height=2.1,
                      stroke_width=0, fill_color=PRETO, fill_opacity=0.6)
    faixa.to_edge(DOWN, buff=0)
    t1 = T("Do Zero ao Algoritmo de Shor Quântico", 42, BRANCO)
    t1.move_to(faixa)

    with narra(cena, "ABN01", 8.3):
        cena.play(FadeIn(arte), run_time=1.2 * VEL)
        cena.play(FadeIn(faixa), Write(t1), run_time=1.6 * VEL)
        # leve zoom cinematográfico (Ken Burns) enquanto a locução corre
        cena.play(arte.animate.scale(1.07), run_time=5.0 * VEL, rate_func=linear)
    cena.play(FadeOut(t1), FadeOut(faixa), FadeOut(arte), run_time=0.6 * VEL)


def encerramento(cena):
    t1 = formula(("21", LARANJA), ("=", PRETO), ("3", ROSA), ("×", PRETO),
                 ("7", VERDE2), tamanho=54)
    t2 = T("fim", 24, CINZA)
    g = VGroup(t1, t2).arrange(DOWN, buff=0.6)
    with narra(cena, "FIM01", 6.0):
        cena.play(FadeIn(t1, scale=1.3), run_time=1.1 * VEL)
    cena.play(FadeIn(t2), run_time=0.7 * VEL)
    cena.wait(2.2 * VEL)