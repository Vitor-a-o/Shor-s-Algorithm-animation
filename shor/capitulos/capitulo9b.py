# -*- coding: utf-8 -*-
from manim import *
import numpy as np

from ..paleta import *
from ..ferramentas import *

# ============================================================================
# CAPÍTULO 9b — Da Ordem Modular à fatoração (slides do anexo)
#   1) alvo: n = 35 = p × q escondidos; base a = 8
#   2) ENCONTRANDO a ordem modular de 8 módulo 35 (cadeia ×8) → r = 4
#   3) 8⁴ ≡ 1 → 8⁴ − 1 é múltiplo de 35 → x = 117 — a ÁRVORE 117·35
#      nasce JUNTO da conta
#   4) r par → diferença de quadrados → 65 · 63 — a segunda ÁRVORE
#   5) p, q, z, y e a comutatividade: 65 e 63 COMPARTILHAM fatores com 35
#   6) o mdc pesca p e q → 35 = 5 × 7
#   7) o caso INÚTIL (a = 24): 13825 é múltiplo de n → fatores triviais
#   8) por que isso quebra o RSA (lembrete do Capítulo 8)
#
# É o capítulo 10 EM TELA: as tags são C10N01–C10N36.
# ============================================================================
def parte9b(cena):
    def liga(de, para):
        return Line(de.get_bottom() + 0.06 * DOWN, para.get_top() + 0.06 * UP,
                    color=CINZA, stroke_width=1.8)

    # o alvo — um n que é produto de dois primos escondidos
    obj = formula(("n", LARANJA), ("=", PRETO), ("35", LARANJA),
                  ("=", PRETO), ("p", ROSA), ("×", PRETO), ("q", VERDE2),
                  ("?", PRETO), tamanho=34).to_edge(UP, buff=0.45)
    with narra(cena, "C10N01", 5.8):
        cena.play(Write(obj), run_time=1.0 * VEL)

    # escolhemos a base a = 8
    base = formula(("base:", CINZA), ("a", VERMELHO), ("=", PRETO),
                   ("8", VERMELHO), tamanho=28).move_to([0, 2.6, 0])
    with narra(cena, "C10N02", 6.7):
        cena.play(Write(base), run_time=0.8 * VEL)

    # ENCONTRANDO a ordem modular de 8 módulo 35 (como no Capítulo 9)
    rotulo = formula(("encontrando a", CINZA), ("ordem modular", PRETO),
                     ("de", CINZA), ("8", VERMELHO), ("módulo", CINZA),
                     ("35", LARANJA), tamanho=24,
                     buff=0.12).move_to([0, 2.05, 0])

    #   cadeia 1 → 8 → 29 → 22 → (volta ao 1): quatro passos ×8
    valores = ["1", "8", "29", "22"]
    xs = [-4.6, -1.6, 1.4, 4.4]
    caixas = VGroup()
    for v, x in zip(valores, xs):
        f = T(v, 30, PRETO)
        r = RoundedRectangle(corner_radius=0.12, width=1.15, height=0.62,
                             stroke_color=VERDE, stroke_width=2.5)
        r.move_to([x, 1.55, 0])
        f.move_to(r)
        caixas.add(VGroup(r, f))
    setas_o = VGroup()
    # o arco de retorno passa POR BAIXO das caixas
    volta = ArcBetweenPoints(caixas[3].get_bottom() + 0.08 * DOWN,
                             caixas[0].get_bottom() + 0.08 * DOWN,
                             angle=-0.5, color=LARANJA, stroke_width=3)
    rv = T("×8", 20, LARANJA).next_to(volta, DOWN, buff=0.08)

    # a busca inteira cabe numa fala só: o laço roda DENTRO do with, porque
    # "multiplicando pela base até o um voltar" é um gesto contínuo
    with narra(cena, "C10N03", 7.5):
        cena.play(Write(rotulo), run_time=0.9 * VEL)
        cena.play(FadeIn(caixas[0]), run_time=0.5 * VEL)
        for i in range(3):
            seta = Arrow(caixas[i].get_right(), caixas[i + 1].get_left(),
                         buff=0.08, color=LARANJA, stroke_width=3,
                         max_tip_length_to_length_ratio=0.25)
            rot = T("×8", 20, LARANJA).next_to(seta, DOWN, buff=0.08)
            setas_o.add(seta, rot)
            cena.play(GrowArrow(seta), FadeIn(rot), FadeIn(caixas[i + 1]),
                      run_time=0.6 * VEL)
        cena.play(Create(volta), FadeIn(rv), run_time=0.8 * VEL)
        cena.play(Flash(caixas[0].get_center(), color=VERDE,
                        flash_radius=0.55), run_time=0.6 * VEL)

    # quatro passos ×8 para voltar ao 1 ⇒ r = 4
    rper = formula(("r", AMARELO), ("=", PRETO), ("4", AMARELO),
                   tamanho=32).move_to([6.0, 1.55, 0])
    with narra(cena, "C10N04", 2.9):
        cena.play(Write(rper),
                  *[Indicate(m, color=LARANJA) for m in (setas_o[1], setas_o[3],
                                                         setas_o[5], rv)],
                  run_time=0.9 * VEL)

    # a ordem escrita como congruência — nasce da cadeia
    e1 = VGroup(pot("8", "4", VERMELHO, AMARELO, 32), T("≡", 32, PRETO),
                T("1", 32, VERDE), fmod("35", 30))
    e1.arrange(RIGHT, buff=0.15).move_to([0, 0.45, 0])
    with narra(cena, "C10N05", 5.4):
        cena.play(Write(e1), Indicate(rper, color=AMARELO), run_time=1.1 * VEL)

    # passa o 1 para o outro lado — 8⁴ − 1 é múltiplo de 35.
    # A cadeia cumpriu o papel e sai no COMEÇO desta fala (r = 4 fica, sobe
    # para o canto); a congruência só se move depois
    e2 = VGroup(pot("8", "4", VERMELHO, AMARELO, 32), T("− 1", 32, PRETO),
                T("≡", 32, PRETO), T("0", 32, VERDE), fmod("35", 30))
    e2.arrange(RIGHT, buff=0.15).move_to(e1)
    with narra(cena, "C10N06", 3.8):
        cena.play(FadeOut(VGroup(caixas, setas_o, volta, rv, base, rotulo)),
                  rper.animate.move_to([6.0, 2.6, 0]),
                  run_time=0.8 * VEL)
        cena.play(ReplacementTransform(e1, e2), run_time=1.0 * VEL)

    nota = formula(("8⁴ − 1", PRETO), ("é múltiplo de", CINZA),
                   ("35", LARANJA), tamanho=24,
                   buff=0.12).next_to(e2, DOWN, buff=0.28)
    with narra(cena, "C10N07", 6.3):
        cena.play(FadeIn(nota), run_time=0.8 * VEL)

    # quantas vezes o 35 cabe? 8⁴ − 1 = x · 35
    e3 = VGroup(pot("8", "4", VERMELHO, AMARELO, 32), T("− 1 =", 32, PRETO),
                T("x", 32, PRETO), T("·", 32, PRETO), T("35", 32, LARANJA))
    e3.arrange(RIGHT, buff=0.15).move_to(e2)
    with narra(cena, "C10N08", 3.8):
        cena.play(ReplacementTransform(e2, e3), FadeOut(nota),
                  run_time=1.0 * VEL)

    # a PRIMEIRA ÁRVORE nasce junto da conta: 8⁴ − 1 se abre em 35 e x
    rb = VGroup(pot("8", "4", VERMELHO, AMARELO, 26),
                T("− 1", 26, PRETO)).arrange(RIGHT, buff=0.08)
    rb.move_to([3.4, -1.35, 0])
    fB35 = T("35", 28, LARANJA).move_to([2.3, -2.35, 0])
    fBx = T("x", 28, PRETO).move_to([4.5, -2.35, 0])
    linB = VGroup(liga(rb, fB35), liga(rb, fBx))
    with narra(cena, "C10N09", 7.1):
        cena.play(ReplacementTransform(VGroup(e3[0], e3[1]).copy(), rb),
                  run_time=0.9 * VEL)
        cena.play(Create(linB[0]), Create(linB[1]),
                  ReplacementTransform(e3[4].copy(), fB35),
                  ReplacementTransform(e3[2].copy(), fBx), run_time=0.9 * VEL)

    # x = (8⁴ − 1)/35 = 117 — a conta preenche a árvore
    ex = formula(("x", PRETO), ("=", PRETO), ("(8⁴ − 1)", PRETO),
                 ("/", PRETO), ("35", LARANJA), ("=", PRETO),
                 ("117", PRETO), tamanho=24,
                 buff=0.10).next_to(e3, DOWN, buff=0.28)
    e4 = VGroup(pot("8", "4", VERMELHO, AMARELO, 32), T("− 1 =", 32, PRETO),
                T("117", 32, PRETO), T("·", 32, PRETO), T("35", 32, LARANJA))
    e4.arrange(RIGHT, buff=0.15).move_to(e3)
    fB117 = T("117", 28, PRETO).move_to(fBx)
    with narra(cena, "C10N10", 5.4):
        cena.play(Write(ex), run_time=0.9 * VEL)
        cena.play(ReplacementTransform(e3, e4), FadeOut(ex),
                  ReplacementTransform(fBx, fB117), run_time=1.0 * VEL)

    # r é PAR → diferença de quadrados
    d0 = formula(("r", AMARELO), ("par", PRETO), ("⇒", PRETO),
                 ("diferença de quadrados", PRETO), tamanho=24,
                 buff=0.12).move_to([0, -0.55, 0])
    with narra(cena, "C10N11", 5.8):
        cena.play(Write(d0), run_time=0.9 * VEL)

    d1 = VGroup(pot("8", "4", VERMELHO, AMARELO, 28), T("− 1 =", 28, PRETO),
                T("(8² − 1)(8² + 1)", 28, PRETO))
    d1.arrange(RIGHT, buff=0.14).move_to([0, -0.55, 0])
    with narra(cena, "C10N12", 9.6):
        cena.play(ReplacementTransform(d0, d1), run_time=1.0 * VEL)

    d2 = VGroup(pot("8", "4", VERMELHO, AMARELO, 28), T("− 1 =", 28, PRETO),
                T("65", 28, PRETO), T("·", 28, PRETO), T("63", 28, PRETO))
    d2.arrange(RIGHT, buff=0.14).move_to(d1)
    with narra(cena, "C10N13", 5.4):
        cena.play(ReplacementTransform(d1, d2), run_time=1.0 * VEL)

    # a SEGUNDA ÁRVORE: o mesmo 8⁴ − 1 se abre em 65 e 63
    ra = VGroup(pot("8", "4", VERMELHO, AMARELO, 26),
                T("− 1", 26, PRETO)).arrange(RIGHT, buff=0.08)
    ra.move_to([-3.8, -1.35, 0])
    fA65 = T("65", 28, PRETO).move_to([-4.9, -2.35, 0])
    fA63 = T("63", 28, PRETO).move_to([-2.7, -2.35, 0])
    linA = VGroup(liga(ra, fA65), liga(ra, fA63))
    with narra(cena, "C10N14", 3.3):
        cena.play(ReplacementTransform(VGroup(d2[0], d2[1]).copy(), ra),
                  run_time=0.9 * VEL)
        cena.play(Create(linA[0]), Create(linA[1]),
                  ReplacementTransform(d2[2].copy(), fA65),
                  ReplacementTransform(d2[4].copy(), fA63), run_time=0.9 * VEL)

    # as DUAS fatorações do MESMO número
    junta = formula(("65 · 63", PRETO), ("=", PRETO), ("117 ·", PRETO),
                    ("35", LARANJA), tamanho=30,
                    buff=0.12).move_to([0, -0.55, 0])
    with narra(cena, "C10N15", 3.8):
        cena.play(ReplacementTransform(d2, junta), Indicate(e4, color=CINZA),
                  run_time=1.0 * VEL)

    # dentro do 35 moram p e q; dentro do 117, z e y
    nB = VGroup(T("p", 26, ROSA).move_to([1.7, -3.15, 0]),
                T("q", 26, VERDE2).move_to([2.9, -3.15, 0]),
                T("z", 26, PRETO).move_to([3.9, -3.15, 0]),
                T("y", 26, PRETO).move_to([5.1, -3.15, 0]))
    linB2 = VGroup(liga(fB35, nB[0]), liga(fB35, nB[1]),
                   liga(fB117, nB[2]), liga(fB117, nB[3]))
    j2 = formula(("65 · 63", PRETO), ("=", PRETO), ("(z · y)", PRETO),
                 ("·", PRETO), ("(", PRETO), ("p", ROSA), ("·", PRETO),
                 ("q", VERDE2), (")", PRETO), tamanho=28,
                 buff=0.08).move_to(junta)
    with narra(cena, "C10N16", 5.8):
        cena.play(*[Create(l) for l in linB2], FadeIn(nB),
                  ReplacementTransform(junta, j2), run_time=1.2 * VEL)

    # pela COMUTATIVIDADE, os mesmos fatores se reagrupam em 65 e 63
    comut = T("pela comutatividade da multiplicação", 20,
              CINZA).move_to([0, -0.05, 0])
    nA = VGroup(T("p", 26, ROSA).move_to([-5.5, -3.15, 0]),
                T("y", 26, PRETO).move_to([-4.3, -3.15, 0]),
                T("z", 26, PRETO).move_to([-3.3, -3.15, 0]),
                T("q", 26, VERDE2).move_to([-2.1, -3.15, 0]))
    linA2 = VGroup(liga(fA65, nA[0]), liga(fA65, nA[1]),
                   liga(fA63, nA[2]), liga(fA63, nA[3]))
    j3 = formula(("65 · 63", PRETO), ("=", PRETO), ("(", PRETO),
                 ("p", ROSA), ("· y)", PRETO), ("·", PRETO),
                 ("(z ·", PRETO), ("q", VERDE2), (")", PRETO),
                 tamanho=28, buff=0.08).move_to(j2)
    with narra(cena, "C10N17", 8.3):
        cena.play(FadeIn(comut), run_time=0.7 * VEL)
        cena.play(*[Create(l) for l in linA2], FadeIn(nA),
                  ReplacementTransform(j2, j3), run_time=1.2 * VEL)

    # o p mora no 65 E no 35; o q mora no 63 E no 35
    with narra(cena, "C10N18", 2.5):
        cena.play(Indicate(nA[0], color=ROSA), Indicate(nB[0], color=ROSA),
                  run_time=0.9 * VEL)

    with narra(cena, "C10N19", 1.7):
        cena.play(Indicate(nA[3], color=VERDE2), Indicate(nB[1], color=VERDE2),
                  run_time=0.9 * VEL)

    expl = formula(("65 e 63", PRETO), ("compartilham fatores com", CINZA),
                   ("35", LARANJA), tamanho=22, buff=0.12).move_to(comut)
    with narra(cena, "C10N20", 7.5):
        cena.play(ReplacementTransform(comut, expl), run_time=0.8 * VEL)

    # o mdc PESCA os fatores compartilhados
    m1 = formula(("mdc(", PRETO), ("63", PRETO), (", ", PRETO),
                 ("35", LARANJA), (") =", PRETO), ("7", VERDE2),
                 tamanho=26, buff=0.08).move_to([-0.2, -2.9, 0])
    m2 = formula(("mdc(", PRETO), ("65", PRETO), (", ", PRETO),
                 ("35", LARANJA), (") =", PRETO), ("5", ROSA),
                 tamanho=26, buff=0.08).move_to([-0.2, -3.45, 0])
    with narra(cena, "C10N21", 9.2):
        cena.play(Write(m1), Indicate(nA[3], color=VERDE2),
                  Indicate(nB[1], color=VERDE2), run_time=1.0 * VEL)

    with narra(cena, "C10N22", 2.1):
        cena.play(Write(m2), Indicate(nA[0], color=ROSA),
                  Indicate(nB[0], color=ROSA), run_time=1.0 * VEL)

    # p e q foram encontrados: 35 = 5 × 7
    fim = formula(("35", LARANJA), ("=", PRETO), ("5", ROSA), ("×", PRETO),
                  ("7", VERDE2), tamanho=36).move_to([-0.2, -3.15, 0])
    cxa = SurroundingRectangle(fim, color=VERDE, buff=0.2, corner_radius=0.14)
    with narra(cena, "C10N23", 2.1):
        cena.play(ReplacementTransform(VGroup(m1, m2), fim), Create(cxa),
                  run_time=1.1 * VEL)

    obj2 = formula(("n", LARANJA), ("=", PRETO), ("35", LARANJA),
                   ("=", PRETO), ("5", ROSA), ("×", PRETO), ("7", VERDE2),
                   ("✓", VERDE), tamanho=34).move_to(obj)
    with narra(cena, "C10N24", 3.8):
        cena.play(ReplacementTransform(obj, obj2), run_time=1.0 * VEL)

    # ---------- o caso INÚTIL (slides 19–20): a = 24 ----------
    # a limpeza pertence a ESTA fala e vai EMENDADA no FadeIn: separada, ela
    # leria como fim de capítulo. O `fim` na moldura verde NÃO sai — o sucesso
    # segue à vista enquanto a falha roda, e o C10N33 puxa φ(35) dele
    cap5 = T("às vezes a ordem modular não dá informação útil",
             24).move_to([0, 2.45, 0])
    with narra(cena, "C10N25", 2.9):
        cena.play(FadeOut(VGroup(e4, j3, expl, ra, linA, fA65, fA63, nA, linA2,
                                 rb, linB, fB35, fB117, nB, linB2, rper)),
                  FadeIn(cap5), run_time=0.8 * VEL)

    u0 = formula(("a", VERMELHO), ("=", PRETO), ("24", VERMELHO),
                 ("→", CINZA), ("r", AMARELO), ("=", PRETO), ("6", AMARELO),
                 tamanho=28).move_to([0, 1.7, 0])
    with narra(cena, "C10N26", 4.2):
        cena.play(Write(u0), run_time=0.9 * VEL)

    u1a = VGroup(pot("24", "6", VERMELHO, AMARELO, 26),
                 T("− 1 = (24³ − 1)(24³ + 1)", 26, PRETO))
    u1a.arrange(RIGHT, buff=0.12).move_to([0, 0.9, 0])
    u1 = VGroup(pot("24", "6", VERMELHO, AMARELO, 26), T("− 1 =", 26, PRETO),
                T("13825", 26, PRETO), T("·", 26, PRETO),
                T("13823", 26, PRETO))
    u1.arrange(RIGHT, buff=0.12).move_to(u1a)
    with narra(cena, "C10N27", 3.3):
        cena.play(Write(u1a), run_time=1.0 * VEL)
        cena.play(ReplacementTransform(u1a, u1), run_time=1.0 * VEL)

    # a árvore do azar: p e q caem JUNTOS no 13825 (múltiplo de 35)
    ru = VGroup(pot("24", "6", VERMELHO, AMARELO, 24),
                T("− 1", 24, PRETO)).arrange(RIGHT, buff=0.08)
    ru.move_to([-2.8, -0.4, 0])
    fu1 = T("13825", 26, PRETO).move_to([-4.3, -1.4, 0])
    fu2 = T("13823", 26, PRETO).move_to([-1.3, -1.4, 0])
    linU = VGroup(liga(ru, fu1), liga(ru, fu2))
    nU = VGroup(T("p", 24, ROSA).move_to([-4.9, -2.2, 0]),
                T("q", 24, VERDE2).move_to([-3.7, -2.2, 0]),
                T("z", 24, PRETO).move_to([-1.9, -2.2, 0]),
                T("y", 24, PRETO).move_to([-0.7, -2.2, 0]))
    linU2 = VGroup(liga(fu1, nU[0]), liga(fu1, nU[1]),
                   liga(fu2, nU[2]), liga(fu2, nU[3]))
    with narra(cena, "C10N28", 5.4):
        cena.play(ReplacementTransform(VGroup(u1[0], u1[1]).copy(), ru),
                  run_time=0.9 * VEL)
        cena.play(Create(linU[0]), Create(linU[1]),
                  ReplacementTransform(u1[2].copy(), fu1),
                  ReplacementTransform(u1[4].copy(), fu2), run_time=0.9 * VEL)
        cena.play(*[Create(l) for l in linU2], FadeIn(nU), run_time=1.0 * VEL)

    multi = formula(("múltiplo de", CINZA), ("35", LARANJA),
                    tamanho=20, buff=0.10).move_to([-5.6, -0.65, 0])
    setam = Arrow(multi.get_bottom() + 0.05 * DOWN,
                  fu1.get_top() + 0.08 * UP, buff=0, color=PRETO,
                  stroke_width=3, max_tip_length_to_length_ratio=0.2)
    with narra(cena, "C10N29", 3.8):
        cena.play(FadeIn(multi), GrowArrow(setam),
                  Indicate(nU[0], color=ROSA), Indicate(nU[1], color=VERDE2),
                  run_time=1.1 * VEL)

    # o mdc devolve só fatores TRIVIAIS: 35 e 1
    m3 = formula(("mdc(", PRETO), ("13825", PRETO), (", ", PRETO),
                 ("35", LARANJA), (") =", PRETO), ("35", LARANJA),
                 tamanho=26, buff=0.08).move_to([3.4, -0.7, 0])
    m4 = formula(("mdc(", PRETO), ("13823", PRETO), (", ", PRETO),
                 ("35", LARANJA), (") =", PRETO), ("1", PRETO),
                 tamanho=26, buff=0.08).move_to([3.4, -1.35, 0])
    with narra(cena, "C10N30", 3.3):
        cena.play(Write(m3), run_time=0.9 * VEL)

    with narra(cena, "C10N31", 4.2):
        cena.play(Write(m4), run_time=0.9 * VEL)

    triv = formula(("fatores triviais", VERMELHO), ("✗", VERMELHO),
                   tamanho=24, buff=0.12).move_to([3.4, -2.05, 0])
    sol = T("solução: escolher outro a e recomeçar", 20,
            CINZA).move_to([3.4, -2.6, 0])
    # animação curta sob fala longa: o quadro fica parado no ✗ vermelho
    # durante a segunda metade da linha, e é essa parada que faz a falha pesar
    with narra(cena, "C10N32", 13.4):
        cena.play(Write(triv), FadeIn(sol), run_time=1.0 * VEL)

    # ---------- POR QUE isso quebra o RSA (lembrete do Capítulo 8) ----------
    # com p e q em mãos, φ(n) sai de graça — e com φ(n), a chave privada d.
    # A contagem de Euler NASCE DE DENTRO dos dois primos que ficaram na
    # moldura verde, e a limpeza do caso inútil vai emendada no mesmo play
    r1 = formula(("φ(", PRETO), ("35", LARANJA), (")", PRETO), ("=", PRETO),
                 ("(", PRETO), ("5", ROSA), ("− 1)", PRETO), ("×", PRETO),
                 ("(", PRETO), ("7", VERDE2), ("− 1)", PRETO), ("=", PRETO),
                 ("24", PRETO), tamanho=30, buff=0.10).move_to([0, 1.1, 0])
    with narra(cena, "C10N33", 7.1):
        cena.play(FadeOut(VGroup(cap5, u0, u1, ru, linU, fu1, fu2, nU, linU2,
                                 multi, setam, m3, m4, triv, sol)),
                  ReplacementTransform(fim.copy(), r1), run_time=1.1 * VEL)

    r2 = formula(("e", VERMELHO), ("·", PRETO), ("d", AZUL), ("≡", PRETO),
                 ("1", VERDE), ("(mod φ(", PRETO), ("n", LARANJA),
                 ("))", PRETO), ("⇒", PRETO), ("d", AZUL),
                 ("encontrado", PRETO),
                 tamanho=28, buff=0.10).move_to([0, 0.15, 0])
    with narra(cena, "C10N34", 8.8):
        cena.play(Write(r2), run_time=1.0 * VEL)

    r3 = formula(("fatorar", PRETO), ("n", LARANJA), ("=", PRETO),
                 ("descobrir a chave privada", PRETO),
                 tamanho=30).move_to([0, -1.1, 0])
    cxa2 = SurroundingRectangle(r3, color=VERDE, buff=0.2,
                                corner_radius=0.14)
    with narra(cena, "C10N35", 5.4):
        cena.play(Write(r3), Create(cxa2), run_time=1.1 * VEL)

    # a tese fica parada em cena enquanto a fala passa o bastão ao quântico
    so_fala(cena, "C10N36", 9.2)
