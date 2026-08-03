# -*- coding: utf-8 -*-
from manim import *
import numpy as np

from ..paleta import *
from ..ferramentas import *


# ---------------------------------------------------------------------------
# peças do capítulo 10
# ---------------------------------------------------------------------------
def _carta_qubit(w=0.78, h=1.02, tam=22):
    """Cartão de qubit em superposição (gradiente verde↔laranja dos slides)."""
    r = RoundedRectangle(corner_radius=0.10, width=w, height=h,
                         stroke_width=0)
    r.set_fill(color=[LARANJA, VERDE], opacity=1)
    r.set_sheen_direction(UR)
    um = T("1", tam, PRETO).move_to(r.get_center() + [0.18, 0.26, 0])
    zero = T("0", tam, PRETO).move_to(r.get_center() + [-0.18, -0.26, 0])
    return VGroup(r, um, zero)


def _carta_fixa(txt, cor, w=0.78, h=1.02, tam=22):
    """Cartão colapsado: verde para 1, laranja para 0 (slide 148)."""
    r = RoundedRectangle(corner_radius=0.10, width=w, height=h,
                         stroke_width=0).set_fill(cor, opacity=1)
    return VGroup(r, T(txt, tam, PRETO).move_to(r))


def _caixa_porta(expo, w=1.72, h=1.15, tam=17):
    """Porta 2^(2^i) (mod 21) do circuito: gradiente com o "1" embaixo."""
    r = RoundedRectangle(corner_radius=0.10, width=w, height=h,
                         stroke_width=0)
    r.set_fill(color=[LARANJA, VERDE], opacity=1)
    r.set_sheen_direction(UP)
    topo = VGroup(pot("2", expo, VERMELHO, CIANO, tam), fmod("21", tam - 2))
    topo.arrange(RIGHT, buff=0.07).move_to(r.get_center() + [0, 0.26, 0])
    um = T("1", tam + 1, PRETO).move_to(r.get_center() + [0, -0.30, 0])
    return VGroup(r, topo, um)


# ============================================================================
# CAPÍTULO 10 — Shor Quântico (slides 143–179), cores adaptadas ao branco
# ============================================================================
def p10_fundamentos(cena):
    """Slide 148: superposição e emaranhamento — os fenômenos que dão
    o paralelismo do computador quântico."""
    t1 = T("superposição", 26, PRETO).move_to([-4.0, 2.6, 0])
    q1 = _carta_qubit().scale(1.15).move_to([-4.0, 1.3, 0])
    cena.play(FadeIn(t1), FadeIn(q1, scale=0.8), run_time=1.0 * VEL)

    t2 = T("emaranhamento", 26, PRETO).move_to([2.6, 2.6, 0])
    qa = _carta_qubit().move_to([1.2, 1.3, 0])
    qb = _carta_qubit().move_to([3.9, -0.3, 0])
    no = Dot([3.9, 1.3, 0], radius=0.07, color=PRETO)
    fio = VGroup(Line(qa.get_right(), no.get_center(), color=PRETO,
                      stroke_width=2.5),
                 Line(no.get_center(), qb.get_top(), color=PRETO,
                      stroke_width=2.5))
    cena.play(FadeIn(t2), FadeIn(qa, scale=0.8), run_time=0.8 * VEL)
    cena.play(Create(fio), FadeIn(no), FadeIn(qb, scale=0.8),
              run_time=0.9 * VEL)
    cena.wait(0.6 * VEL)

    # medir UM decide o OUTRO: os dois colapsam juntos (1,1) — ou (0,0)
    nota = T("medir um decide o outro", 22, CINZA).move_to([2.6, -1.8, 0])
    cena.play(FadeIn(nota), run_time=0.7 * VEL)
    par_1 = VGroup(_carta_fixa("1", VERDE).move_to(qa),
                   _carta_fixa("1", VERDE).move_to(qb))
    cena.play(Flash(qa.get_center(), color=VERDE, flash_radius=0.7),
              ReplacementTransform(VGroup(qa, qb), par_1),
              run_time=1.0 * VEL)
    cena.wait(0.7 * VEL)
    par_0 = VGroup(_carta_fixa("0", LARANJA).move_to(par_1[0]),
                   _carta_fixa("0", LARANJA).move_to(par_1[1]))
    cena.play(ReplacementTransform(par_1, par_0), run_time=0.9 * VEL)
    cena.wait(0.9 * VEL)
    cena.play(FadeOut(VGroup(t1, q1, t2, par_0, no, fio, nota)),
              run_time=0.7 * VEL)


def p10_circuito(cena):
    """Slides 151–157 e 165–166: o circuito que calcula 2ᵇ (mod 21) para
    TODOS os b ao mesmo tempo, e a caixa TQF."""
    eqc = VGroup(T("c", 30, VERDE), T("≡", 30, PRETO),
                 pot("2", "b", VERMELHO, AZUL, 30), fmod("21", 28))
    eqc.arrange(RIGHT, buff=0.14).to_edge(UP, buff=0.4)
    cena.play(Write(eqc), run_time=1.0 * VEL)

    # fios: 4 controles (com ⋮) em cima, alvo |1⟩ embaixo
    ys = [2.0, 0.9, 0.1, -0.7]
    yt = -2.3
    x0, x1 = -5.3, 5.6
    fios = VGroup(*[Line([x0, y, 0], [x1, y, 0], color=PRETO,
                         stroke_width=2) for y in ys + [yt]])
    kets = VGroup(*[T("|0⟩", 22, PRETO).next_to([x0, y, 0], LEFT, buff=0.15)
                    for y in ys])
    keta = T("|1⟩", 22, PRETO).next_to([x0, yt, 0], LEFT, buff=0.15)
    vd = T("⋮", 26, PRETO).move_to([x0 - 0.5, (ys[0] + ys[1]) / 2, 0])
    cena.play(*[Create(f) for f in fios], FadeIn(kets), FadeIn(keta),
              FadeIn(vd), run_time=1.2 * VEL)

    # cada |0⟩ entra em SUPERPOSIÇÃO (cartão-gradiente nos slides)
    inis = VGroup(*[_carta_qubit(0.5, 0.66, 15).move_to([-4.55, y, 0])
                    for y in ys])
    cena.play(LaggedStart(*[FadeIn(i, scale=0.7) for i in inis],
                          lag_ratio=0.15), run_time=1.1 * VEL)

    # portas 2^(2ⁱ) (mod 21) no fio alvo, controladas de baixo para cima
    xs_cx = [-3.2, -1.3, 0.6, 3.4]
    expos = ["2⁰", "2¹", "2²", "2⁸"]
    ctrls = [ys[3], ys[2], ys[1], ys[0]]
    portas, plugues = VGroup(), VGroup()
    for xb, ex, yc in zip(xs_cx, expos, ctrls):
        px = _caixa_porta(ex).move_to([xb, yt, 0])
        dot = Dot([xb, yc, 0], radius=0.07, color=PRETO)
        lig = Line([xb, yc, 0], [xb, yt + 0.62, 0], color=PRETO,
                   stroke_width=2)
        portas.add(px)
        plugues.add(VGroup(dot, lig))
        cena.play(FadeIn(px), Create(lig), FadeIn(dot), run_time=0.6 * VEL)
    retic = T("…", 28, PRETO).move_to([2.15, yt, 0])
    cena.play(FadeIn(retic), run_time=0.4 * VEL)
    cena.wait(0.7 * VEL)

    # medimos o fio alvo: sai UM dos restos possíveis — c = 4 (slide 157)
    med = caixa_cinza(T("M", 20, PRETO), pad=0.14).move_to([4.9, yt, 0])
    c4 = T("4", 34, VERDE).next_to(fios[4].get_end(), RIGHT, buff=0.25)
    cena.play(FadeIn(med), run_time=0.6 * VEL)
    cena.play(Flash(med.get_center(), color=VERDE, flash_radius=0.5),
              FadeIn(c4, scale=1.4), run_time=0.9 * VEL)
    cena.wait(0.6 * VEL)

    # nos fios de cima entra a TRANSFORMADA QUÂNTICA DE FOURIER (slide 165)
    tqf = RoundedRectangle(corner_radius=0.12, width=1.7,
                           height=ys[0] - ys[3] + 0.9, stroke_width=0)
    tqf.set_fill(CAIXA2, opacity=1).move_to([4.6, (ys[0] + ys[3]) / 2, 0])
    rot_tqf = T("TQF", 30, PRETO).move_to(tqf)
    nq = formula(("N", PRETO), ("=", PRETO), ("2⁹", PRETO), ("=", PRETO),
                 ("512", PRETO), tamanho=24,
                 buff=0.08).next_to(tqf, UP, buff=0.2)
    cena.play(FadeIn(tqf), Write(rot_tqf), run_time=1.0 * VEL)
    cena.play(FadeIn(nq), run_time=0.7 * VEL)
    cena.wait(1.0 * VEL)

    cena.play(FadeOut(VGroup(eqc, fios, kets, keta, vd, inis, portas,
                             plugues, retic, med, c4, tqf, rot_tqf, nq)),
              run_time=0.8 * VEL)


def p10_ato1(cena):
    sub = VGroup(pot("2", "b", VERMELHO, AZUL, 30), T("≡", 30, PRETO),
                 T("4", 30, VERDE), fmod("21", 28), T("⇒", 30, PRETO),
                 T("b ∈ {2, 8, 14, 20, …}", 30, AZUL))
    sub.arrange(RIGHT, buff=0.14).to_edge(UP, buff=0.45)
    cena.play(Write(sub), run_time=1.2 * VEL)

    retaZ = NumberLine(x_range=[0, 32, 4], length=12, color=CINZA,
                       stroke_width=2, include_ticks=True, tick_size=0.06)
    retaZ.shift(0.55 * DOWN)
    rotZ = VGroup(*[T(str(v), 18, CINZA).next_to(retaZ.n2p(v), DOWN, buff=0.24)
                    for v in (0, 8, 16, 24, 32)])
    cena.play(Create(retaZ), FadeIn(rotZ), run_time=1.0 * VEL)

    def dente(reta, b, altura=0.5):
        return Line(reta.n2p(b) + altura * UP, reta.n2p(b),
                    color=VERDE, stroke_width=3.5)

    bs_zoom = [2, 8, 14, 20, 26]
    dentesZ = VGroup(*[dente(retaZ, b) for b in bs_zoom])
    rotulos_b = VGroup(*[T(str(b), 22, VERDE).next_to(d, UP, buff=0.12)
                         for b, d in zip(bs_zoom, dentesZ)])
    for d, rb in zip(dentesZ, rotulos_b):
        cena.play(GrowFromEdge(d, DOWN), FadeIn(rb), run_time=0.4 * VEL)

    chaves = VGroup()
    for b1, b2 in zip(bs_zoom[:-1], bs_zoom[1:]):
        ch = BraceBetweenPoints(retaZ.n2p(b1) + 1.0 * UP,
                                retaZ.n2p(b2) + 1.0 * UP,
                                direction=UP, color=LARANJA).scale(0.8)
        chaves.add(VGroup(ch, T("+6", 18, LARANJA).next_to(ch, UP, buff=0.07)))
    legenda_r = formula(("r", AMARELO), ("=", PRETO), ("6", AMARELO),
                        tamanho=30).next_to(retaZ, DOWN, buff=0.95)
    cena.play(LaggedStart(*[FadeIn(c) for c in chaves], lag_ratio=0.25),
              Write(legenda_r), run_time=1.6 * VEL)
    cena.wait(0.9 * VEL)

    # zoom-out: rótulos saem ANTES da compressão (sem sobreposição)
    cena.play(FadeOut(rotulos_b), FadeOut(chaves), FadeOut(rotZ),
              run_time=0.5 * VEL)
    retaF = NumberLine(x_range=[0, N, 64], length=12, color=CINZA,
                       stroke_width=2, include_ticks=True, tick_size=0.06)
    retaF.shift(0.55 * DOWN)
    rotF = VGroup(*[T(str(v), 18, CINZA).next_to(retaF.n2p(v), DOWN, buff=0.24)
                    for v in (0, 128, 256, 384, 512)])
    dentesF = VGroup(*[dente(retaF, b, 0.45) for b in bs_zoom])
    cena.play(ReplacementTransform(retaZ, retaF),
              *[ReplacementTransform(z, f) for z, f in zip(dentesZ, dentesF)],
              FadeIn(rotF), run_time=1.7 * VEL)
    resto = VGroup(*[dente(retaF, b, 0.45) for b in PENTE[5:]])
    cena.play(LaggedStart(*[GrowFromEdge(d, DOWN) for d in resto],
                          lag_ratio=0.01), run_time=2.2 * VEL)
    cena.wait(0.8 * VEL)

    cena.pente_grupo = VGroup(retaF, dentesF, resto)
    cena.play(FadeOut(VGroup(sub, legenda_r, rotF)),
              cena.pente_grupo.animate.scale(0.85).to_edge(UP, buff=0.35),
              run_time=1.3 * VEL)


def p10_ondas(cena):
    """Cada b compatível vira uma SENOIDE em k; a soma de todas (…) é o
    que a TQF devolve — picos nos múltiplos de N/r."""
    titulo = formula(("cada", CINZA), ("b", VERDE),
                     ("vira uma onda em", CINZA), ("k", LARANJA),
                     tamanho=22, buff=0.10)
    titulo.next_to(cena.pente_grupo, DOWN, buff=0.25)
    cena.play(FadeIn(titulo), run_time=0.8 * VEL)

    LX0, LX1 = -6.3, -1.0
    KMAX = 256.0

    def onda(b, y0, amp=0.30):
        return FunctionGraph(
            lambda x, b=b, y0=y0: y0 + amp * np.cos(
                TAU * b * ((x - LX0) / (LX1 - LX0)) * KMAX / N),
            x_range=[LX0, LX1], color=AZUL, stroke_width=2.2)

    ys_o = [1.15, 0.15, -0.85]
    bs_o = [2, 8, 14]
    ondas, rots_o = VGroup(), VGroup()
    for b, y in zip(bs_o, ys_o):
        o = onda(b, y)
        r = formula(("b", VERDE), ("=", PRETO), (str(b), VERDE),
                    tamanho=18, buff=0.05).move_to([LX0 - 0.02, y + 0.45, 0],
                                                   aligned_edge=LEFT)
        ondas.add(o)
        rots_o.add(r)
    mais = VGroup(T("+", 24, PRETO).move_to([(LX0 + LX1) / 2, 0.68, 0]),
                  T("+", 24, PRETO).move_to([(LX0 + LX1) / 2, -0.32, 0]))
    tres_pontos = T("⋮", 30, PRETO).move_to([(LX0 + LX1) / 2, -1.55, 0])
    for o, r in zip(ondas, rots_o):
        cena.play(Create(o), FadeIn(r), run_time=0.7 * VEL)
    cena.play(FadeIn(mais), FadeIn(tres_pontos), run_time=0.7 * VEL)

    # a soma de TODAS as ondas: interferência → picos em 0, N/r, 2N/r, …
    seta = Arrow([-0.75, -0.2, 0], [0.35, -0.2, 0], buff=0, color=PRETO,
                 stroke_width=3.5, max_tip_length_to_length_ratio=0.25)
    rot_s = T("soma", 20, CINZA).next_to(seta, UP, buff=0.10)
    SX0, SX1 = 0.7, 6.4
    soma = FunctionGraph(
        lambda x: -1.35 + 2.1 * amplitude((x - SX0) / (SX1 - SX0) * KMAX),
        x_range=[SX0, SX1, 0.01], color=CIANO, stroke_width=2.6)
    cena.play(GrowArrow(seta), FadeIn(rot_s), run_time=0.7 * VEL)
    cena.play(Create(soma), run_time=1.6 * VEL)
    picos = VGroup()
    for m, rot in ((0, "0"), (1, "N/r"), (2, "2N/r")):
        kx = SX0 + (SX1 - SX0) * (m * N / R) / KMAX
        picos.add(T(rot, 17, LARANJA).move_to([kx + 0.28, 0.95, 0]))
    cena.play(LaggedStart(*[FadeIn(p, shift=0.15 * DOWN) for p in picos],
                          lag_ratio=0.2), run_time=1.0 * VEL)
    cena.wait(1.2 * VEL)
    cena.play(FadeOut(VGroup(titulo, ondas, rots_o, mais, tres_pontos,
                             seta, rot_s, soma, picos)), run_time=0.7 * VEL)


def p10_ato2(cena):
    # O QUE É A LINHA QUE RODA: para um k fixo, cada b vira uma SETA
    # girada de 2π·b·k/N; a corrente é a soma de todas as setas
    giro = VGroup(
        formula(("para um", CINZA), ("k", LARANJA), ("fixo, cada", CINZA),
                ("b", VERDE), ("vira uma seta girada de", CINZA),
                ("2π·b·k/N", AZUL), tamanho=22, buff=0.10),
        formula(("a corrente azul é a SOMA das setas de todos os", CINZA),
                ("b", VERDE), tamanho=20, buff=0.10))
    giro.arrange(DOWN, buff=0.12).next_to(cena.pente_grupo, DOWN, buff=0.25)
    cena.play(FadeIn(giro), run_time=1.0 * VEL)

    RAIO = 1.75
    centro = np.array([-3.6, -1.45, 0.0])
    passo = RAIO / M
    guia = Circle(radius=RAIO, color="#c9d2dc", stroke_width=1.5)
    guia.move_to(centro)
    k_tr = ValueTracker(0.0)

    def cadeia_fasores():
        k = k_tr.get_value()
        pontos = [centro.copy()]
        p = centro.copy()
        for b in PENTE:
            th = TAU * b * k / N
            p = p + passo * np.array([np.cos(th), np.sin(th), 0.0])
            pontos.append(p.copy())
        cadeia = VMobject(stroke_color=AZUL, stroke_width=2.2,
                          stroke_opacity=0.8)
        cadeia.set_points_as_corners(pontos)
        mag = amplitude(k)
        cor = CIANO if mag > 0.6 else LARANJA
        return VGroup(cadeia, Line(centro, pontos[-1], color=cor,
                                   stroke_width=6),
                      Dot(pontos[-1], radius=0.06, color=cor))

    roleta = always_redraw(cadeia_fasores)
    leitura_k = always_redraw(lambda: T(
        f"k = {int(round(k_tr.get_value()))}", 34, LARANJA
    ).move_to([2.9, -0.55, 0], aligned_edge=LEFT))
    leitura_mag = always_redraw(lambda: T(
        f"|soma| = {amplitude(k_tr.get_value()):.2f}", 26,
        CIANO if amplitude(k_tr.get_value()) > 0.6 else CINZA
    ).move_to([2.9, -1.25, 0], aligned_edge=LEFT))
    barra_fundo = Rectangle(width=3.2, height=0.26, stroke_color="#c9d2dc",
                            stroke_width=1.5, fill_opacity=0)
    barra_fundo.move_to([2.9, -1.95, 0], aligned_edge=LEFT)
    barra = always_redraw(lambda: Rectangle(
        width=max(3.2 * amplitude(k_tr.get_value()), 1e-3), height=0.26,
        stroke_width=0, fill_opacity=1,
        fill_color=CIANO if amplitude(k_tr.get_value()) > 0.6 else LARANJA,
    ).move_to(barra_fundo.get_left(), aligned_edge=LEFT))

    cena.play(Create(guia), FadeIn(roleta), FadeIn(leitura_k),
              FadeIn(leitura_mag), Create(barra_fundo), FadeIn(barra),
              run_time=1.4 * VEL)
    cena.wait(0.8 * VEL)

    # k viaja SEM saltos: 0 → 3 → 82 → 85 (rótulos mínimos, só o essencial)
    m2 = T("setas desalinhadas → soma → 0", 24,
           VERMELHO).move_to([2.9, -2.75, 0], aligned_edge=LEFT)
    cena.play(k_tr.animate.set_value(3), FadeIn(m2),
              run_time=3.0 * VEL, rate_func=linear)
    cena.wait(0.6 * VEL)
    m2b = T("k = 4, 5, 6, …", 24, CINZA).move_to([2.9, -2.75, 0],
                                                 aligned_edge=LEFT)
    cena.play(FadeOut(m2), FadeIn(m2b), run_time=0.4 * VEL)
    cena.play(k_tr.animate.set_value(82), run_time=4.0 * VEL,
              rate_func=linear)
    m3 = formula(("k ≈ N/r", LARANJA), ("→ setas alinhadas!", CIANO),
                 tamanho=24, buff=0.12).move_to([2.9, -2.75, 0],
                                                aligned_edge=LEFT)
    cena.play(FadeOut(m2b), FadeIn(m3), run_time=0.5 * VEL)
    cena.play(k_tr.animate.set_value(85), run_time=4.0 * VEL,
              rate_func=rate_functions.ease_out_sine)
    cena.play(Flash(roleta[2].get_center(), color=CIANO, flash_radius=0.5),
              run_time=0.8 * VEL)
    cena.wait(1.0 * VEL)

    cena.k_tr = k_tr
    cena.grupo_roleta = VGroup(guia, barra_fundo)
    cena.grupo_vivo = [roleta, leitura_k, leitura_mag, barra]
    cena.textos_ato2 = VGroup(giro, m3)


def p10_ato3(cena):
    k_tr = cena.k_tr
    eixos = Axes(x_range=[0, N, 64], y_range=[0, 1.1, 0.5],
                 x_length=12.4, y_length=1.7,
                 axis_config={"color": CINZA, "stroke_width": 2,
                              "include_ticks": True, "tick_size": 0.04},
                 ).to_edge(DOWN, buff=0.45)
    rotulo_x = T("k", 22, CINZA).next_to(eixos.x_axis, RIGHT, buff=0.15)
    rotulo_y = T("prob.", 18, CINZA).next_to(eixos.y_axis, UP, buff=0.1)
    cena.play(FadeOut(cena.textos_ato2), Create(eixos),
              FadeIn(rotulo_x), FadeIn(rotulo_y), run_time=1.1 * VEL)

    curva = always_redraw(lambda: eixos.plot(
        amplitude, x_range=[0, max(k_tr.get_value(), 0.5), 0.5],
        color=CIANO, stroke_width=2.5, use_smoothing=False))
    ja_visto = eixos.plot(amplitude, x_range=[0, 85, 0.5], color=CIANO,
                          stroke_width=2.5, use_smoothing=False)
    cena.play(Create(ja_visto), run_time=1.1 * VEL)
    cena.add(curva)
    cena.remove(ja_visto)
    cena.play(k_tr.animate.set_value(N - 1), run_time=10.0 * VEL,
              rate_func=linear)

    curva_final = eixos.plot(amplitude, x_range=[0, N - 1, 0.5], color=CIANO,
                             stroke_width=2.5, use_smoothing=False)
    for m in cena.grupo_vivo:
        m.clear_updaters()
    curva.clear_updaters()
    cena.remove(curva)
    cena.add(curva_final)
    cena.play(FadeOut(VGroup(*cena.grupo_vivo)), FadeOut(cena.grupo_roleta),
              run_time=0.9 * VEL)

    marcas = VGroup()
    for mlt in range(1, 6):
        kx = mlt * N / R
        linha = DashedLine(eixos.c2p(kx, 0), eixos.c2p(kx, 1.05),
                           color=LARANJA, stroke_width=1.5, dash_length=0.08)
        rot = T(f"{mlt}·N/r", 16, LARANJA).next_to(linha, UP, buff=0.08)
        marcas.add(VGroup(linha, rot))
    cena.play(LaggedStart(*[Create(mv) for mv in marcas], lag_ratio=0.15),
              run_time=2.0 * VEL)
    cena.wait(1.2 * VEL)

    cena.eixos, cena.marcas = eixos, marcas
    cena.curva_final = VGroup(curva_final, rotulo_x, rotulo_y)


def p10_ato4(cena):
    eixos = cena.eixos
    seta = Arrow(eixos.c2p(85, 1.35), eixos.c2p(85, 1.0), buff=0,
                 color=LARANJA, stroke_width=5)
    med = T("k = 85", 26, LARANJA).next_to(seta, UP, buff=0.1)
    cena.play(GrowArrow(seta), Write(med),
              Flash(eixos.c2p(85, 1.0), color=LARANJA, flash_radius=0.4),
              run_time=1.3 * VEL)
    cena.wait(0.6 * VEL)
    cena.play(FadeOut(VGroup(cena.pente_grupo, cena.curva_final, cena.marcas,
                             eixos, seta, med)), run_time=0.9 * VEL)

    # cascata: cada linha se TRANSFORMA na conclusão seguinte
    linhas = VGroup(
        formula(("85", LARANJA), ("/", PRETO), ("512", PRETO), ("=", PRETO),
                ("x", PRETO), ("/", PRETO), ("r", AMARELO),
                tamanho=32, buff=0.10),
        formula(("85", LARANJA), ("/", PRETO), ("512", PRETO), ("≈", PRETO),
                ("1", PRETO), ("/", PRETO), ("6", PRETO),
                ("(frações contínuas)", CINZA), tamanho=28, buff=0.10),
        formula(("r", AMARELO), ("=", PRETO), ("6", AMARELO), tamanho=40),
        VGroup(pot("2", "6", VERMELHO, AMARELO, 30), T("≡", 30, PRETO),
               T("1", 30, VERDE), fmod("21", 28),
               T("✓", 30, VERDE)).arrange(RIGHT, buff=0.14),
        formula(("2⁶ − 1", PRETO), ("=", PRETO),
                ("(2³ − 1)(2³ + 1)", PRETO), ("=", PRETO),
                ("7 · 9", PRETO), tamanho=26, buff=0.10),
        VGroup(formula(("mdc(", PRETO), ("7", PRETO), (", ", PRETO),
                       ("21", LARANJA), (") =", PRETO), ("7", VERDE2),
                       tamanho=26, buff=0.08),
               formula(("mdc(", PRETO), ("9", PRETO), (", ", PRETO),
                       ("21", LARANJA), (") =", PRETO), ("3", ROSA),
                       tamanho=26, buff=0.08)).arrange(RIGHT, buff=0.7),
        formula(("21", LARANJA), ("=", PRETO), ("3", ROSA), ("×", PRETO),
                ("7", VERDE2), tamanho=42),
    ).arrange(DOWN, buff=0.34).move_to(0.15 * DOWN)
    for i, linha in enumerate(linhas):
        cena.play(Write(linha), run_time=1.0 * VEL)
        cena.wait((0.35 if i < len(linhas) - 1 else 0.9) * VEL)
    caixa = SurroundingRectangle(linhas[-1], color=VERDE, buff=0.22,
                                 corner_radius=0.15)
    cena.play(Create(caixa), run_time=0.9 * VEL)
    cena.wait(1.8 * VEL)


def parte10(cena):
    p10_fundamentos(cena)
    p10_circuito(cena)
    p10_ato1(cena)
    p10_ondas(cena)
    p10_ato2(cena)
    p10_ato3(cena)
    p10_ato4(cena)
