# -*- coding: utf-8 -*-
"""Peças compartilhadas entre os vídeos da série.

Aqui mora o que aparece em MAIS DE UM vídeo e não pertence a capítulo
nenhum. O que serve a um vídeo só continua morando no videoN.py dele.
"""

from manim import *

from ..paleta import CINZA, COR_TEXTO, LARANJA, VEL
from ..ferramentas import T, _agora, narra
from ..sincronias import _ate
from ..textos import tx

# os quatro vídeos, nos mesmos nomes dos cartões de marca de cada um
# (video2.py, video3.py, video4.py e o cartão do V1N00 no roteiro do 1)
VIDEOS = (tx("geral.video1"), tx("geral.titulo_cap1"),
          tx("geral.video3"), tx("geral.video4"))


def trilha_videos(acesos=(), tamanho=26, apagado=0.25):
    """A trilha vertical dos quatro títulos da série, numerados 1 a 4 e
    alinhados à esquerda.

    Quem usa: o V1N09 do vídeo 1, onde ela nasce apagada e só o 1 acende
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


def apresentacao(cena, ancora):
    """A apresentação do autor (V0N00), tocada por cima do cartão de marca.

    Quem usa: os quatro videoN.py, durante o cartão. `ancora` é o subtítulo
    ("Vídeo n de 4 — …") já em cena; o nome e o curso entram embaixo dele e a
    seta ↓ nasce no rodapé em "descrição". No fim, nome, curso e seta saem
    juntos; `ancora` e o título ficam para o vídeo que chamou tirar, e o
    cartão continua com a emenda de sempre."""
    nome = VGroup(T(tx("v0.nome"), 34, COR_TEXTO),
                  T(tx("v0.curso"), 26, CINZA))
    nome.arrange(DOWN, buff=0.2).next_to(ancora, DOWN, buff=0.7)
    seta = T(tx("v0.seta"), 40, CINZA).to_edge(DOWN, buff=0.5)
    with narra(cena, "V0N00", 17.1):
        t0 = _agora(cena)
        cena.play(FadeIn(nome, shift=0.2 * UP, run_time=0.8 * VEL))
        cena.play(Succession(
            _ate(cena, t0, "V0N00", 17.1, "descrição"),
            FadeIn(seta, shift=0.25 * DOWN, run_time=0.6 * VEL)))
    cena.play(FadeOut(VGroup(nome, seta), run_time=0.5 * VEL))
