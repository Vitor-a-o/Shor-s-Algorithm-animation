# -*- coding: utf-8 -*-
"""Vídeo 1 — Introdução: o vídeo inteiro mora aqui
(roteiro_video1_introducao.md). Não há capítulo por trás dele."""

from manim import *
import numpy as np

from ..paleta import (AMARELO, AZUL, BRANCO, CAIXA, CARTAO_ESCURO, CIANO,
                      CINZA, LARANJA, PRETO, ROSA, VERDE, VERDE2, VERMELHO, VEL)
from ..ferramentas import DUR, T, _agora, formula, narra, pot, traco
from ..cadeado import (_ABERTURA, abrir, cadeado, gravar, quebrar, rachar,
                       rede)
from .comum import VIDEOS, trilha_videos

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


def _pacote(cad):
    """Um pacote da rede do V1N00, na escala 1 do cadeado (o updater o
    encolhe): um envelope com `cad` fechado em pé em cima. O envelope fica
    centrado na origem — é o ponto que corre sobre a aresta.
    Devolve VGroup(envelope, cad), com envelope = VGroup(corpo, aba)."""
    corpo = RoundedRectangle(width=2.4, height=1.5, corner_radius=0.12)
    corpo.set_fill(CAIXA, opacity=1).set_stroke(CINZA, width=3)
    aba = VMobject().set_points_as_corners(
        [[-1.1, 0.66, 0], [0, -0.1, 0], [1.1, 0.66, 0]])
    aba.set_stroke(CINZA, width=3)
    cad.shift([0, 0.75, 0] - cad[1].get_bottom())
    return VGroup(VGroup(corpo, aba), cad)


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
    (a conta à mão não via a abertura da janela e empurrava o V1N07 2 s
    além da fala)."""
    return Wait(max(0.0, t0 + _em(tag, est, frac) - _agora(cena)))


def abertura(cena):
    """V1N00, o cartão silencioso e V1N01. O vídeo abre FALANDO, e já em
    movimento: a internet funcionando, pacotes com cadeado correndo pela
    rede. O empurrão isola um deles, e o cadeado desse pacote — `cad`, o
    MESMO objeto do vídeo inteiro — atravessa o cartão e abre no V1N01.

    Devolve (cad, bloco, interrogacoes), todos ainda em cena — o V1N02
    nasce em cima das interrogações e reabre o bloco, então nada disto
    sai aqui."""
    # --- montagem do V1N00 -----------------------------------------------
    tag, est = "V1N00", 9.6
    k = _k(tag, est)
    t_zoom = _em(tag, est, 0.185)          # "protege"
    t_para = _em(tag, est, 0.546)          # fim de "internet"
    freio = 1.8 * VEL * k                  # o escolhido freia até parar

    # a rede do V1N03 (mesma semente: é a mesma rede que volta lá), sem os
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
    with narra(cena, "V1N00", 9.6):
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
            Wait(max(0.0, _em(tag, est, 0.563) - t)),
            AnimationGroup(ReplacementTransform(envelope[0], campo),
                           FadeOut(envelope[1], scale=0.4,
                                   target_position=campo.get_center()),
                           run_time=0.6 * VEL * k)))
        t = _em(tag, est, 0.563) + 0.6 * VEL * k
        # "uma senha forte" ≈ 0,66: os pontos entram um a um, cada um num
        # estalo, com a pausa da digitação entre eles
        cena.play(Succession(
            Wait(max(0.0, _em(tag, est, 0.664) - t)),
            LaggedStart(*[GrowFromCenter(d) for d in senha], lag_ratio=3.0,
                        run_time=1.2 * VEL * k)))
        t = _em(tag, est, 0.664) + 1.2 * VEL * k
        # "que você possa" ≈ 0,80: riscado de vermelho...
        cena.play(Succession(
            Wait(max(0.0, _em(tag, est, 0.798) - t)),
            Create(risco, run_time=0.35 * VEL * k)))
        t = _em(tag, est, 0.798) + 0.35 * VEL * k
        # ...e em "escolher" ≈ 0,92 some. O cadeado não se mexeu: no fim da
        # fala ele está sozinho, grande, no centro
        cena.play(Succession(
            Wait(max(0.0, _em(tag, est, 0.924) - t)),
            AnimationGroup(*[FadeOut(m, shift=0.4 * DOWN)
                             for m in (campo, *senha, risco)],
                           run_time=0.6 * VEL * k)))
    cad.set_z_index(0)

    # --- cartão silencioso: o título entra e o cadeado sai do caminho dele,
    # encolhendo para cima — sem sair de cena. Ele sai mais depressa e o
    # título começa um pouco depois: quando a escrita chega ao meio da
    # linha, o cadeado já não está lá
    t1 = T("Do Zero ao Algoritmo de Shor Quântico", 42)
    t2 = T(f"Vídeo 1 de 4 — {VIDEOS[0]}", 28, CINZA)
    VGroup(t1, t2).arrange(DOWN, buff=0.5)
    cena.play(cad.animate(run_time=0.7 * VEL).scale(_SELO / _GRANDE)
                 .next_to(t1, UP, buff=0.45),
              Succession(Wait(0.3 * VEL), Write(t1, run_time=0.8 * VEL)))
    cena.play(FadeIn(t2, shift=0.25 * UP), run_time=0.8 * VEL)
    cena.wait(1.0 * VEL)
    cena.play(FadeOut(t1), FadeOut(t2), run_time=0.6 * VEL)

    # --- V1N01 -----------------------------------------------------------
    # o cadeado volta ao centro no tamanho natural; os itens se posicionam
    # pelo lugar aonde ele vai chegar
    cad.generate_target()
    cad.target.scale(1 / _SELO)
    cad.target.shift([0, 0.9, 0] - cad.target[1].get_center())

    itens = VGroup(T("contas bancárias", 30), T("compras online", 30),
                   T("mensagens privadas", 30))
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
    volta = Arrow([2.4, _FAIXA, 0], [-2.55, _FAIXA, 0], buff=0, color=PRETO,
                  stroke_width=5)
    interrogacoes = VGroup(*[T("?", 36, CINZA) for _ in _ESPALHA])
    for q, x in zip(interrogacoes, np.linspace(2.2, -2.35, len(_ESPALHA))):
        q.move_to([x, _FAIXA, 0])

    with narra(cena, "V1N01", 14.2):
        tag, est = "V1N01", 14.2
        k = _k(tag, est)
        # "Ela está por trás de...": o cadeado desce ao centro e abre em
        # silêncio (os mesmos 2,0 s dos dois plays do rótulo de antes: as
        # contas de Wait abaixo continuam valendo)
        cena.play(MoveToTarget(cad), run_time=1.2 * VEL * k)
        abrir(cena, cad, run_time=0.8 * k)
        # "contas bancárias" ≈ 0,11 (o play acima já cobre) · "compras
        # online" ≈ 0,20 · "mensagens privadas" ≈ 0,29 — uma a cada respiro
        cena.play(FadeIn(itens[0], shift=0.3 * RIGHT), run_time=0.8 * VEL * k)
        cena.play(Succession(Wait(max(0.0, _em(tag, est, 0.202) - k * 2.8)),
                             FadeIn(itens[1], shift=0.3 * LEFT,
                                    run_time=0.8 * VEL * k)))
        cena.play(Succession(
            Wait(max(0.0, _em(tag, est, 0.290) - k * 3.668)),
            FadeIn(itens[2], shift=0.3 * UP, run_time=0.8 * VEL * k)))
        # e se condensam dentro dele
        cena.play(*[it.animate.scale(0.05).move_to(cad[1]).set_opacity(0)
                    for it in itens],
                  run_time=1.2 * VEL * k)
        cena.remove(*itens)

        # "operações": os dois fatores cinzas na faixa de baixo
        cena.play(FadeIn(f1, shift=0.2 * UP), FadeIn(f2, shift=0.2 * UP),
                  run_time=1.2 * VEL * k)
        # "fáceis de fazer numa direção" ≈ 0,61: a seta varre para a
        # direita...
        cena.play(Succession(
            Wait(max(0.0, _em(tag, est, 0.611) - k * 7.318)),
            GrowArrow(ida, run_time=1.6 * VEL * k)))
        # ...e os fatores se fundem no bloco no instante em que o cadeado
        # trava — o play é o do _fechar() (o fechar() com o pivô no pé)
        _no_mesmo_play(cena, [ReplacementTransform(f1, bloco[0]),
                              ReplacementTransform(f2, bloco[1]),
                              FadeOut(ida)],
                       _fechar, cad, run_time=0.6 * k)

        # "impraticáveis de desfazer" ≈ 0,77: a volta tenta e se despedaça
        cena.play(Succession(
            Wait(max(0.0, _em(tag, est, 0.772) - k * 10.876)),
            GrowArrow(volta, run_time=1.0 * VEL * k)))
        cena.play(ReplacementTransform(volta, interrogacoes),
                  run_time=0.6 * VEL * k)
        # as interrogações se espalham e o cadeado chacoalha sem abrir
        cena.play(*[q.animate.shift([dx, dy, 0]).rotate(ang * DEGREES)
                    for q, (dx, dy, ang) in zip(interrogacoes, _ESPALHA)],
                  Wiggle(cad), run_time=1.2 * VEL * k)

    return cad, bloco, interrogacoes


def _anos(e):
    """O contador do V1N02: 10^e − 1 anos, com ponto de milhar."""
    return f"{int(10 ** e) - 1:,}".replace(",", ".")


def _contador(e, ponto):
    """O contador do V1N02, que dispara de novo no V1N11: segue o
    ValueTracker `e` e engorda com ele, centrado em `ponto`."""
    return always_redraw(
        lambda: T(_anos(e.get_value()), 44)
        .scale(1 + e.get_value() / 10).move_to(ponto))


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
    contador = _contador(e, ponto)

    with narra(cena, "V1N02", 18.3):
        tag, est = "V1N02", 18.3
        k = _k(tag, est)
        # "fatoração" ≈ 0,15 da fala, mas o roteiro pede que ela nasça "logo
        # nos primeiros segundos" — ou seja, ANTES da fração mecânica da
        # palavra, não nela: fica imediato, só com o run_time esticado
        cena.play(Write(fat), FadeOut(interrogacoes), run_time=1.4 * VEL * k)
        cena.play(Succession(
            fat.animate(run_time=1.2 * VEL * k).scale(0.55)
               .to_edge(UP, buff=0.4),
            Wait(0.5 * VEL * k)))

        # "Multiplicar dois primos grandes" ≈ 0,20: o bloco se reabre pela
        # emenda e cada metade volta a ser o fator cinza de que era feita...
        cena.play(Succession(
            Wait(max(0.0, _em(tag, est, 0.195) - k * 3.1)),
            AnimationGroup(Transform(bloco[0], cinzas[0]),
                          Transform(bloco[1], cinzas[1]),
                          run_time=1.0 * VEL * k)))
        # ...que ganha identidade: rosa é p, verde-claro é q, e cada número
        # nasce de dentro do seu quadrado
        cena.play(bloco[0].animate.set_fill(ROSA),
                  bloco[1].animate.set_fill(VERDE2),
                  GrowFromPoint(p, cinzas[0].get_center()),
                  GrowFromPoint(q, cinzas[1].get_center()),
                  run_time=0.9 * VEL * k)
        # os dois deslizam um contra o outro e se fundem de novo no mesmo
        # bloco laranja; os números se juntam no produto, por cima dele
        cena.play(Transform(bloco[0], fechado[0]),
                  Transform(bloco[1], fechado[1]),
                  ReplacementTransform(VGroup(p, q), n), run_time=1.2 * VEL * k)

        # "voltar do produto para os primos" ≈ 0,37: a volta tenta de novo
        # e se despedaça, no mesmo espalhar do V1N01
        cena.play(Succession(
            Wait(max(0.0, _em(tag, est, 0.365) - k * 6.6685)),
            GrowArrow(volta, run_time=1.0 * VEL * k)))
        cena.play(ReplacementTransform(volta, cacos), run_time=0.6 * VEL * k)
        cena.play(Succession(
            AnimationGroup(*[c.animate.shift([dx, dy, 0]).rotate(ang * DEGREES)
                             for c, (dx, dy, ang) in zip(cacos, _ESPALHA)],
                           run_time=1.2 * VEL * k),
            Wait(0.6 * VEL * k)))

        # "bilhões de anos" ≈ 0,77 (target 14,0 s de 18,3), mas o rabo deste
        # bloco (contador + saída) já soma 5,6 s fixos: puxar para a fração
        # exata estouraria a locução em ~1,3 s. Capado no último instante
        # que ainda cabe (12,7 s de 18,3 — fração efetiva ≈0,69), para o
        # bloco fechar exatamente no fim da fala, sem sobra nem estouro
        cena.play(Succession(
            Wait(max(0.0, k * (est - 5.6 - 10.0795))),
            AnimationGroup(FadeOut(cacos), *[FadeOut(m) for m in bloco],
                          FadeOut(n), FadeIn(contador),
                          run_time=0.8 * VEL * k)))
        cena.play(e.animate.set_value(10), run_time=3.0 * VEL * k,
                  rate_func=linear)
        contador.clear_updaters()
        cena.play(FadeOut(contador, scale=4), run_time=0.6 * VEL * k)

        # o cadeado fica sozinho, no centro
        cena.play(FadeOut(fat), cad.animate.move_to(ORIGIN),
                  run_time=1.2 * VEL * k)

    return cacos


def corpo_rsa(cena, cad):
    """V1N03. O cadeado ganha as letras RSA e encolhe no miolo de uma rede
    de cadeados anônimos, que brotam de trás dele.

    Devolve a rede — VGroup(arestas, pontos, cadeados), tudo em cena — para
    o V1N04 piscá-la e estalá-la."""
    malha = rede()
    arestas, pontos, anonimos = malha

    with narra(cena, "V1N03", 20.0):
        tag, est = "V1N03", 20.0
        k = _k(tag, est)
        # "é o RSA" ≈ 0,22: o cadeado cresce e as letras se gravam com o
        # flash seco do travamento
        cena.play(Succession(
            Wait(max(0.0, _em(tag, est, 0.219))),
            cad.animate(run_time=2.2 * VEL * k).scale(1.4)))
        gravar(cena, cad, "RSA", run_time=0.9 * k)
        # o aceso vai na frente de tudo o que nascer daqui em diante: a rede
        # é desenhada DEPOIS dele e mesmo assim fica atrás (depois do
        # gravar(), para as letras subirem junto com o corpo)
        cad.set_z_index(1)

        # "não é o único" ≈ 0,68: o cadeado encolhe e a rede se desenha ao
        # fundo, já apagada
        cena.play(Succession(
            Wait(max(0.0, _em(tag, est, 0.683) - k * 7.48)),
            AnimationGroup(cad.animate.scale(0.8 / 1.4),
                           Create(arestas),
                           LaggedStart(*[GrowFromCenter(d) for d in pontos],
                                       lag_ratio=0.15),
                           run_time=1.6 * VEL * k)))
        # os anônimos brotam de trás dele e pousam cada um na sua aresta
        for c in anonimos:
            c.generate_target()
            c.move_to(cad[1])
        cena.add(anonimos)
        cena.play(LaggedStart(*[MoveToTarget(c) for c in anonimos],
                              lag_ratio=0.12), run_time=1.8 * VEL * k)

        # "nem vai ser o único a cair" ≈ 0,88: todos pulsam uma vez, junto
        cena.play(Succession(
            Wait(max(0.0, _em(tag, est, 0.879) - k * 17.06)),
            AnimationGroup(*[c.animate.scale(1.35) for c in anonimos],
                          rate_func=there_and_back, run_time=0.8 * VEL * k)))

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
    tag, est = "V1N04", 17.9
    kv = _k(tag, est)
    qubits, quando = VGroup(), []
    for f, altura in _QUBITS:
        for k in range(altura):
            qubits.add(_qubit().move_to(
                [x0 + f * (x1 - x0), _LINHA + 0.2 + 0.17 * k, 0]))
            quando.append((f, k))               # onde na linha, que andar
    varre = 2.1 * VEL * kv                      # a linha vai de 1994 a hoje

    with narra(cena, "V1N04", 17.9):
        # "vence essa aposta" ≈ 0,37: as interrogações voltam onde pararam e
        # o espalhar se desfaz, de trás para frente, até a linha da seta...
        cena.play(Succession(Wait(max(0.0, _em(tag, est, 0.368))),
                             FadeIn(interrogacoes, run_time=0.2 * VEL * kv)))
        cena.play(*[c.animate.rotate(-ang * DEGREES).shift([-dx, -dy, 0])
                    for c, (dx, dy, ang) in zip(interrogacoes, _ESPALHA)],
                  run_time=0.4 * VEL * kv)
        # ...e a volta que era impossível acontece: as da esquerda viram o
        # 3, as da direita o 11 (elas nasceram da direita para a esquerda)
        cena.play(ReplacementTransform(interrogacoes[4:], p),
                  ReplacementTransform(interrogacoes[:4], q),
                  run_time=0.6 * VEL * kv)

        # "não só a do RSA" ≈ 0,46: os anônimos piscam uma vez, acesos por
        # inteiro (o arco pelo traço: um fill no arco tamparia a aresta atrás
        # dele). O there_and_back vai em cada um, não no grupo: o finish() do
        # grupo leva cada animação ao fim dela, e eles ficariam acesos
        pisca = dict(rate_func=there_and_back)
        cena.play(Succession(
            Wait(max(0.0, _em(tag, est, 0.461) - kv * 7.7872)),
            AnimationGroup(
                *[c[1].animate(**pisca).set_opacity(1) for c in anonimos],
                *[c[0].animate(**pisca).set_stroke(opacity=1) for c in anonimos],
                run_time=0.8 * VEL * kv)))

        # "nos últimos anos" ≈ 0,61: os primos se recolhem no ponto de
        # 1994... (glifo a glifo, cada um num ponto: do Text inteiro para o
        # Dot, os glifos sumiam no lugar em vez de viajar)
        copias = [d94.copy() for _ in range(len(p) + len(q) - 1)]
        cena.play(Succession(
            Wait(max(0.0, _em(tag, est, 0.605) - kv * 9.0519)),
            AnimationGroup(
                *[ReplacementTransform(g, d)
                  for g, d in zip([*p, *q], [d94, *copias])],
                FadeIn(r94, shift=0.15 * UP), run_time=0.8 * VEL * kv)))
        cena.remove(*copias)
        # ...e a linha corre até hoje; cada qubit nasce quando ela passa, e
        # a coluna sobe um andar de cada vez
        cena.play(Create(linha, rate_func=linear, run_time=varre),
                  *[Succession(Wait(f * varre + 0.05 * k * VEL * kv),
                               GrowFromCenter(u, run_time=0.25 * VEL * kv))
                    for u, (f, k) in zip(qubits, quando)],
                  Succession(Wait(varre - 0.2 * VEL * kv), AnimationGroup(
                      GrowFromCenter(hoje), FadeIn(rhoje, shift=0.15 * UP),
                      run_time=0.4 * VEL * kv)))

        # "prazo de validade" ≈ 0,92 (target 16,5 s de 17,9), mas o rabo
        # deste bloco (fade da linha + crescer + rachar + quebrar + estalar
        # a rede, 3,31 s fixos) não cabe atrás dela: capado no último
        # instante que ainda fecha o bloco sem estourar (fração efetiva
        # ≈0,82, bem perto do que o Wait(0,4) antigo já fazia por tentativa)
        alvo7 = min(_em(tag, est, 0.921), kv * (est - 3.31))
        cena.play(Succession(Wait(max(0.0, alvo7 - kv * 14.1245)),
                             AnimationGroup(
            *[FadeOut(m) for m in (linha, d94, hoje, r94, rhoje, *qubits)],
            cad.animate.scale(1.2 / 0.8), run_time=0.8 * VEL * kv)))

        # o z_index do V1N03 punha o cadeado na frente da rede; mas a fissura
        # do rachar() e as corridas do quebrar() nascem no z 0, e ficariam
        # POR BAIXO do traço do arco. Volta ao 0 e vai para a frente pela
        # ordem da cena
        cad.set_z_index(0)
        cena.bring_to_front(cad)
        # e quebra, num gesto só: a rachadura mal aparece e já corre até as
        # pontas
        rachar(cena, cad, run_time=0.25 * kv)
        pecas = quebrar(cena, cad, run_time=1.4 * kv)

        # os anônimos estalam em cascata, do centro para fora — o quebrar()
        # já passou ~0,75 s do estalo, a folga do "meio segundo depois"
        ordem = sorted(anonimos,
                       key=lambda c: np.linalg.norm(c.get_center()
                                                    - cad[1].get_center()))
        estalos = [_estalar_rede(cena, c, run_time=0.5 * kv) for c in ordem]
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
        tag, est = "V1N05", 8.3
        k = _k(tag, est)
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
                  run_time=0.6 * VEL * k)
        # "a promessa, ou a ameaça, do algoritmo de Shor": sobem e viram as
        # letras, da esquerda para a direita
        cena.play(LaggedStart(*[ReplacementTransform(c, a) for c, a in pares],
                              lag_ratio=0.08), run_time=2.4 * VEL * k)
        # as letras entraram soltas; o título volta a ser um só
        cena.remove(*[a for _, a in pares])
        cena.add(titulo)
        # "esta série" ≈ 0,75: os quatro vídeos saem de trás do título,
        # apagados
        cena.play(Succession(
            Wait(max(0.0, _em(tag, est, 0.750) - k * 3.0)),
            AnimationGroup(
                *[FadeIn(n, target_position=[n.get_x(), 0, 0]) for n in nomes],
                run_time=1.0 * VEL * k)))

    with narra(cena, "V1N06", 8.3):
        tag, est = "V1N06", 8.3
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
        alvo = max(_em(tag, est, 0.263),
                   0.85 * _dur(tag, est) - 0.8 * VEL * k)
        cena.play(Succession(Wait(max(0.0, alvo - k * 2.4)), AnimationGroup(
            Restore(trilha[0]), GrowFromCenter(marca),
            run_time=0.8 * VEL * k)))

    return titulo, trilha, marca


def _abre_janela(cena, titulo, trilha, i, k, some=(), rotulo=None):
    """Abre a prévia do vídeo i + 1 — a MESMA nas três aberturas (V1N07,
    V1N08, V1N10): o item i da trilha acende e os outros saem (junto com
    `some`, a marca do V1N06), ele sobe para o topo e a moldura nasce de
    uma linha que sai do pé dele e se expande. Só então o conteúdo começa.

    0,80 s × k: acende 0,15 · sobe 0,30 · linha 0,15 · expande 0,20.

    `rotulo`, quando dado (o "Fermat" do V1N08), entra no canto superior-
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
    volta 0,25. Deixa a `trilha` em cena como um VGroup só, como o V1N06 a
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
    # to_edge do V1N06; trilha_videos já a devolve apagada)
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
    """V1N07 — os dez trechos da decupagem (roteiro_video1_introducao.md,
    V1N07), na ordem exata da tabela: capítulos 1, 2, 3, 4, 2, 2, 1, 5, 5,
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
    tag, est = "V1N07", 20.3
    k = _k(tag, est)

    def rt(s):
        return s * VEL * k

    def ancora(seg, sai=None):
        """Espera até `seg` s da fala e apaga `sai` nos 0,12 s antes."""
        fo = rt(0.12) if sai is not None else 0.0
        espera = _ate(cena, t0 - fo, tag, est, seg / est)
        if espera.run_time > 1e-3:
            cena.play(espera)
        if sai is not None:
            cena.play(FadeOut(sai), run_time=fo)

    def cap1():
        (reta, b11, r11, tres, r3s, tenta, r3x, xis, s2, r2,
         bate) = pecas = _v2_cap1()
        quadro = VGroup(*pecas[:-1])
        s, leva = _encaixa(quadro, moldura)
        _confere(quadro, moldura, "V1N07 cap. 1")
        return pecas[:-1] + (leva(bate), s)

    def cap2():
        reta, soma, atual, estados = pecas = _v2_cap2()
        quadro = VGroup(reta, soma, atual, *estados)
        _encaixa(quadro, moldura)
        _confere(quadro, moldura, "V1N07 cap. 2")
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
        ancora(5.6, sai)
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
        _confere(base, moldura, "V1N07 cap. 3")
        segs, rots = base
        ancora(7.2, sai)
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
        _confere(quadro, moldura, "V1N07 cap. 4")
        ancora(8.6, sai)
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
        # 11,6–12,8 · cap. 2 (C2N07): os quatro estados n = 8…11 em
        # ReplacementTransform — o x engorda e o c vira um ponto
        reta, soma, atual, estados = cap2()
        n7, x2, cver, rn, rx, rc = atual
        ancora(10.1, sai)
        cena.play(FadeIn(reta), FadeIn(soma), run_time=rt(0.12))
        cena.play(AnimationGroup(
            Create(n7, run_time=rt(0.63), rate_func=linear),
            Succession(Wait(rt(0.45)),
                       Create(x2, run_time=rt(0.18), rate_func=linear))))
        cena.play(FadeIn(rn), FadeIn(rx), run_time=rt(0.18))
        cena.play(Create(cver), FadeIn(rc), run_time=rt(0.25))

        ancora(11.6)
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
        ancora(12.8, sai)
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
        _confere(quadro, moldura, "V1N07 cap. 5 (filas)")
        ancora(14.6, sai)
        for f in filas2:
            cena.play(Succession(
                AnimationGroup(FadeIn(f[0]), Create(f[2]),
                               run_time=rt(0.13)),
                LaggedStart(*[Create(s) for s in f[1]], lag_ratio=0.2,
                            run_time=rt(0.16)),
                AnimationGroup(*[FadeIn(m) for m in f[3:]],
                               run_time=rt(0.14))))
        ancora(16.2, filas2)
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
        _confere(quadro, moldura, "V1N07 cap. 5 (tabela)")
        ancora(18.0, sai)
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
    """V1N07. A _abre_janela acende o 2, os outros três (e a marca) somem,
    o 2 sobe para o topo — ele é o rótulo da janela — e a moldura nasce;
    a prévia do vídeo 2 roda dentro dela e a _fecha_janela devolve o 2 à
    trilha, apagada, no fim da fala.

    Devolve (titulo, trilha), em cena: o V1N08 abre o 3 do mesmo jeito."""
    with narra(cena, "V1N07", 20.3):
        k = _k("V1N07", 20.3)
        t0 = _agora(cena)
        moldura, _ = _abre_janela(cena, titulo, trilha, 1, k, some=(marca,))
        _previa_v2(cena, moldura, t0)
        _fecha_janela(cena, titulo, trilha, 1, moldura, k)

    return titulo, trilha


def _previa_v3a(cena, moldura, fermat, t0):
    """V1N08 — cap. 6 (Fermat: a permutação da tabela mod 7) e cap. 7
    (Euler: o contra-exemplo mod 9), na ordem exata da tabela.

    `fermat` é o rótulo que a _abre_janela pôs na moldura; em 5,4 ele vira
    "Euler" no mesmo lugar. Devolve o "Euler" (em cena): o V1N09 o recebe
    e o vira "RSA" no mesmo canto, e só a _fecha_janela do fim do V1N09
    leva esse rótulo junto com o conteúdo.

    Três encaixes: a tabela mod 7 com os arcos (0,0–5,4, a mesma cena), a
    mod 9 com as cruzes, as chaves e a caixa (5,4–11,0), o cadeado."""
    tag, est = "V1N08", 12.1
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
    _confere(quadro, moldura, "V1N08 tabela mod 7")

    cena.play(LaggedStart(*[FadeIn(l) for l in linhas], lag_ratio=0.25),
              run_time=1.3 * VEL * k)
    # ≈ 0,182 da fala: a elipse entra e liga a linha 1 à sua fileira de cima
    cena.play(Succession(
        _ate(cena, t0, tag, est, 0.182),
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
    _confere(quadro, moldura, "V1N08 tabela mod 9")

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
    _confere(mini_cad, moldura, "V1N08 cadeado")
    cena.play(FadeOut(VGroup(chave_e, restantes, chave_d, caixa)),
              FadeIn(mini_cad), run_time=0.5 * VEL * k)
    cena.play(FadeOut(mini_cad), run_time=0.6 * VEL * k)

    return euler


def _previa_v3b(cena, moldura, euler, t0):
    """V1N09 — cap. 8: o esquema do RSA (mensagem → cifra → mensagem),
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
    tag, est = "V1N09", 12.5
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
    pub = _caixa("pública", CINZA, PRETO, largura=1.5).scale(0.75)
    pub.move_to(seta1.get_center() + [0, 0.9, 0])
    priv = _caixa("privada", AMARELO, PRETO, largura=1.5).scale(0.75)
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
    _confere(quadro, moldura, "V1N09 esquema do RSA")

    cena.play(LaggedStart(FadeIn(msg1, shift=0.2 * s * RIGHT), GrowArrow(seta1),
                          FadeIn(cif, shift=0.2 * s * RIGHT), GrowArrow(seta2),
                          FadeIn(msg2, shift=0.2 * s * RIGHT), lag_ratio=0.5),
              run_time=2.6 * VEL * k)

    # "RSA" ≈ 0,236 da fala (38 / 161 caracteres, o começo da palavra
    # "RSA" no texto do V1N09): "Euler" vira "RSA" no rótulo da janela
    cena.play(Succession(
        _ate(cena, t0, tag, est, 0.236),
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
    """V1N08 e V1N09. A _abre_janela acende o 3 e abre a moldura com
    "Fermat" como rótulo; ela fica aberta nas duas falas — o 3 é o único
    título da trilha que não troca de número — e só a _fecha_janela do fim
    do V1N09 a fecha, devolvendo o 3 à trilha.

    Devolve (titulo, trilha), em cena: o V1N10 abre o 4 do mesmo jeito."""
    with narra(cena, "V1N08", 12.1):
        k = _k("V1N08", 12.1)
        t0 = _agora(cena)
        moldura, fermat = _abre_janela(cena, titulo, trilha, 2, k,
                                       rotulo="Fermat")
        euler = _previa_v3a(cena, moldura, fermat, t0)

    with narra(cena, "V1N09", 12.5):
        k = _k("V1N09", 12.5)
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
    """V1N10 — cap. 9, cap. 10 e de novo cap. 9, na ordem da decupagem: a
    tabela mod 9 se preenche e o zigue-zague começa a percorrê-la sem
    fechar o ciclo; as árvores do cap. 10 entram no meio; a MESMA tabela
    volta com o zigue-zague onde ele parou, o último arco fecha o ciclo e
    o flash amarelo dá a volta. Como nas prévias anteriores, cada trecho
    recria só o gesto mínimo, sem importar capitulo9/9b/10, e passa por
    _encaixa e _confere antes de animar.

    `t0` é o começo do narra do V1N10. Devolve o ciclo fechado, em cena:
    o V1N11 congela a janela nele."""
    tag, est = "V1N10", 11.0
    k = _k(tag, est)

    def ancora(frac):
        espera = _ate(cena, t0, tag, est, frac)
        if espera.run_time > 1e-3:
            cena.play(espera)

    def _arvores(kv):
        # cap. 10: um tronco, duas árvores; os ramos que se repetem nos dois
        # lados acendem juntos, o resto cai e sobram dois números pequenos
        # (o 7 e o 9 do 2³ − 1 e do 2³ + 1 — ainda não o 3 × 7)
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
        quadro = VGroup(tronco, *filhos, *netos, *folhas, numeros)
        _, leva = _encaixa(quadro, moldura)
        _confere(quadro, moldura, "V1N10 árvores")
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
        cena.play(FadeOut(VGroup(tronco, *filhos, *acesos, numeros)),
                  run_time=0.2 * VEL * kv)

    (head_c, head_l, lin_h, lin_v, linhas_cel, c00, degraus, fecha,
     caminho) = pecas = _v4_tabela()
    quadro = VGroup(*pecas)
    _encaixa(quadro, moldura)
    _confere(quadro, moldura, "V1N10 tabela mod 9")
    no_ar = VGroup(head_c, head_l, lin_h, lin_v, linhas_cel, c00, degraus)

    # 0,0–5,2 · cap. 9 (C9N03): depois da _abre_janela (0,8 s), cabeçalhos
    # e linhas-guia, e as nove linhas em LaggedStart, uma a uma
    cena.play(FadeIn(head_c), FadeIn(head_l), Create(lin_h), Create(lin_v),
              run_time=0.4 * VEL * k)
    cena.play(LaggedStart(*[FadeIn(l) for l in linhas_cel], lag_ratio=0.25),
              run_time=1.8 * VEL * k)
    # ≈ 0,319 "entra a ordem modular" (C9N05–C9N08): o 1 de partida acende
    # e o zigue-zague desce, sobe, desce, sobe, desce — para no 1 da
    # linha 4, sem o arco que fecha o ciclo
    ancora(0.319)
    cena.play(Create(c00), run_time=0.25 * VEL * k)
    cena.play(LaggedStart(*[AnimationGroup(
        GrowArrow(seg) if isinstance(seg, Arrow) else Create(seg),
        Create(circ)) for seg, circ in degraus], lag_ratio=1.0),
        run_time=1.35 * VEL * k)

    # 5,2–8,4 · cap. 10 (≈ 0,473, "Com ela"): a tabela sai e as árvores
    # entram, com os gestos 1,3× mais longos que na prévia de uma fala só
    ancora(0.473)
    cena.play(FadeOut(no_ar), run_time=0.2 * VEL * k)
    _arvores(1.3 * k)

    # 8,4–11,0 · volta ao cap. 9 (≈ 0,764): a MESMA tabela, com o
    # zigue-zague onde parou; em "procurar" (≈ 0,870) o último arco fecha o
    # ciclo de volta no 1 de partida (C9N09) e o flash amarelo dá uma
    # volta inteira no caminho
    ancora(0.764)
    cena.play(FadeIn(no_ar), run_time=0.4 * VEL * k)
    ancora(0.870)
    cena.play(Create(fecha), Indicate(c00, color=VERDE),
              run_time=0.6 * VEL * k)
    cena.play(LaggedStart(*[ShowPassingFlash(
        p.copy().set_stroke(AMARELO, width=7), time_width=1.0)
        for p in caminho], lag_ratio=1.0), run_time=0.7 * VEL * k)

    return VGroup(no_ar, fecha)


def _previa_v4b(cena, moldura, ciclo, t0):
    """V1N11 — os três trechos do cap. 11 dentro da MESMA moldura: nada
    aqui a reabre, porque o 4 não troca de número nesta fala, o mesmo
    recurso do V1N09. Os trechos são os da prévia de uma fala só; mudam
    só de lugar e de tempo, e as ondas ganham os vales e os picos que o
    roteiro pede sob "se cancelam" e "se reforçam".

    `ciclo` é o que a _previa_v4a deixou em cena, e sai por FadeOut assim
    que a fala chega em "quântico"; `t0` é o começo do narra do V1N11.
    Termina com a seta laranja no pico: a _fecha_janela vem logo depois,
    no corpo_previa4."""
    tag, est = "V1N11", 18.7
    k = _k(tag, est)

    def ancora(frac):
        espera = _ate(cena, t0, tag, est, frac)
        if espera.run_time > 1e-3:
            cena.play(espera)

    def _qubits(kv):
        # cap. 11: o mesmo círculo ciano dos qubits da linha do tempo do
        # V1N04, grande, com o gradiente dos bits 1 e 0 dentro (a
        # superposição); o fio liga os dois e eles colapsam juntos, no
        # mesmo quadro, no ciano chapado
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
        _confere(quadro, moldura, "V1N11 qubits")
        cena.play(LaggedStart(*[GrowFromCenter(q) for q in par],
                              lag_ratio=0.3), run_time=0.5 * VEL * kv)
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
        _confere(quadro, moldura, "V1N11 circuito")

        cena.play(LaggedStart(*[Create(f) for f in fios], lag_ratio=0.2),
                  run_time=0.5 * VEL * kv)
        cena.play(LaggedStart(*[FadeIn(p, shift=1.2 * s * DOWN)
                                for p in portas],
                              lag_ratio=0.4), run_time=0.8 * VEL * kv)
        cena.play(FadeIn(medida),
                  Flash(medidor, color=AMARELO, line_length=0.3,
                        flash_radius=0.45), run_time=0.4 * VEL * kv)
        cena.play(FadeOut(VGroup(fios, portas, medida)), run_time=0.2 * VEL * kv)

    def _ondas():
        # cap. 11: quatro ondas empilhadas descem e se somam numa curva de
        # interferência com os picos espaçados — o período delas é o mesmo
        # 2,8 da tela, então os picos caem em cx e cx ± 2,8. Sob "se
        # cancelam" os vales achatam e apagam, sob "se reforçam" os picos
        # crescem, e a seta laranja pousa no pico da direita
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
        _confere(quadro, moldura, "V1N11 ondas")

        cena.play(LaggedStart(*[Create(o) for o in ondas], lag_ratio=0.2),
                  run_time=0.55 * VEL * k)
        copias = [curva.copy() for _ in ondas]
        cena.play(*[ReplacementTransform(o, c) for o, c in zip(ondas, copias)],
                  run_time=0.65 * VEL * k)
        # a curva inteira dá lugar aos seus pedaços, no mesmo quadro
        cena.remove(*copias)
        cena.add(picos, vales)

        ancora(0.737)                       # "se cancelam"
        cena.play(*[Transform(v, r) for v, r in zip(vales, vales_rasos)],
                  run_time=0.4 * VEL * k)
        ancora(0.817)                       # "se reforçam"
        cena.play(*[Transform(p, h) for p, h in zip(picos, picos_altos)],
                  run_time=0.5 * VEL * k)
        ancora(0.866)                       # "E esse é o algoritmo de Shor"
        cena.play(FadeIn(seta, shift=0.5 * s * DOWN), run_time=0.5 * VEL * k)

    # 0,0–6,2: a janela fica parada no ciclo fechado que o V1N10 deixou,
    # até "quântico" (≈ 0,332), quando o ciclo sai
    ancora(0.332)
    cena.play(FadeOut(ciclo), run_time=0.3 * VEL * k)

    # 6,2–9,4 · cap. 11 ("Então"): os qubits, 1,6× mais lentos
    _qubits(1.6 * k)
    # 9,4–12,6 · cap. 11 (≈ 0,503, "circuito"): o circuito, 1,2×
    ancora(0.503)
    _circuito(1.2 * k)
    # 12,6–16,4 · cap. 11 (≈ 0,674): as ondas se somam na curva de
    # interferência
    ancora(0.674)
    _ondas()


def corpo_previa4(cena, titulo, trilha):
    """V1N10 e V1N11. A _abre_janela acende o 4 e abre a moldura; ela fica
    aberta nas duas falas — o 4 não troca de número entre elas, como o 3
    entre o V1N08 e o V1N09 — e só a _fecha_janela do fim do V1N11 a
    fecha, devolvendo o 4 à trilha. No corte, o 21 = 3 × 7 entra grande —
    a única fórmula fixa das prévias (roteiro, "Critério das prévias"):
    nasce de um corte seco, sem Write e sem transformar outra fórmula —,
    no centro do espaço livre à direita da trilha, que já voltou. Por fim
    os quatro títulos acendem juntos e a trilha pulsa uma vez.

    Devolve (titulo, trilha, fatoracao), em cena: o encerramento (V1N12)
    os tira de baixo para cima."""
    fatoracao = formula(("21", LARANJA), ("=", PRETO), ("3", ROSA),
                        ("×", PRETO), ("7", VERDE2), tamanho=96, buff=0.3)

    with narra(cena, "V1N10", 11.0):
        k = _k("V1N10", 11.0)
        t0 = _agora(cena)
        moldura, _ = _abre_janela(cena, titulo, trilha, 3, k)
        ciclo = _previa_v4a(cena, moldura, t0)

    with narra(cena, "V1N11", 18.7):
        tag, est = "V1N11", 18.7
        k = _k(tag, est)
        t0 = _agora(cena)
        _previa_v4b(cena, moldura, ciclo, t0)
        _fecha_janela(cena, titulo, trilha, 3, moldura, k)

        # o corte: o 21 = 3 × 7 entra seco, no meio do que sobra à direita
        # da trilha (no centro do quadro ele cobriria a ponta dela)
        fatoracao.move_to([(trilha.get_right()[0] + config.frame_width / 2)
                           / 2, 0, 0])
        _confere(fatoracao, None, "21 = 3 × 7")
        cena.add(fatoracao)

        # ≈ 0,950: os quatro títulos acendem juntos, e a trilha pulsa uma vez
        cena.play(Succession(
            _ate(cena, t0, tag, est, 0.950),
            trilha.animate(run_time=0.3 * VEL * k).set_opacity(1)))
        cena.play(trilha.animate(rate_func=there_and_back).scale(1.1),
                  run_time=0.4 * VEL * k)

    return titulo, trilha, fatoracao


def encerramento(cena, titulo, trilha, fatoracao):
    """V1N12. Tudo sai de baixo para cima, por altura na tela — o 4, o 3,
    o 21 = 3 × 7, o 2, o 1 e o título da série —, menos o "2 ·
    Aritmética modular": esse vira a palavra "resto", no verde de c, no
    centro. É a costura para o corte: termina com "resto" sozinho em cena,
    e a abertura do vídeo 2 entra no corte seguinte."""
    resto = T("resto", 72, VERDE)
    pecas = sorted([*trilha, fatoracao, titulo], key=lambda m: m.get_y())

    with narra(cena, "V1N12", 8.8):
        tag, est = "V1N12", 8.8
        k = _k(tag, est)
        # "o resto de uma divisão" ≈ 0,41 é onde a palavra cai, mas é a
        # ÚNICA animação do bloco: presa à fração exata, o quadro final
        # ficaria parado por quase 30% da fala. Empurrada para o piso de
        # 85% em vez de concentrada no início
        alvo = max(_em(tag, est, 0.414), 0.85 * _dur(tag, est) - 2.6 * VEL * k)
        cena.play(Succession(Wait(max(0.0, alvo)), LaggedStart(
            *[ReplacementTransform(m, resto) if m is trilha[1] else FadeOut(m)
              for m in pecas], lag_ratio=0.25, run_time=2.6 * VEL * k)))

    return resto
