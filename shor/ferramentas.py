# -*- coding: utf-8 -*-
"""Funções auxiliares compartilhadas por todos os capítulos do filme."""

from manim import *
import numpy as np

from .paleta import COR_TEXTO, CINZA, PRETO, CAIXA, CIANO, AMARELO, LARANJA, VEL, R, N, M
from .paleta import VERMELHO, AZUL

from contextlib import contextmanager
from types import SimpleNamespace
from importlib import import_module
from pathlib import Path

from .idioma import IDIOMA
from .textos import tx

try:
    DUR = import_module(f".duracoes_{IDIOMA}", __package__).DUR
except ImportError:
    DUR = {}

RAIZ = Path(__file__).resolve().parent.parent
AUDIO = RAIZ / "audio" / IDIOMA
NARRA = True      # False = preview mudo, sem as pausas de fala
PAD = 0.35        # respiro no fim de cada linha
TRATAR_AUDIO = True   # False = usa o .wav original, sem redução de ruído/fades


def _agora(cena):
    return float(getattr(cena.renderer, "time", 0.0))

def _tratar(wav):
    """Cópia do .wav com ruído reduzido e fades, em media/audio_tratado/<idioma>/.
    Mesma duração do original, amostra por amostra. O original nunca é tocado."""
    import soundfile as sf
    import noisereduce as nr
    wav = Path(wav)
    saida = RAIZ / "media" / "audio_tratado" / IDIOMA / wav.name
    # Reuso só se o registro .fonte (tamanho + mtime_ns do original) bater exatamente:
    # data da cópia não basta, pois mv/renomear preserva o mtime e reaproveitava o
    # tratado de outra fala.
    est = wav.stat()
    fonte = saida.with_name(wav.name + ".fonte")
    registro = f"{est.st_size} {est.st_mtime_ns}"
    if saida.exists() and fonte.exists() and fonte.read_text().strip() == registro:
        return saida
    d, sr = sf.read(str(wav), always_2d=True)          # (amostras, canais)
    info = sf.info(str(wav))
    y = d.T                                            # (canais, amostras)
    # perfil de ruído: janela de 0,3 s mais silenciosa (RMS) do próprio arquivo
    jan = min(int(0.3 * sr), y.shape[1])
    passo = max(jan // 3, 1)
    ini = min(range(0, y.shape[1] - jan + 1, passo),
              key=lambda i: float(np.mean(y[:, i:i + jan] ** 2)))
    out = nr.reduce_noise(y=y, sr=sr, stationary=True, prop_decrease=0.8,
                          y_noise=y[:, ini:ini + jan])
    n = out.shape[1]
    fi, fo = min(int(0.030 * sr), n), min(int(0.200 * sr), n)
    out[:, :fi] *= np.linspace(0.0, 1.0, fi)
    out[:, n - fo:] *= np.linspace(1.0, 0.0, fo)
    out = np.clip(out.T, -1.0, 1.0)
    assert out.shape == d.shape, (wav.name, out.shape, d.shape)
    saida.parent.mkdir(parents=True, exist_ok=True)
    sf.write(str(saida), out, sr, subtype=info.subtype)
    assert sf.info(str(saida)).frames == info.frames, wav.name
    fonte.write_text(registro + "\n")
    return saida

def _add_som(cena, wav):
    """add_sound() é ignorado quando renderer.skip_animations está ligado —
    e ele fica ligado depois de qualquer play() servido pelo cache.
    Derrubamos a flag só durante a inserção, preservando -s / -n."""
    r = cena.renderer
    antes = r.skip_animations
    r.skip_animations = getattr(r, "_original_skipping_status", False)
    try:
        cena.add_sound(str(_tratar(wav) if TRATAR_AUDIO else wav))
    finally:
        r.skip_animations = antes

@contextmanager
def narra(cena, tag, est=3.0):
    """Bloco de narração: dispara o áudio, roda as animações do `with`
    e completa em silêncio o que faltar para a locução terminar."""
    if not NARRA:
        yield 0.0
        return
    dur = DUR.get(tag, est)
    wav = AUDIO / f"{tag}.wav"
    if wav.exists():
        _add_som(cena, wav)
    t0 = _agora(cena)
    yield dur
    sobra = dur + PAD - (_agora(cena) - t0)
    if sobra > 0:
        cena.wait(sobra)


def so_fala(cena, tag, est=3.0):
    """Linha de narração sem animação embaixo."""
    with narra(cena, tag, est):
        pass

def T(texto, tamanho=30, cor=COR_TEXTO, **kw):
    return Text(texto, font_size=tamanho, color=cor, **kw)


def formula(*pares, tamanho=32, buff=0.16):
    """Fórmula colorida por tokens: formula(("2",VERDE), ("≡",PRETO), ...)"""
    return VGroup(*[T(t, tamanho, c) for t, c in pares]).arrange(RIGHT, buff=buff)


def MOD(n, cor=LARANJA):
    """Tokens de "(mod n)" com cor SÓ no número: formula(..., *MOD("7"))."""
    return (("(mod ", PRETO), (n, cor), (")", PRETO))


def fmod(n, tamanho=24, cor=LARANJA):
    """VGroup "(mod n)" pronto (parênteses/mod pretos, número colorido)."""
    return formula(*MOD(n, cor), tamanho=tamanho, buff=0.09)


def pot(base, expo, cor_base, cor_expo=None, tam=32):
    """Potência com expoente pequeno deslocado (ex.: 2² com cores próprias).
    base/expo podem ser strings OU Mobjects já coloridos por token."""
    b = T(base, tam, cor_base) if isinstance(base, str) else base
    if isinstance(expo, str):
        e = T(expo, max(int(tam * 0.62), 14), cor_expo)
    else:
        e = expo
    e.next_to(b.get_corner(UR), RIGHT, buff=0.03).shift(0.10 * UP)
    return VGroup(b, e)


def expoente(*pares, tam=32):
    """Expoente composto colorido por tokens, para usar com pot()."""
    return formula(*pares, tamanho=max(int(tam * 0.62), 14), buff=0.03)


def traco(p1, p2, cor, gap=0.10, w=7):
    """Traço com folga nas pontas — o 'bloco' das retas segmentadas dos slides."""
    p1, p2 = np.array(p1, float), np.array(p2, float)
    v = p2 - p1
    if np.linalg.norm(v) < 1e-9:
        return Line(p1, p2, color=cor, stroke_width=w)
    L = float(np.linalg.norm(v))
    u = v / L
    g = min(gap, 0.3 * L)
    return Line(p1 + u * g, p2 - u * g, color=cor, stroke_width=w)


def caixa_cinza(conteudo, pad=0.22, fundo=CAIXA):
    """Caixa cinza dos diagramas dos slides (27/34) com conteúdo dentro."""
    r = SurroundingRectangle(conteudo, color=fundo, buff=pad, corner_radius=0.05)
    r.set_fill(fundo, opacity=1).set_stroke(width=0)
    return VGroup(r, conteudo)


def _cor_da_peca(m):
    """A cor com que a peça foi desenhada: o fill do primeiro glifo (ou o
    traço, nas linhas). `Text.get_color()` devolve o preto do invólucro."""
    for f in m.get_family():
        if f.has_points():
            return (f.get_fill_color() if f.get_fill_opacity() > 0
                    else f.get_stroke_color())
    return m.get_color()


def realce(*mobs):
    """O realce do vídeo 2: quando a fala nomeia um número ou variável que
    está na tela, a peça pulsa (Indicate) na cor DELA — nunca no amarelo
    padrão, que é o papel do x. Várias peças (a cópia na equação e a barra
    na reta) pulsam no mesmo instante, cada uma em volta do próprio centro
    e na própria cor: um Indicate no VGroup escalaria em volta do centro do
    grupo e jogaria longe peças que estão distantes (o 11 do topo e a
    barra). Para disparar na palavra: sincronias.na_palavra."""
    return AnimationGroup(*[Indicate(m, color=_cor_da_peca(m),
                                     scale_factor=1.25, run_time=0.6 * VEL)
                            for m in mobs])


# ----------------------------------------------------------------------------
# Succession no Cairo — os gestos da tabela dos capítulos 6 e 7
# ----------------------------------------------------------------------------
def _etapa(*anims, **kw):
    """Uma etapa de Succession: introducer, para o que NASCE nela só entrar
    em cena na vez dela (e não no primeiro quadro do play)."""
    return AnimationGroup(*anims, introducer=True, **kw)


def _serie(*etapas):
    return Succession(*etapas, introducer=True)


def _copia(origem, alvo):
    """TransformFromCopy marcado como introducer: o alvo só aparece quando a
    animação começa, mesmo dentro de um Succession."""
    a = TransformFromCopy(origem, alvo)
    a.introducer = True
    return a


def _vira(m, alvo):
    """m assume o desenho de `alvo` — para dentro de um Succession, no lugar
    do ReplacementTransform. No Cairo, durante um play só é desenhado o que
    estava em cena quando ele começou, e o ReplacementTransform só põe o
    alvo em cena no fim do play: o alvo não aparece e a origem deformada
    fica congelada. Depois do play, cena.replace(m, alvo) troca a peça pela
    canônica (mesmo desenho, mesmo lugar)."""
    return Transform(m, alvo.copy())


def _mv(m, ponto):
    """Move m até ponto (centro) — alvo explícito, sem .animate."""
    return Transform(m, m.copy().move_to(ponto))


def evidencia(base, nums, centro, tam=26, mod="7", tam_mod=24, cores=None):
    """O produto da linha do multiplicador, (b·n₁)(b·n₂)…(b·nₖ) ≡ (n₁·…·nₖ)
    (mod m), e a extração do b em evidência até bᵏ·(n₁·…·nₖ) ≡ (n₁·…·nₖ)
    (mod m) — C6N08–C6N09, C7N03 e C7N10. Cada peça é um token próprio; o
    estado final, `eq` = VGroup(bᵏ, mid, igual, rhs, modg), é feito dos
    mesmos tokens, então nada sobra em cena. O lado direito já nasce no
    lugar final (eq centrado em `centro`) e não se mexe; o lado esquerdo se
    junta contra ele. `cores`: {n: cor} dos números que não são pretos, nos
    dois lados.

    Devolve um SimpleNamespace com os tokens (PO, PC, R, D, N, pto, BO, BC,
    pots, mid, igual, rd, ro, rc, rhs, modg), o `eq` e:
    - nasce(fonte_b, fontes, rt_esq, rt_dir, rt_resto): as três animações
      do nascimento — cada b de cópia de fonte_b, cada número dos dois
      lados de cópia de fontes[i];
    - passos(rt, primeiro=()): as k etapas da extração, para _serie;
      `primeiro` entra na primeira. Depois do play, R[1] fez o papel de
      b², …, bᵏ: cena.replace(R[1], pots[k])."""
    nums = list(nums)
    k = len(nums)
    cor = lambda n: (cores or {}).get(n, PRETO)
    PO = {i: T("(", tam, PRETO) for i in range(1, k + 1)}
    PC = {i: T(")", tam, PRETO) for i in range(1, k + 1)}
    R = {i: T(base, tam, VERMELHO) for i in range(1, k + 1)}
    D = {i: T("·", tam, PRETO) for i in range(1, k + 1)}
    N = {i: T(str(n), tam, cor(n)) for i, n in enumerate(nums, 1)}
    pto = {i: T("·", tam, PRETO) for i in range(2, k + 1)}   # os · da fila de dentro
    BO, BC = T("(", tam, PRETO), T(")", tam, PRETO)          # o parêntese grande

    meio = [D[1], BO, N[1]]
    for i in range(2, k + 1):
        meio += [pto[i], N[i]]
    meio.append(BC)
    pots = {m: pot(base, str(m), VERMELHO, AZUL, tam) for m in range(2, k + 1)}
    mid = VGroup(*meio).arrange(RIGHT, buff=0.04)
    igual = T("≡", tam, PRETO)
    rd = []
    for i, n in enumerate(nums, 1):
        rd += [T(str(n), tam, cor(n))] + ([T("·", tam, PRETO)] if i < k else [])
    ro, rc = T("(", tam, PRETO), T(")", tam, PRETO)
    rhs = VGroup(ro, *rd, rc).arrange(RIGHT, buff=0.04)
    modg = fmod(mod, tam_mod)
    eq = VGroup(pots[k], mid, igual, rhs, modg)
    eq.arrange(RIGHT, buff=0.15).move_to(centro)
    ref_x, ref_y = meio[-1].get_right()[0], meio[0].get_center()[1]

    def estado(m):
        """(front, tokens) do estado m da extração (0 … k)."""
        if m == 0:
            return None, [t for i in range(1, k + 1)
                          for t in (PO[i], R[i], D[i], N[i], PC[i])]
        toks = [D[1], BO, N[1]]
        for i in range(2, m + 1):
            toks += [pto[i], N[i]]
        if m < k:
            toks.append(pto[m + 1])
            for i in range(m + 1, k + 1):
                toks += [PO[i], R[i], D[i], N[i], PC[i]]
        toks.append(BC)
        return (R[1] if m == 1 else pots[m]), toks

    def posicoes(m):
        """centro de cada token do estado m, alinhado ao eq final. Calculado
        com cópias, com a mesma receita de arrange do eq."""
        front, toks = estado(m)
        cp = [t.copy() for t in toks]
        g = VGroup(*cp).arrange(RIGHT, buff=0.04)
        todos = list(cp)
        cf = None
        if front is not None:
            cf = front.copy()
            VGroup(cf, g).arrange(RIGHT, buff=0.15)
            todos.append(cf)
        dx, dy = ref_x - cp[-1].get_right()[0], ref_y - cp[0].get_center()[1]
        for c in todos:
            c.shift(dx * RIGHT + dy * UP)
        pos = {id(t): c.get_center() for t, c in zip(toks, cp)}
        return (None if cf is None else cf.get_center()), pos

    pos_est = [posicoes(m) for m in range(k + 1)]
    est_tok = [estado(m) for m in range(k + 1)]
    # estado 0: os tokens vão para o lugar antes de nascerem
    for t in est_tok[0][1]:
        t.move_to(pos_est[0][1][id(t)])

    def nasce(fonte_b, fontes, rt_esq, rt_dir, rt_resto):
        esq = LaggedStart(*[AnimationGroup(
            Write(PO[i]), _copia(fonte_b, R[i]), Write(D[i]),
            _copia(fontes[i - 1], N[i]), Write(PC[i])) for i in range(1, k + 1)],
            lag_ratio=0.15, run_time=rt_esq)
        digs = rd[0::2]
        dir_ = LaggedStart(*[_copia(fontes[j], digs[j]) for j in range(k)],
                           lag_ratio=0.1, run_time=rt_dir)
        resto = AnimationGroup(
            FadeIn(igual), FadeIn(modg), FadeIn(ro), FadeIn(rc),
            *[FadeIn(t) for t in rd[1::2]], run_time=rt_resto)
        return esq, dir_, resto

    def passos(rt, primeiro=()):
        etapas = []
        for m in range(1, k + 1):
            fa, ta = est_tok[m - 1]
            fn, tn = est_tok[m]
            pa, pn = pos_est[m - 1][1], pos_est[m][1]
            pf = pos_est[m][0]
            anims = list(primeiro) if m == 1 else []
            for t in (PO[m], PC[m]) + ((D[m],) if m >= 2 else ()):
                anims.append(FadeOut(t))
            if m == 1:
                anims.append(_mv(R[1], pf))
            else:
                pots[m].move_to(pf)
                anims.append(FadeOut(R[m], target_position=pf))
                anims.append(_vira(R[1], pots[m]))
            antes = {id(t) for t in ta}
            for t in tn:
                if id(t) in antes:
                    if np.linalg.norm(pn[id(t)] - pa[id(t)]) > 1e-3:
                        anims.append(_mv(t, pn[id(t)]))
                else:
                    t.move_to(pn[id(t)])
                    anims.append(Write(t))
            etapas.append(_etapa(*anims, run_time=rt))
        return etapas

    return SimpleNamespace(PO=PO, PC=PC, R=R, D=D, N=N, pto=pto, BO=BO, BC=BC,
                           pots=pots, mid=mid, igual=igual, rd=rd, ro=ro,
                           rc=rc, rhs=rhs, modg=modg, eq=eq,
                           nasce=nasce, passos=passos)


def origina_binario(cena, fonte, bits, y=None, ref=None, espac=0.55, tam=36,
                    junto=()):
    """REGRA 4: os dígitos binários NASCEM do número decimal — cópias do
    número voam, se separam e se metamorfoseiam nos bits (1 azul-claro,
    0 amarelo, como nos slides). Retorna o VGroup dos dígitos.
    `junto`: animações que entram no MESMO play do nascimento dos dígitos."""
    seta = Arrow(fonte.get_bottom() + 0.06 * DOWN,
                 fonte.get_bottom() + 0.72 * DOWN,
                 buff=0, color=PRETO, stroke_width=3,
                 max_tip_length_to_length_ratio=0.35)
    mini = T(tx("geral.binario"), 16, CINZA).next_to(seta, RIGHT, buff=0.12)
    digs = VGroup(*[T(b, tam, CIANO if b == "1" else AMARELO) for b in bits])
    digs.arrange(RIGHT, buff=espac)
    digs.next_to(seta, DOWN, buff=0.18) if ref is None else digs.move_to(ref)
    if y is not None:
        digs.set_y(y)
    cena.play(GrowArrow(seta), FadeIn(mini), run_time=0.7 * VEL)
    cena.play(LaggedStart(*[ReplacementTransform(fonte.copy(), d) for d in digs],
                          lag_ratio=0.22), *junto, run_time=1.7 * VEL)
    cena.play(FadeOut(seta), FadeOut(mini), run_time=0.4 * VEL)
    return digs


def cartao_capitulo(cena, rotulo, titulo, tag=None, est=3.0, sai=None):
    """`sai` é a última peça viva do capítulo anterior, entregue por ele: em
    vez de um limpar() genérico antes do cartão, ela apaga DENTRO do mesmo
    play em que o cartão entra — a emenda do t1 no CAP09 (video4.py), sem
    quadro vazio entre os dois."""
    r = T(rotulo, 26, LARANJA)
    t = T(titulo, 38)
    g = VGroup(r, t).arrange(DOWN, buff=0.35)
    linha = Line(3 * LEFT, 3 * RIGHT, color=CINZA, stroke_width=1.5)
    linha.next_to(g, DOWN, buff=0.45)
    entra = [FadeIn(r, shift=0.3 * DOWN), Write(t), Create(linha)]
    if sai is not None:
        entra.insert(0, FadeOut(sai, scale=0.5))
    with narra(cena, tag or rotulo.replace(" ", ""), est):
        cena.play(*entra, run_time=1.3 * VEL)
    cena.play(FadeOut(g), FadeOut(linha), run_time=0.5 * VEL)


def limpar(cena):
    for m in list(cena.mobjects):
        m.clear_updaters()
    if cena.mobjects:
        cena.play(*[FadeOut(m) for m in list(cena.mobjects)],
                  run_time=0.6 * VEL)
    cena.wait(0.2 * VEL)


def amplitude(k: float) -> float:
    x = R * k / N
    den = np.sin(PI * x)
    if abs(den) < 1e-9:
        return 1.0
    return abs(np.sin(PI * M * x) / (M * den))
