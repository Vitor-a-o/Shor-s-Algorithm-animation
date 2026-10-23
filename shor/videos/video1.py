# -*- coding: utf-8 -*-
"""Vídeo 1 — Introdução: o vídeo inteiro mora aqui
(roteiro_video1_introducao.md). Não há capítulo por trás dele."""

from manim import *
import numpy as np

from ..paleta import (AMARELO, AZUL, BRANCO, CAIXA, CARTAO_ESCURO, CIANO,
                      CINZA, LARANJA, PRETO, ROSA, ROXO, VERDE, VERDE2,
                      VERMELHO, VEL)
from ..ferramentas import DUR, T, _agora, formula, narra, pot, traco
from ..cadeado import (_ABERTURA, _PARCIAL, _traco_fissura, abrir, cadeado,
                       gravar, quebrar, rachar, rede)
from ..textos import tx
from .comum import VIDEOS, apresentacao, trilha_videos
from ..sincronias import _f

# só para testar com uma voz mais lenta (sessão de acerto de ritmo): 1.0 fora
# de teste. Multiplica a duração que _dur() devolve, simulando uma locução
# gravada mais longa que o est= antes de duracoes.py ter os tempos reais
_ESTICA = 1.0


def _dur(tag, est):
    """A mesma duração que narra() usaria para essa tag (DUR real, com est=
    de fallback) — ver ferramentas.narra."""
    return DUR.get(tag, est) * _ESTICA


def _em(tag, est, frac):
    """O instante, em segundos, de uma fração da fala (frac × _dur)."""
    return frac * _dur(tag, est)


def _k(tag, est):
    """_dur/est: o fator para esticar o run_time dos gestos na mesma
    proporção em que a locução real difere do est= do roteiro."""
    return _dur(tag, est) / est


def _resta(cena, t0, tag, est):
    """O run_time do ÚLTIMO gesto de uma fala que começou em `t0`: o que
    falta, de agora, até o fim dela, em quadros inteiros e sem passar dele.
    Cada play arredonda o run_time PARA CIMA, a quadros inteiros (o
    np.arange(0, run_time, 1/fps) do Manim), e um gesto que ocupasse o
    resto exato passava do fim da fala por até um quadro (a folga do V1N01
    dava −0,04 s em -ql). O meio quadro a menos garante o arredondamento
    para n quadros, não n + 1. Zero se já não couber nenhum."""
    fps = config.frame_rate
    n = np.floor((t0 + _dur(tag, est) - _agora(cena)) * fps + 1e-6)
    return max(0.0, (n - 0.5) / fps)

# a abertura (V1N00): pacotes correndo pela rede, cada um com um cadeado
# fechado em cima. As escalas são as do cadeado() (1 = tamanho natural)
_MINI = 0.16           # os cadeados dos pacotes
_GRANDE = 1.5          # o cadeado no fim do V1N00, sozinho no centro
_SELO = 0.6            # o mesmo cadeado em cima do título, no cartão
_TRACO_CHEIO = 0.6     # abaixo desta escala o traço afina junto com a peça
                       # (o arco de traço 8 viraria uma bolha no _MINI)
_OUTROS = 11           # os pacotes além do escolhido
# a aresta em que o escolhido para, pelos índices dos pontos da rede():
# quase horizontal e a 1,42 de qualquer outra aresta — no fim do empurrão
# (×9,4) nenhum vizinho cabe no quadro. Os outros nunca passam por ela
_ARESTA_ALVO = (5, 6)

# os pontinhos de qubit de "talvez" (V1N00): (x, y) nas bordas do quadro e o
# atraso, em segundos depois da palavra, com que cada um pisca. Fixos, para
# dois renders darem o mesmo quadro
_BORDAS = ((-6.55, 3.15, 0.0), (-6.8, -0.7, 0.22), (-4.9, -3.65, 0.1),
           (-1.3, 3.7, 0.36), (2.6, -3.7, 0.15), (6.7, 2.4, 0.3),
           (6.5, -2.0, 0.05))
_APAGADO = 0.5         # a opacidade deles, sobre a do _qubit()
_DERIVA = 0.08         # fração do caminho até o cadeado andada por segundo

# a faixa da operação de mão única (V1N01), abaixo do cadeado
_FAIXA = -2.3

# a ficha da aposta (V1N01 em diante): o raio dela de pé, e quanto ela
# achata ao cair deitada — a elipse de um disco no chão, visto de lado
_R_FICHA = 0.3
_DEITADA = 0.42
# o "?" do despedaçar que não se espalha e vai para a fechadura em "até
# onde se sabe": um do meio, nascido no trecho que a volta chegou a andar.
# O do centro (3) nasce embaixo da ficha, e o caminho dele a atravessaria
_DA_FECHADURA = 2

# para onde cada "?" do despedaçar se espalha, a partir do seu lugar na
# seta de volta — fixo, para dois renders darem o mesmo quadro (o V1N02
# e o V1N05 contam com as interrogações onde elas pararam)
_ESPALHA = ((-0.7, 0.95, 18), (-0.35, -0.85, -12), (0.15, 1.15, 8),
            (0.3, -0.7, 22), (-0.1, 0.8, -20), (0.55, -1.0, -6),
            (0.8, 0.9, 14))

# os dois primos do V1N02 e o produto — os MESMOS do exemplo do capítulo 8
# (33 = 3 × 11), porque o V1N12 promete que o n de lá se parte "exatamente
# nos primos do V1N02"
_P, _Q, _N = "3", "11", "33"

# os mesmos dois, grandes de verdade (V1N02, "grandes"): primos de 150
# dígitos, gerados uma vez com sympy — o prefixo, os dígitos seguintes
# sorteados por random.Random(1994) e nextprime() a partir daí, os dois
# conferidos com isprime() — e guardados aqui, para o render não depender
# do sympy. Começam com os dígitos de _P e _Q ("30…" e "110…"): crescem do 3
# e do 11 sem trocar o começo, e o produto (a parede de dígitos) começa com
# "33", como o _N
_P_LONGO = ("307746592054454059001688882887722746689248027331205468905908"
            "016903518908958529518359287026649768940152700937245481393089"
            "717765317241437400249635157809")
_Q_LONGO = ("110100769292431055598612420222421041831798981428027792915252"
            "686967364714779617164199177747729576514221599546262285955822"
            "304968548158481558681834799759")
_N_LONGO = str(int(_P_LONGO) * int(_Q_LONGO))      # 299 dígitos

# a parede do V1N02: o _N_LONGO inteiro em linhas de _COLUNAS dígitos,
# alinhadas à direita na face _X_PAREDE (onde a ida termina). A de cima
# fica com o que sobra — começa dentro do quadro, mostrando o "33…" —, e as
# outras saem pela borda esquerda
_COLUNAS = 51
_X_PAREDE = 2.0

# a linha do tempo do V1N06, na faixa livre abaixo da rede, e as colunas de
# qubits que se empilham nela: (fração do caminho de 1994 até hoje, altura).
# Cada vez mais juntas e mais altas — "nos últimos anos"
_LINHA = -3.25
_QUBITS = ((0.12, 1), (0.22, 1), (0.47, 2), (0.66, 2), (0.77, 3),
           (0.86, 4), (0.95, 6))
# o ponto "?" do V1N06, onde o tracejado termina: na mesma linha, à direita
# de "hoje" (x = 2,6) e dentro do quadro. É o caminho que a cópia do pacote
# percorre no V1N07
_X_DUVIDA = 5.2

# as três palavras do V1N07, cada uma com o seu cadeado mini, na metade de
# cima (a de baixo é da linha do tempo): a do meio no alto, acima da ponta
# da rede, e as dos lados mais baixas, nos cantos que a rede deixa livres.
# Todas acima do título que nasce no centro no V1N08
_ALTO_MEIO, _ALTO_LADOS = 3.25, 2.2
# o pacote de "gravado hoje" (V1N07): o do V1N00, maior que o _MINI de lá
# para o estalo do cadeado e a aba se lerem no "?"
_PACOTE = 0.2

# o título da série, que o V1N08 remonta com os cacos dos cadeados
_TITULO = tx("geral.titulo_serie")

# a janela de prévia (V1N10 em diante): uma região fixa da tela, abaixo de
# onde o título da série fica ancorado no topo depois do V1N09. Cada
# trecho da decupagem é montado e passa por _encaixa, que o escala e o
# centra dentro dela — a faixa de fórmula dos capítulos 2–5 nunca entra
# no enquadramento porque as miniaturas não desenham fórmula nenhuma
_JANELA_CENTRO = np.array([0.0, -0.7, 0.0])
_JANELA_LARGURA, _JANELA_ALTURA = 10.2, 4.6


def _grafo(arestas, pontos):
    """Os nós da rede() (os centros dos pontos), os vizinhos de cada um e
    as ligações (i, j) na ordem das arestas, lidos das próprias Lines."""
    pos = [d.get_center() for d in pontos]

    def no(q):
        return int(np.argmin([np.linalg.norm(q - p) for p in pos]))

    viz = {i: [] for i in range(len(pos))}
    lig = []
    for a in arestas:
        i, j = no(a.get_start()), no(a.get_end())
        viz[i].append(j)
        viz[j].append(i)
        lig.append((i, j))
    return pos, viz, lig


def _passeio(rng, viz, de, para, n, proibida):
    """Os n nós de um passeio que começa andando de `de` para `para`: em
    cada nó sorteia a próxima aresta, nunca a `proibida` e sem voltar pela
    que acabou de percorrer (a não ser que não haja outra)."""
    nos = [de, para]
    while len(nos) < n:
        ant, atual = nos[-2], nos[-1]
        op = [v for v in viz[atual]
              if v != ant and {atual, v} != set(proibida)]
        nos.append(int(rng.choice(op or [ant])))
    return nos


def _trilho(pontos):
    """d → o ponto a d unidades do começo da poligonal (parado nas pontas)."""
    pts = [np.array(p, dtype=float) for p in pontos]
    acum = np.concatenate([[0.0], np.cumsum(
        [np.linalg.norm(b - a) for a, b in zip(pts, pts[1:])])])

    def em(d):
        d = min(max(d, 0.0), acum[-1])
        i = min(int(np.searchsorted(acum, d, side="right")) - 1, len(pts) - 2)
        f = (d - acum[i]) / (acum[i + 1] - acum[i])
        return pts[i] + f * (pts[i + 1] - pts[i])
    return em


def _envelope():
    """O envelope fechado, na escala 1 e centrado na origem: o do pacote do
    V1N00 e o do "gravado hoje" do V1N07. Devolve VGroup(corpo, aba); a aba
    é o V de cima, com as duas pontas na altura 0,66 — a dobra."""
    corpo = RoundedRectangle(width=2.4, height=1.5, corner_radius=0.12)
    corpo.set_fill(CAIXA, opacity=1).set_stroke(CINZA, width=3)
    aba = VMobject().set_points_as_corners(
        [[-1.1, 0.66, 0], [0, -0.1, 0], [1.1, 0.66, 0]])
    aba.set_stroke(CINZA, width=3)
    return VGroup(corpo, aba)


def _pacote(cad):
    """Um pacote da rede do V1N00, na escala 1 do cadeado (o updater o
    encolhe): um envelope com `cad` fechado em pé em cima. O envelope fica
    centrado na origem — é o ponto que corre sobre a aresta.
    Devolve VGroup(envelope, cad), com envelope = VGroup(corpo, aba)."""
    envelope = _envelope()
    cad.shift([0, 0.75, 0] - cad[1].get_bottom())
    return VGroup(envelope, cad)


def _mini(m, esc=_MINI):
    """`m` — um cadeado() ou um _pacote(), montado na escala 1 — encolhido
    para `esc` em volta da ORIGEM (o corpo do cadeado, o envelope do pacote:
    o centro deles não sai do lugar), com o traço afinando junto abaixo de
    _TRACO_CHEIO, a mesma regra do _anda(). Os cadeados mini do V1N07 e o
    pacote de "gravado hoje"."""
    fator = min(1.0, esc / _TRACO_CHEIO)
    for sm in m.family_members_with_points():
        sm.set_stroke(width=sm.get_stroke_width() * fator, family=False)
    return m.scale(esc, about_point=ORIGIN)


def _anda(pac, onde, relogio, camera):
    """Põe `pac` (montado em escala 1, envelope na origem) para correr:
    a cada quadro ele vai para `onde(relogio())`, na escala _MINI, e passa
    pela `camera()` — (s, g, foco) do empurrão: o mundo escala s vezes em
    volta do foco e o foco vai para g·foco (s=1, g=1 é a rede parada).

    Os pontos são refeitos a partir da forma guardada, nunca acumulados:
    o quadro não depende do fps nem de quantos quadros já passaram."""
    fam = pac.family_members_with_points()
    base = [sm.points.copy() for sm in fam]
    larguras = [sm.get_stroke_width() for sm in fam]

    def upd(m):
        s, g, foco = camera()
        esc = _MINI * s
        centro = s * (onde(relogio()) - foco) + g * foco
        for sm, pts, w in zip(fam, base, larguras):
            sm.points = centro + esc * pts
            sm.set_stroke(width=w * min(1.0, esc / _TRACO_CHEIO))

    pac.add_updater(upd)
    upd(pac)


def _ficha():
    """A ficha da aposta (fio "A ficha" do roteiro): uma ficha de cassino de
    desenho próprio — disco ROXO com anel interno e seis marcas brancas na
    borda —, de pé (vista de frente) e centrada na origem.

    É um objeto à parte do cadeado: abrir(), gravar(), rachar() e quebrar()
    indexam cad[0], cad[1] e cad[2], então ela nunca entra no VGroup dele.
    Quem move ou escala o cadeado leva a ficha no mesmo play.
    Devolve VGroup(disco, marcas, anel, contorno)."""
    disco = Circle(radius=_R_FICHA).set_fill(ROXO, opacity=1)
    disco.set_stroke(width=0)
    marcas = VGroup(*[AnnularSector(inner_radius=0.7 * _R_FICHA,
                                    outer_radius=_R_FICHA,
                                    angle=26 * DEGREES,
                                    start_angle=(60 * i - 13) * DEGREES)
                      for i in range(6)])
    marcas.set_fill(BRANCO, opacity=1).set_stroke(width=0)
    anel = Circle(radius=0.55 * _R_FICHA).set_stroke(BRANCO, width=2)
    # o contorno por último: as marcas vão até a borda e cobririam metade
    # de um traço desenhado no disco
    contorno = Circle(radius=_R_FICHA).set_stroke(PRETO, width=2.5)
    return VGroup(disco, marcas, anel, contorno)


def _rola(ficha, ate, run_time=1.0, rate_func=rate_functions.ease_out_cubic):
    """A ficha de pé rola no chão até `ate` (o centro dela no fim): anda na
    horizontal e gira o que um disco de raio _R_FICHA gira ao percorrer essa
    distância sem escorregar. Os pontos são refeitos a partir da forma
    guardada a cada quadro — um Rotate somado a um shift no mesmo play
    giraria em volta do centro de partida."""
    fam = ficha.family_members_with_points()
    base = [sm.points.copy() for sm in fam]
    c0 = ficha.get_center()
    desl = np.array(ate, dtype=float) - c0

    def passo(_, a):
        giro = rotation_matrix(-a * desl[0] / _R_FICHA, OUT)
        for sm, pts in zip(fam, base):
            sm.points = (pts - c0) @ giro.T + c0 + a * desl
    return UpdateFromAlphaFunc(ficha, passo, run_time=run_time,
                               rate_func=rate_func)


def _trajeto(m, desl, run_time):
    """`m` deslocado de desl(alpha) a partir dos pontos que ele tem AGORA —
    montar logo antes do play. Refeito da forma guardada a cada quadro, sem
    acumular: com desl(1) = 0 ele volta exatamente aos pontos de antes."""
    fam = m.family_members_with_points()
    base = [sm.points.copy() for sm in fam]

    def passo(_, a):
        d = desl(a)
        for sm, pts in zip(fam, base):
            sm.points = pts + d
    return UpdateFromAlphaFunc(m, passo, run_time=run_time, rate_func=linear)


def _salto(m, ate, altura, run_time=0.5, avanco=linear):
    """`m` salta em arco até `ate` (o centro dele no fim): a reta até lá
    mais uma parábola de `altura` por cima — rápida perto do chão, lenta no
    alto. Com `ate` no próprio centro é o pulinho no lugar.

    `avanco(alpha)` é quanto do caminho na HORIZONTAL já foi andado (a
    vertical segue a parábola). O padrão é o salto em linha reta; um avanço
    que demora a sair faz `m` subir quase na vertical e só depois ir, e
    chegar sem correr de lado — é assim que a ficha deixa o pé do cadeado
    sem passar por cima do canto do corpo."""
    reta = np.array(ate, dtype=float) - m.get_center()
    return _trajeto(m, lambda a: (avanco(a) * reta[0] * RIGHT
                                  + a * reta[1] * UP
                                  + 4 * altura * a * (1 - a) * UP),
                    run_time)


def _treme(m, amp, n, run_time=0.25):
    """`m` treme no lugar: n vaivéns verticais de `amp`, cada vez menores."""
    return _trajeto(m, lambda a: amp * np.sin(2 * PI * n * a) * (1 - a) * UP,
                    run_time)


def _no_mesmo_play(cena, anims, fn, *args, **kw):
    """Roda `fn(cena, *args)` — uma função que faz UM cena.play, como o
    _fechar() — com `anims` somadas àquele mesmo play.

    É o "no mesmo instante" do V1N01: a fusão acontece no quadro do
    travamento, e o travamento continua sendo o gesto do cadeado, com o
    flash seco dele, sem espalhar o Rotate pelo corpo da abertura.
    O play original volta no primeiro uso."""
    def junto(*a, **k):
        cena.__dict__.pop("play", None)
        cena.play(*a, *anims, **k)
    cena.play = junto
    try:
        fn(cena, *args, **kw)
    finally:
        cena.__dict__.pop("play", None)


def _nos_plays(cena, extras, fn, *args, **kw):
    """O _no_mesmo_play para uma função que faz VÁRIOS cena.play, como o
    quebrar(): `extras` é {i: função sem argumentos}, e o play i de
    `fn(cena, *args)` (contando do 0) ganha as animações que extras[i]()
    devolver.

    Cada função roda logo antes do play dela, e não na montagem: pode trocar
    peças na cena e montar .animate a partir do estado daquele instante. As
    animações somadas recebem o run_time de cada play, então `fn` não ganha
    um quadro — é a ficha que racha junto com o arco no V1N06. Devolve o que
    `fn` devolver; o play original volta no fim."""
    feitos = [0]

    def junto(*a, **k):
        extra = extras.get(feitos[0], lambda: ())
        feitos[0] += 1
        type(cena).play(cena, *a, *extra(), **k)
    cena.play = junto
    try:
        return fn(cena, *args, **kw)
    finally:
        cena.__dict__.pop("play", None)


def _fechar(cena, cad, run_time=0.6):
    """O fechar() do cadeado.py com o pivô no PÉ da perna direita.

    Lá o pivô é `cad[0][2].get_bottom()`, o centro de baixo da caixa da
    perna: com o arco aberto a perna está inclinada 60° e esse ponto fica
    fora do pé, então o arco fecha deslocado para a direita e para dentro
    do corpo. O fim da Line (o pé) é o ponto em que o cadeado("aberto")
    girou o arco, em qualquer escala ou posição."""
    pivot = cad[0][2].get_end()
    cena.play(Rotate(cad[0], -_ABERTURA, about_point=pivot),
              Flash(cad[1].get_top(), color=PRETO, flash_radius=0.55,
                    line_length=0.22),
              run_time=run_time * VEL)


def _aviso_fissura(cena, cad, espera=0.0, run_time=0.5, junto=()):
    """O aviso do V1N00, em "perdida": uma fissura fina corre pelo arco e
    some na mesma hora. Não é a quebra — essa é a do V1N06.

    O rachar() não serve aqui. Ele PENDURA a fissura no cad (vira o
    cad[3]), e o quebrar() do V1N06 lê justamente o cad[3] como a rachadura
    que ele continua; e ele a cria no z 0, por baixo do arco do cad, que no
    V1N00 está no z 1. Então o traço é montado aqui com a mesma geometria
    (_traco_fissura e _PARCIAL são os pontos do rachar()) e fica SOLTO na
    cena, um z acima do cadeado: o cad não ganha nem perde nada, e o cartão
    e o V1N01 o recebem como estava.

    `espera` vai no mesmo Succession, antes do traço — é o Wait da âncora.
    O Succession é `introducer`: sem isso o play põe em cena, no primeiro
    quadro, o Group com a fissura inteira, e ela ficava à vista durante o
    Wait. Pelo mesmo motivo o FadeOut não entra nele (um filho que não é
    introducer seria posto em cena no começo); vem no play seguinte.

    `junto` são animações que somem com o traço: entram no play do FadeOut,
    com o run_time dele (os qubits de "talvez", no mesmo instante)."""
    arco = cad[0][0]
    centro = arco.get_arc_center()
    raio = float(np.linalg.norm(arco.point_from_proportion(0.5) - centro))
    fissura = _traco_fissura(arco, centro, 0.07 * raio, _PARCIAL)
    fissura.set_z_index(cad.z_index + 1)
    antes = [id(m) for m in cad.get_family()]
    cena.play(Succession(Wait(espera),
                         Create(fissura, run_time=0.6 * run_time * VEL),
                         introducer=True))
    cena.play(FadeOut(fissura), *junto, run_time=0.4 * run_time * VEL)
    cena.remove(fissura)
    assert [id(m) for m in cad.get_family()] == antes, \
        "o aviso do V1N00 mexeu na estrutura do cadeado"


def _ameaca_abrir(cena, cad, espera=0.0, run_time=0.8, fracao=0.25,
                  fresta=None):
    """O arco sobe uma fração do caminho do abrir(), como se fosse abrir, e
    volta a travar com o flash seco do fechar() (V1N03, "teria acesso").

    O pivô é o pé da perna direita, o mesmo do abrir() e do _fechar(): com
    o cadeado fechado a perna está de pé e cad[0][2].get_bottom() É o pé
    (o get_end()). Ele é lido UMA vez, com o arco fechado, e serve à ida e
    à volta — com a perna inclinada o get_bottom() já não seria o pé.
    No fim os pontos do arco voltam aos guardados: a ida e a volta já se
    desfazem uma à outra, mas assim o cadeado termina fechado sem nem o
    erro de arredondamento das duas rotações.

    `espera` vai no mesmo Succession, antes da subida — é o Wait da âncora.
    A volta com o flash é o play seguinte, emendado, e não o terceiro filho
    do Succession: os raios do Flash nascem prontos, e o play os poria em
    cena no primeiro quadro, parados em volta do cadeado durante o Wait.

    `fresta` (opcional) é o que escapa pela fresta enquanto o arco está
    levantado — os fantasmas das três palavras, no V1N03. Fica em cima e à
    esquerda da ponta da perna esquerda (onde a fresta abre), nasce dela
    junto com a subida e volta para ela, sumindo, no play do travamento:
    cada um no run_time do seu play, então a ameaça não ganha um quadro. O
    Succession da subida vira introducer só com ela (o FadeIn é introducer;
    sem isso a fresta ficaria à vista durante o Wait)."""
    pivot = cad[0][2].get_end()
    angulo = fracao * _ABERTURA
    antes = [m.points.copy() for m in cad[0].get_family()]
    sobe = 0.45 * run_time * VEL
    junto_sobe, junto_trava = [], []
    if fresta is not None:
        ponta = cad[0][1].get_end()        # o pé da perna esquerda, fechado
        ponta = pivot + rotation_matrix(angulo, OUT) @ (ponta - pivot)
        fresta.next_to(ponta, UL, buff=0.1)
        junto_sobe = [Succession(Wait(espera),
                                 FadeIn(fresta, target_position=ponta,
                                        scale=0.1, run_time=sobe),
                                 introducer=True)]
        junto_trava = [FadeOut(fresta, target_position=ponta, scale=0.1)]
    cena.play(Succession(
        Wait(espera),
        Rotate(cad[0], angulo, about_point=pivot, run_time=sobe)),
        *junto_sobe)
    cena.play(Rotate(cad[0], -angulo, about_point=pivot),
              Flash(cad[1].get_top(), color=PRETO, flash_radius=0.55,
                    line_length=0.22), *junto_trava,
              run_time=0.55 * run_time * VEL)
    for m, pts in zip(cad[0].get_family(), antes):
        m.points = pts


def _confere(mobj, area, nome, margem=0.15):
    """Checagem de enquadramento: a caixa de `mobj` tem de caber dentro da
    de `area` (um Rectangle — a moldura da prévia, por exemplo — ou o quadro
    inteiro, quando area=None) com `margem` de folga de cada lado.

    Se sobrar para fora, avisa por logger.warning com o `nome` e quanto
    passou de cada lado; o render segue. Devolve {lado: quanto passou},
    vazio quando está tudo dentro."""
    if area is None:
        esq, dir_ = -config.frame_width / 2, config.frame_width / 2
        baixo, cima = -config.frame_height / 2, config.frame_height / 2
    else:
        esq, dir_ = area.get_left()[0], area.get_right()[0]
        baixo, cima = area.get_bottom()[1], area.get_top()[1]
    passou = {
        "esquerda": (esq + margem) - mobj.get_left()[0],
        "direita": mobj.get_right()[0] - (dir_ - margem),
        "baixo": (baixo + margem) - mobj.get_bottom()[1],
        "cima": mobj.get_top()[1] - (cima - margem),
    }
    passou = {lado: float(v) for lado, v in passou.items() if v > 1e-3}
    if passou:
        onde = "do quadro" if area is None else "da área"
        logger.warning("_confere: %s passa %s (margem %.2f) — %s", nome,
                       onde, margem,
                       ", ".join(f"{lado} {v:.2f}" for lado, v in passou.items()))
    return passou


def _encaixa(grupo, janela, margem=0.25):
    """Enquadramento das prévias: escala `grupo` para caber na área interna
    de `janela` (a moldura menos `margem` de cada lado) — nunca acima do
    tamanho natural — e o centra no centro DA JANELA, não do quadro.

    `grupo` é tudo o que o trecho vai mostrar, no estado mais espalhado:
    o que cresce ou anda entra pelo fim do gesto (as prévias montam um
    "fantasma" do estado final só para a medida, que nunca vai à cena).
    Devolve (s, leva): o fator de escala e a função que leva um ponto das
    coordenadas de montagem para as da janela — para o que o trecho ainda
    calcula à mão depois (always_redraw, deslocamentos)."""
    c0 = grupo.get_center()
    c1 = janela.get_center()
    s = min(1.0, (janela.width - 2 * margem) / grupo.width,
            (janela.height - 2 * margem) / grupo.height)
    grupo.scale(s, about_point=c0).shift(c1 - c0)

    def leva(p):
        return c1 + s * (np.array(p, dtype=float) - c0)
    return s, leva


def _ate(cena, t0, tag, est, frac):
    """Wait até `frac` da fala `tag`, pelo relógio da cena contado de `t0`
    (o começo do narra) — a âncora dos trechos das prévias. É montado logo
    antes do play, então não depende de somar à mão o tempo que já passou
    (a conta à mão não via a abertura da janela e empurrava o V1N10 2 s
    além da fala)."""
    return Wait(max(0.0, t0 + _em(tag, est, frac) - _agora(cena)))


def abertura(cena):
    """V1N00, o cartão (com a apresentação do autor, V0N00) e V1N01. O
    vídeo abre FALANDO, e já em movimento: a internet funcionando, pacotes
    com cadeado correndo pela rede. O empurrão isola um deles, e o cadeado desse pacote — `cad`, o
    MESMO objeto do vídeo inteiro — atravessa o cartão e abre no V1N01.

    Devolve (cad, bloco, interrogacoes, ficha), todos ainda em cena — o
    V1N02 nasce em cima das interrogações e reabre o bloco, então nada disto
    sai aqui. A ficha fica deitada no meio da faixa das setas, e uma das
    interrogações (a _DA_FECHADURA) em cima do buraco da fechadura."""
    # --- montagem do V1N00 -----------------------------------------------
    tag, est = "V1N00", 12.9
    k = _k(tag, est)
    t_zoom = _em(tag, est, _f(tag, "protege"))
    t_para = _em(tag, est, _f(tag, "internet"))      # fim da palavra
    freio = 1.8 * VEL * k                  # o escolhido freia até parar

    # a rede do V1N04 (mesma semente: é a mesma rede que volta lá), sem os
    # cadeados anônimos e mais acesa que os 0,3 de lá
    arestas, pontos, _ = rede()
    arestas.set_stroke(opacity=0.75)
    pontos.set_fill(opacity=0.75).set_z_index(0.5)
    pos, viz, lig = _grafo(arestas, pontos)
    rng = np.random.default_rng(1)

    # o escolhido para no meio da _ARESTA_ALVO, entrando pelo primeiro nó
    # dela. O passeio é montado DE TRÁS PARA FRENTE, a partir do ponto de
    # parada: anda `v` até o freio e desacelera até zero em t_para
    a, b = _ARESTA_ALVO
    cad = cadeado()
    escolhido = _pacote(cad)
    meio = (pos[a] + pos[b]) / 2
    atras = _passeio(rng, viz, b, a, 12, _ARESTA_ALVO)[1:]
    volta_de = _trilho([meio, *[pos[i] for i in atras]])
    v = 1.25
    total = v * (t_para - freio / 2)

    def percorrido(t):
        if t <= t_para - freio:
            return v * t
        tau = min(t, t_para) - (t_para - freio)
        return v * (t_para - freio) + v * (tau - tau ** 2 / (2 * freio))

    def onde_escolhido(t):
        return volta_de(total - percorrido(t))

    # os outros: espalhados pelas arestas (duas delas com dois pacotes, em
    # sentidos contrários — cruzam-se logo no começo), cada um no seu passo
    # Sorteados até caber: ninguém começa a menos de 0,8 de outro pacote (no
    # primeiro quadro eles não se amontoam) nem passa a menos de 1,6 do
    # escolhido na segunda metade do empurrão (um vizinho colado a ele, já
    # grande no quadro, deixaria em dúvida qual é o alvo)
    outras = [e for e in lig if set(e) != set(_ARESTA_ALVO)]
    longas = sorted(range(len(outras)), key=lambda i: -np.linalg.norm(
        pos[outras[i][0]] - pos[outras[i][1]]))
    perto = np.linspace((t_zoom + t_para) / 2, t_para, 25)
    sentidos, trajetos, comecos = [], [], [onde_escolhido(0.0)]
    for n in range(_OUTROS):
        if n < len(outras):
            de, para = outras[n][::int(rng.choice([1, -1]))]
        else:                           # os que sobram vão para as arestas
            # mais longas, no sentido contrário ao do primeiro de lá
            para, de = sentidos[longas[n - len(outras)]]
        for _ in range(200):
            nos = _passeio(rng, viz, de, para, 30, _ARESTA_ALVO)
            comeco = pos[de] + float(rng.uniform(0.1, 0.9)) * (pos[para] - pos[de])
            trilho = _trilho([comeco, *[pos[i] for i in nos[1:]]])
            vel = float(rng.uniform(1.0, 1.5))
            if (min(np.linalg.norm(comeco - c) for c in comecos) > 0.8 and
                    min(np.linalg.norm(trilho(vel * t) - onde_escolhido(t))
                        for t in perto) > 1.6):
                break
        else:
            raise ValueError(f"pacote {n} da abertura não achou lugar")
        sentidos.append((de, para))
        comecos.append(comeco)
        trajetos.append((trilho, vel))
    outros = [_pacote(cadeado()) for _ in trajetos]

    # o empurrão: como no V4N00, é o mundo que escala em volta do alvo (a
    # cena não tem câmera móvel). Zoom exponencial — ritmo constante para o
    # olho. O foco é o corpo do cadeado escolhido ONDE ELE ESTÁ: a câmera o
    # acompanha enquanto ele freia (a rede passa por baixo) e o leva ao
    # centro; quando ele para, o foco para junto
    zoom = ValueTracker(0.0)
    corpo_no_pacote = _MINI * cad[1].get_center()

    def camera():
        u = smooth(zoom.get_value())
        foco = onde_escolhido(relogio()) + corpo_no_pacote
        return (_GRANDE / _MINI) ** u, 1 - u, foco

    # a senha: o envelope do escolhido escorrega para o lado do cadeado e
    # vira o campo; seis pontos digitados um a um; um risco por cima
    lado = (_GRANDE * 1.9 / 2) + 0.5      # a borda direita do corpo + folga
    campo = RoundedRectangle(width=3.6, height=0.9, corner_radius=0.15)
    campo.set_fill(BRANCO, opacity=1).set_stroke(CINZA, width=3)
    campo.move_to([lado + 1.8, 0, 0])
    senha = VGroup(*[Dot(radius=0.1, color=PRETO) for _ in range(6)])
    senha.arrange(RIGHT, buff=0.25)
    senha.move_to(campo).align_to(campo, LEFT).shift(0.35 * RIGHT)
    risco = Line(campo.get_left() + 0.15 * RIGHT + 0.14 * DOWN,
                 campo.get_right() + 0.15 * LEFT + 0.14 * UP,
                 color=VERMELHO, stroke_width=8)

    # o relógio dos pacotes é o do vídeo (o mesmo do narra), não a soma dos
    # dt: cada play perde o dt do último quadro e o cache soma o run_time
    # inteiro, e o escolhido pararia em lugar diferente em -ql e em -qh
    inicio = _agora(cena)

    def relogio():
        return _agora(cena) - inicio

    # --- V1N00 -------------------------------------------------------------
    with narra(cena, "V1N00", 12.9):
        _anda(escolhido, onde_escolhido, relogio, camera)
        for pac, (trilho, vel) in zip(outros, trajetos):
            _anda(pac, lambda t, tr=trilho, vl=vel: tr(vl * t),
                  relogio, camera)
        pacotes = [escolhido, *outros]
        for pac in pacotes:
            pac.set_z_index(1)
        # o primeiro quadro já tem os nós e os pacotes andando; as arestas
        # se desenham por baixo deles, rápido
        cena.add(pontos, *pacotes)
        desenha = 0.8 * VEL * k
        cena.play(Succession(
            LaggedStart(*[Create(l) for l in arestas], lag_ratio=0.1,
                        run_time=desenha),
            Wait(max(0.0, t_zoom - desenha))))

        # "protege quase tudo que você faz na internet": o empurrão. A rede
        # escala com os pacotes e se apaga nos últimos 40%. O updater mora na
        # PRIMEIRA aresta e move a rede inteira: o Manim congela num fundo
        # estático tudo o que se desenha antes do primeiro mobject com
        # updater, e as arestas (z 0) se desenham antes dos pontos (z 0,5)
        fam_rede = [*arestas, *pontos]
        base_rede = [m.points.copy() for m in fam_rede]

        def rede_upd(_):
            s, g, foco = camera()
            for m, pts in zip(fam_rede, base_rede):
                m.points = s * (pts - foco) + g * foco
            op = 0.75 * (1 - np.clip((smooth(zoom.get_value()) - 0.45) / 0.45,
                                     0, 1))
            arestas.set_stroke(opacity=op)
            pontos.set_fill(opacity=op)

        arestas[0].add_updater(rede_upd)
        cena.play(zoom.animate.set_value(1.0), run_time=t_para - t_zoom,
                  rate_func=linear)
        # o último quadro fica exato (câmera em 1, escolhido parado) e tudo
        # para de andar; o que não é o escolhido já está fora do quadro
        for m in (arestas[0], *pacotes):
            m.update(0)
            m.clear_updaters()
        cena.remove(*arestas, pontos, *outros, escolhido)
        # o cadeado segue no z 1 até o fim da fala: o Succession de cada play
        # embrulha as peças num Group novo, que o Manim empilha no topo, e o
        # envelope passaria por cima do corpo ao escorregar
        envelope = escolhido[0]
        cena.add(envelope, cad)
        envelope.set_z_index(0)

        # "e ela não é": o envelope sai de baixo do cadeado e vira o campo
        t = t_para
        cena.play(Succession(
            Wait(max(0.0, _em(tag, est, _f(tag, "e ela não é")) - t)),
            AnimationGroup(ReplacementTransform(envelope[0], campo),
                           FadeOut(envelope[1], scale=0.4,
                                   target_position=campo.get_center()),
                           run_time=0.6 * VEL * k)))
        t = _em(tag, est, _f(tag, "e ela não é")) + 0.6 * VEL * k
        # "uma senha forte" ≈ 0,52: os pontos entram um a um, cada um num
        # estalo, com a pausa da digitação entre eles
        cena.play(Succession(
            Wait(max(0.0, _em(tag, est, _f(tag, "senha forte")) - t)),
            LaggedStart(*[GrowFromCenter(d) for d in senha], lag_ratio=3.0,
                        run_time=1.2 * VEL * k)))
        t = _em(tag, est, _f(tag, "senha forte")) + 1.2 * VEL * k
        # "que você possa" ≈ 0,59: riscado de vermelho...
        cena.play(Succession(
            Wait(max(0.0, _em(tag, est, _f(tag, "que você possa")) - t)),
            Create(risco, run_time=0.35 * VEL * k)))
        t = _em(tag, est, _f(tag, "que você possa")) + 0.35 * VEL * k

        # "E talvez" ≈ 0,76: pontinhos de qubit apagados piscam nas bordas e
        # derivam devagar rumo ao cadeado, sem chegar nele. Não ganham play
        # nenhum: como os pacotes, tudo sai do relógio, e o updater os acende
        # e os empurra durante os plays que já vêm — a saída do campo e a
        # espera do _aviso_fissura, que assim não atrasa um quadro. Entram
        # em cena apagados já aqui, para piscar na hora mesmo se a palavra
        # cair durante a saída do campo
        t_talvez = _em(tag, est, _f(tag, "talvez"))
        qubits = VGroup(*[_qubit().scale(1.3).move_to([x, y, 0])
                          for x, y, _ in _BORDAS])
        _confere(qubits, None, "qubits de \"talvez\"")
        rumo = cad[1].get_center()
        origens = [d.get_center() for d in qubits]

        def acende(g):
            for d, p0, (_, _, atraso) in zip(g, origens, _BORDAS):
                s = relogio() - t_talvez - atraso
                # o pisca: acende, quase apaga, volta; depois só cintila
                op = _APAGADO * float(np.interp(s, (0, 0.1, 0.18, 0.3),
                                                (0, 1, 0.2, 1)))
                op *= 0.85 + 0.15 * np.cos(2 * PI * 0.9 * s + 5 * atraso)
                d.move_to(p0 + _DERIVA * max(0.0, s) * (rumo - p0))
                d.set_stroke(opacity=op).set_fill(opacity=0.35 * op)

        qubits.add_updater(acende)
        acende(qubits)
        cena.add(qubits)

        # ...e em "escolher" ≈ 0,68 some. O cadeado não se mexeu: no fim da
        # fala ele está sozinho, grande, no centro
        cena.play(Succession(
            Wait(max(0.0, _em(tag, est, _f(tag, "escolher")) - t)),
            AnimationGroup(*[FadeOut(m, shift=0.4 * DOWN)
                             for m in (campo, *senha, risco)],
                           run_time=0.6 * VEL * k)))
        # "perto de ser perdida" ≈ 0,95: a fissura corre pelo arco e some —
        # o aviso, solto por cima do cad (ver _aviso_fissura). Capada como o
        # alvo7 do V1N06: os 0,5 s do traço têm de acabar dentro da fala
        # (teto 12,4 s de 12,9, fração ≈0,96 — hoje a palavra manda). A
        # espera conta do instante em que o campo terminou de sair, mas lido
        # no relógio (o mesmo do narra), não somado como o t acima: cada play
        # arredonda para quadros inteiros, e a soma à mão chegava aqui ~0,4 s
        # atrasada em -ql — o traço passava do fim da fala. Os qubits somem
        # no play em que a fissura some
        alvo = min(_em(tag, est, _f(tag, "perdida")), k * (est - 0.5))
        _aviso_fissura(cena, cad, espera=max(0.0, alvo - relogio()),
                       run_time=0.5 * k, junto=[FadeOut(qubits)])
        qubits.clear_updaters()
    cad.set_z_index(0)

    # --- cartão: o título entra e o cadeado sai do caminho dele,
    # encolhendo para cima — sem sair de cena. Ele sai mais depressa e o
    # título começa um pouco depois: quando a escrita chega ao meio da
    # linha, o cadeado já não está lá
    t1 = T(tx("geral.titulo_serie"), 42)
    t2 = T(tx("geral.video_n_de_4").format(n=1, nome=VIDEOS[0]), 28, CINZA)
    VGroup(t1, t2).arrange(DOWN, buff=0.5)
    cena.play(cad.animate(run_time=0.7 * VEL).scale(_SELO / _GRANDE)
                 .next_to(t1, UP, buff=0.45),
              Succession(Wait(0.3 * VEL), Write(t1, run_time=0.8 * VEL)))
    cena.play(FadeIn(t2, shift=0.25 * UP), run_time=0.8 * VEL)
    apresentacao(cena, t2)
    cena.play(FadeOut(t1), FadeOut(t2), run_time=0.6 * VEL)

    # --- V1N01 -----------------------------------------------------------
    # o cadeado volta ao centro no tamanho natural; os itens se posicionam
    # pelo lugar aonde ele vai chegar
    cad.generate_target()
    cad.target.scale(1 / _SELO)
    cad.target.shift([0, 0.9, 0] - cad.target[1].get_center())

    itens = VGroup(T(tx("v1.contas_bancarias"), 30), T(tx("v1.compras_online"), 30),
                   T(tx("v1.mensagens_privadas"), 30))
    itens[0].next_to(cad.target[1], LEFT, buff=1.2)
    itens[1].next_to(cad.target[1], RIGHT, buff=1.2)
    itens[2].next_to(cad.target[1], DOWN, buff=0.5)

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
    # a volta aos trancos: o primeiro pedaço (35% do caminho) e onde ela
    # para de vez, com a ponta embaixo da ficha. O Transform de um no outro
    # é o "avança mais um pouco" (as duas têm a ponta do mesmo tamanho)
    meio = (-2.55 + 2.4) / 2
    volta = Arrow([2.4, _FAIXA, 0], [2.4 - 0.35 * 4.95, _FAIXA, 0], buff=0,
                  color=PRETO, stroke_width=5)
    volta_mais = Arrow([2.4, _FAIXA, 0], [meio, _FAIXA, 0], buff=0,
                       color=PRETO, stroke_width=5)
    interrogacoes = VGroup(*[T("?", 36, CINZA) for _ in _ESPALHA])
    for q, x in zip(interrogacoes, np.linspace(2.2, -2.35, len(_ESPALHA))):
        q.move_to([x, _FAIXA, 0])

    # a ficha entra rolando pela esquerda, de pé, no chão do cadeado (a
    # linha de baixo do corpo, onde ele vai chegar), e para ao pé dele, do
    # lado de onde veio; ali cai deitada para trás, pela borda que toca o
    # chão. O "deitada" é montado do estado em que o rolar a deixa (o
    # .animate de dentro do mesmo Succession seria montado da ficha ainda
    # na partida, e a levaria de volta para lá)
    ficha = _ficha()
    chao = cad.target[1].get_bottom()[1]
    pe = np.array([cad.target[1].get_left()[0] - 0.25 - _R_FICHA,
                   chao + _R_FICHA, 0])
    ficha.move_to([-config.frame_width / 2 - _R_FICHA - 0.1, pe[1], 0])
    deitada = ficha.copy().rotate((ficha.get_x() - pe[0]) / _R_FICHA)
    deitada.move_to(pe).stretch(_DEITADA, 1, about_point=pe + _R_FICHA * DOWN)
    # onde ela pousa em "o que se aposta": no meio da faixa das setas,
    # deitada, um pouco acima da linha — a ponta da seta (0,35 de altura) e
    # o "?" que nasce embaixo dela (0,37) passam sem encostar
    mesa = [meio, _FAIXA + 0.4 + _DEITADA * _R_FICHA, 0]

    with narra(cena, "V1N01", 14.6):
        tag, est = "V1N01", 14.6
        k = _k(tag, est)
        t0 = _agora(cena)                  # o começo da fala, o do narra
        # "Essa aposta está por trás de...": o cadeado desce ao centro e
        # abre em silêncio (os mesmos 2,0 s dos dois plays do rótulo de
        # antes: as contas de Wait abaixo continuam valendo). No mesmo
        # movimento a ficha rola até o pé dele e deita — o run_time do play
        # vale para o Succession inteiro, que o divide na proporção dos dois
        cena.add(ficha)
        cena.play(MoveToTarget(cad),
                  Succession(_rola(ficha, pe, run_time=0.75),
                             Transform(ficha, deitada, run_time=0.25,
                                       rate_func=rush_into)),
                  run_time=1.2 * VEL * k)
        _confere(ficha, None, "a ficha ao pé do cadeado")
        abrir(cena, cad, run_time=0.8 * k)
        # "contas bancárias" ≈ 0,11 (o play acima já cobre) · "compras
        # online" ≈ 0,20 · "mensagens privadas" ≈ 0,29 — uma a cada respiro.
        # Cada Wait conta a partir da âncora anterior mais os run_time que
        # vieram depois dela, não de um total somado à mão: trocar a fração
        # de uma âncora não desloca as seguintes
        cena.play(FadeIn(itens[0], shift=0.3 * RIGHT), run_time=0.8 * VEL * k)
        t_compras = _em(tag, est, _f(tag, "compras online"))
        cena.play(Succession(Wait(max(0.0, t_compras - k * 2.8)),
                             FadeIn(itens[1], shift=0.3 * LEFT,
                                    run_time=0.8 * VEL * k)))
        t_msgs = _em(tag, est, _f(tag, "mensagens privadas"))
        cena.play(Succession(
            Wait(max(0.0, t_msgs - (t_compras + 0.8 * VEL * k))),
            FadeIn(itens[2], shift=0.3 * UP, run_time=0.8 * VEL * k)))
        # e se condensam dentro dele. "o que se aposta" ≈ 0,43 cai no meio
        # disso: a ficha salta em arco do pé do cadeado até a faixa das
        # setas e pousa no meio do caminho — a aposta é sobre essa volta.
        # Ela sobe quase na vertical e só depois avança (sine⁵ na
        # horizontal): num arco reto ela passaria por cima do canto do corpo;
        # assim passa a 0,14 dele e pousa sem correr de lado.
        # Cada animação leva o seu run_time e o play não leva nenhum: o do
        # play esticaria a espera e o salto para dentro do 1,2 da condensação
        # (desde "mensagens": FadeIn 0,8)
        t_aposta = _em(tag, est, _f(tag, "o que se aposta"))
        cena.play(*[it.animate(run_time=1.2 * VEL * k).scale(0.05)
                    .move_to(cad[1]).set_opacity(0) for it in itens],
                  Succession(
                      Wait(max(0.0, t_aposta - (t_msgs + 0.8 * VEL * k))),
                      _salto(ficha, mesa, 1.1, run_time=0.9 * VEL * k,
                             avanco=lambda a:
                                 rate_functions.ease_in_out_sine(a) ** 5)))
        cena.remove(*itens)
        _confere(ficha, None, "a ficha na faixa das setas")

        # "operações": os dois fatores cinzas na faixa de baixo
        cena.play(FadeIn(f1, shift=0.2 * UP), FadeIn(f2, shift=0.2 * UP),
                  run_time=1.2 * VEL * k)
        # "fáceis de fazer numa direção" ≈ 0,63: a seta varre para a
        # direita, rápida e sem esforço — acelera e solta...
        # (desde "o que se aposta": salto 0,9 + fatores 1,2 — é o salto que
        # fecha o play da condensação: ela acaba antes dele)
        t_ida = _em(tag, est, _f(tag, "fáceis de fazer"))
        cena.play(Succession(
            Wait(max(0.0, t_ida - (t_aposta + 2.1 * VEL * k))),
            GrowArrow(ida, run_time=0.4 * VEL * k,
                      rate_func=rate_functions.ease_in_out_cubic)))
        # ...e os fatores se fundem no bloco no instante em que o cadeado
        # trava — o play é o do _fechar() (o fechar() com o pivô no pé)
        _no_mesmo_play(cena, [ReplacementTransform(f1, bloco[0]),
                              ReplacementTransform(f2, bloco[1]),
                              FadeOut(ida)],
                       _fechar, cad, run_time=0.6 * k)

        # "impraticáveis de desfazer" ≈ 0,78: a volta avança aos trancos —
        # cresce um pedaço e para...
        # (desde "fáceis": ida 0,4 + trava 0,6)
        t_imp = _em(tag, est, _f(tag, "impraticáveis"))
        cena.play(Succession(
            Wait(max(0.0, t_imp - (t_ida + 1.0 * VEL * k))),
            GrowArrow(volta, run_time=0.28 * VEL * k, rate_func=rush_from)))
        # ...treme, avança mais um pouco e emperra embaixo da ficha. Num play
        # à parte do GrowArrow: o tremor e o Transform não são introducers, e
        # o Succession poria a seta inteira em cena durante o Wait de cima
        cena.play(Succession(
            Wait(0.12 * VEL * k),
            _treme(volta, 0.05, 4, run_time=0.25 * VEL * k),
            Transform(volta, volta_mais, run_time=0.2 * VEL * k,
                      rate_func=rush_from)))
        # e só então se despedaça em interrogações cinzas; a ficha, logo
        # acima, dá um pulinho só e fica intacta: a aposta se mantém
        cena.play(ReplacementTransform(volta, interrogacoes),
                  _salto(ficha, ficha.get_center(), 0.3),
                  run_time=0.4 * VEL * k)

        # as interrogações se espalham e o cadeado chacoalha sem abrir. Uma
        # do meio não se espalha: fica onde nasceu e, em "até onde se sabe"
        # ≈ 0,92, vai para cima do buraco da fechadura. A palavra leva um
        # teto, como o "perdida" do V1N00: o voo (0,45) e um pisca (0,4) têm
        # de caber na fala (teto 13,75 s de 14,6, fração ≈0,94 — hoje a
        # palavra manda)
        # (desde "impraticáveis": cresce 0,28 + para 0,12 + treme 0,25 +
        # avança 0,2 + despedaça 0,4 = 1,25)
        t_sabe = min(_em(tag, est, _f(tag, "até onde se sabe")),
                     k * (est - 0.85 * VEL))
        # em cima do buraco, cinza sobre preto, o "?" se perdia no desenho do
        # buraco (que também é um ponto e uma haste): um contorno branco POR
        # TRÁS dele recorta o buraco. Ganha o contorno só agora, já fora do
        # Transform do despedaçar (lá o traço viria do preto da seta); no
        # fundo branco ele não aparece até o "?" chegar ao cadeado
        fica = interrogacoes[_DA_FECHADURA]
        fica.set_stroke(BRANCO, width=6, background=True)
        cena.play(*[q.animate(run_time=1.2 * VEL * k)
                    .shift([dx, dy, 0]).rotate(ang * DEGREES)
                    for i, (q, (dx, dy, ang)) in enumerate(
                        zip(interrogacoes, _ESPALHA)) if i != _DA_FECHADURA],
                  Wiggle(cad, run_time=1.2 * VEL * k),
                  Succession(
                      Wait(max(0.0, t_sabe - (t_imp + 1.25 * VEL * k))),
                      fica.animate(run_time=0.45 * VEL * k, path_arc=0.6)
                          .move_to(cad[2])))
        # e fica ali, piscando fraco, até o fim da fala. É o último gesto,
        # então lê o relógio, como o aviso do V1N00: os plays acima podem
        # ter acabado pelo espalhar ou pelo voo, conforme a gravação
        piscar = max(0.1, _resta(cena, t0, tag, est))
        vezes = max(1, round(piscar / (0.55 * VEL * k)))
        cena.play(UpdateFromAlphaFunc(
            fica, lambda m, a: m.set_fill(
                opacity=1 - 0.6 * (1 - np.cos(2 * PI * vezes * a)) / 2),
            rate_func=linear), run_time=piscar)

    return cad, bloco, interrogacoes, ficha


def _anos(e):
    """O contador do V1N03: 10^e − 1 anos, com ponto de milhar."""
    return f"{int(10 ** e) - 1:,}".replace(",", ".")


def _contador(e, ponto):
    """O contador do V1N03, que dispara de novo no V1N14: segue o
    ValueTracker `e` e engorda com ele, centrado em `ponto`."""
    return always_redraw(
        lambda: T(_anos(e.get_value()), 44)
        .scale(1 + e.get_value() / 10).move_to(ponto))


def _primo_longo(digitos, cor, curto, ate_x):
    """O primo grande do V1N02, a partir do curto que já está em cena: os
    primeiros dígitos de `digitos` e um "…", no tamanho do `curto` (36), com
    os primeiros glifos (tantos quantos o curto tem) exatamente em cima
    dele — o curto é trocado por eles sem pulo, e o resto cresce para a
    direita. Corta no maior número de dígitos que ainda termina antes de
    `ate_x` (a busca parte de uma estimativa pela largura de um dígito do
    curto, não dos 150)."""
    por_digito = curto.width / len(curto)
    n0 = min(len(digitos), int((ate_x - curto.get_x()) / por_digito) + 3)
    for n in range(n0, 1, -1):
        longo = T(digitos[:n] + "…", 36, cor)
        comeco = VGroup(*longo[:len(curto)])
        if longo.width - comeco.width / 2 <= ate_x - curto.get_x():
            break
    longo.shift(curto.get_center() - comeco.get_center())
    return longo


def _parede(centro_y):
    """A parede de dígitos do V1N02: o _N_LONGO inteiro, laranja (é o n), em
    letra pequena, em linhas de _COLUNAS dígitos alinhadas à direita na face
    _X_PAREDE e empilhadas em volta de `centro_y`. As linhas são cortadas do
    FIM do número, então a de cima fica com a sobra (começa dentro do quadro,
    no "33…") e as outras saem pela borda esquerda.
    Devolve VGroup das linhas, de cima para baixo."""
    n = _N_LONGO
    cortes = list(range(len(n), 0, -_COLUNAS))[::-1]
    linhas = [n[max(0, c - _COLUNAS):c] for c in cortes]
    parede = VGroup(*[T(l, 24, LARANJA) for l in linhas])
    parede.arrange(DOWN, buff=0.07, aligned_edge=RIGHT)
    parede.shift([_X_PAREDE - parede.get_right()[0],
                  centro_y - parede.get_y(), 0])
    return parede


def _barra(esq, y, largura, relogio, desde, k=1.0):
    """A barra de progresso do V1N02/V1N03 (o fio "O tempo", sempre em
    linha): contorno e preenchimento, cinzas — é o computador comum. O
    preenchimento segue o relógio a partir de `desde` e anda quase nada,
    cada vez mais devagar (logaritmo): ~2,5% no fim do V1N02, ~4% quando sai
    com o contador. O updater recebe o dt (é por tempo) para o wait do fim
    do narra também ser desenhado quadro a quadro, e refaz a largura a
    partir da forma cheia guardada, sem acumular.
    Devolve VGroup(contorno, enche); o updater mora no `enche`."""
    contorno = RoundedRectangle(width=largura, height=0.22,
                                corner_radius=0.11)
    contorno.set_stroke(CINZA, width=2.5).set_fill(opacity=0)
    contorno.move_to([esq + largura / 2, y, 0])
    enche = Rectangle(width=largura - 0.08, height=0.13)
    enche.set_fill(CINZA, opacity=1).set_stroke(width=0)
    enche.move_to(contorno)
    base = enche.points.copy()
    borda = enche.get_left()[0]

    def upd(m, dt):
        f = 0.012 * np.log1p(max(0.0, relogio() - desde) / (0.15 * k))
        f = min(1.0, max(f, 0.004))
        m.points = base.copy()
        m.points[:, 0] = borda + (base[:, 0] - borda) * f

    enche.add_updater(upd)
    upd(enche, 0)
    return VGroup(contorno, enche)


def _chip(cor):
    """O chip do computador: quadrado arredondado de `cor` com um miolo
    claro e quatro pinos curtos, pretos, em cada lado — cinza no V1N03 (o
    comum), ciano no V1N05 (o quântico: basta um set_fill no corpo). Lado
    1,0 sem os pinos, centrado na origem.
    Devolve VGroup(pinos, corpo, miolo): os pinos primeiro, por baixo."""
    pinos = VGroup()
    for ang in (0, PI / 2, PI, 3 * PI / 2):
        for s in (-0.3, -0.1, 0.1, 0.3):
            pinos.add(Line([0.45, s, 0], [0.64, s, 0])
                      .rotate(ang, about_point=ORIGIN))
    pinos.set_stroke(PRETO, width=3)
    corpo = RoundedRectangle(width=1.0, height=1.0, corner_radius=0.12)
    corpo.set_fill(cor, opacity=1).set_stroke(PRETO, width=2.5)
    miolo = RoundedRectangle(width=0.5, height=0.5, corner_radius=0.06)
    miolo.set_stroke(BRANCO, width=2).set_fill(opacity=0)
    return VGroup(pinos, corpo, miolo)


def _fila(de_x, ate_x, y, relogio, desde, k=1.0):
    """A fila de tentativas do computador comum (V1N03): ÷2, ÷3, ÷5, ÷7, …
    (os primos em ordem) saem do chip, em `de_x`, e andam até a parede, em
    `ate_x`; lá cada uma leva um risco vermelho curto e se apaga. Saem cada
    vez mais depressa e andam cada vez mais rápido, até se encavalarem num
    borrão. Tudo pelo relógio a partir de `desde`, como os qubits do V1N00:
    atravessa os plays do contador sem play próprio e sem somar tempo.
    Devolve VGroup de VGroup(tentativa, risco)."""
    primos = [n for n in range(2, 500)
              if all(n % d for d in range(2, int(n ** 0.5) + 1))]
    fila = VGroup()
    for n in primos:
        tent = T(f"÷{n}", 26, CINZA)
        risco = Line(LEFT, RIGHT, color=VERMELHO, stroke_width=4)
        risco.set_width(tent.width + 0.12).rotate(20 * DEGREES)
        fila.add(VGroup(tent, risco))
    # a i-ésima sai quando N(s) = s·(1,5 + 2,1·s) — 1,5 por segundo no
    # começo, ~22 por segundo depois de 5 s — e anda de 0,9 s a 0,35 s
    sai = [(-1.5 + np.sqrt(1.5 ** 2 + 8.4 * i)) / 4.2 for i in range(len(fila))]
    anda = [max(0.35, 0.9 - 0.11 * s) for s in sai]

    def upd(g, dt):
        s = (relogio() - desde) / k
        for par, t_sai, t_anda in zip(g, sai, anda):
            tent, risco = par
            a = s - t_sai
            w = tent.width
            if a < 0 or a > t_anda + 0.25:
                op_t = op_r = 0.0
                x = de_x - w / 2
            elif a < t_anda:
                op_t, op_r = min(1.0, a / 0.08), 0.0
                x = (de_x - w / 2) - (de_x - ate_x - w) * a / t_anda
            else:
                op_t = op_r = 1 - (a - t_anda) / 0.25
                x = ate_x + w / 2
            par.move_to([x, y, 0])
            tent.set_fill(opacity=op_t)
            risco.set_stroke(opacity=op_r)

    fila.add_updater(upd)
    upd(fila, 0)
    return fila


def corpo_fatoracao(cena, cad, bloco, interrogacoes, ficha):
    """V1N02 e V1N03. Recebe o que a abertura deixou em cena e termina com
    o cadeado sozinho no centro, com a ficha ao pé.

    O bloco é o MESMO do V1N01: no V1N02 as duas metades se reabrem nos
    fatores cinzas e ganham a cor de p e q; os números crescem até os primos
    de 150 dígitos e, na ida rápida, tudo se funde na parede — o produto
    inteiro. A volta, que vem da direita, bate na face da parede e se
    despedaça, e uma barra de progresso quase não anda. No V1N03 o chip
    cinza ataca a parede com uma fila de divisões, o contador dispara, tudo
    sai, o cadeado vai ao centro e ameaça abrir; pela fresta, por um
    instante, os fantasmas das três palavras do V1N01.

    Devolve (cacos, primos, chip, contador, anos, ficha):
    - cacos: as interrogações novas, fora de cena, onde pararam — o V1N05
      as traz de volta;
    - primos: VGroup(p, q) dos dois primos longos cortados em "…", fora de
      cena, onde estavam antes de se fundirem na parede;
    - chip: o chip cinza, fora de cena, no lugar (o V1N05 o traz de volta);
    - contador e anos: o contador de anos, parado em cheio, fora de cena,
      no tamanho de antes do estouro, e o ValueTracker dele, em 10;
    - ficha: em cena, deitada ao pé do cadeado, que está no centro."""
    fat = T(tx("v1.fatoracao"), 72).move_to([0, _FAIXA, 0])

    # os dois fatores cinzas em que o bloco se reabre, nas medidas e no
    # lugar do f1 e do f2 do V1N01: os primos vêm de lá, da esquerda para a
    # direita, como antes. O p nasce em cima do seu quadrado e o q embaixo
    # do dele: os dois crescem para a direita, cada um na sua linha, e a
    # ida passa entre eles
    cinzas = VGroup(Square(0.55), Square(0.8))
    cinzas.set_fill(CINZA, opacity=1).set_stroke(width=0)
    cinzas[0].move_to([-4.3, _FAIXA, 0])
    cinzas[1].move_to([-3.35, _FAIXA, 0])
    p = T(_P, 36, ROSA).next_to(cinzas[0], UP, buff=0.3)
    q = T(_Q, 36, VERDE2).next_to(cinzas[1], DOWN, buff=0.3)
    # os primos longos, cortados antes da face da parede; o V1N05 recebe
    # cópias tiradas aqui (o ReplacementTransform da parede deforma estes)
    p_longo = _primo_longo(_P_LONGO, ROSA, p, _X_PAREDE - 0.2)
    q_longo = _primo_longo(_Q_LONGO, VERDE2, q, _X_PAREDE - 0.2)
    _confere(p_longo, None, "o primo p longo")
    _confere(q_longo, None, "o primo q longo")
    primos = VGroup(p_longo.copy(), q_longo.copy())

    def rajadas(longo, curto):
        """Os dígitos do primo longo depois dos do curto (que já estão em
        cena), escorrendo para a direita de quatro em quatro."""
        return LaggedStart(*[AnimationGroup(*[FadeIn(g, shift=0.15 * RIGHT)
                                              for g in longo[i:i + 4]])
                             for i in range(len(curto), len(longo), 4)],
                           lag_ratio=0.7)

    # a parede ocupa a faixa da borda esquerda até a face, onde a ida
    # termina; a volta vem da direita e bate nessa face. Os cacos nascem ao
    # longo dela e se espalham do lado de fora da parede
    parede = _parede(_FAIXA)
    ida = Arrow([-2.55, _FAIXA, 0], [_X_PAREDE, _FAIXA, 0], buff=0,
                color=PRETO, stroke_width=5)
    volta = Arrow([6.4, _FAIXA, 0], [_X_PAREDE + 0.1, _FAIXA, 0], buff=0,
                  color=PRETO, stroke_width=5)
    cacos = VGroup(*[T("?", 36, CINZA) for _ in _ESPALHA])
    for c, x in zip(cacos, np.linspace(6.15, _X_PAREDE + 0.45,
                                       len(_ESPALHA))):
        c.move_to([x, _FAIXA, 0])

    # o chip do V1N03, à direita da parede, de onde a volta veio
    chip = _chip(CINZA).move_to([5.3, _FAIXA, 0])

    # o contador nasce da ponta da barra e cresce na faixa livre entre o
    # cadeado e a parede (no meio da parede, preto sobre os dígitos, não se
    # lia). Cheio, ele dobra de altura: centrado em -0,55, vai de -1,0 a
    # -0,1, entre a primeira linha da parede e o pé do cadeado
    e = ValueTracker(0)
    contador = _contador(e, [0, -0.55, 0])

    # os fantasmas do V1N03: as três palavras do V1N01, apagadas, numa
    # pilha — o _ameaca_abrir a põe na fresta
    fantasmas = VGroup(*[T(tx(c), 24) for c in (
        "v1.contas_bancarias", "v1.compras_online", "v1.mensagens_privadas")])
    fantasmas.arrange(DOWN, buff=0.1, aligned_edge=RIGHT).set_opacity(0.3)

    with narra(cena, "V1N02", 12.9):
        tag, est = "V1N02", 12.9
        k = _k(tag, est)
        t0 = _agora(cena)                  # o começo da fala, o do narra
        # "fatoração" ≈ 0,23 da fala, mas o roteiro pede que ela nasça "logo
        # nos primeiros segundos" — ou seja, ANTES da fração mecânica da
        # palavra, não nela: fica imediato, só com o run_time esticado. A
        # ficha volta para o pé do cadeado junto com a escrita, pelo salto
        # do V1N01 ao contrário (o avanço espelhado: sai de lado, sobe e cai
        # quase na vertical, sem passar pelo canto do corpo). Cada animação
        # com o seu run_time: o do play esticaria o salto
        pe = [cad[1].get_left()[0] - 0.25 - _R_FICHA,
              cad[1].get_bottom()[1] + _DEITADA * _R_FICHA, 0]
        cena.play(Write(fat, run_time=1.4 * VEL * k),
                  FadeOut(interrogacoes, run_time=1.4 * VEL * k),
                  _salto(ficha, pe, 1.1, run_time=0.9 * VEL * k,
                         avanco=lambda a: 1 - rate_functions.ease_in_out_sine(
                             1 - a) ** 5))
        cena.play(Succession(
            fat.animate(run_time=1.2 * VEL * k).scale(0.55)
               .to_edge(UP, buff=0.4),
            Wait(0.5 * VEL * k)))

        # "Multiplicar dois primos grandes" ≈ 0,30: o bloco se reabre pela
        # emenda e cada metade volta a ser o fator cinza de que era feita,
        # lá na esquerda, onde o V1N01 o montou...
        t_mult = _em(tag, est, _f(tag, "multiplicar"))
        cena.play(Succession(
            Wait(max(0.0, t_mult - k * 3.1)),
            AnimationGroup(Transform(bloco[0], cinzas[0]),
                          Transform(bloco[1], cinzas[1]),
                          run_time=0.8 * VEL * k)))
        # ...que ganha identidade: rosa é p, verde-claro é q, e cada número
        # nasce de dentro do seu quadrado
        cena.play(bloco[0].animate.set_fill(ROSA),
                  bloco[1].animate.set_fill(VERDE2),
                  GrowFromPoint(p, cinzas[0].get_center()),
                  GrowFromPoint(q, cinzas[1].get_center()),
                  run_time=0.7 * VEL * k)

        # "grandes" ≈ 0,43: os dois crescem para a direita, em rajadas, até
        # os primos de 150 dígitos cortados em "…". O curto dá lugar aos
        # primeiros glifos do longo, que estão exatamente em cima dele
        # (desde "multiplicar": reabre 0,8 + cores 0,7)
        t_grandes = _em(tag, est, _f(tag, "grandes"))
        cena.remove(p, q)
        cena.add(*p_longo[:len(p)], *q_longo[:len(q)])
        cena.play(Succession(
            Wait(max(0.0, t_grandes - (t_mult + 1.5 * VEL * k))),
            AnimationGroup(rajadas(p_longo, p), rajadas(q_longo, q),
                           run_time=0.5 * VEL * k)))

        # "é fácil" ≈ 0,48: a ida rápida do V1N01 — acelera e solta — entre
        # as duas linhas, até a face da parede...
        # (desde "grandes": cresce 0,5)
        t_facil = _em(tag, est, _f(tag, "é fácil"))
        cena.play(Succession(
            Wait(max(0.0, t_facil - (t_grandes + 0.5 * VEL * k))),
            GrowArrow(ida, run_time=0.4 * VEL * k,
                      rate_func=rate_functions.ease_in_out_cubic)))
        # ...e os dois primos se fundem na parede: o produto inteiro,
        # laranja (é o n) — o p nas três linhas de cima, o q nas três de
        # baixo (uma fileira virando a parede toda passava por um borrão), e
        # os quadrados encolhem e somem. Os glifos que o crescimento soltou
        # na cena saem dela antes: o ReplacementTransform troca só o grupo
        # de origem, e um glifo solto sobraria em cena por cima da parede.
        # Pelo mesmo motivo, no fim, as duas metades dão lugar à parede
        # inteira, que é o grupo que o V1N03 tira
        cima, baixo = VGroup(*parede[:3]), VGroup(*parede[3:])
        cena.remove(*p_longo, *q_longo)
        cena.play(ReplacementTransform(p_longo, cima),
                  ReplacementTransform(q_longo, baixo),
                  *[FadeOut(b, scale=0.3) for b in bloco],
                  FadeOut(ida), run_time=0.5 * VEL * k)
        cena.remove(cima, baixo)
        cena.add(parede)

        # "voltar do produto para os primos" ≈ 0,55: a volta vem da direita,
        # acelerando, e bate na face da parede — que recua com o golpe — e
        # se despedaça em interrogações, que se espalham do lado de fora,
        # no mesmo espalhar do V1N01
        # (desde "é fácil": ida 0,4 + funde 0,5)
        t_volta = _em(tag, est, _f(tag, "voltar do produto"))
        cena.play(Succession(
            Wait(max(0.0, t_volta - (t_facil + 0.9 * VEL * k))),
            GrowArrow(volta, run_time=0.5 * VEL * k, rate_func=rush_into)))
        cena.play(ReplacementTransform(volta, cacos),
                  _trajeto(parede, lambda a: -0.12 * np.sin(PI * a) * RIGHT,
                           0.4),
                  run_time=0.4 * VEL * k)
        cena.play(*[c.animate.shift([dx, dy, 0]).rotate(ang * DEGREES)
                    for c, (dx, dy, ang) in zip(cacos, _ESPALHA)],
                  run_time=1.2 * VEL * k)

        # "em tempo razoável" ≈ 0,91: a barra de progresso surge embaixo da
        # parede e enche quase nada, cada vez mais devagar, até o fim da fala
        # — e segue no V1N03, pelo relógio. A palavra leva um teto: o surgir
        # (0,4) e um pouco de enchimento (0,2) têm de caber na fala (teto
        # 12,3 s de 12,9, fração ≈0,95 — hoje a palavra manda)
        # (desde "voltar": volta 0,5 + despedaça 0,4 + espalha 1,2)
        t_tempo = min(_em(tag, est, _f(tag, "tempo razoável")),
                      k * (est - 0.6 * VEL))
        barra = _barra(-5.8, parede.get_bottom()[1] - 0.3, 6.5,
                       lambda: _agora(cena), t0 + t_tempo + 0.4 * VEL * k, k)
        cena.play(Succession(
            Wait(max(0.0, t_tempo - (t_volta + 2.1 * VEL * k))),
            Create(barra[0], run_time=0.4 * VEL * k)))
        # a barra entra inteira como um grupo só (o contorno que o Create
        # pôs solto sai): o FadeOut do V1N03 tira o grupo, e um membro solto
        # ficaria em cena
        cena.remove(barra[0])
        cena.add(barra)

    with narra(cena, "V1N03", 10.4):
        tag, est = "V1N03", 10.4
        k = _k(tag, est)
        t0 = _agora(cena)
        # "teria acesso" ≈ 0,74 (target 7,7 s de 10,4) leva o seu próprio
        # teto, no estilo do alvo7 do V1N06: os 0,8 s da ameaça de abrir têm
        # de acabar dentro da fala (9,6 s de 10,4, fração ≈0,92)
        t_acesso = min(_em(tag, est, _f(tag, "teria acesso")),
                       k * (est - 0.8))
        # "bilhões de anos" ≈ 0,17 (target 1,7 s de 10,4). Depois dele vêm
        # o contador e a saída dele (0,8 + 3,0 + 0,6) e o cadeado indo ao
        # centro (1,2): 5,6 s fixos, que têm de caber ANTES de "teria
        # acesso". O teto é o instante daquele gesto menos eles (2,1 s de
        # 10,4, fração ≈0,20); hoje a palavra cai antes dele e manda, mas só
        # por 0,3 s — numa gravação em que as duas palavras fiquem mais
        # perto, é ele que segura a ameaça em "teria acesso"
        alvo = min(_em(tag, est, _f(tag, "bilhões de anos")),
                   t_acesso - k * 5.6)
        # "Um computador comum" ≈ 0,02: o chip cinza aparece à direita da
        # parede, onde a volta nasceu, e as interrogações dela saem; dele sai
        # a fila de divisões. A fila e a barra andam pelo relógio, e o chip
        # vai no MESMO play da espera até "bilhões", em paralelo com ela:
        # nada disto soma aos 5,6 s fixos
        t_comum = _em(tag, est, _f(tag, "computador comum"))
        fila = _fila(chip.get_left()[0] - 0.05, _X_PAREDE + 0.05, _FAIXA,
                     lambda: _agora(cena), t0 + t_comum + 0.5 * VEL * k, k)
        cena.add(fila)
        # "bilhões de anos": o contador nasce da ponta da barra
        cena.play(
            Succession(Wait(t_comum),
                       AnimationGroup(GrowFromCenter(chip), FadeOut(cacos),
                                      run_time=0.5 * VEL * k)),
            Succession(Wait(max(0.0, alvo)),
                       GrowFromPoint(contador, barra[1].get_right(),
                                     run_time=0.8 * VEL * k)))
        cena.play(e.animate.set_value(10), run_time=3.0 * VEL * k,
                  rate_func=linear)
        contador.clear_updaters()
        # o contador estoura fora da tela, e saem com ele a parede, a fila,
        # a barra e o chip (o chip fica fora de cena, no lugar: o V1N05 o
        # traz de volta)
        cena.play(FadeOut(contador, scale=4), FadeOut(parede), FadeOut(fila),
                  FadeOut(barra), FadeOut(chip), run_time=0.6 * VEL * k)
        fila.clear_updaters()
        barra[1].clear_updaters()

        # o cadeado fica sozinho, no centro, e a ficha vai junto, ao pé dele
        cena.play(FadeOut(fat), cad.animate.move_to(ORIGIN),
                  ficha.animate.shift(ORIGIN - cad.get_center()),
                  run_time=1.2 * VEL * k)

        # "teria acesso a tudo que essa aposta protege": o arco ameaça abrir
        # e trava de novo; pela fresta, só enquanto ele está levantado, os
        # fantasmas das três palavras (dentro dos 0,8 da ameaça: o fim dela
        # não muda)
        # (desde "bilhões": aparece 0,8 + conta 3,0 + estoura 0,6 + centro
        # 1,2 = 5,6)
        _ameaca_abrir(cena, cad,
                      espera=max(0.0, t_acesso - (alvo + 5.6 * VEL * k)),
                      run_time=0.8 * k, fresta=fantasmas)

    return cacos, primos, chip, contador, e, ficha


def _pe(cad):
    """O centro da ficha deitada ao pé de `cad`: à esquerda do corpo, no
    chão dele — a conta do V1N01 e do V1N02, lida do corpo onde ele estiver
    (qualquer escala, qualquer posição)."""
    corpo = cad[1]
    return np.array([corpo.get_left()[0] - 0.25 - _R_FICHA,
                     corpo.get_bottom()[1] + _DEITADA * _R_FICHA, 0.0])


def _rotulos_rsa():
    """Os quatro rótulos da vista explodida do V1N04, escritos como o
    roteiro pede ("Peças e notação"): p·q, mod n, φ(n), e·d — fórmulas, sem
    chave em textos.py, nessa ordem (a do roteiro e a do retorno do
    corpo_rsa).

    O formula() alinha os tokens pelo CENTRO: a haste do "d" põe o centro
    de "mod" e de "d" acima do de "n" e de "e", e o "n" subia, o "d"
    descia. Aqui os tokens sem perna voltam à linha de base do primeiro, e
    o "·" ao meio da altura do "e" (do "p", contando só a parte de cima da
    perna)."""
    pq = formula(("p", ROSA), ("·", PRETO), ("q", VERDE2), tamanho=34,
                 buff=0.08)
    modn = formula(("mod", PRETO), ("n", LARANJA), tamanho=34, buff=0.14)
    phi = formula(("φ(", PRETO), ("n", LARANJA), (")", PRETO), tamanho=34,
                  buff=0.06)
    ed = formula(("e", PRETO), ("·", PRETO), ("d", PRETO), tamanho=34,
                 buff=0.08)
    modn[1].align_to(modn[0], DOWN)
    ed[2].align_to(ed[0], DOWN)
    ed[1].set_y(ed[0].get_y())
    # o "x" de altura do p: do topo dele até onde o "n" (sem perna) acaba
    alto = T("n", 34)
    pq[1].set_y(pq[0].get_top()[1] - alto.height / 2)
    return VGroup(pq, modn, phi, ed)


# a vista explodida do V1N04 ("peça por peça"), em frações da altura do
# corpo, para valer em qualquer escala: quanto o arco sobe, quanto o corpo
# desce, quanto o rótulo "RSA" cresce ao vir para a frente
_SOBE_ARCO, _DESCE_CORPO, _FRENTE = 0.35, 0.45, 1.4

# os dois anônimos da rede que ganham nome no V1N04 — índices dos cadeados
# da rede(): o 3 (o mais à esquerda, a 3,8 do centro) e o 2 (o de cima, à
# esquerda, a 3,1). Os outros longe do centro estão à direita, onde o
# V1N05 trabalha: embaixo do 6 caem as interrogações, e o nome do 0
# encostava no arco do 9, logo abaixo dele
_BATIZADOS = ((3, "v1.diffie_hellman"), (2, "v1.curvas_elipticas"))


def corpo_rsa(cena, cad, ficha):
    """V1N04. O cadeado ganha as letras RSA, se desmonta "peça por peça"
    numa vista explodida com os quatro rótulos do RSA, se remonta "do zero"
    e encolhe no miolo de uma rede de cadeados anônimos, que brotam de trás
    dele; dois deles ganham nome. A ficha acompanha o cadeado a fala toda,
    sempre ao pé dele (`_pe`), e fica em cena.

    A vista explodida só MOVE as peças do cad — o arco (cad[0]) sobe, o
    corpo (cad[1]) desce, o rótulo (cad[2]) cresce no vão entre os dois — e
    cada uma volta por Restore aos pontos que tinha: a estrutura
    [arco, corpo, rótulo] do cadeado.py não muda, e abrir()/quebrar() seguem
    valendo para ele.

    Devolve (malha, rotulos, nomes):
    - malha: a rede — VGroup(arestas, pontos, cadeados), tudo em cena, como
      a rede() a monta — para o V1N06 piscá-la e estalá-la;
    - rotulos: VGroup(p·q, mod n, φ(n), e·d), FORA de cena, inteiros (no
      tamanho e no lugar da vista explodida: o FadeOut os devolve assim) —
      o V1N08 os traz de volta em volta do título;
    - nomes: VGroup("Diffie-Hellman", "curvas elípticas"), em cena, cada um
      embaixo do seu anônimo (`_BATIZADOS`). Ficam À PARTE da malha, e não
      dentro dela: a malha continua sendo a da rede() (o V4N03 e o V1N06
      contam com VGroup(arestas, pontos, cadeados)), e o estalo do V1N06
      derruba só o arco do anônimo — o corpo e o nome ficam. Saem no
      V1N08, com o resto."""
    malha = rede()
    arestas, pontos, anonimos = malha

    with narra(cena, "V1N04", 20.0):
        tag, est = "V1N04", 20.0
        k = _k(tag, est)
        t0 = _agora(cena)                  # o começo da fala, o do narra
        # cada espera lê o relógio (conta a partir de t0), e não a soma dos
        # run_times desde a âncora anterior: entre o gravar e "não é o
        # único" entraram os plays da vista explodida, e em -ql cada play
        # arredonda para quadros inteiros

        def ate(alvo):
            return Wait(max(0.0, t0 + alvo - _agora(cena)))

        # "é o RSA" ≈ 0,22: o cadeado cresce e as letras se gravam com o
        # flash seco do travamento. A ficha vai junto, para o pé dele
        t_rsa = _em(tag, est, _f(tag, "RSA"))
        maior = cad.copy().scale(1.4)
        cena.play(Succession(ate(t_rsa), AnimationGroup(
            cad.animate.scale(1.4), ficha.animate.move_to(_pe(maior)),
            run_time=2.2 * VEL * k)))
        gravar(cena, cad, "RSA", run_time=0.9 * k)
        # o aceso vai na frente de tudo o que nascer daqui em diante: a rede
        # é desenhada DEPOIS dele e mesmo assim fica atrás (depois do
        # gravar(), para as letras subirem junto com o corpo)
        cad.set_z_index(1)

        # --- "peça por peça" ≈ 0,43: a vista explodida ---------------------
        arco, corpo, letras = cad[0], cad[1], cad[2]
        for m in (arco, corpo, letras, ficha):
            m.save_state()
        h = corpo.height
        sobe, desce = _SOBE_ARCO * h * UP, _DESCE_CORPO * h * DOWN
        # o vão entre o pé das pernas do arco, que sobe, e o topo do corpo,
        # que desce: o rótulo vem para a frente — cresce — e flutua nele
        vao = (arco.get_bottom()[1] + sobe[1] + corpo.get_top()[1]
               + desce[1]) / 2
        # as peças no lugar da vista explodida, só para medir os rótulos
        arco_x, corpo_x = arco.copy().shift(sobe), corpo.copy().shift(desce)

        # e·d e φ(n) no arco — o que tranca e destranca: as duas chaves e o
        # que as amarra; p·q e mod n no corpo — o n, laranja como ele. Cada
        # rótulo a 1,1 da peça, ligado a um ponto dela por um traço fino
        # (com um pingo na ponta da peça)
        rotulos = _rotulos_rsa()
        pq, modn, phi, ed = rotulos
        curva = arco_x[0]                      # o Arc, sem as pernas
        # (no corpo, à meia altura: mais baixo, o p·q encostava na ficha)
        ancoras = [corpo_x.get_left(),                        # p·q
                   corpo_x.get_right(),                       # mod n
                   curva.point_from_proportion(0.82),         # φ(n)
                   curva.point_from_proportion(0.18)]         # e·d
        lados = (LEFT, RIGHT, RIGHT, LEFT)
        for r, a, lado in zip(rotulos, ancoras, lados):
            r.next_to(a, lado, buff=1.1)
            _confere(r, None, "rótulo da vista explodida")
        tracos = VGroup()
        for r, a, lado in zip(rotulos, ancoras, lados):
            ponta = r.get_edge_center(-lado) + 0.12 * lado
            tracos.add(VGroup(Line(a, ponta, color=CINZA, stroke_width=1.5),
                              Dot(a, radius=0.035, color=CINZA)))
        # onde cada rótulo some no "do zero": no ponto dele na peça JÁ de
        # volta ao lugar (a âncora menos o deslocamento da peça)
        pousos = [ancoras[0] - desce, ancoras[1] - desce,
                  ancoras[2] - sobe, ancoras[3] - sobe]

        t_pecas = _em(tag, est, _f(tag, "peça por peça"))
        cena.play(Succession(ate(t_pecas), AnimationGroup(
            arco.animate.shift(sobe),
            corpo.animate.shift(desce), ficha.animate.shift(desce),
            letras.animate.scale(_FRENTE).move_to([letras.get_x(), vao, 0]),
            run_time=0.6 * VEL * k)))
        # os rótulos, um a um: o traço sai da peça e o rótulo acende na ponta
        # dele (o FadeIn só começa quando o traço chega; até lá ele está em
        # cena, invisível)
        chega = lambda t: smooth(float(np.clip((t - 0.45) / 0.55, 0, 1)))
        cena.play(LaggedStart(*[
            AnimationGroup(Create(tr[0]), GrowFromCenter(tr[1]),
                           FadeIn(r, shift=0.15 * lado, rate_func=chega))
            for r, tr, lado in zip(rotulos, tracos, lados)],
            lag_ratio=0.25), run_time=0.8 * VEL * k)

        # --- "do zero" ≈ 0,63: as peças voltam uma a uma ------------------
        # o corpo (com a ficha), o rótulo e por último o arco, que desce
        # acelerando e trava com o flash seco do fechar(); os traços apagam
        # e os rótulos encolhem e somem, cada um no seu ponto da peça — o
        # FadeOut os devolve inteiros, fora de cena, para o V1N08. A
        # palavra leva um teto, como o "bilhões" do V1N03: os 1,1 s × k da
        # volta (0,77 s no DUR pt de hoje) têm de acabar antes de "não é o
        # único" — com as frações de hoje as duas palavras ficam a só 0,06
        # da fala (0,81 s): a palavra ainda manda, por 0,04 s; numa gravação
        # em que elas fiquem mais perto, é o teto que adianta a volta
        t_unico = _em(tag, est, _f(tag, "não é o único"))
        t_zero = min(_em(tag, est, _f(tag, "do zero")),
                     t_unico - 1.1 * VEL * k)
        um = 0.4 * VEL * k
        cena.play(Succession(ate(t_zero), AnimationGroup(
            *[FadeOut(tr, run_time=0.25 * VEL * k) for tr in tracos],
            *[FadeOut(r, scale=0.1, target_position=p,
                      run_time=0.45 * VEL * k)
              for r, p in zip(rotulos, pousos)],
            Restore(corpo, run_time=um), Restore(ficha, run_time=um),
            Succession(Wait(0.15 * VEL * k), Restore(letras, run_time=um)),
            Succession(Wait(0.3 * VEL * k),
                       Restore(arco, run_time=um, rate_func=rush_into)))))
        # o flash no instante em que o arco assenta — num play à parte: num
        # Succession, os raios do Flash ficariam parados à vista desde o
        # primeiro quadro. O do fechar() (raio 0,55, traço 0,22) na escala
        # do cadeado de agora, para ter o mesmo tamanho em relação a ele
        s = corpo.width / 1.9
        cena.play(Flash(corpo.get_top(), color=PRETO,
                        flash_radius=0.55 * s, line_length=0.22 * s),
                  run_time=0.4 * VEL * k)

        # "não é o único" ≈ 0,68: o cadeado encolhe e a rede se desenha ao
        # fundo, já apagada; a ficha vai para o pé dele
        menor = cad.copy().scale(0.8 / 1.4)
        cena.play(Succession(ate(t_unico), AnimationGroup(
            cad.animate.scale(0.8 / 1.4), ficha.animate.move_to(_pe(menor)),
            Create(arestas),
            LaggedStart(*[GrowFromCenter(d) for d in pontos],
                        lag_ratio=0.15),
            run_time=1.6 * VEL * k)))
        # os anônimos brotam de trás dele e pousam cada um na sua aresta; os
        # dois batizados ganham o nome embaixo junto com o pouso (o FadeIn
        # só acende no fim do caminho deles). Pequenos e cinzas, um contorno
        # branco por trás corta a aresta que passa por baixo do nome
        for c in anonimos:
            c.generate_target()
            c.move_to(cad[1])
        nomes = VGroup()
        for i, chave in _BATIZADOS:
            # no tamanho 18 o Text abre as letras e come o espaço (lia-se
            # "curvaselípticas", "ellipticcurves"): nasce no 36 e encolhe
            nome = T(tx(chave), 36, CINZA).scale(0.5)
            # (a 0,12: no pulso de "único a cair" o anônimo cresce 35%)
            nome.next_to(anonimos[i].target, DOWN, buff=0.12)
            nome.set_stroke(BRANCO, width=5, background=True)
            _confere(nome, None, "nome de um anônimo")
            nomes.add(nome)
        dono = {i: nome for (i, _), nome in zip(_BATIZADOS, nomes)}
        pousa = lambda t: smooth(float(np.clip((t - 0.6) / 0.4, 0, 1)))
        cena.add(anonimos)
        cena.play(LaggedStart(*[
            AnimationGroup(MoveToTarget(c),
                           FadeIn(dono[i], shift=0.1 * UP, rate_func=pousa))
            if i in dono else MoveToTarget(c)
            for i, c in enumerate(anonimos)],
            lag_ratio=0.12), run_time=1.8 * VEL * k)

        # "nem vai ser o único a cair" ≈ 0,88: todos pulsam uma vez, junto
        cena.play(Succession(
            ate(_em(tag, est, _f(tag, "único a cair"))),
            AnimationGroup(*[c.animate.scale(1.35) for c in anonimos],
                          rate_func=there_and_back, run_time=0.8 * VEL * k)))

    return malha, rotulos, nomes


def _qubit():
    """O marcador de qubit da linha do tempo do V1N06: uma bolinha na cor
    do bit 1, de miolo claro."""
    return (Circle(radius=0.065).set_stroke(CIANO, width=2.5)
            .set_fill(CIANO, opacity=0.35))


def _estalar_rede(cena, cad_pequeno, run_time=0.5):
    """O estalo discreto de um cadeado anônimo da rede (V1N06): o arco pula
    um dedo, gira e cai para fora da rede, apagando. Sem fissura correndo —
    o `quebrar()` fica para o cadeado grande.

    NÃO chama play: devolve (animação, arco), para o chamador somar os
    estalos de todos num LaggedStart. A `cena` serve só para soltar o arco:
    ele sai do VGroup do cadeado e entra na cena sozinho, então o corpo fica
    parado onde está e só o arco cai.

    Como no `quebrar()`, o arco caído continua em cena, invisível, onde
    caiu: o V1N08 o reacende dali (por `set_stroke`, não `set_opacity`)."""
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


def _frente(arestas, pontos, origem):
    """O pulso do V1N06 como uma frente de onda pela rede: sai de `origem`
    (o corpo do cadeado RSA, no miolo, fora do _grafo), vai em linha reta
    até o nó mais perto dele e dali corre por TODAS as arestas, sempre na
    mesma velocidade. É a busca em largura do _grafo com o comprimento de
    cada Line como peso: cada nó é alcançado pelo caminho mais curto, e numa
    aresta alcançada pelas duas pontas os dois pulsos se encontram no meio
    do caminho e somem juntos.

    Devolve, em DISTÂNCIA percorrida pela frente (o chamador divide pela
    velocidade):
    - trechos: [(de, ate, d0, d1)] — um pontinho anda em linha reta de `de`
      a `ate` enquanto a frente vai de d0 a d1;
    - meios: onde a frente passa pelo meio de cada aresta — onde pende o
      anônimo dela —, na ordem das arestas (a dos cadeados da rede())."""
    pos, viz, lig = _grafo(arestas, pontos)
    raiz = int(np.argmin([np.linalg.norm(p - origem) for p in pos]))

    def comp(i, j):
        return float(np.linalg.norm(pos[i] - pos[j]))

    dist = {i: np.inf for i in viz}
    dist[raiz] = float(np.linalg.norm(pos[raiz] - origem))
    abertos = set(viz)
    while abertos:
        i = min(abertos, key=dist.get)
        abertos.remove(i)
        for j in viz[i]:
            dist[j] = min(dist[j], dist[i] + comp(i, j))

    trechos = [(np.array(origem, dtype=float), pos[raiz], 0.0, dist[raiz])]
    meios = []
    for i, j in lig:
        L = comp(i, j)
        encontro = (dist[i] + dist[j] + L) / 2
        for a, b in ((i, j), (j, i)):
            if encontro - dist[a] > 1e-6:
                ate = pos[a] + (encontro - dist[a]) / L * (pos[b] - pos[a])
                trechos.append((pos[a], ate, dist[a], encontro))
        meios.append(min(dist[i], dist[j]) + L / 2)
    return trechos, meios


def _folha():
    """A folha de papel do V1N06 ("Era teoria"): um retângulo claro com
    cinco traços cinzas — linhas de texto, a última mais curta — na metade
    de cima, levemente inclinado. Centrada na origem; a metade de baixo fica
    livre para o ponto 1994, que pousa por cima dela."""
    papel = Rectangle(width=0.72, height=0.95)
    papel.set_fill(BRANCO, opacity=1).set_stroke(CINZA, width=2)
    tracos = VGroup(*[Line([-0.27, y, 0], [-0.27 + c, y, 0])
                      for y, c in zip((0.34, 0.24, 0.14, 0.04, -0.06),
                                      (0.54, 0.54, 0.46, 0.54, 0.3))])
    tracos.set_stroke(CINZA, width=2)
    return VGroup(papel, tracos).rotate(5 * DEGREES)


# a rachadura da ficha (V1N06): (desvio, posição) em frações de _R_FICHA. A
# posição corre ao longo do corte, de uma borda (1) à outra (−1); o desvio é
# para o lado. Zero nas bordas e na altura do anel (±0,55): o anel e o
# contorno se partem em dois semicírculos exatos. O corte passa no meio de
# um vão entre marcas, a 0,2 delas, e o desvio não passa de 0,16: nenhuma
# marca é cortada
_FENDA = ((0.0, 1.0), (0.14, 0.78), (0.0, 0.55), (-0.16, 0.3), (0.13, 0.04),
          (-0.15, -0.26), (0.0, -0.55), (0.14, -0.78), (0.0, -1.0))


def _racha_ficha(ficha):
    """A ficha partida em duas (V1N06), montada à parte para o quebrar():
    devolve (fenda, metades) no lugar e na forma da `ficha` de agora —
    deitada e girada pelo rolar do V1N01 —, sem mexer nela.

    - fenda: o risco cinza da rachadura, de borda a borda, para o Create;
    - metades: VGroup(esquerda, direita), cada uma VGroup(disco, marcas,
      anel, contorno) como a _ficha(), com o disco cortado em zigue-zague.
      Juntas cobrem a ficha inteira: a troca de uma pela outra não se vê.

    As peças são desenhadas na ficha de pé da _ficha() e levadas até a de
    agora pela mesma transformação afim que a levou até ali (rolar, deitar,
    deslizar), lida dos próprios pontos por mínimos quadrados. O corte passa
    num dos três vãos entre as marcas (30°, 90° ou 150°): o que, com a ficha
    deitada, fica mais perto da vertical."""
    r = _R_FICHA
    base = _ficha()
    de = np.vstack([m.points for m in base.family_members_with_points()])
    para = np.vstack([m.points for m in ficha.family_members_with_points()])
    assert de.shape == para.shape, "a ficha mudou de estrutura"
    uns = np.c_[de[:, :2], np.ones(len(de))]
    X = np.linalg.lstsq(uns, para[:, :2], rcond=None)[0]
    assert np.abs(uns @ X - para[:, :2]).max() < 1e-6, \
        "a ficha não é uma transformação afim da _ficha()"
    A, b = X[:2].T, X[2]
    M = np.eye(3)
    M[:2, :2] = A

    def vertical(g):
        v = A @ [np.cos(g * DEGREES), np.sin(g * DEGREES)]
        return abs(v[1]) / np.linalg.norm(v)

    phi = max((30, 90, 150), key=vertical) * DEGREES
    d = np.array([np.cos(phi), np.sin(phi), 0.0])
    n = np.array([-d[1], d[0], 0.0])
    corte = [r * (t * d + o * n) for o, t in _FENDA]

    disco, marcas, anel, contorno = base
    metades = VGroup()
    # cada metade: o semicírculo de um lado do corte, fechado pelo próprio
    # corte, percorrido no sentido contrário
    for lado, ini, borda in ((1, phi, corte[::-1]), (-1, phi + PI, corte)):
        meia = VMobject().set_points(
            Arc(radius=r, start_angle=ini, angle=PI).points)
        for p in borda[1:]:
            meia.add_line_to(p)
        metades.add(VGroup(
            meia.match_style(disco),
            VGroup(*[m.copy() for m in marcas
                     if lado * np.dot(m.get_center(), n) > 0]),
            Arc(radius=0.55 * r, start_angle=ini, angle=PI).match_style(anel),
            Arc(radius=r, start_angle=ini, angle=PI).match_style(contorno)))
    fenda = VMobject(stroke_color=CINZA, stroke_width=2.5)
    fenda.set_points_as_corners(corte)
    for m in (*metades, fenda):
        m.apply_matrix(M).shift([b[0], b[1], 0])
    if metades[0].get_x() > metades[1].get_x():
        metades = VGroup(metades[1], metades[0])
    return fenda, metades


def corpo_shor(cena, cad, malha, ficha, cacos, duvidas, primos, chip,
               contador, anos):
    """V1N05 e V1N06. No V1N05 o ponto 1994 marca o começo da linha do
    tempo, as interrogações voltam, o chip do V1N03 volta e vira quântico, a
    seta de volta ciano passa e as interrogações se desfazem nos dois primos
    longos; o contador despenca até "horas". No V1N06 um pulso ciano sai do
    RSA e acende os anônimos da rede um a um; a folha de papel pousa no
    1994, os primos se recolhem nele, a linha do tempo sai de dentro da
    folha e junta qubits até hoje, e segue tracejada até um "?"; quando o
    tracejado chega lá, o cadeado grande quebra, a ficha racha junto, e os
    da rede estalam em cascata.

    Recebe, além do cad, da rede e da ficha (deitada ao pé do cad), o que o
    V1N01 ao V1N03 deixaram fora de cena: os cacos do V1N02 (as
    interrogações, onde pararam), as interrogações do V1N01 (`duvidas`: só
    a _DA_FECHADURA volta), os dois primos longos, o chip cinza e o
    contador cheio, com o ValueTracker dele (`anos`, em 10).

    O ponto e o rótulo "1994" (d94, r94) nascem AQUI, no começo do V1N05, e
    são os mesmos objetos que o V1N06 usa: os primos se recolhem nele e a
    linha do tempo sai dele.

    Devolve (cacos, tempo, ficha), tudo em cena:
    - cacos: (as duas metades do arco grande, VGroup dos dez arcos
      pequenos, cad) — os arcos todos em cena, invisíveis onde caíram: o
      V1N08 os remonta no título. O `cad` ficou só com o corpo "RSA" e os
      cotos: as palavras do V1N07 saem de dentro dele. Ele e o que sobrou
      da rede também ficam em cena;
    - tempo: a linha do tempo inteira, que fica para o V1N07 — VGroup(linha,
      pontos, rótulos, qubits, tracejado), com pontos = VGroup(1994, hoje,
      "?") e rótulos = VGroup("1994", "hoje", "?"), na mesma ordem;
    - ficha: as duas metades da ficha rachada, VGroup(esquerda, direita),
      caídas ao pé do cadeado. A ficha inteira saiu de cena."""
    arestas, pontos, anonimos = malha
    fechadura = duvidas[_DA_FECHADURA]

    # a linha do tempo: de 1994 até hoje, com as colunas de qubits, e o
    # tracejado de hoje até o "?"
    x0, x1 = -2.6, 2.6
    linha = Line([x0, _LINHA, 0], [x1, _LINHA, 0], color=CINZA,
                 stroke_width=3)
    d94 = Dot([x0, _LINHA, 0], radius=0.08, color=PRETO)
    hoje = Dot([x1, _LINHA, 0], radius=0.08, color=PRETO)
    r94 = T("1994", 22, CINZA).next_to(d94, DOWN, buff=0.15)
    rhoje = T(tx("v1.hoje"), 22, CINZA).next_to(hoje, DOWN, buff=0.15)
    qubits, quando = VGroup(), []
    for f, altura in _QUBITS:
        for k in range(altura):
            qubits.add(_qubit().move_to(
                [x0 + f * (x1 - x0), _LINHA + 0.2 + 0.17 * k, 0]))
            quando.append((f, k))               # onde na linha, que andar
    tracejado = DashedLine([x1, _LINHA, 0], [_X_DUVIDA, _LINHA, 0],
                           color=CINZA, stroke_width=3, dash_length=0.14)
    duvida = Dot([_X_DUVIDA, _LINHA, 0], radius=0.08, color=PRETO)
    rduvida = T("?", 26, CINZA).next_to(duvida, DOWN, buff=0.15)
    _confere(VGroup(tracejado, duvida, rduvida), None,
             'o tracejado até o "?"')

    # a folha de "Era teoria", pousada no 1994: o ponto fica na metade de
    # baixo dela, livre dos traços, e o rótulo logo abaixo da borda (a
    # 0,08). Um tico à esquerda, para a borda direita não encostar nos
    # primos, que ainda estão ali até "últimos anos". Na ordem de desenho,
    # a linha vai por baixo da folha (sai de dentro dela) e os pontos por
    # cima de tudo (a folha some atrás do 1994)
    folha = _folha().move_to(d94.get_center() + 0.35 * UP + 0.04 * LEFT)
    folha.set_z_index(0.4)
    for m in (d94, hoje, duvida):
        m.set_z_index(0.6)

    # os dois primos longos do V1N02 — os mesmos textos, já cortados em
    # "…" — na faixa de baixo, onde o V1N06 os recolhe no ponto 1994: um
    # em cima do outro, como lá (p em cima), entre a rede e a linha do
    # tempo, alinhados à esquerda logo depois do "1994" — o ponto fica no
    # canto de baixo, à esquerda, e o recolher anda para ele. Os dois
    # acima da altura do ponto: com o q ao lado do "1994", lia-se "1994
    # 110100…" numa linha só
    p, q = primos
    for primo, dy in ((p, 0.65), (q, 0.21)):
        primo.shift([r94.get_right()[0] + 0.25 - primo.get_left()[0],
                     _LINHA + dy - primo.get_y(), 0])
        _confere(primo, None, "primo longo na faixa de baixo")

    # a seta de volta ciano (V1N05): na faixa das interrogações, saindo do
    # chip — é ele que faz a volta — até em cima do começo dos primos
    seta = Arrow([chip.get_left()[0] - 0.08, _FAIXA, 0],
                 [p.get_left()[0] + 0.1, _FAIXA, 0], buff=0, color=CIANO,
                 stroke_width=5)

    # a interrogação da fechadura volta por cima do cadeado "RSA": no vão
    # do arco, entre o topo do corpo e o alto da curva. No lugar do buraco,
    # onde agora está o rótulo, ela cobria o "S" (lia-se "R?A"). Na escala
    # de agora — no V1N01 o cadeado tinha o tamanho natural
    curva = cad[0][0]
    alto = curva.get_arc_center()[1] + np.linalg.norm(
        curva.point_from_proportion(0.5) - curva.get_arc_center())
    fechadura.scale(cad[1].width / 1.9).move_to(
        [cad[1].get_x(), (cad[1].get_top()[1] + alto) / 2, 0])
    fechadura.set_z_index(cad[1].z_index + 1)

    # o contador do V1N03, cheio, na faixa livre acima da rede; volta a
    # seguir o ValueTracker (o V1N03 tirou o updater quando ele estourou)
    onde = np.array([0.0, 3.38, 0.0])
    contador.move_to(onde)
    _confere(contador, None, "contador cheio do V1N05", margem=0.1)
    horas = T(tx("v1.horas"), 44, CIANO).move_to(onde)

    with narra(cena, "V1N05", 12.1):
        tag, est = "V1N05", 12.1
        kv = _k(tag, est)
        t0 = _agora(cena)                  # o começo da fala, o do narra

        def ate(alvo):
            return Wait(max(0.0, t0 + alvo - _agora(cena)))

        # "Em mil novecentos e noventa e quatro", o começo da fala: o ponto
        # e o rótulo 1994 aparecem onde a linha do tempo do V1N06 vai nascer
        cena.play(GrowFromCenter(d94), FadeIn(r94, shift=0.15 * UP),
                  run_time=0.5 * VEL * kv)

        # "Peter Shor" ≈ 0,23: as interrogações voltam, paradas onde caíram,
        # e a da fechadura por cima do cadeado RSA. Introducer: sem isso o
        # play poria as duas em cena, inteiras, durante o Wait
        t_shor = _em(tag, est, _f(tag, "Peter Shor"))
        cena.play(Succession(ate(t_shor), AnimationGroup(
            FadeIn(cacos), FadeIn(fechadura, scale=1.4),
            run_time=0.4 * VEL * kv), introducer=True))

        # "computador quântico" ≈ 0,38: o chip do V1N03 volta, cinza, onde
        # estava, e passa a ciano — corpo, contorno e pinos
        t_chip = _em(tag, est, _f(tag, "computador quântico"))
        cena.play(Succession(ate(t_chip),
                             FadeIn(chip, scale=0.6, run_time=0.4 * VEL * kv),
                             introducer=True))
        cena.play(chip[0].animate.set_stroke(CIANO),
                  chip[1].animate.set_fill(CIANO).set_stroke(CIANO),
                  run_time=0.6 * VEL * kv)

        # "fatorar esses números" ≈ 0,63: a seta de volta, agora ciano, sai
        # do chip e PASSA, da direita para a esquerda, rápida e sem esforço
        # como a ida do V1N01 (acelera e solta). Atrás dela, cada "?" desfaz
        # o espalhar do V1N02 de trás para frente — começa no quadro em que
        # a ponta passa pelo lugar onde ele nasceu (os dois que nasceram à
        # direita do chip começam com a seta)...
        t_vence = _em(tag, est, _f(tag, "fatorar esses números"))
        corre = 0.5 * VEL * kv
        rf = rate_functions.ease_in_out_cubic
        xs, xe = seta.get_start()[0], seta.get_end()[0]
        a_ = np.linspace(0, 1, 201)
        frac_ = np.array([rf(a) for a in a_])
        espera = max(0.0, t0 + t_vence - _agora(cena))
        volta = []
        for c, (dx, dy, ang) in zip(cacos, _ESPALHA):
            # x onde ele nasceu, na linha da seta (o espalhar ao contrário)
            x_nasceu = c.get_x() - dx
            passa = float(np.interp((x_nasceu - xs) / (xe - xs), frac_, a_))
            volta.append(Succession(
                Wait(espera + passa * corre),
                c.animate(run_time=0.3 * VEL * kv)
                 .rotate(-ang * DEGREES).shift([-dx, -dy, 0])))
        cena.play(Succession(Wait(espera),
                             GrowArrow(seta, run_time=corre, rate_func=rf),
                             introducer=True),
                  *volta)
        # ...e a volta que era impossível acontece: as interrogações viram
        # os dois primos longos — as da esquerda e a da fechadura o p, as da
        # direita o q (elas nasceram da direita para a esquerda) —, na faixa
        # de baixo, e a seta, que já passou, apaga. É o momento-chave do
        # vídeo: a volta que o V1N02 chamou de impossível se faz no instante
        # em que a fala diz que ela é possível. A seta parte NA âncora e o
        # Transform roda de +0,5 a +1,1 s × kv dela (8,1 a 8,7 s de 12,1) —
        # dentro de "fatorar esses números", antes de "em horas" ≈ 0,77.
        # Os "?" saem da cena um a um antes (o espalhar e o desfazer os
        # penduraram em Groups da cena, e um "?" que sobrasse em algum deles
        # ficaria em cena, deformado no primo, por cima do recolher do V1N06)
        cena.remove(*cacos, fechadura)
        cena.play(ReplacementTransform(VGroup(*cacos[4:], fechadura), p),
                  ReplacementTransform(VGroup(*cacos[:4]), q),
                  FadeOut(seta), run_time=0.6 * VEL * kv)

        # "em horas ou dias" ≈ 0,77: o contador do V1N03 volta cheio e
        # despenca — os anos caem acelerando, e ele encolhe com eles — até
        # virar "horas", em ciano, que fica até o fim da fala — com o chip
        # ciano, que só sai no começo do V1N06. O bloco tem 1,75 s × kv e
        # leva um teto, como o "bilhões" do V1N03: tem de acabar 0,1 s antes
        # do fim da fala (hoje a palavra manda: teto a 0,84 da fala)
        t_horas = min(_em(tag, est, _f(tag, "horas ou dias")),
                      _dur(tag, est) - 1.75 * VEL * kv - 0.1)
        contador.add_updater(lambda m: m.become(
            T(_anos(anos.get_value()), 44)
            .scale(1 + anos.get_value() / 10).move_to(onde)))
        cena.play(Succession(ate(t_horas),
                             FadeIn(contador, run_time=0.3 * VEL * kv),
                             introducer=True))
        cena.play(anos.animate.set_value(1), rate_func=rush_into,
                  run_time=1.0 * VEL * kv)
        contador.clear_updaters()
        cena.play(ReplacementTransform(contador, horas),
                  run_time=0.45 * VEL * kv)

    with narra(cena, "V1N06", 12.1):
        tag, est = "V1N06", 12.1
        kv = _k(tag, est)
        t0 = _agora(cena)                  # o começo da fala, o do narra

        def falta(alvo):
            """Quanto falta, de agora, para `alvo` (s da fala): o Wait de
            uma âncora, montado logo antes do play. Lê o relógio, então não
            depende de somar à mão o que já passou (em -ql cada play
            arredonda para quadros inteiros)."""
            return max(0.0, t0 + alvo - _agora(cena))

        # "não serve só para o RSA" ≈ 0,08: um pulso ciano sai do corpo do
        # RSA (por baixo dele: o cad está no z 1), desce até o nó mais perto
        # e corre por todas as arestas (_frente). Cada anônimo acende por
        # inteiro quando o pulso passa pelo meio da aresta dele (o arco pelo
        # traço: um fill no arco tamparia a aresta atrás dele). O
        # there_and_back vai em cada um, não no grupo: o finish() do grupo
        # leva cada animação ao fim dela, e eles ficariam acesos. Os
        # pontinhos saem do relógio do play: cada um anda o seu trecho e some
        # no fim dele — no nó, de onde outros partem, ou no encontro com o
        # que veio da outra ponta.
        # Tudo acaba antes de "Era teoria": a frente leva 1,3 s × kv até o
        # último encontro, e o último anônimo acende antes disso (o meio da
        # aresta de cima fica a 0,9 do caminho) e brilha 0,8 s × kv — hoje
        # 0,93 + 0,9 × 1,3 + 0,8 = 2,90 s, contra 3,07 de "Era teoria".
        # Numa gravação em que as duas palavras fiquem mais perto, é a
        # janela entre elas que manda, e a frente corre mais depressa.
        # O chip ciano e o "horas" do V1N05 saem logo no começo, no mesmo
        # play
        t_pisca = _em(tag, est, _f(tag, "não serve só para o RSA"))
        t_teoria = _em(tag, est, _f(tag, "Era teoria"))
        acende = 0.8 * VEL * kv
        trechos, meios = _frente(arestas, pontos, cad[1].get_center())
        d_fim, d_meio = max(t[3] for t in trechos), max(meios)
        janela = t_teoria - t_pisca
        corre = max(0.4 * VEL * kv,
                    min(1.3 * VEL * kv, janela,
                        (janela - acende) * d_fim / d_meio))
        vel = d_fim / corre
        espera = falta(t_pisca)
        pingos = VGroup(*[Dot(de, radius=0.075, color=CIANO)
                          for de, *_ in trechos])
        pingos.set_opacity(0).set_z_index(0.5)

        def anda(g, a, total=espera + corre):
            d = vel * (a * total - espera)
            for pingo, (de, para, d0, d1) in zip(g, trechos):
                f = (d - d0) / (d1 - d0)
                pingo.move_to(de + min(max(f, 0.0), 1.0) * (para - de))
                pingo.set_opacity(1.0 if 0.0 < f <= 1.0 else 0.0)

        pisca = dict(rate_func=there_and_back)
        cena.play(
            UpdateFromAlphaFunc(pingos, anda, run_time=espera + corre,
                                rate_func=linear),
            *[Succession(Wait(espera + m / vel), AnimationGroup(
                c[1].animate(**pisca).set_opacity(1),
                c[0].animate(**pisca).set_stroke(opacity=1),
                run_time=acende))
              for c, m in zip(anonimos, meios)],
            FadeOut(horas, run_time=0.4 * VEL * kv),
            FadeOut(chip, scale=0.6, run_time=0.4 * VEL * kv))
        cena.remove(pingos)

        # "Era teoria" ≈ 0,25: a folha de papel pousa no 1994
        cena.play(Succession(
            Wait(falta(t_teoria)),
            FadeIn(folha, shift=0.15 * DOWN, run_time=0.5 * VEL * kv),
            introducer=True))

        # "nos últimos anos" ≈ 0,39: os primos longos se recolhem no ponto
        # de 1994, que já está em cena desde o V1N05... (glifo a glifo, cada
        # um numa cópia do ponto: do Text inteiro para o Dot, os glifos
        # sumiam no lugar em vez de viajar. São 37 glifos, contando os "…").
        # Vão na altura do ponto, por cima da folha: pousam nele à vista
        t_anos = _em(tag, est, _f(tag, "últimos anos"))
        p.set_z_index(d94.z_index)
        q.set_z_index(d94.z_index)
        copias = [d94.copy() for _ in range(len(p) + len(q))]
        cena.play(Succession(
            Wait(falta(t_anos)),
            AnimationGroup(
                *[ReplacementTransform(g, d)
                  for g, d in zip([*p, *q], copias)],
                run_time=0.8 * VEL * kv)))
        cena.remove(*copias)

        # O teto. "Prazo de validade" ≈ 0,87 (10,6 s de 12,1), mas o rabo do
        # bloco não cabe atrás dela. O rabo é tudo do alvo7 em diante:
        # crescer 0,6 + rachar 0,25 + quebrar 1,4 + estalar a rede 0,5 × (1 +
        # 9 × 0,12) = 1,04 (dez estalos em LaggedStart) — 3,29 s × kv, os
        # mesmos de antes do redesenho, e que não podem crescer: a ficha racha
        # DENTRO dos três plays do quebrar() (_nos_plays, sem play próprio), e
        # a linha do tempo não sai mais no crescer (fica para o V1N07). O
        # alvo7 é o começo do crescer, capado no último instante que ainda
        # fecha o bloco dentro da fala: kv × (12,1 − 3,29) − 0,1 = 8,71 s
        # (fração efetiva ≈0,72, em cima de "e talvez", 0,718) — a quebra
        # corre por cima de "a aposta tenha prazo de validade". O 0,1 s sem
        # kv é o arredondamento de cada play a quadros inteiros, que em -qh
        # empurrava o fim 0,07 s além da fala.
        # O rachar() começa em t_racha = alvo7 + 0,6 = 9,31 s, e o tracejado
        # chega ao "?" nesse instante: o fim dele é sempre o t_racha, então
        # ele nunca empurra o teto. Quem se mexe é o começo: em "talvez"
        # (8,69 s), se dali ao t_racha couber o 1,0 s × kv dele; senão mais
        # cedo, quando "hoje" acaba de acender — a linha sai do recolher em
        # 5,57 s, corre 2,1 s até hoje e o ponto termina de acender 0,2 s
        # depois, em 7,87 s. Hoje só sobram 0,62 s depois de "talvez": ele
        # parte de hoje e corre 1,44 s, e o "?" acende na palavra, com o
        # tracejado já a caminho. A linha (o último qubit da coluna de 6 em
        # 8,06 s) termina antes do teto. Numa gravação em que nem a partir de
        # hoje caibam 0,3 s, ele parte antes de hoje acender — o teto, nunca
        t_papel = _em(tag, est, _f(tag, "saindo do papel"))
        t_talvez = _em(tag, est, _f(tag, "talvez"))
        varre = 2.1 * VEL * kv                  # a linha vai de 1994 a hoje
        cresce = 0.6 * VEL * kv
        traca = 1.0 * VEL * kv                  # o tracejado, quando cabe
        aparece = 0.4 * VEL * kv                # o ponto "?"
        alvo7 = min(_em(tag, est, _f(tag, "prazo de validade")),
                    kv * (est - 3.29) - 0.1)
        t_racha = alvo7 + cresce
        t_hoje = _agora(cena) - t0 + varre + 0.2 * VEL * kv
        t_traco = t_talvez if t_racha - t_talvez >= traca else t_hoje
        t_traco = min(t_traco, t_racha - 0.3 * VEL * kv)
        t_duvida = min(max(t_talvez, t_traco), t_racha - aparece)
        maior = cad.copy().scale(1.2 / 0.8)

        # ...e a linha sai de dentro da folha e corre até hoje; cada qubit
        # nasce quando ela passa, e a coluna sobe um andar de cada vez. No
        # mesmo play, cada gesto na sua palavra: em "saindo do papel" a folha
        # encolhe e some atrás do 1994; o tracejado de hoje ao "?", e o "?"
        # em "talvez"; no alvo7 o cadeado volta a crescer no centro, e a
        # ficha vai junto, para o pé dele (sem isso o corpo maior a cobria).
        # O play acaba no t_racha, com o tracejado no "?"
        cena.play(
            Create(linha, rate_func=linear, run_time=varre),
            *[Succession(Wait(f * varre + 0.05 * k * VEL * kv),
                         GrowFromCenter(u, run_time=0.25 * VEL * kv))
              for u, (f, k) in zip(qubits, quando)],
            Succession(Wait(varre - 0.2 * VEL * kv), AnimationGroup(
                GrowFromCenter(hoje), FadeIn(rhoje, shift=0.15 * UP),
                run_time=0.4 * VEL * kv)),
            Succession(Wait(falta(t_papel)), FadeOut(
                folha, scale=0.05, target_position=d94.get_center(),
                run_time=0.5 * VEL * kv)),
            Succession(Wait(falta(t_traco)), Create(
                tracejado, rate_func=linear, run_time=t_racha - t_traco),
                introducer=True),
            Succession(Wait(falta(t_duvida)), AnimationGroup(
                GrowFromCenter(duvida), FadeIn(rduvida, shift=0.15 * UP),
                run_time=aparece), introducer=True),
            Succession(Wait(falta(alvo7)), AnimationGroup(
                cad.animate.scale(1.2 / 0.8),
                ficha.animate.move_to(_pe(maior)), run_time=cresce)))

        # o z_index do V1N04 punha o cadeado na frente da rede; mas a fissura
        # do rachar() e as corridas do quebrar() nascem no z 0, e ficariam
        # POR BAIXO do traço do arco. Volta ao 0 e vai para a frente pela
        # ordem da cena
        cad.set_z_index(0)
        cena.bring_to_front(cad)
        # e quebra, num gesto só: a rachadura mal aparece e já corre até as
        # pontas. A ficha racha junto, dentro dos três plays do quebrar(): a
        # fenda corre por ela enquanto a fissura corre pelo arco; no estalo
        # ela dá lugar às duas metades, que se apartam um dedo; e as metades
        # caem com os pedaços do arco, girando para fora — mas ficam à vista,
        # ao pé do cadeado: são a ficha rachada que o V1N08 recolhe. Caem
        # pouco: o espaço ao pé do cadeado é curto, entre o corpo crescido à
        # direita e o anônimo de baixo, à esquerda
        rachar(cena, cad, run_time=0.25 * kv)
        fenda, metades = _racha_ficha(ficha)
        lados = (LEFT, RIGHT)

        def parte():
            cena.remove(ficha, fenda)
            cena.add(metades)
            return [m.animate.shift(0.06 * lado)
                    for m, lado in zip(metades, lados)]

        def caem():
            return [m.animate.shift(0.12 * DOWN + 0.16 * lado)
                    .rotate(-lado[0] * 18 * DEGREES)
                    for m, lado in zip(metades, lados)]

        pecas = _nos_plays(cena, {0: lambda: [Create(fenda)], 1: parte,
                                  2: caem},
                           quebrar, cad, run_time=1.4 * kv)

        # os anônimos estalam em cascata, do centro para fora — o quebrar()
        # já passou ~0,75 s do estalo, a folga do "meio segundo depois"
        ordem = sorted(anonimos,
                       key=lambda c: np.linalg.norm(c.get_center()
                                                    - cad[1].get_center()))
        estalos = [_estalar_rede(cena, c, run_time=0.5 * kv) for c in ordem]
        # é o último gesto da fala: o teto do alvo7 deixa 0,1 s para o
        # arredondamento dos plays a quadros inteiros, que em -ql (15 fps)
        # não basta (a folga dava −0,10 s em pt, −0,07 em inglês). A
        # cascata encurta para o que ainda cabe — nunca para menos da metade
        cascata = LaggedStart(*[a for a, _ in estalos], lag_ratio=0.12)
        cena.play(cascata, run_time=max(0.5 * cascata.run_time,
                                        min(cascata.run_time,
                                            _resta(cena, t0, tag, est))))

    return ((pecas, VGroup(*[arco for _, arco in estalos]), cad),
            VGroup(linha, VGroup(d94, hoje, duvida),
                   VGroup(r94, rhoje, rduvida), qubits, tracejado),
            metades)


def corpo_serie(cena, cacos, tempo, ficha, rotulos):
    """V1N07, V1N08 e V1N09. No V1N07, o que a quebra expõe: as três
    palavras do V1N01 saem de dentro do corpo "RSA" (`cad`, que vem junto
    com os cacos), cada uma com um cadeado mini fechado ao lado, e os três
    cadeados abrem; a coluna de qubits de "hoje" alcança as palavras; um
    pacote do V1N00 para acima de "hoje" e solta ali uma cópia, que anda
    pelo tracejado até o "?" e é aberta lá. No V1N08 os cacos do V1N06 sobem
    e se remontam no título da série, o "Shor" dele pisca em ciano, e os
    quatro rótulos do V1N04 voltam em volta dele e viram os quatro vídeos,
    apagados; no V1N09 eles se organizam na trilha, onde o 1 acende.

    `tempo` é a linha do tempo do V1N06, inteira e em cena — VGroup(linha,
    pontos, rótulos, qubits, tracejado), com pontos = VGroup(1994, hoje,
    "?") e rótulos na mesma ordem: os qubits de "hoje" e o tracejado até o
    "?" são do V1N07. Ela não sai à parte: o V1N08 recolhe tudo o que não é
    caco, e ela vai junto — como a `ficha` (as duas metades da rachada, em
    cena), que vem só para o pacote do V1N07 passar por baixo dela.

    `rotulos` são os quatro do V1N04 — VGroup(p·q, mod n, φ(n), e·d), fora
    de cena, como o corpo_rsa os devolveu.

    Devolve (título, trilha, marca), tudo em cena: o V1N10 acende o 2."""
    pecas, arcos, cad = cacos
    _, pontos, _, qubits, _ = tempo
    hoje, duvida = pontos[1], pontos[2]
    # a coluna de "hoje": a última das _QUBITS, a mais alta, que fecha o
    # VGroup dos qubits
    coluna = qubits[-_QUBITS[-1][1]:]

    # o título da série, montado já aqui: as palavras do V1N07 não podem
    # encostar nele
    titulo = T(_TITULO, 42)

    # as três palavras do V1N01, os mesmos textos no mesmo tamanho, cada uma
    # com um cadeado mini fechado à esquerda: a primeira no canto de cima à
    # esquerda, a segunda no alto, no meio, a terceira no canto de cima à
    # direita (_ALTO_MEIO, _ALTO_LADOS). Partem pequenas e transparentes do
    # miolo do corpo, o caminho inverso do condensar do V1N01
    palavras = VGroup()
    for chave in ("v1.contas_bancarias", "v1.compras_online",
                  "v1.mensagens_privadas"):
        # (a 0,22: aberto, o arco gira para a direita, rumo à palavra)
        palavras.add(VGroup(_mini(cadeado()), T(tx(chave), 30))
                     .arrange(RIGHT, buff=0.22))
    palavras[0].to_edge(LEFT, buff=0.6).set_y(_ALTO_LADOS)
    palavras[1].move_to([0, _ALTO_MEIO, 0])
    palavras[2].to_edge(RIGHT, buff=0.6).set_y(_ALTO_LADOS)
    for g in palavras:
        _confere(g, None, "palavra do V1N07")
        folga = g.get_bottom()[1] - titulo.get_top()[1]
        if folga < 0.3:
            logger.warning("corpo_serie: palavra do V1N07 encosta no título "
                           "(folga %.2f)", folga)
        g.save_state()
        g.scale(0.05).move_to(cad[1]).set_opacity(0)

    # os traços de "quem tiver a máquina": do alto da coluna de "hoje" até o
    # pé de cada palavra. Por trás de tudo (z −0,1): o da esquerda passa
    # pelo corpo "RSA", e por cima dele riscava as letras
    raiz = coluna[-1].get_top()
    tracos = VGroup(*[Line(raiz, g.saved_state.get_bottom() + 0.08 * DOWN,
                           color=CIANO, stroke_width=2)
                      for g in palavras]).set_z_index(-0.1)
    for u in coluna:
        u.save_state()

    # o pacote de "gravado hoje": o do V1N00 — um envelope com um cadeado
    # mini fechado em cima —, na escala _PACOTE. Entra pela esquerda POR
    # BAIXO do corpo e das metades da ficha e só sobe no fim, para passar por
    # cima da coluna de "hoje" e parar acima do ponto. Na frente da linha do
    # tempo (os pontos dela estão no z 0,6): a cópia cobre o ponto em que
    # pousa
    pacote = _mini(_pacote(cadeado()), _PACOTE).set_z_index(0.7)
    env = pacote[0]
    meia = env.width / 2
    topo = pacote.get_top()[1] - env.get_y()     # do envelope ao alto do arco
    y_baixo = min(cad[1].get_bottom()[1], ficha.get_bottom()[1]) - 0.08 - topo
    y_alto = coluna.get_top()[1] + 0.06 + env.height / 2
    x_ini = -config.frame_width / 2 - meia - 0.1
    # em cima do ponto "hoje" — um tico à direita dele, se for preciso para
    # o envelope não encostar na coluna, que fica logo à esquerda; ele cobre
    # o ponto do mesmo jeito
    x_pouso = max(hoje.get_x(), coluna.get_right()[0] + 0.05 + meia)
    x_fora = config.frame_width / 2 + meia + 0.1
    # a subida: de x_a em diante o pacote já passou do corpo; em x_b ele tem
    # de estar no alto, antes de a borda do envelope chegar à coluna
    x_a = cad[1].get_right()[0] + meia + 0.05
    x_b = coluna.get_left()[0] - meia - 0.03

    def altura(x):
        return y_baixo + (y_alto - y_baixo) * smooth(
            float(np.clip((x - x_a) / (x_b - x_a), 0, 1)))

    pacote.shift([x_ini, y_baixo, 0] - env.get_center())
    _confere(pacote.copy().shift([x_pouso - x_ini, y_alto - y_baixo, 0]),
             None, "pacote acima de hoje")
    _confere(pacote.copy().shift([duvida.get_x() - x_ini,
                                  duvida.get_y() - y_baixo, 0]),
             None, 'pacote no "?"')

    # o título, letra a letra. O "S" de Shor nasce das duas metades do arco
    # grande; as outras 30 letras, de três em três, dos dez arcos pequenos —
    # Arc, perna esquerda e perna direita, nessa ordem —, com os arcos da
    # esquerda indo para as letras da esquerda
    letras = "".join(_TITULO.split())     # o Text não tem glifo de espaço
    i_s = letras.index("S")
    resto = [g for i, g in enumerate(titulo) if i != i_s]
    trincas = [VGroup(*resto[k:k + 3]) for k in range(0, len(resto), 3)]
    assert len(trincas) == len(arcos), "o título não fecha com os cacos"
    pares = [(pecas, VGroup(titulo[i_s], titulo[i_s].copy()))]
    pares += zip(sorted(arcos, key=lambda a: a.get_x()), trincas)
    pares.sort(key=lambda par: par[1].get_x())
    # a palavra "Shor" do título, que pisca em ciano no V1N08
    i_shor = letras.index("Shor")
    shor = VGroup(*titulo[i_shor:i_shor + len("Shor")])

    # os quatro vídeos, apagados, dois acima e dois abaixo do título — no
    # tamanho da trilha, para o V1N09 só os deslocar. Nascem dos quatro
    # rótulos do V1N04, que reaparecem cada um no lugar de um deles, na
    # ordem dos dois (p·q → 1, mod n → 2, φ(n) → 3, e·d → 4)
    nomes = VGroup(*[T(v, 26) for v in VIDEOS]).set_opacity(0.25)
    for nome, rotulo, (x, y) in zip(nomes, rotulos,
                                    ((-3.3, 1.5), (3.3, 1.5),
                                     (-3.3, -1.5), (3.3, -1.5))):
        nome.move_to([x, y, 0])
        rotulo.move_to(nome)

    # a trilha já no lugar final, com o 1 aceso; ela nasce apagada e o 1
    # acende depois, então o estado aceso fica guardado
    trilha = trilha_videos(acesos=(1,)).to_edge(LEFT, buff=1.3)
    trilha[0].save_state()
    trilha[0].set_opacity(0.25)
    # "você está aqui": um triângulo ao lado do 1
    marca = (Triangle().set_fill(LARANJA, opacity=1).set_stroke(width=0)
             .rotate(-90 * DEGREES).scale_to_fit_height(0.2)
             .next_to(trilha[0], LEFT, buff=0.3))

    with narra(cena, "V1N07", 11.2):
        tag, est = "V1N07", 11.2
        k = _k(tag, est)
        t0 = _agora(cena)                  # o começo da fala, o do narra

        def falta(alvo):
            """O Wait de uma âncora, montado logo antes do play: lê o
            relógio, como no V1N06."""
            return max(0.0, t0 + alvo - _agora(cena))

        # os tetos, do fim para o começo. O último gesto — o cadeado da
        # cópia estala e a aba abre, 0,6 s × k — tem de acabar 0,1 s antes
        # do fim da fala: "aberto depois" ≈ 0,91 leva um teto (hoje a palavra
        # manda: o teto cai a 0,94). A cópia chega ao "?" exatamente nele, e
        # o trecho de "gravado hoje" até lá — o pacote entra 0,8, a cópia
        # desce 0,35 e anda 0,55 — leva outro: hoje a palavra manda, com
        # 0,08 s de folga, que a cópia passa parada em "hoje"
        entra, desce, viaja = 0.8 * VEL * k, 0.35 * VEL * k, 0.55 * VEL * k
        t_aberto = min(_em(tag, est, _f(tag, "aberto depois")),
                       _dur(tag, est) - 0.6 * VEL * k - 0.1)
        t_gravado = min(_em(tag, est, _f(tag, "gravado hoje")),
                        t_aberto - (entra + desce + viaja))

        # "contas bancárias" ≈ 0,07: as palavras saem de dentro do corpo
        # "RSA", cada uma com o seu cadeado, e se espalham, uma atrás da
        # outra. Entram na cena já (invisíveis no miolo do corpo), para o
        # Succession não as embrulhar num Group
        cena.add(*palavras)
        cena.play(Succession(
            Wait(falta(_em(tag, est, _f(tag, "contas bancárias")))),
            LaggedStart(*[Restore(g) for g in palavras], lag_ratio=0.3,
                        run_time=1.9 * VEL * k)))

        # "ficam abertas" ≈ 0,41: os três cadeados abrem em cascata — o
        # Rotate do abrir(), com o mesmo pivô, num LaggedStart só
        cena.play(Succession(
            Wait(falta(_em(tag, est, _f(tag, "ficam abertas")))),
            LaggedStart(*[Rotate(g[0][0], _ABERTURA,
                                 about_point=g[0][0][2].get_bottom())
                          for g in palavras], lag_ratio=0.35,
                        run_time=0.9 * VEL * k)))

        # "quem tiver a máquina" ≈ 0,54: a coluna de qubits de "hoje"
        # acende — cheia e um pouco maior —, os traços cianos correm dela
        # até as três palavras e se apagam logo, com a coluna voltando ao
        # que era (1,25 s × k, bem antes de "gravado hoje")
        cena.play(Succession(
            Wait(falta(_em(tag, est, _f(tag, "quem tiver a máquina")))),
            AnimationGroup(*[u.animate.scale(1.3).set_fill(opacity=1)
                             for u in coluna], run_time=0.3 * VEL * k)))
        cena.play(LaggedStart(*[Create(t) for t in tracos], lag_ratio=0.2),
                  run_time=0.5 * VEL * k)
        cena.play(FadeOut(tracos), *[Restore(u) for u in coluna],
                  run_time=0.45 * VEL * k)

        # "gravado hoje" ≈ 0,75: o pacote entra pela esquerda, desacelerando,
        # e para acima de "hoje" (durante o Wait ele está fora do quadro)
        def x_de(a):
            return x_ini + (x_pouso - x_ini) * rate_functions.ease_out_cubic(a)

        cena.play(Succession(
            Wait(falta(t_gravado)),
            _trajeto(pacote, lambda a: np.array(
                [x_de(a) - x_ini, altura(x_de(a)) - y_baixo, 0.0]), entra)))

        # uma cópia se solta e desce até o ponto "hoje", espera ali e anda
        # pelo tracejado até o "?" — chega nele no t_aberto, lido no relógio.
        # O original segue, no mesmo play, e sai pela direita. A aba da cópia
        # ganha o preenchimento do envelope e vai para a frente do cadeado:
        # aberta, ela sobe por cima do corpo dele, e atrás dele o V sumia
        copia = pacote.copy()
        copia[0][1].set_fill(CAIXA, opacity=1).set_z_index(0.8)
        cena.add(copia)
        total = max(desce + viaja, t0 + t_aberto - _agora(cena))
        sai = total - viaja                      # quando ela deixa "hoje"
        queda = (hoje.get_y() - y_alto) * UP
        anda = (duvida.get_x() - x_pouso) * RIGHT

        def caminho(a):
            t = a * total
            return (smooth(min(t / desce, 1.0)) * queda
                    + smooth(float(np.clip((t - sai) / viaja, 0, 1))) * anda)

        cena.play(_trajeto(copia, caminho, total),
                  _trajeto(pacote, lambda a: rush_into(a) * (x_fora - x_pouso)
                           * RIGHT, total))
        cena.remove(pacote)

        # "aberto depois" ≈ 0,91: o cadeado mini da cópia estala — o gesto
        # do _estalar_rede, sem fissura — e, com o arco no ar, a aba abre: o
        # Rotate em volta da dobra, a reta entre as duas pontas dela
        estalo, _ = _estalar_rede(cena, copia[1], run_time=0.5 * k)
        aba = copia[0][1]
        dobra = (aba.get_start() + aba.get_end()) / 2
        cena.play(estalo, Succession(
            Wait(0.2 * VEL * k),
            Rotate(aba, PI, axis=RIGHT, about_point=dobra,
                   run_time=0.4 * VEL * k)))

    with narra(cena, "V1N08", 8.3):
        tag, est = "V1N08", 8.3
        k = _k(tag, est)
        t0 = _agora(cena)                  # o começo da fala, o do narra

        def falta(alvo):
            return max(0.0, t0 + alvo - _agora(cena))

        # "Essa é a promessa", o começo da fala: os cacos reacendem onde
        # caíram (pelo traço, como no V4N03) e tudo o mais sai: as palavras
        # com os cadeados mini, a cópia do pacote, a linha do tempo, as
        # metades da ficha, o corpo "RSA", as arestas, os pontos, os corpos
        # pequenos — tudo o que está em cena menos os cacos. Até aqui eles
        # não foram tocados. Reacendem já de traço fino: o traço vira
        # preenchimento no caminho até a letra, e um traço grosso passava
        # por um borrão
        cena.bring_to_front(pecas)
        restos = [m for m in cena.mobjects
                  if m is not pecas and all(m is not a for a in arcos)]
        cena.play(*[FadeOut(m) for m in restos],
                  pecas.animate.set_stroke(opacity=1, width=2.5),
                  arcos.animate.set_stroke(opacity=1, width=2.5),
                  run_time=0.6 * VEL * k)
        # "a promessa, ou a ameaça, do algoritmo de Shor": sobem e viram as
        # letras, da esquerda para a direita
        cena.play(LaggedStart(*[ReplacementTransform(c, a) for c, a in pares],
                              lag_ratio=0.08), run_time=2.4 * VEL * k)
        # as letras entraram soltas; o título volta a ser um só
        cena.remove(*[a for _, a in pares])
        cena.add(titulo)
        # "algoritmo de Shor" ≈ 0,35: "Shor" pisca uma vez em ciano — vai à
        # cor e volta. As letras só acabam de subir 3,0 s × k depois do
        # começo (2,24 s no DUR de hoje, logo depois da palavra, em 2,17): o
        # pisca sai atrás delas, ainda em cima de "Shor"
        cena.play(Succession(
            Wait(falta(_em(tag, est, _f(tag, "algoritmo de Shor")))),
            shor.animate(rate_func=there_and_back, run_time=0.8 * VEL * k)
                .set_color(CIANO)))
        # "esta série" ≈ 0,75: os quatro rótulos do V1N04 reaparecem em
        # volta do título, cada um onde um dos vídeos vai ficar, e viram o
        # nome dele, apagado. Teto: os 0,9 s × k têm de acabar 0,1 s antes do
        # fim da fala (hoje a palavra manda: o teto cai a 0,88). Os rótulos
        # entram num play introducer (sem isso ficariam à vista no Wait) e
        # viram os nomes no seguinte
        aparece, vira = 0.35 * VEL * k, 0.55 * VEL * k
        t_serie = min(_em(tag, est, _f(tag, "esta série")),
                      _dur(tag, est) - (aparece + vira) - 0.1)
        cena.play(Succession(
            Wait(falta(t_serie)),
            AnimationGroup(*[FadeIn(r, scale=0.6) for r in rotulos],
                           run_time=aparece), introducer=True))
        cena.play(*[ReplacementTransform(r, n) for r, n in zip(rotulos, nomes)],
                  run_time=vira)

    with narra(cena, "V1N09", 8.3):
        tag, est = "V1N09", 8.3
        k = _k(tag, est)
        # "são quatro vídeos": o título sobe e os quatro se enfileiram na
        # trilha, num bloco só; os números entram na frente de cada um
        cena.play(titulo.animate.scale(0.6).to_edge(UP, buff=0.5),
                  *[ReplacementTransform(n, linha[1])
                    for n, linha in zip(nomes, trilha)],
                  run_time=1.6 * VEL * k)
        cena.play(LaggedStart(*[FadeIn(linha[0], shift=0.2 * RIGHT)
                                for linha in trilha], lag_ratio=0.3),
                  run_time=0.8 * VEL * k)
        for linha in trilha:
            cena.remove(*linha)
        cena.add(trilha)
        # "neles eu passo por cada peça" ≈ 0,26 da fala, mas é o ÚLTIMO
        # gesto do bloco — preso a essa fração, o quadro ficaria parado por
        # quase 60% da fala (o resto da frase, "para entender como se chega
        # nesse algoritmo", não tem contrapartida visual). Empurrado para o
        # piso de 85% em vez de concentrado no início, como pede a regra de
        # distribuir gestos soltos ao longo da fala
        alvo = max(_em(tag, est, _f(tag, "neles eu passo")),
                   0.85 * _dur(tag, est) - 0.8 * VEL * k)
        cena.play(Succession(Wait(max(0.0, alvo - k * 2.4)), AnimationGroup(
            Restore(trilha[0]), GrowFromCenter(marca),
            run_time=0.8 * VEL * k)))

    return titulo, trilha, marca


def _abre_janela(cena, titulo, trilha, i, k, some=(), rotulo=None):
    """Abre a prévia do vídeo i + 1 — a MESMA nas três aberturas (V1N10,
    V1N11, V1N13): o item i da trilha acende e os outros saem (junto com
    `some`, a marca do V1N09), ele sobe para o topo e a moldura nasce de
    uma linha que sai do pé dele e se expande. Só então o conteúdo começa.

    0,80 s × k: acende 0,15 · sobe 0,30 · linha 0,15 · expande 0,20.

    `rotulo`, quando dado (o "Fermat" do V1N11), entra no canto superior-
    esquerdo da moldura junto com a expansão. A moldura passa por _confere
    contra o quadro, e ela e o rótulo não podem encostar no título que
    subiu. Devolve (moldura, rotulo_ou_None)."""
    item = trilha[i]
    outros = [linha for j, linha in enumerate(trilha) if j != i]
    moldura = RoundedRectangle(width=_JANELA_LARGURA, height=_JANELA_ALTURA,
                               corner_radius=0.15, color=CINZA,
                               stroke_width=2)
    moldura.move_to(_JANELA_CENTRO)
    _confere(moldura, None, "janela")
    rot = None
    if rotulo is not None:
        rot = T(rotulo, 24, LARANJA)
        rot.next_to(moldura, UP, buff=0.15).align_to(moldura, LEFT)

    cena.play(item.animate.set_opacity(1),
              *[FadeOut(m) for m in (*outros, *some)],
              run_time=0.15 * VEL * k)
    cena.play(item.animate.scale(0.85).next_to(titulo, DOWN, buff=0.35)
                  .to_edge(LEFT, buff=0.8),
              run_time=0.30 * VEL * k)
    for nome, peca in (("janela", moldura), ("rótulo da janela", rot)):
        if peca is None:
            continue
        folga = item.get_bottom()[1] - peca.get_top()[1]
        if folga < 0.15:
            logger.warning("_abre_janela: %s encosta no título (folga %.2f)",
                           nome, folga)

    # a linha é a própria moldura achatada: sai do pé do título e, aberta,
    # já é a moldura, sem troca de forma no meio
    linha = moldura.copy().stretch_to_fit_height(1e-3)
    cena.play(GrowFromPoint(linha, item.get_bottom()), run_time=0.15 * VEL * k)
    entra = [ReplacementTransform(linha, moldura)]
    if rot is not None:
        entra.append(FadeIn(rot, shift=0.15 * DOWN))
    cena.play(*entra, run_time=0.20 * VEL * k)
    return moldura, rot


def _fecha_janela(cena, titulo, trilha, i, moldura, k):
    """Fecha a prévia do vídeo i + 1 — o avesso da _abre_janela: tudo o que
    está em cena além do título da série, do item i e da moldura sai (o
    conteúdo e o rótulo), a moldura colapsa até virar uma linha, a linha
    recolhe no pé do título e o título volta para o seu lugar na trilha,
    que reaparece inteira apagada.

    0,75 s × k: conteúdo sai 0,15 · colapsa 0,20 · recolhe 0,15 ·
    volta 0,25. Deixa a `trilha` em cena como um VGroup só, como o V1N09 a
    deixou, e `trilha[i]` continua sendo o mesmo objeto."""
    item = trilha[i]
    outros = [linha for j, linha in enumerate(trilha) if j != i]
    fixos = {id(s) for m in (titulo, item, moldura) for s in m.get_family()}
    conteudo = [m for m in cena.mobjects if id(m) not in fixos]
    # pelas folhas: cena.mobjects também guarda os Group dos LaggedStart,
    # que não têm set_opacity e não esmaeceriam
    folhas = {id(s): s for m in conteudo
              for s in m.family_members_with_points()
              if id(s) not in fixos and isinstance(s, VMobject)}
    if folhas:
        cena.play(FadeOut(VGroup(*folhas.values())), run_time=0.15 * VEL * k)
    cena.remove(*conteudo)

    cena.play(moldura.animate.stretch_to_fit_height(1e-3),
              run_time=0.20 * VEL * k)
    cena.play(moldura.animate.stretch_to_fit_width(1e-3)
                  .move_to(item.get_bottom()),
              run_time=0.15 * VEL * k)
    cena.remove(moldura)

    # o lugar do item na trilha, recalculado numa trilha nova (a mesma
    # to_edge do V1N09; trilha_videos já a devolve apagada)
    casa = trilha_videos().to_edge(LEFT, buff=1.3)[i]
    for linha in outros:
        linha.set_opacity(0.25)
    cena.play(Transform(item, casa),
              *[FadeIn(linha) for linha in outros],
              run_time=0.25 * VEL * k)
    cena.remove(*trilha)
    cena.add(trilha)


# ---- as peças do vídeo 2, COPIADAS dos capítulos 1–5 (nunca importadas):
# mesmas coordenadas de tela, cores, espessuras, rótulos e números do
# original. A prévia só as escala e posiciona (_encaixa) e muda o tempo.
# Ficam de fora a faixa de fórmula do topo e as fórmulas do meio, que o
# critério das prévias corta.

def _v2_cap1():
    """capitulo1.py:10-47 — a reta, o 11 e o encaixe dos blocos 3 (C1N01–
    C1N04). Devolve também o ponto do Flash do C1N03."""
    reta = NumberLine(x_range=[0, 12, 1], length=10, color=CINZA,
                      include_ticks=True, tick_size=0.06).shift(1.9 * DOWN)
    n2 = reta.n2p
    b11 = traco(n2(0) + 2.35 * UP, n2(11) + 2.35 * UP, AZUL)
    r11 = T("11", 30, AZUL).next_to(b11, UP, buff=0.12)
    tres, r3s = VGroup(), VGroup()
    for i in (2, 1, 0):
        s = traco(n2(5 + 3 * i) + 0.5 * UP, n2(2 + 3 * i) + 0.5 * UP, LARANJA)
        tres.add(s)
        r3s.add(T("3", 26, LARANJA).next_to(s, UP, buff=0.10))
    tenta = traco(n2(2) + 0.5 * UP, n2(-1) + 0.5 * UP, LARANJA)
    r3x = T("3", 26, LARANJA).next_to(tenta, UP, buff=0.10)
    xis = T("✗", 30, VERMELHO).move_to(n2(-0.5) + 0.95 * UP)
    s2 = traco(n2(2) + 0.5 * UP, n2(0) + 0.5 * UP, VERDE)
    r2 = T("2", 26, VERDE).next_to(s2, UP, buff=0.10)
    return reta, b11, r11, tres, r3s, tenta, r3x, xis, s2, r2, n2(0) + 0.5 * UP


def _v2_cap2_estado(n2, n):
    """capitulo2.py:112-128, o estado(n) do laço do C2N07 — só as barras e
    os rótulos."""
    xv, cv = n - 5, 11 - n
    bn = traco(n2(11) + 0.95 * UP, n2(11 - n) + 0.95 * UP, LARANJA)
    bx = traco(n2(6) + 1.5 * UP, n2(11 - n) + 1.5 * UP, AMARELO)
    # com n = 11 não sobra NADA: o traço vira um ponto em cima do zero
    bc = (Dot(n2(0) + 0.95 * UP, radius=0.06, color=VERDE) if cv == 0
          else traco(n2(0) + 0.95 * UP, n2(11 - n) + 0.95 * UP, VERDE))
    ln = T(str(n), 24, LARANJA).next_to(bn, DOWN, buff=0.10)
    lx = T(str(xv), 22, AMARELO).next_to(bx, RIGHT, buff=0.12)
    lc = T(str(cv), 24, VERDE).next_to(bc, DOWN, buff=0.10)
    return VGroup(bn, bx, bc, ln, lx, lc)


def _v2_cap2():
    """capitulo2.py:15-39 e 112-137 — a reta, as parcelas 6 + 5, a linha de
    baixo do C2N02 (na ordem do estado: n, x, c e os rótulos) e os estados
    n = 8, 9, 10, 11 do C2N07."""
    reta = NumberLine(x_range=[0, 14, 1], length=11, color=CINZA,
                      include_ticks=True, tick_size=0.06).shift(2.45 * DOWN)
    n2 = reta.n2p
    b6 = traco(n2(0) + 2.1 * UP, n2(6) + 2.1 * UP, VERMELHO)
    r6 = T("6", 26, VERMELHO).next_to(b6, UP, buff=0.10)
    a5 = traco(n2(6) + 2.1 * UP, n2(11) + 2.1 * UP, AZUL)
    r5 = T("5", 26, AZUL).next_to(a5, UP, buff=0.10)
    cver = traco(n2(0) + 0.95 * UP, n2(4) + 0.95 * UP, VERDE)
    rc = T("c", 24, VERDE).next_to(cver, DOWN, buff=0.10)
    n7 = traco(n2(11) + 0.95 * UP, n2(4) + 0.95 * UP, LARANJA)
    rn = T("7", 24, LARANJA).next_to(n7, DOWN, buff=0.10)
    x2 = traco(n2(6) + 1.5 * UP, n2(4) + 1.5 * UP, AMARELO)
    rx = T("x", 22, AMARELO).next_to(x2, RIGHT, buff=0.12)
    estados = [_v2_cap2_estado(n2, n) for n in (8, 9, 10, 11)]
    return (reta, VGroup(b6, r6, a5, r5), VGroup(n7, x2, cver, rn, rx, rc),
            estados)


def _v2_fila_cima(m, W):
    """capitulo3.py:25-34 — m blocos "4" azuis ocupando a largura W,
    rótulos na escala."""
    y1 = 1.55
    xs = np.linspace(-W / 2, W / 2, m + 1)
    tam = max(int(28 * (xs[1] - xs[0]) / 2.2), 6)
    blocos = VGroup(*[traco([xs[i], y1, 0], [xs[i + 1], y1, 0],
                            AZUL, gap=0.09, w=6) for i in range(m)])
    rotulos = VGroup(*[T("4", tam, AZUL)
                       .move_to([(xs[i] + xs[i + 1]) / 2, 1.95, 0])
                       for i in range(m)])
    return VGroup(blocos, rotulos)


def _v2_corrente(k, W=None):
    """capitulo4.py:261-271 — k trêses em corrente de multiplicações."""
    pares = []
    for i in range(k):
        pares.append(("3", AZUL))
        if i < k - 1:
            pares.append(("×", PRETO))
    f = formula(*pares, tamanho=30, buff=0.22)
    if W is not None:
        f.scale_to_fit_width(W)
    return f.move_to([0, 1.95, 0])


def _v2_linha_resultado(x_max, com_ret=True):
    """capitulo4.py:273-280 — a linha tracejada que só sugere o TAMANHO do
    resultado."""
    g = VGroup(*[traco([x, 1.5, 0], [x + 1.25, 1.5, 0], AZUL,
                       gap=0.09, w=6)
                 for x in np.arange(-x_max, x_max - 1.25, 1.25)])
    if com_ret:
        g.add(T("…", 30, AZUL).move_to([x_max - 0.45, 1.5, 0]))
    return g


def _v2_filas(a, xs, y0, passo):
    """capitulo5.py:44-76 (a = 2, C5N05) e 176-196 (a = 3, C5N11) — uma
    fila por x: rótulo a·x, x blocos vermelhos de tamanho a, o módulo 9
    laranja embaixo e o resultado com a marca. Cada fila é
    VGroup(rot, vs, n9, *o que aparece por último)."""
    u, x0 = 0.42, -3.9
    filas = VGroup()
    for fila, x in enumerate(xs):
        y = y0 - fila * passo
        rot = formula((str(a), VERMELHO), ("·", PRETO), (str(x), PRETO),
                      tamanho=28).move_to([-5.3, y + 0.2, 0])
        vs = VGroup(*[traco([x0 + i * a * u, y + 0.35, 0],
                            [x0 + (i + 1) * a * u, y + 0.35, 0],
                            VERMELHO, w=6) for i in range(x)])
        n9 = traco([x0, y, 0], [x0 + 9 * u, y, 0], LARANJA, w=6)
        prod = a * x
        grupo = VGroup(rot, vs, n9)
        if a == 3:
            resto = prod % 9
            resu = T(str(resto), 30,
                     CINZA if resto else VERMELHO).move_to(
                         [x0 + max(prod, 9) * u + 0.55, y + 0.35, 0])
            grupo.add(resu, T("✗", 30, VERMELHO).next_to(resu, RIGHT,
                                                        buff=0.25))
        elif prod <= 9:
            resu = T(str(prod), 30,
                     CINZA).move_to([x0 + prod * u + 0.55, y + 0.35, 0])
            grupo.add(resu, T("✗", 30, VERMELHO).next_to(resu, RIGHT,
                                                        buff=0.25))
        else:
            sobra = traco([x0 + 9 * u, y, 0], [x0 + prod * u, y, 0],
                          VERDE, w=8, gap=0.03)
            resu = T("1", 30, VERDE).move_to([x0 + prod * u + 0.5, y, 0])
            grupo.add(sobra, resu,
                      T("✓", 30, VERDE).next_to(resu, RIGHT, buff=0.25))
        filas.add(grupo)
    return filas


def _v2_tabela():
    """capitulo5.py:219-235, 254-256, 272-275 e 292-295 — a tabela mod 9:
    cabeçalhos, as duas linhas-guia, as células, os círculos dos inversos
    e os retângulos das linhas 0, 3, 6. E, à direita, o ÷ riscado e o a⁻¹
    do encerramento do vídeo 2 (video2.py:42-47)."""
    tam = 0.52
    canto = np.array([-5.9, 2.35, 0.0])

    def ponto(i, j):
        return canto + np.array([(j + 1) * tam, -(i + 1) * tam, 0.0])

    head_c = VGroup(*[T(str(j), 22, AZUL).move_to(canto + [(j + 1) * tam, 0, 0])
                      for j in range(9)])
    head_l = VGroup(*[T(str(i), 22, VERMELHO)
                      .move_to(canto + [0, -(i + 1) * tam, 0])
                      for i in range(9)])
    lin_h = Line(canto + [0.55 * tam, -0.5 * tam, 0],
                 canto + [9.5 * tam, -0.5 * tam, 0], color=PRETO,
                 stroke_width=1.5)
    lin_v = Line(canto + [0.55 * tam, -0.5 * tam, 0],
                 canto + [0.55 * tam, -9.5 * tam, 0], color=PRETO,
                 stroke_width=1.5)
    linhas_cel = VGroup(*[VGroup(*[T(str((i * j) % 9), 22, PRETO)
                                   .move_to(ponto(i, j)) for j in range(9)])
                          for i in range(9)])
    circulos = VGroup(*[Circle(radius=0.21, color=VERDE, stroke_width=2.5)
                        .move_to(ponto(i, j))
                        for i in range(1, 9) for j in range(1, 9)
                        if (i * j) % 9 == 1])
    mortos = VGroup(*[SurroundingRectangle(linhas_cel[i], color=VERMELHO,
                                           buff=0.06, corner_radius=0.08,
                                           stroke_width=2)
                      for i in (0, 3, 6)])
    # o ÷ ocupa o lado direito, onde o capítulo 5 tinha as frases
    div = T("÷", 48, PRETO).move_to([1.2, 0.0, 0])
    risco = Line(div.get_corner(DL) + 0.14 * DL,
                 div.get_corner(UR) + 0.14 * UR,
                 color=VERMELHO, stroke_width=6)
    ainv = pot("a", "−1", VERDE, VERDE, 44).next_to(div, RIGHT, buff=0.65)
    return (head_c, head_l, lin_h, lin_v, linhas_cel, circulos, mortos,
            div, risco, ainv)


def _previa_v2(cena, moldura, t0):
    """V1N10 — os dez trechos da decupagem (roteiro_video1_introducao.md,
    V1N10), na ordem exata da tabela: capítulos 1, 2, 3, 4, 2, 2, 1, 5, 5,
    5. Cada trecho monta as peças COPIADAS do capítulo (_v2_*), com as
    coordenadas do original, e as leva à janela por _encaixa — sempre pelo
    conjunto inteiro do capítulo, para que dois trechos do mesmo capítulo
    ponham a reta no mesmo lugar e na mesma escala. O que muda é só escala,
    posição e tempo; a quantidade encolhe, a aparência não.

    As âncoras são pelo relógio real, contado de `t0`, o começo da fala: o
    que sobrou do trecho anterior apaga nos 0,12 s antes da âncora e o
    gesto começa nela. Quando um gesto parte de algo que no capítulo já
    estava em cena (a reta dos trechos 5 e 7), esse cenário entra num
    FadeIn curto antes dele.

    Os run_time evitam múltiplos de 1/15 s: a 15 fps um 0,2 vira 4 quadros
    pelo arredondamento do arange, e a soma disso atrasava as âncoras.

    O último trecho termina em ~19,6 s: a _fecha_janela (0,75 s) vem logo
    depois, dentro da mesma fala, e tira o que sobrou, a⁻¹ inclusive."""
    tag, est = "V1N10", 20.3
    k = _k(tag, est)

    def rt(s):
        return s * VEL * k

    def ancora(nome, sai=None):
        """Espera até a âncora `nome` da fala e apaga `sai` nos 0,12 s
        antes. As âncoras são o começo de cada trecho da decupagem, em
        segundos dos 20,3 s do roteiro (sincronias_v1.py)."""
        fo = rt(0.12) if sai is not None else 0.0
        espera = _ate(cena, t0 - fo, tag, est, _f(tag, nome))
        if espera.run_time > 1e-3:
            cena.play(espera)
        if sai is not None:
            cena.play(FadeOut(sai), run_time=fo)

    def cap1():
        (reta, b11, r11, tres, r3s, tenta, r3x, xis, s2, r2,
         bate) = pecas = _v2_cap1()
        quadro = VGroup(*pecas[:-1])
        s, leva = _encaixa(quadro, moldura)
        _confere(quadro, moldura, "V1N10 cap. 1")
        return pecas[:-1] + (leva(bate), s)

    def cap2():
        reta, soma, atual, estados = pecas = _v2_cap2()
        quadro = VGroup(reta, soma, atual, *estados)
        _encaixa(quadro, moldura)
        _confere(quadro, moldura, "V1N10 cap. 2")
        return pecas

    def _trecho1():
        # 0,0–5,6 · cap. 1 (C1N01–C1N02): a reta se desenha e a barra 11
        # azul cresce sobre ela. Começa depois da _abre_janela (0,8 s).
        # run_time esticado (×2,333, o mesmo fator de crescimento da
        # janela do trecho) para não deixar a espera até o trecho 2 crescer
        reta, b11, r11 = cap1()[:3]
        cena.play(Create(reta), run_time=rt(1.33))
        cena.play(Create(b11), FadeIn(r11), run_time=rt(1.33))
        return VGroup(reta, b11, r11)

    def _trecho2(sai):
        # 5,6–7,2 · cap. 2 (C2N01–C2N02): a reta e as parcelas 6 e 5
        # encostadas ponta a ponta, uma play cada, como no original
        reta, soma = cap2()[:2]
        b6, r6, a5, r5 = soma
        ancora("somar", sai)
        cena.play(Create(reta), run_time=rt(0.43))
        cena.play(Create(b6), FadeIn(r6), run_time=rt(0.37))
        cena.play(Create(a5), FadeIn(r5), run_time=rt(0.37))
        return VGroup(reta, soma)

    def _trecho3(sai):
        # 7,2–8,6 · cap. 3 (C3N01): os cinco "4" azuis em cadeia. No
        # original os rótulos saem do 4 da equação do topo, que a janela
        # corta: aqui eles entram por FadeIn, no mesmo LaggedStart
        base = _v2_fila_cima(5, 11.0)
        _encaixa(base, moldura)
        _confere(base, moldura, "V1N10 cap. 3")
        segs, rots = base
        ancora("multiplicar", sai)
        cena.play(LaggedStart(*[AnimationGroup(Create(s), FadeIn(r))
                                for s, r in zip(segs, rots)],
                              lag_ratio=0.15), run_time=rt(1.03))
        return base

    def _trecho4(sai):
        # 8,6–10,1 · cap. 4 (C4N01–C4N02): a corrente de seis 3 (os 3 saem
        # do 3⁶ do topo no original; aqui, FadeIn) e a linha tracejada
        prod = _v2_corrente(6)
        segs = _v2_linha_resultado(5.5)
        quadro = VGroup(prod, segs)
        _encaixa(quadro, moldura)
        _confere(quadro, moldura, "V1N10 cap. 4")
        ancora("potências", sai)
        cena.play(LaggedStart(*[FadeIn(prod[i]) for i in range(0, 11, 2)],
                              lag_ratio=0.12),
                  *[FadeIn(prod[i]) for i in range(1, 11, 2)],
                  run_time=rt(0.63))
        cena.play(LaggedStart(*[(Create(s) if isinstance(s, Line)
                                 else FadeIn(s)) for s in segs],
                              lag_ratio=0.08), run_time=rt(0.57))
        return quadro

    def _trecho5_6(sai):
        # 10,1–11,6 · cap. 2 (C2N02): com a reta e o 6 + 5 já em cena, o n
        # laranja cresce da direita para a esquerda e o x amarelo nasce
        # quando a ponta cruza o 6 (a razão 1,5/2,1 do Wait do original);
        # os rótulos e o c verde vêm em seguida.
        # 11,6–12,8 · cap. 2 (C2N07, laço mudo): os quatro estados n = 8…11 em
        # ReplacementTransform — o x engorda e o c vira um ponto
        reta, soma, atual, estados = cap2()
        n7, x2, cver, rn, rx, rc = atual
        ancora("num mundo", sai)
        cena.play(FadeIn(reta), FadeIn(soma), run_time=rt(0.12))
        cena.play(AnimationGroup(
            Create(n7, run_time=rt(0.63), rate_func=linear),
            Succession(Wait(rt(0.45)),
                       Create(x2, run_time=rt(0.18), rate_func=linear))))
        cena.play(FadeIn(rn), FadeIn(rx), run_time=rt(0.18))
        cena.play(Create(cver), FadeIn(rc), run_time=rt(0.25))

        ancora("dão a volta")
        for novo in estados:
            cena.play(*[ReplacementTransform(a, b)
                        for a, b in zip(atual, novo)], run_time=rt(0.19))
            atual = novo
        return VGroup(reta, soma, atual)

    def _trecho7(sai):
        # 12,8–14,6 · cap. 1 (C1N03–C1N04): com a reta e o 11 já em cena,
        # os três 3 laranja encaixam, o quarto estoura o zero (Flash, ✗,
        # Wiggle) e vira o 2 verde
        (reta, b11, r11, tres, r3s, tenta, r3x, xis, s2, r2,
         bate, s) = cap1()
        ancora("só o que sobra", sai)
        cena.play(FadeIn(reta), FadeIn(b11), FadeIn(r11), run_time=rt(0.12))
        cena.play(LaggedStart(*[AnimationGroup(Create(t), FadeIn(r))
                                for t, r in zip(tres, r3s)],
                              lag_ratio=0.35), run_time=rt(0.43))
        cena.play(Create(tenta), FadeIn(r3x), run_time=rt(0.25))
        cena.play(Flash(bate, color=VERMELHO, flash_radius=0.4 * s,
                        line_length=0.2 * s),
                  FadeIn(xis, scale=1.4), Wiggle(tenta), run_time=rt(0.37))
        cena.play(ReplacementTransform(tenta, s2),
                  ReplacementTransform(r3x, r2),
                  FadeOut(xis), run_time=rt(0.3))
        return VGroup(reta, b11, r11, tres, r3s, s2, r2)

    def _trecho8_9(sai):
        # 14,6–16,2 · cap. 5 (C5N05): as filas 2·3 e 2·4 falham e a 2·5
        # passa do 9, com o sobrinho verde e o ✓ — os três play do original
        # numa Succession por fila.
        # 16,2–18,0 · cap. 5 (C5N11): as seis filas 3·1…3·6, todas com ✗,
        # um play por fila como no original
        filas2 = _v2_filas(2, (3, 4, 5), 1.45, 1.0)
        filas3 = _v2_filas(3, (1, 2, 3, 4, 5, 6), 1.6, 0.72)
        quadro = VGroup(filas2, filas3)
        _encaixa(quadro, moldura)
        _confere(quadro, moldura, "V1N10 cap. 5 (filas)")
        ancora("no fim", sai)
        for f in filas2:
            cena.play(Succession(
                AnimationGroup(FadeIn(f[0]), Create(f[2]),
                               run_time=rt(0.13)),
                LaggedStart(*[Create(s) for s in f[1]], lag_ratio=0.2,
                            run_time=rt(0.16)),
                AnimationGroup(*[FadeIn(m) for m in f[3:]],
                               run_time=rt(0.14))))
        ancora("jeito de dividir", filas2)
        for f in filas3:
            cena.play(FadeIn(f[0]), Create(f[2]),
                      LaggedStart(*[Create(s) for s in f[1]], lag_ratio=0.2),
                      FadeIn(f[3]), FadeIn(f[4]), run_time=rt(0.25))
        return filas3

    def _trecho10(sai):
        # 18,0–19,6 · cap. 5 (C5N15–C5N19): cabeçalhos e linhas-guia, as
        # células em cadeia, os círculos verdes e as linhas 0, 3, 6
        # apagando nos retângulos vermelhos; por cima, o ÷ do encerramento
        # do vídeo 2 (V2N00): entra, é riscado e o a⁻¹ verde nasce ao lado
        (head_c, head_l, lin_h, lin_v, linhas_cel, circulos, mortos,
         div, risco, ainv) = pecas = _v2_tabela()
        quadro = VGroup(*pecas)
        _encaixa(quadro, moldura)
        _confere(quadro, moldura, "V1N10 cap. 5 (tabela)")
        ancora("sem dividir", sai)
        cena.play(FadeIn(head_c), FadeIn(head_l),
                  Create(lin_h), Create(lin_v), run_time=rt(0.25))
        cena.play(LaggedStart(*[FadeIn(l) for l in linhas_cel],
                              lag_ratio=0.1), run_time=rt(0.37))
        cena.play(LaggedStart(*[Create(c) for c in circulos],
                              lag_ratio=0.12),
                  FadeIn(div, scale=1.3), run_time=rt(0.3))
        cena.play(*[linhas_cel[i].animate.set_opacity(0.2) for i in (0, 3, 6)],
                  *[head_l[i].animate.set_opacity(0.3) for i in (0, 3, 6)],
                  LaggedStart(*[Create(m) for m in mortos], lag_ratio=0.2),
                  Create(risco), run_time=rt(0.3))
        cena.play(FadeIn(ainv, shift=0.2 * UP), run_time=rt(0.25))

    sai = _trecho1()
    sai = _trecho2(sai)
    sai = _trecho3(sai)
    sai = _trecho4(sai)
    sai = _trecho5_6(sai)
    sai = _trecho7(sai)
    sai = _trecho8_9(sai)
    _trecho10(sai)


def corpo_previa2(cena, titulo, trilha, marca):
    """V1N10. A _abre_janela acende o 2, os outros três (e a marca) somem,
    o 2 sobe para o topo — ele é o rótulo da janela — e a moldura nasce;
    a prévia do vídeo 2 roda dentro dela e a _fecha_janela devolve o 2 à
    trilha, apagada, no fim da fala.

    Devolve (titulo, trilha), em cena: o V1N11 abre o 3 do mesmo jeito."""
    with narra(cena, "V1N10", 20.3):
        k = _k("V1N10", 20.3)
        t0 = _agora(cena)
        moldura, _ = _abre_janela(cena, titulo, trilha, 1, k, some=(marca,))
        _previa_v2(cena, moldura, t0)
        _fecha_janela(cena, titulo, trilha, 1, moldura, k)

    return titulo, trilha


def _previa_v3a(cena, moldura, fermat, t0):
    """V1N11 — cap. 6 (Fermat: a permutação da tabela mod 7) e cap. 7
    (Euler: o contra-exemplo mod 9), na ordem exata da tabela.

    `fermat` é o rótulo que a _abre_janela pôs na moldura; em 5,4 ele vira
    "Euler" no mesmo lugar. Devolve o "Euler" (em cena): o V1N12 o recebe
    e o vira "RSA" no mesmo canto, e só a _fecha_janela do fim do V1N12
    leva esse rótulo junto com o conteúdo.

    Três encaixes: a tabela mod 7 com os arcos (0,0–5,4, a mesma cena), a
    mod 9 com as cruzes, as chaves e a caixa (5,4–11,0), o cadeado."""
    tag, est = "V1N11", 12.1
    k = _k(tag, est)
    cx, cy = moldura.get_center()[:2]

    # 0,0–2,2 · cap. 6: a tabela mod 7 se preenchendo linha a linha em
    # LaggedStart — o quadro aparecendo é a imagem, ninguém precisa ler os
    # números
    tam = 0.5
    canto = np.array([cx - 1.5, cy + 1.1, 0.0])

    def ponto(i, j):
        return canto + np.array([j * tam, -i * tam, 0.0])

    linhas = [VGroup(*[T(str((i * j) % 7), 16, PRETO).move_to(ponto(i, j))
                       for j in range(1, 7)]) for i in range(1, 5)]

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
    arcos = VGroup()
    for j in range(6):
        idx = Bv.index(j + 1)
        arcos.add(ArcBetweenPoints(A[j].get_bottom() + 0.05 * DOWN,
                                   B[idx].get_top() + 0.05 * UP,
                                   angle=(0.6 if idx > j else -0.6),
                                   color=VERDE, stroke_width=2))
    quadro = VGroup(*linhas, el, A, B, arcos)
    _encaixa(quadro, moldura)
    _confere(quadro, moldura, "V1N11 tabela mod 7")

    cena.play(LaggedStart(*[FadeIn(l) for l in linhas], lag_ratio=0.25),
              run_time=1.3 * VEL * k)
    # ≈ 0,182 da fala: a elipse entra e liga a linha 1 à sua fileira de cima
    cena.play(Succession(
        _ate(cena, t0, tag, est, _f(tag, "teoremas")),
        AnimationGroup(Create(el), LaggedStart(
            *[TransformFromCopy(linha1[j], A[j]) for j in range(6)],
            lag_ratio=0.12), run_time=1.1 * VEL * k)))
    cena.play(el.animate.move_to(linha3),
              LaggedStart(*[TransformFromCopy(linha3[j], B[j])
                            for j in range(6)], lag_ratio=0.12),
              run_time=1.1 * VEL * k)
    cena.play(LaggedStart(*[Create(a) for a in arcos], lag_ratio=0.1),
              run_time=0.7 * VEL * k)
    cena.play(FadeOut(VGroup(*linhas, el, A, B)), run_time=0.3 * VEL * k)

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
    # 7,6–9,6 · cap. 7: duas cruzes riscam os múltiplos de 3 no cabeçalho —
    # os únicos sem inverso — e sobram seis, reunidos entre chaves;
    # 9,6–11,0: a caixa verde se fecha em volta do que sobrou. `fim` é o
    # fantasma dos seis já reunidos, de onde saem as chaves e a caixa
    cruzes = VGroup(Cross(header[2], stroke_color=VERMELHO, stroke_width=3),
                    Cross(header[5], stroke_color=VERMELHO, stroke_width=3))
    restantes = VGroup(*[header[i] for i in range(8) if i not in (2, 5)])
    fim = restantes.copy().arrange(RIGHT, buff=0.3).move_to([cx, y0, 0])
    chave_e = T("{", 30, PRETO).next_to(fim, LEFT, buff=0.1)
    chave_d = T("}", 30, PRETO).next_to(fim, RIGHT, buff=0.1)
    caixa = SurroundingRectangle(VGroup(chave_e, fim, chave_d),
                                 color=VERDE, buff=0.15, corner_radius=0.08,
                                 stroke_width=2.5)
    quadro = VGroup(header, row3, row6, el9, cruzes, fim, chave_e, chave_d,
                    caixa)
    _encaixa(quadro, moldura)
    _confere(quadro, moldura, "V1N11 tabela mod 9")

    cena.play(FadeOut(arcos), ReplacementTransform(fermat, euler),
              FadeIn(header), run_time=0.6 * VEL * k)
    cena.play(FadeIn(row3), FadeIn(row6), run_time=0.5 * VEL * k)
    cena.play(Create(el9), run_time=0.4 * VEL * k)
    cena.play(FadeOut(row3), FadeOut(row6), run_time=0.7 * VEL * k)

    cena.play(Create(cruzes), FadeOut(el9), run_time=0.6 * VEL * k)
    cena.play(FadeOut(header[2]), FadeOut(header[5]), FadeOut(cruzes),
              *[m.animate.move_to(f) for m, f in zip(restantes, fim)],
              run_time=0.8 * VEL * k)
    cena.play(FadeIn(chave_e), FadeIn(chave_d), run_time=0.6 * VEL * k)

    cena.play(Create(caixa), run_time=1.0 * VEL * k)
    cena.play(Indicate(caixa, color=VERDE, scale_factor=1.03),
              run_time=0.4 * VEL * k)

    # 11,0–12,1: o cadeado com as letras RSA reaparece por meio segundo,
    # intacto — rima com o V1N01
    mini_cad = cadeado("fechado", "RSA").scale(0.45)
    _encaixa(mini_cad, moldura)
    _confere(mini_cad, moldura, "V1N11 cadeado")
    cena.play(FadeOut(VGroup(chave_e, restantes, chave_d, caixa)),
              FadeIn(mini_cad), run_time=0.5 * VEL * k)
    cena.play(FadeOut(mini_cad), run_time=0.6 * VEL * k)

    return euler


def _previa_v3b(cena, moldura, euler, t0):
    """V1N12 — cap. 8: o esquema do RSA (mensagem → cifra → mensagem),
    as duas chaves, o exemplo rodando e o n se partindo nos primos do
    V1N02. A janela continua exatamente como a _previa_v3a deixou — nada
    aqui a reabre, porque o título 3 é o único da trilha que não troca de
    número nesta fala.

    `euler` é o rótulo que a _previa_v3a deixou no canto da moldura; na
    palavra "RSA" da fala (≈ 0,236, `t0` é o começo do narra desta tag)
    ele vira "RSA" no mesmo canto e tamanho da troca Fermat → Euler. O
    "RSA" fica em cena — só a _fecha_janela do fim desta fala o leva
    junto com o conteúdo.

    O esquema fica em cena de 0,0 a 12,5, então o encaixe é um só, com os
    cartões nas duas posições, os "?" já espalhados e a caixa final.
    O último trecho foi comprimido de 2,3 para 1,5 s: a _fecha_janela vem
    logo depois e é ela que apaga os "?"."""
    tag, est = "V1N12", 12.5
    k = _k(tag, est)
    cx, cy = moldura.get_center()[:2]

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
    # o meio do esquema: o n e a seta de despedaçar ficam embaixo dele
    xm = VGroup(msg1, msg2).get_center()[0]

    # o rótulo da janela: "Euler" vira "RSA" no mesmo canto e tamanho da
    # troca Fermat → Euler da _previa_v3a
    rsa = T("RSA", 24, LARANJA).move_to(euler, aligned_edge=LEFT)

    # 2,6–5,6 · cap. 8: os dois cartões nascem acima das setas e descem até
    # elas — o cinza "pública" na primeira, o amarelo "privada" na segunda
    pub = _caixa(tx("geral.publica"), CINZA, PRETO, largura=1.5).scale(0.75)
    pub.move_to(seta1.get_center() + [0, 0.9, 0])
    priv = _caixa(tx("geral.privada"), AMARELO, PRETO, largura=1.5).scale(0.75)
    priv.move_to(seta2.get_center() + [0, 0.9, 0])
    pub_fim = pub.copy().move_to(seta1.get_center() + [0, 0.35, 0])
    priv_fim = priv.copy().move_to(seta2.get_center() + [0, 0.35, 0])
    # e de onde eles descem no FadeIn: a meio caminho já aparecem, e sem
    # isso na medida o "privada" encostava na borda de cima da moldura
    entram = VGroup(pub.copy().shift(0.3 * UP), priv.copy().shift(0.3 * UP))

    # 8,0–10,2 · cap. 8: o n se parte em p rosa e q verde-claro
    n_txt = T(_N, 26, LARANJA).move_to([xm, cy - 1.3, 0])
    p_txt = T(_P, 24, ROSA).move_to(n_txt.get_center() + [-0.5, -0.7, 0])
    q_txt = T(_Q, 24, VERDE2).move_to(n_txt.get_center() + [0.5, -0.7, 0])

    # 10,2–12,5: a caixa verde final e, sobre ela, a seta de despedaçar
    caixa_final = SurroundingRectangle(
        VGroup(msg1, seta1, cif, seta2, msg2, pub_fim, priv_fim, p_txt,
               q_txt),
        color=VERDE, buff=0.25, corner_radius=0.12, stroke_width=2.5)
    mini_volta = Arrow([xm + 1.2, cy - 0.5, 0], [xm - 1.2, cy - 0.5, 0],
                       buff=0, color=PRETO, stroke_width=4)
    mini_q = VGroup(*[T("?", 20, CINZA) for _ in range(3)])
    for q, x in zip(mini_q, np.linspace(0.9, -0.9, 3)):
        q.move_to([xm + x, cy - 0.5, 0])
    q_fim = VGroup(*[q.copy().shift([0.3 * dx, 0.3 * dy, 0])
                     for q, (dx, dy, _) in zip(mini_q, _ESPALHA[:3])])

    quadro = VGroup(msg1, seta1, cif, seta2, msg2, pub, priv, pub_fim,
                    priv_fim, entram, n_txt, p_txt, q_txt, caixa_final,
                    mini_volta, mini_q, q_fim)
    s, _ = _encaixa(quadro, moldura)
    _confere(quadro, moldura, "V1N12 esquema do RSA")

    cena.play(LaggedStart(FadeIn(msg1, shift=0.2 * s * RIGHT), GrowArrow(seta1),
                          FadeIn(cif, shift=0.2 * s * RIGHT), GrowArrow(seta2),
                          FadeIn(msg2, shift=0.2 * s * RIGHT), lag_ratio=0.5),
              run_time=2.6 * VEL * k)

    # "RSA" ≈ 0,236 da fala (38 / 161 caracteres, o começo da palavra
    # "RSA" no texto do V1N12): "Euler" vira "RSA" no rótulo da janela
    cena.play(Succession(
        _ate(cena, t0, tag, est, _f(tag, "RSA")),
        ReplacementTransform(euler, rsa, run_time=0.4 * VEL * k)))

    cena.play(FadeIn(pub, shift=0.3 * s * DOWN), run_time=0.8 * VEL * k)
    cena.play(pub.animate.move_to(pub_fim), run_time=0.5 * VEL * k)
    cena.play(FadeIn(priv, shift=0.3 * s * DOWN), run_time=0.8 * VEL * k)
    cena.play(priv.animate.move_to(priv_fim), run_time=0.5 * VEL * k)
    cena.play(Indicate(priv, color=AMARELO), run_time=0.4 * VEL * k)

    # 5,6–8,0 · cap. 8: o exemplo roda dentro do mesmo esquema, cada caixa
    # acendendo na sua vez, sem nenhuma conta aparecendo por baixo
    cena.play(Indicate(msg1, color=CIANO, scale_factor=1.15), run_time=0.8 * VEL * k)
    cena.play(Indicate(cif, color=CIANO, scale_factor=1.15), run_time=0.8 * VEL * k)
    cena.play(Indicate(msg2, color=CIANO, scale_factor=1.15), run_time=0.8 * VEL * k)

    # 8,0–10,2 · cap. 8: o n se parte nos MESMOS primos do V1N02, e os dois
    # cartões de chave piscam junto, porque foi dali que nasceram
    cena.play(FadeIn(n_txt, scale=1.3), run_time=0.5 * VEL * k)
    cena.play(TransformFromCopy(n_txt, p_txt), TransformFromCopy(n_txt, q_txt),
              FadeOut(n_txt), run_time=0.9 * VEL * k)
    cena.play(Indicate(pub, color=CINZA), Indicate(priv, color=AMARELO),
              run_time=0.8 * VEL * k)

    # 10,2–11,7: a caixa verde final se fecha; sobre ela, a seta de
    # despedaçar do V1N01 volta por meio segundo — rima visual
    cena.play(Create(caixa_final), run_time=1.0 * VEL * k)
    cena.play(GrowArrow(mini_volta), run_time=0.2 * VEL * k)
    cena.play(ReplacementTransform(mini_volta, mini_q),
              *[q.animate.move_to(f) for q, f in zip(mini_q, q_fim)],
              run_time=0.3 * VEL * k)


def corpo_previa3(cena, titulo, trilha):
    """V1N11 e V1N12. A _abre_janela acende o 3 e abre a moldura com
    "Fermat" como rótulo; ela fica aberta nas duas falas — o 3 é o único
    título da trilha que não troca de número — e só a _fecha_janela do fim
    do V1N12 a fecha, devolvendo o 3 à trilha.

    Devolve (titulo, trilha), em cena: o V1N13 abre o 4 do mesmo jeito."""
    with narra(cena, "V1N11", 12.1):
        k = _k("V1N11", 12.1)
        t0 = _agora(cena)
        moldura, fermat = _abre_janela(cena, titulo, trilha, 2, k,
                                       rotulo="Fermat")
        euler = _previa_v3a(cena, moldura, fermat, t0)

    with narra(cena, "V1N12", 12.5):
        k = _k("V1N12", 12.5)
        t0 = _agora(cena)
        _previa_v3b(cena, moldura, euler, t0)
        _fecha_janela(cena, titulo, trilha, 2, moldura, k)

    return titulo, trilha


def _v4_tabela():
    """capitulo9.py:52-67 e 107-171 — a tabela mod 9 e o zigue-zague da
    base 4 (1 → 4 → 7 → 1): cabeçalhos, linhas-guia, células, o círculo do
    1 de partida, os cinco degraus até o 1 da linha 4 (seta que desce e
    círculo, arco que sobe e círculo, …) e o arco que fecha o ciclo.

    Devolve também o caminho do ciclo — as descidas sem a ponta, os arcos
    e o fecho —, que nunca vai à cena: é o molde do flash amarelo."""
    tam = 0.52
    canto = np.array([-6.0, 2.2, 0.0])

    def ponto(i, j):
        return canto + np.array([(j + 1) * tam, -(i + 1) * tam, 0.0])

    def circ(i, j):
        return Circle(radius=0.22, color=VERDE,
                      stroke_width=2.5).move_to(ponto(i, j))

    head_c = VGroup(*[T(str(j), 22, AZUL).move_to(canto + [(j + 1) * tam, 0, 0])
                      for j in range(9)])
    head_l = VGroup(*[T(str(i), 22, VERMELHO)
                      .move_to(canto + [0, -(i + 1) * tam, 0])
                      for i in range(9)])
    lin_h = Line(canto + [0.55 * tam, -0.5 * tam, 0],
                 canto + [9.5 * tam, -0.5 * tam, 0], color=PRETO,
                 stroke_width=1.5)
    lin_v = Line(canto + [0.55 * tam, -0.5 * tam, 0],
                 canto + [0.55 * tam, -9.5 * tam, 0], color=PRETO,
                 stroke_width=1.5)
    linhas_cel = VGroup(*[VGroup(*[T(str((i * j) % 9), 22, PRETO)
                                   .move_to(ponto(i, j)) for j in range(9)])
                          for i in range(9)])

    c00 = circ(1, 1)
    degraus, caminho = VGroup(), VGroup()
    for k in range(3):
        j = (1, 4, 7)[k]
        desce = Arrow(ponto(1, j) + 0.22 * DOWN, ponto(4, j) + 0.24 * UP,
                      buff=0, color=VERDE, stroke_width=2.5,
                      max_tip_length_to_length_ratio=0.18)
        degraus.add(VGroup(desce, circ(4, j)))
        caminho.add(Line(ponto(1, j) + 0.22 * DOWN, ponto(4, j) + 0.24 * UP))
        if k < 2:
            prox_j = (4, 7)[k]
            sobe = ArcBetweenPoints(ponto(4, j) + 0.24 * RIGHT,
                                    ponto(1, prox_j) + 0.24 * DOWN,
                                    angle=-0.55, color=VERDE,
                                    stroke_width=2.0)
            degraus.add(VGroup(sobe, circ(1, prox_j)))
            caminho.add(sobe.copy())
    fecha = ArcBetweenPoints(ponto(4, 7) + 0.24 * DOWN,
                             ponto(1, 1) + 0.26 * LEFT, angle=-1.3,
                             color=VERDE, stroke_width=2.0)
    caminho.add(fecha.copy())
    return (head_c, head_l, lin_h, lin_v, linhas_cel, c00, degraus, fecha,
            caminho)


def _previa_v4a(cena, moldura, t0):
    """V1N13 — cap. 9 e cap. 10, na ordem da decupagem: a tabela mod 9 se
    preenche e o zigue-zague a percorre desde o começo; em "ordem modular"
    o último arco fecha o ciclo e o flash amarelo dá a volta. Em "Depois"
    a tabela sai e as árvores do cap. 10 entram, e não volta mais. Em
    "quebrar" o cadeado RSA do V1N11 reaparece entre as duas árvores e
    racha — a rima com a seta de despedaçar do fim do V1N12. Como nas
    prévias anteriores, cada trecho recria só o gesto mínimo, sem importar
    capitulo9/9b/10, e passa por _encaixa e _confere antes de animar.

    `t0` é o começo do narra do V1N13. Devolve o que fica em cena — o que
    sobrou das árvores e o cadeado rachado —: o V1N14 os tira em
    "computador quântico"."""
    tag, est = "V1N13", 17.6
    k = _k(tag, est)

    def ancora(nome):
        espera = _ate(cena, t0, tag, est, _f(tag, nome))
        if espera.run_time > 1e-3:
            cena.play(espera)

    def _arvores(kv):
        # cap. 10: um tronco, duas árvores; os ramos que se repetem nos dois
        # lados acendem juntos, o resto cai e sobram dois números pequenos
        # (o 7 e o 9 do 2³ − 1 e do 2³ + 1 — ainda não o 3 × 7). O cadeado
        # do "quebrar" é montado aqui, no vão entre os dois ramos acesos,
        # para entrar na mesma medida; quem o anima é o corpo da prévia.
        # Devolve (o que fica das árvores, o cadeado fora de cena)
        cx, cy = moldura.get_center()[:2]
        ponta = np.array([cx, cy + 1.45, 0])
        garfo = np.array([cx, cy + 0.9, 0])

        def ramo(a, b):
            return Line(a, b, color=PRETO, stroke_width=3)

        tronco = ramo(ponta, garfo)
        filhos, netos, folhas = [], [], []
        acesos, apagam, pontas_internas = [], [], []
        for lado in (-1, 1):
            f = garfo + [2.2 * lado, -0.6, 0]
            filhos.append(ramo(garfo, f))
            for s in (-1, 1):
                g = f + [1.0 * s, -0.7, 0]
                n = ramo(f, g)
                netos.append(n)
                for t in (-1, 1):
                    h = g + [0.5 * t, -0.7, 0]
                    fo = ramo(g, h)
                    folhas.append(fo)
                    # o caminho que vai para o centro é o que se repete
                    # nos dois lados, espelhado
                    if s == -lado and t == -lado:
                        acesos += [n, fo]
                        pontas_internas.append(h)
                    elif s != -lado:
                        apagam.append(fo)
                if s != -lado:
                    apagam.append(n)
        numeros = VGroup(T("7", 28, CINZA), T("9", 28, CINZA))
        for num, h in zip(numeros, pontas_internas):
            num.move_to(h + 0.3 * DOWN)
        outras = [fo for fo in folhas if fo not in acesos and fo not in apagam]
        mini_cad = cadeado("fechado", "RSA").scale(0.45)
        mini_cad.move_to([cx, cy - 0.25, 0])
        quadro = VGroup(tronco, *filhos, *netos, *folhas, numeros, mini_cad)
        _, leva = _encaixa(quadro, moldura)
        _confere(quadro, moldura, "V1N13 árvores")
        pontas_internas = [leva(h) for h in pontas_internas]

        cena.play(Create(tronco), run_time=0.35 * VEL * kv)
        cena.play(*[Create(f) for f in filhos], run_time=0.4 * VEL * kv)
        cena.play(LaggedStart(*[Create(n) for n in netos],
                              *[Create(fo) for fo in folhas],
                              lag_ratio=0.12), run_time=0.5 * VEL * kv)
        cena.play(*[r.animate.set_stroke(AMARELO, width=5) for r in acesos],
                  run_time=0.3 * VEL * kv)
        cena.play(*[FadeOut(r) for r in apagam + outras],
                  *[GrowFromPoint(num, h) for num, h
                    in zip(numeros, pontas_internas)], run_time=0.35 * VEL * kv)
        return VGroup(tronco, *filhos, *acesos, numeros), mini_cad

    (head_c, head_l, lin_h, lin_v, linhas_cel, c00, degraus, fecha,
     caminho) = pecas = _v4_tabela()
    quadro = VGroup(*pecas)
    _encaixa(quadro, moldura)
    _confere(quadro, moldura, "V1N13 tabela mod 9")
    no_ar = VGroup(head_c, head_l, lin_h, lin_v, linhas_cel, c00, degraus)

    # do começo até "a ordem modular" (≈ 0,525) · cap. 9: depois da
    # _abre_janela (0,8 s), cabeçalhos e linhas-guia, as nove linhas em
    # LaggedStart (C9N03), e o 1 de partida acende e o zigue-zague desce,
    # sobe, desce, sobe, desce até o 1 da linha 4 (C9N05–C9N08). Os quatro
    # gestos somam 8,0 s × k e terminam ~0,4 s antes da âncora
    cena.play(FadeIn(head_c), FadeIn(head_l), Create(lin_h), Create(lin_v),
              run_time=0.6 * VEL * k)
    cena.play(LaggedStart(*[FadeIn(l) for l in linhas_cel], lag_ratio=0.25),
              run_time=2.9 * VEL * k)
    cena.play(Create(c00), run_time=0.5 * VEL * k)
    cena.play(LaggedStart(*[AnimationGroup(
        GrowArrow(seg) if isinstance(seg, Arrow) else Create(seg),
        Create(circ)) for seg, circ in degraus], lag_ratio=1.0),
        run_time=4.0 * VEL * k)
    # "a ordem modular": o último arco fecha o ciclo de volta no 1 de
    # partida (C9N09) e o flash amarelo dá uma volta inteira no caminho —
    # 1,0 s × k, dentro dos 1,2 s × k até "Depois"
    ancora("ordem modular")
    cena.play(Create(fecha), Indicate(c00, color=VERDE),
              run_time=0.45 * VEL * k)
    cena.play(LaggedStart(*[ShowPassingFlash(
        p.copy().set_stroke(AMARELO, width=7), time_width=1.0)
        for p in caminho], lag_ratio=1.0), run_time=0.55 * VEL * k)

    # "Depois" (≈ 0,593) · cap. 10: a tabela sai e as árvores entram, com
    # os gestos 2× mais longos que na prévia de uma fala só — 4,2 s × k,
    # ~0,6 s antes de "quebrar". A tabela não volta
    ancora("Depois")
    cena.play(FadeOut(VGroup(no_ar, fecha)), run_time=0.4 * VEL * k)
    arvores, mini_cad = _arvores(2.0 * k)

    # "quebrar" (≈ 0,864): o cadeado RSA reaparece por meio segundo, intacto
    # como no fim do V1N11, e racha — o rachar() do V3N02, o mesmo traço
    ancora("quebrar")
    cena.play(FadeIn(mini_cad, scale=0.8), run_time=0.5 * VEL * k)
    rachar(cena, mini_cad, run_time=0.7 * k)

    return VGroup(arvores, mini_cad)


def _previa_v4b(cena, moldura, sobra, t0):
    """V1N14 — os trechos do cap. 11 dentro da MESMA moldura: nada aqui a
    reabre, porque o 4 não troca de número nesta fala, o mesmo recurso do
    V1N12. Cada trecho entra na palavra que o nomeia — o circuito em
    "lógica incomum", os qubits em "superposição", o par colapsando em
    "emaranhamento", as ondas em "interferência", com os vales achatando
    em "apaga" e os picos crescendo em "até sobrar" — e a seta laranja em
    "algoritmo de Shor". Os fatores de tempo de cada trecho são os que o
    fazem preencher a sua janela entre âncoras.

    `sobra` é o que a _previa_v4a deixou em cena (as árvores e o cadeado
    rachado), e sai por FadeOut assim que a fala chega em "computador
    quântico"; `t0` é o começo do narra do V1N14. Termina com a seta
    laranja no pico: a _fecha_janela vem depois da fala, no encerramento."""
    tag, est = "V1N14", 23.3
    k = _k(tag, est)

    def ancora(nome):
        espera = _ate(cena, t0, tag, est, _f(tag, nome))
        if espera.run_time > 1e-3:
            cena.play(espera)

    def _cartoes(kv):
        # cap. 11: o mesmo círculo ciano dos qubits da linha do tempo do
        # V1N06, grande, com o gradiente dos bits 1 e 0 dentro (a
        # superposição). Monta também o fio do _par, para os dois entrarem
        # na mesma medida; devolve (par, fio), o fio ainda fora de cena
        cx, cy = moldura.get_center()[:2]
        par = VGroup()
        for x in (cx - 2.0, cx + 2.0):
            q = _qubit().scale(5.5).set_stroke(width=4)
            q.set_fill([CIANO, AMARELO], opacity=0.9).set_sheen_direction(UR)
            par.add(q.move_to([x, cy + 0.1, 0]))
        fio = Line(par[0].get_right(), par[1].get_left(), color=PRETO,
                   stroke_width=3)
        quadro = VGroup(par, fio)
        _encaixa(quadro, moldura)
        _confere(quadro, moldura, "V1N14 qubits")
        cena.play(LaggedStart(*[GrowFromCenter(q) for q in par],
                              lag_ratio=0.3), run_time=0.5 * VEL * kv)
        return par, fio

    def _par(par, fio, kv):
        # cap. 11 (C11N07–C11N09): o fio liga os dois qubits e eles colapsam
        # juntos, no mesmo quadro, no ciano chapado — medir um decide o outro
        cena.play(Create(fio), run_time=0.4 * VEL * kv)
        cena.play(*[q.animate.set_fill(CIANO, opacity=1) for q in par],
                  *[Flash(q, color=CIANO, line_length=0.25, flash_radius=0.5)
                    for q in par],
                  Indicate(fio, color=CIANO, scale_factor=1.0),
                  run_time=0.6 * VEL * kv)
        cena.play(FadeOut(par), FadeOut(fio), run_time=0.3 * VEL * kv)

    def _circuito(kv):
        # cap. 11: três fios, as portas descendo no fio de baixo (cada uma
        # presa a um fio de cima por um ponto de controle) e o flash da
        # medição na ponta
        cx, cy = moldura.get_center()[:2]
        x0, x1 = cx - 3.8, cx + 3.0
        ys = (cy + 0.9, cy + 0.2, cy - 0.5)
        fios = VGroup(*[Line([x0, y, 0], [x1, y, 0], color=PRETO,
                             stroke_width=2.5) for y in ys])
        portas = VGroup()
        for x, y_ctrl in ((cx - 2.0, ys[0]), (cx - 0.4, ys[1]),
                          (cx + 1.2, ys[0])):
            caixa = (Square(0.55).set_fill(CAIXA, opacity=1)
                     .set_stroke(PRETO, width=2.5).move_to([x, ys[2], 0]))
            haste = Line([x, y_ctrl, 0], caixa.get_top(), color=PRETO,
                         stroke_width=2.5)
            ctrl = Dot([x, y_ctrl, 0], radius=0.07, color=PRETO)
            portas.add(VGroup(haste, ctrl, caixa))
        medidor = (Square(0.55).set_fill(BRANCO, opacity=1)
                   .set_stroke(PRETO, width=2.5).move_to([x1, ys[2], 0]))
        mostrador = Arc(radius=0.18, start_angle=PI / 6, angle=2 * PI / 3,
                        color=PRETO, stroke_width=2.5)
        mostrador.move_to(medidor.get_center() + 0.02 * DOWN)
        agulha = Line(medidor.get_center() + 0.12 * DOWN,
                      medidor.get_center() + [0.14, 0.14, 0], color=PRETO,
                      stroke_width=2.5)
        medida = VGroup(medidor, mostrador, agulha)
        quadro = VGroup(fios, portas, medida)
        s, _ = _encaixa(quadro, moldura)
        _confere(quadro, moldura, "V1N14 circuito")

        cena.play(LaggedStart(*[Create(f) for f in fios], lag_ratio=0.2),
                  run_time=0.5 * VEL * kv)
        cena.play(LaggedStart(*[FadeIn(p, shift=1.2 * s * DOWN)
                                for p in portas],
                              lag_ratio=0.4), run_time=0.8 * VEL * kv)
        cena.play(FadeIn(medida),
                  Flash(medidor, color=AMARELO, line_length=0.3,
                        flash_radius=0.45), run_time=0.4 * VEL * kv)
        cena.play(FadeOut(VGroup(fios, portas, medida)), run_time=0.2 * VEL * kv)

    def _ondas(kv_soma, kv_vales, kv_picos):
        # cap. 11: quatro ondas empilhadas descem e se somam numa curva de
        # interferência com os picos espaçados — o período delas é o mesmo
        # 2,8 da tela, então os picos caem em cx e cx ± 2,8. Em "apaga" os
        # vales achatam e apagam, em "até sobrar" os picos crescem, e a seta
        # laranja pousa no pico da direita em "algoritmo de Shor"
        cx, cy = moldura.get_center()[:2]
        w = 2 * PI / 2.8
        a, b = cx - 4.2, cx + 4.2
        y0 = cy - 1.15
        ondas = VGroup(*[FunctionGraph(
            lambda x, j=j: cy + 1.35 - 0.35 * (j - 1)
            + 0.14 * np.cos(j * w * (x - cx)),
            x_range=[a, b, 0.02], color=AZUL, stroke_width=2.5)
            for j in range(1, 5)])

        def g(x):
            return 0.25 * sum(np.cos(j * w * (x - cx)) for j in range(1, 5))

        curva = FunctionGraph(lambda x: y0 + g(x), x_range=[a, b, 0.01],
                              color=PRETO, stroke_width=4)
        # a mesma curva cortada nos zeros de g ao lado de cada pico: com as
        # pontas em y0, esticar ou achatar um pedaço em torno de y0 não
        # descola dele os vizinhos
        dx = np.linspace(0.0, 1.4, 1401)
        meia = dx[np.argmax(g(cx + dx) < 0)]
        centros = (cx - 2.8, cx, cx + 2.8)
        faixas_pico = [(c - meia, c + meia) for c in centros]
        faixas_vale = [(a, centros[0] - meia),
                       *[(c1 + meia, c2 - meia)
                         for c1, c2 in zip(centros, centros[1:])],
                       (centros[-1] + meia, b)]

        def pedaco(x0, x1, amp):
            return FunctionGraph(lambda x: y0 + amp * g(x),
                                 x_range=[x0, x1, 0.01], color=PRETO,
                                 stroke_width=4)

        picos = VGroup(*[pedaco(x0, x1, 1.0) for x0, x1 in faixas_pico])
        vales = VGroup(*[pedaco(x0, x1, 1.0) for x0, x1 in faixas_vale])
        picos_altos = VGroup(*[pedaco(x0, x1, 1.6) for x0, x1 in faixas_pico])
        vales_rasos = VGroup(*[pedaco(x0, x1, 0.2).set_stroke(opacity=0.3)
                               for x0, x1 in faixas_vale])
        pico = np.array([cx + 2.8, y0 + 1.6, 0])
        seta = Arrow(pico + 1.3 * UP, pico + 0.08 * UP, buff=0, color=LARANJA,
                     stroke_width=6)
        quadro = VGroup(ondas, curva, picos, vales, picos_altos, vales_rasos,
                        seta)
        s, _ = _encaixa(quadro, moldura)
        _confere(quadro, moldura, "V1N14 ondas")

        cena.play(LaggedStart(*[Create(o) for o in ondas], lag_ratio=0.2),
                  run_time=0.55 * VEL * kv_soma)
        copias = [curva.copy() for _ in ondas]
        cena.play(*[ReplacementTransform(o, c) for o, c in zip(ondas, copias)],
                  run_time=0.65 * VEL * kv_soma)
        # a curva inteira dá lugar aos seus pedaços, no mesmo quadro
        cena.remove(*copias)
        cena.add(picos, vales)

        ancora("apaga")                      # "apaga as respostas erradas"
        cena.play(*[Transform(v, r) for v, r in zip(vales, vales_rasos)],
                  run_time=0.4 * VEL * kv_vales)
        ancora("até sobrar")                 # "até sobrar a ordem"
        cena.play(*[Transform(p, h) for p, h in zip(picos, picos_altos)],
                  run_time=0.5 * VEL * kv_picos)
        ancora("algoritmo de Shor")          # "E esse é o algoritmo de Shor"
        # é o último gesto da fala: a seta fica no pico até o fim dela, e
        # o fechamento da janela só vem no encerramento, já em silêncio
        cena.play(FadeIn(seta, shift=0.5 * s * DOWN), run_time=0.5 * VEL * k)

    # As janelas, em segundos do est= de 23,3 (todas escalam com k): o
    # fator de cada trecho é o que o faz ocupar a maior parte da sua, sem
    # chegar na âncora seguinte
    # "computador quântico" (≈ 0,089) → "lógica incomum": 2,1 s; o que o
    # V1N13 deixou sai em 1,0 s
    ancora("computador quântico")
    cena.play(FadeOut(sobra), run_time=1.0 * VEL * k)
    # "lógica incomum" (≈ 0,177) → "superposição": 3,0 s; o circuito, 1,4×
    # (2,7 s)
    ancora("lógica incomum")
    _circuito(1.4 * k)
    # "superposição" (≈ 0,304) → "emaranhamento": 4,8 s; os qubits, 6×
    # (3,0 s) — o gesto é um crescer só, mais lento que isso vira câmera
    # lenta, e os dois ficam parados ~1,8 s antes do fio
    ancora("superposição")
    par, fio = _cartoes(6.0 * k)
    # "emaranhamento" (≈ 0,509) → "interferência": 4,3 s; o par, 2,6×
    # (3,4 s)
    ancora("emaranhamento")
    _par(par, fio, 2.6 * k)
    # "interferência" (≈ 0,693) → "apaga": 1,1 s, curta para as ondas se
    # somarem — 0,85× (1,0 s); "apaga" → "até sobrar": 2,1 s, os vales em
    # 4× (1,6 s); "até sobrar" → "algoritmo de Shor": 2,5 s, os picos em
    # 4× (2,0 s)
    ancora("interferência")
    _ondas(0.85 * k, 4.0 * k, 4.0 * k)


def corpo_previa4(cena, titulo, trilha):
    """V1N13 e V1N14. A _abre_janela acende o 4 e abre a moldura; ela fica
    aberta nas duas falas — o 4 não troca de número entre elas, como o 3
    entre o V1N11 e o V1N12 — e o V1N14 termina com ela ainda aberta, a
    seta no pico. Na passagem de uma fala para a outra a janela fica com
    as árvores e o cadeado rachado do V1N13, que saem em "computador
    quântico".

    Devolve (titulo, trilha, moldura), em cena: o encerramento fecha a
    janela."""
    with narra(cena, "V1N13", 17.6):
        k = _k("V1N13", 17.6)
        t0 = _agora(cena)
        moldura, _ = _abre_janela(cena, titulo, trilha, 3, k)
        sobra = _previa_v4a(cena, moldura, t0)

    with narra(cena, "V1N14", 23.3):
        t0 = _agora(cena)
        _previa_v4b(cena, moldura, sobra, t0)

    return titulo, trilha, moldura


def encerramento(cena, titulo, trilha, moldura):
    """Depois do V1N14, sem fala. A janela do 4 fecha no passo das outras
    prévias, sem a pressa de caber na fala (o dobro dos 0,75 s da
    _fecha_janela), os quatro títulos acendem juntos e a trilha pulsa uma
    vez. A cena fica parada ~1,5 s e tudo sai num FadeOut só, o fim do
    vídeo 1."""
    _fecha_janela(cena, titulo, trilha, 3, moldura, 2.0)
    cena.play(trilha.animate.set_opacity(1), run_time=0.6 * VEL)
    cena.play(trilha.animate(rate_func=there_and_back).scale(1.1),
              run_time=0.6 * VEL)
    cena.wait(1.5 * VEL)
    cena.play(FadeOut(titulo), FadeOut(trilha), run_time=1.0 * VEL)
