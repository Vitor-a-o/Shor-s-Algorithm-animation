# -*- coding: utf-8 -*-
"""O cadeado da série — a criptografia que protege a internet.

Genérico de propósito: é usado fechado no encerramento do vídeo 2 (V2N01)
e é pendência do vídeo 1, onde também abre.
"""

from manim import *

from .paleta import LARANJA, PRETO


def cadeado(estado="fechado", rotulo=None):
    """VGroup [arco, corpo, …] com o ARCO separado do corpo, para que o
    cadeado possa abrir e fechar: animar `cad[0]` move só o arco.

    estado: "fechado" (arco encaixado) ou "aberto" (arco girado para cima,
    apoiado na perna direita). rotulo: texto opcional no corpo (sem rótulo,
    o corpo ganha o buraco de fechadura)."""
    corpo = RoundedRectangle(width=1.9, height=1.5, corner_radius=0.18)
    corpo.set_fill(LARANJA, opacity=1).set_stroke(PRETO, width=3)

    raio = 0.62
    topo = corpo.get_top()[1]
    arco = VGroup(
        Arc(radius=raio, start_angle=PI, angle=-PI,
            arc_center=[0, topo + 0.28, 0]),
        Line([-raio, topo + 0.28, 0], [-raio, topo - 0.18, 0]),
        Line([raio, topo + 0.28, 0], [raio, topo - 0.18, 0]))
    arco.set_stroke(PRETO, width=8)
    if estado == "aberto":
        arco.rotate(-60 * DEGREES, about_point=[raio, topo - 0.18, 0])

    cad = VGroup(arco, corpo)
    if rotulo is None:
        buraco = VGroup(Dot(radius=0.10, color=PRETO),
                        Line(ORIGIN, 0.26 * DOWN, color=PRETO,
                             stroke_width=6))
        buraco.arrange(DOWN, buff=0).move_to(corpo).shift(0.05 * UP)
        cad.add(buraco)
    else:
        from .ferramentas import T
        cad.add(T(rotulo, 26, PRETO).move_to(corpo))
    return cad
