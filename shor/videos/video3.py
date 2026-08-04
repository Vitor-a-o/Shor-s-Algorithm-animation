# -*- coding: utf-8 -*-
"""Vídeo 3 — Do teorema ao RSA: abertura e encerramento próprios
(roteiro_video3_do_teorema_ao_rsa.md)."""

from manim import *

from ..paleta import CINZA, LARANJA, PRETO, VEL
from ..ferramentas import T, narra, pot
from ..montagem import TITULOS
from ..cadeado import cadeado, gravar, rachar


def abertura(cena):
    """V3N00 é o gancho falado, antes de qualquer cartão — mesma lógica do
    V1N00/V1N01 do vídeo 1 ("o gancho vem primeiro, a marca vem depois").
    Só depois entra o cartão de marca, que se EMENDA ao CAP06 num
    movimento só, como o vídeo 2 fazia com o CAP01: por isso esta função
    também toca o CAP06 — quem a chama NÃO deve chamar
    abre_capitulo(cena, 6)."""
    # os quatro símbolos do V2N00 voltam em fila, acesos, e fecham em
    # volta do cadeado intacto; duas lacunas vazias se abrem entre eles —
    # os lugares que os capítulos 6 e 7 vão ocupar
    fila = VGroup(T("+", 48, PRETO), T("×", 48, PRETO),
                  pot("x", "n", PRETO, PRETO, 44), T("÷", 48, PRETO))
    fila.arrange(RIGHT, buff=1.1)
    esq = VGroup(fila[0], fila[1])
    dta = VGroup(fila[2], fila[3])
    cad = cadeado("fechado").scale(0.8)
    lac6 = DashedVMobject(Rectangle(width=1.15, height=1.15, color=CINZA,
                                    stroke_width=2.5), num_dashes=14)
    lac7 = lac6.copy()
    with narra(cena, "V3N00", 8.8):
        for s in fila:
            cena.play(FadeIn(s, scale=1.3), run_time=0.6 * VEL)
        # "constrói com elas o RSA": a fila fecha em volta do cadeado, que
        # entra intacto no centro
        cena.play(FadeIn(cad, scale=1.15),
                  esq.animate.next_to(cad, LEFT, buff=0.15),
                  dta.animate.next_to(cad, RIGHT, buff=0.15),
                  run_time=1.2 * VEL)
        # "dois teoremas": a fila abre espaço e as duas lacunas nascem nele
        lac6.next_to(cad, LEFT, buff=0.15)
        lac7.next_to(cad, RIGHT, buff=0.15)
        cena.play(esq.animate.next_to(lac6, LEFT, buff=0.15),
                  dta.animate.next_to(lac7, RIGHT, buff=0.15),
                  FadeIn(lac6), FadeIn(lac7), run_time=1.0 * VEL)
    cena.play(FadeOut(fila), FadeOut(cad), FadeOut(lac6), FadeOut(lac7),
              run_time=0.5 * VEL)

    # cartão de marca: mesma emenda do vídeo 2, agora para o CAP06
    t1 = T("Do Zero ao Algoritmo de Shor Quântico", 42)
    t2 = T("Vídeo 3 de 4 — Do teorema ao RSA", 28, CINZA)
    VGroup(t1, t2).arrange(DOWN, buff=0.5)
    cena.play(Write(t1), run_time=1.1 * VEL)
    cena.play(FadeIn(t2, shift=0.25 * UP), run_time=0.8 * VEL)
    cena.wait(1.3 * VEL)
    cena.play(FadeOut(t2), run_time=0.6 * VEL)

    r = T("Capítulo 6", 26, LARANJA)
    t = T(TITULOS[5], 38)
    g = VGroup(r, t).arrange(DOWN, buff=0.35)
    linha = Line(3 * LEFT, 3 * RIGHT, color=CINZA, stroke_width=1.5)
    linha.next_to(g, DOWN, buff=0.45)
    with narra(cena, "CAP06", 4.6):
        cena.play(FadeOut(t1, scale=0.5),
                  FadeIn(r, shift=0.3 * DOWN), Write(t), Create(linha),
                  run_time=1.3 * VEL)
    cena.play(FadeOut(g), FadeOut(linha), run_time=0.5 * VEL)


def encerramento(cena, tese):
    """`tese` é o "quebrar RSA = fatorar n" dentro da moldura verde, que
    fecha o capítulo 8 e chega aqui intacto — quem chama esta função não
    passa por limpar() entre os dois. O resto do capítulo (a coluna de
    fórmulas do C8N44, deslocada mas nunca apagada) ainda está em cena e
    sai antes da primeira fala, em silêncio.

    A composição é a própria frase do V3N01: a segurança do RSA está
    APOIADA numa única frase, então o cadeado pousa EM CIMA da tese, que
    vira o pedestal dele — ele não a cobre."""
    # a tese desce para virar a base do conjunto; o resto do capítulo sai
    sobra = [m for m in cena.mobjects if m not in tese.submobjects]
    cena.play(*[FadeOut(m) for m in sobra],
              tese.animate.move_to([0, -1.2, 0]), run_time=0.6 * VEL)

    # "apoiada numa única frase": o cadeado desce e pousa sobre a moldura.
    # Maior que no V2N01 porque aqui ele é a imagem final do vídeo — e
    # porque a rachadura do V3N02 precisa caber no arco para ser vista
    cad = cadeado("fechado").scale(1.25)
    cad.next_to(tese, UP, buff=0)
    with narra(cena, "V3N01", 7.9):
        cena.play(FadeIn(cad, shift=0.7 * DOWN), run_time=1.4 * VEL)
        # "ninguém sabe fatorar": a frase se grava no corpo do cadeado
        gravar(cena, cad, "fatorar n", tamanho=24, run_time=1.2)

    # a rachadura CORRE pelo arco e para no meio — devagar, porque é a
    # última imagem do vídeo. Ele não quebra: a quebra é o vídeo 4
    with narra(cena, "V3N02", 7.9):
        rachar(cena, cad, run_time=2.4)

    # cartão final silencioso (~3 s)
    fim = T("Vídeo 4 de 4 — O algoritmo de Shor", 32)
    cena.play(FadeOut(*tese), FadeOut(cad), FadeIn(fim), run_time=0.8 * VEL)
    cena.wait(1.6 * VEL)
    cena.play(FadeOut(fim), run_time=0.6 * VEL)
