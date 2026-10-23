# -*- coding: utf-8 -*-
"""Funções auxiliares compartilhadas por todos os capítulos do filme."""

from manim import *
import numpy as np

from .paleta import COR_TEXTO, CINZA, PRETO, CAIXA, CIANO, AMARELO, LARANJA, VEL, R, N, M

from contextlib import contextmanager
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
    if saida.exists() and saida.stat().st_mtime >= wav.stat().st_mtime:
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
