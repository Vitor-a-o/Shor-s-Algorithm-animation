# -*- coding: utf-8 -*-
from manim import *
import numpy as np

from ..paleta import *
from ..ferramentas import *

# ============================================================================
# CAPÍTULO 9 — Ordem Modular NA TABELA multiplicativa (slides 107–119)
#   Tabela mod 9, base a = 4: o zigue-zague verde 1 → 4 → 7 → 1 mostra
#   que multiplicar por a é saltar para a linha 4 na coluna do valor
#   atual. 3 passos para voltar ao 1 ⇒ r = 3.
#   Depois, no C9N13, a MESMA tabela recebe a base 5: o ciclo passa pelos
#   seis restos invertíveis antes de voltar ao 1 — r = 6 = φ(9), o pior
#   caso acontecendo. E no C9N14 o módulo cresce e só sobra malha.
# ============================================================================
_TAM = 0.52                              # lado da célula da tabela mod 9
_CANTO = np.array([-6.0, 2.2, 0.0])      # célula (0, 0): os cabeçalhos
_MEIO_X = _CANTO[0] + 5 * _TAM           # eixo vertical do miolo da grade
_LADO = 9 * _TAM                         # lado do quadrado do miolo


def _malha(m, w=0.9):
    """A malha da tabela (mod m) inscrita no MESMO quadrado que o miolo da
    tabela mod 9 ocupa: o quadrado é fixo, quem cresce é o número de células.
    É a grade que adensa no C9N14, irmã da do C8N39."""
    p = _LADO / m
    a = _CANTO + np.array([0.5 * _TAM, -0.5 * _TAM, 0.0])
    return VGroup(
        *[Line(a + [0, -k * p, 0], a + [_LADO, -k * p, 0], color=CINZA,
               stroke_width=w) for k in range(m + 1)],
        *[Line(a + [k * p, 0, 0], a + [k * p, -_LADO, 0], color=CINZA,
               stroke_width=w) for k in range(m + 1)])


def parte9(cena):
    # slide 108: tabela multiplicativa + exponenciação modular
    eq = VGroup(T("c", 34, VERDE), T("≡", 34, PRETO),
                pot("4", "b", VERMELHO, AZUL, 34), fmod("9", 32))
    eq.arrange(RIGHT, buff=0.15).to_edge(UP, buff=0.4)
    with narra(cena, "C9N01", 8.5):
        cena.play(Write(eq), run_time=1.0 * VEL)
    escolha = formula(("n", LARANJA), ("=", PRETO), ("9", LARANJA),
                      ("e", CINZA), ("a", VERMELHO), ("=", PRETO),
                      ("4", VERMELHO), ("inversível", CINZA),
                      tamanho=22, buff=0.12).move_to([3.6, 2.55, 0])
    with narra(cena, "C9N02", 8.2):
        cena.play(FadeIn(escolha), run_time=0.7 * VEL)
        # "tem inverso": a condição do capítulo 5 já está escrita ali
        cena.play(Indicate(escolha[7], color=VERMELHO), run_time=0.8 * VEL)

    # a tabela mod 9 (slide 109), com a seta vermelha na linha do 4
    tam, canto = _TAM, _CANTO

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
    linhas_cel = [VGroup(*[T(str((i * j) % 9), 22, PRETO).move_to(ponto(i, j))
                           for j in range(9)]) for i in range(9)]
    # a grade e o miolo num movimento só: a tabela entra como UMA peça
    with narra(cena, "C9N03", 6.1):
        cena.play(LaggedStart(
            AnimationGroup(FadeIn(head_c), FadeIn(head_l), Create(lin_h),
                           Create(lin_v), run_time=0.9 * VEL),
            LaggedStart(*[FadeIn(l) for l in linhas_cel], lag_ratio=0.1,
                        run_time=1.8 * VEL),
            lag_ratio=0.6))
    seta4 = Arrow(canto + [-1.05, -5 * tam, 0], canto + [-0.35, -5 * tam, 0],
                  buff=0, color=VERMELHO, stroke_width=5,
                  max_tip_length_to_length_ratio=0.4)
    with narra(cena, "C9N04", 2.6):
        cena.play(GrowArrow(seta4), Indicate(head_l[4], color=VERMELHO),
                  run_time=0.8 * VEL)

    # slide 110: objetivo — todos os restos c possíveis, um b de cada vez
    def circ(i, j):
        return Circle(radius=0.22, color=VERDE,
                      stroke_width=2.5).move_to(ponto(i, j))

    # b = 0: c = 1 (slide 111)
    f0 = VGroup(pot("4", "0", VERMELHO, AZUL, 26), T("≡", 26, PRETO),
                T("1", 26, VERDE), fmod("9", 24))
    f0.arrange(RIGHT, buff=0.12).move_to([3.6, 1.75, 0])
    c00 = circ(1, 1)
    with narra(cena, "C9N05", 3.6):
        cena.play(Create(c00), Write(f0), run_time=0.9 * VEL)

    # slide 112: somar 1 em b = multiplicar o resultado anterior por 4
    nota = T("somar 1 em b = multiplicar por 4", 20,
             CINZA).move_to([3.6, 1.2, 0])
    with narra(cena, "C9N06", 7.5):
        cena.play(FadeIn(nota), run_time=0.7 * VEL)

    # o ZIGUE-ZAGUE dos slides 113–115: descer para a linha 4 multiplica;
    # o resultado vira a coluna do próximo salto
    passos = [(1, 1, 4), (4, 1, None), (1, 4, 4), (4, 4, None),
              (1, 7, 4), (4, 7, None)]
    fs = [VGroup(pot("4", "1", VERMELHO, AZUL, 26), T("≡", 26, PRETO),
                 T("4", 26, VERDE), fmod("9", 24)),
          VGroup(pot("4", "2", VERMELHO, AZUL, 26), T("≡", 26, PRETO),
                 T("7", 26, VERDE), fmod("9", 24)),
          VGroup(pot("4", "3", VERMELHO, AZUL, 26), T("≡", 26, PRETO),
                 T("1", 26, VERDE), fmod("9", 24), T("✓", 26, VERDE))]
    for k, f in enumerate(fs):
        f.arrange(RIGHT, buff=0.12).move_to([3.6, 0.55 - 0.62 * k, 0])
    zig = VGroup(c00)
    trilha = VGroup()           # o caminho do ciclo, para as voltas extras

    def _passo(k):
        """Um degrau do zigue-zague: desce até a linha da base, escreve a
        potência e sobe de volta na coluna do resultado."""
        j = (1, 4, 7)[k]
        desce = Arrow(ponto(1, j) + 0.22 * DOWN, ponto(4, j) + 0.24 * UP,
                      buff=0, color=VERDE, stroke_width=2.5,
                      max_tip_length_to_length_ratio=0.18)
        alvo = circ(4, j)
        cena.play(GrowArrow(desce), Create(alvo), run_time=0.7 * VEL)
        cena.play(Write(fs[k]), run_time=0.7 * VEL)
        zig.add(desce, alvo)
        trilha.add(Line(ponto(1, j) + 0.22 * DOWN, ponto(4, j) + 0.24 * UP))
        if k < 2:
            prox_j = (4, 7)[k]
            sobe = ArcBetweenPoints(ponto(4, j) + 0.24 * RIGHT,
                                    ponto(1, prox_j) + 0.24 * DOWN,
                                    angle=-0.55, color=VERDE,
                                    stroke_width=2.0)
            topo = circ(1, prox_j)
            cena.play(Create(sobe), Create(topo), run_time=0.7 * VEL)
            zig.add(sobe, topo)
            trilha.add(sobe.copy())

    # os dois primeiros degraus inteiros sob uma fala só: o with envolve o
    # laço, não cada iteração dele
    with narra(cena, "C9N07", 6.2):
        for k in range(2):
            _passo(k)

    # o terceiro degrau é o que devolve o 1 — o Flash pertence a ele
    with narra(cena, "C9N08", 4.7):
        _passo(2)
        cena.play(Flash(ponto(4, 7), color=VERDE, flash_radius=0.5),
                  run_time=0.7 * VEL)

    # o CICLO SE FECHA: do 1 reencontrado, de volta ao ponto de partida
    fecha = ArcBetweenPoints(ponto(4, 7) + 0.24 * DOWN,
                             ponto(1, 1) + 0.26 * LEFT, angle=-1.3,
                             color=VERDE, stroke_width=2.0)
    # slide 118: cada VOLTA COMPLETA no ciclo soma 3 ao expoente —
    # surgem 4⁶, 4⁹, … todos congruentes a 1
    mult = VGroup(T("1", 26, VERDE), T("≡", 26, PRETO),
                  pot("4", "3", VERMELHO, AZUL, 26), T("≡", 26, PRETO),
                  pot("4", "6", VERMELHO, AZUL, 26), T("≡", 26, PRETO),
                  pot("4", "9", VERMELHO, AZUL, 26), fmod("9", 24))
    mult.arrange(RIGHT, buff=0.12).move_to([3.6, -1.65, 0])
    with narra(cena, "C9N09", 5.1):
        cena.play(Create(fecha), Indicate(c00, color=VERDE),
                  run_time=1.0 * VEL)
        cena.play(Write(VGroup(mult[0], mult[1], mult[2])), run_time=0.8 * VEL)
    trilha.add(fecha.copy())
    zig.add(fecha)

    def volta_no_ciclo():
        return Succession(*[ShowPassingFlash(
            s.copy().set_stroke(AMARELO, width=6), time_width=0.7)
            for s in trilha])

    def _sobe_expoentes(volta):
        """A volta soma 3 a cada expoente da coluna do zigue-zague:
        4¹,4²,4³ viram 4⁴,4⁵,4⁶ e depois 4⁷,4⁸,4⁹ — as congruências andam
        junto com o flash amarelo. Devolve (animações, trocas a aplicar
        no VGroup depois do play)."""
        anims, trocas = [], []
        for k, f in enumerate(fs):
            velho = f[0][1]
            novo = T(str(k + 1 + 3 * volta), velho.font_size,
                     AZUL).move_to(velho, aligned_edge=DL)
            anims.append(ReplacementTransform(velho, novo))
            trocas.append((f[0], velho, novo))
        return anims, trocas

    def _troca(trocas):
        for grupo, velho, novo in trocas:
            grupo.remove(velho)
            grupo.add(novo)

    # as duas voltas extras correm sob uma fala só — o "e assim por diante"
    with narra(cena, "C9N10", 5.6):
        anims, trocas = _sobe_expoentes(1)
        cena.play(volta_no_ciclo(), *anims, run_time=1.3 * VEL)
        _troca(trocas)
        cena.play(FadeIn(mult[3]), TransformFromCopy(mult[2], mult[4]),
                  run_time=0.8 * VEL)
        anims, trocas = _sobe_expoentes(2)
        cena.play(volta_no_ciclo(), *anims, run_time=1.3 * VEL)
        _troca(trocas)
        cena.play(FadeIn(mult[5]), TransformFromCopy(mult[4], mult[6]),
                  FadeIn(mult[7]), run_time=0.8 * VEL)

    # slides 116–117: 3 passos para fechar o ciclo ⇒ o r NASCE do expoente 3
    rdef = VGroup(T("r", 38, AMARELO), T("=", 38, PRETO),
                  T("3", 38, AMARELO))
    rdef.arrange(RIGHT, buff=0.16).move_to([3.6, -2.5, 0])
    with narra(cena, "C9N11", 2.4):
        cena.play(Write(rdef[0]), Write(rdef[1]),
                  TransformFromCopy(mult[2][1], rdef[2]), run_time=0.9 * VEL)

    # slide 117 (definição) + slide 119 (pior caso r = φ(n))
    d1 = formula(("ordem modular de", PRETO), ("a", VERMELHO),
                 ("módulo", PRETO), ("n", LARANJA), (":", PRETO),
                 tamanho=26, buff=0.14)
    d2 = formula(("o menor", PRETO), ("r", AMARELO), ("tal que", PRETO),
                 tamanho=24, buff=0.14)
    d3 = VGroup(pot("a", "r", VERMELHO, AMARELO, 30), T("≡", 30, PRETO),
                T("1", 30, VERDE), fmod("n", 28))
    d3.arrange(RIGHT, buff=0.15)
    d4 = formula(("pior caso:", CINZA), ("r", AMARELO), ("=", CINZA),
                 ("φ(", CINZA), ("n", LARANJA), (")", CINZA),
                 tamanho=20, buff=0.08)
    caixa_d = VGroup(d1, d2, d3, d4).arrange(DOWN, buff=0.24)
    # sem a tabela e sem a coluna do exemplo, a definição não divide mais a
    # tela com ninguém: ela nasce no centro
    caixa_d.move_to(ORIGIN)
    # a borda já abraça o d4, que só entra no C9N13 — assim o layout não se
    # mexe quando o pior caso chegar
    borda = SurroundingRectangle(caixa_d, color=VERDE, buff=0.25,
                                 corner_radius=0.12)

    # A VIRADA, o mesmo pouso do C6N12 e do C7N13: a tabela e a coluna do
    # exemplo saem enquanto o geral nasce, num play único. O rdef é a última
    # coisa a sumir — e o r dele não morre: viaja por cópia para os dois
    # lugares onde a definição o usa, o d2 e o expoente do d3
    corpo = VGroup(d1, d2[0], d2[2], d3[0][0], d3[1], d3[2], d3[3])
    saida = AnimationGroup(
        FadeOut(head_c), FadeOut(head_l), FadeOut(lin_h), FadeOut(lin_v),
        *[FadeOut(l) for l in linhas_cel], FadeOut(seta4), FadeOut(zig),
        FadeOut(eq), FadeOut(escolha), FadeOut(f0), FadeOut(nota),
        *[FadeOut(f) for f in fs], FadeOut(mult),
        Write(corpo), Create(borda),
        TransformFromCopy(rdef[0], d2[1]),
        TransformFromCopy(rdef[0], d3[0][1]),
        run_time=1.2 * VEL,
    )
    with narra(cena, "C9N12", 2.4):
        cena.play(LaggedStart(saida, FadeOut(rdef, run_time=0.6 * VEL),
                              lag_ratio=0.4))

    # ------------------------------------------------------------------------
    # C9N13 — o PIOR CASO ACONTECENDO, na mesma tabela e com outra base. Com
    # a = 5 o ciclo não fecha em 3 passos: ele passa pelos SEIS restos
    # invertíveis mod 9 antes de devolver o 1 — r = 6 = φ(9). A definição sai
    # do centro e vira coluna da direita para a tabela voltar ao lugar dela.
    # ------------------------------------------------------------------------
    bloco = VGroup(borda, caixa_d)            # a definição, para mover junto
    tab9 = VGroup(head_c, head_l, *linhas_cel)
    phi4 = VGroup(d4[3], d4[4], d4[5])        # o φ(n) do pior caso
    leg5 = VGroup(formula(("a", VERMELHO), ("=", PRETO), ("5", VERMELHO),
                          tamanho=22, buff=0.12),
                  fmod("9", 22)).arrange(RIGHT, buff=0.20)
    leg5.move_to([_MEIO_X, 2.72, 0])
    seta5 = Arrow(canto + [-1.05, -6 * tam, 0], canto + [-0.35, -6 * tam, 0],
                  buff=0, color=VERMELHO, stroke_width=5,
                  max_tip_length_to_length_ratio=0.4)
    ini5 = circ(1, 1)
    # 1 → 5 → 7 → 8 → 4 → 2 → 1: seis degraus, um por resto invertível. A fala
    # não lê nenhum deles, então aqui não entra congruência escrita: o que a
    # tela mostra é o COMPRIMENTO do caminho
    ciclo5 = [1, 5, 7, 8, 4, 2, 1]
    caminho5 = VGroup()
    degraus = []
    for k in range(6):
        j, prox = ciclo5[k], ciclo5[k + 1]
        desce = Arrow(ponto(1, j) + 0.22 * DOWN, ponto(5, j) + 0.24 * UP,
                      buff=0, color=VERDE, stroke_width=2.5,
                      max_tip_length_to_length_ratio=0.18)
        alvo = circ(5, j)
        degraus.append(AnimationGroup(GrowArrow(desce), Create(alvo)))
        caminho5.add(desce, alvo)
        # o arco sai pelo lado para onde vai: a ida atravessa a tabela para a
        # direita e a volta desce de novo pela esquerda, até o 1 do começo
        pd = prox > j
        sobe = ArcBetweenPoints(ponto(5, j) + 0.24 * (RIGHT if pd else LEFT),
                                ponto(1, prox) + 0.24 * DOWN,
                                angle=-0.55 if pd else 0.55,
                                color=VERDE, stroke_width=2.0)
        if k == 5:
            degraus.append(AnimationGroup(Create(sobe),
                                          Indicate(ini5, color=VERDE)))
            caminho5.add(sobe)
        else:
            topo = circ(1, prox)
            degraus.append(AnimationGroup(Create(sobe), Create(topo)))
            caminho5.add(sobe, topo)
    # a contagem do pior caso, embaixo da tabela: r não é menor que φ aqui,
    # ele É φ — os dois números são o mesmo 6
    cont9 = formula(("r", AMARELO), ("=", PRETO), ("6", AMARELO),
                    ("=", PRETO), ("φ(", CINZA), ("9", LARANJA), (")", CINZA),
                    tamanho=26, buff=0.10).move_to([_MEIO_X, -3.15, 0])
    with narra(cena, "C9N13", 5.3):
        cena.play(Write(d4), run_time=0.8 * VEL)
        # a definição encolhe para a direita e a tabela volta por baixo dela
        cena.play(bloco.animate.scale(0.8).move_to([3.3, 0, 0]),
                  FadeIn(tab9), FadeIn(lin_h), FadeIn(lin_v), FadeIn(leg5),
                  GrowArrow(seta5), Create(ini5), run_time=1.2 * VEL)
        cena.play(LaggedStart(*degraus, lag_ratio=0.8), run_time=2.2 * VEL)
        # "a contagem de Euler": a peça que o capítulo 7 definiu e o 8 gastou
        cena.play(Write(cont9), Indicate(phi4, color=LARANJA),
                  run_time=0.9 * VEL)

    # ------------------------------------------------------------------------
    # C9N14 — o custo: o módulo cresce, os dígitos somem e o que sobra é malha,
    # cada vez mais densa. A contagem de tentativas acompanha e no fim vira um
    # "?" que colapsa dentro do φ(n) da definição. Mesmo gesto do C8N39.
    # ------------------------------------------------------------------------
    malha21, malha39, malha77 = _malha(21, 0.8), _malha(39, 0.6), _malha(77, 0.5)

    def _leg(n):
        return formula(("n", LARANJA), ("=", PRETO), (n, LARANJA),
                       tamanho=22, buff=0.12).move_to(leg5)

    def _conta(n, valor, cor):
        return formula(("φ(", CINZA), (n, LARANJA), (") =", CINZA),
                       (valor, cor), tamanho=26, buff=0.10).move_to(cont9)

    l21, l39, l77 = _leg("21"), _leg("39"), _leg("77")
    c21 = _conta("21", "12", AMARELO)
    c39 = _conta("39", "24", AMARELO)
    c77 = _conta("77", "?", CINZA)
    with narra(cena, "C9N14", 5.9):
        # as duas linhas da tabela mod 9 é que se desdobram na malha inteira
        cena.play(FadeOut(tab9), FadeOut(caminho5), FadeOut(ini5),
                  FadeOut(seta5),
                  ReplacementTransform(VGroup(lin_h, lin_v), malha21),
                  ReplacementTransform(leg5, l21),
                  ReplacementTransform(cont9, c21), run_time=1.5 * VEL)
        cena.play(ReplacementTransform(malha21, malha39),
                  ReplacementTransform(l21, l39),
                  ReplacementTransform(c21, c39), run_time=1.1 * VEL)
        cena.play(ReplacementTransform(malha39, malha77),
                  ReplacementTransform(l39, l77),
                  ReplacementTransform(c39, c77), run_time=1.0 * VEL)
        # a contagem COLAPSA dentro do φ(n): é a conta que ninguém faz à mão
        cena.play(c77.animate.move_to(phi4).scale(0.2).set_opacity(0),
                  Indicate(phi4, color=LARANJA), run_time=1.0 * VEL)
        cena.remove(c77)
        # e a definição retoma o centro, sozinha, para a fala final
        cena.play(FadeOut(malha77), FadeOut(l77),
                  bloco.animate.scale(1 / 0.8).move_to(ORIGIN),
                  run_time=1.0 * VEL)

    # a caixa fica parada em cena; só o r pisca, porque é o que o capítulo
    # seguinte vem cobrar
    with narra(cena, "C9N15", 8.6):
        cena.play(Indicate(d3[0][1], color=AMARELO), run_time=0.9 * VEL)

    # a caixa da definição (a borda E o conteúdo) sobrevive ao capítulo: ela
    # não sai por um limpar(), sai DENTRO do play em que o cartão do capítulo
    # seguinte entra — mesma entrega da tese no fim do parte8
    return bloco
