# -*- coding: utf-8 -*-
"""As âncoras DENTRO de cada fala: em que fração da locução cai a palavra
que dispara cada gesto. Elas dependem da ordem das palavras, então mudam de
um idioma para o outro — o código das cenas não muda.

Cada âncora é (tag, palavra-alvo em pt). A chave é a mesma nos dois
idiomas; em "en" o valor é a fração em que a palavra CORRESPONDENTE cai na
locução em inglês (roteiros/sincronias.md). Âncora que falta em "en" usa a
do pt, com um aviso por âncora.

As do vídeo 1 moram em videos/sincronias_v1.py e entram aqui inteiras; as
dos outros trechos estão logo abaixo. Traduzir é trocar números aqui e lá,
nunca código nas cenas."""

from manim import Wait, logger

from .idioma import IDIOMA
from .ferramentas import DUR, _agora
from .videos.sincronias_v1 import SINC as _V1

SINC = {
    "pt": {
        **_V1["pt"],
        # fora do vídeo 1 as frações são o instante da palavra que o
        # comentário do código dava, em segundos do est= da tag
        # C11N10 — o Write(eqc) da congruência com o 21
        ("C11N10", "outro exemplo"): 4.2 / 15.0,
        # V4N01 — a fissura chega às pontas e o arco estala
        ("V4N01", "vencer a aposta"): 6.2 / 11.9,
        # V4N03
        ("V4N03", "a aposta continua de pé"): 3.7 / 16.2,  # a rede volta
        ("V4N03", "prazo de validade"): 5.9 / 16.2,        # os cacos sobem
        ("V4N03", "a resposta já está"): 9.0 / 16.2,       # o cadeado novo
        ("V4N03", "não depende de fatorar"): 12.3 / 16.2,  # a armação fecha
        # V4N04
        ("V4N04", "o caminho foi seu"): 11.7 / 18.3,       # a trilha pulsa
        ("V4N04", "obrigado"): 15.5 / 18.3,                # o título pousa
    },
    "en": {
        **_V1["en"],
    },
}

_avisadas = set()


def _f(tag, ancora):
    """A fração da fala `tag` em que cai `ancora` no idioma ativo. Sem ela
    em SINC[IDIOMA], usa a do pt e avisa — uma vez por âncora."""
    chave = (tag, ancora)
    if chave not in SINC["pt"]:
        raise KeyError(f"âncora sem fração em pt: {chave}")
    tabela = SINC[IDIOMA]
    if chave in tabela:
        return tabela[chave]
    if chave not in _avisadas:
        _avisadas.add(chave)
        logger.warning('sincronia %s "%s": sem fração em %s, usando a do '
                       "pt (%.3f)", tag, ancora, IDIOMA, SINC["pt"][chave])
    return SINC["pt"][chave]


def _em(tag, est, frac):
    """O instante, em segundos, de uma fração da fala: frac × a mesma
    duração que narra() usa (DUR real, com est= de fallback)."""
    return frac * DUR.get(tag, est)


def _ate(cena, t0, tag, est, ancora):
    """Wait até a palavra `ancora` da fala `tag`, pelo relógio da cena
    contado de `t0` (o começo do narra), nunca negativo. Montado logo antes
    do play, não depende de somar à mão o tempo que já passou. Quando o
    Wait não abre o play — vem depois de outra animação dentro do mesmo
    Succession —, passar t0 recuado da duração dela."""
    return Wait(max(0.0, t0 + _em(tag, est, _f(tag, ancora)) - _agora(cena)))
