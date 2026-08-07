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
# É o capítulo 10 EM TELA: as tags são C10N01–C10N32.
# ============================================================================

# --- a reta dos restos mod 35 (o palco do passeio ×8) -----------------------
# O Capítulo 9 encontrou a ordem numa TABELA mod 9. Aqui o módulo é 35 e uma
# grade de 35 colunas não caberia no quadro — então o gesto de lá (o caminho
# em zigue-zague, a trilha que guarda o ciclo, o Flash no 1 que volta) é
# refeito sobre a RETA SEGMENTADA da REGRA 1: uma casa por resto, 0 a 34, e
# cada ×8 é um salto de casa em casa.
_X0, _YR, _U = -6.30, 1.52, 0.309
# o arco sai rente à reta quando sobe e mais embaixo quando desce: é embaixo
# que mora a fileira de rótulos dos restos visitados
_ACIMA, _ABAIXO = 0.12, 0.44


def _cx(k):
    """Centro da casa do resto k."""
    return np.array([_X0 + (k + 0.5) * _U, _YR, 0.0])


def _casa(k, cor, w, gap=0.05):
    return traco([_X0 + k * _U, _YR, 0], [_X0 + (k + 1) * _U, _YR, 0],
                 cor, gap=gap, w=w)


def _salto(v, w, alt, ponta=True):
    """Um ×8, de resto a resto. O arco abre sempre para a ESQUERDA de quem
    anda — para cima quando o salto avança, para baixo quando ele volta —, e
    é essa alternância que faz o zigue-zague sem nenhum arco cruzar outro.
    `alt` é a flecha do arco; o ângulo sai dela e do tamanho do salto."""
    p1 = _cx(v) + (_ACIMA if w > v else -_ABAIXO) * UP
    p2 = _cx(w) + (_ACIMA if w > v else -_ABAIXO) * UP
    # o sinal negativo é o que joga a barriga do arco para a esquerda de quem
    # anda (no Manim o ângulo positivo abre para a direita)
    ang = -4 * np.arctan(2 * alt / float(np.linalg.norm(p2 - p1)))
    if not ponta:
        return ArcBetweenPoints(p1, p2, angle=ang, color=LARANJA,
                                stroke_width=3)
    return CurvedArrow(p1, p2, angle=ang, color=LARANJA, stroke_width=3,
                       tip_length=0.18)


def parte9b(cena):
    def liga(de, para):
        return Line(de.get_bottom() + 0.06 * DOWN, para.get_top() + 0.06 * UP,
                    color=CINZA, stroke_width=1.8)

    # o alvo — um n que é produto de dois primos escondidos
    obj = formula(("n", LARANJA), ("=", PRETO), ("35", LARANJA),
                  ("=", PRETO), ("p", ROSA), ("×", PRETO), ("q", VERDE2),
                  ("?", PRETO), tamanho=34).to_edge(UP, buff=0.45)
    with narra(cena, "C10N01", 6.3):
        cena.play(Write(obj), run_time=1.0 * VEL)
        cena.play(Indicate(obj[2], color=LARANJA), run_time=0.8 * VEL)
        cena.play(Indicate(obj[4], color=ROSA), Indicate(obj[6], color=VERDE2),
                  run_time=0.8 * VEL)

    # escolhemos a base a = 8
    base = formula(("base:", CINZA), ("a", VERMELHO), ("=", PRETO),
                   ("8", VERMELHO), tamanho=28).move_to([0, 2.90, 0])
    with narra(cena, "C10N02", 2.3):
        cena.play(Write(base), run_time=0.8 * VEL)

    # ENCONTRANDO a ordem modular de 8 módulo 35 (o gesto do Capítulo 9,
    # traduzido da tabela para a reta — ver o cabeçalho do arquivo)
    rotulo = formula(("encontrando a", CINZA), ("ordem modular", PRETO),
                     ("de", CINZA), ("8", VERMELHO), ("módulo", CINZA),
                     ("35", LARANJA), tamanho=24,
                     buff=0.12).move_to([0, 2.45, 0])

    # a reta dos restos mod 35: 35 casas, uma por resto
    reta = VGroup(*[_casa(k, CINZA, 5) for k in range(35)])
    lim = VGroup(T("0", 16, CINZA).next_to(reta[0], DOWN, buff=0.13),
                 T("34", 16, CINZA).next_to(reta[34], DOWN, buff=0.13))

    #   o passeio 1 → 8 → 29 → 22 → (volta ao 1): quatro saltos ×8
    passos = [(1, 8), (8, 29), (29, 22), (22, 1)]
    marcas = VGroup()
    for k in (1, 8, 29, 22):
        b = _casa(k, VERDE, 9, gap=0.02)
        marcas.add(VGroup(b, T(str(k), 22, VERDE).next_to(b, DOWN, buff=0.13)))
    saltos, rots = VGroup(), VGroup()
    trilha = VGroup()          # o caminho sem ponta, para o flash da volta
    for v, w in passos:
        alt = 0.30 if abs(w - v) > 10 else 0.24
        s = _salto(v, w, alt)
        t = _salto(v, w, alt, ponta=False)
        saltos.add(s)
        trilha.add(t)
        # o ×8 pousa sempre logo acima do topo do arco: fora da barriga nos
        # saltos que sobem, DENTRO dela nos que voltam — assim o passeio
        # inteiro cabe acima da linha onde a congruência vai nascer
        rots.add(T("×8", 18, LARANJA)
                 .move_to(t.point_from_proportion(0.5) + 0.19 * UP))

    # a busca inteira cabe numa fala só: o laço roda DENTRO do with, porque
    # "multiplicando pela base até o um voltar" é um gesto contínuo
    with narra(cena, "C10N03", 8.3):
        cena.play(Write(rotulo), run_time=0.9 * VEL)
        cena.play(Create(reta, lag_ratio=0.02), FadeIn(lim),
                  FadeIn(marcas[0]), run_time=0.9 * VEL)
        for k in range(3):
            cena.play(Create(saltos[k]), FadeIn(rots[k]),
                      FadeIn(marcas[k + 1]), run_time=0.9 * VEL)
        # o quarto ×8 é o que reencontra o 1 do começo
        cena.play(Create(saltos[3]), FadeIn(rots[3]),
                  Indicate(marcas[0], color=VERDE), run_time=0.9 * VEL)
        # o ciclo se fecha: o flash amarelo corre a trilha inteira
        cena.play(Flash(_cx(1), color=VERDE, flash_radius=0.42),
                  Succession(*[ShowPassingFlash(
                      s.copy().set_stroke(AMARELO, width=6), time_width=0.7)
                      for s in trilha]), run_time=0.9 * VEL)

    # quatro saltos ×8 para voltar ao 1 ⇒ r = 4
    rper = formula(("r", AMARELO), ("=", PRETO), ("4", AMARELO),
                   tamanho=32).move_to([5.95, 1.52, 0])
    # a fala tem dois tempos — os quatro passos, depois o valor — e a animação
    # acompanha: os ×8 acendem em cascata, e só então o r nasce.
    # O Indicate no 4 vai em play PRÓPRIO: dentro do Write ele guardaria o
    # estado sem preenchimento que o Write instala no começo e o devolveria
    # no fim, deixando o 4 invisível
    with narra(cena, "C10N04", 4.9):
        cena.play(LaggedStart(*[Indicate(m, color=LARANJA) for m in rots],
                              lag_ratio=0.25), run_time=1.4 * VEL)
        cena.play(Write(rper), run_time=1.0 * VEL)
        cena.play(Indicate(rper[2], color=AMARELO), run_time=0.6 * VEL)

    # a ordem escrita como congruência — nasce do passeio
    e1 = VGroup(pot("8", "4", VERMELHO, AMARELO, 32), T("≡", 32, PRETO),
                T("1", 32, VERDE), fmod("35", 30))
    e1.arrange(RIGHT, buff=0.15).move_to([0, 0.45, 0])
    with narra(cena, "C10N05", 3.0):
        cena.play(Write(e1), Indicate(rper, color=AMARELO), run_time=1.1 * VEL)

    # passa o 1 para o outro lado — 8⁴ − 1 é múltiplo de 35.
    # O passeio cumpriu o papel e sai no COMEÇO desta fala (r = 4 fica, sobe
    # para o canto); a congruência só se move depois
    e2 = VGroup(pot("8", "4", VERMELHO, AMARELO, 32), T("− 1", 32, PRETO),
                T("≡", 32, PRETO), T("0", 32, VERDE), fmod("35", 30))
    # a conta sobe para a faixa que o passeio acabou de liberar: daqui em
    # diante ela é o teto do capítulo, e as árvores crescem debaixo dela
    e2.arrange(RIGHT, buff=0.15).move_to([0, 2.15, 0])
    nota = formula(("8⁴ − 1", PRETO), ("é múltiplo de", CINZA),
                   ("35", LARANJA), tamanho=24,
                   buff=0.12).next_to(e2, DOWN, buff=0.28)
    # os dois destaques desta linha (o "− 1" e o 35 da nota) vão em play
    # próprio, pela mesma razão do C10N04: Indicate junto do transform que
    # traz o e2 injetaria o "− 1" na cena como peça avulsa, que sobreviveria
    # ao e2 → e3 e ficaria de fantasma em cima do e4
    with narra(cena, "C10N06", 8.4):
        cena.play(FadeOut(VGroup(reta, lim, marcas, saltos, rots,
                                 base, rotulo)),
                  rper.animate.move_to([6.0, 2.6, 0]),
                  run_time=0.8 * VEL)
        cena.play(ReplacementTransform(e1, e2), run_time=1.0 * VEL)
        cena.play(Indicate(e2[1], color=PRETO), run_time=0.6 * VEL)
        # a nota escreve a frase que a fala acaba de dizer
        cena.play(FadeIn(nota), run_time=0.8 * VEL)
        cena.play(Indicate(nota[2], color=LARANJA), run_time=0.6 * VEL)

    # quantas vezes o 35 cabe? 8⁴ − 1 = x · 35
    e3 = VGroup(pot("8", "4", VERMELHO, AMARELO, 32), T("− 1 =", 32, PRETO),
                T("x", 32, PRETO), T("·", 32, PRETO), T("35", 32, LARANJA))
    e3.arrange(RIGHT, buff=0.15).move_to(e2)
    with narra(cena, "C10N07", 5.3):
        cena.play(ReplacementTransform(e2, e3), FadeOut(nota),
                  run_time=1.0 * VEL)
        cena.play(Indicate(e3[4], color=LARANJA), Indicate(e3[2], color=PRETO),
                  run_time=0.9 * VEL)

    # a PRIMEIRA ÁRVORE nasce junto da conta: 8⁴ − 1 se abre em x e 35.
    # A ordem dos ramos é a ordem da conta — x à esquerda, 35 à direita —
    # porque a equação vai morar logo acima da árvore e as duas têm de ser
    # lidas do mesmo jeito
    rb = VGroup(pot("8", "4", VERMELHO, AMARELO, 26),
                T("− 1", 26, PRETO)).arrange(RIGHT, buff=0.08)
    rb.move_to([3.5, -0.5, 0])
    fBx = T("x", 28, PRETO).move_to([2.55, -1.55, 0])
    fB35 = T("35", 28, LARANJA).move_to([4.45, -1.55, 0])
    linB = VGroup(liga(rb, fBx), liga(rb, fB35))
    with narra(cena, "C10N08", 6.9):
        cena.play(ReplacementTransform(VGroup(e3[0], e3[1]).copy(), rb),
                  run_time=0.9 * VEL)
        cena.play(Create(linB[0]), Create(linB[1]),
                  ReplacementTransform(e3[2].copy(), fBx),
                  ReplacementTransform(e3[4].copy(), fB35), run_time=0.9 * VEL)
        # "o tronco em cima" e "os fatores embaixo": a árvore que reparte
        cena.play(Indicate(rb, color=CINZA), run_time=0.7 * VEL)
        cena.play(Indicate(VGroup(fBx, fB35), color=CINZA), run_time=0.7 * VEL)

    # x = (8⁴ − 1)/35 = 117 — a conta preenche a árvore e DESCE para a faixa
    # da própria árvore, devolvendo o topo do quadro para a diferença de
    # quadrados. O `eqB` inteiro (cabeça + cauda) já nasce arranjado e
    # centrado na árvore: só a cabeça é escrita agora, e o lugar da cauda
    # fica reservado à direita — quando ela chegar, no C10N15, nada reflui
    ex = formula(("x", PRETO), ("=", PRETO), ("(8⁴ − 1)", PRETO),
                 ("/", PRETO), ("35", LARANJA), ("=", PRETO),
                 ("117", PRETO), tamanho=24,
                 buff=0.10).next_to(e3, DOWN, buff=0.28)
    e4 = VGroup(pot("8", "4", VERMELHO, AMARELO, 32), T("− 1 =", 32, PRETO),
                T("117", 32, PRETO), T("·", 32, PRETO), T("35", 32, LARANJA))
    e4.arrange(RIGHT, buff=0.15).move_to(e3)
    fB117 = T("117", 28, PRETO).move_to(fBx)
    eqB_a = VGroup(pot("8", "4", VERMELHO, AMARELO, 26), T("− 1 =", 26, PRETO),
                   T("117", 26, PRETO), T("·", 26, PRETO),
                   T("35", 26, LARANJA)).arrange(RIGHT, buff=0.10)
    eqB_b = VGroup(T("= (z · y) · (", 26, PRETO), T("q", 26, VERDE2),
                   T("·", 26, PRETO), T("p", 26, ROSA),
                   T(")", 26, PRETO)).arrange(RIGHT, buff=0.07)
    eqB = VGroup(eqB_a, eqB_b).arrange(RIGHT, buff=0.16)
    eqB.move_to([3.5, 0.62, 0])
    with narra(cena, "C10N09", 7.9):
        cena.play(Write(ex), Indicate(fBx, color=PRETO), run_time=0.9 * VEL)
        cena.play(ReplacementTransform(e3, e4), FadeOut(ex),
                  ReplacementTransform(fBx, fB117), run_time=1.0 * VEL)
        cena.play(ReplacementTransform(e4, eqB_a), run_time=1.0 * VEL)

    # r é PAR → o produto notável, no topo do quadro que acabou de vagar.
    # O nome "diferença de quadrados" fica só na fala: na tela entra direto a
    # identidade GENÉRICA, com o x ainda solto, sem base nenhuma — é ela que
    # vai virar a conta do 8
    d0 = formula(("r", AMARELO), ("par", PRETO), ("⇒", PRETO), tamanho=24,
                 buff=0.12)
    dgen = VGroup(T("x²", 24, PRETO), T("− 1 =", 24, PRETO),
                  T("(", 24, PRETO), T("x", 24, PRETO),
                  T("− 1)(", 24, PRETO), T("x", 24, PRETO),
                  T("+ 1)", 24, PRETO)).arrange(RIGHT, buff=0.06)
    # a linha inteira já nasce diagramada: a identidade entra agora no lugar
    # definitivo e o espaço do "r par ⇒" fica reservado à esquerda — quando ele
    # chegar, no C10N11, nada reflui
    VGroup(d0, dgen).arrange(RIGHT, buff=0.12).move_to([0, 2.15, 0])
    # animação curta sob fala longa: depois do Write o quadro fica parado o
    # resto da linha, segurando a identidade genérica em cena
    with narra(cena, "C10N10", 8.8):
        cena.play(Indicate(eqB_a, color=CINZA), run_time=0.8 * VEL)
        # a identidade se escreve devagar, token a token, sem passar por texto
        cena.play(Write(dgen), run_time=2.0 * VEL)

    d1 = VGroup(pot("8", "4", VERMELHO, AMARELO, 28), T("− 1 =", 28, PRETO),
                T("(", 28, PRETO), pot("8", "2", VERMELHO, AMARELO, 28),
                T("− 1)(", 28, PRETO), pot("8", "2", VERMELHO, AMARELO, 28),
                T("+ 1)", 28, PRETO))
    d1.arrange(RIGHT, buff=0.10).move_to([0, 2.15, 0])
    d2 = VGroup(pot("8", "4", VERMELHO, AMARELO, 28), T("− 1 =", 28, PRETO),
                T("65", 28, PRETO), T("·", 28, PRETO), T("63", 28, PRETO))
    d2.arrange(RIGHT, buff=0.14).move_to(d1)
    # esta linha é só o "r par ⇒" nascendo — nada mais compete pelo tempo
    # dela, e é isso que faz a condição pesar antes da manobra continuar
    with narra(cena, "C10N11", 4.6):
        cena.play(TransformFromCopy(rper[0], d0[0]), Write(d0[1:3]),
                  run_time=2.6 * VEL)

    # a substituição x → 8² roda em silêncio, como a segunda árvore que nasce
    # muda antes do C10N12: nem C10N10 nem C10N11 dizem "oito" em voz alta.
    # O "r par ⇒" já cumpriu o papel de justificar a manobra e some; o "8⁴ − 1"
    # não é reescrito do vazio, volta como cópia da conta que já está em cena
    # o "r par ⇒" sai sozinho, um instante antes: sem ele competindo, a troca
    # token a token fica legível e a substituição respira
    cena.play(FadeOut(VGroup(d0[0], d0[1], d0[2])), run_time=0.6 * VEL)
    cena.play(FadeOut(VGroup(dgen[0], dgen[1])),
              TransformFromCopy(eqB_a[0], d1[0]),
              TransformFromCopy(eqB_a[1], d1[1]),
              ReplacementTransform(dgen[2], d1[2]),
              ReplacementTransform(dgen[3], d1[3]),
              ReplacementTransform(dgen[4], d1[4]),
              ReplacementTransform(dgen[5], d1[5]),
              ReplacementTransform(dgen[6], d1[6]),
              run_time=1.6 * VEL)
    cena.add(d1)
    cena.play(ReplacementTransform(d1, d2), run_time=1.3 * VEL)

    # a SEGUNDA ÁRVORE: o mesmo 8⁴ − 1 se abre em 65 e 63
    ra = VGroup(pot("8", "4", VERMELHO, AMARELO, 26),
                T("− 1", 26, PRETO)).arrange(RIGHT, buff=0.08)
    ra.move_to([-3.5, -0.5, 0])
    fA65 = T("65", 28, PRETO).move_to([-4.45, -1.55, 0])
    fA63 = T("63", 28, PRETO).move_to([-2.55, -1.55, 0])
    linA = VGroup(liga(ra, fA65), liga(ra, fA63))
    cena.play(ReplacementTransform(VGroup(d2[0], d2[1]).copy(), ra),
              run_time=0.9 * VEL)
    cena.play(Create(linA[0]), Create(linA[1]),
              ReplacementTransform(d2[2].copy(), fA65),
              ReplacementTransform(d2[4].copy(), fA63), run_time=0.9 * VEL)

    # a conta da esquerda desce para a faixa da SUA árvore, espelhando o que a
    # da direita fez no C10N10 — mesmo espaço reservado à direita
    eqA_a = VGroup(pot("8", "4", VERMELHO, AMARELO, 26), T("− 1 =", 26, PRETO),
                   T("65", 26, PRETO), T("·", 26, PRETO),
                   T("63", 26, PRETO)).arrange(RIGHT, buff=0.10)
    eqA_b = VGroup(T("= (", 26, PRETO), T("p", 26, ROSA),
                   T("· y) · (z ·", 26, PRETO), T("q", 26, VERDE2),
                   T(")", 26, PRETO)).arrange(RIGHT, buff=0.07)
    eqA = VGroup(eqA_a, eqA_b).arrange(RIGHT, buff=0.16)
    eqA.move_to([-3.5, 0.62, 0])

    # as DUAS fatorações do MESMO número: a igualdade do meio não é escrita,
    # ela NASCE dos dois lados direitos — um voando de cada equação
    junta = formula(("65 · 63", PRETO), ("=", PRETO), ("117 ·", PRETO),
                    ("35", LARANJA), tamanho=30,
                    buff=0.12).move_to([0, 2.15, 0])
    with narra(cena, "C10N12", 5.5):
        cena.play(ReplacementTransform(d2, eqA_a), run_time=0.9 * VEL)
        cena.play(TransformFromCopy(eqA_a[2:5], junta[0]),
                  TransformFromCopy(eqB_a[2:5], junta[2:4]),
                  Write(junta[1]), run_time=1.0 * VEL)
        cena.add(junta)
        # os dois troncos acendem juntos: é o mesmo número aberto de dois jeitos
        cena.play(Indicate(ra, color=CINZA), Indicate(rb, color=CINZA),
                  run_time=0.9 * VEL)

    # dentro do 117 moram z e y; dentro do 35, q e p — e a cauda reservada da
    # equação da direita é preenchida com esses mesmos quatro fatores
    nB = VGroup(T("z", 26, PRETO).move_to([1.95, -2.55, 0]),
                T("y", 26, PRETO).move_to([3.15, -2.55, 0]),
                T("q", 26, VERDE2).move_to([3.85, -2.55, 0]),
                T("p", 26, ROSA).move_to([5.05, -2.55, 0]))
    linB2 = VGroup(liga(fB117, nB[0]), liga(fB117, nB[1]),
                   liga(fB35, nB[2]), liga(fB35, nB[3]))
    j2 = formula(("65 · 63", PRETO), ("=", PRETO), ("(z · y) · (", PRETO),
                 ("q", VERDE2), ("·", PRETO), ("p", ROSA), (")", PRETO),
                 tamanho=30, buff=0.10).move_to(junta)
    with narra(cena, "C10N13", 5.3):
        cena.play(*[Create(l) for l in linB2], FadeIn(nB), run_time=0.9 * VEL)
        cena.play(Write(eqB_b), ReplacementTransform(junta, j2),
                  run_time=1.1 * VEL)
        # "os dois primos" são os dois últimos do nB (a ordem é z, y, q, p);
        # "números desconhecidos", os dois primeiros
        cena.play(Indicate(nB[2], color=VERDE2), Indicate(nB[3], color=ROSA),
                  run_time=0.7 * VEL)
        cena.play(Indicate(nB[0], color=PRETO), Indicate(nB[1], color=PRETO),
                  run_time=0.7 * VEL)

    # pela COMUTATIVIDADE, os mesmos quatro fatores se reagrupam em 65 e 63:
    # primeiro a igualdade do meio se reescreve, depois os fatores descem
    # para a árvore da esquerda e para a cauda reservada da equação dela
    comut = T("pela comutatividade da multiplicação", 20,
              CINZA).move_to([0, 1.35, 0])
    nA = VGroup(T("p", 26, ROSA).move_to([-5.05, -2.55, 0]),
                T("y", 26, PRETO).move_to([-3.85, -2.55, 0]),
                T("z", 26, PRETO).move_to([-3.15, -2.55, 0]),
                T("q", 26, VERDE2).move_to([-1.95, -2.55, 0]))
    linA2 = VGroup(liga(fA65, nA[0]), liga(fA65, nA[1]),
                   liga(fA63, nA[2]), liga(fA63, nA[3]))
    j3 = formula(("(", PRETO), ("p", ROSA), ("· y) · (z ·", PRETO),
                 ("q", VERDE2), (")", PRETO), ("=", PRETO),
                 ("(z · y) · (", PRETO), ("q", VERDE2), ("·", PRETO),
                 ("p", ROSA), (")", PRETO),
                 tamanho=30, buff=0.10).move_to(j2)
    with narra(cena, "C10N14", 6.7):
        # "como isso é uma igualdade": o sinal de igual do meio
        cena.play(FadeIn(comut), Indicate(j2[1], color=PRETO),
                  run_time=0.7 * VEL)
        cena.play(ReplacementTransform(j2, j3), run_time=1.0 * VEL)
        cena.play(*[Create(l) for l in linA2], FadeIn(nA), Write(eqA_b),
                  run_time=1.1 * VEL)

    # o p mora no 65 E no 35; o q mora no 63 E no 35 — cada um caiu de um lado,
    # e é dessa separação que os fatores úteis de n dependem
    with narra(cena, "C10N15", 7.3):
        cena.play(Indicate(nA[0], color=ROSA), Indicate(nB[3], color=ROSA),
                  run_time=0.9 * VEL)
        cena.play(Indicate(nA[3], color=VERDE2), Indicate(nB[2], color=VERDE2),
                  run_time=0.9 * VEL)
        cena.play(Indicate(obj[0], color=LARANJA), run_time=0.8 * VEL)

    expl = formula(("65 e 63", PRETO), ("compartilham fatores com", CINZA),
                   ("35", LARANJA), tamanho=22, buff=0.12).move_to(comut)
    with narra(cena, "C10N16", 8.4):
        # "os dois números que acabamos de calcular"
        cena.play(Indicate(fA65, color=PRETO), Indicate(fA63, color=PRETO),
                  run_time=0.9 * VEL)
        cena.play(ReplacementTransform(comut, expl), run_time=0.8 * VEL)
        # "o número que queremos fatorar"
        cena.play(Indicate(expl[2], color=LARANJA), run_time=0.8 * VEL)

    # o mdc PESCA os fatores compartilhados
    m1 = formula(("mdc(", PRETO), ("63", PRETO), (", ", PRETO),
                 ("35", LARANJA), (") =", PRETO), ("7", VERDE2),
                 tamanho=26, buff=0.08).move_to([-0.2, -1.55, 0])
    m2 = formula(("mdc(", PRETO), ("65", PRETO), (", ", PRETO),
                 ("35", LARANJA), (") =", PRETO), ("5", ROSA),
                 tamanho=26, buff=0.08).move_to([-0.2, -2.25, 0])
    with narra(cena, "C10N17", 9.6):
        cena.play(Write(m1), Indicate(nA[3], color=VERDE2),
                  Indicate(nB[2], color=VERDE2), run_time=1.0 * VEL)
        cena.play(Write(m2), Indicate(nA[0], color=ROSA),
                  Indicate(nB[3], color=ROSA), run_time=1.0 * VEL)

    # p e q foram encontrados: 35 = 5 × 7
    fim = formula(("35", LARANJA), ("=", PRETO), ("5", ROSA), ("×", PRETO),
                  ("7", VERDE2), tamanho=36).move_to([-0.2, -3.0, 0])
    cxa = SurroundingRectangle(fim, color=VERDE, buff=0.2, corner_radius=0.14)
    with narra(cena, "C10N18", 7.3):
        cena.play(ReplacementTransform(VGroup(m1, m2), fim), Create(cxa),
                  run_time=1.1 * VEL)
        # "os fatores p e q"
        cena.play(Indicate(fim[2], color=ROSA), Indicate(fim[4], color=VERDE2),
                  run_time=0.9 * VEL)

    obj2 = formula(("n", LARANJA), ("=", PRETO), ("35", LARANJA),
                   ("=", PRETO), ("5", ROSA), ("×", PRETO), ("7", VERDE2),
                   ("✓", VERDE), tamanho=34).move_to(obj)
    with narra(cena, "C10N19", 3.8):
        cena.play(ReplacementTransform(obj, obj2), run_time=1.0 * VEL)
        cena.play(Indicate(obj2[7], color=VERDE), run_time=0.7 * VEL)

    # ---------- o caso INÚTIL (slides 19–20): a = 24 ----------
    # a limpeza pertence a ESTA fala e vai EMENDADA no FadeIn: separada, ela
    # leria como fim de capítulo. O `fim` na moldura verde NÃO sai — o sucesso
    # segue à vista enquanto a falha roda, e o C10N33 puxa φ(35) dele
    cap5 = T("às vezes a ordem modular não dá informação útil",
             24).move_to([0, 2.45, 0])
    with narra(cena, "C10N20", 9.6):
        cena.play(FadeOut(VGroup(j3, expl, eqA, ra, linA, fA65, fA63, nA,
                                 linA2, eqB, rb, linB, fB117, fB35, nB, linB2,
                                 rper)),
                  FadeIn(cap5), run_time=0.8 * VEL)

    with narra(cena, "C10N21", 3.3):
        cena.play(Indicate(cap5, color=CINZA), run_time=0.9 * VEL)

    u0 = formula(("a", VERMELHO), ("=", PRETO), ("24", VERMELHO),
                 ("→", CINZA), ("r", AMARELO), ("=", PRETO), ("6", AMARELO),
                 tamanho=28).move_to([0, 1.7, 0])
    with narra(cena, "C10N22", 3.7):
        cena.play(Write(u0), run_time=0.9 * VEL)
        cena.play(Indicate(u0[6], color=AMARELO), run_time=0.8 * VEL)

    # a mesma manobra do C10N10–C10N11 (x → 24³ na diferença de quadrados),
    # só que rápida: a fala é seca de propósito, a tela repete um trajeto
    # que o espectador acabou de ver — nada aqui é texto corrido
    u1a = VGroup(pot("24", "6", VERMELHO, AMARELO, 26), T("− 1 =", 26, PRETO),
                 T("(", 26, PRETO), pot("24", "3", VERMELHO, AMARELO, 26),
                 T("− 1)(", 26, PRETO), pot("24", "3", VERMELHO, AMARELO, 26),
                 T("+ 1)", 26, PRETO))
    u1a.arrange(RIGHT, buff=0.08).move_to([0, 0.9, 0])
    u1 = VGroup(pot("24", "6", VERMELHO, AMARELO, 26), T("− 1 =", 26, PRETO),
                T("13825", 26, PRETO), T("·", 26, PRETO),
                T("13823", 26, PRETO))
    u1.arrange(RIGHT, buff=0.12).move_to(u1a)
    with narra(cena, "C10N23", 3.3):
        cena.play(Write(u1a), run_time=1.0 * VEL)
        cena.play(ReplacementTransform(u1a, u1), run_time=1.0 * VEL)

    # a árvore do azar: p e q caem JUNTOS no 13825 (múltiplo de 35)
    ru = VGroup(pot("24", "6", VERMELHO, AMARELO, 24),
                T("− 1", 24, PRETO)).arrange(RIGHT, buff=0.08)
    ru.move_to([-2.8, -0.25, 0])
    fu1 = T("13825", 26, PRETO).move_to([-4.3, -1.25, 0])
    fu2 = T("13823", 26, PRETO).move_to([-1.3, -1.25, 0])
    linU = VGroup(liga(ru, fu1), liga(ru, fu2))
    nU = VGroup(T("p", 24, ROSA).move_to([-4.9, -2.05, 0]),
                T("q", 24, VERDE2).move_to([-3.7, -2.05, 0]),
                T("z", 24, PRETO).move_to([-1.9, -2.05, 0]),
                T("y", 24, PRETO).move_to([-0.7, -2.05, 0]))
    linU2 = VGroup(liga(fu1, nU[0]), liga(fu1, nU[1]),
                   liga(fu2, nU[2]), liga(fu2, nU[3]))
    with narra(cena, "C10N24", 5.5):
        cena.play(ReplacementTransform(VGroup(u1[0], u1[1]).copy(), ru),
                  run_time=0.9 * VEL)
        cena.play(Create(linU[0]), Create(linU[1]),
                  ReplacementTransform(u1[2].copy(), fu1),
                  ReplacementTransform(u1[4].copy(), fu2), run_time=0.9 * VEL)
        cena.play(*[Create(l) for l in linU2], FadeIn(nU), run_time=1.0 * VEL)
        cena.play(Indicate(nU[0], color=ROSA), Indicate(nU[1], color=VERDE2),
                  run_time=0.9 * VEL)

    multi = formula(("múltiplo de", CINZA), ("35", LARANJA),
                    tamanho=20, buff=0.10).move_to([-5.45, -0.5, 0])
    setam = Arrow(multi.get_bottom() + 0.05 * DOWN,
                  fu1.get_top() + 0.08 * UP, buff=0, color=PRETO,
                  stroke_width=3, max_tip_length_to_length_ratio=0.2)
    with narra(cena, "C10N25", 3.8):
        cena.play(FadeIn(multi), GrowArrow(setam),
                  Indicate(fu1, color=PRETO), run_time=1.1 * VEL)
        cena.play(Indicate(multi[1], color=LARANJA), run_time=0.7 * VEL)

    # o mdc devolve só fatores TRIVIAIS: 35 e 1
    m3 = formula(("mdc(", PRETO), ("13825", PRETO), (", ", PRETO),
                 ("35", LARANJA), (") =", PRETO), ("35", LARANJA),
                 tamanho=26, buff=0.08).move_to([3.7, -0.6, 0])
    m4 = formula(("mdc(", PRETO), ("13823", PRETO), (", ", PRETO),
                 ("35", LARANJA), (") =", PRETO), ("1", PRETO),
                 tamanho=26, buff=0.08).move_to([3.7, -1.25, 0])
    # o destaque no resultado vai em play PRÓPRIO, pela razão do C10N04:
    # dentro do Write ele guardaria o estado sem preenchimento do começo e o
    # devolveria no fim, deixando o resultado invisível o resto do capítulo
    with narra(cena, "C10N26", 3.3):
        cena.play(Write(m3), run_time=0.9 * VEL)
        cena.play(Indicate(m3[5], color=LARANJA), run_time=0.7 * VEL)

    with narra(cena, "C10N27", 4.2):
        cena.play(Write(m4), run_time=0.9 * VEL)
        cena.play(Indicate(m4[5], color=PRETO), run_time=0.7 * VEL)

    triv = formula(("fatores triviais", VERMELHO), ("✗", VERMELHO),
                   tamanho=24, buff=0.12).move_to([3.7, -1.95, 0])
    sol = T("solução: escolher outro a e recomeçar", 20,
            CINZA).move_to([3.7, -2.5, 0])
    # animação curta sob fala longa: o quadro fica parado no ✗ vermelho
    # durante a segunda metade da linha, e é essa parada que faz a falha pesar
    with narra(cena, "C10N28", 14.4):
        cena.play(Write(triv), FadeIn(sol), run_time=1.0 * VEL)
        cena.play(Indicate(m3[5], color=LARANJA), Indicate(m4[5], color=PRETO),
                  run_time=0.9 * VEL)

    # ---------- POR QUE isso quebra o RSA (lembrete do Capítulo 8) ----------
    # com p e q em mãos, φ(n) sai de graça — e com φ(n), a chave privada d.
    # A contagem de Euler NASCE DE DENTRO dos dois primos que ficaram na
    # moldura verde, e a limpeza do caso inútil vai emendada no mesmo play
    r1 = formula(("φ(", PRETO), ("35", LARANJA), (")", PRETO), ("=", PRETO),
                 ("(", PRETO), ("5", ROSA), ("− 1)", PRETO), ("×", PRETO),
                 ("(", PRETO), ("7", VERDE2), ("− 1)", PRETO), ("=", PRETO),
                 ("24", PRETO), tamanho=30, buff=0.10).move_to([0, 1.8, 0])
    with narra(cena, "C10N32", 7.1):
        cena.play(FadeOut(VGroup(cap5, u0, u1, ru, linU, fu1, fu2, nU, linU2,
                                 multi, setam, m3, m4, triv, sol)),
                  ReplacementTransform(fim.copy(), r1), run_time=1.1 * VEL)

    r2 = formula(("e", VERMELHO), ("·", PRETO), ("d", AZUL), ("≡", PRETO),
                 ("1", VERDE), ("(mod φ(", PRETO), ("n", LARANJA),
                 ("))", PRETO), ("⇒", PRETO), ("d", AZUL),
                 ("encontrado", PRETO),
                 tamanho=28, buff=0.10).move_to([0, 0.7, 0])
    with narra(cena, "C10N33", 8.8):
        cena.play(Write(r2), run_time=1.0 * VEL)

    r3 = formula(("fatorar", PRETO), ("n", LARANJA), ("=", PRETO),
                 ("descobrir a chave privada", PRETO),
                 tamanho=30).move_to([0, -0.6, 0])
    cxa2 = SurroundingRectangle(r3, color=VERDE, buff=0.2,
                                corner_radius=0.14)
    with narra(cena, "C10N34", 5.4):
        cena.play(Write(r3), Create(cxa2), run_time=1.1 * VEL)

    # a tese fica parada em cena enquanto a fala passa o bastão ao quântico
    so_fala(cena, "C10N35", 9.2)
