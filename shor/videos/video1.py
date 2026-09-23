# -*- coding: utf-8 -*-
"""Vídeo 1 — Introdução: o vídeo inteiro mora aqui
(roteiro_video1_introducao.md). Não há capítulo por trás dele."""

from manim import *
import numpy as np

from ..paleta import CINZA, LARANJA, PRETO, ROSA, VERDE2, VEL
from ..ferramentas import T, narra
from ..cadeado import cadeado, fechar, gravar, rede
from .comum import VIDEOS

# o gancho do V1N00, já quebrado nas três linhas em que ele nasce
_GANCHO = ("Existe uma aposta que protege quase tudo",
           "que você faz na internet, e ela não é",
           "uma senha forte que você possa escolher.")

# a faixa da operação de mão única (V1N01), abaixo do cadeado
_FAIXA = -2.3

# para onde cada "?" do despedaçar se espalha, a partir do seu lugar na
# seta de volta — fixo, para dois renders darem o mesmo quadro (o V1N02
# e o V1N04 contam com as interrogações onde elas pararam)
_ESPALHA = ((-0.7, 0.95, 18), (-0.35, -0.85, -12), (0.15, 1.15, 8),
            (0.3, -0.7, 22), (-0.1, 0.8, -20), (0.55, -1.0, -6),
            (0.8, 0.9, 14))

# os dois primos do V1N02 e o produto — os MESMOS do exemplo do capítulo 8
# (33 = 3 × 11), porque o V1N09 promete que o n de lá se parte "exatamente
# nos primos do V1N02"
_P, _Q, _N = "3", "11", "33"


def _frase(linhas, tamanho=40):
    """As linhas centradas, cada uma um Text inteiro (a tipografia não
    pula), e a lista das palavras recortadas dos glifos de cada linha — o
    Text não tem glifo para espaço, então cada palavra é uma fatia."""
    textos = VGroup(*[T(l, tamanho) for l in linhas]).arrange(DOWN, buff=0.35)
    palavras = []
    for txt, linha in zip(textos, linhas):
        i = 0
        for p in linha.split():
            palavras.append(txt[i:i + len(p)])
            i += len(p)
        assert i == len(txt), f"glifos não batem com as letras: {linha!r}"
    return textos, palavras


def _no_mesmo_play(cena, anims, fn, *args, **kw):
    """Roda `fn(cena, *args)` — uma função do cadeado.py que faz UM
    cena.play, como o fechar() — com `anims` somadas àquele mesmo play.

    É o "no mesmo instante" do V1N01: a fusão acontece no quadro do
    travamento, e o travamento continua sendo o fechar() de verdade, com o
    flash seco dele, sem copiar o Rotate para cá nem editar o cadeado.py.
    O play original volta no primeiro uso."""
    def junto(*a, **k):
        cena.__dict__.pop("play", None)
        cena.play(*a, *anims, **k)
    cena.play = junto
    try:
        fn(cena, *args, **kw)
    finally:
        cena.__dict__.pop("play", None)


def abertura(cena):
    """V1N00, o cartão silencioso e V1N01. O vídeo abre FALANDO: o gancho
    vem primeiro, a marca vem depois.

    Devolve (cad, bloco, interrogacoes), todos ainda em cena — o V1N02
    nasce em cima das interrogações e reabre o bloco, então nada disto
    sai aqui."""
    # --- V1N00: a frase nasce palavra por palavra; "aposta" pisca -------
    _, palavras = _frase(_GANCHO)
    aposta = palavras[2]
    with narra(cena, "V1N00", 9.6):
        cena.play(LaggedStart(*[Write(w) for w in palavras[:3]],
                              lag_ratio=0.6), run_time=1.2 * VEL)
        # a frase segue no mesmo ritmo enquanto "aposta" pisca uma vez
        cena.play(Indicate(aposta, color=LARANJA, scale_factor=1.08,
                           run_time=1.0 * VEL),
                  LaggedStart(*[Write(w) for w in palavras[3:]],
                              lag_ratio=0.5, run_time=6.8 * VEL))
        # o resto esmaece; "aposta" sobrevive como rótulo aceso no canto
        cena.play(*[FadeOut(w) for w in palavras if w is not aposta],
                  aposta.animate.scale(0.7).set_color(LARANJA)
                        .to_corner(UL, buff=0.5),
                  run_time=1.1 * VEL)
    rotulo = aposta

    # --- cartão silencioso: o rótulo continua aceso no canto ------------
    t1 = T("Do Zero ao Algoritmo de Shor Quântico", 42)
    t2 = T(f"Vídeo 1 de 4 — {VIDEOS[0]}", 28, CINZA)
    VGroup(t1, t2).arrange(DOWN, buff=0.5)
    cena.play(Write(t1), run_time=1.1 * VEL)
    cena.play(FadeIn(t2, shift=0.25 * UP), run_time=0.8 * VEL)
    cena.wait(1.0 * VEL)
    cena.play(FadeOut(t1), FadeOut(t2), run_time=0.6 * VEL)

    # --- V1N01 -----------------------------------------------------------
    # o cadeado aberto, só o contorno: o corpo se enche depois, com o que
    # ele protege
    cad = cadeado("aberto")
    cad.shift([0, 0.9, 0] - cad[1].get_center())
    cad[1].set_fill(opacity=0)

    itens = VGroup(T("contas bancárias", 30), T("compras online", 30),
                   T("mensagens privadas", 30))
    itens[0].next_to(cad[1], LEFT, buff=1.2)
    itens[1].next_to(cad[1], RIGHT, buff=1.2)
    itens[2].next_to(cad[1], DOWN, buff=0.5)

    # os dois fatores cinzas e o bloco laranja em que eles se fundem. O
    # bloco são duas metades encostadas, sem traço entre elas: lê como um
    # só, mas o V1N02 pode reabri-lo e mostrar do que era feito
    f1 = Square(0.55).set_fill(CINZA, opacity=1).set_stroke(width=0)
    f2 = Square(0.8).set_fill(CINZA, opacity=1).set_stroke(width=0)
    f1.move_to([-4.3, _FAIXA, 0])
    f2.move_to([-3.35, _FAIXA, 0])
    bloco = VGroup(Rectangle(width=0.62, height=0.8),
                   Rectangle(width=0.92, height=0.8))
    bloco.arrange(RIGHT, buff=0).move_to([3.4, _FAIXA, 0])
    bloco.set_fill(LARANJA, opacity=1).set_stroke(LARANJA, width=1)

    ida = Arrow([-2.55, _FAIXA, 0], [2.4, _FAIXA, 0], buff=0, color=PRETO,
                stroke_width=5)
    volta = Arrow([2.4, _FAIXA, 0], [-2.55, _FAIXA, 0], buff=0, color=PRETO,
                  stroke_width=5)
    interrogacoes = VGroup(*[T("?", 36, CINZA) for _ in _ESPALHA])
    for q, x in zip(interrogacoes, np.linspace(2.2, -2.35, len(_ESPALHA))):
        q.move_to([x, _FAIXA, 0])

    with narra(cena, "V1N01", 14.2):
        # o rótulo desce para o centro, já da largura do corpo, e se abre
        # no contorno do cadeado letra a letra, por posição: "a p s" viram
        # o corpo, o "o" vira o buraco e o "ta" da direita sobe no arco,
        # que no cadeado aberto também fica à direita
        cena.play(rotulo.animate.scale_to_fit_width(cad[1].width)
                        .move_to(cad[1]), run_time=1.0 * VEL)
        a, p, o, s, t, a2 = rotulo
        cena.play(ReplacementTransform(VGroup(a, p, s), cad[1]),
                  ReplacementTransform(o, cad[2]),
                  ReplacementTransform(VGroup(t, a2), cad[0]),
                  run_time=1.0 * VEL)
        # as três peças entraram soltas; o cadeado volta a ser um só
        cena.remove(*cad)
        cena.add(cad)
        # contas, compras, mensagens: uma a cada respiro
        for it, d in zip(itens, (RIGHT, LEFT, UP)):
            cena.play(FadeIn(it, shift=0.3 * d), run_time=0.8 * VEL)
        # e se condensam dentro dele, que se enche de laranja
        cena.play(*[it.animate.scale(0.05).move_to(cad[1]).set_opacity(0)
                    for it in itens],
                  cad[1].animate.set_fill(LARANJA, opacity=1),
                  run_time=1.2 * VEL)
        cena.remove(*itens)

        # "operações": os dois fatores cinzas na faixa de baixo
        cena.play(FadeIn(f1, shift=0.2 * UP), FadeIn(f2, shift=0.2 * UP),
                  run_time=1.2 * VEL)
        # "fáceis de fazer numa direção": a seta varre para a direita...
        cena.play(GrowArrow(ida), run_time=1.6 * VEL)
        # ...e os fatores se fundem no bloco no instante em que o cadeado
        # trava — o play é o do próprio fechar()
        _no_mesmo_play(cena, [ReplacementTransform(f1, bloco[0]),
                              ReplacementTransform(f2, bloco[1]),
                              FadeOut(ida)],
                       fechar, cad)

        # "impraticáveis de desfazer": a volta tenta e se despedaça
        cena.play(GrowArrow(volta), run_time=1.0 * VEL)
        cena.play(ReplacementTransform(volta, interrogacoes),
                  run_time=0.6 * VEL)
        # as interrogações se espalham e o cadeado chacoalha sem abrir
        cena.play(*[q.animate.shift([dx, dy, 0]).rotate(ang * DEGREES)
                    for q, (dx, dy, ang) in zip(interrogacoes, _ESPALHA)],
                  Wiggle(cad), run_time=1.2 * VEL)

    return cad, bloco, interrogacoes


def _anos(e):
    """O contador do V1N02: 10^e − 1 anos, com ponto de milhar."""
    return f"{int(10 ** e) - 1:,}".replace(",", ".")


def corpo_fatoracao(cena, cad, bloco, interrogacoes):
    """V1N02. Recebe o que a abertura deixou em cena e termina com o
    cadeado sozinho no centro.

    O bloco é o MESMO do V1N01 do começo ao fim: as duas metades se
    reabrem nos fatores cinzas, ganham a cor de p e q e se fundem de novo,
    sempre por Transform — nenhuma peça nasce do zero.

    Devolve as interrogações novas (fora de cena, mas nas posições onde
    pararam): o V1N04 as traz de volta e as remonta nos dois primos."""
    fat = T("fatoração", 72).move_to([0, _FAIXA, 0])

    # a forma do bloco fechado, guardada para a volta; e os dois fatores
    # cinzas em que ele se reabre, nas medidas do f1 e do f2 do V1N01
    fechado = bloco.copy()
    cinzas = VGroup(Square(0.55), Square(0.8))
    cinzas.set_fill(CINZA, opacity=1).set_stroke(width=0)
    cinzas[0].move_to([2.45, _FAIXA, 0])
    cinzas[1].move_to([4.2, _FAIXA, 0])
    p = T(_P, 36, ROSA).next_to(cinzas[0], UP, buff=0.2)
    q = T(_Q, 36, VERDE2).next_to(cinzas[1], UP, buff=0.2)
    n = T(_N, 36, LARANJA).next_to(fechado, UP, buff=0.2)

    volta = Arrow([2.4, _FAIXA, 0], [-2.55, _FAIXA, 0], buff=0, color=PRETO,
                  stroke_width=5)
    cacos = VGroup(*[T("?", 36, CINZA) for _ in _ESPALHA])
    for c, x in zip(cacos, np.linspace(2.2, -2.35, len(_ESPALHA))):
        c.move_to([x, _FAIXA, 0])

    e = ValueTracker(0)
    ponto = [0, _FAIXA, 0]
    contador = always_redraw(
        lambda: T(_anos(e.get_value()), 44)
        .scale(1 + e.get_value() / 10).move_to(ponto))

    with narra(cena, "V1N02", 18.3):
        # "fatoração" nasce grande em cima das interrogações, que somem
        # sob ela; depois sobe e vira o rótulo do trecho, como a "aposta"
        cena.play(Write(fat), FadeOut(interrogacoes), run_time=1.4 * VEL)
        cena.play(Succession(
            fat.animate(run_time=1.2 * VEL).scale(0.55).to_edge(UP, buff=0.4),
            Wait(0.5 * VEL)))

        # "multiplicar dois primos grandes": o bloco se reabre pela emenda
        # e cada metade volta a ser o fator cinza de que era feita...
        cena.play(Transform(bloco[0], cinzas[0]),
                  Transform(bloco[1], cinzas[1]), run_time=1.0 * VEL)
        # ...que ganha identidade: rosa é p, verde-claro é q, e cada número
        # nasce de dentro do seu quadrado
        cena.play(bloco[0].animate.set_fill(ROSA),
                  bloco[1].animate.set_fill(VERDE2),
                  GrowFromPoint(p, cinzas[0].get_center()),
                  GrowFromPoint(q, cinzas[1].get_center()),
                  run_time=0.9 * VEL)
        # os dois deslizam um contra o outro e se fundem de novo no mesmo
        # bloco laranja; os números se juntam no produto, por cima dele
        cena.play(Transform(bloco[0], fechado[0]),
                  Transform(bloco[1], fechado[1]),
                  ReplacementTransform(VGroup(p, q), n), run_time=1.2 * VEL)

        # "voltar do produto para os primos": a volta tenta de novo e se
        # despedaça, no mesmo espalhar do V1N01
        cena.play(GrowArrow(volta), run_time=1.0 * VEL)
        cena.play(ReplacementTransform(volta, cacos), run_time=0.6 * VEL)
        cena.play(Succession(
            AnimationGroup(*[c.animate.shift([dx, dy, 0]).rotate(ang * DEGREES)
                             for c, (dx, dy, ang) in zip(cacos, _ESPALHA)],
                           run_time=1.2 * VEL),
            Wait(0.6 * VEL)))

        # "bilhões de anos": a faixa se esvazia sob o contador, que dispara
        # — cada casa decimal custa o mesmo tempo — e estoura para fora
        # (as metades, uma a uma: o V1N01 as pôs soltas na cena, e um
        # FadeOut do grupo tiraria só o grupo e as deixaria lá)
        cena.play(FadeOut(cacos), *[FadeOut(m) for m in bloco], FadeOut(n),
                  FadeIn(contador), run_time=0.8 * VEL)
        cena.play(e.animate.set_value(10), run_time=3.0 * VEL,
                  rate_func=linear)
        contador.clear_updaters()
        cena.play(FadeOut(contador, scale=4), run_time=0.6 * VEL)

        # o cadeado fica sozinho, no centro
        cena.play(FadeOut(fat), cad.animate.move_to(ORIGIN),
                  run_time=1.2 * VEL)

    return cacos


def corpo_rsa(cena, cad):
    """V1N03. O cadeado ganha as letras RSA e encolhe no miolo de uma rede
    de cadeados anônimos, que brotam de trás dele.

    Devolve a rede — VGroup(arestas, pontos, cadeados), tudo em cena — para
    o V1N04 piscá-la e estalá-la."""
    malha = rede()
    arestas, pontos, anonimos = malha

    with narra(cena, "V1N03", 20.0):
        # "é o RSA": o cadeado cresce e as letras se gravam com o flash seco
        # do travamento
        cena.play(cad.animate.scale(1.4), run_time=2.2 * VEL)
        gravar(cena, cad, "RSA")
        # o aceso vai na frente de tudo o que nascer daqui em diante: a rede
        # é desenhada DEPOIS dele e mesmo assim fica atrás (depois do
        # gravar(), para as letras subirem junto com o corpo)
        cad.set_z_index(1)

        # "não é o único" (~10 s): o cadeado encolhe e a rede se desenha ao
        # fundo, já apagada
        cena.play(Succession(
            Wait(7.0 * VEL),
            AnimationGroup(cad.animate.scale(0.8 / 1.4),
                           Create(arestas),
                           LaggedStart(*[GrowFromCenter(d) for d in pontos],
                                       lag_ratio=0.15),
                           run_time=1.6 * VEL)))
        # os anônimos brotam de trás dele e pousam cada um na sua aresta
        for c in anonimos:
            c.generate_target()
            c.move_to(cad[1])
        cena.add(anonimos)
        cena.play(LaggedStart(*[MoveToTarget(c) for c in anonimos],
                              lag_ratio=0.12), run_time=1.8 * VEL)

        # "nem vai ser o único a cair": todos pulsam uma vez, junto
        cena.play(*[c.animate.scale(1.35) for c in anonimos],
                  rate_func=there_and_back, run_time=0.8 * VEL)

    return malha
