# -*- coding: utf-8 -*-
"""Peças compartilhadas entre os vídeos da série.

Aqui mora o que aparece em MAIS DE UM vídeo e não pertence a capítulo
nenhum. O que serve a um vídeo só continua morando no videoN.py dele.
"""

from manim import *

from ..paleta import COR_TEXTO, LARANJA
from ..ferramentas import T

# os quatro vídeos, nos mesmos nomes dos cartões de marca de cada um
# (video2.py, video3.py, video4.py e o cartão do V1N00 no roteiro do 1)
VIDEOS = ("Introdução", "Aritmética modular",
          "Do teorema ao RSA", "O algoritmo de Shor")


def trilha_videos(acesos=(), tamanho=26, apagado=0.25):
    """A trilha vertical dos quatro títulos da série, numerados 1 a 4 e
    alinhados à esquerda.

    Quem usa: o V1N06 do vídeo 1, onde ela nasce apagada e só o 1 acende
    (`trilha_videos(acesos=(1,))`), e o V4N04 do vídeo 4, onde ela volta
    com os quatro acesos (`trilha_videos(acesos=(1, 2, 3, 4))`).

    `acesos` são os números 1..4 que ficam em opacidade cheia; os outros
    entram em `apagado`. Devolve VGroup de quatro VGroup(número, título),
    então o vídeo 1 pode acender um deles depois, um a um."""
    linhas = VGroup()
    for i, nome in enumerate(VIDEOS, start=1):
        linha = VGroup(T(str(i), tamanho, LARANJA),
                       T(nome, tamanho, COR_TEXTO))
        linha.arrange(RIGHT, buff=0.35)
        if i not in acesos:
            linha.set_opacity(apagado)
        linhas.add(linha)
    return linhas.arrange(DOWN, buff=0.45, aligned_edge=LEFT)
