# -*- coding: utf-8 -*-
from manim import *
import numpy as np
from functools import partial
from manim.animation.animation import prepare_animation

from ..paleta import *
from ..ferramentas import *
from ..ferramentas import _agora
from ..sincronias import na_palavra, _ate
# _ABERTURA é o ângulo do arco em cadeado.py. abrir()/fechar() são plays
# inteiros e a fase 0 precisa do travamento DENTRO do mesmo play do
# embaralhamento, então o gesto é remontado aqui a partir do mesmo ângulo.
from ..cadeado import cadeado, _ABERTURA


def _antes_de(cena, t0, tag, est, ancora, dur_gesto):
    """Espera até a palavra `ancora` para um gesto de `dur_gesto` segundos que
    vem logo depois (o trancar/abrir do palco, que não aceitam espera),
    encurtada como no na_palavra: o gesto acaba até o fim da fala + PAD.
    Devolve o Wait para `cena.play`, ou None se não há o que esperar."""
    espera = _ate(cena, t0, tag, est, ancora)
    sobra = (DUR.get(tag, est) + PAD - 0.1 - (_agora(cena) - t0)
             - dur_gesto)
    espera.run_time = max(0.0, min(espera.run_time, sobra))
    return espera if espera.run_time > 0.02 else None


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


LEGIVEL, CIFRADO = tx("c8.segredo"), "Xk9#R2q"   # sete glifos dos dois lados


def _glifos(s):
    """Os glifos da mensagem, um mobject por caractere — a fase 0 casa os sete
    de um lado com os sete do outro, e o C8N12 os colapsa dentro do `a`."""
    return VGroup(*[T(c, 28, BRANCO) for c in s]).arrange(RIGHT, buff=0.06)


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
    Y_CANAL = -0.4                            # tudo o que atravessa anda na linha
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
        T(tx("c8.quem_envia"), 20, CINZA).move_to([-5.95, -1.05, 0]),
        T(tx("c8.canal_publico"), 20, CINZA).move_to([0, -1.05, 0]),
        T(tx("c8.quem_recebe"), 20, CINZA).move_to([5.95, -1.05, 0]))
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

    def atravessar(mobj, sentido=RIGHT, captura=True, vaga=0, fim=None,
                   rt=1.25, junto=None):
        """O percurso do canal, sempre no mesmo passo (rate_func linear): o
        objeto vai de uma ponta à outra e, no ponto médio, o olho leva uma
        cópia para a prateleira. sentido=LEFT é o único percurso invertido.
        `fim` encurta a chegada quando a ponta já está ocupada.
        `rt` é o tempo de CADA metade: a fase 0 anda mais devagar, porque é
        cena figurativa sob falas longas; da fase A2 em diante o trânsito é
        citação e tem de caber em falas de 4,6 s."""
        if fim is None:
            fim = X_D if sentido[0] > 0 else X_E
        # `junto(i)`: animações extras (os realces na palavra) que entram no
        # play da metade i (1 ou 2). O run_time do play sobrescreveria o do
        # Wait delas, então com extras cada animação leva o seu; sem `junto`
        # o play é o de sempre
        def jogar(anims, i):
            extras = junto(i) if junto else []
            if not extras:
                cena.play(*anims, run_time=rt * VEL, rate_func=linear)
                return
            anims = [prepare_animation(a) for a in anims]
            for a in anims:
                a.run_time, a.rate_func = rt * VEL, linear
            cena.play(*anims, *extras)

        jogar([mobj.animate.set_x(0.0)], 1)
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
        jogar(anims, 2)
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
                Y_CANAL=Y_CANAL, Y_MAO=Y_MAO,
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
    X_E, X_D = p["X_E"], p["X_D"]
    Y_CANAL = p["Y_CANAL"]
    Y_MAO, Y_POUSO = p["Y_MAO"], p["Y_POUSO"]
    olho, prat, xis, prateleira = p["olho"], p["prat"], p["xis"], p["prateleira"]
    _trancar, _abrir = p["trancar"], p["abrir"]
    _atravessar, _piscar = p["atravessar"], p["piscar"]
    # a travessia da fase 0 é lenta: são falas de 8 a 14 s sobre uma cena
    # figurativa, e o percurso é o que o espectador tem para olhar
    RT_CANAL = 2.0

    def _nova_caixa():
        return _caixa_msg(_glifos(LEGIVEL), CARTAO_ESCURO, BRANCO, 28)

    # === PRIMEIRA VOLTA: uma chave só ====================================
    caixa = _nova_caixa().move_to([X_E, Y_CANAL, 0])
    with narra(cena, "C8N01", 9.2):
        cena.play(FadeIn(p["cenario"]), FadeIn(olho), run_time=1.2 * VEL)
        cena.play(FadeIn(caixa, shift=0.25 * UP), run_time=0.7 * VEL)
        _atravessar(caixa, RIGHT, vaga=0, rt=RT_CANAL)

    chave = _chave().move_to([X_E, Y_MAO, 0])
    with narra(cena, "C8N02", 8.3):
        # a viagem recomeça da esquerda, com a caixa legível outra vez — e a
        # prateleira zera junto: a captura da volta anterior sai com o original
        pacote = p["pacote"](_glifos(LEGIVEL), X_E, larg=None)
        cena.play(FadeOut(caixa), *p["esvaziar"](), FadeIn(pacote[0]),
                  run_time=0.6 * VEL)
        cena.play(FadeIn(chave, shift=0.4 * DOWN), FadeIn(pacote[1]),
                  run_time=0.7 * VEL)
        cena.add(pacote)
        _trancar(pacote, _glifos(CIFRADO), letras=True)
        _atravessar(pacote, RIGHT, vaga=0, rt=RT_CANAL)
        cena.play(FadeIn(xis), run_time=0.4 * VEL)

    with narra(cena, "C8N03", 8.8):
        # a mesma chave entra no canal, PELO TRACEJADO — mesmo percurso e mesma
        # velocidade da caixa, e o olho a copia no meio do caminho, como copiou
        # a cifra. Ela para antes da ponta: a cifra já ocupa a marca
        cena.play(chave.animate.move_to([X_E, Y_CANAL, 0]), run_time=0.8 * VEL)
        _atravessar(chave, RIGHT, vaga=1, fim=X_D - 2.2, rt=RT_CANAL)
        # e desce para baixo da cifra, no meio das duas marcas em que o par do
        # C8N05 vai pousar: a chave já espera no lugar onde ela vai se partir
        cena.play(chave.animate.move_to([X_D, 0.5 * (-1.30 + Y_POUSO), 0]),
                  run_time=0.8 * VEL)

    with narra(cena, "C8N04", 8.8):
        # os dois objetos capturados, juntos, na prateleira do olho
        cena.play(Indicate(prateleira[1], color=AMARELO), run_time=0.6 * VEL)
        # a fala afirma o gesto, então a tela tem de executá-lo: a chave
        # capturada sobe da vaga até o cadeado capturado, abre, e volta para a
        # vaga. É a ida que o C8N08 vai inverter — sem ela a inversão não lê
        vaga_ch = prateleira[1].get_center()
        cena.play(prateleira[1].animate.next_to(prateleira[0][1], LEFT,
                                                buff=0.06),
                  run_time=0.8 * VEL)
        _abrir(prateleira[0], _glifos(LEGIVEL), letras=True)
        cena.play(prateleira[1].animate.move_to(vaga_ch), run_time=0.6 * VEL)
        cena.play(FadeOut(xis), run_time=0.4 * VEL)
        _piscar(VERMELHO)

    # === SEGUNDA VOLTA: o par do RSA, mesmo enquadramento =================
    # duas CHAVES, não retângulos: elas só viram os cartões (e, n) e (d, n)
    # lá na frente, no C8N22 e no C8N24
    ch_pub = _chave(CINZA).move_to([X_D, -1.30, 0])
    ch_priv = _chave(AMARELO).move_to([X_D, Y_POUSO, 0])
    with narra(cena, "C8N05", 8.3):
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

    with narra(cena, "C8N06", 14.0):
        # o único objeto do capítulo que anda ao contrário
        cena.play(ch_pub.animate.move_to([X_D, Y_CANAL, 0]), run_time=1.1 * VEL)
        # a fala mais longa do capítulo, e o percurso é o argumento inteiro
        # da assimetria: anda ainda mais devagar que o resto da fase
        _atravessar(ch_pub, LEFT, vaga=1, rt=2.8)
        cena.play(ch_pub.animate.move_to([X_E, Y_POUSO, 0]), run_time=1.1 * VEL)

    with narra(cena, "C8N07", 8.3):
        pacote = p["pacote"](_glifos(LEGIVEL), X_E, larg=None)
        cena.play(FadeIn(pacote[0], shift=0.25 * UP), FadeIn(pacote[1]),
                  run_time=0.7 * VEL)
        cena.add(pacote)
        cena.play(ch_pub.animate.move_to([X_E, Y_MAO, 0]), run_time=0.8 * VEL)
        _trancar(pacote, _glifos(CIFRADO), letras=True)
        # a chave cinza TENTA voltar atrás: o arco cede no sentido de abrir e
        # volta antes de soltar. O Wiggle é o cadeado reclamando; isto aqui é
        # a chave tentando, que é o que a fala afirma
        arco = pacote[1][0]
        piv = arco[2].get_bottom()
        cena.play(Rotate(arco, 0.35 * _ABERTURA, about_point=piv),
                  run_time=0.25 * VEL)
        cena.play(Rotate(arco, -0.35 * _ABERTURA, about_point=piv),
                  run_time=0.25 * VEL)
        # quem trancou também ficou de fora
        x2 = T("✗", 34, VERMELHO).next_to(pacote[1], RIGHT, buff=0.25)
        cena.play(Wiggle(pacote[1]), FadeIn(x2), run_time=1.0 * VEL)
        cena.play(FadeOut(x2), run_time=0.4 * VEL)

    with narra(cena, "C8N08", 9.5):
        # a rima com o C8N04: os mesmos dois objetos na prateleira
        _atravessar(pacote, RIGHT, vaga=0, rt=RT_CANAL)
        cena.play(Indicate(prateleira[1], color=CINZA), run_time=0.6 * VEL)
        cena.play(Wiggle(prateleira[0][1]), FadeIn(xis), run_time=1.1 * VEL)

    with narra(cena, "C8N09", 7.0):
        # a chave amarela nunca entrou no canal: acende parada na ponta e SOBE
        # até o cadeado, o mesmo gesto com que a cinza desceu para trancar
        cena.play(Indicate(ch_priv, color=AMARELO), run_time=0.6 * VEL)
        cena.play(ch_priv.animate.move_to([X_D, Y_MAO, 0]), run_time=0.7 * VEL)
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
                  ch_priv.animate.set_opacity(0.3).move_to([X_D, Y_POUSO, 0]),
                  run_time=1.0 * VEL)
        cena.play(GrowArrow(ida), run_time=0.9 * VEL)
        cena.play(GrowArrow(volta), run_time=0.9 * VEL)
        cena.play(LaggedStart(*[FadeIn(c, shift=0.25 * UP) for c in cacos],
                              lag_ratio=0.14), run_time=1.2 * VEL)

    return dict(pub=ch_pub, priv=ch_priv, ida=ida, volta=VGroup(volta, cacos))


# ============================================================================
# A TABELA MULTIPLICATIVA DA FASE C (C8N36–C8N46)
#
# É a mesma grade do C8N17, agora com o módulo variável — e é ela que carrega
# o argumento de segurança inteiro. A leitura é sempre a mesma: a linha e a
# coluna são os dois expoentes, e um 1 dentro da grade é um par de inversos.
# Linha SEM nenhum 1 = número que compartilha fator com o módulo. Contar as
# linhas que TÊM um 1 é, portanto, calcular φ do módulo — o fato de onde a
# dificuldade inteira vem, e que só a grade mostra acontecendo.
#
# A legenda mora EM CIMA da grade, em duas linhas: a primeira diz em que
# módulo a tabela vive (φ(n) enquanto o assunto é inverter, n a partir do
# C8N38, quando vira contar) e a segunda carrega o caso da vez — o módulo
# crescendo no C8N39, o lugar vazio do módulo no C8N40, o primo no C8N41,
# o p × q montado no C8N42.
# ============================================================================
_TAB_LADO = 4.8                                # lado do quadrado da grade
_TAB_CANTO = np.array([-6.50, 2.00, 0.0])      # célula (0, 0): os cabeçalhos
_TAB_MEIO = _TAB_CANTO[0] + 0.47 * _TAB_LADO   # eixo vertical da grade
_TAB_MEIOY = _TAB_CANTO[1] - 0.47 * _TAB_LADO  # eixo horizontal da grade


def _tab_passo(m):
    """Passo da grade e o ponto da célula (i, j) — a faixa 0 é o cabeçalho.
    O quadrado é FIXO: quem muda com o módulo é o tamanho da célula."""
    tam = _TAB_LADO / m
    return tam, lambda i, j: _TAB_CANTO + np.array([j * tam, -i * tam, 0.0])


def _tab_malha(m, w=0.9):
    """Só a grade das células 1…m−1. É ela que adensa no C8N39: os dígitos
    saem e o que cresce sozinho é a malha."""
    tam, ponto = _tab_passo(m)
    a = ponto(1, 1) + np.array([-0.5 * tam, 0.5 * tam, 0.0])
    L = (m - 1) * tam
    return VGroup(
        *[Line(a + [0, -k * tam, 0], a + [L, -k * tam, 0], color=CINZA,
               stroke_width=w) for k in range(m)],
        *[Line(a + [k * tam, 0, 0], a + [k * tam, -L, 0], color=CINZA,
               stroke_width=w) for k in range(m)])


def _tabela(m):
    """Tabela multiplicativa (mod m) inteira. Cabeçalho de linha VERMELHO e
    de coluna AZUL — as cores do e e do d desde o C8N17."""
    tam, ponto = _tab_passo(m)
    f = max(int(47 * tam), 9)
    col = VGroup(*[T(str(j), f, AZUL).move_to(ponto(0, j))
                   for j in range(1, m)])
    lin = VGroup(*[T(str(i), f, VERMELHO).move_to(ponto(i, 0))
                   for i in range(1, m)])
    cel = VGroup(*[VGroup(*[T(str(i * j % m), f, PRETO).move_to(ponto(i, j))
                            for j in range(1, m)]) for i in range(1, m)])
    return VGroup(_tab_malha(m), col, lin, cel)


def _tab_col(t, j):
    return t[1][j - 1]


def _tab_lin(t, i):
    return t[2][i - 1]


def _tab_cel(t, i, j):
    return t[3][i - 1][j - 1]


def _tab_uns(m):
    """Os 1 da grade — exatamente um por linha invertível, nenhum nas outras.
    Contá-los é contar φ(m)."""
    tam, ponto = _tab_passo(m)
    return VGroup(*[Circle(radius=0.34 * tam, color=VERDE,
                           stroke_width=max(1.4, 6 * tam)).move_to(ponto(i, j))
                    for i in range(1, m) for j in range(1, m)
                    if i * j % m == 1])


def _tab_risco(m, i, cor):
    """O risco da linha inteira: o número que compartilha fator com o módulo
    e não tem 1 nenhum para ser inverso de ninguém."""
    tam, ponto = _tab_passo(m)
    return Line(ponto(i, 0) + np.array([-0.42 * tam, 0, 0]),
                ponto(i, m - 1) + np.array([0.45 * tam, 0, 0]),
                color=cor, stroke_width=max(2.0, 9 * tam))


def _tab_sem_um(m):
    """As linhas riscadas: as que compartilham fator com o módulo."""
    return [i for i in range(1, m) if np.gcd(i, m) > 1]


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
    with narra(cena, "C8N11", 8.8):
        # a fase 0 sai e o L NASCE DE DENTRO da seta de ida — um movimento só,
        # sem corte no meio
        cena.play(FadeOut(p["cenario"]), FadeOut(p["olho"]),
                  FadeOut(fase0["volta"]), FadeOut(fase0["pub"]),
                  FadeOut(fase0["priv"]),
                  ReplacementTransform(fase0["ida"], L), run_time=2.5 * VEL)
        # o gancho que o C7N15 deixou: o expoente que a fala vai manipular
        cena.play(Indicate(L[0][1], color=LARANJA), run_time=0.9 * VEL)

    # slide 86: multiplicamos os dois lados por a
    L2 = VGroup(T("a", 34, ROXO), T("·", 34, PRETO),
                pot("a", expoente(("φ(", PRETO), ("n", LARANJA),
                                  (")", PRETO), tam=34), ROXO, tam=34),
                T("≡", 34, PRETO), T("a", 34, ROXO), T("·", 34, PRETO),
                T("1", 34, VERDE), fmod("n", 32))
    L2.arrange(RIGHT, buff=0.16).move_to(L)
    # a ponte texto→número: a caixa SEGREDO da fase 0 volta pequena e os sete
    # glifos colapsam DENTRO do a. É a única vez que a mensagem figurativa
    # encosta na álgebra, e a fala não tem outra imagem para se apoiar
    msg_fig = _caixa_msg(_glifos(LEGIVEL), CARTAO_ESCURO, BRANCO, 28)
    msg_fig.scale(0.55).next_to(L, LEFT, buff=0.8)
    with narra(cena, "C8N12", 8.3):
        na = partial(na_palavra, cena, _agora(cena), "C8N12", 8.3)
        cena.play(FadeIn(msg_fig, shift=0.25 * RIGHT), run_time=0.6 * VEL)
        cena.play(LaggedStart(*[FadeOut(g, target_position=L[0][0], scale=0.3)
                                for g in msg_fig[1]], lag_ratio=0.12),
                  # a caixa sai antes dos glifos: eles têm de viajar no branco
                  Succession(FadeOut(msg_fig[0], scale=0.9), Wait()),
                  run_time=1.2 * VEL)
        cena.remove(msg_fig)
        # a única parada da dedução para dizer o que a letra é
        cena.play(na("número a",
                     Indicate(L[0][0], color=ROXO, run_time=0.7 * VEL)))
        cena.play(na("Multiplicamos",
                     ReplacementTransform(L, L2, run_time=1.1 * VEL)))

    # slide 87: os expoentes se somam
    L3 = VGroup(pot("a", expoente(("φ(", PRETO), ("n", LARANJA),
                                  (") + 1", PRETO), tam=34), ROXO, tam=34),
                T("≡", 34, PRETO), T("a", 34, ROXO), fmod("n", 32))
    L3.arrange(RIGHT, buff=0.16).move_to(L2)
    with narra(cena, "C8N13", 2.9):
        na = partial(na_palavra, cena, _agora(cena), "C8N13", 2.9)
        cena.play(na("se somam",
                     ReplacementTransform(L2, L3, run_time=1.1 * VEL)))

    # slide 88: NO EXPOENTE a aritmética é módulo φ(n)
    L4 = VGroup(pot("a", expoente(("1 (mod φ(", PRETO), ("n", LARANJA),
                                  ("))", PRETO), tam=34), ROXO, tam=34),
                T("≡", 34, PRETO), T("a", 34, ROXO), fmod("n", 32))
    L4.arrange(RIGHT, buff=0.16).move_to(L3)
    with narra(cena, "C8N14", 6.7):
        na = partial(na_palavra, cena, _agora(cena), "C8N14", 6.7)
        cena.play(na("expoente", realce(*L3[0][1])))
        cena.play(na("reescrito",
                     ReplacementTransform(L3, L4, run_time=1.1 * VEL)))
        # os dois mod na tela ao mesmo tempo: a hierarquia tem que ser VISTA
        cena.play(na("fi de ene",
                     Indicate(L4[3], color=LARANJA, run_time=1.0 * VEL),
                     Indicate(L4[0][1], color=LARANJA, run_time=1.0 * VEL)))

    with narra(cena, "C8N15", 8.8):
        na = partial(na_palavra, cena, _agora(cena), "C8N15", 8.8)
        cena.play(na("Qualquer expoente", realce(*L4[0][1])))
        cena.play(na("mensagem", realce(L4[2])))

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
    grade = VGroup(head_c, head_l, lin_h, lin_v, *celulas)
    # a legenda diz em que módulo a tabela vive — sem ela, a grade fica ao lado
    # de um (mod n) e os dois módulos se confundem
    legenda = formula((tx("c8.tabela_multiplicativa") + " ", CINZA), ("(mod φ(", PRETO),
                      ("n", LARANJA), ("))", PRETO),
                      tamanho=20, buff=0.06).next_to(grade, DOWN, buff=0.30)
    tabela = VGroup(grade, legenda)
    # enquanto a tabela está em cena o único módulo escrito é o do expoente:
    # o "≡ a (mod n)" sai aqui e volta no C8N18, com o L5
    dir4 = VGroup(L4[1], L4[2], L4[3])
    with narra(cena, "C8N16", 5.0):
        na = partial(na_palavra, cena, _agora(cena), "C8N16", 5.0)
        cena.play(FadeIn(tabela), FadeOut(dir4), run_time=2.0 * VEL)
        # "expoente": o (mod φ(n)) da legenda, token a token
        cena.play(na("expoente", realce(legenda[1], legenda[2], legenda[3])))
    L4.remove(*dir4)

    uns = VGroup(*[Circle(radius=0.16, color=VERDE, stroke_width=2)
                   .move_to(ponto(i, j))
                   for i in range(1, 9) for j in range(1, 9)
                   if (i * j) % 9 == 1])
    ed = formula(("e", VERMELHO), ("·", PRETO), ("d", AZUL), ("≡", PRETO),
                 ("1", VERDE), ("(mod φ(", PRETO), ("n", LARANJA),
                 ("))", PRETO), tamanho=30, buff=0.10).move_to([3.0, -0.4, 0])
    nota = formula(("(e, d)", PRETO), (tx("c8.par_de_inversos"), CINZA),
                   tamanho=22, buff=0.12).next_to(ed, DOWN, buff=0.3)
    with narra(cena, "C8N17", 9.2):
        na = partial(na_palavra, cena, _agora(cena), "C8N17", 9.2)
        # a fala descreve exatamente os círculos nascendo, um a um: eles
        # precisam de lag para serem contados, não de simultaneidade. Os
        # realces entram no mesmo play (cada peça com o próprio run_time: o
        # do play sobrescreveria o do Wait); as três âncoras caem depois dos
        # 4,5 s da escrita, então nada pulsa o que ainda está sendo escrito
        cena.play(LaggedStart(*[Create(c) for c in uns], lag_ratio=0.22,
                              run_time=4.5 * VEL),
                  Write(ed, run_time=4.5 * VEL),
                  FadeIn(nota, run_time=4.5 * VEL),
                  na("dois números",
                     Indicate(celulas[2][5], color=VERDE, run_time=0.6 * VEL),
                     Indicate(celulas[5][2], color=VERDE, run_time=0.6 * VEL)),
                  na("dê um", realce(ed[4])),
                  na("módulo do expoente", realce(ed[5], ed[6], ed[7])))

    # slide 90: substituímos e·d no expoente
    L5 = VGroup(pot("a", expoente(("e", VERMELHO), ("·", PRETO),
                                  ("d", AZUL), tam=34), ROXO, tam=34),
                T("≡", 34, PRETO), T("a", 34, ROXO), fmod("n", 32))
    L5.arrange(RIGHT, buff=0.16).move_to([0, 1.6, 0])
    with narra(cena, "C8N18", 2.9):
        na = partial(na_palavra, cena, _agora(cena), "C8N18", 2.9)
        # o lado direito guardado no C8N16 volta junto com o e·d no expoente
        cena.play(na("par", Indicate(ed, color=VERDE, run_time=1.2 * VEL)),
                  na("expoente",
                     ReplacementTransform(L4[0], L5[0], run_time=1.2 * VEL),
                     FadeIn(VGroup(L5[1], L5[2], L5[3]), shift=0.2 * RIGHT,
                            run_time=1.2 * VEL)))

    # slide 91: rearranjando — (aᵉ)ᵈ com o expoente NO LUGAR CERTO
    par_ae = VGroup(T("(", 36, PRETO), pot("a", "e", ROXO, VERMELHO, 36),
                    T(")", 36, PRETO)).arrange(RIGHT, buff=0.04)
    L6 = VGroup(pot(par_ae, "d", None, AZUL, 36),
                T("≡", 36, PRETO), T("a", 36, ROXO), fmod("n", 34))
    L6.arrange(RIGHT, buff=0.16).move_to(L5)
    with narra(cena, "C8N19", 8.8):
        na = partial(na_palavra, cena, _agora(cena), "C8N19", 8.8)
        cena.play(na("produto no expoente", realce(*L5[0][1])))
        # a tabela cumpriu o papel e sai NO MESMO play em que o produto do
        # expoente vira duas potências encadeadas
        cena.play(na("potência de outra potência",
                     ReplacementTransform(L5, L6, run_time=1.2 * VEL),
                     FadeOut(tabela, run_time=1.2 * VEL),
                     FadeOut(uns, run_time=1.2 * VEL),
                     FadeOut(nota, run_time=1.2 * VEL),
                     FadeOut(ed, run_time=1.2 * VEL)))
        # o par de setas do C8N10 virando álgebra — uma de cada vez: são duas
        # operações encadeadas, e o par só é lido como par se houver silêncio
        # entre elas. O silêncio é o intervalo entre as duas palavras, e cada
        # pulso dura 0,6 s para caber nele
        cena.play(na("uma desfazendo",
                     Indicate(L6[0][0][1][1], color=VERMELHO,
                              run_time=0.6 * VEL)))
        cena.play(na("a outra",
                     Indicate(L6[0][1], color=AZUL, run_time=0.6 * VEL)))

    # ---------- FASE A2: o esquema simbólico REENCENADO NO PALCO -----------
    # é a segunda volta da fase 0 na MESMA ORDEM: quem recebe cria o par, a
    # pública atravessa o canal à vista do intruso, tranca a mensagem do outro
    # lado, o pacote atravessa — e só a privada, que nunca entrou no canal,
    # devolve o a. O que mudou em relação à fase 0 é QUANDO cada chave vira
    # aritmética: a metamorfose acontece no play em que a fala nomeia a peça,
    # depois de ela já ter feito o serviço
    Y_POUSO, Y_BERCO = p["Y_POUSO"], -3.20
    pacA = p["pacote"](T("a", 32, ROXO), p["X_E"])
    ch_pub = fase0["pub"].set_opacity(1).move_to([p["X_D"], Y_POUSO, 0])
    ch_priv = fase0["priv"].set_opacity(1).move_to([p["X_D"], Y_BERCO, 0])
    with narra(cena, "C8N20", 4.2):
        na = partial(na_palavra, cena, _agora(cena), "C8N20", 4.2)
        cena.play(FadeIn(p["cenario"]), FadeIn(p["olho"].set_opacity(1)),
                  FadeIn(p["prat"]), FadeIn(pacA, shift=0.2 * UP),
                  run_time=1.2 * VEL)
        # o par nasce inteiro na mão de QUEM RECEBE — nenhuma das duas veio
        # de fora
        cena.play(FadeIn(ch_pub, shift=0.2 * UP),
                  FadeIn(ch_priv, shift=0.2 * UP), run_time=0.8 * VEL)
        # "mensagem": o a da fórmula e o a do pacote, juntos (o Indicate do
        # L6[2] saiu do primeiro play para a palavra, que cai depois dos dois)
        cena.play(na("mensagem", realce(L6[2], pacA[0][1])))

    # a pública desce para o canal e ATRAVESSA, da direita para a esquerda: o
    # olho copia e guarda, à vista, sem nenhuma consequência — nada pisca
    f1s = VGroup(pot("a", "e", ROXO, VERMELHO, 24), fmod("n", 22))
    f1s.arrange(RIGHT, buff=0.12).move_to([-2.3, 0.35, 0])
    with narra(cena, "C8N21", 6.6):
        t0 = _agora(cena)
        na = partial(na_palavra, cena, t0, "C8N21", 6.6)
        # os realces de L6 correm enquanto as chaves e o pacote viajam: cada
        # animação leva o próprio run_time (o do play sobrescreveria o do Wait)
        sai = [ch_pub.animate.move_to([p["X_D"], p["Y_CANAL"], 0]).build(),
               ch_priv.animate.move_to([p["X_D"], Y_POUSO, 0]).build()]
        for a in sai:
            a.set_run_time(0.6 * VEL)
        cena.play(*sai, na("primeira potência", realce(*L6[0][0][1])))
        p["atravessar"](ch_pub, LEFT, vaga=1,
                        junto=lambda i: ([na("módulo", realce(L6[3][1]))]
                                         if i == 2 else []))
        # e quem envia tranca: a primeira potência É o embaralhamento
        mao = ch_pub.animate.move_to([p["X_E"], p["Y_MAO"], 0]).build()
        mao.set_run_time(0.9 * VEL)
        cena.play(mao, Write(f1s, run_time=0.9 * VEL),
                  na("mensagem", realce(pacA[0][1])))
        # o trancar() é um play inteiro e não aceita espera: ela vem antes
        espera = _antes_de(cena, t0, "C8N21", 6.6, "cifra", 0.9 * VEL)
        if espera:
            cena.play(espera)
        p["trancar"](pacA, pot("a", "e", BRANCO, BRANCO, 30))

    # só AGORA a chave vira aritmética dentro do retângulo: o e e o n saem do
    # próprio f1s que acabou de trancar a caixa
    fpub = formula((tx("geral.publica"), CINZA), ("(", PRETO), ("e", VERMELHO),
                   (", ", PRETO), ("n", LARANJA), (")", PRETO),
                   tamanho=22, buff=0.10)
    rpub = RoundedRectangle(corner_radius=0.14, width=fpub.width + 0.7,
                            height=0.72, stroke_color=CINZA, stroke_width=2.5)
    rpub.move_to(ch_pub)
    fpub.move_to(rpub)
    pubS = VGroup(rpub, fpub)
    with narra(cena, "C8N22", 2.9):
        cena.play(ReplacementTransform(ch_pub, rpub),
                  FadeIn(fpub[0]), FadeIn(fpub[1]), FadeIn(fpub[3]),
                  FadeIn(fpub[5]),
                  ReplacementTransform(f1s[0][1].copy(), fpub[2]),
                  ReplacementTransform(f1s[1][1].copy(), fpub[4]),
                  run_time=1.4 * VEL)
        cena.add(pubS)
        cena.play(pubS.animate.move_to([p["X_E"], Y_POUSO, 0]),
                  run_time=0.6 * VEL)

    # a segunda potência desfaz a primeira, com a chave que nunca circulou
    par_s = VGroup(T("(", 24, PRETO), pot("a", "e", ROXO, VERMELHO, 24),
                   T(")", 24, PRETO)).arrange(RIGHT, buff=0.03)
    f2s = VGroup(pot(par_s, "d", None, AZUL, 24), T("≡", 24, PRETO),
                 T("a", 24, ROXO), fmod("n", 22))
    f2s.arrange(RIGHT, buff=0.12).move_to([2.3, 0.35, 0])
    with narra(cena, "C8N23", 4.6):
        t0 = _agora(cena)
        na = partial(na_palavra, cena, t0, "C8N23", 4.6)
        # a prateleira fica com os mesmos dois objetos do C8N08: cifra e
        # pública. Os realces de L6 correm durante a travessia: o d na
        # primeira metade, o aᵉ na segunda
        p["atravessar"](pacA, RIGHT, vaga=0,
                        junto=lambda i: ([na("segunda potência",
                                             realce(L6[0][1]))] if i == 1 else
                                         [na("primeira",
                                             realce(*L6[0][0][1]))]))
        cena.play(FadeIn(p["xis"]),
                  ch_priv.animate.move_to([p["X_D"], p["Y_MAO"], 0]),
                  Write(f2s), run_time=0.9 * VEL)
        # o abrir() é um play inteiro e não aceita espera: ela vem antes
        espera = _antes_de(cena, t0, "C8N23", 4.6, "mensagem original",
                           0.9 * VEL)
        if espera:
            cena.play(espera)
        p["abrir"](pacA, T("a", 32, ROXO))

    fpriv = formula((tx("geral.privada"), AMARELO), ("(", PRETO), ("d", AZUL),
                    (", ", PRETO), ("n", LARANJA), (")", PRETO),
                    tamanho=22, buff=0.10)
    rpriv = RoundedRectangle(corner_radius=0.14, width=fpriv.width + 0.7,
                             height=0.72, stroke_color=AMARELO,
                             stroke_width=2.5)
    rpriv.move_to(ch_priv)
    fpriv.move_to(rpriv)
    privS = VGroup(rpriv, fpriv)
    with narra(cena, "C8N24", 9.1):
        na = partial(na_palavra, cena, _agora(cena), "C8N24", 9.1)
        cena.play(ReplacementTransform(ch_priv, rpriv),
                  FadeIn(fpriv[0]), FadeIn(fpriv[1]), FadeIn(fpriv[3]),
                  FadeIn(fpriv[5]),
                  ReplacementTransform(f2s[0][1].copy(), fpriv[2]),
                  ReplacementTransform(f2s[3][1].copy(), fpriv[4]),
                  run_time=1.4 * VEL)
        cena.add(privS)
        # depois do ReplacementTransform que monta o cartão: o d e o n dele,
        # junto dos de f2s de onde nasceram
        cena.play(na("expoente que desfaz", realce(fpriv[2], f2s[0][1])))
        cena.play(na("módulo", realce(fpriv[4], f2s[3][1])))
        p["piscar"](VERDE)
        cena.play(privS.animate.move_to([p["X_D"], Y_POUSO, 0]),
                  run_time=0.6 * VEL)

    # o esquema simbólico E a fórmula geral (aᵉ)ᵈ saem de cena:
    # o exemplo será reconstruído a partir de a^(1 (mod φ(n)))
    with narra(cena, "C8N25", 4.2):
        cena.play(FadeOut(VGroup(pacA, f1s, f2s, pubS, privS, L6)),
                  FadeOut(p["cenario"]), FadeOut(p["olho"]),
                  FadeOut(p["prat"]), FadeOut(p["xis"]), *p["esvaziar"](),
                  run_time=0.9 * VEL)

    # ---------- FASE B: o exemplo dos slides 95–96 (n = 33, a = 5) ----------
    def cartao(tokens, cor, x):
        f = formula(*tokens, tamanho=22, buff=0.10)
        r = RoundedRectangle(corner_radius=0.14, width=f.width + 0.7,
                             height=0.72, stroke_color=cor, stroke_width=2.5)
        r.move_to([x, 2.55, 0])
        f.move_to(r)
        return VGroup(r, f)

    # 1) o criador escolhe o módulo: n = 33 (o C8N45 é que paga essa dívida)
    esc = formula(("n", LARANJA), ("=", PRETO), ("33", LARANJA),
                  tamanho=30).move_to([0, 2.55, 0])
    # 2) partimos de a^(1 (mod φ(n))) ≡ a, com n = 33 — no lugar de honra
    E1 = VGroup(pot("a", expoente(("1 (mod φ(", PRETO), ("33", LARANJA),
                                  ("))", PRETO), tam=34), ROXO, tam=34),
                T("≡", 34, PRETO), T("a", 34, ROXO), fmod("33", 32))
    E1.arrange(RIGHT, buff=0.14).move_to([0, 1.6, 0])
    # a fala promete que o módulo vem de algum lugar ainda não mostrado. O ?
    # é a promessa em cena: nasce colado no 33 do esc, passa para o 33 do
    # módulo no C8N33 e acompanha o exemplo numérico inteiro. Sai no C8N36
    # com o resto do exemplo — a tela tem de ficar limpa para o argumento
    # final —, e quem quita a dívida é o c3b do C8N45
    inter = T("?", 22, CINZA).next_to(esc[2], UR, buff=0.05)
    with narra(cena, "C8N26", 7.1):
        na = partial(na_palavra, cena, _agora(cena), "C8N26", 7.1)
        cena.play(na("módulo", Write(esc, run_time=1.2 * VEL),
                     Write(E1, run_time=1.2 * VEL)))
        cena.play(FadeIn(inter, shift=0.18 * DOWN), run_time=0.6 * VEL)

    # 3) por enquanto, SÓ o valor: φ(33) = 20
    phi = formula(("φ(", PRETO), ("33", LARANJA), (")", PRETO), ("=", PRETO),
                  ("20", PRETO), tamanho=30, buff=0.08).move_to([0, 0.85, 0])
    E2 = VGroup(pot("a", expoente(("1 (mod ", PRETO), ("20", PRETO),
                                  (")", PRETO), tam=34), ROXO, tam=34),
                T("≡", 34, PRETO), T("a", 34, ROXO), fmod("33", 32))
    E2.arrange(RIGHT, buff=0.14).move_to(E1)
    with narra(cena, "C8N27", 5.8):
        na = partial(na_palavra, cena, _agora(cena), "C8N27", 5.8)
        # o Write(phi) e o E1 → E2, que corriam juntos em 2,4 s, caem cada um na
        # sua palavra, com 1,2 s cada: dois de 2,4 s não cabem na fala
        cena.play(na("módulo", realce(esc[2], E1[0][1][1], E1[3][1])))
        cena.play(na("fi de ene", Write(phi, run_time=1.2 * VEL)))
        cena.play(na("módulo do expoente",
                     ReplacementTransform(E1, E2, run_time=1.2 * VEL)))

    # 4) encontrar e e d inversos (mod 20): 3 × 7 = 21 ≡ 1 ✓  (slide 95)
    ed2 = formula(("e", VERMELHO), ("·", PRETO), ("d", AZUL), ("≡", PRETO),
                  ("1", VERDE), *MOD("20"), tamanho=28,
                  buff=0.10).move_to([0, 0.1, 0])
    edn = formula(("3", VERMELHO), ("×", PRETO), ("7", AZUL), ("=", PRETO),
                  ("21", PRETO), ("≡", PRETO), ("1", VERDE),
                  *MOD("20"), ("✓", VERDE), tamanho=28).move_to(ed2)
    with narra(cena, "C8N28", 2.9):
        na = partial(na_palavra, cena, _agora(cena), "C8N28", 2.9)
        cena.play(Write(ed2), run_time=0.8 * VEL)
        cena.play(na("par de inversos",
                     ReplacementTransform(ed2, edn, run_time=0.9 * VEL)))

    # as chaves NASCEM dos números encontrados: (3, 33) e (7, 33)
    pub = cartao(((tx("geral.publica"), CINZA), ("(", PRETO), ("3", VERMELHO),
                  (", ", PRETO), ("33", LARANJA), (")", PRETO)),
                 CINZA, -3.5)
    priv = cartao(((tx("geral.privada"), AMARELO), ("(", PRETO), ("7", AZUL),
                   (", ", PRETO), ("33", LARANJA), (")", PRETO)),
                  AMARELO, 3.5)
    with narra(cena, "C8N29", 7.1):
        na = partial(na_palavra, cena, _agora(cena), "C8N29", 7.1)
        # a fala tem ordem — "uma leva cada expoente, e as duas levam o mesmo
        # módulo" — então os dois cartões nascem um de cada vez
        cena.play(Create(pub[0]),
                  FadeIn(pub[1][0]), FadeIn(pub[1][1]), FadeIn(pub[1][3]),
                  FadeIn(pub[1][5]),
                  ReplacementTransform(edn[0].copy(), pub[1][2]),
                  ReplacementTransform(esc[2].copy(), pub[1][4]),
                  run_time=1.4 * VEL)
        # os realces entram no play do segundo cartão (o run_time do play
        # sobrescreveria o do Wait, então o bloco vira um AnimationGroup)
        cena.play(AnimationGroup(
            Create(priv[0]),
            FadeIn(priv[1][0]), FadeIn(priv[1][1]), FadeIn(priv[1][3]),
            FadeIn(priv[1][5]),
            ReplacementTransform(edn[2].copy(), priv[1][2]),
            ReplacementTransform(esc[2].copy(), priv[1][4]),
            run_time=1.4 * VEL),
            na("desse par", realce(edn[0], edn[2])))
        cena.play(na("mesmo módulo",
                     realce(esc[2], pub[1][4], priv[1][4])))

    # 5) a PRÓPRIA equação evolui: o 1 (mod 20) vira 3·7, que vira (a³)⁷
    E3 = VGroup(pot("a", expoente(("3", VERMELHO), ("·", PRETO),
                                  ("7", AZUL), tam=34), ROXO, tam=34),
                T("≡", 34, PRETO), T("a", 34, ROXO), fmod("33", 32))
    E3.arrange(RIGHT, buff=0.14).move_to(E2)
    par_a3 = VGroup(T("(", 36, PRETO), pot("a", "3", ROXO, VERMELHO, 36),
                    T(")", 36, PRETO)).arrange(RIGHT, buff=0.04)
    E4 = VGroup(pot(par_a3, "7", None, AZUL, 36),
                T("≡", 36, PRETO), T("a", 36, ROXO), fmod("33", 34))
    E4.arrange(RIGHT, buff=0.16).move_to(E3)
    with narra(cena, "C8N30", 3.8):
        na = partial(na_palavra, cena, _agora(cena), "C8N30", 3.8)
        cena.play(na("números escolhidos",
                     ReplacementTransform(E2, E3, run_time=1.0 * VEL),
                     Indicate(edn, color=VERDE, run_time=1.0 * VEL)))
        cena.play(ReplacementTransform(E3, E4), run_time=1.0 * VEL)

    # …e a mensagem escolhida: a = 5, que precisa ser menor que o módulo
    msg_esc = formula((tx("c8.mensagem"), CINZA), ("a", ROXO), ("=", PRETO),
                      ("5", ROXO), ("<", PRETO), ("33", LARANJA),
                      tamanho=26).move_to([0, 0.85, 0])
    with narra(cena, "C8N31", 5.0):
        na = partial(na_palavra, cena, _agora(cena), "C8N31", 5.0)
        # a fala termina em "menor que o módulo": o < e o 33 chegam por último,
        # junto do 33 de E4. As duas partes do Write, que eram um LaggedStart
        # de 1,8 s, caem cada uma na sua palavra, com 1,2 s
        cena.play(FadeOut(phi, run_time=1.8 * VEL),
                  FadeOut(edn, run_time=1.8 * VEL),
                  na("mensagem",
                     Write(VGroup(*msg_esc[0:4]), run_time=1.2 * VEL)),
                  na("menor que o módulo",
                     Write(VGroup(*msg_esc[4:6]), run_time=1.2 * VEL),
                     realce(E4[3][1])))

    par_53 = VGroup(T("(", 36, PRETO), pot("5", "3", ROXO, VERMELHO, 36),
                    T(")", 36, PRETO)).arrange(RIGHT, buff=0.04)
    L7 = VGroup(pot(par_53, "7", None, AZUL, 36),
                T("≡", 36, PRETO), T("5", 36, ROXO), fmod("33", 34))
    L7.arrange(RIGHT, buff=0.16).move_to(E4)
    with narra(cena, "C8N32", 2.9):
        na = partial(na_palavra, cena, _agora(cena), "C8N32", 2.9)
        cena.play(na("lugar da letra",
                     ReplacementTransform(E4, L7, run_time=1.1 * VEL),
                     Indicate(msg_esc, color=ROXO, run_time=1.1 * VEL)))

    # ---------- o exemplo RODANDO NO MESMO PALCO (slides 93–96) ------------
    # terceira e última volta. As duas chaves descem da bancada direto para as
    # pontas: o percurso da pública pelo canal já foi feito duas vezes e não
    # cabe nas duas falas curtas do trânsito
    pacB = p["pacote"](T("5", 30, ROXO), p["X_E"])
    f1 = VGroup(pot("5", "3", ROXO, VERMELHO, 22), T("≡", 22, PRETO),
                T("26", 22, VERDE), fmod("33", 20))
    f1.arrange(RIGHT, buff=0.08).move_to([-2.3, 0.35, 0])
    # a pública é pública: mesmo sem refazer o percurso pelo canal, o intruso
    # tem de estar com ela — a cópia sobe para a prateleira na mesma vaga do
    # C8N08 e do C8N21, e o (3, 33) fica à vista dele o exemplo inteiro
    pub_olho = pub.copy()
    with narra(cena, "C8N33", 4.6):
        # o esc sai (a prateleira ocupa aquela faixa), mas a dívida do 33 não:
        # o ? se transfere para o 33 do módulo, que segue em cena
        cena.play(inter.animate.next_to(L7[3][1], UR, buff=0.04),
                  FadeOut(esc), FadeIn(p["cenario"]), FadeIn(p["olho"]),
                  FadeIn(p["prat"]), FadeIn(pacB, shift=0.2 * UP),
                  pub.animate.scale(0.8).move_to([p["X_E"], p["Y_MAO"], 0]),
                  pub_olho.animate.scale(0.8 * 0.72)
                  .move_to(p["VAGAS"][1], aligned_edge=DOWN),
                  priv.animate.scale(0.8).move_to([p["X_D"], p["Y_POUSO"], 0]),
                  Write(f1), run_time=1.2 * VEL)
        p["prateleira"][1] = pub_olho     # some no esvaziar() do C8N36
        p["trancar"](pacB, T("26", 30, BRANCO))
        p["atravessar"](pacB, RIGHT, vaga=0)

    # descriptografar: SÓ quem tem a chave PRIVADA (7, 33)
    f2 = VGroup(pot("26", "7", VERDE, AZUL, 22), T("≡", 22, PRETO),
                T("5", 22, ROXO), fmod("33", 20))
    f2.arrange(RIGHT, buff=0.08).move_to([2.3, 0.35, 0])
    with narra(cena, "C8N34", 4.6):
        na = partial(na_palavra, cena, _agora(cena), "C8N34", 4.6)
        cena.play(FadeIn(p["xis"]),
                  pub.animate.move_to([p["X_E"], p["Y_POUSO"], 0]),
                  priv.animate.move_to([p["X_D"], p["Y_MAO"], 0]), Write(f2),
                  run_time=0.9 * VEL)
        p["abrir"](pacB, T("5", 30, ROXO))
        p["piscar"](VERDE)
        # "cifra": o 26 de f1 e o de f2, no play da última volta da chave
        vai = priv.animate.move_to([p["X_D"], p["Y_POUSO"], 0]).build()
        vai.set_run_time(0.6 * VEL)
        cena.play(vai, na("cifra", realce(f1[2], f2[0][0])))

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
    par_f2 = VGroup(T("(", 32, PRETO), pot("5", "3", ROXO, VERMELHO, 32),
                    T(")", 32, PRETO)).arrange(RIGHT, buff=0.04)
    fim3 = VGroup(pot(par_f2, "7", None, AZUL, 32), T("≡", 32, PRETO),
                  T("5", 32, ROXO), fmod("33", 30), T("✓", 32, VERDE))
    fim3.arrange(RIGHT, buff=0.16).move_to(fim2)
    with narra(cena, "C8N35", 6.3):
        na = partial(na_palavra, cena, _agora(cena), "C8N35", 6.3)
        cena.play(na("números", Write(fim2, run_time=1.3 * VEL)))
        cena.play(ReplacementTransform(fim2, fim3), run_time=1.1 * VEL)

    # ---------- FASE C: a segurança (slides 97–104) ----------
    # A fase inteira roda em duas colunas: a TABELA MULTIPLICATIVA à esquerda,
    # com a legenda em cima, e as quatro fórmulas à direita. Cada fala mexe nas
    # duas — a fórmula diz o movimento geral, a grade mostra o caso acontecendo.
    X_F = 2.6                                   # eixo da coluna das fórmulas

    # a grade do C8N17 volta com os dois eixos NOMEADOS: linha é o e, coluna é
    # o d. Só o par (e, d) tem eixo com nome, e só enquanto o módulo é φ(n)
    tab = _tabela(9)
    eixo_e = T("e", 22, VERMELHO).move_to([_TAB_CANTO[0] - 0.42, _TAB_MEIOY, 0])
    eixo_d = T("d", 22, AZUL).move_to([_TAB_MEIO, _TAB_CANTO[1] + 0.40, 0])
    uns = _tab_uns(9)
    lpre = T(tx("c8.tabela_multiplicativa"), 20, CINZA)
    lphi = formula(("(mod ", PRETO), ("φ(", PRETO), ("n", LARANJA),
                   (")", PRETO), (")", PRETO), tamanho=20, buff=0.05)
    leg = VGroup(lpre, lphi).arrange(RIGHT, buff=0.13)
    leg.move_to([_TAB_MEIO, 3.22, 0])
    with narra(cena, "C8N36", 12.1):
        na = partial(na_palavra, cena, _agora(cena), "C8N36", 12.1)
        cena.play(FadeOut(VGroup(pacB, f1, f2, pub, priv, L7, fim3, msg_esc,
                                 inter)),
                  FadeOut(p["cenario"]), FadeOut(p["olho"]),
                  FadeOut(p["prat"]), FadeOut(p["xis"]), *p["esvaziar"](),
                  run_time=0.9 * VEL)
        # a seta despedaçada do C8N10 volta a cobrar a promessa: pisca no
        # centro da tela limpa e sai
        volta = fase0["volta"].move_to(ORIGIN)
        cena.play(FadeIn(volta), run_time=0.9 * VEL)
        cena.play(FadeOut(volta), run_time=0.7 * VEL)
        # e no lugar dela entra a grade onde a pergunta teria resposta
        cena.play(FadeIn(leg), FadeIn(tab), run_time=1.5 * VEL)
        cena.play(FadeIn(eixo_e, shift=0.25 * RIGHT),
                  FadeIn(eixo_d, shift=0.25 * DOWN), run_time=1.1 * VEL)
        # os 1 do C8N17: cada um é um par de inversos, um por linha. A legenda
        # e os eixos já nasceram antes de cada palavra, então só pulsam; os
        # três realces entram neste play, o último da linha
        cena.play(LaggedStart(*[Create(c) for c in uns], lag_ratio=0.16,
                              run_time=2.2 * VEL),
                  na("fi de ene", realce(lphi[1], lphi[2], lphi[3])),
                  na("encontrar a privada", realce(eixo_d)),
                  na("a partir da pública", realce(eixo_e)))

    c1 = formula(("achar", PRETO), ("d", AZUL), ("⇒", PRETO),
                 ("achar", PRETO), ("φ(", PRETO), ("n", LARANJA),
                 (")", PRETO), tamanho=30, buff=0.12).move_to([X_F, 2.0, 0])
    phin = VGroup(c1[4], c1[5], c1[6])          # o sujeito das próximas falas
    # a consulta: entra pela linha do e, para no 1 e sai pela coluna do d
    tam9, ponto9 = _tab_passo(9)
    faixa = Rectangle(width=8.6 * tam9, height=0.86 * tam9, stroke_width=0)
    faixa.set_fill(AMARELO, opacity=0.22).move_to(ponto9(2, 4.5))
    alvo = Rectangle(width=0.86 * tam9, height=0.86 * tam9, stroke_width=0)
    alvo.set_fill(AMARELO, opacity=0.45).move_to(ponto9(2, 5))
    with narra(cena, "C8N37", 6.7):
        na = partial(na_palavra, cena, _agora(cena), "C8N37", 6.7)
        cena.play(FadeIn(faixa), Indicate(_tab_lin(tab, 2), color=VERMELHO),
                  run_time=1.0 * VEL)
        # "conhece o módulo": a legenda inteira, token a token, junto da faixa
        # que encolhe até o 1 (o play vira um AnimationGroup para o run_time
        # do play não sobrescrever o do Wait)
        cena.play(AnimationGroup(ReplacementTransform(faixa, alvo),
                                 Indicate(_tab_cel(tab, 2, 5), color=VERDE),
                                 run_time=0.9 * VEL),
                  na("conhece o módulo", realce(*lphi)))
        cena.play(Indicate(_tab_col(tab, 5), color=AZUL), run_time=0.8 * VEL)
        cena.play(Write(c1), run_time=1.1 * VEL)
        # a fórmula e a legenda dizem o mesmo φ(n) — acendem juntas
        cena.play(na("fi de ene",
                     Indicate(phin, color=LARANJA, run_time=1.0 * VEL),
                     Indicate(VGroup(lphi[1], lphi[2], lphi[3]),
                              color=LARANJA, run_time=1.0 * VEL)))

    # C8N38: o assunto deixa de ser inverter e passa a ser CONTAR. O φ e os
    # parênteses caem da legenda, a grade troca de módulo e os eixos com nome
    # saem junto: agora as linhas são só "os números abaixo do módulo"
    ln = formula(("(mod ", PRETO), ("n", LARANJA), (")", PRETO),
                 tamanho=20, buff=0.05).next_to(lpre, RIGHT, buff=0.13)
    l2 = formula(("n", LARANJA), ("=", PRETO), ("15", LARANJA),
                 tamanho=20, buff=0.10).move_to([_TAB_MEIO, 2.82, 0])
    tab15 = _tabela(15)
    uns15 = _tab_uns(15)
    fora15 = _tab_sem_um(15)
    riscos = VGroup(*[_tab_risco(15, i, VERMELHO) for i in fora15])
    vivas = VGroup(*[_tab_lin(tab15, i) for i in range(1, 15)
                     if i not in fora15])
    conta = formula(("φ(", PRETO), ("15", LARANJA), (") =", PRETO),
                    ("8", VERDE), tamanho=24,
                    buff=0.08).move_to([_TAB_MEIO, -3.05, 0])
    with narra(cena, "C8N38", 7.1):
        na = partial(na_palavra, cena, _agora(cena), "C8N38", 7.1)
        # a troca de grade segue no começo (AnimationGroup: o run_time do play
        # sobrescreveria o do Wait do realce); o φ(n) do c1 pulsa em "fi de ene"
        cena.play(AnimationGroup(
            FadeOut(lphi[1], shift=0.25 * UP),
            FadeOut(lphi[3], shift=0.25 * UP),
            ReplacementTransform(lphi[0], ln[0]),
            ReplacementTransform(lphi[2], ln[1]),
            ReplacementTransform(lphi[4], ln[2]),
            FadeIn(l2, shift=0.2 * DOWN), FadeOut(alvo),
            FadeOut(eixo_e), FadeOut(eixo_d), FadeOut(uns),
            FadeOut(tab), FadeIn(tab15), run_time=1.4 * VEL),
            na("fi de ene", realce(*phin)))
        cena.play(LaggedStart(*[Create(c) for c in uns15], lag_ratio=0.09,
                              run_time=1.4 * VEL))
        # as linhas que não têm 1 nenhum são exatamente as que compartilham
        # fator com o módulo — riscadas uma a uma; "abaixo do módulo" pulsa
        # o n = 15 e o n da legenda durante os riscos
        cena.play(LaggedStart(*[Create(r) for r in riscos], lag_ratio=0.22,
                              run_time=1.7 * VEL),
                  na("abaixo do módulo", realce(*l2, ln[1])))
        cena.play(na("não compartilham fator",
                     LaggedStart(*[Indicate(h, color=VERDE) for h in vivas],
                                 lag_ratio=0.05, run_time=1.1 * VEL),
                     FadeIn(conta, run_time=1.1 * VEL)))

    # C8N39: o módulo cresce e a grade cresce com ele. Os dígitos saem, o que
    # sobra é malha — e a contagem, que era ver oito linhas, vira um ponto de
    # interrogação que colapsa dentro do φ(n) do c1
    malha35, malha77 = _tab_malha(35, w=0.7), _tab_malha(77, w=0.5)
    l2b = formula(("n", LARANJA), ("=", PRETO), ("35", LARANJA),
                  tamanho=20, buff=0.10).move_to(l2)
    l2c = formula(("n", LARANJA), ("=", PRETO), ("77", LARANJA),
                  tamanho=20, buff=0.10).move_to(l2)
    conta35 = formula(("φ(", PRETO), ("35", LARANJA), (") =", PRETO),
                      ("?", CINZA), tamanho=24, buff=0.08).move_to(conta)
    conta77 = formula(("φ(", PRETO), ("77", LARANJA), (") =", PRETO),
                      ("?", CINZA), tamanho=24, buff=0.08).move_to(conta)
    with narra(cena, "C8N39", 4.2):
        na = partial(na_palavra, cena, _agora(cena), "C8N39", 4.2)
        # o salto para 35 começa em "módulo grande"; os dois seguintes vêm
        # logo depois, como hoje
        cena.play(na("módulo grande", AnimationGroup(
            ReplacementTransform(tab15[0], malha35),
            # cada peça que de fato está em cena: um VGroup montado na hora
            # (ou um grupo cujas peças entraram uma a uma) some da tela mas
            # não sai da cena, e o FadeOut devolve a opacidade no fim
            FadeOut(tab15[1]), FadeOut(tab15[2]), FadeOut(tab15[3]),
            *[FadeOut(c) for c in uns15], *[FadeOut(r) for r in riscos],
            ReplacementTransform(l2, l2b),
            ReplacementTransform(conta, conta35), run_time=1.4 * VEL)))
        cena.play(ReplacementTransform(malha35, malha77),
                  ReplacementTransform(l2b, l2c),
                  ReplacementTransform(conta35, conta77), run_time=1.2 * VEL)
        # a contagem COLAPSA dentro do φ(n): é a conta que ninguém faz à mão
        cena.play(conta77.animate.move_to(phin).scale(0.2).set_opacity(0),
                  Indicate(phin, color=LARANJA), run_time=1.1 * VEL)
        cena.remove(conta77)

    # o módulo deixa de ser dado e passa a ser montado: o 77 vira "?" e o
    # quadrado da grade fica vazio
    l2q = formula(("n", LARANJA), ("=", PRETO), ("?", CINZA),
                  tamanho=20, buff=0.10).move_to(l2c)
    with narra(cena, "C8N40", 13.8):
        na = partial(na_palavra, cena, _agora(cena), "C8N40", 13.8)
        cena.play(na("dessa contagem", realce(*phin),
                     Indicate(c1[1], color=AZUL, run_time=0.8 * VEL)))
        cena.play(na("montado", AnimationGroup(
            FadeOut(malha77), Transform(l2c, l2q.copy()),
            run_time=1.2 * VEL)))
        cena.replace(l2c, l2q)

    # slide 100: n primo entrega φ(n) de graça — não serve. A grade volta a um
    # tamanho legível, e agora NENHUMA linha é riscada
    c2 = formula(("n", LARANJA), (tx("c8.primo_dois_pontos"), PRETO), ("φ(", PRETO),
                 ("n", LARANJA), (")", PRETO), ("=", PRETO), ("n", LARANJA),
                 ("− 1", PRETO), ("✗", VERMELHO),
                 tamanho=28, buff=0.10).move_to([X_F, 0.6, 0])
    tab11 = _tabela(11)
    uns11 = _tab_uns(11)
    l2d = formula(("n", LARANJA), ("=", PRETO), ("11", LARANJA),
                  (tx("c8.primo"), CINZA), tamanho=20, buff=0.12).move_to(l2)
    conta11 = formula(("φ(", PRETO), ("11", LARANJA), (") =", PRETO),
                      ("10", VERDE), tamanho=24, buff=0.08).move_to(conta)
    with narra(cena, "C8N41", 11.2):
        na = partial(na_palavra, cena, _agora(cena), "C8N41", 11.2)
        cena.play(na("fosse primo", AnimationGroup(
            FadeIn(tab11), Transform(l2q, l2d.copy()), run_time=1.5 * VEL)))
        cena.replace(l2q, l2d)
        cena.play(LaggedStart(*[Create(c) for c in uns11], lag_ratio=0.10,
                              run_time=1.7 * VEL))
        cena.play(na("contagem",
                     LaggedStart(*[Indicate(h, color=VERDE)
                                   for h in tab11[2]],
                                 lag_ratio=0.05, run_time=1.2 * VEL),
                     FadeIn(conta11, run_time=1.2 * VEL)))
        cena.play(Write(VGroup(*c2[0:6])), run_time=1.1 * VEL)
        # o n − 1 chega por último, e chega da contagem que a grade acabou
        # de entregar de graça
        cena.play(ReplacementTransform(conta11[3].copy(),
                                       VGroup(c2[6], c2[7])),
                  run_time=0.9 * VEL)
        cena.play(Indicate(VGroup(c2[6], c2[7]), color=LARANJA),
                  run_time=0.8 * VEL)
        cena.play(FadeIn(c2[8], scale=1.6), run_time=0.5 * VEL)
        # …e com φ(n) de graça, o d sai da pública na mão de qualquer um
        cena.play(na("chave privada",
                     Indicate(c1[1], color=AZUL, run_time=0.7 * VEL)))

    # slides 101–104: com n = p × q, só o criador conhece φ(n). O c3 é escrito
    # em TRÊS tempos — o lado esquerdo no C8N42, o `⇒ φ(n) =` no C8N44 e o
    # produto no C8N45, vindo da dedu
    c3 = formula(("n", LARANJA), ("=", PRETO), ("p", ROSA), ("×", PRETO),
                 ("q", VERDE2), ("⇒", PRETO), ("φ(", PRETO), ("n", LARANJA),
                 (")", PRETO), ("=", PRETO), ("(", PRETO), ("p", ROSA),
                 ("− 1)", PRETO), ("×", PRETO), ("(", PRETO), ("q", VERDE2),
                 ("− 1)", PRETO), ("✓", VERDE),
                 tamanho=28, buff=0.08).move_to([X_F, -0.9, 0])
    # a grade volta ao módulo 15 do C8N38 — as MESMAS seis linhas riscadas,
    # agora separadas em duas cores: as de p e as de q
    l2e = formula(("n", LARANJA), ("=", PRETO), ("15", LARANJA), ("=", PRETO),
                  ("3", ROSA), ("×", PRETO), ("5", VERDE2),
                  tamanho=20, buff=0.10).move_to(l2)
    tab15b, uns15b = _tabela(15), _tab_uns(15)
    conta15 = formula(("φ(", PRETO), ("15", LARANJA), (") =", PRETO),
                      ("8", VERDE), tamanho=24, buff=0.08).move_to(conta)
    r_p = VGroup(*[_tab_risco(15, i, ROSA) for i in (3, 6, 9, 12)])
    r_q = VGroup(*[_tab_risco(15, i, VERDE2) for i in (5, 10)])
    # C8N42: o módulo é MONTADO — dois primos escolhidos, multiplicados, e a
    # legenda, a grade do produto e a fórmula geral nascem juntas
    l2m = formula(("n", LARANJA), ("=", PRETO), ("3", ROSA), ("×", PRETO),
                  ("5", VERDE2), tamanho=20, buff=0.10).move_to(l2d)
    with narra(cena, "C8N42", 9.2):
        na = partial(na_palavra, cena, _agora(cena), "C8N42", 9.2)
        cena.play(FadeOut(tab11, run_time=0.9 * VEL),
                  FadeOut(uns11, run_time=0.9 * VEL),
                  FadeOut(conta11, run_time=0.9 * VEL),
                  na("escolher o módulo", realce(l2d[0], ln[1])))
        # o "11 primo" dá lugar ao 3 × 5: o 5 nasce do rótulo "primo"
        cena.play(na("dois primos", AnimationGroup(
            Transform(l2d[0], l2m[0].copy()), Transform(l2d[1], l2m[1].copy()),
            Transform(l2d[2], l2m[2].copy()), Transform(l2d[3], l2m[3].copy()),
            TransformFromCopy(l2d[3], l2m[4], introducer=True),
            run_time=0.8 * VEL)))
        cena.remove(l2d)
        cena.add(l2m)
        # o 15 nasce do 3 e do 5; a grade do produto e o n = p × q entram
        # junto, no mesmo gesto
        cena.play(na("multiplica", AnimationGroup(
            Transform(l2m[0], l2e[0].copy()), Transform(l2m[1], l2e[1].copy()),
            Transform(l2m[2], l2e[4].copy()), Transform(l2m[3], l2e[5].copy()),
            Transform(l2m[4], l2e[6].copy()),
            TransformFromCopy(VGroup(l2m[2], l2m[4]), l2e[2], introducer=True),
            FadeIn(l2e[3]), FadeIn(tab15b), FadeIn(uns15b), FadeIn(conta15),
            Write(VGroup(*c3[0:5])), run_time=1.4 * VEL)))
        cena.remove(l2m)
        cena.add(l2e)

    with narra(cena, "C8N43", 8.3):
        na = partial(na_palavra, cena, _agora(cena), "C8N43", 8.3)
        cena.play(na("dois primos", realce(c3[2], c3[4], l2e[4], l2e[6])))
        # os riscos de p e de q, junto do p/q da fórmula e do 3/5 da legenda
        cena.play(na("múltiplos de p",
                     LaggedStart(*[Create(r) for r in r_p], lag_ratio=0.25,
                                 run_time=1.4 * VEL),
                     Indicate(c3[2], color=ROSA, run_time=1.4 * VEL),
                     realce(l2e[4])))
        cena.play(na("os de q",
                     LaggedStart(*[Create(r) for r in r_q], lag_ratio=0.30,
                                 run_time=1.1 * VEL),
                     Indicate(c3[4], color=VERDE2, run_time=1.1 * VEL),
                     realce(l2e[6])))

    # a linha instanciada paga as duas dívidas da fase B: de onde veio o 33
    # (C8N26) e de onde veio o 20 (C8N27)
    c3b = formula(("33", LARANJA), ("=", PRETO), ("3", ROSA), ("×", PRETO),
                  ("11", VERDE2), ("⇒", PRETO), ("φ(", PRETO), ("33", LARANJA),
                  (")", PRETO), ("=", PRETO), ("2", ROSA), ("×", PRETO),
                  ("10", VERDE2), ("=", PRETO), ("20", PRETO),
                  tamanho=24, buff=0.08).move_to([X_F, -1.75, 0])
    # o que desconta de n − 1: abaixo do produto, os múltiplos de um primo são
    # tantos quanto vale o outro, menos um — a linha provisória nasce do
    # cabeçalho de linhas e dos riscos, e ocupa o lugar que o c3b vai tomar
    dedu = formula(("(", PRETO), ("n", LARANJA), ("− 1)", PRETO), ("−", PRETO),
                   ("(", PRETO), ("q", VERDE2), ("− 1)", PRETO), ("−", PRETO),
                   ("(", PRETO), ("p", ROSA), ("− 1)", PRETO),
                   tamanho=28, buff=0.08).move_to([X_F, -1.75, 0])
    dedu2 = formula(("p", ROSA), ("q", VERDE2), ("−", PRETO), ("p", ROSA),
                    ("−", PRETO), ("q", VERDE2), ("+ 1", PRETO),
                    tamanho=28, buff=0.08).move_to(dedu)
    dedu3 = formula(("(", PRETO), ("p", ROSA), ("− 1)", PRETO), ("×", PRETO),
                    ("(", PRETO), ("q", VERDE2), ("− 1)", PRETO),
                    tamanho=28, buff=0.08).move_to(dedu)
    d_n1, d_q1, d_p1 = (VGroup(*dedu[0:3]), VGroup(*dedu[3:7]),
                        VGroup(*dedu[7:11]))
    with narra(cena, "C8N44", 10.4):
        na = partial(na_palavra, cena, _agora(cena), "C8N44", 10.4)
        cena.play(Write(VGroup(*c3[5:10])), run_time=0.7 * VEL)
        cena.play(na("abaixo do produto",
                     TransformFromCopy(tab15b[2], d_n1, run_time=0.8 * VEL)))
        # os múltiplos de 3 (rosa) contam pelo 5, e os de 5 (verde-claro)
        # pelo 3: cada risco vira o desconto do outro primo
        cena.play(na("vale o outro", AnimationGroup(
            TransformFromCopy(r_p, d_q1, introducer=True), Indicate(l2e[6], color=VERDE2),
            TransformFromCopy(r_q, d_p1, introducer=True), Indicate(l2e[4], color=ROSA),
            run_time=1.0 * VEL)))
        # a linha inteira passa a ser um objeto só, para os passos do C8N45
        cena.remove(d_n1, d_q1, d_p1)
        cena.add(dedu)

    with narra(cena, "C8N45", 7.0):
        # a dedução fecha em três passos, na própria linha provisória:
        # (n − 1) − (q − 1) − (p − 1) → pq − p − q + 1 → (p − 1) × (q − 1)
        cena.play(TransformMatchingShapes(dedu, dedu2), run_time=0.7 * VEL)
        cena.play(TransformMatchingShapes(dedu2, dedu3), run_time=0.7 * VEL)
        # o produto sobe e completa o c3
        cena.play(ReplacementTransform(dedu3, VGroup(*c3[10:17])),
                  run_time=0.7 * VEL)
        # o ✓ e a contagem da grade fecham juntos: 2 × 4 são as oito linhas
        # que sobraram, sem contar nenhuma
        cena.play(FadeIn(c3[17], scale=1.5), Indicate(conta15, color=VERDE),
                  run_time=0.5 * VEL)
        cena.play(LaggedStart(*[FadeIn(t, shift=0.15 * UP) for t in c3b],
                              lag_ratio=0.06), run_time=1.3 * VEL)

    # C8N46: sem p e sem q, o atalho evapora — a fatoração some da legenda, os
    # riscos somem da grade e a contagem volta a ser um ponto de interrogação
    l2f = formula(("n", LARANJA), ("=", PRETO), ("15", LARANJA), ("=", PRETO),
                  ("?", CINZA), ("×", PRETO), ("?", CINZA),
                  tamanho=20, buff=0.10).move_to(l2)
    conta_q = formula(("φ(", PRETO), ("15", LARANJA), (") =", PRETO),
                      ("?", CINZA), tamanho=24, buff=0.08).move_to(conta)
    with narra(cena, "C8N46", 9.6):
        na = partial(na_palavra, cena, _agora(cena), "C8N46", 9.6)
        cena.play(ReplacementTransform(l2e, l2f), FadeOut(r_p), FadeOut(r_q),
                  run_time=1.3 * VEL)
        cena.play(ReplacementTransform(conta15, conta_q), run_time=0.9 * VEL)
        # a mesma seta do C8N10 e do V1N01, agora sobre números: o caminho de
        # volta do n para o p × q se despedaça no meio
        a0 = c3[0].get_top() + 0.28 * UP
        a1 = c3[4].get_top() + 0.28 * UP
        volta3 = Arrow(a0, a0 + 0.45 * (a1 - a0), buff=0, color=VERMELHO,
                       stroke_width=5, max_tip_length_to_length_ratio=0.22)
        cacos3 = VGroup(*[T("?", 20, CINZA).move_to(a0 + t * (a1 - a0)
                                                    + d * UP)
                          for t, d in ((0.62, 0.09), (0.78, -0.05),
                                       (0.94, 0.11))])
        # "p e q": todas as cópias; "produto dos dois": o n, e só depois o
        # caminho de volta que se despedaça
        cena.play(na("p e q", realce(c3[2], c3[4], c3[11], c3[15])))
        cena.play(na("produto dos dois",
                     Indicate(c3[0], color=LARANJA, run_time=0.8 * VEL)))
        cena.play(GrowArrow(volta3), run_time=0.9 * VEL)
        cena.play(LaggedStart(*[FadeIn(c, shift=0.2 * UP) for c in cacos3],
                              lag_ratio=0.18), run_time=1.1 * VEL)

    # a grade cumpriu o papel e sai; a tese fica sozinha, no meio da tela
    c4 = formula((tx("c8.quebrar_rsa"), PRETO), ("=", PRETO), (tx("geral.fatorar"), PRETO),
                 ("n", LARANJA), tamanho=32).move_to([0, -3.0, 0])
    caixa = SurroundingRectangle(c4, color=VERDE, buff=0.2,
                                 corner_radius=0.14)
    with narra(cena, "C8N47", 7.1):
        na = partial(na_palavra, cena, _agora(cena), "C8N47", 7.1)
        cena.play(FadeOut(VGroup(tab15b, uns15b, lpre, ln, l2f, conta_q)),
                  VGroup(c1, c2, c3, c3b, volta3,
                         cacos3).animate.shift(X_F * LEFT),
                  run_time=1.2 * VEL)
        # a tese fecha o capítulo: a caixa se desenha devagar em volta dela
        cena.play(Write(c4), Create(caixa), run_time=3.0 * VEL)
        # "esse número": o n da tese e o n de n = p × q, depois que a tese
        # termina de se escrever
        cena.play(na("esse número", realce(c4[3], c3[0])))

    # a tese (o texto E a moldura verde) sobrevive ao capítulo: o
    # encerramento do vídeo 3 (V3N01) a reaproveita sem limpar() no meio
    return VGroup(c4, caixa)
