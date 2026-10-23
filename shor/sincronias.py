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

from manim import AnimationGroup, Succession, Wait, logger

from .idioma import IDIOMA
from .ferramentas import DUR, PAD, _agora
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
        # V0N00 — a seta ↓ nasce no rodapé
        ("V0N00", "descrição"): 0.957,
        # vídeo 2, capítulo 1 — realces e nascimentos na palavra (estimativa
        # por caracteres: início da âncora ÷ comprimento da fala)
        ("C1N04", "dois"): 0.762,            # s2 + r2 pulsam
        ("C1N05", "Dois é"): 0.0,            # eq[0] nasce de r2, com eq[1], [3], [5]
        ("C1N05", "onze"): 0.134,            # eq[2] nasce de r11
        ("C1N05", "três"): 0.221,            # eq[4] nasce de r3s[0]
        ("C1N06", "onze"): 0.047,            # r11 + b11 + eq[2]
        ("C1N07", "resto"): 0.778,           # s2 + r2
        ("C1N08", "cinco"): 0.133,           # b5 + r5 nascem
        ("C1N09", "dois"): 0.114,            # b2 + r2b nascem; eq[0] pulsa
        ("C1N10", "três"): 0.043,            # eq[4] pulsa
        ("C1N10", "quatro números"): 0.117,  # cadeia[0,2,4,6] com b11, b8, b5, b2
        # vídeo 2, capítulo 2 — idem (estimativa por caracteres)
        ("C2N01", "números"): 0.336,         # eq[2] + eq[4]
        ("C2N01", "resto"): 0.476,           # eq[0]
        ("C2N03", "um x"): 0.189,            # Write(ex0) começa
        ("C2N03", "por n"): 0.288,           # ex0[2] + n7 + rn
        ("C2N03", "menos a"): 0.342,         # ex0[4] + a5 + r5
        ("C2N03", "Sete"): 0.423,            # ex0[2:] → exf[2:5]; exf[2] pulsa
        ("C2N03", "cinco"): 0.523,           # exf[4]
        ("C2N03", "a dois"): 0.631,          # exf[5] e exf[6] nascem
        ("C2N03", "traço amarelo"): 0.874,   # Flash(x2) + rx → rx2
        ("C2N04", "comparação"): 0.092,      # Write(tst0) começa
        ("C2N04", "x é"): 0.214,             # tst0[0] + x2
        ("C2N04", "que b"): 0.316,           # tst0[2] + b6 + r6
        ("C2N04", "módulo"): 0.633,          # n7 + rn
        ("C2N04", "soma"): 0.949,            # b6 + a5
        ("C2N05", "resto"): 0.118,           # t2s[0] + cver + rc
        ("C2N05", "a b"): 0.324,             # t2s[2] + b6 + r6
        ("C2N05", "menos x"): 0.382,         # t2s[4] + x2 + rx2
        ("C2N05", "Seis"): 0.515,            # t2s[2:] → t2f[2:5]
        ("C2N05", "dois"): 0.676,            # t2f[4]
        ("C2N05", "quatro"): 0.897,          # t2f[5], t2f[6] nascem; Flash + rc → rc4
        ("C2N06", "seis"): 0.076,            # eq2[2]
        ("C2N06", "cinco"): 0.160,           # eq2[4]
        ("C2N06", "quatro"): 0.336,          # eq2[0] + rc4
        ("C2N06", "sete"): 0.462,            # eq2[6] + rn
        ("C2N07", "módulo"): 0.659,          # rn + n7 + eq2[6]
        ("C2N08", "doze"): 0.044,            # ln12 + eqc[6] + fx12[2]
        ("C2N08", "amarelo"): 0.389,         # bx12 + lx12
        ("C2N08", "vermelho"): 0.622,        # b6 + r6
        ("C2N08", "teste"): 0.778,           # Flash + Indicate(tst12[3])
        ("C2N09", "módulo"): 0.086,          # bn12 + ln12
        ("C2N09", "resto"): 0.505,           # bc12 nasce de b6 + a5; lc12
        ("C2N09", "Seis"): 0.763,            # f2ab → f2n; f2n[2] pulsa
        ("C2N09", "cinco"): 0.871,           # f2n[4]
        ("C2N09", "onze"): 0.946,            # f2n[6]
        ("C2N10", "Onze é"): 0.0,            # eqc → eq12, Flash(bc12), lc12 → lc11
        ("C2N10", "a onze"): 0.146,          # eq12[2:5]
        ("C2N10", "doze"): 0.268,            # eq12[6] + ln12
        ("C2N10", "x maior"): 0.423,         # tst12[0] + bx12
        ("C2N10", "que b"): 0.488,           # tst12[2] + b6
        # vídeo 2, capítulo 3 — idem (estimativa por caracteres)
        ("C3N01", "somas sucessivas"): 0.712, # os quatro + nascem entre os 4
        ("C3N02", "vinte"): 0.243,            # a fila de cima inteira pulsa
        ("C3N02", "o sete"): 0.568,           # baixo[1,2] + rb[1,2], em cascata
        ("C3N02", "resto"): 0.919,            # baixo[0] + rb[0]
        ("C3N03", "multiplicador"): 0.335,    # Indicate(eq[2])
        ("C3N05", "por dois"): 0.652,         # d1[0] + d2[0]
        ("C3N06", "juntamos"): 0.225,         # grupoA → p1
        ("C3N06", "termo que sobrou"): 0.716, # d3 → p3
        ("C3N07", "potências de dois"): 0.078,# o 2² de p1 e o 2⁰ de p3
        ("C3N07", "multiplicador"): 0.818,    # eq[2] (o 5)
        ("C3N08", "bit do meio"): 0.029,      # digs[1]
        ("C3N08", "termo dele"): 0.638,       # p2 nasce de digs[1]
        ("C3N09", "sete"): 0.590,             # os três 7 de e1, e2, e3
        ("C3N10", "bit desligado"): 0.145,    # bits_cx[1]
        ("C3N10", "zero"): 0.566,             # res[1]
        ("C3N11", "as três"): 0.200,          # res, em cascata
        ("C3N11", "sete"): 0.889,             # soma_f[8]
        ("C3N12", "seis"): 0.800,             # o seis nasce; eq → eq2 logo depois
        ("C3N13", "multiplicador"): 0.737,    # eq2[2]
        ("C3N13", "bits"): 0.943,             # bits_cx, em cascata
        # vídeo 2, capítulo 4 — idem (estimativa por caracteres)
        ("C4N02", "setecentos"): 0.204,       # segs (a reta tracejada) pulsa
        ("C4N02", "setes"): 0.634,            # baixo[1], baixo[2], rb[1], rb[2] pulsam em cascata
        ("C4N02", "resto"): 0.935,            # baixo[0] + rb[0] pulsam
        ("C4N03", "expoente"): 0.353,         # Indicate(tre[1]) (o 6 vermelho, escala 1,6)
        ("C4N05", "quadrado"): 0.662,         # os expoentes 2 de q1, q2, q3 pulsam
        ("C4N07", "juntamos"): 0.230,         # grupoA → p1 e grupoB → p2
        ("C4N07", "potências de dois"): 0.820,# os expoentes 2² de p1 e 2¹ de p2 pulsam
        ("C4N08", "potências de dois"): 0.083,# os expoentes 2² de p1 e 2¹ de p2 pulsam
        ("C4N08", "expoente"): 0.875,         # tre[1] (o 6) pulsa, logo depois do nascimento dos bits
        ("C4N09", "último bit"): 0.029,       # digs[2] pulsa
        ("C4N09", "termo dele"): 0.632,       # p3 nasce de digs[2]
        ("C4N10", "sete"): 0.533,             # os três 7 de e1, e2, e3 pulsam
        ("C4N11", "bit desligado"): 0.133,    # o dígito 0 de bits_cx[2] pulsa
        ("C4N11", "é o um"): 0.470,           # res[2] pulsa
        ("C4N12", "os três"): 0.176,          # res pulsa em cascata
        ("C4N12", "sete"): 0.902,             # soma_f[8] pulsa
        ("C4N13", "um"): 0.870,               # o um nasce; eq → eq2 logo depois, na mesma sequência
        ("C4N14", "expoente"): 0.776,         # tre2[1] (o 6 do eq2) pulsa
        ("C4N14", "bits"): 0.945,             # os dígitos de bits_cx pulsam em cascata
        # vídeo 2, capítulo 5 — idem (estimativa por caracteres)
        ("C5N02", "meio número"): 0.452,            # meio + rmeio nascem na palavra (a primeira das duas)
        ("C5N03", "qual número"): 0.349,            # eq2[2] (o x) pulsa
        ("C5N04", "inverso"): 0.439,                # eq2[2] (o x) pulsa
        ("C5N05", "resto um"): 0.889,               # o 1 verde, a sobra e o ✓ da última fila nascem
        ("C5N06", "Cinco"): 0.000,                  # eq3[2] pulsa
        ("C5N06", "dois"): 0.538,                   # eq3[0] pulsa
        ("C5N06", "nove"): 0.872,                   # eq3[6] pulsa
        ("C5N08", "módulo"): 0.323,                 # Indicate(eq3[6]) (o 9 laranja, escala 1,6)
        ("C5N10", "inverso"): 0.714,                # eq4[2] (o x) pulsa
        ("C5N11", "três"): 0.471,                   # eq4[0] pulsa, em paralelo com as filas
        ("C5N11", "nove"): 0.706,                   # eq4[6] pulsa, em paralelo com as filas
        ("C5N12", "O um"): 0.756,                   # eq4[4] pulsa
        ("C5N13", "três"): 0.164,                   # eq4[0] pulsa
        ("C5N13", "nove"): 0.329,                   # eq4[6] pulsa
        ("C5N14", "módulo"): 0.554,                 # mdc3[3] (o 9) pulsa
        ("C5N14", "um fator"): 0.862,               # mdc3[4] (o "= 3") pulsa
        ("C5N15", "módulo"): 0.765,                 # como[6] (o 9) pulsa, depois do Write(como)
        ("C5N17", "dá um"): 0.424,                  # os circulos nascem
        ("C5N17", "linha"): 0.475,                  # inv1[0] (o a) + head_l pulsam
        ("C5N17", "coluna"): 0.532,                 # inv1[2] (o b) + head_c pulsam
        ("C5N19", "números sem inverso"): 0.841,    # m_rot[0] + head_l[0], [3], [6] pulsam
        ("C5N20", "módulo"): 0.921,                 # c1[3] (o 9) pulsa
    },
    "en": {
        **_V1["en"],
        # V0N00 — a seta ↓ nasce no rodapé
        ("V0N00", "descrição"): 0.942,   # "description" — estimativa por caracteres
        # vídeo 2, capítulo 1 — palavra correspondente em en, estimativa por
        # caracteres (a medir na gravação)
        ("C1N04", "dois"): 0.846,            # "two"
        ("C1N05", "Dois é"): 0.0,            # "Two is"
        ("C1N05", "onze"): 0.132,            # "eleven"
        ("C1N05", "três"): 0.230,            # "three"
        ("C1N06", "onze"): 0.0,              # "Eleven"
        ("C1N07", "resto"): 0.688,           # "remainder"
        ("C1N08", "cinco"): 0.615,           # "five"
        ("C1N09", "dois"): 0.108,            # "two"
        ("C1N10", "três"): 0.045,            # "Three"
        ("C1N10", "quatro números"): 0.130,  # "four numbers"
        # vídeo 2, capítulo 2 — idem
        ("C2N01", "números"): 0.194,         # "numbers"
        ("C2N01", "resto"): 0.363,           # "remainder"
        ("C2N03", "um x"): 0.239,            # "x as"
        ("C2N03", "por n"): 0.293,           # "n minus"
        ("C2N03", "menos a"): 0.315,         # "minus a"
        ("C2N03", "Sete"): 0.413,            # "Seven"
        ("C2N03", "cinco"): 0.543,           # "five"
        ("C2N03", "a dois"): 0.598,          # "is two"
        ("C2N03", "traço amarelo"): 0.837,   # "yellow segment"
        ("C2N04", "comparação"): 0.136,      # "comparison"
        ("C2N04", "x é"): 0.245,             # "is x"
        ("C2N04", "que b"): 0.364,           # "than b"
        ("C2N04", "módulo"): 0.673,          # "modulus"
        ("C2N04", "soma"): 0.964,            # "sum"
        ("C2N05", "resto"): 0.132,           # "remainder"
        ("C2N05", "a b"): 0.321,             # "is b"
        ("C2N05", "menos x"): 0.415,         # "minus x"
        ("C2N05", "Seis"): 0.585,            # "Six"
        ("C2N05", "dois"): 0.774,            # "two"
        ("C2N05", "quatro"): 0.906,          # "four"
        ("C2N06", "seis"): 0.086,            # "six"
        ("C2N06", "cinco"): 0.164,           # "five"
        ("C2N06", "quatro"): 0.345,          # "four"
        ("C2N06", "sete"): 0.457,            # "seven"
        ("C2N07", "módulo"): 0.708,          # "modulus"
        ("C2N08", "doze"): 0.031,            # "twelve"
        ("C2N08", "amarelo"): 0.449,         # "yellow"
        ("C2N08", "vermelho"): 0.663,        # "red"
        ("C2N08", "teste"): 0.796,           # "test"
        ("C2N09", "módulo"): 0.130,          # "modulus"
        ("C2N09", "resto"): 0.528,           # "remainder"
        ("C2N09", "Seis"): 0.796,            # "Six"
        ("C2N09", "cinco"): 0.880,           # "five"
        ("C2N09", "onze"): 0.935,            # "eleven"
        ("C2N10", "Onze é"): 0.0,            # "Eleven is"
        ("C2N10", "a onze"): 0.134,          # "to eleven"
        ("C2N10", "doze"): 0.255,            # "twelve"
        ("C2N10", "x maior"): 0.436,         # "is x"
        ("C2N10", "que b"): 0.523,           # "than b"
        # vídeo 2, capítulo 3 — idem
        ("C3N01", "somas sucessivas"): 0.673, # "repeated addition"
        ("C3N02", "vinte"): 0.280,            # "twenty"
        ("C3N02", "o sete"): 0.366,           # "seven fits"
        ("C3N02", "resto"): 0.892,            # "remainder"
        ("C3N03", "multiplicador"): 0.352,    # "multiplier"
        ("C3N05", "por dois"): 0.561,         # "by two"
        ("C3N06", "juntamos"): 0.177,         # "merge"
        ("C3N06", "termo que sobrou"): 0.719, # "leftover term"
        ("C3N07", "potências de dois"): 0.098,# "powers of two"
        ("C3N07", "multiplicador"): 0.820,    # "multiplier"
        ("C3N08", "bit do meio"): 0.080,      # "middle bit"
        ("C3N08", "termo dele"): 0.520,       # "its term"
        ("C3N09", "sete"): 0.581,             # "seven"
        ("C3N10", "bit desligado"): 0.127,    # "bit is off"
        ("C3N10", "zero"): 0.494,             # "zero"
        ("C3N11", "as três"): 0.280,          # "the three"
        ("C3N11", "sete"): 0.880,             # "seven"
        ("C3N12", "seis"): 0.833,             # "six"
        ("C3N13", "multiplicador"): 0.760,    # "multiplier"
        ("C3N13", "bits"): 0.936,             # "bits"
        # vídeo 2, capítulo 4 — idem
        ("C4N02", "setecentos"): 0.203,       # "seven hundred"
        ("C4N02", "setes"): 0.500,            # "sevens"
        ("C4N02", "resto"): 0.915,            # "remainder"
        ("C4N03", "expoente"): 0.332,         # "exponent"
        ("C4N05", "quadrado"): 0.528,         # "squaring"
        ("C4N07", "juntamos"): 0.210,         # "merge"
        ("C4N07", "potências de dois"): 0.827,# "powers of two"
        ("C4N08", "potências de dois"): 0.102,# "powers of two"
        ("C4N08", "expoente"): 0.847,         # "exponent"
        ("C4N09", "último bit"): 0.083,       # "last bit"
        ("C4N09", "termo dele"): 0.500,       # "its term"
        ("C4N10", "sete"): 0.554,             # "seven"
        ("C4N11", "bit desligado"): 0.119,    # "bit is off"
        ("C4N11", "é o um"): 0.429,           # "is one"
        ("C4N12", "os três"): 0.255,          # "the three"
        ("C4N12", "sete"): 0.891,             # "seven"
        ("C4N13", "um"): 0.833,               # "one"
        ("C4N14", "expoente"): 0.787,         # "exponent"
        ("C4N14", "bits"): 0.940,             # "bits"
        # vídeo 2, capítulo 5 — idem
        ("C5N02", "meio número"): 0.483,            # "half a number"
        ("C5N03", "qual número"): 0.358,            # "which number"
        ("C5N04", "inverso"): 0.810,                # "inverse"
        ("C5N05", "resto um"): 0.911,               # "is one"
        ("C5N06", "Cinco"): 0.000,                  # "Five"
        ("C5N06", "dois"): 0.575,                   # "two"
        ("C5N06", "nove"): 0.875,                   # "nine"
        ("C5N08", "módulo"): 0.336,                 # "modulus"
        ("C5N10", "inverso"): 0.734,                # "inverse"
        ("C5N11", "três"): 0.417,                   # "three"
        ("C5N11", "nove"): 0.688,                   # "nine"
        ("C5N12", "O um"): 0.806,                   # "One is"
        ("C5N13", "três"): 0.167,                   # "three"
        ("C5N13", "nove"): 0.347,                   # "nine"
        ("C5N14", "módulo"): 0.884,                 # "modulus"
        ("C5N14", "um fator"): 0.623,               # "a factor"
        ("C5N15", "módulo"): 0.759,                 # "modulus"
        ("C5N17", "dá um"): 0.444,                  # "is one"
        ("C5N17", "linha"): 0.523,                  # "row"
        ("C5N17", "coluna"): 0.575,                 # "column"
        ("C5N19", "números sem inverso"): 0.820,    # "numbers with no inverse"
        ("C5N20", "módulo"): 0.789,                 # "modulus"
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


def na_palavra(cena, t0, tag, est, ancora, *anims):
    """Atalho do vídeo 2: `anims` começam na palavra `ancora` da fala `tag`
    e entram NO MESMO play da animação principal da linha, como irmãs dela
    (cena.play(principal, na_palavra(...))). É o Succession(_ate, grupo) que
    cada cena escreveria à mão, com duas garantias:
    - o que NASCE na palavra (Create, FadeIn, TransformFromCopy) só entra em
      cena nela: o Succession e as animações viram `introducer`, senão o play
      poria a peça em cena no primeiro quadro, parada durante o Wait;
    - o gesto nunca empurra a linha para fora da locução: a espera é
      encurtada, se preciso, para o gesto acabar até o fim da fala + PAD.
    Cada animação leva o próprio run_time (o do play sobrescreveria o do
    Wait). Passar t0 = _agora(cena) tirado no começo do narra()."""
    for a in anims:
        a.introducer = True
    grupo = AnimationGroup(*anims, introducer=True)
    espera = _ate(cena, t0, tag, est, ancora)
    # 0,1 s de margem: terminar a menos de um quadro do fim da fala deixa o
    # wait(sobra) do narra() curto demais para o Manim e ele avisa
    sobra = (DUR.get(tag, est) + PAD - 0.1 - (_agora(cena) - t0)
             - grupo.run_time)
    espera.run_time = max(0.0, min(espera.run_time, sobra))
    return Succession(espera, grupo, introducer=True)
