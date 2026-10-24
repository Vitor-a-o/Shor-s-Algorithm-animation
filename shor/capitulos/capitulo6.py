# -*- coding: utf-8 -*-
from manim import *
import numpy as np
from functools import partial

from ..paleta import *
from ..ferramentas import *
from ..ferramentas import _agora
from ..sincronias import na_palavra

# ============================================================================
# CAPÍTULO 6 — Fermat NA TABELA multiplicativa mod 7 (slides 59–66)
#   Narração: C6N01 … C6N15 (roteiro_video3_do_teorema_ao_rsa.md)
# ============================================================================
def _etapa(*anims, **kw):
    """Uma etapa de Succession: introducer, para o que NASCE nela só entrar
    em cena na vez dela (e não no primeiro quadro do play)."""
    return AnimationGroup(*anims, introducer=True, **kw)


def _serie(*etapas):
    return Succession(*etapas, introducer=True)


def _copia(origem, alvo):
    """TransformFromCopy marcado como introducer: o alvo só aparece quando a
    animação começa, mesmo dentro de um Succession."""
    a = TransformFromCopy(origem, alvo)
    a.introducer = True
    return a


def _vira(m, alvo):
    """m assume o desenho de `alvo` — para dentro de um Succession, no lugar
    do ReplacementTransform. No Cairo, durante um play só é desenhado o que
    estava em cena quando ele começou, e o ReplacementTransform só põe o
    alvo em cena no fim do play: o alvo não aparece e a origem deformada
    fica congelada. Depois do play, cena.replace(m, alvo) troca a peça pela
    canônica (mesmo desenho, mesmo lugar)."""
    return Transform(m, alvo.copy())


def _mv(m, ponto):
    """Move m até ponto (centro) — alvo explícito, sem .animate."""
    return Transform(m, m.copy().move_to(ponto))


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
    # O produto da linha 3, (3·1)…(3·6), e a extração dos 3 (slides 61–62).
    # Cada peça é um token próprio; o estado final é o `eq` (os mesmos
    # tokens), então nada sobra em cena. O lado direito já nasce no lugar
    # final e não se mexe; o lado esquerdo se junta contra ele.
    TK = 26
    PO = {k: T("(", TK, PRETO) for k in range(1, 7)}
    PC = {k: T(")", TK, PRETO) for k in range(1, 7)}
    R = {k: T("3", TK, VERMELHO) for k in range(1, 7)}
    D = {k: T("·", TK, PRETO) for k in range(1, 7)}
    N = {k: T(str(k), TK, PRETO) for k in range(1, 7)}
    pto = {k: T("·", TK, PRETO) for k in range(2, 7)}      # os · da fila de dentro
    BO, BC = T("(", TK, PRETO), T(")", TK, PRETO)           # o parêntese grande

    meio = [D[1], BO, N[1]]
    for k in range(2, 7):
        meio += [pto[k], N[k]]
    meio.append(BC)
    tre = {m: pot("3", str(m), VERMELHO, AZUL, TK) for m in range(2, 7)}
    mid = VGroup(*meio).arrange(RIGHT, buff=0.04)
    igual = T("≡", TK, PRETO)
    rd = []
    for k in range(1, 7):
        rd += [T(str(k), TK, PRETO)] + ([T("·", TK, PRETO)] if k < 6 else [])
    ro, rc = T("(", TK, PRETO), T(")", TK, PRETO)
    rhs = VGroup(ro, *rd, rc).arrange(RIGHT, buff=0.04)
    mod7 = fmod("7", 24)
    eq = VGroup(tre[6], mid, igual, rhs, mod7)
    eq.arrange(RIGHT, buff=0.15).move_to([0, -2.4, 0])
    ref_x, ref_y = meio[-1].get_right()[0], meio[0].get_center()[1]

    def estado(m):
        """(front, tokens) do estado m da extração (0 … 6)."""
        if m == 0:
            return None, [t for k in range(1, 7)
                          for t in (PO[k], R[k], D[k], N[k], PC[k])]
        toks = [D[1], BO, N[1]]
        for i in range(2, m + 1):
            toks += [pto[i], N[i]]
        if m < 6:
            toks.append(pto[m + 1])
            for k in range(m + 1, 7):
                toks += [PO[k], R[k], D[k], N[k], PC[k]]
        toks.append(BC)
        return (R[1] if m == 1 else tre[m]), toks

    def posicoes(m):
        """centro de cada token do estado m, alinhado ao eq final. Calculado
        com cópias, com a mesma receita de arrange do eq."""
        front, toks = estado(m)
        cp = [t.copy() for t in toks]
        g = VGroup(*cp).arrange(RIGHT, buff=0.04)
        todos = list(cp)
        cf = None
        if front is not None:
            cf = front.copy()
            VGroup(cf, g).arrange(RIGHT, buff=0.15)
            todos.append(cf)
        dx, dy = ref_x - cp[-1].get_right()[0], ref_y - cp[0].get_center()[1]
        for c in todos:
            c.shift(dx * RIGHT + dy * UP)
        pos = {id(t): c.get_center() for t, c in zip(toks, cp)}
        return (None if cf is None else cf.get_center()), pos

    pos_est = [posicoes(m) for m in range(7)]
    est_tok = [estado(m) for m in range(7)]
    # estado 0: os tokens vão para o lugar antes de nascerem
    for t in est_tok[0][1]:
        t.move_to(pos_est[0][1][id(t)])

    nota = T(tx("c6.comutativa"), 20, CINZA).move_to([0, -1.75, 0])
    with narra(cena, "C6N08", 5.0):
        esq = LaggedStart(*[AnimationGroup(
            Write(PO[k]), _copia(head_l[2], R[k]), Write(D[k]),
            _copia(A[k - 1], N[k]), Write(PC[k])) for k in range(1, 7)],
            lag_ratio=0.15, run_time=2.2 * VEL)
        digs = [t for t in rd if t.text != "·"]
        dir_ = LaggedStart(*[_copia(A[j], digs[j]) for j in range(6)],
                           lag_ratio=0.1, run_time=1.4 * VEL)
        resto = AnimationGroup(
            FadeIn(igual), FadeIn(mod7), FadeIn(ro), FadeIn(rc),
            *[FadeIn(t) for t in rd if t.text == "·"], run_time=0.8 * VEL)
        cena.play(esq, dir_, resto, FadeIn(nota, run_time=0.6 * VEL))

    # a extração dos 3: seis passos de ~0,5 s, sem pausa entre eles
    passos = []
    for m in range(1, 7):
        fa, ta = est_tok[m - 1]
        fn, tn = est_tok[m]
        pa, pn = pos_est[m - 1][1], pos_est[m][1]
        pf = pos_est[m][0]
        anims = []
        if m == 1:
            anims.append(FadeOut(nota))
        for t in (PO[m], PC[m]) + ((D[m],) if m >= 2 else ()):
            anims.append(FadeOut(t))
        if m == 1:
            anims.append(_mv(R[1], pf))
        else:
            tre[m].move_to(pf)
            anims.append(FadeOut(R[m], target_position=pf))
            anims.append(_vira(R[1], tre[m]))
        antes = {id(t) for t in ta}
        for t in tn:
            if id(t) in antes:
                if np.linalg.norm(pn[id(t)] - pa[id(t)]) > 1e-3:
                    anims.append(_mv(t, pn[id(t)]))
            else:
                t.move_to(pn[id(t)])
                anims.append(Write(t))
        passos.append(_etapa(*anims, run_time=0.5 * VEL))
    with narra(cena, "C6N09", 6.3):
        cena.play(_serie(*passos))
        # o 3 da frente (R[1]) fez o papel de 3², …, 3⁶; o eq leva o tre[6]
        cena.replace(R[1], tre[6])

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
