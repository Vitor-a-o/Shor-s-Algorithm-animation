# -*- coding: utf-8 -*-
from manim import *
import numpy as np
from functools import partial

from ..paleta import *
from ..ferramentas import *
from ..ferramentas import _agora, _etapa, _serie, _copia, _vira, _mv
from ..sincronias import na_palavra

# ============================================================================
# CAPÍTULO 6 — Fermat NA TABELA multiplicativa mod 7 (slides 59–66)
#   Narração: C6N01 … C6N15 (roteiro_video3_do_teorema_ao_rsa.md)
# ============================================================================
def _alvo(valor, sobre):
    """O número vermelho do tamanho de B, em cima de `sobre`."""
    return T(str(valor), 30, VERMELHO).move_to(sobre)


def parte6(cena):
    # tabela 6×6 dos resíduos de 7
    tam = 0.6
    canto = np.array([-6.0, 2.1, 0.0])

    def ponto(i, j):
        return canto + np.array([j * tam, -i * tam, 0.0])

    head_c = VGroup(*[T(str(j), 24, AZUL).move_to(ponto(0, j))
                      for j in range(1, 7)])
    head_l = VGroup(*[T(str(i), 24, VERMELHO).move_to(ponto(i, 0))
                      for i in range(1, 7)])
    lin_h = Line(canto + [0.5 * tam, -0.5 * tam, 0],
                 canto + [6.45 * tam, -0.5 * tam, 0], color=PRETO,
                 stroke_width=1.5)
    lin_v = Line(canto + [0.5 * tam, -0.5 * tam, 0],
                 canto + [0.5 * tam, -6.45 * tam, 0], color=PRETO,
                 stroke_width=1.5)
    titulo_tab = T(tx("geral.tabela_mult_mod").format(n=7), 26).move_to([-4.2, 2.85, 0])
    linhas_cel = [VGroup(*[T(str((i * j) % 7), 24, PRETO).move_to(ponto(i, j))
                           for j in range(1, 7)]) for i in range(1, 7)]

    # a tabela entra completa, em dois tempos: a moldura, depois as linhas
    with narra(cena, "C6N01", 7.5):
        na = partial(na_palavra, cena, _agora(cena), "C6N01", 7.5)
        moldura = _etapa(
            FadeIn(titulo_tab),
            LaggedStart(*[FadeIn(h) for h in head_c], lag_ratio=0.3),
            LaggedStart(*[FadeIn(h) for h in head_l], lag_ratio=0.3),
            Create(lin_h), Create(lin_v), run_time=1.5 * VEL)
        corpo = LaggedStart(*[FadeIn(l) for l in linhas_cel], lag_ratio=0.2,
                            run_time=2.5 * VEL, introducer=True)
        cena.play(_serie(moldura, corpo))
        # "módulo sete": o sete está escrito no título da tabela
        cena.play(na("módulo sete", realce(titulo_tab)))

    # elipse verde na linha 1 (slide 59) e cópia da linha para fora da tabela
    el1 = Ellipse(width=6 * tam + 0.55, height=0.55, color=VERDE,
                  stroke_width=2.5).move_to(canto + [3.5 * tam, -1 * tam, 0])
    xsr = np.linspace(1.4, 6.4, 6)
    yA, yB = 2.05, 0.25
    A = VGroup(*[T(str(j + 1), 30, PRETO).move_to([xsr[j], yA, 0])
                 for j in range(6)])
    with narra(cena, "C6N02", 6.7):
        na = partial(na_palavra, cena, _agora(cena), "C6N02", 6.7)
        cena.play(Create(el1, run_time=0.7 * VEL),
                  LaggedStart(*[TransformFromCopy(linhas_cel[0][j], A[j])
                                for j in range(6)], lag_ratio=0.1,
                              run_time=1.5 * VEL))
        cena.play(na("sete", realce(titulo_tab)))

    # MULTIPLICAR POR 3 (slide 61): primeiro UM número (o 5), depois a linha
    # inteira. Os produtos moram na altura de B: cada um vira o próprio resto
    # no mesmo lugar.
    Bv = [3, 6, 2, 5, 1, 4]
    B = VGroup(*[T(str(Bv[j]), 30, VERMELHO).move_to([xsr[j], yB, 0])
                 for j in range(6)])
    prods = VGroup(*[formula(("3", VERMELHO), ("·" + str(j + 1), PRETO),
                             tamanho=22, buff=0.03)
                     .move_to([xsr[j], yB, 0]) for j in range(6)])
    mod_rot = fmod("7", 24).next_to(B, LEFT, buff=0.3)

    def nasce_prod(j):
        # o 3 nasce de head_l[2], o ·j do A[j]: prods[j] é o mobject que fica
        return _copia(VGroup(head_l[2], A[j]), prods[j])

    with narra(cena, "C6N03", 5.8):
        cena.play(realce(A[4], head_l[2]))
        cena.play(nasce_prod(4), run_time=1.2 * VEL)
        cena.play(FadeIn(mod_rot), ReplacementTransform(prods[4], B[4]),
                  run_time=1.0 * VEL)

    # a mesma coluna, na linha do multiplicador (slide 63): o círculo na
    # célula (3, 5) e a cópia dela caindo EXATAMENTE sobre o resto
    circ = Circle(radius=0.21, color=VERDE, stroke_width=2.5).move_to(ponto(3, 5))
    with narra(cena, "C6N04", 5.0):
        cena.play(Create(circ), realce(head_l[2], head_c[4]),
                  run_time=0.9 * VEL)
        alvo4 = _alvo(Bv[4], B[4])
        cena.play(_copia(linhas_cel[2][4], alvo4), run_time=1.2 * VEL)
        cena.play(FadeOut(alvo4), realce(B[4]))

    # a linha inteira: os cinco produtos que faltam viram o próprio resto, e
    # a linha 3 cai sobre B
    el3 = Ellipse(width=6 * tam + 0.55, height=0.55, color=VERDE,
                  stroke_width=2.5).move_to(canto + [3.5 * tam, -3 * tam, 0])
    with narra(cena, "C6N05", 5.0):
        outros = [j for j in range(6) if j != 4]
        caem = [_alvo(Bv[j], B[j]) for j in range(6)]
        cena.play(_serie(
            _etapa(LaggedStart(*[nasce_prod(j) for j in outros],
                               lag_ratio=0.15, introducer=True),
                   Create(el3), FadeOut(circ), realce(head_l[2]),
                   run_time=1.4 * VEL),
            LaggedStart(*[_vira(prods[j], B[j])
                          for j in outros], lag_ratio=0.12,
                        run_time=1.0 * VEL, introducer=True),
            LaggedStart(*[_copia(linhas_cel[2][j], caem[j])
                          for j in range(6)], lag_ratio=0.1,
                        run_time=1.1 * VEL, introducer=True),
            # até o fim do play, quem está em cena no lugar de B[j] é prods[j]
            _etapa(*[FadeOut(c) for c in caem],
                   *[realce(B[j] if j == 4 else prods[j]) for j in range(6)],
                   run_time=0.8 * VEL)))
        for j in outros:
            cena.replace(prods[j], B[j])

    # CURVAS ligando os valores iguais: A (embaixo) ao B igual (em cima)
    def arcos_de(valores):
        arcos = VGroup()
        for j in range(6):
            idx = valores.index(j + 1)
            arcos.add(ArcBetweenPoints(
                np.array([xsr[j], yA - 0.23, 0.0]),
                np.array([xsr[idx], yB + 0.23, 0.0]),
                angle=(0.65 if idx > j else -0.65),
                color=VERDE, stroke_width=2.5))
        return arcos

    arcos = arcos_de(Bv)
    with narra(cena, "C6N06", 3.8):
        na = partial(na_palavra, cena, _agora(cena), "C6N06", 3.8)
        cena.play(LaggedStart(*[Create(a) for a in arcos], lag_ratio=0.12,
                              run_time=1.8 * VEL),
                  na("Os números", realce(A, B)))

    # A VARREDURA: toda linha é um rearranjo da primeira. B e os arcos se
    # transformam no lugar (são os mesmos mobjects que a virada tira).
    def centro_linha(r):
        return canto + np.array([3.5 * tam, -r * tam, 0.0])

    with narra(cena, "C6N07", 4.6):
        etapas = []
        for r in (4, 5, 6, 2):
            v = [(r * (j + 1)) % 7 for j in range(6)]
            caem = [_alvo(v[j], B[j]) for j in range(6)]
            novos = [_alvo(v[j], B[j]) for j in range(6)]
            novos_arcos = arcos_de(v)
            etapas += [
                _etapa(_mv(el3, centro_linha(r)), realce(head_l[r - 1]),
                       run_time=0.25 * VEL),
                LaggedStart(*[_copia(linhas_cel[r - 1][j], caem[j])
                              for j in range(6)], lag_ratio=0.1,
                            run_time=0.3 * VEL, introducer=True),
                _etapa(*[Transform(B[j], novos[j]) for j in range(6)],
                       *[Transform(arcos[j], novos_arcos[j]) for j in range(6)],
                       *[FadeOut(c) for c in caem], run_time=0.25 * VEL),
            ]
        orig = arcos_de(Bv)
        etapas.append(_etapa(
            _mv(el3, centro_linha(3)),
            *[Transform(B[j], _alvo(Bv[j], B[j])) for j in range(6)],
            *[Transform(arcos[j], orig[j]) for j in range(6)],
            run_time=0.6 * VEL))
        cena.play(_serie(*etapas))

    # ------------------------------------------------------------------
    # O produto da linha 3, (3·1)…(3·6), e a extração dos 3 (slides 61–62):
    # evidencia() em ferramentas.py, a mesma do capítulo 7. O estado final é
    # o `eq` (os mesmos tokens), então nada sobra em cena.
    ev = evidencia("3", range(1, 7), [0, -2.4, 0], tam=26, mod="7")
    eq = ev.eq

    nota = T(tx("c6.comutativa"), 20, CINZA).move_to([0, -1.75, 0])
    with narra(cena, "C6N08", 5.0):
        cena.play(*ev.nasce(head_l[2], A, 2.2 * VEL, 1.4 * VEL, 0.8 * VEL),
                  FadeIn(nota, run_time=0.6 * VEL))

    # a extração dos 3: seis passos de ~0,5 s, sem pausa entre eles
    passos = ev.passos(0.5 * VEL, primeiro=[FadeOut(nota)])
    with narra(cena, "C6N09", 6.3):
        cena.play(_serie(*passos))
        # o 3 da frente (R[1]) fez o papel de 3², …, 3⁶; o eq leva o pots[6]
        cena.replace(ev.R[1], ev.pots[6])

    # dividir os dois lados pela MESMA multiplicação (slides 64–65) — a
    # narração separa em dois tempos: primeiro o porquê (inverso), depois o ato
    nota2 = T(tx("c6.dividir_os_dois_lados"), 20,
              CINZA).move_to([0, -1.75, 0])
    with narra(cena, "C6N10", 6.7):
        na = partial(na_palavra, cena, _agora(cena), "C6N10", 6.7)
        cena.play(FadeIn(nota2), run_time=0.6 * VEL)
        # "restos": a lista 1·2·3·4·5·6; "módulo": o 7 do (mod 7)
        cena.play(na("restos", realce(eq[3])))
        cena.play(na("módulo", realce(eq[4][1])))

    div_e = formula(("÷", VERDE), ("(1·2·3·4·5·6)", PRETO),
                    tamanho=20, buff=0.05).next_to(eq[1], DOWN, buff=0.2)
    div_d = formula(("÷", VERDE), ("(1·2·3·4·5·6)", PRETO),
                    tamanho=20, buff=0.05).next_to(eq[3], DOWN, buff=0.2)
    with narra(cena, "C6N11", 8.8):
        na = partial(na_palavra, cena, _agora(cena), "C6N11", 8.8)
        cena.play(na("módulo", realce(eq[4][1])))
        cena.play(na("produto inteiro",
                     Write(div_e, run_time=0.9 * VEL),
                     Write(div_d, run_time=0.9 * VEL)))

    tre2 = pot("3", "6", VERMELHO, AZUL, 34)
    resultado = VGroup(tre2, T("≡", 34, PRETO), T("1", 34, VERDE),
                       fmod("7", 32))
    resultado.arrange(RIGHT, buff=0.16).move_to([0, -2.4, 0])
    with narra(cena, "C6N12", 4.6):
        na = partial(na_palavra, cena, _agora(cena), "C6N12", 4.6)
        cena.play(ReplacementTransform(VGroup(eq, div_e, div_d), resultado),
                  FadeOut(nota2), run_time=1.1 * VEL)
        cena.play(na("potência", realce(resultado[0])))
        cena.play(na("a um", realce(resultado[2])))
        cena.play(na("sete", realce(resultado[3][1])))

    geral = VGroup(pot("a", expoente(("n", LARANJA), ("−1", PRETO), tam=28),
                       VERMELHO, tam=28),
                   T("≡", 28, PRETO), T("1", 28, VERDE), fmod("n", 26),
                   T(tx("c6.n_primo"), 22, CINZA))
    geral.arrange(RIGHT, buff=0.16).move_to([0, -3.35, 0])
    with narra(cena, "C6N13", 8.8):
        na = partial(na_palavra, cena, _agora(cena), "C6N13", 8.8)
        cena.play(Write(geral), run_time=1.2 * VEL)
        # o n do módulo e o n do expoente (geral[0][1][0]) pulsam juntos
        cena.play(na("módulo é primo", realce(geral[3][1], geral[0][1][0])))
        cena.play(na("valor a", realce(geral[0][0])))
        cena.play(na("múltiplo do módulo",
                     realce(geral[3][1], geral[0][1][0])))

    # A VIRADA: a tabela inteira e o aparato de exemplo saem, e no mesmo
    # bloco o geral sobe e cresce — sobrevivendo à limpeza — enquanto o
    # título do teorema nasce. resultado é a última coisa a sumir,
    # desaparecendo um instante depois, debaixo do geral que a generaliza.
    titulo = T(tx("geral.titulo_cap6"), 40).move_to([0, 0.9, 0])
    saida = AnimationGroup(
        FadeOut(titulo_tab), FadeOut(head_c), FadeOut(head_l),
        FadeOut(lin_h), FadeOut(lin_v), *[FadeOut(l) for l in linhas_cel],
        FadeOut(el1), FadeOut(el3), FadeOut(A), FadeOut(B),
        FadeOut(mod_rot), FadeOut(arcos),
        geral.animate.move_to([0, -0.5, 0]).scale(40 / 28),
        Write(titulo), run_time=1.0 * VEL,
    )
    with narra(cena, "C6N14", 2.9):
        cena.play(LaggedStart(saida, FadeOut(resultado, run_time=0.6 * VEL),
                              lag_ratio=0.4))

    with narra(cena, "C6N15", 6.7):
        na = partial(na_palavra, cena, _agora(cena), "C6N15", 6.7)
        cena.play(na("o módulo precisa",
                     realce(geral[3][1], geral[0][1][0])))
        cena.play(na("precisa ser primo",
                     Indicate(geral[4], color=LARANJA, run_time=1.0 * VEL)))
