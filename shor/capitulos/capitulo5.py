# -*- coding: utf-8 -*-
from manim import *
import numpy as np

from ..paleta import *
from ..ferramentas import *

# ============================================================================
# CAPÍTULO 5 — Inverso modular (slides 37–57): busca, ciclo do 3, tabela
#   As barras vermelhas são CÓPIAS do número vermelho (a): 2·x são x
#   segmentos de tamanho 2; 3·x são x segmentos de tamanho 3 (slides 40–50).
#   Narração: C5N01 … C5N20 (roteiro_video2_aritmetica_modular.md)
# ============================================================================
def parte5(cena):
    eq = formula(("x", PRETO), ("≡", PRETO), ("1", VERDE), ("/", PRETO),
                 ("2", VERMELHO), *MOD("9"),
                 tamanho=38).to_edge(UP, buff=0.55)
    with narra(cena, "C5N01", 6.7):
        cena.play(Write(eq), run_time=1.0 * VEL)

    # numa reta feita só de inteiros não existe meio número: a reta do
    # capítulo 1 volta por um instante, um traço de meio número tenta
    # entrar e dá erro — Flash + ✗ + Wiggle, o mesmo fecho do capítulo 1
    reta = NumberLine(x_range=[0, 12, 1], length=10, color=CINZA,
                      include_ticks=True, tick_size=0.06).shift(1.9 * DOWN)
    n2r = reta.n2p
    meio = traco(n2r(0) + 0.5 * UP, n2r(0.5) + 0.5 * UP, VERMELHO)
    rmeio = T("½", 26, VERMELHO).next_to(meio, UP, buff=0.10)
    xmeio = T("✗", 30, VERMELHO).next_to(rmeio, RIGHT, buff=0.25)
    with narra(cena, "C5N02", 7.1):
        cena.play(Create(reta), run_time=1.0 * VEL)
        cena.play(Create(meio), FadeIn(rmeio), run_time=0.8 * VEL)
        cena.play(Flash(meio.get_end(), color=VERMELHO, flash_radius=0.35),
                  FadeIn(xmeio, scale=1.4), Wiggle(meio), run_time=1.0 * VEL)
        cena.play(FadeOut(meio), FadeOut(rmeio), FadeOut(xmeio),
                  FadeOut(reta), run_time=0.6 * VEL)

    eq2 = formula(("2", VERMELHO), ("·", PRETO), ("x", PRETO), ("≡", PRETO),
                  ("1", VERDE), *MOD("9"), tamanho=38).move_to(eq)
    with narra(cena, "C5N03", 7.9):
        cena.play(ReplacementTransform(eq, eq2), run_time=0.9 * VEL)
    so_fala(cena, "C5N04", 3.3)

    # testes na reta segmentada (slides 40–42): x segmentos de TAMANHO 2 —
    # as três filas correm emendadas, sob uma locução só
    u = 0.42
    x0 = -3.9
    linhas_teste = VGroup()
    with narra(cena, "C5N05", 6.3):
        for fila, x in enumerate((3, 4, 5)):
            y = 1.45 - fila * 1.0
            rot = formula(("2", VERMELHO), ("·", PRETO), (str(x), PRETO),
                          tamanho=28).move_to([-5.3, y + 0.2, 0])
            prod = 2 * x
            vs = VGroup(*[traco([x0 + i * 2 * u, y + 0.35, 0],
                                [x0 + (i + 1) * 2 * u, y + 0.35, 0],
                                VERMELHO, w=6) for i in range(x)])
            n9 = traco([x0, y, 0], [x0 + 9 * u, y, 0], LARANJA, w=6)
            grupo = VGroup(rot, vs, n9)
            if prod <= 9:
                resu = T(str(prod), 30,
                         CINZA).move_to([x0 + prod * u + 0.55, y + 0.35, 0])
                marca = T("✗", 30, VERMELHO).next_to(resu, RIGHT, buff=0.25)
                grupo.add(resu, marca)
            else:
                sobra = traco([x0 + 9 * u, y, 0], [x0 + prod * u, y, 0],
                              VERDE, w=8, gap=0.03)
                resu = T("1", 30, VERDE).move_to([x0 + prod * u + 0.5, y, 0])
                marca = T("✓", 30, VERDE).next_to(resu, RIGHT, buff=0.25)
                grupo.add(sobra, resu, marca)
            # as cópias do 2 NASCEM do 2 vermelho da equação
            cena.play(FadeIn(rot), Create(n9), run_time=0.5 * VEL)
            cena.play(LaggedStart(*[Create(s) for s in vs], lag_ratio=0.2),
                      run_time=0.6 * VEL)
            cena.play(*[FadeIn(m) for m in grupo[3:]], run_time=0.6 * VEL)
            linhas_teste.add(grupo)

    def eq_inv(n):
        return formula(("2", VERMELHO), ("·", PRETO), ("5", PRETO),
                       ("≡", PRETO), ("1", VERDE), *MOD(str(n)),
                       tamanho=38).move_to(eq2)

    eq3 = eq_inv(9)
    with narra(cena, "C5N06", 3.3):
        cena.play(ReplacementTransform(eq2, eq3), run_time=0.9 * VEL)

    par = formula(("5", PRETO), ("≡", PRETO), ("1", VERDE), ("/", PRETO),
                  ("2", VERMELHO), ("e", CINZA), ("2", VERMELHO),
                  ("≡", PRETO), ("1", VERDE), ("/", PRETO), ("5", PRETO),
                  *MOD("9"), tamanho=30).move_to([0, -2.4, 0])
    with narra(cena, "C5N07", 6.7):
        cena.play(Write(par), run_time=1.2 * VEL)

    # ---- procurar assim custa o TAMANHO DO MÓDULO (quarto elo da
    # corrente): a reta laranja se estica e as filas vermelhas se
    # multiplicam para baixo, encolhendo até escapar pela borda inferior
    ecos = VGroup()
    y_e, gap = -1.2, 0.75
    for i in range(8):
        s = max(0.85 ** i, 0.28)
        L = (9 + 3 * i) * u
        w_ = max(6.0 * 0.88 ** i, 2.5)
        lin = VGroup(traco([x0, y_e, 0], [x0 + L, y_e, 0], LARANJA, w=w_))
        blocos = VGroup(*[traco([x0 + j * 2 * u, y_e + 0.32 * s, 0],
                                [x0 + (j + 1) * 2 * u, y_e + 0.32 * s, 0],
                                VERMELHO, w=w_)
                          for j in range(int(np.ceil(L / (2 * u))))])
        ecos.add(VGroup(lin, blocos))
        y_e -= gap
        gap *= 0.82
    with narra(cena, "C5N08", 8.8):
        cena.play(Indicate(eq3[6], color=LARANJA, scale_factor=1.6),
                  run_time=0.9 * VEL)
        # o módulo cresce MUITO em cena (9 → 27 → 81 → 243) enquanto as
        # filas se multiplicam em ondas; o par sai antes da cascata descer
        eq_v = eq3
        for n, onda, extra in ((27, ecos[0:3], [FadeOut(par)]),
                               (81, ecos[3:6], []),
                               (243, ecos[6:8], [])):
            eq_n = eq_inv(n)
            cena.play(ReplacementTransform(eq_v, eq_n), *extra,
                      LaggedStart(*[FadeIn(e, shift=0.3 * DOWN)
                                    for e in onda], lag_ratio=0.2),
                      run_time=1.0 * VEL)
            eq_v = eq_n
        # e volta ao caso pequeno: 2 · 5 ≡ 1 (mod 9) de novo
        eq3 = eq_inv(9)
        cena.play(ReplacementTransform(eq_v, eq3), run_time=0.8 * VEL)

    # ---- o algoritmo de Euclides, correndo por baixo, SEM a fala comentar:
    # o nome do algoritmo fica escrito entre a equação e a demonstração,
    # e a escada roda embaixo — o módulo laranja medido pelo vermelho, a
    # sobra virando a régua do passo seguinte, até o pedaço de tamanho um.
    # Roda rápido e sai antes do eq3 → eq4.
    titulo_euc = T("Algoritmo de Euclides estendido", 30).move_to([0, 1.9, 0])
    xe = -1.9
    esc1_mod = traco([xe, 0.2, 0], [xe + 9 * u, 0.2, 0], LARANJA, w=6)
    esc1_reg = VGroup(*[traco([xe + i * 2 * u, 0.5, 0],
                              [xe + (i + 1) * 2 * u, 0.5, 0],
                              VERMELHO, w=6) for i in range(4)])
    esc1_sob = traco([xe + 8 * u, 0.5, 0], [xe + 9 * u, 0.5, 0],
                     VERDE, w=8, gap=0.03)
    esc2_mod = traco([xe, -0.9, 0], [xe + 2 * u, -0.9, 0], VERMELHO, w=6)
    esc2_reg = VGroup(*[traco([xe + i * u, -0.6, 0],
                              [xe + (i + 1) * u, -0.6, 0],
                              VERDE, w=6, gap=0.03) for i in range(2)])
    esc3 = traco([xe, -1.8, 0], [xe + u, -1.8, 0], VERDE, w=8, gap=0.03)
    esc3_rot = T("1", 24, VERDE).next_to(esc3, RIGHT, buff=0.20)
    escada = VGroup(esc1_mod, esc1_reg, esc1_sob, esc2_mod, esc2_reg,
                    esc3, esc3_rot)
    with narra(cena, "C5N09", 6.3):
        # as filas e os ecos saem: o palco é da escada
        cena.play(FadeOut(linhas_teste), FadeOut(ecos),
                  run_time=0.5 * VEL)
        cena.play(Write(titulo_euc), run_time=0.8 * VEL)
        cena.play(Create(esc1_mod), run_time=0.4 * VEL)
        cena.play(LaggedStart(*[Create(s) for s in esc1_reg], lag_ratio=0.2),
                  run_time=0.6 * VEL)
        cena.play(Create(esc1_sob), run_time=0.4 * VEL)
        # a régua do passo seguinte é a sobra do passo anterior
        cena.play(TransformFromCopy(esc1_reg[0], esc2_mod), run_time=0.4 * VEL)
        cena.play(TransformFromCopy(esc1_sob, esc2_reg[0]),
                  TransformFromCopy(esc1_sob, esc2_reg[1]),
                  run_time=0.5 * VEL)
        cena.play(TransformFromCopy(esc2_reg[1], esc3), FadeIn(esc3_rot),
                  run_time=0.4 * VEL)
        cena.play(FadeOut(escada), FadeOut(titulo_euc), run_time=0.5 * VEL)

    # contra-exemplo NAS RETAS (slides 45–51): 3·x até 3·6 — a REPETIÇÃO
    eq4 = formula(("3", VERMELHO), ("·", PRETO), ("x", PRETO), ("≡", PRETO),
                  ("1", VERDE), *MOD("9"), tamanho=38).move_to(eq3)
    with narra(cena, "C5N10", 7.1):
        cena.play(ReplacementTransform(eq3, eq4), run_time=0.9 * VEL)

    # as seis filas do contra-exemplo correm emendadas, num bloco só
    linhas3 = VGroup()
    with narra(cena, "C5N11", 3.8):
        for fila, x in enumerate((1, 2, 3, 4, 5, 6)):
            y = 1.6 - fila * 0.72
            rot = formula(("3", VERMELHO), ("·", PRETO), (str(x), PRETO),
                          tamanho=28).move_to([-5.3, y + 0.2, 0])
            vs = VGroup(*[traco([x0 + i * 3 * u, y + 0.35, 0],
                                [x0 + (i + 1) * 3 * u, y + 0.35, 0],
                                VERMELHO, w=6) for i in range(x)])
            n9 = traco([x0, y, 0], [x0 + 9 * u, y, 0], LARANJA, w=6)
            prod = 3 * x
            resto = prod % 9
            resu = T(str(resto), 30,
                     CINZA if resto else VERMELHO).move_to(
                         [x0 + max(prod, 9) * u + 0.55, y + 0.35, 0])
            marca = T("✗", 30, VERMELHO).next_to(resu, RIGHT, buff=0.25)
            grupo = VGroup(rot, vs, n9, resu, marca)
            cena.play(FadeIn(rot), Create(n9),
                      LaggedStart(*[Create(s) for s in vs], lag_ratio=0.2),
                      FadeIn(resu), FadeIn(marca), run_time=0.6 * VEL)
            linhas3.add(grupo)

    # o padrão se repete para sempre: 3, 6, 0, 3, 6, 0, … nunca dá 1
    ciclo = VGroup(*[T(s, 30, VERMELHO if s == "…" else CINZA)
                     for s in ["3", "6", "0", "3", "6", "0", "…"]])
    ciclo.arrange(RIGHT, buff=0.5).move_to([0, -2.75, 0])
    with narra(cena, "C5N12", 5.8):
        cena.play(LaggedStart(
            *[TransformFromCopy(linhas3[j][3], ciclo[j]) for j in range(6)],
            FadeIn(ciclo[6], shift=0.2 * DOWN),
            lag_ratio=0.2), run_time=1.8 * VEL)

    xis = T("✗", 44, VERMELHO).next_to(eq4, RIGHT, buff=0.4)
    with narra(cena, "C5N13", 5.4):
        cena.play(FadeIn(xis, scale=1.5), run_time=0.8 * VEL)

    mdc3 = formula(("mdc(", PRETO), ("3", VERMELHO), (", ", PRETO),
                   ("9", LARANJA), (") = 3", PRETO),
                   tamanho=30, buff=0.08).move_to([0, -3.4, 0])
    with narra(cena, "C5N14", 5.0):
        cena.play(Write(mdc3), run_time=1.0 * VEL)

    # a tabela (slides 55–57)
    tam = 0.52
    canto = np.array([-5.9, 2.35, 0.0])

    def ponto(i, j):
        return canto + np.array([(j + 1) * tam, -(i + 1) * tam, 0.0])

    head_c = VGroup(*[T(str(j), 22, AZUL).move_to(canto + [(j + 1) * tam, 0, 0])
                      for j in range(9)])
    head_l = VGroup(*[T(str(i), 22, VERMELHO)
                      .move_to(canto + [0, -(i + 1) * tam, 0])
                      for i in range(9)])
    lin_h = Line(canto + [0.55 * tam, -0.5 * tam, 0],
                 canto + [9.5 * tam, -0.5 * tam, 0], color=PRETO,
                 stroke_width=1.5)
    lin_v = Line(canto + [0.55 * tam, -0.5 * tam, 0],
                 canto + [0.55 * tam, -9.5 * tam, 0], color=PRETO,
                 stroke_width=1.5)
    titulo_tab = T("Tabela multiplicativa (mod 9)", 26).move_to([-3.3, 3.1, 0])
    # COMO a tabela funciona, ANTES de preenchê-la:
    # cada célula é linha · coluna (mod 9)
    como = formula(("célula", PRETO), ("=", PRETO), ("linha", VERMELHO),
                   ("·", PRETO), ("coluna", AZUL), *MOD("9"),
                   tamanho=24, buff=0.10).move_to([3.6, 1.9, 0])
    with narra(cena, "C5N15", 7.5):
        cena.play(FadeOut(linhas3), FadeOut(ciclo), FadeOut(mdc3),
                  FadeOut(xis), FadeOut(eq4), run_time=0.6 * VEL)
        cena.play(FadeIn(titulo_tab), FadeIn(head_c), FadeIn(head_l),
                  Create(lin_h), Create(lin_v), run_time=0.9 * VEL)
        cena.play(Write(como), run_time=1.0 * VEL)

    # exemplo — justamente o par das retas: linha 2, coluna 5 — e a tabela
    # inteira nascendo da célula, tudo emendado num bloco só
    ex25 = formula(("2", VERMELHO), ("·", PRETO), ("5", AZUL), ("=", PRETO),
                   ("10", PRETO), ("≡", PRETO), ("1", VERDE), *MOD("9"),
                   tamanho=24, buff=0.10).move_to([3.6, 1.25, 0])
    linhas_cel = [VGroup(*[T(str((i * j) % 9), 22, PRETO).move_to(ponto(i, j))
                           for j in range(9)]) for i in range(9)]
    demais = [VGroup(*[c for j, c in enumerate(l) if not (i == 2 and j == 5)])
              for i, l in enumerate(linhas_cel)]
    with narra(cena, "C5N16", 7.1):
        cena.play(Indicate(head_l[2], color=VERMELHO),
                  Indicate(head_c[5], color=AZUL), Write(ex25),
                  run_time=1.2 * VEL)
        cena.play(ReplacementTransform(ex25[6].copy(), linhas_cel[2][5]),
                  run_time=0.9 * VEL)
        cena.play(LaggedStart(*[FadeIn(l) for l in demais], lag_ratio=0.1),
                  run_time=2.0 * VEL)

    # quando a·b ≡ 1 (mod 9), a e b são INVERSOS
    inv1 = formula(("a", VERMELHO), ("·", PRETO), ("b", AZUL), ("≡", PRETO),
                   ("1", VERDE), *MOD("9"),
                   tamanho=26, buff=0.10).move_to([3.6, 1.7, 0])
    inv2 = T("⇒ a e b são inversos", 24, PRETO).next_to(inv1, DOWN, buff=0.25)
    circulos = VGroup(*[Circle(radius=0.21, color=VERDE, stroke_width=2.5)
                        .move_to(ponto(i, j))
                        for i in range(1, 9) for j in range(1, 9)
                        if (i * j) % 9 == 1])
    with narra(cena, "C5N17", 10.4):
        cena.play(FadeOut(como), FadeOut(ex25), run_time=0.5 * VEL)
        cena.play(LaggedStart(*[Create(c) for c in circulos], lag_ratio=0.12),
                  Write(inv1), run_time=1.5 * VEL)
        cena.play(FadeIn(inv2), run_time=0.7 * VEL)

    # RESSALTA o exemplo das retas: 2 e 5 são inversos
    rec1 = formula(("2", VERMELHO), ("·", PRETO), ("5", AZUL), ("≡", PRETO),
                   ("1", VERDE), ("→ inversos", VERDE), ("✓", VERDE),
                   tamanho=22, buff=0.10).move_to([3.6, 0.5, 0])
    with narra(cena, "C5N18", 3.8):
        cena.play(Write(rec1), Indicate(linhas_cel[2][5], color=VERDE),
                  Indicate(linhas_cel[5][2], color=VERDE), run_time=1.2 * VEL)

    # VISUAL: linhas sem nenhum "1" = números NÃO inversíveis (mod 9) — e,
    # emendado, o 3 das retas: o ciclo 3, 6, 0 nunca alcançou o 1
    mortos = VGroup(*[SurroundingRectangle(linhas_cel[i], color=VERMELHO,
                                           buff=0.06, corner_radius=0.08,
                                           stroke_width=2)
                      for i in (0, 3, 6)])
    m_rot = formula(("0, 3, 6", VERMELHO), (": não inversíveis", PRETO),
                    tamanho=24, buff=0.12).move_to([3.6, -0.5, 0])
    rec2 = formula(("3", VERMELHO), ("· x", PRETO), ("nunca ≡", PRETO),
                   ("1", VERDE), ("✗", VERMELHO),
                   tamanho=22, buff=0.10).move_to([3.6, -1.05, 0])
    with narra(cena, "C5N19", 9.2):
        cena.play(*[linhas_cel[i].animate.set_opacity(0.2) for i in (0, 3, 6)],
                  *[head_l[i].animate.set_opacity(0.3) for i in (0, 3, 6)],
                  LaggedStart(*[Create(m) for m in mortos], lag_ratio=0.2),
                  run_time=1.4 * VEL)
        cena.play(FadeIn(m_rot), run_time=0.7 * VEL)
        cena.play(Write(rec2), Indicate(mortos[1], color=VERMELHO),
                  run_time=1.0 * VEL)

    # conclusão em duas linhas (sem cortar na borda)
    c1 = formula(("mdc(", PRETO), ("a", VERMELHO), (", ", PRETO),
                 ("9", LARANJA), (") = 1", PRETO),
                 tamanho=26, buff=0.08)
    c2 = formula(("⇔", PRETO), ("a", VERMELHO), ("inversível", VERDE),
                 tamanho=26, buff=0.14)
    concl = VGroup(c1, c2).arrange(DOWN, buff=0.22).move_to([3.6, -1.9, 0])
    caixa = SurroundingRectangle(concl, color=VERDE, buff=0.2,
                                 corner_radius=0.12)
    with narra(cena, "C5N20", 6.7):
        cena.play(Write(concl), Create(caixa), run_time=1.2 * VEL)
