# -*- coding: utf-8 -*-
"""Vídeo 4 — O algoritmo de Shor: abertura e encerramento próprios
(roteiro_video4_algoritmo_de_shor.md)."""

from manim import *

from ..paleta import AMARELO, CINZA, LARANJA, PRETO, VERDE, VERMELHO, VEL
from ..ferramentas import T, narra
from ..montagem import TITULOS, CARTOES
from ..cadeado import avancar, estado_v3, quebrar, rede
from ..capitulos.capitulo10 import _carta_qubit
from .comum import trilha_videos


def abertura(cena):
    """O vídeo 4 abre no ÚLTIMO QUADRO DO VÍDEO 3: o cadeado com "fatorar n"
    gravado e a rachadura parada no meio do arco entra com cena.add, sem
    animação nenhuma — quem monta esse estado é o estado_v3() do cadeado.py.
    Só depois começa a locução (V4N00), e o cadeado sai de cena por cima do
    ombro do quadro já com o cartão de marca entrando por baixo.

    O cartão se EMENDA ao CAP09 num movimento só, como nos vídeos 2 e 3: por
    isso esta função também toca o CAP09 — quem a chama NÃO deve chamar
    abre_capitulo(cena, 9)."""
    cad = estado_v3()
    cena.add(cad)

    # o cartão de marca nasce durante a última frase da locução, então ele é
    # montado aqui: t1 precisa cair no lugar que terá quando t2 chegar
    t1 = T("Do Zero ao Algoritmo de Shor Quântico", 42)
    t2 = T("Vídeo 4 de 4 — O algoritmo de Shor", 28, CINZA)
    VGroup(t1, t2).arrange(DOWN, buff=0.5)

    with narra(cena, "V4N00", 13.1):
        # "a série inteira levou a uma frase": aproximação lenta no cadeado,
        # o mesmo empurrão de câmera da abertura do filme (ABN01). Ela vem
        # em duas partes só porque o Indicate no meio é um play à parte
        cena.play(cad.animate.scale(1.025), run_time=3.4 * VEL,
                  rate_func=linear)
        # "quebrar o RSA é fatorar": a frase está gravada no corpo
        cena.play(Indicate(cad[2], color=VERMELHO, scale_factor=1.25),
                  run_time=1.8 * VEL)
        cena.play(cad.animate.scale(1.02), run_time=1.7 * VEL,
                  rate_func=linear)
        # "o algoritmo que faz isso": a fissura tenta andar e para de novo —
        # ela só chega às pontas no encerramento
        avancar(cena, cad, segmentos=2, run_time=3.2)
        # "percorre um caminho longo até lá": o cadeado encolhe e sai por
        # cima do ombro direito, com o título subindo por baixo dele
        cena.play(cad.animate.scale(0.3).move_to([8.6, 5.2, 0]),
                  FadeIn(t1, shift=0.6 * UP), run_time=2.8 * VEL)
        cena.remove(cad)          # fora do quadro: sai sem ninguém ver

    # cartão de marca: mesma emenda dos vídeos 2 e 3, agora para o CAP09
    cena.play(FadeIn(t2, shift=0.25 * UP), run_time=0.8 * VEL)
    cena.wait(1.3 * VEL)
    cena.play(FadeOut(t2), run_time=0.6 * VEL)

    r = T("Capítulo 9", 26, LARANJA)
    t = T(TITULOS[8], 38)
    g = VGroup(r, t).arrange(DOWN, buff=0.35)
    linha = Line(3 * LEFT, 3 * RIGHT, color=CINZA, stroke_width=1.5)
    linha.next_to(g, DOWN, buff=0.45)
    with narra(cena, "CAP09", CARTOES[9]):
        cena.play(FadeOut(t1, scale=0.5),
                  FadeIn(r, shift=0.3 * DOWN), Write(t), Create(linha),
                  run_time=1.3 * VEL)
    cena.play(FadeOut(g), FadeOut(linha), run_time=0.5 * VEL)


def _cadeado_novo(escala=1.15):
    """O cadeado que o V4N03 remonta com os cacos do antigo — a criptografia
    que não vive de fatorar. Só aparece neste vídeo, por isso mora aqui.

    Nada a ver com o cadeado() da série, de propósito: o corpo é um
    HEXÁGONO verde de topo plano no lugar do retângulo arredondado laranja,
    e o arco é uma ARMAÇÃO de seis pontos — sobe reto dos ombros, quebra em
    duas diagonais e fecha numa coroa chata — no lugar do semicírculo. Sem
    buraco de fechadura e sem letra gravada: o miolo leva um reticulado de
    pontos, que diz "outra matemática" sem escrever nada.

    Devolve VGroup(armação, corpo, reticulado), na ordem do cadeado(): animar
    o [0] move só a armação, que é como ele fecha."""
    corpo = RegularPolygon(n=6, start_angle=0, radius=1.0)
    corpo.set_fill(VERDE, opacity=1).set_stroke(PRETO, width=3)

    # nenhuma curva, e a coroa CHATA — com um vértice só no alto ele leria
    # como telhado de casa em vez de cadeado. Mais estreita que o corpo, e
    # os pés terminam por dentro do hexágono, que os cobre quando fecha
    armacao = VMobject(stroke_color=PRETO, stroke_width=8)
    armacao.set_points_as_corners([[-0.52, 0.60, 0], [-0.52, 1.22, 0],
                                   [-0.28, 1.58, 0], [0.28, 1.58, 0],
                                   [0.52, 1.22, 0], [0.52, 0.60, 0]])

    # os pontos numa base OBLÍQUA, que é como se desenha um reticulado —
    # num quadrado 3×3 eles leriam como a face de um dado
    reticulado = VGroup(*[Dot([i * 0.36 + j * 0.15, j * 0.34, 0],
                              radius=0.055, color=PRETO)
                          for i in (-1, 0, 1) for j in (-1, 0, 1)])
    return VGroup(armacao, corpo, reticulado).scale(escala)


# os dígitos de fantasia do V4N02 — nenhum destes números é um módulo RSA de
# verdade —, mas FIXOS: dois renders dão exatamente a mesma fila, como a
# semente da rede(). Os 2·_LADO primeiros montam a fila, o resto é a rolagem
_FANTASIA = ("2664737828830059612330669705"
             "8715021107285672207313391187"
             "8635286457865764012707189839")
_LADO = 20      # dígitos de cada lado do "21": no corpo de 42 pt a fila fica
                # com 15,1 de largura e as bordas do quadro (14,2) cortam um
                # dígito de cada lado ao meio — é assim que ela estoura
_BANDA = 2.6    # a faixa dos dígitos, 1,2 acima dos cotos do cadeado quebrado


def _fila_digitos(semente):
    """A fila do V4N02: o "21" da moldura no meio e os dígitos de fantasia
    para os dois lados, mais larga que o quadro.

    `semente` é uma CÓPIA do "21" do C11N46, e é dela que os dígitos herdam
    fonte, corpo (42) e cor (LARANJA) — o número que estoura o quadro é o
    mesmo que acabou de sair do algoritmo, com mais dígitos. O buff é o vão
    natural medido DENTRO do "21", para a fila ler como um número só e não
    como dígitos soltos.

    O par de ordem i é (fila[_LADO - i], fila[_LADO + i]): é por ele que o
    número cresce, um dígito de cada lado por vez."""
    dig = [T(c, 42, LARANJA) for c in _FANTASIA[:2 * _LADO]]
    fila = VGroup(*dig[:_LADO], semente, *dig[_LADO:])
    return fila.arrange(RIGHT, buff=0.098).move_to([0, _BANDA, 0])


def encerramento(cena, caixa):
    """`caixa` é a moldura verde do C11N46 (o "21 = 3 × 7" E o retângulo) que
    o parte10 devolve viva: ela chega aqui intacta, porque quem chama esta
    função NÃO passa por limpar() entre os dois. É o pedestal do V4N01 — o
    cadeado pousa em cima dela, como no V3N01 pousou em cima da tese.

    No V4N02 nada do que está em cena se mexe: a faixa de dígitos corre
    acima do cadeado quebrado, as cartas-qubit entram pelo flanco e no fim
    tudo o que o bloco pôs sai — o V4N03 recebe o quadro do V4N01 inteiro,
    com o velho, os cacos e a moldura onde estavam."""
    # o resto do capítulo 11 sai em silêncio, antes da primeira fala —
    # mesma entrada do encerramento do vídeo 3
    sobra = [m for m in cena.mobjects if m not in caixa.submobjects]
    if sobra:
        cena.play(*[FadeOut(m) for m in sobra], run_time=0.6 * VEL)

    # a moldura desce e vira pedestal; o cadeado do V4N00 volta por cima
    # dela, gravado e rachado como o vídeo 3 o deixou
    piso = [0, -1.5, 0]
    cad = estado_v3()
    cad.next_to(caixa.copy().move_to(piso), UP, buff=0)
    with narra(cena, "V4N01", 11.9):
        # a descida abre a fala; depois o quadro fica PARADO no pedestal até
        # "vencer a aposta" (~6,2 s), enquanto a fala lembra a promessa do
        # vídeo 1. O Wait é rabo deste play — não cena.wait() solto —, no
        # mesmo padrão de atraso do C11N10
        cena.play(Succession(
            AnimationGroup(caixa.animate.move_to(piso),
                           FadeIn(cad, shift=0.7 * DOWN),
                           run_time=1.4 * VEL),
            Wait(4.8 * VEL)))
        # "vencer a aposta" (~6,2 s): a fissura chega às duas pontas, o arco
        # estala e os pedaços caem — a quebra que o V3N02 prometeu. Acaba em
        # ~9,0 s, e "E agora a gente sabe como" cai sobre o cadeado já
        # quebrado, sem animação nova
        cacos = quebrar(cena, cad, run_time=2.8)

    # o número que acabou de sair do algoritmo tem dois dígitos; os do RSA
    # têm centenas. A fila nasce de uma CÓPIA do "21" da moldura, que fica
    # onde está: o V4N03 e o V4N04 contam com ela inteira
    semente = caixa[0][0].copy()
    fila = _fila_digitos(semente)
    pares = [(fila[_LADO - i], fila[_LADO + i]) for i in range(1, _LADO + 1)]
    # as cartas do C11N05, no tamanho em que sempre estiveram: elas entram
    # no flanco direito, livres do corpo do cadeado (que acaba em x = 1,2)
    cartas = VGroup(*[_carta_qubit() for _ in range(5)])
    cartas.arrange(RIGHT, buff=0.26).move_to([4.25, 1.05, 0])
    # a rolagem do último trecho: os dígitos que o quadro mostra viram
    # outros. A semente fica de fora — o "21" que veio da moldura é o único
    # que não muda, e é ele que diz de onde o número saiu
    rola = [d for d in fila
            if d is not semente and abs(d.get_center()[0]) < 7.1]
    novos = [T(c, 42, LARANJA).move_to(d)
             for c, d in zip(_FANTASIA[2 * _LADO:], rola)]

    with narra(cena, "V4N02", 14.6):
        # "o exemplo que acabou de rodar": o 21 da moldura. Indicate porque
        # ele devolve a peça idêntica — a moldura tem de chegar inteira lá
        cena.play(Indicate(caixa[0][0], color=AMARELO, scale_factor=1.25),
                  run_time=1.5 * VEL)
        # "tem dois dígitos": o número sobe da moldura para a faixa, do
        # mesmo tamanho — dois dígitos sozinhos no alto do quadro
        cena.play(TransformFromCopy(caixa[0][0], semente), run_time=1.3 * VEL)
        # e começa a crescer, um dígito de cada lado por vez
        cena.play(LaggedStart(*[AnimationGroup(FadeIn(e, scale=0.4),
                                               FadeIn(d, scale=0.4))
                                for e, d in pares[:5]], lag_ratio=0.8),
                  run_time=1.5 * VEL)
        # "os números do RSA têm centenas": o mesmo passo, sem parar, até a
        # fila sair pelas duas bordas do quadro
        cena.play(LaggedStart(*[AnimationGroup(FadeIn(e, scale=0.4),
                                               FadeIn(d, scale=0.4))
                                for e, d in pares[5:]], lag_ratio=0.8),
                  run_time=4.9 * VEL)
        # "milhares de qubits": as cartas entram enquanto os dígitos ainda
        # correm — num bloco só, porque é a simultaneidade que argumenta.
        # Elas não crescem nem se multiplicam: são cinco, do tamanho de
        # sempre, contra um número que já não cabe na tela
        cena.play(Succession(LaggedStart(*[FadeIn(c, scale=0.7)
                                           for c in cartas],
                                         lag_ratio=0.45, run_time=1.4 * VEL),
                             Wait(0.8 * VEL)),
                  LaggedStart(*[Transform(d, n) for d, n in zip(rola, novos)],
                              lag_ratio=0.15),
                  run_time=2.2 * VEL)
        # "nenhuma máquina de hoje chega perto disso": saem só as peças
        # deste bloco, e o que fica é o quadro do fim do V4N01
        cena.play(FadeOut(fila), FadeOut(cartas), run_time=1.6 * VEL)

    # o que sobrou do cadeado: os dois cotos, o corpo e o rótulo gravado
    velho = VGroup(cad[0], cad[1], cad[2])
    fundo = rede()
    novo = _cadeado_novo()
    novo.shift(cad[1].get_center() - novo[1].get_center())
    novo[0].shift(0.55 * UP)        # chega aberto: a armação ainda vai descer
    fundo.set_z_index(-1)           # atrás de tudo sem bring_to_back: ela só
                                    # entra em cena no meio da fala, e até lá
                                    # não há o que mandar para trás

    with narra(cena, "V4N03", 16.2):
        # "pode ficar tranquilo": a primeira frase não tem imagem nova — de
        # 0 a ~3,7 s o quadro é só o cadeado quebrado. O Wait dentro do
        # Succession segura a entrada (a rede nem entra em cena antes da
        # hora), como o Write atrasado do C11N10
        # "a aposta continua de pé" (~3,7 s): a rede do V1N03 volta ao
        # fundo, apagada e intacta — nenhum dos cadeados dela quebrou
        cena.play(Succession(Wait(3.7 * VEL),
                             FadeIn(fundo, run_time=1.2 * VEL)))
        # "ela só ganhou um prazo de validade" (~5,9 s): os cacos reacendem
        # e sobem, desfazendo o tombo do V4N01 (set_stroke, não set_opacity:
        # eles são só traço, e um fill em cima do traço vira borrão)
        cena.bring_to_front(cacos)
        alto = novo[0].get_center()
        cena.play(Succession(Wait(1.0 * VEL), AnimationGroup(
            cacos[0].animate.set_stroke(opacity=1).rotate(70 * DEGREES)
                .scale(0.75).move_to(alto + 0.18 * LEFT + 0.10 * UP),
            cacos[1].animate.set_stroke(opacity=1).rotate(-55 * DEGREES)
                .scale(0.75).move_to(alto + 0.18 * RIGHT + 0.10 * DOWN),
            run_time=2.6 * VEL)))
        # "E a resposta já está sendo preparada" (~9,0 s): os cacos se
        # remontam na armação e o corpo novo nasce enquanto o velho sai —
        # num bloco só
        cena.play(Succession(Wait(0.5 * VEL), AnimationGroup(
            ReplacementTransform(cacos, novo[0]),
            FadeIn(novo[1]), FadeIn(novo[2]), FadeOut(velho),
            run_time=2.4 * VEL)))
        # "uma criptografia que não depende de fatorar" (~12,3 s): fecha
        # inteiro no lugar do antigo, com o mesmo flash seco do fechar()
        cena.play(Succession(Wait(0.9 * VEL), AnimationGroup(
            novo[0].animate.shift(0.55 * DOWN),
            Flash(novo[1].get_top(), color=PRETO, flash_radius=0.55,
                  line_length=0.22),
            run_time=1.4 * VEL)))

    trilha = trilha_videos(acesos=(1, 2, 3, 4))
    trilha.to_edge(LEFT, buff=1.2).shift(0.4 * DOWN)
    titulo = T("Do Zero ao Algoritmo de Shor Quântico", 42).to_edge(UP, buff=0.7)
    with narra(cena, "V4N04", 18.3):
        # a rede, o cadeado novo e a moldura saem no começo; em "Quatro
        # vídeos atrás" a trilha do V1N06 volta, agora com os quatro acesos
        cena.play(FadeOut(fundo), FadeOut(novo), FadeOut(caixa),
                  run_time=0.8 * VEL)
        cena.play(LaggedStart(*[FadeIn(l, shift=0.3 * RIGHT) for l in trilha],
                              lag_ratio=0.35), run_time=2.4 * VEL)
        # "O caminho foi seu" (~11,7 s): a trilha inteira pulsa uma vez —
        # um destaque só, porque o caminho que a fala nomeia já está na tela
        cena.play(Succession(Wait(8.5 * VEL),
                             Indicate(trilha, color=AMARELO,
                                      scale_factor=1.06,
                                      run_time=1.2 * VEL)))
        # "Obrigado por ter vindo até o fim" (~15,5 s): o título pousa por
        # cima deles
        cena.play(Succession(Wait(2.6 * VEL),
                             FadeIn(titulo, shift=0.5 * DOWN,
                                    run_time=1.6 * VEL)))

    # cartão final silencioso (~3 s), no molde do video3.py
    fim = T("fim", 32, CINZA)
    alvo = VGroup(titulo.copy(), fim).arrange(DOWN, buff=0.55).move_to(ORIGIN)
    cena.play(FadeOut(trilha), titulo.animate.move_to(alvo[0]), FadeIn(fim),
              run_time=0.8 * VEL)
    cena.wait(1.6 * VEL)
    cena.play(FadeOut(titulo), FadeOut(fim), run_time=0.6 * VEL)
