# -*- coding: utf-8 -*-
from manim import *
import numpy as np

from ..paleta import *
from ..ferramentas import *


# ---------------------------------------------------------------------------
# peças do capítulo 10
# ---------------------------------------------------------------------------
def _carta_qubit(w=0.78, h=1.02, tam=22):
    """Cartão de qubit em superposição (gradiente verde↔laranja dos slides)."""
    r = RoundedRectangle(corner_radius=0.10, width=w, height=h,
                         stroke_width=0)
    r.set_fill(color=[LARANJA, VERDE], opacity=1)
    r.set_sheen_direction(UR)
    um = T("1", tam, PRETO).move_to(r.get_center() + [0.18, 0.26, 0])
    zero = T("0", tam, PRETO).move_to(r.get_center() + [-0.18, -0.26, 0])
    return VGroup(r, um, zero)


def _carta_fixa(txt, cor, w=0.78, h=1.02, tam=22):
    """Cartão colapsado: verde para 1, laranja para 0 (slide 148)."""
    r = RoundedRectangle(corner_radius=0.10, width=w, height=h,
                         stroke_width=0).set_fill(cor, opacity=1)
    return VGroup(r, T(txt, tam, PRETO).move_to(r))


def _fila_classica(n=9, buff=0.34):
    """A fila de bits clássicos do C11N01: cartões chapados alternando 0
    laranja e 1 verde. Ímpar de propósito — o cartão do meio é um `0` e fica
    no centro do quadro, que é onde o bloco inteiro vai acontecer."""
    cartas = [_carta_fixa("0", LARANJA) if i % 2 == 0 else _carta_fixa("1", VERDE)
              for i in range(n)]
    return VGroup(*cartas).arrange(RIGHT, buff=buff)


def _barras_peso(carta, p1=0.68, p0=0.32, alt=1.55, larg=0.34):
    """As barras de peso do C11N06: a chance de a medida devolver 1 (verde)
    e a de devolver 0 (laranja), apoiadas na base do cartão. Alturas
    diferentes de propósito — o qubit não é meio a meio."""
    b1 = Rectangle(width=larg, height=alt * p1,
                   stroke_width=0).set_fill(VERDE, opacity=1)
    b0 = Rectangle(width=larg, height=alt * p0,
                   stroke_width=0).set_fill(LARANJA, opacity=1)
    barras = VGroup(b1, b0).arrange(RIGHT, buff=0.22, aligned_edge=DOWN)
    return barras.next_to(carta, RIGHT, buff=0.34, aligned_edge=DOWN)


def _expo_2i(i, tam=15):
    """O expoente 2ⁱ das portas, montado à mão em vez de com `pot()`.

    Duas razões, e as duas eram o motivo de o expoente não aparecer no fio
    de baixo: o `pot()` tem piso de 14 px no expoente, que aqui deixaria o
    `i` maior que o `2` que ele exponencia; e escrever "2⁰" com o algarismo
    unicode sobrescrito devolve um glifo de sete pixels, ilegível em 1080p.
    Aqui o `i` é um `Text` de verdade, com tamanho próprio. Azul porque
    este expoente é um pedaço do `b` do `c ≡ 2ᵇ (mod 21)` lá em cima."""
    b = T("2", tam, AZUL)
    e = T(i, max(int(tam * 0.78), 10), AZUL)
    e.next_to(b.get_corner(UR), RIGHT, buff=0.02).shift(0.05 * UP)
    return VGroup(b, e)


def _caixa_porta(i, w=1.72, h=1.15, tam=20):
    """Porta 2^(2ⁱ) (mod 21) do circuito: gradiente com o "1" embaixo.

    O gradiente entra a 0,7 de opacidade: cheio, ele tem a mesma
    luminosidade das cores da paleta que escrevem por cima dele e engolia
    o rótulo inteiro. Os cartõezinhos de qubit continuam a 1 — eles só
    carregam preto."""
    r = RoundedRectangle(corner_radius=0.10, width=w, height=h,
                         stroke_width=0)
    r.set_fill(color=[LARANJA, VERDE], opacity=0.7)
    r.set_sheen_direction(UP)
    topo = VGroup(pot("2", _expo_2i(i), VERMELHO, tam=tam), fmod("21", 15))
    topo.arrange(RIGHT, buff=0.07).move_to(r.get_center() + [0, 0.26, 0])
    um = T("1", tam, PRETO).move_to(r.get_center() + [0, -0.30, 0])
    return VGroup(r, topo, um)


def _carta_super(valores, cor, cor2, passo=0.55, larg=1.16, tam=24, op=0.30):
    """O cartão de superposição de um registrador, pousado no fio depois das
    portas: a coluna dos valores que ele pode devolver, num degradê da cor do
    próprio registrador, com o `⋮` embaixo dizendo que a sequência segue.

    É a versão em lista do cartão-gradiente do qubit — mesma ideia, mas
    guardando números em vez de bits. O degradê entra fraco (0,3) porque
    quem tem que ser lido são os números, não o fundo; forte, ele apaga a
    cor da paleta que escreve por cima dele.

    O fundo são dois retângulos: uma base branca opaca e o degradê por
    cima. A base existe porque o painel pousa EM CIMA dos fios — sem ela os
    traços pretos atravessariam a coluna de números.

    Devolve `VGroup(fundo, numeros, ⋮)`: os números vivem num VGroup
    próprio porque o colapso da medida troca só eles, deixando o fundo e o
    `⋮` em cena."""
    alt = (len(valores) + 1) * passo + 0.16
    base = RoundedRectangle(corner_radius=0.10, width=larg, height=alt,
                            stroke_width=0).set_fill(BRANCO, opacity=1)
    grad = RoundedRectangle(corner_radius=0.10, width=larg, height=alt,
                            stroke_width=0)
    grad.set_fill(color=[cor2, cor], opacity=op)
    grad.set_sheen_direction(UP)
    fundo = VGroup(base, grad)
    y0 = fundo.get_top()[1] - passo / 2 - 0.08
    nums = VGroup(*[T(v, tam, cor).move_to([fundo.get_x(), y0 - i * passo, 0])
                    for i, v in enumerate(valores)])
    tres = T("⋮", tam + 6, cor).move_to([fundo.get_x(),
                                         y0 - len(valores) * passo, 0])
    # o conteúdo sobe por z_index, e não pela ordem de entrada em cena: um
    # `ReplacementTransform` herda a posição z da ORIGEM, então uma coluna
    # que nasce de peça antiga entraria atrás do fundo e sumiria
    nums.set_z_index(1)
    tres.set_z_index(1)
    return VGroup(fundo, nums, tres)


def _carta_valor(txt, cor, cor2, larg=1.16, alt=0.88, tam=34, op=0.30):
    """O painel depois do colapso: o mesmo fundo do `_carta_super`, com um
    valor só dentro. O número medido aparece EM CAIXA, do jeito que a letra
    genérica aparecia — solto em cima do fio ele não lê como conteúdo de
    registrador, lê como rótulo do fio."""
    base = RoundedRectangle(corner_radius=0.10, width=larg, height=alt,
                            stroke_width=0).set_fill(BRANCO, opacity=1)
    grad = RoundedRectangle(corner_radius=0.10, width=larg, height=alt,
                            stroke_width=0)
    grad.set_fill(color=[cor2, cor], opacity=op)
    grad.set_sheen_direction(UP)
    fundo = VGroup(base, grad)
    val = T(txt, tam, cor).move_to(fundo).set_z_index(1)
    return VGroup(fundo, val)


def _caixa_classica(i, w=1.72, h=0.92, tam=20):
    """A caixa cinza do esquema do capítulo 4, com a base e o módulo DESTE
    capítulo: 2^(2ⁱ) (mod 21). É a mesma peça do `capitulo4.py`, só que com
    os nossos números — o capítulo 4 não muda.

    A largura é a mesma da `_caixa_porta` de propósito: no `C11N13` uma vira
    a outra sem mudar de tamanho, e é isso que faz a correspondência ser
    lida. Nenhuma caixa entra apagada porque aqui o `b` é genérico: não se
    sabe quais bits estão ligados, e é justamente esse "não se sabe" que o
    circuito vai resolver fazendo todos de uma vez."""
    r = RoundedRectangle(corner_radius=0.10, width=w, height=h,
                         stroke_width=0).set_fill(CAIXA, opacity=1)
    rot = VGroup(pot("2", _expo_2i(i), VERMELHO, tam=tam), fmod("21", 15))
    rot.arrange(RIGHT, buff=0.07).move_to(r)
    return VGroup(r, rot)


def _bit_i(i, tam=26):
    """O bit `bᵢ` do expoente. O índice é montado à mão pelo mesmo motivo do
    `_expo_2i`: em unicode ele sai como um glifo minúsculo."""
    b = T("b", tam, AZUL)
    e = T(i, max(int(tam * 0.62), 12), AZUL)
    e.next_to(b.get_corner(DR), RIGHT, buff=0.02).shift(0.06 * DOWN)
    return VGroup(b, e)


def _resto_i(i, tam=30):
    """O resto `cᵢ` que sai da caixa `2^(2ⁱ) (mod 21)`. Verde porque é um
    resto — a mesma cor do `c` que sai lá embaixo, que é o produto de todos
    eles. Índice montado à mão pelo mesmo motivo do `_bit_i`."""
    c = T("c", tam, VERDE)
    e = T(i, max(int(tam * 0.62), 12), VERDE)
    e.next_to(c.get_corner(DR), RIGHT, buff=0.02).shift(0.06 * DOWN)
    return VGroup(c, e)


def _seta(de, para, larg=0.25):
    """Seta preta fina do esquema de árvore dos slides 33/34."""
    return Arrow(de.get_bottom() + 0.05 * DOWN, para.get_top() + 0.05 * UP,
                 buff=0, color=PRETO, stroke_width=2.5,
                 max_tip_length_to_length_ratio=larg)


def _troca_coluna(modelo, valores, cor, tam=24):
    """Uma coluna nova de números no lugar exato da coluna `modelo`, para
    o `ReplacementTransform` do colapso e do rodízio de restos."""
    novos = VGroup(*[T(v, tam, cor) for v in valores])
    for n, m in zip(novos, modelo):
        n.move_to(m)
    return novos.set_z_index(1)


# ============================================================================
# CAPÍTULO 10 — Shor Quântico (slides 143–179), cores adaptadas ao branco
# ============================================================================
def p10_fundamentos(cena):
    """Slide 148: do bit clássico ao qubit — superposição e emaranhamento,
    os fenômenos que dão o paralelismo do computador quântico.

    A limpeza do bloco NÃO mora aqui: o `FadeOut` de fim pertence ao
    `C11N10` e roda no topo do `p10_circuito`, emendado com o `Write(eqc)`
    num `play` só. O que fica em cena espera em `cena.grupo_fundamentos`."""
    fila = _fila_classica()
    rot_cl = T("computação clássica", 26, CINZA).next_to(fila, UP, buff=0.55)
    with narra(cena, "C11N01", 7.9):
        cena.play(LaggedStart(*[FadeIn(c, scale=0.8) for c in fila],
                              lag_ratio=0.12),
                  FadeIn(rot_cl), run_time=1.8 * VEL)

    # o cartão do meio se destaca crescendo e esgota o repertório do bit:
    # 0 → 1 → 0, e acabou. É esse esgotamento que dá sentido ao gradiente
    meio = fila[4]
    bit_1 = _carta_fixa("1", VERDE).scale(1.5).move_to(meio)
    bit_0 = _carta_fixa("0", LARANJA).scale(1.5).move_to(meio)
    with narra(cena, "C11N02", 5.8):
        cena.play(Succession(
            ReplacementTransform(meio, bit_1, run_time=1.2 * VEL),
            ReplacementTransform(bit_1, bit_0, run_time=1.2 * VEL)))

    # a fila sai inteira MENOS o cartão do meio: ele já foi consumido pelo
    # ReplacementTransform e um FadeOut(fila) o traria de volta piscando
    resto_fila = VGroup(*fila[:4], *fila[5:])
    with narra(cena, "C11N03", 7.0):
        cena.play(FadeOut(resto_fila), FadeOut(rot_cl), run_time=1.0 * VEL)

    # REGRA 4: o qubit não entra em cena, ele NASCE do bit — o sólido vira
    # gradiente no lugar em que o cartão já estava
    qub = _carta_qubit().scale(1.5).move_to(bit_0)
    with narra(cena, "C11N04", 7.4):
        cena.play(ReplacementTransform(bit_0, qub), run_time=1.3 * VEL)

    t1 = T("superposição", 26, PRETO).move_to([-4.0, 2.6, 0])
    q1 = _carta_qubit().scale(1.15).move_to([-4.0, 1.3, 0])
    with narra(cena, "C11N05", 7.0):
        cena.play(FadeIn(t1), ReplacementTransform(qub, q1),
                  run_time=1.4 * VEL)

    # as duas barras nascem do próprio gradiente (q1[0]), não do vazio
    barras = _barras_peso(q1)
    with narra(cena, "C11N06", 7.0):
        cena.play(*[TransformFromCopy(q1[0], b) for b in barras],
                  run_time=1.2 * VEL)

    t2 = T("emaranhamento", 26, PRETO).move_to([2.6, 2.6, 0])
    qa = _carta_qubit().move_to([1.2, 1.3, 0])
    qb = _carta_qubit().move_to([3.9, -0.3, 0])
    no = Dot([3.9, 1.3, 0], radius=0.07, color=PRETO)
    fio = VGroup(Line(qa.get_right(), no.get_center(), color=PRETO,
                      stroke_width=2.5),
                 Line(no.get_center(), qb.get_top(), color=PRETO,
                      stroke_width=2.5))
    with narra(cena, "C11N07", 3.8):
        cena.play(FadeIn(qa, scale=0.8), run_time=0.8 * VEL)
        cena.play(Create(fio), FadeIn(no), FadeIn(qb, scale=0.8),
                  run_time=0.9 * VEL)

    # medir UM decide o OUTRO: os dois colapsam juntos (1,1) — ou (0,0)
    nota = T("medir um decide o outro", 22, CINZA).move_to([2.6, -1.8, 0])
    with narra(cena, "C11N08", 5.5):
        cena.play(FadeIn(nota), FadeIn(t2), run_time=0.7 * VEL)
    par_1 = VGroup(_carta_fixa("1", VERDE).move_to(qa),
                   _carta_fixa("1", VERDE).move_to(qb))
    par_0 = VGroup(_carta_fixa("0", LARANJA).move_to(par_1[0]),
                   _carta_fixa("0", LARANJA).move_to(par_1[1]))
    with narra(cena, "C11N09", 5.4):
        cena.play(Flash(qa.get_center(), color=VERDE, flash_radius=0.7),
                  ReplacementTransform(VGroup(qa, qb), par_1),
                  run_time=1.0 * VEL)
        cena.play(ReplacementTransform(par_1, par_0), run_time=0.9 * VEL)

    cena.grupo_fundamentos = VGroup(t1, q1, barras, t2, par_0, no, fio, nota)


# ---------------------------------------------------------------------------
# a geometria do circuito, compartilhada com o esquema clássico que o gera
# ---------------------------------------------------------------------------
YS = [2.0, 0.9, 0.1, -0.7]      # fios de controle, de cima para baixo
YT = -2.3                       # fio alvo
X0, X1 = -5.9, 6.6              # começo e fim dos fios
XS_CX = [-4.75, -2.85, -0.95, 1.75]   # onde ficam as portas
EXPOS = ["0", "1", "2", "8"]          # o i de cada 2^(2ⁱ)
CTRLS = [YS[3], YS[2], YS[1], YS[0]]  # qual fio controla cada porta
XRET = 0.40                     # o "…" das portas que não cabem
XP = 4.15                       # onde os dois painéis pousam
XTQF = 5.70                     # a TQF, depois do painel azul

# o esquema clássico mora nas MESMAS colunas do circuito, 1,5 à direita para
# o desenho ficar centrado no quadro. Como o deslocamento é o mesmo para as
# quatro caixas, o C11N13 é uma translação rígida — e é isso que deixa a
# correspondência legível
DX = 1.5
# cinco linhas, como no slide 34 do capítulo 4: bits, caixas, os restos que
# saem delas, o produto dos restos e o resultado
YBIT, YCX, YRES, YPROD, YC = 2.55, 1.30, 0.05, -1.15, -2.60


def p10_esquema(cena):
    """Slides 33–34 revisitados: o esquema de caixas cinzas do capítulo 4,
    refeito com a base e o módulo deste capítulo, para o circuito quântico
    entrar como tradução de uma coisa que o espectador já viu.

    Tudo genérico: `bᵢ` nas caixas de bit, `cᵢ` nos restos e `(c₀ × c₁ × …)
    (mod 21)` no produto, como no slide 34 do capítulo 4 — só que com letra no
    lugar do número. Sem exemplo numérico de propósito: o circuito não roda um
    `b`, ele roda todos, e um número na tela aqui diria o contrário.

    Abre limpando o bloco anterior: o `FadeOut` do `p10_fundamentos` é do
    `C11N10` e entra emendado com o `Write(eqc)`, num `play` só. O que fica
    em cena espera em `cena.esquema` — o `p10_circuito` transforma peça por
    peça no equivalente do circuito."""
    eqc = VGroup(T("c", 30, VERDE), T("≡", 30, PRETO),
                 pot("2", "b", VERMELHO, AZUL, 30), fmod("21", 28))
    eqc.arrange(RIGHT, buff=0.14).to_edge(UP, buff=0.4)
    with narra(cena, "C11N10", 9.0):
        cena.play(FadeOut(cena.grupo_fundamentos), Write(eqc),
                  run_time=1.0 * VEL)

    # linha de cima: os bits do expoente, um por coluna; embaixo, a caixa
    # que cada um liga ou desliga
    xs = [x + DX for x in XS_CX]
    bits = VGroup(*[caixa_cinza(_bit_i(i), pad=0.16).move_to([x, YBIT, 0])
                    for i, x in zip(EXPOS, xs)])
    caixas = VGroup(*[_caixa_classica(i).move_to([x, YCX, 0])
                      for i, x in zip(EXPOS, xs)])
    ret_bit = T("…", 28, PRETO).move_to([XRET + DX, YBIT, 0])
    ret_cx = T("…", 28, PRETO).move_to([XRET + DX, YCX, 0])
    setas1 = VGroup(*[_seta(b, c) for b, c in zip(bits, caixas)])
    with narra(cena, "C11N11", 9.0):
        cena.play(LaggedStart(*[FadeIn(b, scale=0.8) for b in bits],
                              lag_ratio=0.12),
                  FadeIn(ret_bit), run_time=1.6 * VEL)
        cena.play(LaggedStart(*[AnimationGroup(GrowArrow(s), FadeIn(c))
                                for s, c in zip(setas1, caixas)],
                              lag_ratio=0.14),
                  FadeIn(ret_cx), run_time=2.2 * VEL)

    # cada caixa devolve um resto — é a linha verde do slide 34, aqui com
    # letra em vez de número porque o b é genérico
    restos = VGroup(*[_resto_i(i).move_to([x, YRES, 0])
                      for i, x in zip(EXPOS, xs)])
    ret_res = T("…", 28, PRETO).move_to([XRET + DX, YRES, 0])
    setas2 = VGroup(*[_seta(c, r) for c, r in zip(caixas, restos)])

    # e o produto dos restos é a potência inteira: a caixa de baixo é a mesma
    # do capítulo 4, ( c₀ × c₁ × … ) (mod 21), e é ELA que devolve o c
    itens = [T("(", 30, PRETO), _resto_i("0"), T("×", 26, PRETO),
             _resto_i("1"), T("×", 26, PRETO), _resto_i("2"),
             T("×", 26, PRETO), T("…", 28, PRETO), T("×", 26, PRETO),
             _resto_i("8"), T(")", 30, PRETO), fmod("21", 26)]
    prod = caixa_cinza(VGroup(*itens).arrange(RIGHT, buff=0.12))
    prod.move_to([(xs[0] + xs[-1]) / 2, YPROD, 0])
    setas3 = VGroup(*[Arrow(r.get_bottom() + 0.05 * DOWN,
                            prod[0].get_top() + np.array([dx, 0.05, 0]),
                            buff=0, color=PRETO, stroke_width=2.5,
                            max_tip_length_to_length_ratio=0.16)
                      for r, dx in zip(restos, (-2.4, -0.8, 0.8, 2.4))])
    saida = T("c", 42, VERDE).move_to([prod.get_x(), YC, 0])
    seta4 = _seta(prod, saida)
    with narra(cena, "C11N12", 7.0):
        cena.play(LaggedStart(*[AnimationGroup(GrowArrow(s), FadeIn(r))
                                for s, r in zip(setas2, restos)],
                              lag_ratio=0.12),
                  FadeIn(ret_res), run_time=1.6 * VEL)
        cena.play(LaggedStart(*[GrowArrow(s) for s in setas3], lag_ratio=0.1),
                  run_time=1.2 * VEL)
        cena.play(FadeIn(prod), run_time=0.9 * VEL)
        cena.play(GrowArrow(seta4), TransformFromCopy(eqc[0], saida),
                  run_time=1.1 * VEL)

    cena.esquema = dict(eqc=eqc, bits=bits, caixas=caixas, ret_bit=ret_bit,
                        ret_cx=ret_cx, setas1=setas1, setas2=setas2,
                        restos=restos, ret_res=ret_res, setas3=setas3,
                        prod=prod, seta4=seta4, saida=saida)


def p10_circuito(cena):
    """Slides 151–157 e 165–166: o circuito que calcula 2ᵇ (mod 21) para
    TODOS os b ao mesmo tempo, e a caixa TQF.

    Abre com o `C11N13`, a tradução: o esquema do `p10_esquema` não sai de
    cena por `FadeOut`, ele **vira** o circuito peça por peça — caixa cinza
    vira porta, caixa de bit vira ponto de controle, seta vira ligação, e o
    resultado final vira o que sai na ponta do fio de baixo. A limpeza do
    circuito é do `C11N25` e roda no topo do `p10_ato1`, por dentro da caixa
    da TQF crescendo. Por isso o que fica em cena espera em TRÊS lugares:
    `cena.grupo_circuito` é o que sai, `cena.leva_junto` é o que atravessa a
    expansão de pé — a coluna viva de expoentes, o `⋮`, a pergunta e o
    tamanho do registrador — e `cena.caixa_tqf` é a caixa que vira o quadro
    inteiro, com o rótulo que vai para o canto virar título do trecho."""
    e = cena.esquema
    eqc = e["eqc"]

    # A ordem no eixo x é a ordem em que as coisas acontecem: entradas,
    # portas, painel do registrador e SÓ ENTÃO a TQF — o painel azul é a
    # entrada dela, não a saída, e por isso vem antes no fio.
    ys, yt, x0, x1, xp = YS, YT, X0, X1, XP
    fios = VGroup(*[Line([x0, y, 0], [x1, y, 0], color=PRETO,
                         stroke_width=2) for y in ys + [yt]])
    kets = VGroup(*[T("|0⟩", 22, PRETO).next_to([x0, y, 0], LEFT, buff=0.15)
                    for y in ys])
    keta = T("|1⟩", 22, PRETO).next_to([x0, yt, 0], LEFT, buff=0.15)
    vd = T("⋮", 26, PRETO).move_to([x0 - 0.5, (ys[0] + ys[1]) / 2, 0])

    portas = VGroup(*[_caixa_porta(i).move_to([x, yt, 0])
                      for i, x in zip(EXPOS, XS_CX)])
    pontos = VGroup(*[Dot([x, yc, 0], radius=0.07, color=PRETO)
                      for x, yc in zip(XS_CX, CTRLS)])
    ligas = VGroup(*[Line([x, yc, 0], [x, yt + 0.62, 0], color=PRETO,
                          stroke_width=2)
                     for x, yc in zip(XS_CX, CTRLS)])
    plugues = VGroup(*[VGroup(p, l) for p, l in zip(pontos, ligas)])
    retic = T("…", 28, PRETO).move_to([XRET, yt, 0])

    # a saída c do esquema continua sendo a saída do circuito: ela não sai
    # de cena, atravessa para a ponta do fio de baixo
    saida_circ = e["saida"].copy().scale(46 / 42).move_to([xp, yt, 0])
    saida_circ.set_z_index(1)

    # onde cada caixa de bit vai parar: no cartão do seu fio, à esquerda.
    # NÃO no ponto de controle — os bits do expoente são o que vira qubit,
    # e o ponto preto é só onde o fio toca a porta
    # a ordem é a de CTRLS, não a de `ys`: quem controla a porta 2⁰ é o
    # bit b₀, e essa porta é a primeira da esquerda, controlada pelo fio de
    # BAIXO dos quatro. Ler `ys` aqui punha b₀ em cima e b₈ embaixo
    alvos_bit = [[x0 + 0.75, yc, 0] for yc in CTRLS]

    with narra(cena, "C11N13", 7.8):
        # 1. a metade de baixo do esquema se recolhe PRIMEIRO, para o
        #    circuito não ser desenhado por cima de nada
        cena.play(FadeOut(e["setas2"]), FadeOut(e["restos"]),
                  FadeOut(e["ret_res"]), FadeOut(e["setas3"]),
                  FadeOut(e["prod"]), FadeOut(e["seta4"]),
                  ReplacementTransform(e["saida"], saida_circ),
                  run_time=1.5 * VEL)
        # 2. as caixas cinzas descem para a linha do fio alvo já virando
        #    porta, no espaço que acabou de ficar livre
        cena.play(*[ReplacementTransform(c, p)
                    for c, p in zip(e["caixas"], portas)],
                  ReplacementTransform(e["ret_cx"], retic),
                  run_time=1.6 * VEL)
        # 3. cada caixa de bit atravessa para a esquerda e pousa onde vai
        #    ficar o qubit do seu fio; a seta que ligava bit e caixa estica
        #    e vira a ligação do controle
        cena.play(*[b.animate.move_to(a) for b, a in zip(e["bits"], alvos_bit)],
                  *[ReplacementTransform(s, l)
                    for s, l in zip(e["setas1"], ligas)],
                  FadeOut(e["ret_bit"]), run_time=1.7 * VEL)
        # 4. e só agora, com tudo já no lugar, os fios ligam as peças
        cena.play(LaggedStart(*[Create(f) for f in fios], lag_ratio=0.06),
                  FadeIn(kets), FadeIn(keta), FadeIn(vd), FadeIn(pontos),
                  run_time=1.5 * VEL)

    # o que cada registrador guarda, dito com uma letra só antes de virar
    # superposição: o b azul em cima, o c verde embaixo. Sem esse passo o
    # painel do C11N16 é uma coluna de números sem nome
    carta_b = _carta_super(["0", "1", "2", "3"], AZUL, CIANO)
    carta_b.move_to([xp, (ys[0] + ys[3]) / 2, 0])
    carta_c = _carta_super(["1", "2", "4"], VERDE, VERDE2, passo=0.50, tam=22)
    carta_c.move_to([xp, yt, 0])
    letra_b = T("b", 46, AZUL).move_to(carta_b).set_z_index(1)
    # os fundos entram num `play` e o conteúdo no seguinte, nunca no mesmo:
    # no Manim 0.20.1 um `FadeIn` de retângulo preenchido junto do conteúdo
    # deixa o conteúdo ATRÁS do preenchimento, e a letra some
    with narra(cena, "C11N14", 6.0):
        cena.play(FadeIn(carta_b[0]), FadeIn(carta_c[0]), run_time=1.0 * VEL)
        cena.play(TransformFromCopy(eqc[2][1], letra_b),
                  saida_circ.animate.move_to(carta_c), run_time=1.5 * VEL)

    # cada bit clássico vira o QUBIT do seu fio — a caixa cinza que veio do
    # esquema abre no cartão-gradiente —, e a letra b abre na coluna dos
    # expoentes possíveis: a superposição ganha nome antes de ganhar conteúdo
    inis = VGroup(*[_carta_qubit(0.5, 0.66, 15).move_to([x0 + 0.75, yc, 0])
                    for yc in CTRLS])
    with narra(cena, "C11N15", 3.9):
        cena.play(LaggedStart(*[ReplacementTransform(b, i)
                                for b, i in zip(e["bits"], inis)],
                              lag_ratio=0.15), run_time=1.8 * VEL)

    with narra(cena, "C11N16", 9.6):
        cena.play(ReplacementTransform(letra_b, carta_b[1]),
                  FadeIn(carta_b[2]), run_time=1.6 * VEL)

    with narra(cena, "C11N17", 7.0):
        cena.play(ReplacementTransform(saida_circ, carta_c[1]),
                  FadeIn(carta_c[2]), run_time=1.6 * VEL)

    # medimos o fio alvo: sai UM dos restos possíveis — c = 4 (slide 157)
    med = caixa_cinza(T("M", 20, PRETO), pad=0.14).move_to([3.07, yt, 0])
    with narra(cena, "C11N18", 2.0):
        cena.play(FadeIn(med), run_time=0.6 * VEL)

    # O COLAPSO, e os dois registradores colapsam JUNTOS: o de baixo vira um
    # número só, e o de cima perde os expoentes que não dão aquele número.
    # O de cima NÃO vira um b: continua em superposição, agora só dos b que
    # sobreviveram — é exatamente a frase que o C11N25 vai dizer
    # o resto medido fica EM CAIXA, no lugar exato onde estava o painel: é
    # conteúdo de registrador, como o `c` genérico era, e não um rótulo solto
    # em cima do fio
    lista_b = carta_b[1]
    cartao_c = _carta_valor("4", VERDE, VERDE2).move_to(carta_c)
    bs_de_4 = _troca_coluna(lista_b, ["2", "8", "14", "20"], AZUL)
    with narra(cena, "C11N19", 10.2):
        cena.play(Flash(med.get_center(), color=VERDE, flash_radius=0.5),
                  ReplacementTransform(carta_c, cartao_c),
                  ReplacementTransform(lista_b, bs_de_4),
                  run_time=1.2 * VEL)
    lista_b, cnum = bs_de_4, cartao_c[1]

    # o rodízio: o resto medido podia ter sido qualquer um do ciclo de 2
    # módulo 21 — {1, 2, 4, 8, 16, 11} —, e a cada troca os expoentes que
    # sobram trocam junto. Volta para o 4 no fim porque é com ele que o
    # resto do capítulo trabalha
    rodizio = [("8", ["3", "9", "15", "21"]),
               ("16", ["4", "10", "16", "22"]),
               ("11", ["5", "11", "17", "23"]),
               ("4", ["2", "8", "14", "20"])]
    with narra(cena, "C11N20", 9.2):
        for resto, bs in rodizio:
            novo_c = T(resto, 34, VERDE).move_to(cnum).set_z_index(1)
            novos_b = _troca_coluna(lista_b, bs, AZUL)
            cena.play(ReplacementTransform(cnum, novo_c),
                      ReplacementTransform(lista_b, novos_b),
                      run_time=0.9 * VEL)
            cnum, lista_b = novo_c, novos_b

    # a pergunta sobre a coluna que sobrou, no corpo e na cor exatos do
    # `r` da cascata: é no `C11N39` que ela vira `r = 6`, e o valor só lê
    # como resposta desta pergunta se os dois forem a mesma peça.
    # Espaçamento e valor não entram aqui — o espaçamento é a virada do
    # pente, no `C11N26`/`C11N27`; o valor é a virada da cascata, e só lá
    pergunta_r = formula(("r", AMARELO), ("=", PRETO), ("?", AMARELO),
                         tamanho=30).next_to(carta_b, UP, buff=0.25)
    with narra(cena, "C11N21", 11.3):
        cena.play(Indicate(lista_b, color=AZUL), Write(pergunta_r),
                  run_time=1.4 * VEL)

    # a medida HIPOTÉTICA do C11N22, em cinco batidas na ordem da frase. O
    # bloco inteiro é um parêntese: ao fim dele a cena tem de estar IDÊNTICA
    # a como o C11N21 a deixou, porque é isso que o C11N23 espera encontrar.
    # Por isso cada peça transformada aqui guarda cópia antes, e cada peça
    # escurecida guarda a opacidade que tinha — devolver tudo a 1 acenderia
    # o gradiente das portas (que vive a 0,7) e o do painel do resto (0,3),
    # e entregaria ao C11N23 uma cena diferente da que entrou
    barras = VGroup(*[_barras_peso(n).scale(0.35) for n in lista_b])
    for br, n in zip(barras, lista_b):
        br.next_to(carta_b[0], RIGHT, buff=0.14).align_to(n, DOWN)

    # o M fantasma é peça NOVA. O `med` do C11N18 é o M de verdade, no fio
    # de baixo, e reaproveitá-lo desfaria justamente a distinção que esta
    # batida existe para fazer. Mesmo x e mesmo corpo do `med` — mesma
    # estação de medida, o outro registrador —, mas tracejado e translúcido:
    # esta é uma medida que não acontece
    mf = caixa_cinza(T("M", 20, PRETO), pad=0.14)
    mf[0].set_fill(CAIXA, opacity=0.35)
    mf[1].set_opacity(0.55)
    mf.add(DashedVMobject(mf[0].copy().set_fill(opacity=0)
                          .set_stroke(PRETO, 3, opacity=0.55),
                          num_dashes=24, dashed_ratio=0.6))
    mf.move_to([3.07, (ys[0] + ys[3]) / 2, 0])

    # o que a medida devolveria: um dos quatro expoentes que estavam ali, no
    # corpo do `cnum` — o registrador de cima passaria a guardar um número
    # só, como o de baixo já guarda
    unico = T("8", 34, AZUL).move_to(lista_b).set_z_index(1)
    coluna_volta = lista_b.copy()    # a coluna inteira, para a batida 5
    # a pergunta volta por cópia, e não devolvendo a cor lida de cada token:
    # `get_color()` de um `Text` devolve o preto do invólucro, não a cor com
    # que os glifos foram desenhados, e a volta saía preta
    pergunta_amarela = pergunta_r.copy()
    # "todo o resto da cena" é literalmente isto: o que está em cena menos o
    # painel de cima, a pergunta e as peças da hipótese. A lista é de
    # mobjects que JÁ estão em `cena.mobjects` — animar um VGroup novo por
    # cima deles faria o Manim reempilhar a cena, e os fios passariam a ser
    # desenhados por cima do painel branco
    acesos = (carta_b[0], carta_b[2], lista_b, pergunta_r)
    resto = [m for m in cena.mobjects
             if m.family_members_with_points()
             and not any(m is a for a in acesos)]
    # escurecer e devolver são a MESMA função, peça por peça, a partir da
    # opacidade que cada parte tinha antes do bloco. Não dá para chamar
    # `set_opacity` na peça de cima: `cena.mobjects` guarda também os
    # `Group` que o Manim cria para cada `LaggedStart`, e `Group` não tem
    # `set_opacity` — herda o `set_*` genérico do `Mobject`, que grava um
    # atributo e não pinta nada (era o que deixava os qubits acesos). E
    # multiplicando, não fixando em 0,3: assim o gradiente das portas (0,7)
    # e o do painel do resto (0,3) escurecem na proporção em que vivem, e
    # nenhum preenchimento que era invisível acende
    opacs = [[(s.get_fill_opacity(), s.get_stroke_opacity())
              for s in m.family_members_with_points()] for m in resto]

    def opacidade(m, guardadas, fator=1.0):
        for s, (f, t) in zip(m.family_members_with_points(), guardadas):
            s.set_fill(opacity=f * fator)
            s.set_stroke(opacity=t * fator)
        return m

    with narra(cena, "C11N22", 15.0):
        # 1. as probabilidades: a peça do C11N06 volta em miniatura, uma por
        #    entrada da coluna, nascendo do próprio número
        cena.play(LaggedStart(*[TransformFromCopy(n, br)
                                for n, br in zip(lista_b, barras)],
                              lag_ratio=0.15), run_time=2.0 * VEL)
        # 2. a medida que não acontece entra e, no MESMO play, o resto da
        #    cena cai para 30%: é o escurecimento que marca o trecho como
        #    hipótese, e não como evento
        cena.play(FadeIn(mf),
                  *[ApplyFunction(lambda x, g=g: opacidade(x, g, 0.30), m)
                    for m, g in zip(resto, opacs)],
                  run_time=1.8 * VEL)
        # 3. o colapso hipotético: sobra um valor dos que estavam ali, e com
        #    ele somem os pesos dos outros. O `⋮` sai junto, como saiu no
        #    colapso de verdade do C11N19 — "um valor só" com reticências
        #    embaixo diria o contrário do que a fala está dizendo
        cena.play(Flash(mf.get_center(), color=AZUL, flash_radius=0.5),
                  ReplacementTransform(lista_b, unico),
                  FadeOut(barras), FadeOut(carta_b[2]),
                  run_time=1.2 * VEL)
        # 4. o pagamento: com um expoente sozinho a pergunta do C11N21 perde
        #    a resposta possível, e ela vira a cor de "isto não funciona"
        cena.play(pergunta_r.animate.set_color(VERMELHO), run_time=0.8 * VEL)
        # 5. e tudo desfaz. O desfazer É o argumento, não um detalhe: a
        #    medida NÃO aconteceu, e a cena volta ao quadro do C11N21
        cena.play(*[ApplyFunction(lambda x, g=g: opacidade(x, g), m)
                    for m, g in zip(resto, opacs)],
                  ReplacementTransform(unico, coluna_volta),
                  FadeIn(carta_b[2]), FadeOut(mf),
                  ReplacementTransform(pergunta_r, pergunta_amarela),
                  run_time=1.6 * VEL)
    lista_b, pergunta_r = coluna_volta, pergunta_amarela

    # nos fios de cima entra a TRANSFORMADA QUÂNTICA DE FOURIER (slide 165),
    # DEPOIS do painel azul: é ele que a alimenta
    tqf = RoundedRectangle(corner_radius=0.12, width=1.35,
                           height=ys[0] - ys[3] + 0.9, stroke_width=0)
    tqf.set_fill(CAIXA2, opacity=1).move_to([XTQF, (ys[0] + ys[3]) / 2, 0])
    rot_tqf = T("TQF", 30, PRETO).move_to(tqf)
    nq = formula(("N", PRETO), ("=", PRETO), ("2⁹", PRETO), ("=", PRETO),
                 ("512", PRETO), tamanho=24,
                 buff=0.08).next_to(tqf, UP, buff=0.2)
    with narra(cena, "C11N23", 10.9):
        # "nos fios de cima": eles estão em cena desde o C11N13 e a fala os
        # nomeia ANTES de nomear a TQF — o azul é o do b que eles carregam.
        # scale_factor=1.0 porque um fio esticado a 1,2 sai do quadro
        cena.play(Indicate(VGroup(*fios[:4]), color=AZUL, scale_factor=1.0),
                  run_time=0.6 * VEL)
        cena.play(FadeIn(tqf), Write(rot_tqf), run_time=1.0 * VEL)
    with narra(cena, "C11N24", 6.7):
        cena.play(FadeIn(nq), run_time=0.7 * VEL)

    # o painel de b entra na saída DESMONTADO — fundo, ⋮ e a coluna viva de
    # números —, e não como `carta_b`: a coluna original foi consumida pelo
    # ReplacementTransform do colapso, e um FadeOut(carta_b) traria a coluna
    # morta de volta piscando. O painel de restos não entra: ele virou `cnum`
    #
    # e a saída se divide em três, porque o C11N25 faz três coisas ao mesmo
    # tempo. SAI o circuito inteiro; ATRAVESSA a expansão o que a fala diz
    # que levamos junto — a coluna que sobrou do colapso, o `⋮` que ainda
    # promete continuação (ele vira o quinto dente no C11N26), a pergunta
    # sem resposta e o `N = 2⁹`, que o C11N28 vai cobrar; e CRESCE a caixa
    # da TQF, que não está em nenhum dos dois grupos porque ela não some
    # nem viaja. `lista_b` e `pergunta_r` são as cópias que o desfazer do
    # C11N22 deixou em cena, nunca as peças originais
    cena.grupo_circuito = VGroup(eqc, fios, kets, keta, vd, inis, portas,
                                 plugues, retic, med, carta_b[0],
                                 cartao_c[0], cnum)
    # e o que VOLTA no C11N35, quando a câmera sai da transformada: o mesmo
    # circuito menos o painel de entrada. A coluna dele foi consumida pelo
    # C11N26 — virou o pente —, e o fundo sozinho leria como um registrador
    # vazio; o lugar dele no fio é justamente o que a TQF ocupa na volta,
    # para o registrador de SAÍDA caber depois dela
    cena.volta_circuito = VGroup(eqc, fios, kets, keta, vd, inis, portas,
                                 plugues, retic, med, cartao_c[0], cnum)
    cena.leva_junto = VGroup(lista_b, carta_b[2], pergunta_r, nq)
    cena.caixa_tqf = VGroup(tqf, rot_tqf)


def p10_ato1(cena):
    """Slides 158–164: o pente — os b que dão o mesmo resto aparecem de r
    em r na reta, e o espaçamento é a ordem.

    Abre com o `C11N25`, a entrada na transformada: a caixa da TQF cresce
    até ser o quadro inteiro — a câmera entra nela —, o circuito sai por
    dentro dessa expansão e a coluna de expoentes que sobreviveram ao
    colapso a atravessa de pé. O rótulo da caixa não cresce junto: pousa no
    canto e fica de título, porque daqui até o `C11N29` tudo acontece
    dentro da transformada. Daí nada aqui nasce do vazio: os dentes do
    pente são os números dessa coluna, o quinto é o `⋮` dela e o `r` que
    rotula as chaves nasce do `r = ?` do `C11N21` — que sai daqui ainda
    sem resposta, porque nada do que acontece dentro da caixa é observável.
    O valor só é conhecido na cascata, no `C11N39`."""
    lista_b, tres_b, pergunta_r, nq = cena.leva_junto
    tqf, rot_tqf = cena.caixa_tqf

    # a caixa é preenchida e opaca: crescendo, ela passa por cima de tudo
    # que não estiver acima dela em z. A coluna e o `⋮` já sobem desde o
    # `_carta_super`; a pergunta, o `N` e o rótulo da caixa não subiam
    # porque até aqui nada passava por baixo deles — e os três têm de ficar
    # legíveis por cima do cinza, que é justamente o que diz que agora
    # estamos DENTRO da transformada
    pergunta_r.set_z_index(1)
    nq.set_z_index(1)
    rot_tqf.set_z_index(1)

    # o quadro inteiro, com folga para as bordas e os cantos arredondados
    # ficarem fora. A caixa NÃO cresce proporcional: ela é alta e estreita,
    # e crescer assim dava uma faixa vertical atravessando o quadro. Ela
    # vira A TELA, que é o que "entrar na transformada" quer dizer
    alvo_tqf = RoundedRectangle(corner_radius=0.12,
                                width=config.frame_width + 1.0,
                                height=config.frame_height + 1.0,
                                stroke_width=0)
    alvo_tqf.set_fill(CAIXA2, opacity=1).move_to(ORIGIN)

    # onde a coluna pousa: no meio do quadro, alta o bastante para a reta
    # do C11N26 nascer debaixo dela. A pergunta vai junto no mesmo
    # deslocamento — ela está acima da coluna desde o C11N21, e é assim,
    # de pé, que as duas atravessam. O VGroup aqui é só para MEDIR: animar
    # um grupo novo por cima de mobjects que já estão em cena reempilharia
    # a cena, que é o problema anotado no C11N22
    desloc = np.array([0.0, 1.35, 0.0]) - VGroup(lista_b, tres_b).get_center()
    with narra(cena, "C11N25", 13.0):
        # sem `run_time` no `play`: aqui cada peça tem o seu, porque o
        # circuito precisa ter sumido ANTES de o cinza fechar — senão ele
        # reaparece de relance quando o cinza abre
        cena.play(
            # a câmera entrando na caixa, em duas etapas emendadas: ela
            # acelera até ser o quadro inteiro e só então abre, deixando
            # dentro o que viemos trazendo. O FadeOut é do cinza que já
            # cobriu a tela, não da caixa em cima do fio — a caixa não
            # some, ela vira o lugar onde o resto do ato acontece
            Succession(Transform(tqf, alvo_tqf, rate_func=rush_into,
                                 run_time=1.8 * VEL),
                       FadeOut(tqf, run_time=0.8 * VEL)),
            FadeOut(cena.grupo_circuito, run_time=1.5 * VEL),
            # o rótulo não cresce junto: ele vai para o canto e FICA, de
            # título do trecho — daqui até o C11N29 tudo o que acontece
            # acontece dentro da transformada, e é ele que diz isso
            rot_tqf.animate(run_time=2.6 * VEL).to_corner(UL, buff=0.4),
            *[m.animate(run_time=2.6 * VEL).shift(desloc)
              for m in (lista_b, tres_b, pergunta_r)],
            # o tamanho do registrador encolhe para o canto oposto e
            # espera: é ele que o C11N28 acende quando a reta chega a 512
            nq.animate(run_time=2.6 * VEL).scale(0.8).to_corner(UR, buff=0.4))

    retaZ = NumberLine(x_range=[0, 32, 4], length=12, color=CINZA,
                       stroke_width=2, include_ticks=True, tick_size=0.06)
    retaZ.shift(0.55 * DOWN)
    rotZ = VGroup(*[T(str(v), 18, CINZA).next_to(retaZ.n2p(v), DOWN, buff=0.24)
                    for v in (0, 8, 16, 24, 32)])

    def dente(reta, b, altura=0.5):
        # AZUL, e não verde: cada dente é um b. Verde é o resto, e um pente
        # verde diz que aquilo ali é uma fila de c — que é o contrário
        return Line(reta.n2p(b) + altura * UP, reta.n2p(b),
                    color=AZUL, stroke_width=3.5)

    bs_zoom = [2, 8, 14, 20, 26]
    dentesZ = VGroup(*[dente(retaZ, b) for b in bs_zoom])
    rotulos_b = VGroup(*[T(str(b), 22, AZUL).next_to(d, UP, buff=0.12)
                         for b, d in zip(bs_zoom, dentesZ)])
    with narra(cena, "C11N26", 9.6):
        # a reta nasce DEBAIXO da coluna, que está em cena desde o C11N25
        cena.play(Create(retaZ), FadeIn(rotZ), run_time=1.0 * VEL)
        # e o pente nasce da coluna: cada número do painel viaja até a sua
        # posição na reta e VIRA o rótulo de lá, com o dente crescendo por
        # baixo dele no mesmo play. O quinto, o 26, nasce do `⋮` — o "e
        # assim por diante" do painel vira o primeiro dente que ninguém
        # tinha escrito, e é ele que autoriza o C11N28 a estender o pente.
        # Nenhum FadeIn: o "eles" da fala é a própria coluna se
        # transformando, que é o antecedente mais forte que a tela dá
        for n, d, rb in zip([*lista_b, tres_b], dentesZ, rotulos_b):
            cena.play(ReplacementTransform(n, rb), GrowFromEdge(d, DOWN),
                      run_time=0.4 * VEL)

    chaves = VGroup()
    for b1, b2 in zip(bs_zoom[:-1], bs_zoom[1:]):
        ch = BraceBetweenPoints(retaZ.n2p(b1) + 1.0 * UP,
                                retaZ.n2p(b2) + 1.0 * UP,
                                direction=UP, color=LARANJA).scale(0.8)
        # o rótulo da chave é o `r`, não o valor dele: a distância tem
        # NOME e não tem número
        chaves.add(VGroup(ch, T("r", 20, AMARELO).next_to(ch, UP, buff=0.07)))
    with narra(cena, "C11N27", 4.6):
        # cada `r` de chave nasce do `r` do `pergunta_r`, que fica em cena
        # exatamente como está. Esta linha diz ONDE a ordem está escrita —
        # no espaçamento —, nunca quanto ela vale: o pente é o estado
        # DENTRO da transformada, e ninguém o observa. Escrever `r = 6`
        # aqui ensinaria que a transformada entrega a ordem, e o resto do
        # capítulo viraria enfeite; o valor só aparece no C11N39, depois
        # da medida e das frações contínuas
        nasce_r = [AnimationGroup(FadeIn(c[0]),
                                  TransformFromCopy(pergunta_r[0], c[1]))
                   for c in chaves]
        cena.play(LaggedStart(*nasce_r, lag_ratio=0.25), run_time=1.6 * VEL)

    # zoom-out: rótulos saem ANTES da compressão (sem sobreposição)
    retaF = NumberLine(x_range=[0, N, 64], length=12, color=CINZA,
                       stroke_width=2, include_ticks=True, tick_size=0.06)
    retaF.shift(0.55 * DOWN)
    rotF = VGroup(*[T(str(v), 18, CINZA).next_to(retaF.n2p(v), DOWN, buff=0.24)
                    for v in (0, 128, 256, 384, 512)])
    dentesF = VGroup(*[dente(retaF, b, 0.45) for b in bs_zoom])
    resto = VGroup(*[dente(retaF, b, 0.45) for b in PENTE[5:]])
    with narra(cena, "C11N28", 6.8):
        cena.play(FadeOut(rotulos_b), FadeOut(chaves), FadeOut(rotZ),
                  run_time=0.5 * VEL)
        cena.play(ReplacementTransform(retaZ, retaF),
                  *[ReplacementTransform(z, f)
                    for z, f in zip(dentesZ, dentesF)],
                  FadeIn(rotF), run_time=1.7 * VEL)
        # "o fim do registrador" é o `N = 2⁹ = 512` que espera no canto
        # desde o C11N25: sem este destaque o número fica em cena sem
        # nunca ser cobrado
        cena.play(LaggedStart(*[GrowFromEdge(d, DOWN) for d in resto],
                              lag_ratio=0.01), Indicate(nq),
                  run_time=2.2 * VEL)

    cena.pente_grupo = VGroup(retaF, dentesF, resto)
    # o que sai junto quando o pente sobe, no topo do `C11N29`: os rótulos
    # da reta longa, o tamanho do registrador e o título da caixa — acabou
    # o que só valia dentro da transformada. O `pergunta_r` NÃO está aqui:
    # ele encolhe para a borda e atravessa o resto do capítulo sem resposta
    cena.sai_com_o_pente = VGroup(rotF, nq, rot_tqf)
    cena.pergunta_r = pergunta_r


def p10_ondas(cena):
    """O instrumento das ondas (`C11N29`–`C11N34`), na estrutura do
    `qft_shor_ondas_N512.html`: à direita uma cossenoide por expoente,
    nascida do dente dele; à esquerda o círculo em que cada onda vira uma
    seta e as setas se emendam até a seta grossa da soma; embaixo das
    ondas o traço da soma, que se desenha conforme o cursor anda.

    As três peças são uma peça só: tudo o que se mexe está preso ao mesmo
    `k_tr`, e é isso que deixa ver que o encontro dos pontos nas ondas, o
    alinhamento das setas e o pico do traço são o MESMO fato. Antes eram
    três trechos seguidos — as ondas, a roleta e a curva —, que explicavam
    a interferência duas vezes e desenhavam a mesma curva em dois lugares.

    Uma diferença deliberada em relação ao HTML: lá o traço de baixo é a
    parte real da soma, com picos de alturas e sinais diferentes, que
    confundem; aqui ele é o TAMANHO da seta grossa — a `amplitude` —, que
    é o que a transformada de fato entrega e o que a curva antiga já
    desenhava.

    O bloco não limpa nada: quem tira o instrumento é o `C11N35`, por
    baixo do cinza da TQF — saem lá o pente, o traço com a base e o rótulo,
    e as linhas das marcas. O que fica em cena espera em
    `cena.grafico_soma`, `cena.marcas` e `cena.rots_marca` — e são os seis
    rótulos das marcas que o `C11N35` transforma na coluna de saída da
    transformada."""
    # --- o painel das ondas, à direita: o eixo k vai de 0 a N na largura
    BS = [2, 8, 14, 20]                       # os quatro primeiros dentes
    YS = [2.70, 2.05, 1.40, 0.75]             # uma linha por expoente
    AMP = 0.24
    OX0, OX1 = -0.60, 5.35                    # o eixo k das ondas E do traço
    SY, SALT = -2.10, 1.20                    # base e altura do traço da soma
    # --- o círculo dos fasores, à esquerda ---
    RAIO = 1.35
    CENTRO = np.array([-4.60, 0.35, 0.0])
    PASSO = RAIO / M                # 85 setas emendadas chegam ao raio
    DESL = [0.42, 0.14, -0.14, -0.42]
    # --- a faixa larga em que o traço da soma termina, no C11N34 ---
    GX0, GX1 = -6.20, 6.20
    GY, GALT = -3.25, 2.15

    with narra(cena, "C11N29", 10.7):
        # o pente sobe para o alto e fica lá o capítulo inteiro, como
        # referência de tudo que vem depois; com ele sai o cenário de
        # dentro da caixa. E o `r = ?` encolhe para a borda direita e
        # FICA: a pergunta atravessa o instrumento inteiro sem resposta,
        # porque nada do que acontece ali é observável. Nada do que é
        # construído daqui em diante pode pousar por cima dele
        cena.play(FadeOut(cena.sai_com_o_pente),
                  cena.pente_grupo.animate.scale(0.85).to_edge(UP, buff=0.35),
                  cena.pergunta_r.animate.scale(0.8).move_to([6.15, 2.05, 0]),
                  run_time=1.3 * VEL)

        # cos(2π·b·k/N) com k de 0 a N na largura do painel: a onda de
        # b = 2 faz duas oscilações e a de b = 20 faz vinte. É aí que
        # "cada expoente dá uma frequência diferente" se vê
        ondas, rots_onda = VGroup(), VGroup()
        for b, y in zip(BS, YS):
            ondas.add(FunctionGraph(
                lambda x, b=b, y=y: y + AMP * np.cos(
                    TAU * b * (x - OX0) / (OX1 - OX0)),
                x_range=[OX0, OX1, 0.01], color=AZUL, stroke_width=2.0))
            rots_onda.add(
                formula(("b", AZUL), ("=", PRETO), (str(b), AZUL),
                        tamanho=17, buff=0.05).move_to([OX0 - 0.15, y, 0],
                                                       aligned_edge=RIGHT))
        # cada onda NASCE do dente dela: os quatro primeiros dentes do
        # pente são exatamente esses quatro b, e é por isso que eles são
        # procurados pela posição no grupo, não desenhados de novo
        dentes_b = cena.pente_grupo[1][:4]
        cena.play(LaggedStart(*[AnimationGroup(TransformFromCopy(d, o),
                                               FadeIn(r))
                                for d, o, r in zip(dentes_b, ondas, rots_onda)],
                              lag_ratio=0.5), run_time=3.4 * VEL)
        # o pente tem 85 dentes: as outras 81 ondas não cabem no quadro, e
        # dizer quantas são é o que mantém a soma honesta
        resto_ondas = VGroup(T("⋮", 26, CINZA),
                             T("+ 81 ondas", 17, CINZA)).arrange(DOWN,
                                                                 buff=0.12)
        resto_ondas.move_to([OX0 - 0.55, 0.10, 0])
        cena.play(FadeIn(resto_ondas), run_time=0.6 * VEL)

    # ----------------------------------------------------------------
    # tudo o que se mexe é função de um k só
    # ----------------------------------------------------------------
    k_tr = ValueTracker(0.0)

    def _x_k(k):
        return OX0 + (OX1 - OX0) * k / N

    def _y_onda(b, y0, k):
        return y0 + AMP * np.cos(TAU * b * k / N)

    def _cursor(k):
        x = _x_k(k)
        return DashedLine([x, YS[0] + 0.45, 0], [x, SY - 0.12, 0],
                          color=LARANJA, stroke_width=1.8, dash_length=0.10)

    def _pontos(k):
        return VGroup(*[Dot([_x_k(k), _y_onda(b, y, k), 0], radius=0.055,
                            color=LARANJA) for b, y in zip(BS, YS)])

    def _dirs(k):
        th = TAU * np.array(PENTE, dtype=float) * k / N
        return np.cos(th), np.sin(th)

    def _raios(cs, sn, w, op):
        """Os raios num VMobject só, um subcaminho por raio: oitenta e uma
        `Line` por quadro dentro de um `always_redraw` derrubam o render,
        e um traço com oitenta e um subcaminhos desenha o mesmo."""
        n = len(cs)
        fim = CENTRO + RAIO * np.stack([cs, sn, np.zeros(n)], axis=1)
        pts = np.empty((4 * n, 3))
        pts[0::4] = CENTRO
        pts[1::4] = CENTRO + (fim - CENTRO) / 3
        pts[2::4] = CENTRO + 2 * (fim - CENTRO) / 3
        pts[3::4] = fim
        m = VMobject(stroke_color=AZUL, stroke_width=w, stroke_opacity=op)
        m.set_points(pts)
        return m

    def _fracos(k):
        cs, sn = _dirs(k)
        return _raios(cs[4:], sn[4:], 1.4, 0.30)

    def _fortes(k):
        cs, sn = _dirs(k)
        return VGroup(*[Line(CENTRO, CENTRO + RAIO * np.array([c, s, 0.0]),
                             color=AZUL, stroke_width=3.0)
                        for c, s in zip(cs[:4], sn[:4])])

    def _poe_rotulo(m, b, desl):
        # na ponta do raio, afastado de lado: em k = 0 os quatro raios
        # apontam para o mesmo lugar, e em k = 85 quase — sem o
        # afastamento os quatro números caem uns sobre os outros
        th = TAU * b * k_tr.get_value() / N
        u = np.array([np.cos(th), np.sin(th), 0.0])
        t = np.array([-np.sin(th), np.cos(th), 0.0])
        m.move_to(CENTRO + 1.16 * RAIO * u + desl * t)

    def _corrente(k):
        cs, sn = _dirs(k)
        pts = np.empty((M + 1, 3))
        pts[0] = CENTRO
        pts[1:, 0] = CENTRO[0] + PASSO * np.cumsum(cs)
        pts[1:, 1] = CENTRO[1] + PASSO * np.cumsum(sn)
        pts[1:, 2] = 0.0
        cadeia = VMobject(stroke_color=AZUL, stroke_width=2.2,
                          stroke_opacity=0.85)
        cadeia.set_points_as_corners(pts)
        cor = CIANO if amplitude(k) > 0.6 else LARANJA
        return VGroup(cadeia, Line(CENTRO, pts[-1], color=cor,
                                   stroke_width=6),
                      Dot(pts[-1], radius=0.06, color=cor))

    # o traço da soma é o TAMANHO da seta grossa, amostrado de terço em
    # terço de k para os picos (largura ~6 em k) não escaparem entre duas
    # amostras. Tabela pronta: por quadro só se corta o prefixo
    KS = np.arange(0.0, N + 1e-9, 1.0 / 3.0)
    PTS_SOMA = np.stack([_x_k(KS),
                         SY + SALT * np.array([amplitude(k) for k in KS]),
                         np.zeros(len(KS))], axis=1)

    def _traco(k):
        i = min(max(int(k * 3.0) + 1, 2), len(PTS_SOMA))
        m = VMobject(stroke_color=CIANO, stroke_width=2.6)
        m.set_points_as_corners(PTS_SOMA[:i])
        return m

    def _ponta(k):
        return Dot([_x_k(k), SY + SALT * amplitude(k), 0], radius=0.055,
                   color=CIANO)

    base_soma = Line([OX0, SY, 0], [OX1, SY, 0], color=CINZA,
                     stroke_width=1.5)
    rot_soma = T("soma", 17, CINZA).move_to([OX0 + 0.35, SY - 0.28, 0])

    with narra(cena, "C11N30", 9.8):
        # (1) o cursor, com um ponto em cada onda: "em cada ponto"
        cursor_e, pontos_e = _cursor(0), _pontos(0)
        cena.play(Create(cursor_e),
                  LaggedStart(*[FadeIn(p, scale=0.4) for p in pontos_e],
                              lag_ratio=0.12), run_time=1.0 * VEL)
        # (2) o círculo: "cada onda vira uma seta". Os quatro raios fortes
        # NASCEM dos quatro pontos do cursor — regra 4 —, e os outros 81
        # entram por FadeIn, que é o que sobra quando a peça é a multidão
        guia = Circle(radius=RAIO, color=CINZA, stroke_width=1.2)
        guia.move_to(CENTRO).set_stroke(opacity=0.5)
        fracos_e, fortes_e = _fracos(0), _fortes(0)
        rots_raio = VGroup(*[T(str(b), 17, AZUL) for b in BS])
        for m, b, d in zip(rots_raio, BS, DESL):
            _poe_rotulo(m, b, d)
        cena.play(Create(guia), FadeIn(fracos_e), FadeIn(rots_raio),
                  *[TransformFromCopy(p, r)
                    for p, r in zip(pontos_e, fortes_e)],
                  run_time=1.8 * VEL)
        # (3) "emendadas uma na outra": a corrente ponta com cauda e, do
        # centro até o fim dela, a seta grossa — a soma
        corrente_e = _corrente(0)
        cena.play(FadeIn(corrente_e), run_time=1.0 * VEL)
        # (4) o traço da soma, embaixo das ondas. Em k = 0 ele é só o
        # ponto no alto: as setas saem todas para o mesmo lado, e a soma
        # vale o máximo que pode valer
        traco_e, ponta_e = _traco(0), _ponta(0)
        cena.play(Create(base_soma), FadeIn(rot_soma), FadeIn(traco_e),
                  FadeIn(ponta_e), run_time=0.9 * VEL)
        # e as peças estáticas dão lugar às vivas: em k = 0 o desenho é o
        # mesmo, então a troca é invisível e não pede play — o mesmo
        # truque que a curva antiga usava para virar `always_redraw`
        cursor = always_redraw(lambda: _cursor(k_tr.get_value()))
        pontos = always_redraw(lambda: _pontos(k_tr.get_value()))
        fracos = always_redraw(lambda: _fracos(k_tr.get_value()))
        fortes = always_redraw(lambda: _fortes(k_tr.get_value()))
        corrente = always_redraw(lambda: _corrente(k_tr.get_value()))
        traco = always_redraw(lambda: _traco(k_tr.get_value()))
        ponta = always_redraw(lambda: _ponta(k_tr.get_value()))
        cena.add(cursor, pontos, fracos, fortes, corrente, traco, ponta)
        # os pontos e os raios fortes entraram um a um (o LaggedStart e os
        # TransformFromCopy), então quem está na cena são as peças soltas
        # e não os VGroups: tirar só o grupo deixaria as quatro estáticas
        # de k = 0 em cena o trecho inteiro
        cena.remove(cursor_e, pontos_e, *pontos_e, fracos_e,
                    fortes_e, *fortes_e, corrente_e, traco_e, ponta_e)
        for m, b, d in zip(rots_raio, BS, DESL):
            m.add_updater(lambda mo, b=b, d=d: _poe_rotulo(mo, b, d))

    with narra(cena, "C11N31", 6.8):
        # tudo anda junto porque tudo pende do mesmo k: os pontos se
        # desencontram nas ondas, os raios giram cada um no seu ritmo, a
        # corrente se enrola, a seta grossa encolhe quase a nada e o traço
        # da soma cai do alto e fica rente à base
        cena.play(k_tr.animate.set_value(70), run_time=4.0 * VEL,
                  rate_func=linear)

    with narra(cena, "C11N32", 6.3):
        # a desaceleração é o que faz o alinhamento ser lido como chegada
        cena.play(k_tr.animate.set_value(85), run_time=3.0 * VEL,
                  rate_func=rate_functions.ease_out_sine)
        # em k = 85 os quatro pontos estão na mesma altura DENTRO DA ONDA
        # de cada um (todos perto de −0,47, e não no alto), e isso não é
        # óbvio sem ajuda. São quatro traços e não um: as ondas estão
        # empilhadas, e uma horizontal só não passa pelos quatro pontos
        mesma = VGroup(*[DashedLine([_x_k(85) - 0.80, _y_onda(b, y, 85), 0],
                                    [_x_k(85) + 0.80, _y_onda(b, y, 85), 0],
                                    color=LARANJA, stroke_width=1.6,
                                    dash_length=0.07)
                         for b, y in zip(BS, YS)])
        # lag_ratio=0: os quatro traços entram JUNTOS, que é o que a
        # frase diz. Com o lag padrão do Create eles nascem um a um e o
        # quarto mal chega a existir antes de a saída começar
        cena.play(Create(mesma, lag_ratio=0),
                  Flash(corrente[2].get_center(), color=CIANO,
                        flash_radius=0.45), run_time=1.0 * VEL)
        cena.play(FadeOut(mesma), run_time=1.5 * VEL)

    with narra(cena, "C11N33", 7.4):
        # a ÚNICA linha da série em que a animação estoura a locução de
        # propósito: dez segundos de varredura contra sete e meio de fala.
        # O excedente é o efeito — o traço termina de se desenhar, com os
        # picos surgindo um a um, enquanto a locução seguinte já entra
        cena.play(k_tr.animate.set_value(N - 1), run_time=10.0 * VEL,
                  rate_func=linear)

    # os updaters param ANTES da saída: o que cresce na parte de baixo é o
    # traço congelado, o mesmo objeto, e não uma curva nova
    for m in (cursor, pontos, fracos, fortes, corrente, traco, ponta,
              *rots_raio):
        m.clear_updaters()

    # a mesma transformação afim para as duas peças do gráfico, aplicada
    # uma a uma: um VGroup novo por cima de mobjects que já estão em cena
    # reempilharia a cena, que é o problema anotado no C11N22
    ESC_X, ESC_Y = (GX1 - GX0) / (OX1 - OX0), GALT / SALT
    ANCORA = np.array([OX0, SY, 0.0])

    def _cresce(m):
        return (m.animate.stretch(ESC_X, 0, about_point=ANCORA)
                .stretch(ESC_Y, 1, about_point=ANCORA)
                .shift([GX0 - OX0, GY - SY, 0]))

    def _x_grande(k):
        return GX0 + (GX1 - GX0) * k / N

    # as linhas e os rótulos em grupos separados: o C11N35 leva os seis
    # rótulos para dentro do painel de saída e apaga as linhas por baixo do
    # cinza, e um FadeOut que pegasse os dois traria os rótulos de volta
    # piscando
    marcas, rots_marca = VGroup(), VGroup()
    for mlt in range(6):
        x = _x_grande(mlt * N / R)
        marcas.add(DashedLine([x, GY, 0], [x, GY + 1.05 * GALT, 0],
                              color=LARANJA, stroke_width=1.5,
                              dash_length=0.08))
        # o rótulo vai EMBAIXO da base, e não no alto do traço: no alto
        # ele disputaria o lugar com o pico, e é dele que a coluna de
        # saída do C11N35 nasce. z_index alto porque é por cima do fundo
        # do painel que ele vai pousar
        # a marca do zero é obrigatória: o traço tem um pico em k = 0 tão
        # alto quanto o de 256 e mais alto que o de 85, o espectador acabou
        # de vê-lo se desenhar, e sem ela ele sumiria na passagem do C11N35.
        # O rótulo dela é `0`, e não `0·N/r`, porque é o inteiro que a
        # coluna de saída vai guardar — e porque zero múltiplos não se lê
        rots_marca.add(T("0" if mlt == 0 else f"{mlt}·N/r", 16, LARANJA)
                       .next_to([x, GY, 0], DOWN, buff=0.14).set_z_index(1))

    with narra(cena, "C11N34", 8.9):
        cena.play(FadeOut(VGroup(guia, fracos, fortes, rots_raio, corrente,
                                 cursor, pontos, ponta, ondas, rots_onda,
                                 resto_ondas)),
                  _cresce(traco), _cresce(base_soma),
                  # afastado da ponta esquerda da base: é ali que pousa o
                  # rótulo `0` da primeira marca, e os dois ficam na mesma
                  # altura. Quem cede é o rótulo da soma, não o `0`, que é
                  # de onde a coluna de saída nasce
                  rot_soma.animate.move_to([GX0 + 0.85, GY - 0.30, 0]),
                  run_time=1.8 * VEL)
        cena.play(LaggedStart(*[AnimationGroup(Create(l), FadeIn(r))
                                for l, r in zip(marcas, rots_marca)],
                              lag_ratio=0.15), run_time=2.2 * VEL)

    cena.grafico_soma = VGroup(traco, base_soma, rot_soma)
    # onde a cascata pega o gráfico: as linhas saem no C11N35, por baixo do
    # cinza, e os seis rótulos viram lá a coluna de saída
    cena.marcas, cena.rots_marca = marcas, rots_marca


def p10_ato4(cena):
    """A câmera sai da transformada, a saída dela vira registrador no
    circuito, a medida cai num pico e a aritmética devolve a ordem.

    O `C11N35` é o `C11N25` ao contrário, e com a MESMA peça: o cinza da
    TQF fecha sobre o instrumento, encolhe até ser de novo a caixa no fio
    e o circuito aparece em volta dela. Só que a caixa volta mais para a
    esquerda, no lugar que era do painel de entrada — aquele painel foi
    consumido pelo `C11N26`, e é depois da TQF que o registrador de saída
    precisa caber. Os seis rótulos das marcas atravessam o cinza (estão
    por cima dele em z) e viram a coluna desse registrador: o que a
    transformada entrega é o que os picos marcaram.

    A medida é a do `C11N18`/`C11N19` outra vez, agora no registrador de
    cima e no lugar que o `M` fantasma do `C11N22` ensaiou: o fundo do
    painel FICA e a coluna vira um número só."""
    # a volta da caixa: mesmo corpo do `tqf` do C11N23, recuado no fio
    XTQF2, XSAI, XMED = 3.25, 5.00, 6.25
    YREG = (YS[0] + YS[3]) / 2
    tqf, rot_tqf = cena.caixa_tqf
    caixa_volta = RoundedRectangle(corner_radius=0.12, width=1.35,
                                   height=YS[0] - YS[3] + 0.9, stroke_width=0)
    caixa_volta.set_fill(CAIXA2, opacity=1).move_to([XTQF2, YREG, 0])
    rot_tqf.move_to(caixa_volta)

    # o registrador de saída, no vocabulário dos outros dois: LARANJA
    # porque é a leitura de k, degradê fraco como nos painéis do circuito,
    # e alto o bastante para cobrir os quatro fios de cima
    # o `passo` é menor que o dos outros painéis porque são SEIS entradas:
    # com o passo de cinco a coluna crescia para fora dos quatro fios e
    # encostava no `pergunta_r`. Quem encolhe é o passo, nunca a lista
    saida = _carta_super(["0", "1·N/r", "2·N/r", "3·N/r", "4·N/r", "5·N/r"],
                         LARANJA, AMARELO, passo=0.38, larg=1.40, tam=20)
    # sem o `⋮` do `_carta_super`: aqui a lista é COMPLETA — são esses os
    # seis picos e mais nenhum, o `0` entre eles —, e a coluna recentra no
    # fundo para não ficar com o buraco que era dele
    saida.remove(saida[2])
    saida[1].move_to(saida[0])
    saida.move_to([XSAI, YREG, 0])
    fundo_k, coluna_k = saida[0], saida[1]

    with narra(cena, "C11N35", 9.0):
        cena.play(
            # o cinza fecha sobre o instrumento e encolhe de volta ao fio:
            # `rush_from` é o `rush_into` do C11N25 lido ao contrário
            Succession(FadeIn(tqf, run_time=0.5 * VEL),
                       Transform(tqf, caixa_volta, rate_func=rush_from,
                                 run_time=1.5 * VEL)),
            # o que era de dentro da transformada sai por baixo do cinza
            FadeOut(VGroup(cena.pente_grupo, cena.grafico_soma, cena.marcas),
                    run_time=0.5 * VEL),
            # e o circuito volta enquanto a caixa encolhe — por baixo dela
            Succession(Wait(0.7 * VEL),
                       FadeIn(cena.volta_circuito, run_time=1.3 * VEL)),
            Succession(Wait(1.5 * VEL),
                       FadeIn(rot_tqf, run_time=0.5 * VEL)),
            # fundo e conteúdo nunca no mesmo play (a nota do C11N14): o
            # fundo do registrador de saída entra junto com o circuito
            Succession(Wait(1.2 * VEL),
                       FadeIn(fundo_k, run_time=0.8 * VEL)),
            # a pergunta volta para cima do registrador que a responde,
            # como ficava em cima do painel de entrada no circuito
            cena.pergunta_r.animate(run_time=1.6 * VEL).move_to([XSAI, 2.55, 0]))
        # os seis rótulos atravessaram o cinza porque estão por cima dele
        # em z, e agora VIRAM as entradas do registrador: o que a
        # transformada entrega é exatamente o que os picos marcaram
        cena.play(*[ReplacementTransform(r, n)
                    for r, n in zip(cena.rots_marca, coluna_k)],
                  run_time=1.2 * VEL)
        # agora em número inteiro: é o que a medida devolve e é o que a
        # aritmética do fim usa. Enquanto a tela disser `N/r`, o `85` da
        # cascata não tem de onde vir
        inteiros = _troca_coluna(coluna_k,
                                 ["0", "85", "171", "256", "341", "427"],
                                 LARANJA, tam=20)
        cena.play(ReplacementTransform(coluna_k, inteiros),
                  run_time=0.9 * VEL)
    coluna_k = inteiros

    # a estação de medida do registrador de cima: no fio e DEPOIS do
    # registrador de saída. O `mf` do C11N22 mediu aqui de mentira, no
    # mesmo corpo e na mesma linha; este é o M de verdade
    med_k = caixa_cinza(T("M", 20, PRETO), pad=0.14).move_to([XMED, YREG, 0])
    # e o colapso é o do C11N19: o fundo do painel FICA — o registrador
    # continua sendo os quatro fios — e a coluna vira um número só
    unico_k = T("85", 34, LARANJA).move_to(fundo_k).set_z_index(1)
    with narra(cena, "C11N36", 2.9):
        cena.play(FadeIn(med_k), run_time=0.4 * VEL)
        cena.play(Flash(med_k.get_center(), color=LARANJA, flash_radius=0.5),
                  ReplacementTransform(coluna_k, unico_k), run_time=1.1 * VEL)

    # cascata: cada linha se TRANSFORMA na conclusão seguinte
    linhas = VGroup(
        formula(("85", LARANJA), ("/", PRETO), ("512", PRETO), ("≈", PRETO),
                ("x", PRETO), ("/", PRETO), ("r", AMARELO),
                tamanho=32, buff=0.10),
        formula(("85", LARANJA), ("/", PRETO), ("512", PRETO), ("≈", PRETO),
                ("1", PRETO), ("/", PRETO), ("6", PRETO),
                ("(frações contínuas)", CINZA), tamanho=28, buff=0.10),
        formula(("r", AMARELO), ("=", PRETO), ("6", AMARELO), tamanho=40),
        VGroup(pot("2", "6", VERMELHO, AMARELO, 30), T("≡", 30, PRETO),
               T("1", 30, VERDE), fmod("21", 28),
               T("✓", 30, VERDE)).arrange(RIGHT, buff=0.14),
        formula(("2⁶ − 1", PRETO), ("=", PRETO),
                ("(2³ − 1)(2³ + 1)", PRETO), ("=", PRETO),
                ("7 · 9", PRETO), tamanho=26, buff=0.10),
        VGroup(formula(("mdc(", PRETO), ("7", PRETO), (", ", PRETO),
                       ("21", LARANJA), (") =", PRETO), ("7", VERDE2),
                       tamanho=26, buff=0.08),
               formula(("mdc(", PRETO), ("9", PRETO), (", ", PRETO),
                       ("21", LARANJA), (") =", PRETO), ("3", ROSA),
                       tamanho=26, buff=0.08)).arrange(RIGHT, buff=0.7),
        formula(("21", LARANJA), ("=", PRETO), ("3", ROSA), ("×", PRETO),
                ("7", VERDE2), tamanho=42),
    ).arrange(DOWN, buff=0.34).move_to(0.15 * DOWN)

    # a leitura é um múltiplo de N/r — é o que os rótulos das marcas
    # diziam, agora com o valor medido dentro. Sete tokens, como a linha
    # de baixo: assim o `85` cai no `85` e o `r` cai no `r`
    # os dois sinais são `≈` e nunca `=`: N/r vale 85,33 e o 85 é o inteiro
    # mais perto. É essa diferença que torna as frações contínuas necessárias
    # no C11N38 — se fosse igualdade, bastava simplificar a fração
    eq_k = formula(("85", LARANJA), ("≈", PRETO), ("x", PRETO), ("·", PRETO),
                   ("N", PRETO), ("/", PRETO), ("r", AMARELO),
                   tamanho=32, buff=0.10).move_to(linhas[0])
    resto_eq = VGroup(*eq_k[1:])

    # o FadeOut pertence ao C11N37 e entra emendado com a primeira conta,
    # num play só — a limpeza é da fala, não do silêncio. Agora quem sai é
    # o circuito inteiro, com a caixa da TQF, a medida e o fundo do
    # registrador de saída; o `pergunta_r` fica, porque é no C11N39 que
    # ele vira a resposta
    with narra(cena, "C11N37", 6.7):
        cena.play(FadeOut(VGroup(cena.volta_circuito, tqf, rot_tqf,
                                 med_k, fundo_k)),
                  # o `85` SAI do registrador e vira o `85` da equação: a
                  # leitura e a conta são a mesma peça na tela
                  ReplacementTransform(unico_k, eq_k[0]),
                  Write(resto_eq), run_time=1.3 * VEL)
        # as duas peças entraram soltas; quem o play seguinte transforma é
        # o grupo, e sem esta troca o ReplacementTransform tiraria só ele
        # da cena e deixaria as soltas
        cena.remove(eq_k[0], resto_eq)
        cena.add(eq_k)
        # dividir os dois lados pelo tamanho do registrador é exatamente o
        # que a fala diz, e é aí que o `N` vira `512`
        cena.play(ReplacementTransform(eq_k, linhas[0]), run_time=1.1 * VEL)
    with narra(cena, "C11N38", 8.3):
        cena.play(Write(linhas[1]), run_time=1.0 * VEL)
        # "que se esconde ali" fecha a frase, e o "ali" é o 85/512 da
        # PRIMEIRA linha, em cena desde o C11N37 — a de baixo, que começa
        # igual, nasce agora e está fora pela regra 2. Circumscribe porque
        # é um pedaço da fórmula; laranja é a cor da leitura k no ato todo
        cena.play(Circumscribe(linhas[0][0:3], color=LARANJA),
                  run_time=0.7 * VEL)
    with narra(cena, "C11N39", 3.5):
        # o único lugar do capítulo em que o valor de r aparece, e é o
        # lugar certo: depois da medida e das frações contínuas, que é
        # quando o algoritmo de fato o conhece. O `r = ?` que espera na
        # borda desde o C11N29, e que nasceu lá no C11N21, VIRA o `r = 6`
        # — pergunta e resposta são o mesmo objeto na tela
        cena.play(ReplacementTransform(cena.pergunta_r, linhas[2]),
                  run_time=1.0 * VEL)
    with narra(cena, "C11N40", 5.4):
        cena.play(Write(linhas[3]), run_time=1.0 * VEL)
    # ---- o parêntese: a medida podia ter caído em outro pico ----------
    # O mecanismo da falha: o pico medido é x·N/r, e as frações contínuas
    # só sabem devolver x/r REDUZIDA. Quando x e r têm fator comum — aqui
    # x = 2 e r = 6 —, o que volta é r dividido por esse fator: 3, um
    # divisor da ordem e não a ordem. Dos seis picos, só o 1·N/r e o 5·N/r
    # dão 6; o `0` não devolve nada (zero sobre 512 não tem denominador
    # para ler) e os outros três caem nisto, e é por isso que a linha da
    # conferência existe.
    #
    # Escurecer a cascata é o device do C11N22: marca o trecho como o que
    # PODIA ter acontecido, e o desfazer do C11N43 é o argumento — a
    # medida que vale continua sendo a de 85. Cada linha escurece sozinha,
    # e não num VGroup novo por cima delas, que reempilharia a cena
    cascata_viva = [linhas[0], linhas[1], linhas[2], linhas[3]]

    # as três linhas da falha pousam nos lugares que as três últimas da
    # cascata vão ocupar: o espaço está vazio, e o desfazer devolve ele
    frac_esq = formula(("171", LARANJA), ("/", PRETO), ("512", PRETO),
                       ("≈", PRETO), ("2", PRETO), ("/", PRETO),
                       ("6", AMARELO), tamanho=28, buff=0.10)
    frac_dir = formula(("=", PRETO), ("1", PRETO), ("/", PRETO),
                       ("3", VERMELHO), tamanho=28, buff=0.10)
    falha_frac = VGroup(frac_esq, frac_dir).arrange(RIGHT, buff=0.14)
    falha_frac.move_to(linhas[4])
    # o `6` é amarelo porque é a ordem de verdade, e o `3` é vermelho
    # porque é o impostor: a cor conta a redução inteira
    falha_r = formula(("r", AMARELO), ("=", PRETO), ("3", VERMELHO),
                      tamanho=40).move_to(linhas[5])
    falha_chk = VGroup(pot("2", "3", VERMELHO, VERMELHO, 30),
                       T("≡", 30, PRETO), T("8", 30, VERDE), fmod("21", 28),
                       T("✗", 30, VERMELHO)).arrange(RIGHT, buff=0.14)
    falha_chk.move_to(linhas[6])

    with narra(cena, "C11N41", 4.2):
        # a cascata escurece e a outra leitura nasce da linha da leitura
        # que valeu: é a mesma conta, com o pico do lado
        cena.play(*[m.animate.set_opacity(0.30) for m in cascata_viva],
                  TransformFromCopy(linhas[1], frac_esq), run_time=1.4 * VEL)

    with narra(cena, "C11N42", 6.6):
        # a fração se reduz: 2/6 é o que a medida guarda, 1/3 é tudo o que
        # as frações contínuas sabem devolver
        cena.play(TransformFromCopy(VGroup(*frac_esq[4:]), frac_dir),
                  run_time=1.0 * VEL)
        # e o denominador vira o r candidato, nascendo do r que valeu
        cena.play(TransformFromCopy(linhas[2], falha_r), run_time=1.1 * VEL)

    with narra(cena, "C11N43", 5.8):
        # a mesma conferência, rodada no candidato errado: nasce da linha
        # de cima e chega com o resto trocado e o visto virado
        cena.play(TransformFromCopy(linhas[3], falha_chk), run_time=1.3 * VEL)
        # e o parêntese fecha: a falha sai e a cascata reacende. O desfazer
        # é o argumento — medir de novo é o que o algoritmo faz
        cena.play(FadeOut(VGroup(falha_frac, falha_r, falha_chk)),
                  *[m.animate.set_opacity(1.0) for m in cascata_viva],
                  run_time=1.6 * VEL)

    with narra(cena, "C11N44", 7.4):
        cena.play(Write(linhas[4]), run_time=1.0 * VEL)
    with narra(cena, "C11N45", 3.4):
        cena.play(Write(linhas[5]), run_time=1.0 * VEL)
    caixa = SurroundingRectangle(linhas[-1], color=VERDE, buff=0.22,
                                 corner_radius=0.15)
    with narra(cena, "C11N46", 3.5):
        cena.play(Write(linhas[6]), Create(caixa), run_time=1.1 * VEL)

    # a moldura verde (o "21 = 3 × 7" E a caixa) sobrevive ao capítulo: o
    # encerramento do vídeo 4 (V4N01) pousa o cadeado em cima dela, sem
    # limpar() no meio — mesma entrega da tese no fim do parte8
    return VGroup(linhas[-1], caixa)


def parte10(cena):
    p10_fundamentos(cena)
    p10_esquema(cena)
    p10_circuito(cena)
    p10_ato1(cena)
    p10_ondas(cena)
    return p10_ato4(cena)
