# -*- coding: utf-8 -*-
"""Vídeo 1 — Introdução: o vídeo inteiro mora aqui
(roteiro_video1_introducao.md). Não há capítulo por trás dele."""

from manim import *
import numpy as np

from ..paleta import (AMARELO, AZUL, BRANCO, CARTAO_ESCURO, CIANO, CINZA,
                      LARANJA, PRETO, ROSA, VERDE, VERDE2, VERMELHO, VEL)
from ..ferramentas import T, formula, narra, pot, traco
from ..cadeado import cadeado, fechar, gravar, quebrar, rachar, rede
from .comum import VIDEOS, trilha_videos

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

# a linha do tempo do V1N04, na faixa livre abaixo da rede, e as colunas de
# qubits que se empilham nela: (fração do caminho de 1994 até hoje, altura).
# Cada vez mais juntas e mais altas — "nos últimos anos"
_LINHA = -3.25
_QUBITS = ((0.12, 1), (0.22, 1), (0.47, 2), (0.66, 2), (0.77, 3),
           (0.86, 4), (0.95, 6))

# o título da série, que o V1N05 remonta com os cacos dos cadeados
_TITULO = "Do Zero ao Algoritmo de Shor Quântico"

# a janela de prévia (V1N07 em diante): uma região fixa da tela, abaixo de
# onde o título da série fica ancorado no topo depois do V1N06. Cada
# trecho da decupagem desenha JÁ nessa escala e posição — é assim que a
# faixa de fórmula dos capítulos 2–5 nunca entra no enquadramento: as
# miniaturas simplesmente não desenham fórmula nenhuma
_JANELA_CENTRO = np.array([0.0, -0.7, 0.0])
_JANELA_LARGURA, _JANELA_ALTURA = 10.2, 4.6


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


def _qubit():
    """O marcador de qubit da linha do tempo do V1N04: uma bolinha na cor
    do bit 1, de miolo claro."""
    return (Circle(radius=0.065).set_stroke(CIANO, width=2.5)
            .set_fill(CIANO, opacity=0.35))


def _estalar_rede(cena, cad_pequeno, run_time=0.5):
    """O estalo discreto de um cadeado anônimo da rede (V1N04): o arco pula
    um dedo, gira e cai para fora da rede, apagando. Sem fissura correndo —
    o `quebrar()` fica para o cadeado grande.

    NÃO chama play: devolve (animação, arco), para o chamador somar os
    estalos de todos num LaggedStart. A `cena` serve só para soltar o arco:
    ele sai do VGroup do cadeado e entra na cena sozinho, então o corpo fica
    parado onde está e só o arco cai.

    Como no `quebrar()`, o arco caído continua em cena, invisível, onde
    caiu: o V1N05 o reacende dali (por `set_stroke`, não `set_opacity`)."""
    arco = cad_pequeno[0]
    cad_pequeno.remove(arco)
    cena.add(arco)

    lado = 1 if arco.get_x() >= 0 else -1      # cai para fora da rede
    h = arco.height
    alto = arco.copy().shift(0.25 * h * UP).rotate(-lado * 15 * DEGREES)
    caido = (arco.copy().shift(2.5 * h * DOWN + 0.8 * h * lado * RIGHT)
             .rotate(-lado * 60 * DEGREES).set_opacity(0))
    anim = Succession(
        Transform(arco, alto, run_time=0.2 * run_time * VEL),
        Transform(arco, caido, run_time=0.8 * run_time * VEL,
                  rate_func=rush_into))
    return anim, arco


def corpo_shor(cena, cad, malha, interrogacoes):
    """V1N04. As interrogações do V1N02 se desfazem nos primos, a rede
    pisca, uma linha do tempo junta qubits até hoje e, no fim, o cadeado
    grande quebra e os da rede estalam em cascata.

    Devolve os cacos — (as duas metades do arco grande, VGroup dos dez
    arcos pequenos) —, todos em cena, invisíveis onde caíram: o V1N05 os
    remonta no título. O corpo "RSA" e o que sobrou da rede também ficam."""
    anonimos = malha[2]

    # os dois primos do V1N02, de volta na faixa livre abaixo da rede
    p = T(_P, 36, ROSA).move_to([-1.1, _LINHA + 0.15, 0])
    q = T(_Q, 36, VERDE2).move_to([1.1, _LINHA + 0.15, 0])

    # a linha do tempo: de 1994 até hoje, com as colunas de qubits
    x0, x1 = -2.6, 2.6
    linha = Line([x0, _LINHA, 0], [x1, _LINHA, 0], color=CINZA,
                 stroke_width=3)
    d94 = Dot([x0, _LINHA, 0], radius=0.08, color=PRETO)
    hoje = Dot([x1, _LINHA, 0], radius=0.08, color=PRETO)
    r94 = T("1994", 22, CINZA).next_to(d94, DOWN, buff=0.15)
    rhoje = T("hoje", 22, CINZA).next_to(hoje, DOWN, buff=0.15)
    qubits, quando = VGroup(), []
    for f, altura in _QUBITS:
        for k in range(altura):
            qubits.add(_qubit().move_to(
                [x0 + f * (x1 - x0), _LINHA + 0.2 + 0.17 * k, 0]))
            quando.append((f, k))               # onde na linha, que andar
    varre = 2.1 * VEL                           # a linha vai de 1994 a hoje

    with narra(cena, "V1N04", 17.9):
        # "vence essa aposta": as interrogações voltam onde pararam e o
        # espalhar se desfaz, de trás para frente, até a linha da seta...
        cena.play(Succession(Wait(5.4 * VEL), FadeIn(interrogacoes,
                                                     run_time=0.2 * VEL)))
        cena.play(*[c.animate.rotate(-ang * DEGREES).shift([-dx, -dy, 0])
                    for c, (dx, dy, ang) in zip(interrogacoes, _ESPALHA)],
                  run_time=0.4 * VEL)
        # ...e a volta que era impossível acontece: as da esquerda viram o
        # 3, as da direita o 11 (elas nasceram da direita para a esquerda)
        cena.play(ReplacementTransform(interrogacoes[4:], p),
                  ReplacementTransform(interrogacoes[:4], q),
                  run_time=0.6 * VEL)

        # "não só a do RSA": os anônimos piscam uma vez, acesos por inteiro
        # (o arco pelo traço: um fill no arco tamparia a aresta atrás dele).
        # O there_and_back vai em cada um, não no grupo: o finish() do grupo
        # leva cada animação ao fim dela, e eles ficariam acesos
        pisca = dict(rate_func=there_and_back)
        cena.play(Succession(Wait(0.7 * VEL), AnimationGroup(
            *[c[1].animate(**pisca).set_opacity(1) for c in anonimos],
            *[c[0].animate(**pisca).set_stroke(opacity=1) for c in anonimos],
            run_time=0.8 * VEL)))

        # "nos últimos anos": os primos se recolhem no ponto de 1994... (glifo
        # a glifo, cada um num ponto: do Text inteiro para o Dot, os glifos
        # sumiam no lugar em vez de viajar)
        copias = [d94.copy() for _ in range(len(p) + len(q) - 1)]
        cena.play(Succession(Wait(2.4 * VEL), AnimationGroup(
            *[ReplacementTransform(g, d)
              for g, d in zip([*p, *q], [d94, *copias])],
            FadeIn(r94, shift=0.15 * UP), run_time=0.8 * VEL)))
        cena.remove(*copias)
        # ...e a linha corre até hoje; cada qubit nasce quando ela passa, e
        # a coluna sobe um andar de cada vez
        cena.play(Create(linha, rate_func=linear, run_time=varre),
                  *[Succession(Wait(f * varre + 0.05 * k * VEL),
                               GrowFromCenter(u, run_time=0.25 * VEL))
                    for u, (f, k) in zip(qubits, quando)],
                  Succession(Wait(varre - 0.2 * VEL), AnimationGroup(
                      GrowFromCenter(hoje), FadeIn(rhoje, shift=0.15 * UP),
                      run_time=0.4 * VEL)))

        # "prazo de validade": a linha apaga e o cadeado volta a crescer —
        # de novo o centro das atenções. Não até o ×1,4 do "é o RSA": lá a
        # rede ainda não existia, e o arco encostaria no anônimo de cima
        cena.play(Succession(Wait(0.4 * VEL), AnimationGroup(
            *[FadeOut(m) for m in (linha, d94, hoje, r94, rhoje, *qubits)],
            cad.animate.scale(1.2 / 0.8), run_time=0.8 * VEL)))

        # o z_index do V1N03 punha o cadeado na frente da rede; mas a fissura
        # do rachar() e as corridas do quebrar() nascem no z 0, e ficariam
        # POR BAIXO do traço do arco. Volta ao 0 e vai para a frente pela
        # ordem da cena
        cad.set_z_index(0)
        cena.bring_to_front(cad)
        # e quebra, num gesto só: a rachadura mal aparece e já corre até as
        # pontas
        rachar(cena, cad, run_time=0.25)
        pecas = quebrar(cena, cad)

        # os anônimos estalam em cascata, do centro para fora — o quebrar()
        # já passou ~0,75 s do estalo, a folga do "meio segundo depois"
        ordem = sorted(anonimos,
                       key=lambda c: np.linalg.norm(c.get_center()
                                                    - cad[1].get_center()))
        estalos = [_estalar_rede(cena, c) for c in ordem]
        cena.play(LaggedStart(*[a for a, _ in estalos], lag_ratio=0.12))

    return pecas, VGroup(*[arco for _, arco in estalos])


def corpo_serie(cena, cacos):
    """V1N05 e V1N06. Os cacos do V1N04 sobem e se remontam no título da
    série; os quatro vídeos saem dele, apagados, e se organizam na trilha,
    onde o 1 acende.

    Devolve (título, trilha, marca), tudo em cena: o V1N07 acende o 2."""
    pecas, arcos = cacos

    # o título, letra a letra. O "S" de Shor nasce das duas metades do arco
    # grande; as outras 30 letras, de três em três, dos dez arcos pequenos —
    # Arc, perna esquerda e perna direita, nessa ordem —, com os arcos da
    # esquerda indo para as letras da esquerda
    titulo = T(_TITULO, 42)
    i_s = "".join(_TITULO.split()).index("S")
    resto = [g for i, g in enumerate(titulo) if i != i_s]
    trincas = [VGroup(*resto[k:k + 3]) for k in range(0, len(resto), 3)]
    assert len(trincas) == len(arcos), "o título não fecha com os cacos"
    pares = [(pecas, VGroup(titulo[i_s], titulo[i_s].copy()))]
    pares += zip(sorted(arcos, key=lambda a: a.get_x()), trincas)
    pares.sort(key=lambda par: par[1].get_x())

    # os quatro vídeos, apagados, dois acima e dois abaixo do título — no
    # tamanho da trilha, para o V1N06 só os deslocar
    nomes = VGroup(*[T(v, 26) for v in VIDEOS]).set_opacity(0.25)
    for nome, (x, y) in zip(nomes, ((-3.3, 1.5), (3.3, 1.5),
                                    (-3.3, -1.5), (3.3, -1.5))):
        nome.move_to([x, y, 0])

    # a trilha já no lugar final, com o 1 aceso; ela nasce apagada e o 1
    # acende depois, então o estado aceso fica guardado
    trilha = trilha_videos(acesos=(1,)).to_edge(LEFT, buff=1.3)
    trilha[0].save_state()
    trilha[0].set_opacity(0.25)
    # "você está aqui": um triângulo ao lado do 1
    marca = (Triangle().set_fill(LARANJA, opacity=1).set_stroke(width=0)
             .rotate(-90 * DEGREES).scale_to_fit_height(0.2)
             .next_to(trilha[0], LEFT, buff=0.3))

    with narra(cena, "V1N05", 8.3):
        # os cacos reacendem onde caíram (pelo traço, como no V4N03) e tudo
        # o mais sai: o corpo "RSA", as arestas, os pontos, os corpos
        # pequenos — tudo o que está em cena menos os cacos
        cena.bring_to_front(pecas)
        restos = [m for m in cena.mobjects
                  if m is not pecas and all(m is not a for a in arcos)]
        # Reacendem já de traço fino: o traço vira preenchimento no caminho
        # até a letra, e um traço grosso passava por um borrão
        cena.play(*[FadeOut(m) for m in restos],
                  pecas.animate.set_stroke(opacity=1, width=2.5),
                  arcos.animate.set_stroke(opacity=1, width=2.5),
                  run_time=0.6 * VEL)
        # "a promessa, ou a ameaça, do algoritmo de Shor": sobem e viram as
        # letras, da esquerda para a direita
        cena.play(LaggedStart(*[ReplacementTransform(c, a) for c, a in pares],
                              lag_ratio=0.08), run_time=2.4 * VEL)
        # as letras entraram soltas; o título volta a ser um só
        cena.remove(*[a for _, a in pares])
        cena.add(titulo)
        # "esta série": os quatro vídeos saem de trás do título, apagados
        cena.play(Succession(Wait(2.4 * VEL), AnimationGroup(
            *[FadeIn(n, target_position=[n.get_x(), 0, 0]) for n in nomes],
            run_time=1.0 * VEL)))

    with narra(cena, "V1N06", 8.3):
        # "são quatro vídeos": o título sobe e os quatro se enfileiram na
        # trilha, num bloco só; os números entram na frente de cada um
        cena.play(titulo.animate.scale(0.6).to_edge(UP, buff=0.5),
                  *[ReplacementTransform(n, linha[1])
                    for n, linha in zip(nomes, trilha)],
                  run_time=1.6 * VEL)
        cena.play(LaggedStart(*[FadeIn(linha[0], shift=0.2 * RIGHT)
                                for linha in trilha], lag_ratio=0.3),
                  run_time=0.8 * VEL)
        for linha in trilha:
            cena.remove(*linha)
        cena.add(trilha)
        # "e neles eu passo por cada peça": o 1 acende e ganha a marca
        cena.play(Succession(Wait(0.9 * VEL), AnimationGroup(
            Restore(trilha[0]), GrowFromCenter(marca), run_time=0.8 * VEL)))

    return titulo, trilha, marca


def _janela_previa(cena, titulo=None):
    """Abre a moldura da prévia: um retângulo fino que nasce no centro da
    região _JANELA_CENTRO/_LARGURA/_ALTURA. `titulo`, quando dado, vira um
    rótulo no canto superior-esquerdo da moldura — usado pelas prévias
    futuras (V1N08 vai passar "Fermat" e depois "Euler"; o V1N07 não passa
    nada, porque o "2" que desliza da trilha já faz esse papel).

    Devolve (moldura, rotulo_ou_None, regiao), onde regiao =
    (centro, largura, altura): a caixa dentro da qual CADA trecho da
    decupagem deve construir sua cena já na escala e posição finais —
    nunca em coordenadas de tela cheia para depois cortar."""
    moldura = RoundedRectangle(width=_JANELA_LARGURA, height=_JANELA_ALTURA,
                               corner_radius=0.15, color=CINZA,
                               stroke_width=2)
    moldura.move_to(_JANELA_CENTRO)
    entra = [Create(moldura)]
    rotulo = None
    if titulo is not None:
        rotulo = T(titulo, 24, LARANJA)
        rotulo.next_to(moldura, UP, buff=0.15).align_to(moldura, LEFT)
        entra.append(FadeIn(rotulo, shift=0.15 * DOWN))
    cena.play(*entra, run_time=0.4 * VEL)
    return moldura, rotulo, (_JANELA_CENTRO, _JANELA_LARGURA, _JANELA_ALTURA)


def _previa_v2(cena, regiao):
    """V1N07 — os oito trechos da decupagem (roteiro_video1_introducao.md,
    seção "Critério das prévias"), na ordem exata da tabela: capítulos
    1, 2, 3, 4, 2, 2, 1, 5. Cada trecho é uma função local, recriando SÓ o
    gesto mínimo descrito na célula — nunca importando capitulo1..5.py —
    para uma trilha futura poder ajustar o timing de um trecho sem mexer
    nos outros.

    Devolve `ainv`, um VGroup com o `a⁻¹` que fecha o último trecho E o
    resto da grade/círculos que nunca saiu de cena (o roteiro só promete
    "fica em cena" para o a⁻¹, mas as linhas sobreviventes ficam juntas
    dele — sem tempo sobrando no V1N07 para as descartar ali). O V1N08 os
    engole inteiros, por cima da primeira miniatura dele."""
    centro, _, _ = regiao
    cx, cy = centro[0], centro[1]

    def _trecho1():
        # 0,0–2,4 · cap. 1: a reta cinza se desenha e uma barra azul cresce
        # sobre ela — um número virando comprimento
        y = cy + 0.3
        reta = Line([cx - 3.6, y, 0], [cx + 3.6, y, 0], color=CINZA,
                    stroke_width=3)
        barra = traco([cx - 3.6, y + 0.4, 0], [cx + 1.4, y + 0.4, 0], AZUL)
        rotulo = T("5", 30, AZUL).next_to(barra, UP, buff=0.12)
        cena.play(Create(reta), run_time=0.8 * VEL)
        cena.play(Create(barra), FadeIn(rotulo), run_time=1.0 * VEL)
        cena.play(FadeOut(reta), FadeOut(barra), FadeOut(rotulo),
                  run_time=0.4 * VEL)

    def _trecho2():
        # 2,4–4,0 · cap. 2: a barra vermelha e a azul emendadas ponta a
        # ponta — somar é encostar dois comprimentos
        y = cy + 0.3
        b = traco([cx - 3.0, y, 0], [cx - 0.4, y, 0], VERMELHO)
        a = traco([cx - 0.4, y, 0], [cx + 2.6, y, 0], AZUL)
        rb = T("6", 24, VERMELHO).next_to(b, UP, buff=0.1)
        ra = T("5", 24, AZUL).next_to(a, UP, buff=0.1)
        cena.play(Create(b), FadeIn(rb), run_time=0.7 * VEL)
        cena.play(Create(a), FadeIn(ra), run_time=0.6 * VEL)
        cena.play(FadeOut(b), FadeOut(a), FadeOut(rb), FadeOut(ra),
                  run_time=0.3 * VEL)

    def _trecho3():
        # 4,0–5,4 · cap. 3: cinco blocos azuis idênticos nascendo em
        # cadeia — multiplicar é repetir o mesmo comprimento
        y = cy + 0.3
        xs = np.linspace(cx - 3.4, cx + 3.4, 6)
        blocos = VGroup(*[traco([xs[i], y, 0], [xs[i + 1], y, 0], AZUL)
                          for i in range(5)])
        cena.play(LaggedStart(*[Create(b) for b in blocos], lag_ratio=0.5),
                  run_time=0.9 * VEL)
        cena.play(FadeOut(blocos), run_time=0.5 * VEL)

    def _trecho4():
        # 5,4–6,9 · cap. 4: a corrente de seis "3" e a linha tracejada
        # gigante embaixo, que só sugere o tamanho do resultado
        pares = []
        for i in range(6):
            pares.append(("3", AZUL))
            if i < 5:
                pares.append(("×", PRETO))
        cadeia = formula(*pares, tamanho=28).move_to([cx, cy + 0.6, 0])
        y = cy - 0.1
        xs = np.arange(cx - 3.6, cx + 3.5, 1.2)
        linha = VGroup(*[traco([x, y, 0], [x + 0.9, y, 0], AZUL)
                        for x in xs])
        cena.play(Write(cadeia), run_time=0.6 * VEL)
        cena.play(LaggedStart(*[Create(s) for s in linha], lag_ratio=0.15),
                  run_time=0.6 * VEL)
        cena.play(FadeOut(cadeia), FadeOut(linha), run_time=0.3 * VEL)

    def _trecho5_6():
        # 6,9–8,4 e 8,4–9,6 · cap. 2, duas vezes seguidas — o MESMO gesto
        # do capítulo 2 (um n crescendo empurra os três juntos): o laranja
        # (módulo) cresce da direita para a esquerda; quando a ponta cruza
        # a barra vermelha (b), o x amarelo nasce (trecho 5); o laranja
        # continua, o amarelo engorda e o verde encolhe até virar um ponto
        # (trecho 6). Um ValueTracker só, porque é a mesma continuidade
        xR, xL = cx + 3.4, cx - 3.4
        yA, yB = cy + 0.5, cy - 0.05
        D = xR - (xL - 0.2)
        t_cross = (xR - xL - 1.4) / D

        vermelha = traco([xL, yA, 0], [xL + 1.4, yA, 0], VERMELHO)
        t = ValueTracker(0)
        laranja = always_redraw(lambda: traco(
            [max(xR - t.get_value() * D, xL - 0.2), yA, 0], [xR, yA, 0],
            LARANJA))
        verde = always_redraw(lambda: traco(
            [xL, yB, 0], [max(xR - t.get_value() * D, xL + 0.05), yB, 0],
            VERDE))
        cena.add(vermelha, laranja, verde)

        # trecho 5: cresce até cruzar a vermelha; o x nasce no mesmo
        # instante em que a ponta chega lá
        cena.play(t.animate.set_value(t_cross), run_time=1.3 * VEL,
                  rate_func=linear)
        x = T("x", 22, AMARELO).move_to([xL + 1.4, yA + 0.45, 0])
        cena.play(FadeIn(x, scale=1.4), run_time=0.2 * VEL)

        # trecho 6: continua crescendo, o amarelo engorda e o verde vira
        # um ponto
        cena.play(t.animate.set_value(1), x.animate.scale(1.6),
                  run_time=0.8 * VEL, rate_func=linear)
        verde.clear_updaters()
        laranja.clear_updaters()
        ponto = Dot([xL, yB, 0], radius=0.07, color=VERDE)
        cena.play(Transform(verde, ponto), run_time=0.2 * VEL)
        cena.play(FadeOut(vermelha), FadeOut(laranja), FadeOut(verde),
                  FadeOut(x), run_time=0.2 * VEL)

    def _trecho7():
        # 9,6–11,4 · cap. 1: três blocos laranja encaixam na barra azul, o
        # quarto tenta, bate e chacoalha com um ✗ vermelho, e sobra o
        # pedacinho verde — o mesmo fecho do C1N03
        y = cy + 0.3
        azul = traco([cx - 3.3, y, 0], [cx + 3.3, y, 0], AZUL)
        razul = T("11", 26, AZUL).next_to(azul, UP, buff=0.1)
        tres = VGroup(*[traco([cx - 3.3 + 2.2 * i, y - 0.55, 0],
                              [cx - 3.3 + 2.2 * (i + 1), y - 0.55, 0],
                              LARANJA) for i in range(3)])
        tenta = traco([cx + 3.3, y - 0.55, 0], [cx + 5.5, y - 0.55, 0],
                     LARANJA)
        xis = T("✗", 30, VERMELHO).next_to(tenta, UP, buff=0.1)
        sobra = traco([cx + 2.9, y - 0.55, 0], [cx + 3.3, y - 0.55, 0],
                      VERDE)
        cena.play(Create(azul), FadeIn(razul), run_time=0.4 * VEL)
        cena.play(LaggedStart(*[Create(b) for b in tres], lag_ratio=0.3),
                  run_time=0.6 * VEL)
        cena.play(Create(tenta), run_time=0.25 * VEL)
        cena.play(FadeIn(xis, scale=1.4), Wiggle(tenta), run_time=0.35 * VEL)
        cena.play(FadeIn(sobra), FadeOut(tenta), FadeOut(xis), FadeOut(azul),
                  FadeOut(razul), FadeOut(tres), run_time=0.3 * VEL)
        cena.remove(sobra)

    def _trecho8():
        # 11,4–17,6 · cap. 5, um trecho só com três batidas: duas filas
        # falham (✗) e a terceira passa (✓); seis filas seguidas, todas
        # ✗ — a repetição é a piada; e por fim a tabela mod 9 com os
        # círculos verdes, três linhas apagando em retângulos vermelhos, e
        # o ÷ riscado que vira a⁻¹ e fica em cena
        alvo = traco([cx + 1.0, cy + 0.6, 0], [cx + 2.6, cy + 0.6, 0],
                     LARANJA)
        cena.add(alvo)

        def fila(y, cor, marca):
            tr = traco([cx - 3.4, y, 0], [cx + 1.0, y, 0], cor)
            m = T(marca, 24, cor).next_to(tr, RIGHT, buff=0.15)
            return VGroup(tr, m)

        tentativas = VGroup(fila(cy + 0.2, VERMELHO, "✗"),
                            fila(cy - 0.1, VERMELHO, "✗"),
                            fila(cy - 0.4, VERDE, "✓"))
        for f in tentativas:
            cena.play(Create(f[0]), FadeIn(f[1], scale=1.3),
                      run_time=0.4 * VEL)
        cena.play(FadeOut(tentativas), run_time=0.1 * VEL)

        seis = VGroup(*[fila(cy + 0.35 - 0.26 * i, VERMELHO, "✗")
                       for i in range(6)])
        cena.play(LaggedStart(*[AnimationGroup(Create(f[0]), FadeIn(f[1]))
                                for f in seis], lag_ratio=0.2),
                  run_time=1.4 * VEL)
        cena.play(FadeOut(seis), FadeOut(alvo), run_time=0.2 * VEL)

        tam = 0.34
        canto = np.array([cx - 1.5, cy + 1.1, 0])

        def ponto(i, j):
            return canto + np.array([j * tam, -i * tam, 0.0])

        grade = VGroup(*[VGroup(*[T(str((i * j) % 9), 15, PRETO)
                                  .move_to(ponto(i, j)) for j in range(9)])
                         for i in range(9)])
        circulos = VGroup(*[Circle(radius=0.12, color=VERDE, stroke_width=2)
                            .move_to(ponto(i, j))
                            for i in range(1, 9) for j in range(1, 9)
                            if (i * j) % 9 == 1])
        mortos = VGroup(*[SurroundingRectangle(grade[i], color=VERMELHO,
                                               buff=0.04, corner_radius=0.05,
                                               stroke_width=1.5)
                          for i in (0, 3, 6)])
        cena.play(LaggedStart(*[FadeIn(l) for l in grade], lag_ratio=0.08),
                  run_time=0.85 * VEL)
        cena.play(LaggedStart(*[Create(c) for c in circulos], lag_ratio=0.08),
                  run_time=0.7 * VEL)
        cena.play(*[FadeOut(grade[i]) for i in (0, 3, 6)],
                  LaggedStart(*[Create(m) for m in mortos], lag_ratio=0.15),
                  run_time=0.6 * VEL)

        div = T("÷", 40, PRETO).move_to([cx + 3.3, cy - 1.2, 0])
        risco = Line(div.get_corner(DL), div.get_corner(UR), color=VERMELHO,
                    stroke_width=4)
        ainv = pot("a", "-1", PRETO, PRETO, 34).move_to(div)
        cena.play(FadeIn(div), run_time=0.2 * VEL)
        cena.play(Create(risco), run_time=0.2 * VEL)
        cena.play(ReplacementTransform(VGroup(div, risco), ainv),
                  run_time=0.4 * VEL)
        # a tabela e os círculos NÃO somem — "fica em cena" no roteiro do
        # V1N07 é só sobre o a⁻¹, mas as três linhas restantes da grade
        # nunca saem. Embrulhados junto com o a⁻¹, o V1N08 os engole
        # inteiros num único FadeOut, no lugar de descartá-los aqui e
        # gastar tempo do V1N07 (que já soma exatos 17,1 s, sem folga)
        resto = VGroup(*[grade[i] for i in range(9) if i not in (0, 3, 6)],
                       circulos, mortos)
        return VGroup(ainv, resto)

    _trecho1()
    _trecho2()
    _trecho3()
    _trecho4()
    _trecho5_6()
    _trecho7()
    return _trecho8()


def corpo_previa2(cena, titulo, trilha, marca):
    """V1N07. O título 2 acende, os outros três somem, o "2" desliza para
    o topo — ele PASSA a ser o rótulo da janela, então _janela_previa não
    recebe titulo — e a janela de prévia do vídeo 2 abre com _previa_v2
    dentro dela.

    Devolve (titulo, alvo, moldura, ainv): o que sobrevive para o V1N08
    (sessão futura) construir a prévia dele em cima — o a⁻¹ por cima da
    primeira miniatura, e a moldura para decidir se reabre ou reaproveita."""
    outros = VGroup(trilha[0], trilha[2], trilha[3])
    alvo = trilha[1]

    with narra(cena, "V1N07", 17.1):
        cena.play(FadeOut(outros), FadeOut(marca),
                  alvo.animate.set_opacity(1).scale(0.85)
                      .next_to(titulo, DOWN, buff=0.35)
                      .to_edge(LEFT, buff=0.8),
                  run_time=0.6 * VEL)
        moldura, _, regiao = _janela_previa(cena)
        ainv = _previa_v2(cena, regiao)

    return titulo, alvo, moldura, ainv


def _previa_v3a(cena, moldura, regiao, alvo, ainv):
    """V1N08 — cap. 6 (Fermat: a permutação da tabela mod 7) e cap. 7
    (Euler: o contra-exemplo mod 9), na ordem exata da tabela.

    A moldura é a MESMA do V1N07 — ninguém chama _janela_previa de novo.
    Os rótulos "Fermat" e "Euler" entram em 0,0 e 5,4 dentro da MESMA
    locução, coisa que _janela_previa não sabe fazer (ela só rotula no
    instante em que a moldura nasce), então o troca-rótulo mora aqui,
    reproduzindo a mesma posição dela (next_to UP, align LEFT na moldura).

    `alvo` é o "2 · Aritmética modular" que o V1N07 deixou: aqui ele vira
    o "3 · Do teorema ao RSA", nascendo dele mesmo — é o "título 3 acende
    sozinho" da tabela.

    Devolve o "3" que substitui `alvo`: o V1N09 o herda em cena, sem
    tocar nele."""
    centro, _, _ = regiao
    cx, cy = centro[0], centro[1]

    tres = VGroup(T("3", 26, LARANJA), T(VIDEOS[2], 26, PRETO))
    tres.arrange(RIGHT, buff=0.35).scale(0.85)
    tres.move_to(alvo).align_to(alvo, LEFT)

    fermat = T("Fermat", 24, LARANJA)
    fermat.next_to(moldura, UP, buff=0.15).align_to(moldura, LEFT)

    # 0,0–2,2 · cap. 6: a tabela mod 7 se preenchendo linha a linha em
    # LaggedStart — o quadro aparecendo é a imagem, ninguém precisa ler os
    # números. O "3" nasce do "2" no mesmo play, e o a⁻¹ do V1N07 é
    # engolido junto
    tam = 0.5
    canto = np.array([cx - 1.5, cy + 1.1, 0.0])

    def ponto(i, j):
        return canto + np.array([j * tam, -i * tam, 0.0])

    linhas = [VGroup(*[T(str((i * j) % 7), 16, PRETO).move_to(ponto(i, j))
                       for j in range(1, 7)]) for i in range(1, 5)]
    cena.play(ReplacementTransform(alvo, tres),
              FadeIn(fermat, shift=0.15 * DOWN), FadeOut(ainv),
              LaggedStart(*[FadeIn(l) for l in linhas], lag_ratio=0.25),
              run_time=1.8 * VEL)

    # 2,2–5,4 · cap. 6: a elipse verde marca a linha 1, que sai da tabela e
    # flutua; a elipse desce para a linha 3, que cai exatamente sob ela —
    # já alinhada embaixo da linha 1 flutuada; os arcos ligam os pares (a
    # mesma permutação (3·j) mod 7 do capítulo 6) e a tela fecha num
    # feixe de arcos
    linha1, linha3 = linhas[0], linhas[2]
    el = Ellipse(width=6 * tam + 0.5, height=0.4, color=VERDE,
                stroke_width=2.5).move_to(linha1)
    yA, yB = cy + 1.7, cy + 1.15
    xs = np.linspace(cx - 2.0, cx + 2.5, 6)
    A = VGroup(*[T(str(j + 1), 20, PRETO).move_to([xs[j], yA, 0])
                for j in range(6)])
    Bv = [(3 * j) % 7 for j in range(1, 7)]
    B = VGroup(*[T(str(Bv[j]), 20, VERMELHO).move_to([xs[j], yB, 0])
                for j in range(6)])
    cena.play(Create(el), LaggedStart(*[TransformFromCopy(linha1[j], A[j])
                                        for j in range(6)], lag_ratio=0.12),
              run_time=1.1 * VEL)
    cena.play(el.animate.move_to(linha3),
              LaggedStart(*[TransformFromCopy(linha3[j], B[j])
                            for j in range(6)], lag_ratio=0.12),
              run_time=1.1 * VEL)
    arcos = VGroup()
    for j in range(6):
        idx = Bv.index(j + 1)
        arcos.add(ArcBetweenPoints(A[j].get_bottom() + 0.05 * DOWN,
                                   B[idx].get_top() + 0.05 * UP,
                                   angle=(0.6 if idx > j else -0.6),
                                   color=VERDE, stroke_width=2))
    cena.play(LaggedStart(*[Create(a) for a in arcos], lag_ratio=0.1),
              run_time=0.7 * VEL)
    cena.play(FadeOut(VGroup(*linhas, el, A, B)), run_time=0.3 * VEL)

    # 5,4–7,6 · cap. 7: corta para a tabela mod 9 — duas linhas que não têm
    # inverso (as dos múltiplos de 3, que colidem em vez de permutar) — a
    # elipse agora vermelha marca as duas e elas apagam sob ela. "Euler"
    # substitui "Fermat" no mesmo instante
    euler = T("Euler", 24, LARANJA).move_to(fermat, aligned_edge=LEFT)
    y0 = cy + 1.4
    header = VGroup(*[T(str(j), 18, AZUL).move_to([cx - 3.0 + 0.85 * (j - 1),
                                                   y0, 0]) for j in range(1, 9)])
    row3 = VGroup(*[T(str((3 * j) % 9), 16, PRETO)
                    .move_to([cx - 3.0 + 0.85 * (j - 1), y0 - 0.5, 0])
                    for j in range(1, 9)])
    row6 = VGroup(*[T(str((6 * j) % 9), 16, PRETO)
                    .move_to([cx - 3.0 + 0.85 * (j - 1), y0 - 0.9, 0])
                    for j in range(1, 9)])
    el9 = Ellipse(width=7.2, height=1.0, color=VERMELHO,
                 stroke_width=2.5).move_to(VGroup(row3, row6))
    cena.play(FadeOut(arcos), ReplacementTransform(fermat, euler),
              FadeIn(header), run_time=0.6 * VEL)
    cena.play(FadeIn(row3), FadeIn(row6), run_time=0.5 * VEL)
    cena.play(Create(el9), run_time=0.4 * VEL)
    cena.play(FadeOut(row3), FadeOut(row6), run_time=0.7 * VEL)

    # 7,6–9,6 · cap. 7: duas cruzes riscam os múltiplos de 3 no cabeçalho —
    # os únicos sem inverso — e sobram seis, reunidos entre chaves
    cruzes = VGroup(Cross(header[2], stroke_color=VERMELHO, stroke_width=3),
                    Cross(header[5], stroke_color=VERMELHO, stroke_width=3))
    cena.play(Create(cruzes), FadeOut(el9), run_time=0.6 * VEL)
    restantes = VGroup(*[header[i] for i in range(8) if i not in (2, 5)])
    cena.play(FadeOut(header[2]), FadeOut(header[5]), FadeOut(cruzes),
              restantes.animate.arrange(RIGHT, buff=0.3).move_to([cx, y0, 0]),
              run_time=0.8 * VEL)
    chave_e = T("{", 30, PRETO).next_to(restantes, LEFT, buff=0.1)
    chave_d = T("}", 30, PRETO).next_to(restantes, RIGHT, buff=0.1)
    cena.play(FadeIn(chave_e), FadeIn(chave_d), run_time=0.6 * VEL)

    # 9,6–11,0 · cap. 7: a caixa verde se fecha em volta do que sobrou
    caixa = SurroundingRectangle(VGroup(chave_e, restantes, chave_d),
                                 color=VERDE, buff=0.15, corner_radius=0.08,
                                 stroke_width=2.5)
    cena.play(Create(caixa), run_time=1.0 * VEL)
    cena.play(Indicate(caixa, color=VERDE, scale_factor=1.03),
              run_time=0.4 * VEL)

    # 11,0–12,1: o cadeado com as letras RSA reaparece por meio segundo,
    # intacto — rima com o V1N01
    mini_cad = cadeado("fechado", "RSA").scale(0.45).move_to([cx, cy, 0])
    cena.play(FadeOut(VGroup(chave_e, restantes, chave_d, caixa)),
              FadeIn(mini_cad), run_time=0.5 * VEL)
    cena.play(FadeOut(mini_cad), run_time=0.6 * VEL)

    return tres, euler


def _previa_v3b(cena, regiao):
    """V1N09 — cap. 8: o esquema do RSA (mensagem → cifra → mensagem),
    as duas chaves, o exemplo rodando e o n se partindo nos primos do
    V1N02. A janela e o rótulo "Euler" continuam exatamente como o
    _previa_v3a deixou — nada aqui os reabre, porque o título 3 é o único
    da trilha que não troca de número nesta fala."""
    centro, _, _ = regiao
    cx, cy = centro[0], centro[1]

    def _caixa(txt, cor_fundo, cor_txt=BRANCO, largura=1.0):
        r = RoundedRectangle(width=largura, height=0.75, corner_radius=0.12,
                             stroke_width=0).set_fill(cor_fundo, opacity=1)
        f = T(txt, 22, cor_txt).move_to(r)
        return VGroup(r, f)

    # 0,0–2,6 · cap. 8: o esquema se monta da esquerda para a direita —
    # caixa da mensagem, seta, caixa da cifra, seta, mensagem de volta
    msg1 = _caixa("M", CARTAO_ESCURO).move_to([cx - 3.4, cy + 0.4, 0])
    seta1 = Arrow(msg1.get_right(), msg1.get_right() + [1.1, 0, 0], buff=0.1,
                 color=PRETO, stroke_width=4)
    cif = _caixa("C", PRETO).next_to(seta1, RIGHT, buff=0.1)
    seta2 = Arrow(cif.get_right(), cif.get_right() + [1.1, 0, 0], buff=0.1,
                 color=PRETO, stroke_width=4)
    msg2 = _caixa("M", CARTAO_ESCURO).next_to(seta2, RIGHT, buff=0.1)
    cena.play(LaggedStart(FadeIn(msg1, shift=0.2 * RIGHT), GrowArrow(seta1),
                          FadeIn(cif, shift=0.2 * RIGHT), GrowArrow(seta2),
                          FadeIn(msg2, shift=0.2 * RIGHT), lag_ratio=0.5),
              run_time=2.6 * VEL)

    # 2,6–5,6 · cap. 8: os dois cartões nascem e se plugam nas setas — o
    # cinza "pública" na primeira, o amarelo "privada" na segunda
    pub = _caixa("pública", CINZA, PRETO, largura=1.5).scale(0.75)
    pub.move_to(seta1.get_center() + [0, 0.9, 0])
    priv = _caixa("privada", AMARELO, PRETO, largura=1.5).scale(0.75)
    priv.move_to(seta2.get_center() + [0, 0.9, 0])
    cena.play(FadeIn(pub, shift=0.3 * DOWN), run_time=0.8 * VEL)
    cena.play(pub.animate.move_to(seta1.get_center() + [0, 0.35, 0]),
              run_time=0.5 * VEL)
    cena.play(FadeIn(priv, shift=0.3 * DOWN), run_time=0.8 * VEL)
    cena.play(priv.animate.move_to(seta2.get_center() + [0, 0.35, 0]),
              run_time=0.5 * VEL)
    cena.play(Indicate(priv, color=AMARELO), run_time=0.4 * VEL)

    # 5,6–8,0 · cap. 8: o exemplo roda dentro do mesmo esquema, cada caixa
    # acendendo na sua vez, sem nenhuma conta aparecendo por baixo
    cena.play(Indicate(msg1, color=CIANO, scale_factor=1.15), run_time=0.8 * VEL)
    cena.play(Indicate(cif, color=CIANO, scale_factor=1.15), run_time=0.8 * VEL)
    cena.play(Indicate(msg2, color=CIANO, scale_factor=1.15), run_time=0.8 * VEL)

    # 8,0–10,2 · cap. 8: o n se parte em p rosa e q verde-claro — os MESMOS
    # primos do V1N02 — e os dois cartões de chave piscam junto, porque
    # foi dali que nasceram
    n_txt = T(_N, 26, LARANJA).move_to([cx, cy - 1.3, 0])
    p_txt = T(_P, 24, ROSA).move_to(n_txt.get_center() + [-0.5, -0.7, 0])
    q_txt = T(_Q, 24, VERDE2).move_to(n_txt.get_center() + [0.5, -0.7, 0])
    cena.play(FadeIn(n_txt, scale=1.3), run_time=0.5 * VEL)
    cena.play(TransformFromCopy(n_txt, p_txt), TransformFromCopy(n_txt, q_txt),
              FadeOut(n_txt), run_time=0.9 * VEL)
    cena.play(Indicate(pub, color=CINZA), Indicate(priv, color=AMARELO),
              run_time=0.8 * VEL)

    # 10,2–12,5: a caixa verde final se fecha; sobre ela, a seta de
    # despedaçar do V1N01 volta por meio segundo — rima visual
    caixa_final = SurroundingRectangle(
        VGroup(msg1, seta1, cif, seta2, msg2, pub, priv, p_txt, q_txt),
        color=VERDE, buff=0.25, corner_radius=0.12, stroke_width=2.5)
    cena.play(Create(caixa_final), run_time=1.1 * VEL)
    mini_volta = Arrow([cx + 1.2, cy - 0.5, 0], [cx - 1.2, cy - 0.5, 0],
                       buff=0, color=PRETO, stroke_width=4)
    mini_q = VGroup(*[T("?", 20, CINZA) for _ in range(3)])
    for q, x in zip(mini_q, np.linspace(0.9, -0.9, 3)):
        q.move_to([cx + x, cy - 0.5, 0])
    cena.play(GrowArrow(mini_volta), run_time=0.2 * VEL)
    cena.play(ReplacementTransform(mini_volta, mini_q),
              *[q.animate.shift([0.3 * dx, 0.3 * dy, 0])
               for q, (dx, dy, _) in zip(mini_q, _ESPALHA[:3])],
              run_time=0.3 * VEL)
    cena.play(FadeOut(mini_q), run_time=0.7 * VEL)


def corpo_previa3(cena, titulo, alvo, moldura, ainv):
    """V1N08 e V1N09. A MESMA moldura do V1N07 continua em cena — nenhuma
    das duas falas reabre _janela_previa. "Fermat"/"Euler" nascem e trocam
    dentro do V1N08; o V1N09 não toca no rótulo, porque só o título 3 da
    trilha continua aceso, e é `alvo3` (não a janela) que carrega isso."""
    regiao = (_JANELA_CENTRO, _JANELA_LARGURA, _JANELA_ALTURA)

    with narra(cena, "V1N08", 12.1):
        alvo3, _ = _previa_v3a(cena, moldura, regiao, alvo, ainv)

    with narra(cena, "V1N09", 12.5):
        _previa_v3b(cena, regiao)

    return titulo, alvo3, moldura
