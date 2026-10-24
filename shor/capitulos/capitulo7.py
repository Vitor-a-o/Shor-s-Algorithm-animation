# -*- coding: utf-8 -*-
from manim import *
import numpy as np
from functools import partial

from ..paleta import *
from ..ferramentas import *
from ..ferramentas import _agora, _etapa, _serie, _copia
from ..sincronias import na_palavra

# ============================================================================
# CAPÍTULO 7 — Euler NA TABELA mod 9 (slides 67–81): o cancelamento proibido
#   Narração: C7N01 … C7N15 (roteiro_video3_do_teorema_ao_rsa.md)
# ============================================================================
def _arcos(xs, ya, yb, de, para):
    """Os arcos do C6N06: cada um liga de[j] (em xs[j], ya) ao número de
    mesmo valor em `para` (na altura yb)."""
    arcos = VGroup()
    for j, v in enumerate(de):
        idx = para.index(v)
        arcos.add(ArcBetweenPoints(
            np.array([xs[j], ya - 0.2, 0.0]),
            np.array([xs[idx], yb + 0.2, 0.0]),
            angle=(0.65 if idx > j else -0.65),
            color=VERDE, stroke_width=2.5))
    return arcos


def parte7(cena):
    # tabela 8×8 dos resíduos de 9
    tam = 0.5
    canto = np.array([-6.1, 2.35, 0.0])

    def ponto(i, j):
        return canto + np.array([j * tam, -i * tam, 0.0])

    head_c = VGroup(*[T(str(j), 22, AZUL).move_to(ponto(0, j))
                      for j in range(1, 9)])
    head_l = VGroup(*[T(str(i), 22, VERMELHO).move_to(ponto(i, 0))
                      for i in range(1, 9)])
    lin_h = Line(canto + [0.5 * tam, -0.5 * tam, 0],
                 canto + [8.45 * tam, -0.5 * tam, 0], color=PRETO,
                 stroke_width=1.5)
    lin_v = Line(canto + [0.5 * tam, -0.5 * tam, 0],
                 canto + [0.5 * tam, -8.45 * tam, 0], color=PRETO,
                 stroke_width=1.5)
    titulo_tab = T(tx("geral.tabela_mult_mod").format(n=9), 26).move_to([-4.1, 2.95, 0])
    linhas_cel = [VGroup(*[T(str((i * j) % 9), 22, PRETO).move_to(ponto(i, j))
                           for j in range(1, 9)]) for i in range(1, 9)]

    # a tabela entra em dois tempos, como no C6N01: a moldura, depois as linhas
    with narra(cena, "C7N01", 7.5):
        moldura = _etapa(
            FadeIn(titulo_tab),
            LaggedStart(*[FadeIn(h) for h in head_c], lag_ratio=0.3),
            LaggedStart(*[FadeIn(h) for h in head_l], lag_ratio=0.3),
            Create(lin_h), Create(lin_v), run_time=1.5 * VEL)
        corpo = LaggedStart(*[FadeIn(l) for l in linhas_cel], lag_ratio=0.2,
                            run_time=2.5 * VEL, introducer=True)
        cena.play(_serie(moldura, corpo))

    # elipses verdes nas linhas 1 e 2 (slide 68): a lista sai da linha 1 e a
    # linha do multiplicador cai sobre B, como no capítulo 6
    el1 = Ellipse(width=8 * tam + 0.5, height=0.5, color=VERDE,
                  stroke_width=2.5).move_to(canto + [4.5 * tam, -1 * tam, 0])
    el2 = Ellipse(width=8 * tam + 0.5, height=0.5, color=VERDE,
                  stroke_width=2.5).move_to(canto + [4.5 * tam, -2 * tam, 0])
    xs = [0.9 * j for j in range(8)]
    yA, yB = 2.05, 0.25
    A = VGroup(*[T(str(j + 1), 26, PRETO).move_to([xs[j], yA, 0])
                 for j in range(8)])
    Bv = [(2 * (j + 1)) % 9 for j in range(8)]
    B = VGroup(*[T(str(Bv[j]), 26, VERMELHO).move_to([xs[j], yB, 0])
                 for j in range(8)])
    mod_rot = fmod("9", 22).next_to(B, LEFT, buff=0.3)
    with narra(cena, "C7N02", 3.3):
        na = partial(na_palavra, cena, _agora(cena), "C7N02", 3.3)
        # "multiplicador": a linha 2 ganha a elipse e o 2 pulsa; logo depois
        # as cópias dela caem sobre B (as cópias SÃO o B); "lista de restos":
        # A pulsa, cada número no lugar
        cai = _serie(
            _etapa(Create(el2), realce(head_l[1]), run_time=0.6 * VEL),
            _etapa(LaggedStart(*[_copia(linhas_cel[1][j], B[j])
                                 for j in range(8)], lag_ratio=0.08),
                   FadeIn(mod_rot), run_time=0.9 * VEL))
        cena.play(Create(el1, run_time=0.6 * VEL),
                  LaggedStart(*[TransformFromCopy(linhas_cel[0][j], A[j])
                                for j in range(8)], lag_ratio=0.08,
                              run_time=1.0 * VEL),
                  na("multiplicador", cai),
                  na("lista de restos", realce(*A)))

    # ------------------------------------------------------------------
    # Os passos do capítulo 6, comprimidos: arcos, o produto (2·1)…(2·8) e a
    # extração dos 2 (evidencia() em ferramentas.py), com o 3 e o 6 já
    # MARROM. O eq final é feito dos mesmos tokens, reagrupados como a
    # tentativa precisa: esq[2], esq[4], dir_[1], dir_[3] são o 3 e o 6,
    # dir_[6] é o 9 do (mod 9).
    arcos = _arcos(xs, yA, yB, list(range(1, 9)), Bv)
    TK = 24
    ev = evidencia("2", range(1, 9), [0, -2.35, 0], tam=TK, mod="9",
                   tam_mod=TK, cores={3: MARROM, 6: MARROM})
    M, r = ev.mid, ev.rhs
    esq = VGroup(ev.pots[8], VGroup(*M[0:6]), M[6], VGroup(*M[7:12]), M[12],
                 VGroup(*M[13:18]))           # 2⁸ ·(1·2· 3 ·4·5· 6 ·7·8)
    dir_ = VGroup(VGroup(*r[0:5]), r[5], VGroup(*r[6:11]), r[11],
                  VGroup(*r[12:17]), *ev.modg)  # (1·2· 3 ·4·5· 6 ·7·8) (mod 9)
    eq = VGroup(esq, ev.igual, dir_)
    with narra(cena, "C7N03", 7.5):
        nasce = AnimationGroup(*ev.nasce(head_l[1], A, 1.6 * VEL, 1.2 * VEL,
                                         0.6 * VEL))
        cena.play(_serie(
            LaggedStart(LaggedStart(*[Create(a) for a in arcos],
                                    lag_ratio=0.12, run_time=1.2 * VEL),
                        nasce, lag_ratio=0.5, introducer=True),
            *ev.passos(0.35 * VEL)))
        # o 2 da frente (R[1]) fez o papel de 2², …, 2⁸; o eq leva o pots[8]
        cena.replace(ev.R[1], ev.pots[8])

    # tentativa: DIVIDIR os dois lados pela mesma multiplicação (montado
    # depois da extração: só agora os tokens estão no lugar final)
    ge = VGroup(*esq[1:])
    gd = VGroup(*dir_[:5])
    div_e = formula(("÷", VERMELHO), ("(1·2·", PRETO), ("3", MARROM),
                    ("·4·5·", PRETO), ("6", MARROM), ("·7·8)", PRETO),
                    tamanho=20, buff=0.05).next_to(ge, DOWN, buff=0.2)
    div_d = formula(("÷", VERMELHO), ("(1·2·", PRETO), ("3", MARROM),
                    ("·4·5·", PRETO), ("6", MARROM), ("·7·8)", PRETO),
                    tamanho=20, buff=0.05).next_to(gd, DOWN, buff=0.2)
    with narra(cena, "C7N04", 6.2):
        na = partial(na_palavra, cena, _agora(cena), "C7N04", 6.2)
        # a área da direita fica livre para o exp1/exp2
        cena.play(FadeOut(A, run_time=0.5 * VEL), FadeOut(B, run_time=0.5 * VEL),
                  FadeOut(arcos, run_time=0.5 * VEL),
                  FadeOut(mod_rot, run_time=0.5 * VEL),
                  na("cancelar a lista",
                     Write(div_e, run_time=1.0 * VEL),
                     Write(div_d, run_time=1.0 * VEL)))

    # POR QUE a divisão é proibida: dividir por um fator é MULTIPLICAR
    # pelo inverso dele — e 1/3 e 1/6 NÃO EXISTEM módulo 9
    exp1 = T(tx("c7.dividir_e_multiplicar"), 22,
             PRETO).move_to([3.7, 1.75, 0])
    exp2 = formula(("1/", PRETO), ("3", MARROM), (tx("geral.e"), PRETO), ("1/", PRETO),
                   ("6", MARROM), (tx("c7.nao_existem"), VERMELHO), *MOD("9"),
                   tamanho=22, buff=0.08).move_to([3.7, 1.2, 0])
    with narra(cena, "C7N05", 8.3):
        na = partial(na_palavra, cena, _agora(cena), "C7N05", 8.3)
        cena.play(FadeIn(exp1), Write(exp2), run_time=1.0 * VEL)
        # "dois desses fatores": os 3 e 6 marrons de todas as cópias;
        # "módulo": o 9 do exp2 e o de dir_
        cena.play(na("dois desses fatores",
                     realce(esq[2], esq[4], dir_[1], dir_[3],
                            div_e[2], div_e[4], div_d[2], div_d[4])))
        cena.play(na("módulo", realce(exp2[7], dir_[6])))

    # RESSALTA os inversos que não existem: os 3 e 6 marrons pulsam,
    # as linhas 3 e 6 da tabela apagam — a divisão é NEGADA
    neq = T("≢", 30, VERMELHO).move_to(eq[1])
    with narra(cena, "C7N06", 10.0):
        na = partial(na_palavra, cena, _agora(cena), "C7N06", 10.0)
        # um bloco só, que começa em "linhas": apagar + Indicate, Wiggle e o
        # ≢ em sequência
        apaga = [linhas_cel[i].animate.set_opacity(0.2).build()
                 for i in (2, 5)]
        apaga += [head_l[i].animate.set_opacity(0.3).build()
                  for i in (2, 5)]
        cena.play(na("linhas", _serie(
            _etapa(*apaga,
                   Indicate(div_e[2], color=MARROM),
                   Indicate(div_e[4], color=MARROM),
                   Indicate(div_d[2], color=MARROM),
                   Indicate(div_d[4], color=MARROM),
                   Indicate(exp2[5], color=VERMELHO), run_time=1.4 * VEL),
            _etapa(Wiggle(div_e), Wiggle(div_d), run_time=0.9 * VEL),
            _etapa(FadeOut(div_e), FadeOut(div_d), Transform(eq[1], neq),
                   run_time=0.8 * VEL))))

    # Euler: RETIRA os inversos que não existem — cruzes riscam o 3 e o 6
    # na equação e no topo da tabela → φ(9) = 6 sobreviventes
    cruzes = VGroup(Cross(head_c[2], stroke_color=VERMELHO, stroke_width=4),
                    Cross(head_c[5], stroke_color=VERMELHO, stroke_width=4))
    cruzes_eq = VGroup(*[Cross(m, stroke_color=VERMELHO, stroke_width=3.5)
                         for m in (esq[2], esq[4], dir_[1], dir_[3])])
    with narra(cena, "C7N07", 5.8):
        na = partial(na_palavra, cena, _agora(cena), "C7N07", 5.8)
        cena.play(FadeOut(exp1), FadeOut(exp2), run_time=1.0 * VEL)
        cena.play(na("números que não têm inverso",
                     Create(cruzes, run_time=1.0 * VEL),
                     Create(cruzes_eq, run_time=1.0 * VEL)))

    sobr = T("{1, 2, 4, 5, 7, 8}", 26, VERDE).move_to([3.6, 1.5, 0])
    with narra(cena, "C7N08", 5.0):
        na = partial(na_palavra, cena, _agora(cena), "C7N08", 5.0)
        cena.play(na("números", FadeIn(sobr, run_time=0.7 * VEL)))
        cena.play(na("módulo", realce(dir_[6])))

    phi = formula(("φ(", PRETO), ("9", LARANJA), (") = 6", PRETO),
                  tamanho=28, buff=0.06).move_to([3.6, 0.9, 0])
    with narra(cena, "C7N09", 7.1):
        na = partial(na_palavra, cena, _agora(cena), "C7N09", 7.1)
        cena.play(na("contagem", Write(phi, run_time=1.0 * VEL)))
        # cada token do φ(9) = 6 pulsa na própria cor (o 9 é laranja)
        cena.play(na("fi de ene", realce(*phi)))

    # a lista REFEITA também se rearranja: A2 (os seis de sobr), a linha do
    # 2 nessas colunas caindo sobre B2, os arcos, e a mesma conta de novo —
    # agora a divisão é permitida
    vals2 = [1, 2, 4, 5, 7, 8]
    xs2 = np.linspace(1.4, 6.4, 6)
    yA2, yB2 = 0.25, -1.25
    A2 = VGroup(*[T(str(v), 26, PRETO).move_to([xs2[j], yA2, 0])
                  for j, v in enumerate(vals2)])
    B2v = [(2 * v) % 9 for v in vals2]
    B2 = VGroup(*[T(str(b), 26, VERMELHO).move_to([xs2[j], yB2, 0])
                  for j, b in enumerate(B2v)])
    mod_rot2 = fmod("9", 22).next_to(B2, LEFT, buff=0.3)
    arcos2 = _arcos(xs2, yA2, yB2, vals2, B2v)
    ev2 = evidencia("2", vals2, [0, -2.35, 0], tam=TK, mod="9", tam_mod=TK)
    esq2 = VGroup(ev2.pots[6], ev2.mid)                # 2⁶ ·(1·2·4·5·7·8)
    dir2 = VGroup(ev2.rhs, *ev2.modg)                  # (1·2·4·5·7·8) (mod 9)
    eq2 = VGroup(esq2, ev2.igual, dir2)
    with narra(cena, "C7N10", 4.2):
        # os tokens do eq entraram um a um; o FadeOut dentro do Succession
        # só os tira de cena se o eq estiver nela como grupo
        cena.add(eq)
        nasce2 = ev2.nasce(head_l[1], A2, 0.8 * VEL, 0.6 * VEL, 0.4 * VEL)
        cena.play(_serie(
            _etapa(LaggedStart(*[_copia(sobr[1 + 2 * j], A2[j])
                                 for j in range(6)], lag_ratio=0.1),
                   LaggedStart(*[_copia(linhas_cel[1][c], B2[j])
                                 for j, c in enumerate((0, 1, 3, 4, 6, 7))],
                               lag_ratio=0.1),
                   FadeIn(mod_rot2), FadeOut(eq), FadeOut(cruzes_eq),
                   run_time=1.0 * VEL),
            _etapa(LaggedStart(*[Create(a) for a in arcos2], lag_ratio=0.1,
                               run_time=0.5 * VEL), *nasce2),
            *ev2.passos(0.3 * VEL)))
        cena.replace(ev2.R[1], ev2.pots[6])

    div2_e = formula(("÷", VERDE), ("(1·2·4·5·7·8)", PRETO),
                     tamanho=20, buff=0.05).next_to(esq2[1], DOWN, buff=0.2)
    div2_d = formula(("÷", VERDE), ("(1·2·4·5·7·8)", PRETO),
                     tamanho=20, buff=0.05).next_to(dir2[0], DOWN, buff=0.2)
    with narra(cena, "C7N11", 4.2):
        cena.play(Write(div2_e), Write(div2_d), run_time=0.8 * VEL)

    res = VGroup(pot("2", "6", VERMELHO, AZUL, 32),
                 *formula(("≡", PRETO), ("1", VERDE), *MOD("9"), tamanho=32))
    res.arrange(RIGHT, buff=0.16).move_to(eq2)
    with narra(cena, "C7N12", 5.0):
        na = partial(na_palavra, cena, _agora(cena), "C7N12", 5.0)
        cena.play(ReplacementTransform(VGroup(eq2, div2_e, div2_d), res),
                  run_time=1.1 * VEL)
        cena.play(na("potência", realce(res[0])))
        cena.play(na("a um", realce(res[2])))
        cena.play(na("nove", realce(res[4])))

    geral = VGroup(pot("a", expoente(("φ(", PRETO), ("n", LARANJA),
                                     (")", PRETO), tam=28), ROXO, tam=28),
                   T("≡", 28, PRETO), T("1", 28, VERDE), fmod("n", 26))
    geral.arrange(RIGHT, buff=0.16).move_to([0, -3.35, 0])
    with narra(cena, "C7N13", 8.3):
        na = partial(na_palavra, cena, _agora(cena), "C7N13", 8.3)
        cena.play(Write(geral), run_time=1.2 * VEL)
        # o n do módulo e o n do expoente (geral[0][1][1]) pulsam juntos; o
        # φ(n) do expoente pulsa token a token, cada um na própria cor
        cena.play(na("qualquer módulo",
                     realce(geral[3][1], geral[0][1][1])))
        cena.play(na("o expoente", realce(*geral[0][1])))
        cena.play(na("totiente", realce(*geral[0][1])))

    # A VIRADA, espelhando o C6N14: a tabela inteira e o aparato de exemplo
    # saem, e no mesmo bloco o geral sobe e cresce — sobrevivendo à limpeza,
    # o mesmo mobject viajando, sem ser redesenhado — enquanto o título
    # nasce. res é a última coisa a sumir, debaixo do geral que o generaliza.
    # (eq2, div2_e e div2_d já viraram o res no C7N12.)
    titulo = T(tx("c7.teorema_euler"), 40).move_to([0, 0.9, 0])
    saida = AnimationGroup(
        FadeOut(titulo_tab), FadeOut(head_c), FadeOut(head_l),
        FadeOut(lin_h), FadeOut(lin_v), *[FadeOut(l) for l in linhas_cel],
        FadeOut(el1), FadeOut(el2), FadeOut(cruzes), FadeOut(sobr), FadeOut(phi),
        FadeOut(A2), FadeOut(B2), FadeOut(arcos2), FadeOut(mod_rot2),
        geral.animate.move_to([0, -0.5, 0]).scale(40 / 28),
        Write(titulo), run_time=1.0 * VEL,
    )
    with narra(cena, "C7N14", 2.5):
        cena.play(LaggedStart(saida, FadeOut(res, run_time=0.6 * VEL),
                              lag_ratio=0.4))

    with narra(cena, "C7N15", 3.8):
        cena.play(Indicate(geral[0][1], color=ROXO), run_time=1.0 * VEL)
