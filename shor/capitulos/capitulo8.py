# -*- coding: utf-8 -*-
from manim import *
import numpy as np

from ..paleta import *
from ..ferramentas import *
# _ABERTURA é o ângulo do arco em cadeado.py. abrir()/fechar() são plays
# inteiros e a fase 0 precisa do travamento DENTRO do mesmo play do
# embaralhamento, então o gesto é remontado aqui a partir do mesmo ângulo.
from ..cadeado import cadeado, _ABERTURA

CARTAO_ESCURO = "#123a46"   # caixa da mensagem (azul-petróleo dos slides)


def _caixa_msg(txt, cor_fundo, cor_txt, tam=30, larg=None):
    """`larg` fixa uma largura mínima — a caixa que tranca e destranca não
    pode encolher quando o conteúdo troca (a → aᵉ, 5 → 26)."""
    f = T(txt, tam, cor_txt) if isinstance(txt, str) else txt
    r = RoundedRectangle(corner_radius=0.16,
                         width=max(larg or 0, f.width + 0.7, 1.15),
                         height=0.9, stroke_width=0)
    r.set_fill(cor_fundo, opacity=1)
    f.move_to(r)
    return VGroup(r, f)


def _olho():
    """O olho do interceptador — duas curvas em amêndoa e a pupila."""
    w = 0.75
    amendoa = VGroup(ArcBetweenPoints([-w, 0, 0], [w, 0, 0], angle=-1.3),
                     ArcBetweenPoints([-w, 0, 0], [w, 0, 0], angle=1.3))
    amendoa.set_stroke(VERMELHO, width=5)
    return VGroup(amendoa, Circle(radius=0.19, color=VERMELHO, stroke_width=4),
                  Dot(radius=0.08, color=VERMELHO))


def _chave(cor=AMARELO):
    return VGroup(Circle(radius=0.19, color=cor, stroke_width=7),
                  Line([0.19, 0, 0], [1.05, 0, 0], color=cor, stroke_width=7),
                  Line([0.70, 0, 0], [0.70, -0.24, 0], color=cor,
                       stroke_width=7),
                  Line([0.94, 0, 0], [0.94, -0.24, 0], color=cor,
                       stroke_width=7))


# ============================================================================
# O PALCO FIGURATIVO — canal, olho, cadeado
#
# A fase 0 (C8N01–C8N10) o estreia sem uma equação em cena; o esquema
# simbólico (C8N20–C8N25) e o exemplo numérico (C8N33–C8N35) REENCENAM nele,
# nas mesmas marcas e com os mesmos gestos, só que agora com aritmética
# dentro das caixas. É a repetição literal que faz um trecho ler como
# resposta ao outro — trancar/abrir são o mesmo movimento nas oito chamadas,
# e atravessar é o mesmo percurso nas oito (só o C8N06 anda ao contrário).
# ============================================================================
def _palco(cena):
    """Devolve as marcas, os mobjects do cenário e os gestos."""
    Y_CANAL, Y_CHAVE = -0.4, -1.75            # a caixa anda na linha, a chave abaixo
    X_E, X_D = -4.6, 4.6                      # pontas do trajeto
    Y_POUSO, Y_MAO = -2.30, 1.45              # chave parada / chave que tranca
    VAGAS = ([0.40, 2.62, 0], [2.85, 2.62, 0])   # prateleira do olho
    ESC_CAD = 0.32
    LARG_CORPO = 1.9 * ESC_CAD   # o corpo do cadeado é a régua de escala:
    #                              é o único pedaço do pacote que nunca muda

    # os papéis ficam nomeados nas pontas o tempo todo — sem nomes próprios
    cenario = VGroup(
        DashedLine([-6.1, Y_CANAL, 0], [6.1, Y_CANAL, 0], color=CINZA,
                   stroke_width=3, dash_length=0.22),
        Dot([-6.1, Y_CANAL, 0], radius=0.11, color=PRETO),
        Dot([6.1, Y_CANAL, 0], radius=0.11, color=PRETO),
        T("quem envia", 20, CINZA).move_to([-5.95, -1.05, 0]),
        T("canal público", 20, CINZA).move_to([0, -1.05, 0]),
        T("quem recebe", 20, CINZA).move_to([5.95, -1.05, 0]))
    olho = _olho().move_to([-2.3, 3.30, 0]).stretch(0.06, dim=1)
    prat = Line([-0.9, 2.55, 0], [3.9, 2.55, 0], color=CINZA, stroke_width=3)
    # grande de propósito: vermelho sobre vermelho só lê se ultrapassar o olho
    xis = T("✗", 78, VERMELHO).move_to([-2.3, 3.30, 0])
    prateleira = [None, None]
    olho_aberto = [False]

    # ------------------------------------------------------------- os gestos
    def pacote(conteudo, x=X_E, larg=1.45):
        """Caixa da mensagem com o cadeado ABERTO em cima, na marca x."""
        cx = _caixa_msg(conteudo, CARTAO_ESCURO, BRANCO, 28, larg)
        cx.move_to([x, Y_CANAL, 0])
        cad = cadeado("aberto").scale(ESC_CAD).next_to(cx, UP, buff=-0.06)
        return VGroup(cx, cad)

    def _troca(cx, alvo, f, letras):
        """A metamorfose do conteúdo da caixa. `letras` casa glifo a glifo —
        é o embaralhamento da fase 0, onde os dois lados têm sete."""
        alvo.scale(f).move_to(cx[0])
        if letras:
            return LaggedStart(*[Transform(g, a) for g, a in zip(cx[1], alvo)],
                               lag_ratio=0.09)
        return Transform(cx[1], alvo)

    def trancar(pac, alvo, letras=False, rt=0.9):
        """A caixa fecha: o cadeado trava com o flash seco do V1N01, o
        conteúdo vira `alvo` e o fundo vira o verde da cifra — num play só."""
        cx, cad = pac
        f = cad[1].width / LARG_CORPO
        cena.play(Rotate(cad[0], -_ABERTURA,
                         about_point=cad[0][2].get_bottom()),
                  Flash(cad[1].get_top(), color=PRETO, flash_radius=0.45 * f,
                        line_length=0.18 * f),
                  _troca(cx, alvo, f, letras),
                  cx[0].animate.set_fill(VERDE, opacity=1),
                  run_time=rt * VEL)

    def abrir(pac, alvo, letras=False, rt=0.9):
        """O inverso exato de trancar — sem flash, porque abrir é silencioso."""
        cx, cad = pac
        f = cad[1].width / LARG_CORPO
        cena.play(Rotate(cad[0], _ABERTURA,
                         about_point=cad[0][2].get_bottom()),
                  _troca(cx, alvo, f, letras),
                  cx[0].animate.set_fill(CARTAO_ESCURO, opacity=1),
                  run_time=rt * VEL)

    def atravessar(mobj, sentido=RIGHT, captura=True, vaga=0):
        """O percurso do canal, sempre no mesmo passo (rate_func linear): o
        objeto vai de uma ponta à outra e, no ponto médio, o olho leva uma
        cópia para a prateleira. sentido=LEFT é o único percurso invertido."""
        fim = X_D if sentido[0] > 0 else X_E
        cena.play(mobj.animate.set_x(0.0), run_time=1.25 * VEL,
                  rate_func=linear)
        anims = [mobj.animate.set_x(fim)]
        copia = None
        if captura:
            copia = mobj.copy()
            anims.append(copia.animate.scale(0.72)
                         .move_to(VAGAS[vaga], aligned_edge=DOWN))
            if prateleira[vaga] is not None:
                anims.append(FadeOut(prateleira[vaga]))
            prateleira[vaga] = copia
            if not olho_aberto[0]:         # a primeira captura abre o olho
                olho_aberto[0] = True
                anims += [olho.animate.stretch(1 / 0.06, dim=1), Create(prat)]
        cena.play(*anims, run_time=1.25 * VEL, rate_func=linear)
        return copia

    def piscar(cor):
        v = Rectangle(width=config.frame_width, height=config.frame_height,
                      stroke_width=0, fill_color=cor, fill_opacity=0)
        cena.play(v.animate.set_fill(cor, opacity=0.20), run_time=0.22 * VEL)
        cena.play(FadeOut(v), run_time=0.35 * VEL)

    def esvaziar():
        """FadeOuts do que estiver na prateleira, para emendar noutro play."""
        fora = [FadeOut(m) for m in prateleira if m is not None]
        prateleira[0] = prateleira[1] = None
        return fora

    return dict(cenario=cenario, olho=olho, prat=prat, xis=xis,
                prateleira=prateleira, pacote=pacote, trancar=trancar,
                abrir=abrir, atravessar=atravessar, piscar=piscar,
                esvaziar=esvaziar, VAGAS=VAGAS, X_E=X_E, X_D=X_D,
                Y_CANAL=Y_CANAL, Y_CHAVE=Y_CHAVE, Y_MAO=Y_MAO,
                Y_POUSO=Y_POUSO)


# ============================================================================
# FASE 0 — o problema que o RSA resolve (C8N01–C8N10)
#
# O MESMO trajeto rodado duas vezes: primeiro com uma chave só, que falha
# (C8N01–C8N04), depois com o par do RSA, que resiste (C8N05–C8N10).
# ============================================================================
def _fase0(cena, p):
    """Devolve o que SOBREVIVE à fase: as duas chaves (elas só viram os
    retângulos (e, n) e (d, n) no C8N22 e no C8N24), a seta de ida (de dentro
    dela nasce o L) e a seta de volta despedaçada (volta no C8N36)."""
    LEGIVEL, CIFRADO = "SEGREDO", "Xk9#R2q"   # sete glifos dos dois lados
    X_E, X_D = p["X_E"], p["X_D"]
    Y_CANAL, Y_CHAVE = p["Y_CANAL"], p["Y_CHAVE"]
    Y_MAO, Y_POUSO = p["Y_MAO"], p["Y_POUSO"]
    olho, prat, xis, prateleira = p["olho"], p["prat"], p["xis"], p["prateleira"]
    _trancar, _abrir = p["trancar"], p["abrir"]
    _atravessar, _piscar = p["atravessar"], p["piscar"]

    def _glifos(s):
        return VGroup(*[T(c, 28, BRANCO) for c in s]).arrange(RIGHT, buff=0.06)

    def _nova_caixa():
        return _caixa_msg(_glifos(LEGIVEL), CARTAO_ESCURO, BRANCO, 28)

    # === PRIMEIRA VOLTA: uma chave só ====================================
    caixa = _nova_caixa().move_to([X_E, Y_CANAL, 0])
    with narra(cena, "C8N01", 9.2):
        cena.play(FadeIn(p["cenario"]), FadeIn(olho), run_time=1.2 * VEL)
        cena.play(FadeIn(caixa, shift=0.25 * UP), run_time=0.7 * VEL)
        _atravessar(caixa, RIGHT, vaga=0)

    chave = _chave().move_to([X_E, Y_MAO, 0])
    with narra(cena, "C8N02", 8.3):
        # a viagem recomeça da esquerda, com a caixa legível outra vez
        pacote = p["pacote"](_glifos(LEGIVEL), X_E, larg=None)
        cena.play(FadeOut(caixa), FadeIn(pacote[0]), run_time=0.6 * VEL)
        cena.play(FadeIn(chave, shift=0.4 * DOWN), FadeIn(pacote[1]),
                  run_time=0.7 * VEL)
        cena.add(pacote)
        _trancar(pacote, _glifos(CIFRADO), letras=True)
        _atravessar(pacote, RIGHT, vaga=0)
        cena.play(FadeIn(xis), run_time=0.4 * VEL)

    with narra(cena, "C8N03", 8.8):
        # a mesma chave entra no canal, atrás da cifra
        cena.play(chave.animate.move_to([X_E, Y_CHAVE, 0]), run_time=0.8 * VEL)
        _atravessar(chave, RIGHT, captura=False)

    with narra(cena, "C8N04", 8.8):
        # a cópia da chave sobe do meio do canal e pousa AO LADO da cifra
        copia_ch = chave.copy().move_to([0, Y_CHAVE, 0])
        cena.play(copia_ch.animate.scale(0.72)
                  .move_to(p["VAGAS"][1], aligned_edge=DOWN),
                  run_time=1.0 * VEL)
        prateleira[1] = copia_ch
        cena.play(Indicate(copia_ch, color=AMARELO), run_time=0.6 * VEL)
        _abrir(prateleira[0], _glifos(LEGIVEL), letras=True)
        cena.play(FadeOut(xis), run_time=0.4 * VEL)
        _piscar(VERMELHO)

    # === SEGUNDA VOLTA: o par do RSA, mesmo enquadramento =================
    # duas CHAVES, não retângulos: elas só viram os cartões (e, n) e (d, n)
    # lá na frente, no C8N22 e no C8N24
    ch_pub = _chave(CINZA).move_to([X_D, -1.30, 0])
    ch_priv = _chave(AMARELO).move_to([X_D, Y_POUSO, 0])
    with narra(cena, "C8N05", 7.5):
        cena.play(FadeOut(prateleira[0]), FadeOut(prateleira[1]),
                  FadeOut(pacote), run_time=0.7 * VEL)
        prateleira[0] = prateleira[1] = None
        cena.play(Indicate(chave, color=AMARELO), run_time=0.7 * VEL)
        # a chave se parte em duas: a que tranca e a que abre
        meia1, meia2 = chave.copy(), chave.copy()
        cena.remove(chave)
        cena.add(meia1, meia2)
        cena.play(ReplacementTransform(meia1, ch_pub),
                  ReplacementTransform(meia2, ch_priv), run_time=1.3 * VEL)

    with narra(cena, "C8N06", 11.7):
        # o único objeto do capítulo que anda ao contrário
        cena.play(ch_pub.animate.move_to([X_D, Y_CANAL, 0]), run_time=0.8 * VEL)
        _atravessar(ch_pub, LEFT, vaga=1)
        cena.play(ch_pub.animate.move_to([X_E, Y_POUSO, 0]), run_time=0.8 * VEL)

    with narra(cena, "C8N07", 8.3):
        pacote = p["pacote"](_glifos(LEGIVEL), X_E, larg=None)
        cena.play(FadeIn(pacote[0], shift=0.25 * UP), FadeIn(pacote[1]),
                  run_time=0.7 * VEL)
        cena.add(pacote)
        cena.play(ch_pub.animate.move_to([X_E, Y_MAO, 0]), run_time=0.8 * VEL)
        _trancar(pacote, _glifos(CIFRADO), letras=True)
        # quem trancou também ficou de fora
        x2 = T("✗", 34, VERMELHO).next_to(pacote[1], RIGHT, buff=0.25)
        cena.play(Wiggle(pacote[1]), FadeIn(x2), run_time=1.0 * VEL)
        cena.play(FadeOut(x2), run_time=0.4 * VEL)

    with narra(cena, "C8N08", 8.3):
        # a rima com o C8N04: os mesmos dois objetos na prateleira
        _atravessar(pacote, RIGHT, vaga=0)
        cena.play(Indicate(prateleira[1], color=CINZA), run_time=0.6 * VEL)
        cena.play(Wiggle(prateleira[0][1]), FadeIn(xis), run_time=1.1 * VEL)

    with narra(cena, "C8N09", 3.3):
        # a chave amarela nunca se moveu — e é ela que abre, do lado certo
        cena.play(Indicate(ch_priv, color=AMARELO), run_time=0.7 * VEL)
        _abrir(pacote, _glifos(LEGIVEL), letras=True)
        _piscar(VERDE)

    # === a promessa que o C8N36 vai cobrar ================================
    ida = Arrow([X_E + 0.3, 0.62, 0], [X_D - 0.3, 0.62, 0], buff=0,
                color=VERDE, stroke_width=6,
                max_tip_length_to_length_ratio=0.05)
    volta = Arrow([X_D - 0.3, -1.55, 0], [-0.2, -1.55, 0], buff=0,
                  color=VERMELHO, stroke_width=6,
                  max_tip_length_to_length_ratio=0.09)
    cacos = VGroup(*[T("?", 24, CINZA).move_to([x, y, 0])
                     for x, y in ((-1.55, -1.35), (-2.15, -2.00),
                                  (-2.80, -1.42), (-3.42, -1.95),
                                  (-4.05, -1.52))])
    with narra(cena, "C8N10", 10.8):
        cena.play(FadeOut(pacote), *p["esvaziar"](), FadeOut(prat),
                  FadeOut(xis), olho.animate.set_opacity(0.3),
                  ch_pub.animate.set_opacity(0.3).move_to([X_E, Y_POUSO, 0]),
                  ch_priv.animate.set_opacity(0.3), run_time=1.0 * VEL)
        cena.play(GrowArrow(ida), run_time=0.9 * VEL)
        cena.play(GrowArrow(volta), run_time=0.9 * VEL)
        cena.play(LaggedStart(*[FadeIn(c, shift=0.25 * UP) for c in cacos],
                              lag_ratio=0.14), run_time=1.2 * VEL)

    return dict(pub=ch_pub, priv=ch_priv, ida=ida, volta=VGroup(volta, cacos))


# ============================================================================
# CAPÍTULO 8 — RSA sem relógios (slides 83–105): fórmulas que se transformam
# ============================================================================
def parte8(cena):
    # ---------- FASE 0: o problema que o RSA resolve (C8N01–C8N10) ---------
    # o palco é montado uma vez e reencenado três: aqui, no esquema
    # simbólico (C8N20–C8N25) e no exemplo numérico (C8N33–C8N35)
    p = _palco(cena)
    fase0 = _fase0(cena, p)

    # ---------- FASE A: dedução dos slides 85–88, fórmula virando fórmula ---
    L = VGroup(pot("a", expoente(("φ(", PRETO), ("n", LARANJA), (")", PRETO),
                                 tam=34), ROXO, tam=34),
               T("≡", 34, PRETO), T("1", 34, VERDE), fmod("n", 32))
    L.arrange(RIGHT, buff=0.16).move_to([0, 1.6, 0])
    # a fase 0 sai e o L NASCE DE DENTRO da seta de ida — um movimento só,
    # sem corte no meio (é a emenda que o C8N11 pede)
    cena.play(FadeOut(p["cenario"]), FadeOut(p["olho"]),
              FadeOut(fase0["volta"]), FadeOut(fase0["pub"]),
              FadeOut(fase0["priv"]),
              ReplacementTransform(fase0["ida"], L), run_time=1.2 * VEL)
    cena.wait(1.0 * VEL)

    # slide 86: multiplicamos os dois lados por a
    L2 = VGroup(T("a", 34, ROXO), T("·", 34, PRETO),
                pot("a", expoente(("φ(", PRETO), ("n", LARANJA),
                                  (")", PRETO), tam=34), ROXO, tam=34),
                T("≡", 34, PRETO), T("a", 34, ROXO), T("·", 34, PRETO),
                T("1", 34, VERDE), fmod("n", 32))
    L2.arrange(RIGHT, buff=0.16).move_to(L)
    cena.play(ReplacementTransform(L, L2), run_time=1.1 * VEL)
    cena.wait(1.0 * VEL)

    # slide 87: os expoentes se somam
    L3 = VGroup(pot("a", expoente(("φ(", PRETO), ("n", LARANJA),
                                  (") + 1", PRETO), tam=34), ROXO, tam=34),
                T("≡", 34, PRETO), T("a", 34, ROXO), fmod("n", 32))
    L3.arrange(RIGHT, buff=0.16).move_to(L2)
    cena.play(ReplacementTransform(L2, L3), run_time=1.1 * VEL)
    cena.wait(1.0 * VEL)

    # slide 88: NO EXPOENTE a aritmética é módulo φ(n)
    L4 = VGroup(pot("a", expoente(("1 (mod φ(", PRETO), ("n", LARANJA),
                                  ("))", PRETO), tam=34), ROXO, tam=34),
                T("≡", 34, PRETO), T("a", 34, ROXO), fmod("n", 32))
    L4.arrange(RIGHT, buff=0.16).move_to(L3)
    cena.play(ReplacementTransform(L3, L4), run_time=1.1 * VEL)
    cena.wait(1.0 * VEL)

    # ---------- slide 89: a TABELA multiplicativa e os pares de inversos ----
    tam = 0.38
    canto = np.array([-6.2, 1.0, 0.0])

    def ponto(i, j):
        return canto + np.array([(j + 1) * tam, -(i + 1) * tam, 0.0])

    head_c = VGroup(*[T(str(j), 17, AZUL).move_to(canto + [(j + 1) * tam, 0, 0])
                      for j in range(9)])
    head_l = VGroup(*[T(str(i), 17, VERMELHO)
                      .move_to(canto + [0, -(i + 1) * tam, 0])
                      for i in range(9)])
    lin_h = Line(canto + [0.55 * tam, -0.5 * tam, 0],
                 canto + [9.5 * tam, -0.5 * tam, 0], color=PRETO,
                 stroke_width=1.2)
    lin_v = Line(canto + [0.55 * tam, -0.5 * tam, 0],
                 canto + [0.55 * tam, -9.5 * tam, 0], color=PRETO,
                 stroke_width=1.2)
    celulas = [VGroup(*[T(str((i * j) % 9), 17, PRETO).move_to(ponto(i, j))
                        for j in range(9)]) for i in range(9)]
    tabela = VGroup(head_c, head_l, lin_h, lin_v, *celulas)
    cena.play(FadeIn(tabela), run_time=1.0 * VEL)
    uns = VGroup(*[Circle(radius=0.16, color=VERDE, stroke_width=2)
                   .move_to(ponto(i, j))
                   for i in range(1, 9) for j in range(1, 9)
                   if (i * j) % 9 == 1])
    ed = formula(("e", VERMELHO), ("·", PRETO), ("d", AZUL), ("≡", PRETO),
                 ("1", VERDE), ("(mod φ(", PRETO), ("n", LARANJA),
                 ("))", PRETO), tamanho=30, buff=0.10).move_to([3.0, -0.4, 0])
    nota = formula(("(e, d)", PRETO), ("= par de inversos", CINZA),
                   tamanho=22, buff=0.12).next_to(ed, DOWN, buff=0.3)
    cena.play(LaggedStart(*[Create(c) for c in uns], lag_ratio=0.1),
              Write(ed), run_time=1.5 * VEL)
    cena.play(FadeIn(nota), Indicate(celulas[2][5], color=VERDE),
              Indicate(celulas[5][2], color=VERDE), run_time=1.2 * VEL)
    cena.wait(1.0 * VEL)

    # slide 90: substituímos e·d no expoente
    L5 = VGroup(pot("a", expoente(("e", VERMELHO), ("·", PRETO),
                                  ("d", AZUL), tam=34), ROXO, tam=34),
                T("≡", 34, PRETO), T("a", 34, ROXO), fmod("n", 32))
    L5.arrange(RIGHT, buff=0.16).move_to(L4)
    cena.play(ReplacementTransform(L4, L5), Indicate(ed, color=VERDE),
              run_time=1.2 * VEL)

    # slide 91: rearranjando — (aᵉ)ᵈ com o expoente NO LUGAR CERTO
    par_ae = VGroup(T("(", 36, PRETO), pot("a", "e", ROXO, VERMELHO, 36),
                    T(")", 36, PRETO)).arrange(RIGHT, buff=0.04)
    L6 = VGroup(pot(par_ae, "d", None, AZUL, 36),
                T("≡", 36, PRETO), T("a", 36, ROXO), fmod("n", 34))
    L6.arrange(RIGHT, buff=0.16).move_to(L5)
    cena.play(ReplacementTransform(L5, L6), run_time=1.1 * VEL)
    cena.wait(1.0 * VEL)
    # a tabela cumpriu o papel; o e·d ≡ 1 sai de cena com ela
    cena.play(FadeOut(tabela), FadeOut(uns), FadeOut(nota), FadeOut(ed),
              run_time=0.9 * VEL)

    # ---------- FASE A2: o esquema simbólico REENCENADO NO PALCO -----------
    # é a segunda volta da fase 0 na MESMA ORDEM: quem recebe cria o par, cada
    # chave vira aritmética dentro do retângulo, a pública atravessa o canal à
    # vista do intruso, tranca a mensagem do outro lado, o pacote atravessa —
    # e só a privada, que nunca entrou no canal, devolve o a
    Y_POUSO, Y_BERCO = p["Y_POUSO"], -3.20
    pacA = p["pacote"](T("a", 32, ROXO), p["X_E"])
    ch_pub = fase0["pub"].set_opacity(1).move_to([p["X_D"], Y_POUSO, 0])
    ch_priv = fase0["priv"].set_opacity(1).move_to([p["X_D"], Y_BERCO, 0])
    cena.play(Indicate(L6[2], color=ROXO), run_time=0.7 * VEL)
    cena.play(FadeIn(p["cenario"]), FadeIn(p["olho"].set_opacity(1)),
              FadeIn(p["prat"]), FadeIn(pacA, shift=0.2 * UP),
              run_time=1.1 * VEL)

    # o par nasce inteiro na mão de QUEM RECEBE — nenhuma das duas veio de fora
    cena.play(FadeIn(ch_pub, shift=0.2 * UP), FadeIn(ch_priv, shift=0.2 * UP),
              run_time=0.8 * VEL)

    # ANTES de trancar coisa nenhuma, cada chave vira aritmética dentro do
    # retângulo: o e, o d e o n saem do próprio L6 — é a fórmula que se
    # desmonta no par de chaves
    fpub = formula(("pública", CINZA), ("(", PRETO), ("e", VERMELHO),
                   (", ", PRETO), ("n", LARANJA), (")", PRETO),
                   tamanho=22, buff=0.10)
    rpub = RoundedRectangle(corner_radius=0.14, width=fpub.width + 0.7,
                            height=0.72, stroke_color=CINZA, stroke_width=2.5)
    rpub.move_to(ch_pub)
    fpub.move_to(rpub)
    pubS = VGroup(rpub, fpub)
    cena.play(ReplacementTransform(ch_pub, rpub),
              FadeIn(fpub[0]), FadeIn(fpub[1]), FadeIn(fpub[3]),
              FadeIn(fpub[5]),
              ReplacementTransform(L6[0][0][1][1].copy(), fpub[2]),
              ReplacementTransform(L6[3][1].copy(), fpub[4]),
              run_time=1.3 * VEL)
    cena.add(pubS)

    fpriv = formula(("privada", AMARELO), ("(", PRETO), ("d", AZUL),
                    (", ", PRETO), ("n", LARANJA), (")", PRETO),
                    tamanho=22, buff=0.10)
    rpriv = RoundedRectangle(corner_radius=0.14, width=fpriv.width + 0.7,
                             height=0.72, stroke_color=AMARELO,
                             stroke_width=2.5)
    rpriv.move_to(ch_priv)
    fpriv.move_to(rpriv)
    privS = VGroup(rpriv, fpriv)
    cena.play(ReplacementTransform(ch_priv, rpriv),
              FadeIn(fpriv[0]), FadeIn(fpriv[1]), FadeIn(fpriv[3]),
              FadeIn(fpriv[5]),
              ReplacementTransform(L6[0][1].copy(), fpriv[2]),
              ReplacementTransform(L6[3][1].copy(), fpriv[4]),
              run_time=1.3 * VEL)
    cena.add(privS)

    # a pública desce para o canal e ATRAVESSA, da direita para a esquerda: o
    # olho copia e guarda, à vista, sem nenhuma consequência — nada pisca
    cena.play(pubS.animate.move_to([p["X_D"], p["Y_CANAL"], 0]),
              privS.animate.move_to([p["X_D"], Y_POUSO, 0]), run_time=0.8 * VEL)
    p["atravessar"](pubS, LEFT, vaga=1)
    cena.play(pubS.animate.move_to([p["X_E"], Y_POUSO, 0]), run_time=0.8 * VEL)

    # só agora quem envia tranca: a primeira potência É o embaralhamento
    f1s = VGroup(pot("a", "e", ROXO, VERMELHO, 24), fmod("n", 22))
    f1s.arrange(RIGHT, buff=0.12).move_to([-2.3, 0.35, 0])
    cena.play(pubS.animate.move_to([p["X_E"], p["Y_MAO"], 0]), Write(f1s),
              run_time=0.9 * VEL)
    p["trancar"](pacA, pot("a", "e", BRANCO, BRANCO, 30))
    p["atravessar"](pacA, RIGHT, vaga=0)
    # a prateleira fica com os mesmos dois objetos do C8N08: cifra e pública
    cena.play(FadeIn(p["xis"]),
              pubS.animate.move_to([p["X_E"], Y_POUSO, 0]), run_time=0.6 * VEL)

    # a segunda potência desfaz a primeira, com a chave que nunca circulou
    par_s = VGroup(T("(", 24, PRETO), pot("a", "e", ROXO, VERMELHO, 24),
                   T(")", 24, PRETO)).arrange(RIGHT, buff=0.03)
    f2s = VGroup(pot(par_s, "d", None, AZUL, 24), T("≡", 24, PRETO),
                 T("a", 24, ROXO), fmod("n", 22))
    f2s.arrange(RIGHT, buff=0.12).move_to([2.3, 0.35, 0])
    cena.play(privS.animate.move_to([p["X_D"], p["Y_MAO"], 0]), Write(f2s),
              run_time=0.9 * VEL)
    p["abrir"](pacA, T("a", 32, ROXO))
    p["piscar"](VERDE)
    cena.play(privS.animate.move_to([p["X_D"], Y_POUSO, 0]), run_time=0.6 * VEL)
    cena.wait(0.8 * VEL)

    # o esquema simbólico E a fórmula geral (aᵉ)ᵈ saem de cena:
    # o exemplo será reconstruído a partir de a^(1 (mod φ(n)))
    cena.play(FadeOut(VGroup(pacA, f1s, f2s, pubS, privS, L6)),
              FadeOut(p["cenario"]), FadeOut(p["olho"]), FadeOut(p["prat"]),
              FadeOut(p["xis"]), *p["esvaziar"](), run_time=0.9 * VEL)

    # ---------- FASE B: o exemplo dos slides 95–96 (n = 33, a = 5) ----------
    def cartao(tokens, cor, x):
        f = formula(*tokens, tamanho=22, buff=0.10)
        r = RoundedRectangle(corner_radius=0.14, width=f.width + 0.7,
                             height=0.72, stroke_color=cor, stroke_width=2.5)
        r.move_to([x, 2.55, 0])
        f.move_to(r)
        return VGroup(r, f)

    # 1) o criador escolhe o módulo: n = 33 (sem revelar de onde veio)
    esc = formula(("n", LARANJA), ("=", PRETO), ("33", LARANJA),
                  tamanho=30).move_to([0, 2.55, 0])
    cena.play(Write(esc), run_time=0.8 * VEL)

    # 2) partimos de a^(1 (mod φ(n))) ≡ a, com n = 33 — no lugar de honra
    E1 = VGroup(pot("a", expoente(("1 (mod φ(", PRETO), ("33", LARANJA),
                                  ("))", PRETO), tam=34), ROXO, tam=34),
                T("≡", 34, PRETO), T("a", 34, ROXO), fmod("33", 32))
    E1.arrange(RIGHT, buff=0.14).move_to([0, 1.6, 0])
    cena.play(Write(E1), run_time=1.0 * VEL)

    # 3) por enquanto, SÓ o valor: φ(33) = 20
    phi = formula(("φ(", PRETO), ("33", LARANJA), (")", PRETO), ("=", PRETO),
                  ("20", PRETO), tamanho=30, buff=0.08).move_to([0, 0.85, 0])
    cena.play(Write(phi), run_time=0.9 * VEL)
    E2 = VGroup(pot("a", expoente(("1 (mod ", PRETO), ("20", PRETO),
                                  (")", PRETO), tam=34), ROXO, tam=34),
                T("≡", 34, PRETO), T("a", 34, ROXO), fmod("33", 32))
    E2.arrange(RIGHT, buff=0.14).move_to(E1)
    cena.play(ReplacementTransform(E1, E2), Indicate(phi, color=LARANJA),
              run_time=1.0 * VEL)

    # 4) encontrar e e d inversos (mod 20): 3 × 7 = 21 ≡ 1 ✓  (slide 95)
    ed2 = formula(("e", VERMELHO), ("·", PRETO), ("d", AZUL), ("≡", PRETO),
                  ("1", VERDE), *MOD("20"), tamanho=28,
                  buff=0.10).move_to([0, 0.1, 0])
    cena.play(Write(ed2), run_time=0.9 * VEL)
    edn = formula(("3", VERMELHO), ("×", PRETO), ("7", AZUL), ("=", PRETO),
                  ("21", PRETO), ("≡", PRETO), ("1", VERDE),
                  *MOD("20"), ("✓", VERDE), tamanho=28).move_to(ed2)
    cena.play(ReplacementTransform(ed2, edn), run_time=1.0 * VEL)

    # as chaves NASCEM dos números encontrados: (3, 33) e (7, 33)
    pub = cartao((("pública", CINZA), ("(", PRETO), ("3", VERMELHO),
                  (", ", PRETO), ("33", LARANJA), (")", PRETO)),
                 CINZA, -3.5)
    priv = cartao((("privada", AMARELO), ("(", PRETO), ("7", AZUL),
                   (", ", PRETO), ("33", LARANJA), (")", PRETO)),
                  AMARELO, 3.5)
    cena.play(Create(pub[0]), Create(priv[0]),
              FadeIn(pub[1][0]), FadeIn(pub[1][1]), FadeIn(pub[1][3]),
              FadeIn(pub[1][5]),
              FadeIn(priv[1][0]), FadeIn(priv[1][1]), FadeIn(priv[1][3]),
              FadeIn(priv[1][5]),
              ReplacementTransform(edn[0].copy(), pub[1][2]),
              ReplacementTransform(esc[2].copy(), pub[1][4]),
              ReplacementTransform(edn[2].copy(), priv[1][2]),
              ReplacementTransform(esc[2].copy(), priv[1][4]),
              run_time=1.4 * VEL)

    # 5) a PRÓPRIA equação evolui: o 1 (mod 20) vira 3·7, que vira (a³)⁷
    E3 = VGroup(pot("a", expoente(("3", VERMELHO), ("·", PRETO),
                                  ("7", AZUL), tam=34), ROXO, tam=34),
                T("≡", 34, PRETO), T("a", 34, ROXO), fmod("33", 32))
    E3.arrange(RIGHT, buff=0.14).move_to(E2)
    cena.play(ReplacementTransform(E2, E3), Indicate(edn, color=VERDE),
              run_time=1.1 * VEL)
    cena.wait(0.6 * VEL)
    par_a3 = VGroup(T("(", 36, PRETO), pot("a", "3", ROXO, VERMELHO, 36),
                    T(")", 36, PRETO)).arrange(RIGHT, buff=0.04)
    E4 = VGroup(pot(par_a3, "7", None, AZUL, 36),
                T("≡", 36, PRETO), T("a", 36, ROXO), fmod("33", 34))
    E4.arrange(RIGHT, buff=0.16).move_to(E3)
    cena.play(ReplacementTransform(E3, E4), run_time=1.1 * VEL)
    cena.wait(0.6 * VEL)

    # …e a mensagem escolhida: a = 5
    cena.play(FadeOut(phi), FadeOut(edn), run_time=0.7 * VEL)
    msg_esc = formula(("mensagem:", CINZA), ("a", ROXO), ("=", PRETO),
                      ("5", ROXO), tamanho=26).move_to([0, 0.85, 0])
    cena.play(Write(msg_esc), run_time=0.8 * VEL)
    par_53 = VGroup(T("(", 36, PRETO), pot("5", "3", ROXO, VERMELHO, 36),
                    T(")", 36, PRETO)).arrange(RIGHT, buff=0.04)
    L7 = VGroup(pot(par_53, "7", None, AZUL, 36),
                T("≡", 36, PRETO), T("5", 36, ROXO), fmod("33", 34))
    L7.arrange(RIGHT, buff=0.16).move_to(E4)
    cena.play(ReplacementTransform(E4, L7), Indicate(msg_esc, color=ROXO),
              run_time=1.1 * VEL)
    cena.wait(1.0 * VEL)

    # ---------- o exemplo RODANDO NO MESMO PALCO (slides 93–96) ------------
    # terceira e última volta, idêntica às outras duas: o 33 sai do topo e as
    # duas chaves descem para as pontas de quem envia e de quem recebe
    pacB = p["pacote"](T("5", 30, ROXO), p["X_E"])
    # o par inteiro desce da bancada para a mão de QUEM RECEBE — os cartões
    # não são copiados, senão ficariam dois pares em cena e o de cima
    # esbarraria na prateleira do olho
    cena.play(FadeOut(esc), FadeIn(p["cenario"]), FadeIn(p["olho"]),
              FadeIn(p["prat"]), FadeIn(pacB, shift=0.2 * UP),
              pub.animate.scale(0.8).move_to([p["X_D"], p["Y_POUSO"], 0]),
              priv.animate.scale(0.8).move_to([p["X_D"], -3.20, 0]),
              run_time=1.2 * VEL)

    # a (3, 33) atravessa o canal à vista do intruso, como no esquema
    cena.play(pub.animate.move_to([p["X_D"], p["Y_CANAL"], 0]),
              priv.animate.move_to([p["X_D"], p["Y_POUSO"], 0]),
              run_time=0.8 * VEL)
    p["atravessar"](pub, LEFT, vaga=1)
    cena.play(pub.animate.move_to([p["X_E"], p["Y_POUSO"], 0]),
              run_time=0.8 * VEL)

    # criptografar: qualquer um com a chave PÚBLICA (3, 33)
    f1 = VGroup(pot("5", "3", ROXO, VERMELHO, 22), T("≡", 22, PRETO),
                T("26", 22, VERDE), fmod("33", 20))
    f1.arrange(RIGHT, buff=0.08).move_to([-2.3, 0.35, 0])
    cena.play(pub.animate.move_to([p["X_E"], p["Y_MAO"], 0]), Write(f1),
              run_time=0.9 * VEL)
    p["trancar"](pacB, T("26", 30, BRANCO))
    p["atravessar"](pacB, RIGHT, vaga=0)
    # a prateleira fica com a cifra e a (3, 33) — e nenhuma das duas abre
    cena.play(FadeIn(p["xis"]),
              pub.animate.move_to([p["X_E"], p["Y_POUSO"], 0]),
              run_time=0.6 * VEL)

    # descriptografar: SÓ quem tem a chave PRIVADA (7, 33)
    f2 = VGroup(pot("26", "7", VERDE, AZUL, 22), T("≡", 22, PRETO),
                T("5", 22, ROXO), fmod("33", 20))
    f2.arrange(RIGHT, buff=0.08).move_to([2.3, 0.35, 0])
    cena.play(priv.animate.move_to([p["X_D"], p["Y_MAO"], 0]), Write(f2),
              run_time=0.9 * VEL)
    p["abrir"](pacB, T("5", 30, ROXO))
    p["piscar"](VERDE)
    cena.play(priv.animate.move_to([p["X_D"], p["Y_POUSO"], 0]),
              run_time=0.6 * VEL)

    # cadeia final de verificação (slide 96) — SÓ fórmulas, sem retas
    par_f = VGroup(T("(", 28, PRETO), pot("5", "3", ROXO, VERMELHO, 28),
                   T(")", 28, PRETO)).arrange(RIGHT, buff=0.04)
    fim2 = VGroup(pot(par_f, "7", None, AZUL, 28), T("=", 28, PRETO),
                  pot("5", "21", ROXO, PRETO, 28), T("=", 28, PRETO),
                  pot("5", "20", ROXO, PRETO, 28), T("·", 28, PRETO),
                  T("5", 28, ROXO), T("≡", 28, PRETO), T("1", 28, VERDE),
                  T("·", 28, PRETO), T("5", 28, ROXO), T("≡", 28, PRETO),
                  T("5", 28, ROXO), fmod("33", 26))
    fim2.arrange(RIGHT, buff=0.14).move_to([0, -3.0, 0])
    cena.play(Write(fim2), run_time=1.3 * VEL)
    par_f2 = VGroup(T("(", 32, PRETO), pot("5", "3", ROXO, VERMELHO, 32),
                    T(")", 32, PRETO)).arrange(RIGHT, buff=0.04)
    fim3 = VGroup(pot(par_f2, "7", None, AZUL, 32), T("≡", 32, PRETO),
                  T("5", 32, ROXO), fmod("33", 30), T("✓", 32, VERDE))
    fim3.arrange(RIGHT, buff=0.16).move_to(fim2)
    cena.play(ReplacementTransform(fim2, fim3), run_time=1.1 * VEL)
    cena.wait(1.0 * VEL)

    # ---------- FASE C: a segurança (slides 97–104) ----------
    cena.play(FadeOut(VGroup(pacB, f1, f2, pub, priv, fim3, msg_esc)),
              FadeOut(p["cenario"]), FadeOut(p["olho"]), FadeOut(p["prat"]),
              FadeOut(p["xis"]), *p["esvaziar"](), run_time=0.8 * VEL)
    c1 = formula(("achar", PRETO), ("d", AZUL), ("⇒", PRETO),
                 ("achar", PRETO), ("φ(", PRETO), ("n", LARANJA),
                 (")", PRETO), tamanho=30, buff=0.12).move_to([0, 0.6, 0])
    cena.play(Write(c1), run_time=0.9 * VEL)

    # slide 100: n primo entrega φ(n) de graça — não serve
    c2 = formula(("n", LARANJA), ("primo:", PRETO), ("φ(", PRETO),
                 ("n", LARANJA), (")", PRETO), ("=", PRETO), ("n", LARANJA),
                 ("− 1", PRETO), ("✗", VERMELHO),
                 tamanho=28, buff=0.10).move_to([0, -0.4, 0])
    cena.play(Write(c2), run_time=0.9 * VEL)

    # slides 101–104: com n = p × q, só o criador conhece φ(n)
    c3 = formula(("n", LARANJA), ("=", PRETO), ("p", ROSA), ("×", PRETO),
                 ("q", VERDE2), ("⇒", PRETO), ("φ(", PRETO), ("n", LARANJA),
                 (")", PRETO), ("=", PRETO), ("(", PRETO), ("p", ROSA),
                 ("− 1)", PRETO), ("×", PRETO), ("(", PRETO), ("q", VERDE2),
                 ("− 1)", PRETO), ("✓", VERDE),
                 tamanho=28, buff=0.08).move_to([0, -1.4, 0])
    cena.play(Write(c3), run_time=1.1 * VEL)

    c4 = formula(("quebrar RSA", PRETO), ("=", PRETO), ("fatorar", PRETO),
                 ("n", LARANJA), tamanho=32).move_to([0, -2.6, 0])
    caixa = SurroundingRectangle(c4, color=VERDE, buff=0.2,
                                 corner_radius=0.14)
    cena.play(Write(c4), Create(caixa), run_time=1.1 * VEL)
    cena.wait(1.8 * VEL)
