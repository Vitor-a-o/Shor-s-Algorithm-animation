# -*- coding: utf-8 -*-
"""O cadeado da série — a criptografia que protege a internet.

Genérico de propósito: é usado fechado no encerramento do vídeo 2 (V2N01),
abre e fecha na abertura do vídeo 1, ganha rótulos gravados no corpo
(RSA no V1N03, "fatorar n" no V3N01) e uma rachadura parcial no V3N02.
É também a peça central da fase 0 do capítulo 8.
"""

from manim import *

from .paleta import CINZA, LARANJA, PRETO, VEL
from .ferramentas import T

# ângulo entre o arco fechado (como construído) e aberto — usado tanto na
# construção (estado="aberto") quanto nas animações abrir()/fechar()
_ABERTURA = -60 * DEGREES


def _rotulo(corpo, texto, tamanho=26, cor=PRETO):
    """Texto centrado no corpo, encolhido se não couber (ex.: "fatorar n")."""
    r = T(texto, tamanho, cor)
    if r.width > corpo.width - 0.3:
        r.scale_to_fit_width(corpo.width - 0.3)
    return r.move_to(corpo)


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
        arco.rotate(_ABERTURA, about_point=[raio, topo - 0.18, 0])

    cad = VGroup(arco, corpo)
    if rotulo is None:
        buraco = VGroup(Dot(radius=0.10, color=PRETO),
                        Line(ORIGIN, 0.26 * DOWN, color=PRETO,
                             stroke_width=6))
        buraco.arrange(DOWN, buff=0).move_to(corpo).shift(0.05 * UP)
        cad.add(buraco)
    else:
        cad.add(_rotulo(corpo, rotulo))
    return cad


def gravar(cena, cad, texto, tamanho=26, cor=PRETO, run_time=0.9):
    """Grava `texto` no corpo de um `cad` já em cena, com o mesmo flash
    seco do travamento (V1N01) — usado para "RSA" (V1N03) e "fatorar n"
    (V3N01). Substitui o buraco de fechadura ou rótulo anterior."""
    corpo = cad[1]
    novo = _rotulo(corpo, texto, tamanho, cor)
    antigo = cad[2] if len(cad) > 2 else None
    anims = [Write(novo),
             Flash(corpo.get_center(), color=PRETO, flash_radius=0.9,
                   line_length=0.25)]
    if antigo is not None:
        anims.insert(0, FadeOut(antigo))
    cena.play(*anims, run_time=run_time * VEL)
    if antigo is not None:
        cad.remove(antigo)
    cad.add(novo)
    return novo


def rachar(cena, cad, run_time=1.0):
    """Racha o arco pela metade sem que o cadeado se abra (V3N02) — a
    quebra completa (arco estala, pedaços caem) fica para o vídeo 4."""
    arco = cad[0][0]  # o Arc, não as pernas
    p0 = arco.point_from_proportion(0.32)
    p1 = arco.point_from_proportion(0.42) + 0.14 * UP
    p2 = arco.point_from_proportion(0.50) + 0.11 * DOWN
    p3 = arco.point_from_proportion(0.60)
    rachadura = VMobject(stroke_color=CINZA, stroke_width=4)
    rachadura.set_points_as_corners([p0, p1, p2, p3])
    cena.play(Create(rachadura), run_time=run_time * VEL)
    cad.add(rachadura)
    return rachadura


def abrir(cena, cad, run_time=0.7):
    """Abre o arco — inverso de `fechar`, sem flash (abrir é silencioso)."""
    pivot = cad[0][2].get_bottom()
    cena.play(Rotate(cad[0], _ABERTURA, about_point=pivot),
              run_time=run_time * VEL)


def fechar(cena, cad, run_time=0.6):
    """Fecha o arco com o flash seco do V1N01 — chamar quando `cad`
    estiver aberto (por `abrir()` ou por `cadeado("aberto")`)."""
    pivot = cad[0][2].get_bottom()
    cena.play(Rotate(cad[0], -_ABERTURA, about_point=pivot),
              Flash(cad[1].get_top(), color=PRETO, flash_radius=0.55,
                    line_length=0.22),
              run_time=run_time * VEL)
