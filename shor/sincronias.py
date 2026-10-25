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
        # vídeo 3, capítulo 6 — idem (estimativa por caracteres)
        ("C6N01", "módulo sete"): 0.887,            # titulo_tab pulsa
        ("C6N02", "sete"): 0.944,                   # titulo_tab pulsa
        ("C6N06", "Os números"): 0.000,             # A + B pulsam
        ("C6N10", "restos"): 0.355,                 # eq[3] (a lista) pulsa
        ("C6N10", "módulo"): 0.753,                 # eq[4][1] (o 7) pulsa
        ("C6N11", "módulo"): 0.057,                 # eq[4][1] (o 7) pulsa
        ("C6N11", "produto inteiro"): 0.631,        # div_e + div_d nascem
        ("C6N12", "potência"): 0.327,               # resultado[0] (o 3⁶) pulsa
        ("C6N12", "a um"): 0.691,                   # resultado[2] (o 1) pulsa
        ("C6N12", "sete"): 0.909,                   # resultado[3][1] (o 7) pulsa
        ("C6N13", "módulo é primo"): 0.079,         # geral[3][1] + n do expoente, logo depois do Write
        ("C6N13", "valor a"): 0.579,                # geral[0][0] (o a) pulsa
        ("C6N13", "múltiplo do módulo"): 0.833,     # geral[3][1] + n do expoente
        ("C6N15", "o módulo precisa"): 0.222,       # geral[3][1] + n do expoente
        ("C6N15", "precisa ser primo"): 0.322,      # Indicate(geral[4])
        # vídeo 3, capítulo 7 — idem (estimativa por caracteres)
        ("C7N02", "multiplicador"): 0.275,          # Create(el2) + Indicate(head_l[1]), e a linha 2 cai sobre B
        ("C7N02", "lista de restos"): 0.686,        # A pulsa
        ("C7N04", "cancelar a lista"): 0.584,       # div_e + div_d nascem
        ("C7N05", "dois desses fatores"): 0.383,    # os 3 e 6 marrons de esq, dir_, div_e, div_d pulsam
        ("C7N05", "módulo"): 0.942,                 # o 9 de exp2 e o de dir_ pulsam
        ("C7N06", "linhas"): 0.129,                 # o bloco (linhas 3 e 6 + Indicate marrons) começa
        ("C7N07", "números que não têm inverso"): 0.627,  # cruzes + cruzes_eq nascem
        ("C7N08", "números"): 0.284,                # sobr nasce
        ("C7N08", "módulo"): 0.896,                 # dir_[6] (o 9) pulsa
        ("C7N09", "contagem"): 0.049,               # Write(phi) começa
        ("C7N09", "fi de ene"): 0.878,              # phi pulsa
        ("C7N12", "potência"): 0.294,               # res[0] (o 2⁶) pulsa
        ("C7N12", "a um"): 0.588,                   # res[2] (o 1) pulsa
        ("C7N12", "nove"): 0.926,                   # res[4] (o 9) pulsa
        ("C7N13", "qualquer módulo"): 0.136,        # geral[3][1] + n do expoente, logo depois do Write
        ("C7N13", "o expoente"): 0.320,             # geral[0][1] (o φ(n)) pulsa
        ("C7N13", "totiente"): 0.913,               # geral[0][1] pulsa
        # vídeo 3, capítulo 8 (C8N12–C8N24) — idem (estimativa por caracteres)
        ("C8N12", "número a"): 0.045,                     # Indicate(L[0][0]) na palavra
        ("C8N12", "Multiplicamos"): 0.673,                # L → L2
        ("C8N13", "se somam"): 0.775,                     # L2 → L3
        ("C8N14", "expoente"): 0.375,                     # L3[0][1] pulsa antes da troca
        ("C8N14", "reescrito"): 0.600,                    # L3 → L4
        ("C8N14", "fi de ene"): 0.875,                    # os dois Indicate (L4[3] e L4[0][1])
        ("C8N15", "Qualquer expoente"): 0.000,            # L4[0][1] pulsa
        ("C8N15", "mensagem"): 0.550,                     # L4[2] (o a) pulsa
        ("C8N16", "expoente"): 0.873,                     # legenda[1:4] (o (mod φ(n))) pulsa
        ("C8N17", "dois números"): 0.538,                 # Indicate(celulas[2][5]) + Indicate(celulas[5][2])
        ("C8N17", "dê um"): 0.756,                        # ed[4] (o 1) pulsa
        ("C8N17", "módulo do expoente"): 0.840,           # ed[5], ed[6], ed[7] pulsam
        ("C8N18", "par"): 0.119,                          # Indicate(ed)
        ("C8N18", "expoente"): 0.786,                     # L4[0] → L5[0] + a volta do lado direito
        ("C8N19", "produto no expoente"): 0.041,          # L5[0][1] (o e·d) pulsa antes da troca
        ("C8N19", "potência de outra potência"): 0.355,   # L5 → L6 + a saída da tabela
        ("C8N19", "uma desfazendo"): 0.810,               # Indicate do e
        ("C8N19", "a outra"): 0.934,                      # Indicate do d
        ("C8N20", "mensagem"): 0.852,                     # Indicate(L6[2]) + o a do pacA
        ("C8N21", "primeira potência"): 0.023,            # o aᵉ de L6 pulsa
        ("C8N21", "módulo"): 0.372,                       # L6[3][1] (o n) pulsa
        ("C8N21", "mensagem"): 0.605,                     # o a do pacA pulsa
        ("C8N21", "cifra"): 0.930,                        # trancar(pacA) começa
        ("C8N23", "segunda potência"): 0.030,             # o d de L6 pulsa
        ("C8N23", "primeira"): 0.418,                     # o aᵉ de L6 pulsa
        ("C8N23", "mensagem original"): 0.731,            # abrir(pacA) começa
        ("C8N24", "expoente que desfaz"): 0.041,          # fpriv[2] + o d de f2s pulsam
        ("C8N24", "módulo"): 0.367,                       # fpriv[4] + o n de f2s pulsam
        # vídeo 3, capítulo 8 (C8N26–C8N44) e encerramento (V3N01) — idem (estimativa por caracteres)
        ("C8N26", "módulo"): 0.273,                           # Write(esc) + Write(E1) começam
        ("C8N27", "módulo"): 0.091,                           # esc[2] + os dois 33 de E1 pulsam
        ("C8N27", "fi de ene"): 0.500,                        # Write(phi) começa
        ("C8N27", "módulo do expoente"): 0.712,               # E1 → E2 começa
        ("C8N28", "par de inversos"): 0.515,                  # ed2 → edn começa
        ("C8N29", "desse par"): 0.250,                        # edn[0] + edn[2] pulsam
        ("C8N29", "mesmo módulo"): 0.852,                     # o 33 dos dois cartões + esc[2] pulsam
        ("C8N30", "números escolhidos"): 0.648,               # E2 → E3 + Indicate(edn)
        ("C8N31", "mensagem"): 0.133,                         # Write de "mensagem: a = 5"
        ("C8N31", "menor que o módulo"): 0.683,               # Write de "< 33" + o 33 de E4 pulsa
        ("C8N32", "lugar da letra"): 0.500,                   # E4 → L7 + Indicate(msg_esc)
        ("C8N34", "cifra"): 0.677,                            # o 26 de f1 e o 26 de f2 pulsam
        ("C8N35", "números"): 0.654,                          # Write(fim2) começa
        ("C8N36", "fi de ene"): 0.559,                        # lphi[1:4] (o φ(n) da legenda) pulsam
        ("C8N36", "encontrar a privada"): 0.737,              # eixo_d pulsa
        ("C8N36", "a partir da pública"): 0.868,              # eixo_e pulsa
        ("C8N37", "conhece o módulo"): 0.360,                 # a legenda inteira (lphi) pulsa
        ("C8N37", "fi de ene"): 0.867,                        # os dois Indicate (phin e o φ(n) da legenda)
        ("C8N38", "fi de ene"): 0.022,                        # phin pulsa
        ("C8N38", "abaixo do módulo"): 0.478,                 # l2 (n = 15) + ln[1] pulsam
        ("C8N38", "não compartilham fator"): 0.663,           # Indicate(vivas) + FadeIn(conta)
        ("C8N39", "módulo grande"): 0.151,                    # o salto para 35 começa
        ("C8N40", "fosse primo"): 0.079,                      # o primeiro play (grade 11, l2c → l2d) começa
        ("C8N40", "contagem"): 0.179,                         # Indicate(tab11[2]) + FadeIn(conta11)
        ("C8N40", "chave privada"): 0.907,                    # Indicate(c1[1])
        ("C8N41", "dois primos"): 0.179,                      # Write(c3[0:5]) começa
        ("C8N41", "múltiplos de p"): 0.737,                   # riscos r_p + Indicate(c3[2]) + o 3 de l2e
        ("C8N41", "os de q"): 0.916,                          # riscos r_q + Indicate(c3[4]) + o 5 de l2e
        ("C8N43", "p e q"): 0.351,                            # c3[2], c3[4], c3[11], c3[15] pulsam
        ("C8N43", "produto dos dois"): 0.561,                 # Indicate(c3[0])
        ("C8N44", "esse número"): 0.842,                      # c4[3] (o n) + c3[0] pulsam
        ("V3N01", "número grande"): 0.712,                    # o n da tese (tese[0][3]) pulsa
        # vídeo 4, abertura e capítulo 9 — idem (estimativa por caracteres)
        ("V4N00", "número grande"):         0.385,  # o Indicate(cad[2]) (o "fatorar n" gravado)
        ("C9N01", "o resto"):               0.927,  # eq[0] (o c) pulsa
        ("C9N02", "módulo"):                0.019,  # escolha[2] (o 9) + eq[3][1] (o 9) pulsam
        ("C9N02", "a base"):                0.107,  # escolha[6] (o 4) + eq[2][0] (o 4) pulsam
        ("C9N02", "expoente"):              0.417,  # eq[2][1] (o b) pulsa
        ("C9N03", "módulo"):                0.354,  # escolha[2] + eq[3][1] pulsam, no play da tabela
        ("C9N04", "linha da base"):         0.294,  # GrowArrow(seta4) + Indicate(head_l[4])
        ("C9N05", "expoente zero"):         0.438,  # f0[0] (o 4⁰) pulsa
        ("C9N05", "vale um"):               0.833,  # f0[2] + c00 pulsam
        ("C9N06", "no expoente"):           0.178,  # eq[2][1] (o b) pulsa
        ("C9N06", "pela base"):             0.554,  # eq[2][0] (o 4) + head_l[4] pulsam
        ("C9N07", "linha da base"):         0.274,  # head_l[4] + seta4 pulsam, em paralelo com o laço
        ("C9N07", "resultado"):             0.500,  # fs[0][2] (o 4) pulsa, em paralelo com o laço
        ("C9N08", "o um"):                  0.438,  # fs[2][2] + c00 pulsam, depois do Write(fs[2])
        ("C9N10", "potências"):             0.513,  # mult[2] e mult[4] (as que já estão em cena) pulsam
        ("C9N10", "mesmo resto"):           0.842,  # mult[0] (o 1) pulsa
        ("C9N11", "O menor"):               0.000,  # o play do rdef
        ("C9N13", "contagem de Euler"):     0.739,  # Write(cont9) + Indicate(phi4)
        ("C9N14", "um expoente"):           0.237,  # d3[0][1] (o r) pulsa
        ("C9N14", "módulos grandes"):       0.789,  # o primeiro salto da malha (malha21, l21, c21)
        ("C9N15", "o menor expoente"):      0.236,  # Indicate(d3[0][1])
        ("C9N15", "devolve um"):            0.427,  # d3[2] (o 1) pulsa
        # vídeo 4, capítulo 11 e V4N02 — idem (estimativa por caracteres)
        ("C11N01", "bits"):                       0.945,  # a `fila` inteira pulsa, em cascata
        ("C11N02", "zero"):                       0.731,  # `meio` (o cartão 0) pulsa
        ("C11N02", "ele é um"):                   0.866,  # `meio → bit_1` começa; `bit_1 → bit_0` logo depois
        ("C11N05", "zero"):                       0.420,  # `q1[2]` (o 0) pulsa
        ("C11N05", "ou um"):                      0.481,  # `q1[1]` (o 1) pulsa
        ("C11N06", "cada um dos dois"):           0.787,  # as duas `barras` + `q1[1]` + `q1[2]` pulsam
        ("C11N10", "um n"):                       0.390,  # `eqc[3][1]` (o 21) pulsa, depois do `Write(eqc)`
        ("C11N11", "cada bit"):                   0.515,  # as caixas de bit (`bits`) nascem
        ("C11N11", "uma potência"):               0.874,  # as caixas cinzas (`caixas`) e as setas nascem
        ("C11N12", "potência inteira"):           0.506,  # `FadeIn(prod)`
        ("C11N12", "resto"):                      0.926,  # `GrowArrow(seta4)` + `TransformFromCopy(eqc[0], saida)`, com `eqc[0]` pulsando
        ("C11N14", "expoente b"):                 0.391,  # `TransformFromCopy(eqc[2][1], letra_b)`, com `eqc[2][1]` pulsando
        ("C11N14", "resto c"):                    0.884,  # o `saida_circ` desliza para o painel, com `eqc[0]` pulsando
        ("C11N15", "cada bit"):                   0.289,  # o `LaggedStart` dos bits virando qubits começa
        ("C11N16", "todos eles"):                 0.500,  # `letra_b → carta_b[1]` + `FadeIn(carta_b[2])`
        ("C11N17", "emaranhados"):                0.293,  # os quatro `plugues` em cascata: o ponto pulsa e o brilho azul desce a ligação — estimada
        ("C11N17", "o expoente"):                 0.481,  # `carta_b[1]` (a coluna) pulsa — estimada
        ("C11N17", "resto c"):                    0.827,  # `saida_circ → carta_c[1]` + `FadeIn(carta_c[2])` — estimada
        ("C11N19", "resto possível"):             0.094,  # `Flash(med)` + `carta_c → cartao_c`
        ("C11N19", "expoentes"):                  0.658,  # `lista_b → bs_de_4`
        ("C11N22", "interessa: o r"):             0.913,  # a batida 4 (`pergunta_r` fica vermelho); a 5 vem logo depois
        ("C11N23", "informação do r"):            0.872,  # `pergunta_r` pulsa
        ("C11N24", "potência de dois"):           0.545,  # `FadeIn(nq)`
        ("C11N25", "expoentes que sobreviveram"): 0.440,  # `lista_b` + `tres_b` (a coluna e o `⋮`) pulsam
        ("C11N25", "pergunta"):                   0.727,  # `pergunta_r` pulsa
        ("C11N27", "a ordem"):                    0.566,  # o `LaggedStart` das chaves com os `r` começa, com `pergunta_r[0]` pulsando
        ("C11N28", "fim do registrador"):         0.762,  # o `Indicate(nq)`
        ("C11N34", "múltiplos"):                  0.412,  # o `LaggedStart` das marcas começa
        ("C11N34", "ordem"):                      0.938,  # `rots_marca[1:]` (os `k·N/r`) pulsam
        ("C11N36", "oitenta e cinco"):            0.515,  # `Flash` + `coluna_k → unico_k`
        ("C11N37", "tamanho do registrador"):     0.325,  # o `N` de `eq_k` (`eq_k[4]`) pulsa
        ("C11N37", "a ordem"):                    0.650,  # o `r` de `linhas[0]` (`linhas[0][6]`) pulsa, depois da troca
        ("C11N38", "fração reduzida"):            0.688,  # o `Write(linhas[1])`
        ("C11N38", "ali"):                        0.958,  # o `Circumscribe(linhas[0][0:3])`
        ("C11N39", "denominador"):                0.093,  # o 6 de `linhas[1]` (`linhas[1][6]`) pulsa
        ("C11N39", "ordem que faltava"):          0.581,  # `pergunta_r → linhas[2]`
        ("C11N40", "potência"):                   0.274,  # o `Write(linhas[3])`
        ("C11N40", "devolve um"):                 0.419,  # `linhas[3][2]` (o 1) pulsa
        ("C11N42", "fração"):                     0.068,  # `frac_esq → frac_dir`
        ("C11N42", "denominador"):                0.507,  # `frac_dir[3]` (o 3) pulsa
        ("C11N42", "da ordem"):                   0.877,  # `TransformFromCopy(linhas[2], falha_r)`
        ("C11N46", "o número"):                   0.410,  # `linhas[6][0]` (o 21) pulsa, depois do `Write(linhas[6])`
        ("V4N02", "o exemplo"):                   0.037,  # o `Indicate(caixa[0][0])` (o 21)
        ("V4N02", "dois dígitos"):                0.217,  # `TransformFromCopy(caixa[0][0], semente)`
        ("V4N02", "centenas"):                    0.407,  # o segundo `LaggedStart` de dígitos começa
        ("V4N02", "milhares de qubits"):          0.624,  # as `cartas` começam a entrar
        # vídeo 4, capítulo 10 — idem (estimativa por caracteres)
        ("C10N01", "número do RSA"):              0.154,  # o `Indicate(obj[2])` (o 35)
        ("C10N01", "dois primos"):                0.526,  # os `Indicate(obj[4])` (o p) + `Indicate(obj[6])` (o q)
        ("C10N02", "uma base"):                   0.419,  # `Write(base)`
        ("C10N03", "pela base"):                  0.724,  # o 8 de `base` + o 8 de `rotulo` pulsam
        ("C10N04", "Quatro passos"):              0.000,  # os `Indicate` dos quatro `×8`
        ("C10N04", "ordem é quatro"):             0.746,  # `Write(rper)`; o `Indicate(rper[2])` logo depois
        ("C10N06", "Diminuindo um"):              0.000,  # `e1 → e2`; o `Indicate(e2[1])` logo depois
        ("C10N06", "a ordem"):                    0.464,  # `rper` pulsa
        ("C10N06", "múltiplo do número"):         0.636,  # `FadeIn(nota)`; `Indicate(nota[2])` + o 35 de `obj` logo depois
        ("C10N07", "potência menos um"):          0.361,  # `e3[0]` + `e3[1]` pulsam
        ("C10N07", "35"):                         0.820,  # o `Indicate(e3[4])`
        ("C10N07", "vezes x"):                    0.869,  # o `Indicate(e3[2])`
        ("C10N08", "tronco"):                     0.544,  # o `Indicate(rb)`
        ("C10N08", "os fatores"):                 0.759,  # o `Indicate(fBx, fB35)`
        ("C10N09", "o x"):                        0.179,  # o `Write(ex)` + `Indicate(fBx)`
        ("C10N10", "potência menos um"):          0.303,  # o `Indicate(eqB_a)`
        ("C10N11", "ordem r"):                    0.478,  # `TransformFromCopy(rper[0], d0[0])` + `Write(d0[1:3])`, com `rper[0]` pulsando
        ("C10N12", "mesmo número"):               0.343,  # os `Indicate(ra)` + `Indicate(rb)`
        ("C10N13", "fatores de 35"):              0.425,  # os `Indicate(fB35, nB[2], nB[3])`
        ("C10N13", "os de 117"):                  0.650,  # os `Indicate(fB117, nB[0], nB[1])`
        ("C10N15", "p e q"):                      0.733,  # os `Indicate` do p (`nA[0]`, `nB[3]`); os do q (`nA[3]`, `nB[2]`) logo depois
        ("C10N16", "dois números"):               0.248,  # o `Indicate(fA65, fA63)`
        ("C10N16", "número que queremos fatorar"):0.769,  # o `Indicate(obj[0])` + `obj[2]` (o 35)
        ("C10N18", "p e q"):                      0.506,  # os `Indicate(fim[2], fim[4])`
        ("C10N19", "O número"):                   0.000,  # `obj2[2]` (o 35) pulsa, depois do `obj → obj2`
        ("C10N20", "a base"):                     0.667,  # `realce(o0[2])` (o 11)
        ("C10N20", "ordem ímpar"):                0.900,  # `Wiggle` nos `3/2` + `✗` + `Indicate(o0[6])`
        ("C10N22", "ordem par"):                  0.859,  # o `Indicate(u0[6])`
        ("C10N24", "dois primos"):                0.267,  # os `Indicate(nU[0], nU[1])`
        ("C10N25", "esse número"):                0.344,  # `FadeIn(multi)` + `GrowArrow(setam)` + `Indicate(fu1)`
        ("C10N25", "de 35"):                      0.902,  # o `Indicate(multi[1])`
        ("C10N26", "35"):                         0.861,  # o `Indicate(m3[5])`
        ("C10N27", "número do outro lado"):       0.289,  # `fu2` + `m4[1]` (o 13823) pulsam
        ("C10N27", "nenhum fator"):               0.639,  # o `Indicate(m4[5])` (o 1)
        ("C10N28", "dois fatores triviais"):      0.079,  # os `Indicate(m3[5], m4[5])`
        ("C10N28", "de 35"):                      0.326,  # `fim[0]` (o 35 da moldura) pulsa
        ("C10N29", "a base"):                     0.203,  # `u0[2]` (o 24) pulsa
        ("C10N30", "dois primos"):                0.119,  # `fim[2]` + `fim[4]` pulsam, no `play` do `fim.copy() → r1`
        ("C10N30", "contagem de Euler"):          0.695,  # o `Indicate(r1[12])` + `r1[0:3]` (o φ(35)) pulsam
        ("C10N31", "a chave privada"):            0.139,  # o `Indicate(r2[2])` (o d)
        ("C10N31", "chave pública"):              0.570,  # o `Indicate(r2[0])` + `Indicate(r2[5:8])`
        ("C10N32", "módulo"):                     0.264,  # `r3[1]` (o n) pulsa, depois do `Write(r3)`
    },
    "en": {
        **_V1["en"],
        # V0N00 — a seta ↓ nasce no rodapé
        ("V0N00", "descrição"): 0.942,   # "description" — estimativa por caracteres
        # vídeo 2, capítulo 1 — palavra correspondente em en, estimativa por
        # caracteres (a medir na gravação)
        ("C1N04", "dois"): 0.695,            # "two"
        ("C1N05", "Dois é"): 0.000,            # "Two is"
        ("C1N05", "onze"): 0.133,            # "eleven"
        ("C1N05", "três"): 0.223,            # "three"
        ("C1N06", "onze"): 0.000,              # "Eleven"
        ("C1N07", "resto"): 0.616,           # "remainder"
        ("C1N08", "cinco"): 0.591,           # "five"
        ("C1N09", "dois"): 0.106,            # "two"
        ("C1N10", "três"): 0.063,            # "Three"
        ("C1N10", "quatro números"): 0.116,  # "four numbers"
        # vídeo 2, capítulo 2 — idem
        ("C2N01", "números"): 0.186,         # "numbers"
        ("C2N01", "resto"): 0.312,           # "remainder"
        ("C2N03", "um x"): 0.195,            # "x as"
        ("C2N03", "por n"): 0.296,           # "n minus"
        ("C2N03", "menos a"): 0.350,         # "minus a"
        ("C2N03", "Sete"): 0.499,            # "Seven"
        ("C2N03", "cinco"): 0.568,           # "five"
        ("C2N03", "a dois"): 0.668,          # "is two"
        ("C2N03", "traço amarelo"): 0.866,   # "yellow segment"
        ("C2N04", "comparação"): 0.110,      # "comparison"
        ("C2N04", "x é"): 0.257,             # "is x"
        ("C2N04", "que b"): 0.350,           # "than b"
        ("C2N04", "módulo"): 0.725,          # "modulus"
        ("C2N04", "soma"): 0.946,            # "sum"
        ("C2N05", "resto"): 0.104,           # "remainder"
        ("C2N05", "a b"): 0.196,             # "is b"
        ("C2N05", "menos x"): 0.319,         # "minus x"
        ("C2N05", "Seis"): 0.581,            # "Six"
        ("C2N05", "dois"): 0.754,            # "two"
        ("C2N05", "quatro"): 0.888,          # "four"
        ("C2N06", "seis"): 0.110,            # "six"
        ("C2N06", "cinco"): 0.158,           # "five"
        ("C2N06", "quatro"): 0.308,          # "four"
        ("C2N06", "sete"): 0.402,            # "seven"
        ("C2N07", "módulo"): 0.634,          # "modulus"
        ("C2N08", "doze"): 0.047,            # "twelve"
        ("C2N08", "amarelo"): 0.487,         # "yellow"
        ("C2N08", "vermelho"): 0.674,        # "red"
        ("C2N08", "teste"): 0.801,           # "test"
        ("C2N09", "módulo"): 0.122,          # "modulus"
        ("C2N09", "resto"): 0.466,           # "remainder"
        ("C2N09", "Seis"): 0.757,            # "Six"
        ("C2N09", "cinco"): 0.821,           # "five"
        ("C2N09", "onze"): 0.915,            # "eleven"
        ("C2N10", "Onze é"): 0.000,            # "Eleven is"
        ("C2N10", "a onze"): 0.160,          # "to eleven"
        ("C2N10", "doze"): 0.264,            # "twelve"
        ("C2N10", "x maior"): 0.436,         # "is x"
        ("C2N10", "que b"): 0.523,           # "than b"
        # vídeo 2, capítulo 3 — idem
        ("C3N01", "somas sucessivas"): 0.665, # "repeated addition"
        ("C3N02", "vinte"): 0.293,            # "twenty"
        ("C3N02", "o sete"): 0.440,           # "seven fits"
        ("C3N02", "resto"): 0.889,            # "remainder"
        ("C3N03", "multiplicador"): 0.297,    # "multiplier"
        ("C3N05", "por dois"): 0.555,         # "by two"
        ("C3N06", "juntamos"): 0.392,         # "merge"
        ("C3N06", "termo que sobrou"): 0.719, # "leftover term"
        ("C3N07", "potências de dois"): 0.104,# "powers of two"
        ("C3N07", "multiplicador"): 0.805,    # "multiplier"
        ("C3N08", "bit do meio"): 0.080,      # "middle bit"
        ("C3N08", "termo dele"): 0.487,       # "its term"
        ("C3N09", "sete"): 0.523,             # "seven"
        ("C3N10", "bit desligado"): 0.078,    # "bit is off"
        ("C3N10", "zero"): 0.448,             # "zero"
        ("C3N11", "as três"): 0.246,          # "the three"
        ("C3N11", "sete"): 0.833,             # "seven"
        ("C3N12", "seis"): 0.607,             # "six"
        ("C3N13", "multiplicador"): 0.739,    # "multiplier"
        ("C3N13", "bits"): 0.909,             # "bits"
        # vídeo 2, capítulo 4 — idem
        ("C4N02", "setecentos"): 0.215,       # "seven hundred"
        ("C4N02", "setes"): 0.512,            # "sevens"
        ("C4N02", "resto"): 0.906,            # "remainder"
        ("C4N03", "expoente"): 0.338,         # "exponent"
        ("C4N05", "quadrado"): 0.597,         # "squaring"
        ("C4N07", "juntamos"): 0.267,         # "merge"
        ("C4N07", "potências de dois"): 0.792,# "powers of two"
        ("C4N08", "potências de dois"): 0.094,# "powers of two"
        ("C4N08", "expoente"): 0.826,         # "exponent"
        ("C4N09", "último bit"): 0.079,       # "last bit"
        ("C4N09", "termo dele"): 0.505,       # "its term"
        ("C4N10", "sete"): 0.563,             # "seven"
        ("C4N11", "bit desligado"): 0.096,    # "bit is off"
        ("C4N11", "é o um"): 0.420,           # "is one"
        ("C4N12", "os três"): 0.288,          # "the three"
        ("C4N12", "sete"): 0.859,             # "seven"
        ("C4N13", "um"): 0.708,               # "one"
        ("C4N14", "expoente"): 0.783,         # "exponent"
        ("C4N14", "bits"): 0.921,             # "bits"
        # vídeo 2, capítulo 5 — idem
        ("C5N02", "meio número"): 0.478,            # "half a number"
        ("C5N03", "qual número"): 0.386,            # "which number"
        ("C5N04", "inverso"): 0.690,                # "inverse"
        ("C5N05", "resto um"): 0.846,               # "is one"
        ("C5N06", "Cinco"): 0.000,                  # "Five"
        ("C5N06", "dois"): 0.543,                   # "two"
        ("C5N06", "nove"): 0.832,                   # "nine"
        ("C5N08", "módulo"): 0.294,                 # "modulus"
        ("C5N10", "inverso"): 0.668,                # "inverse"
        ("C5N11", "três"): 0.358,                   # "three"
        ("C5N11", "nove"): 0.654,                   # "nine"
        ("C5N12", "O um"): 0.810,                   # "One is"
        ("C5N13", "três"): 0.167,                   # "three"
        ("C5N13", "nove"): 0.341,                   # "nine"
        ("C5N14", "módulo"): 0.852,                 # "modulus"
        ("C5N14", "um fator"): 0.625,               # "a factor"
        ("C5N15", "módulo"): 0.710,                 # "modulus"
        ("C5N17", "dá um"): 0.401,                  # "is one"
        ("C5N17", "linha"): 0.496,                  # "row"
        ("C5N17", "coluna"): 0.560,                 # "column"
        ("C5N19", "números sem inverso"): 0.818,    # "numbers with no inverse"
        ("C5N20", "módulo"): 0.753,                 # "modulus"
        # vídeo 3, capítulo 6 — palavra correspondente em en, medida no
        # audio/en com faster-whisper (small.en; início da palavra ÷ duração
        # da locução; o transcritor ouviu "model", "reminders", "7", "1" no
        # lugar de "modulus", "remainders", "seven", "one")
        ("C6N01", "módulo sete"): 0.867,            # "modulus seven" — texto novo: estimativa por caracteres, a medir na gravação
        ("C6N02", "sete"): 0.889,                   # "seven"
        ("C6N06", "Os números"): 0.000,             # "The numbers" — texto novo: estimativa por caracteres, a medir na gravação
        ("C6N10", "restos"): 0.372,                 # "remainders"
        ("C6N10", "módulo"): 0.721,                 # "modulus"
        ("C6N11", "módulo"): 0.072,                 # "modulus"
        ("C6N11", "produto inteiro"): 0.757,        # "whole product"
        ("C6N12", "potência"): 0.326,               # "power"
        ("C6N12", "a um"): 0.600,                   # "to one"
        ("C6N12", "sete"): 0.851,                   # "seven"
        ("C6N13", "módulo é primo"): 0.057,         # "modulus is prime"
        ("C6N13", "valor a"): 0.523,                # "value a"
        ("C6N13", "múltiplo do módulo"): 0.813,     # "multiple of the modulus"
        ("C6N15", "o módulo precisa"): 0.280,       # "the modulus has"
        ("C6N15", "precisa ser primo"): 0.389,      # "has to be prime"
        # vídeo 3, capítulo 7 — medidas no audio/en com faster-whisper
        # (small.en; início da palavra ÷ duração; ouviu "reminders", "rules",
        # "modules", "9" no lugar de "remainders", "rows", "modulus", "nine"; no
        # C7N12 não transcreveu o "to" de "to one": vale o "one")
        ("C7N02", "multiplicador"): 0.224,          # "multiplier"
        ("C7N02", "lista de restos"): 0.554,        # "list of remainders"
        ("C7N04", "cancelar a lista"): 0.611,       # "canceling the list"
        ("C7N05", "dois desses fatores"): 0.415,    # "two of these factors"
        ("C7N05", "módulo"): 0.912,                 # "modulus"
        ("C7N06", "linhas"): 0.132,                 # "rows"
        ("C7N07", "números que não têm inverso"): 0.558,  # "numbers that have no inverse"
        ("C7N08", "números"): 0.269,                # "numbers"
        ("C7N08", "módulo"): 0.821,                 # "modulus"
        ("C7N09", "contagem"): 0.042,               # "how many"
        ("C7N09", "fi de ene"): 0.773,              # "phi of n"
        ("C7N12", "potência"): 0.395,               # "power"
        ("C7N12", "a um"): 0.557,                   # "(to) one"
        ("C7N12", "nove"): 0.904,                   # "nine"
        ("C7N13", "qualquer módulo"): 0.104,        # "any modulus"
        ("C7N13", "o expoente"): 0.271,             # "the exponent"
        ("C7N13", "totiente"): 0.839,               # "totient"
        # vídeo 3, capítulo 8 (C8N12–C8N24) — medidas no audio/en com
        # faster-whisper (small.en; início da palavra ÷ duração). No C8N19 o
        # transcritor ouviu "when" no lugar de "one" em "one undoing" (5,72 s)
        ("C8N12", "número a"): 0.052,                     # "number A"
        ("C8N12", "Multiplicamos"): 0.737,                # "We multiply"
        ("C8N13", "se somam"): 0.754,                     # "add up"
        ("C8N14", "expoente"): 0.406,                     # "exponent"
        ("C8N14", "reescrito"): 0.582,                    # "rewritten"
        ("C8N14", "fi de ene"): 0.816,                    # "phi of n"
        ("C8N15", "Qualquer expoente"): 0.000,            # "Any exponent"
        ("C8N15", "mensagem"): 0.560,                     # "message"
        ("C8N16", "expoente"): 0.837,                     # "exponent"
        ("C8N17", "dois números"): 0.522,                 # "two numbers"
        ("C8N17", "dê um"): 0.667,                        # "is one"
        ("C8N17", "módulo do expoente"): 0.823,           # "modulus of the exponent"
        ("C8N18", "par"): 0.111,                          # "pair"
        ("C8N18", "expoente"): 0.761,                     # "exponent"
        ("C8N19", "produto no expoente"): 0.049,          # "product in the exponent"
        ("C8N19", "potência de outra potência"): 0.390,   # "power of a power"
        ("C8N19", "uma desfazendo"): 0.744,               # "one undoing"
        ("C8N19", "a outra"): 0.905,                      # "the other"
        ("C8N20", "mensagem"): 0.828,                     # "message"
        ("C8N21", "primeira potência"): 0.041,            # "first power"
        ("C8N21", "módulo"): 0.300,                       # "modulus"
        ("C8N21", "mensagem"): 0.523,                     # "message"
        ("C8N21", "cifra"): 0.851,                        # "ciphertext"
        ("C8N23", "segunda potência"): 0.066,             # "second power"
        ("C8N23", "primeira"): 0.358,                     # "the first"
        ("C8N23", "mensagem original"): 0.765,            # "original message"
        ("C8N24", "expoente que desfaz"): 0.067,          # "exponent that undoes"
        ("C8N24", "módulo"): 0.416,                       # "modulus"
        # vídeo 3, capítulo 8 (C8N26–C8N44) e V3N01 — medidas no audio/en com faster-whisper
        # (small.en; início da palavra ÷ duração; "modules" no lugar de "modulus")
        ("C8N26", "módulo"): 0.229,                           # "modulus"
        ("C8N27", "módulo"): 0.085,                           # "modulus"
        ("C8N27", "fi de ene"): 0.436,                        # "phi of n"
        ("C8N27", "módulo do expoente"): 0.695,               # "modulus of the exponent"
        ("C8N28", "par de inversos"): 0.621,                  # "inverse pair"
        ("C8N29", "desse par"): 0.194,                        # "this pair"
        ("C8N29", "mesmo módulo"): 0.844,                     # "same modulus"
        ("C8N30", "números escolhidos"): 0.659,               # "numbers we choose"
        ("C8N31", "mensagem"): 0.048,                         # "message"
        ("C8N31", "menor que o módulo"): 0.692,               # "smaller than the modulus"
        ("C8N32", "lugar da letra"): 0.426,                   # "place of the letter"
        ("C8N34", "cifra"): 0.498,                            # "decrypt it"
        ("C8N35", "números"): 0.653,                          # "numbers"
        ("C8N36", "fi de ene"): 0.596,                        # "phi of n"
        ("C8N36", "encontrar a privada"): 0.798,              # "find a private one"
        ("C8N36", "a partir da pública"): 0.878,              # "from the public one"
        ("C8N37", "conhece o módulo"): 0.324,                 # "know the modulus"
        ("C8N37", "fi de ene"): 0.826,                        # "phi of n"
        ("C8N38", "fi de ene"): 0.046,                        # "phi of n"
        ("C8N38", "abaixo do módulo"): 0.495,                 # "below the modulus"
        ("C8N38", "não compartilham fator"): 0.676,           # "share no factor"
        ("C8N39", "módulo grande"): 0.109,                    # "large modulus"
        ("C8N40", "fosse primo"): 0.076,                      # "were prime"
        ("C8N40", "contagem"): 0.192,                         # "the count"
        ("C8N40", "chave privada"): 0.911,                    # "private key"
        ("C8N41", "dois primos"): 0.143,                      # "two primes"
        ("C8N41", "múltiplos de p"): 0.647,                   # "multiples of p"
        ("C8N41", "os de q"): 0.880,                          # "those of q"
        ("C8N43", "p e q"): 0.343,                            # "p and q"
        ("C8N43", "produto dos dois"): 0.628,                 # "their product"
        ("C8N44", "esse número"): 0.824,                      # "this number"
        ("V3N01", "número grande"): 0.746,                    # "large number"
        # vídeo 4, abertura e capítulo 9 — medidas no audio/en com faster-whisper
        ("V4N00", "número grande"):         0.436,  # "large"
        ("C9N01", "o resto"):               0.858,  # "the remainder"
        ("C9N02", "módulo"):                0.032,  # "modulus"
        ("C9N02", "a base"):                0.131,  # "the base"
        ("C9N02", "expoente"):              0.440,  # "exponent"
        ("C9N03", "módulo"):                0.338,  # "modulus"
        ("C9N04", "linha da base"):         0.284,  # "base's row"
        ("C9N05", "expoente zero"):         0.345,  # "exponent zero"
        ("C9N05", "vale um"):               0.795,  # "is one"
        ("C9N06", "no expoente"):           0.211,  # "in the exponent"
        ("C9N06", "pela base"):             0.526,  # "by the base"
        ("C9N07", "linha da base"):         0.258,  # "base's row"
        ("C9N07", "resultado"):             0.448,  # "the result"
        ("C9N08", "o um"):                  0.383,  # "on one"
        ("C9N10", "potências"):             0.498,  # "powers"
        ("C9N10", "mesmo resto"):           0.792,  # "same remainder"
        ("C9N11", "O menor"):               0.000,  # "The smallest"
        ("C9N13", "contagem de Euler"):     0.817,  # "Euler's count"
        ("C9N14", "um expoente"):           0.196,  # "one exponent"
        ("C9N14", "módulos grandes"):       0.800,  # "large moduli"
        ("C9N15", "o menor expoente"):      0.240,  # "the smallest exponent"
        ("C9N15", "devolve um"):            0.421,  # "gives back one"
        # vídeo 4, capítulo 11 — medidas no audio/en com faster-whisper; V4N02 estimada por caracteres (não há audio/en/V4N02.wav)
        ("C11N10", "outro exemplo"):              0.207,  # "another example" — medida; a pt do C11N10 não mudou
        ("C11N01", "bits"):                       0.879,  # "bits"
        ("C11N02", "zero"):                       0.715,  # "zero"
        ("C11N02", "ele é um"):                   0.814,  # "or one"
        ("C11N05", "zero"):                       0.357,  # "zero"
        ("C11N05", "ou um"):                      0.425,  # "or one"
        ("C11N06", "cada um dos dois"):           0.771,  # "each of the two"
        ("C11N10", "um n"):                       0.311,  # "an n"
        ("C11N11", "cada bit"):                   0.476,  # "each bit"
        ("C11N11", "uma potência"):               0.756,  # "a power"
        ("C11N12", "potência inteira"):           0.561,  # "whole power"
        ("C11N12", "resto"):                      0.888,  # "remainder"
        ("C11N14", "expoente b"):                 0.349,  # "exponent b"
        ("C11N14", "resto c"):                    0.817,  # "remainder c"
        ("C11N15", "cada bit"):                   0.351,  # "each bit"
        ("C11N16", "todos eles"):                 0.496,  # "all of them"
        ("C11N17", "emaranhados"):                0.266,  # "entangled" — estimada, a medir na regravação (o audio/en/C11N17.wav atual é a fala antiga)
        ("C11N17", "o expoente"):                 0.430,  # "the exponent" — estimada, a medir na regravação
        ("C11N17", "resto c"):                    0.773,  # "remainder c" — estimada, a medir na regravação
        ("C11N19", "resto possível"):             0.086,  # "possible remainder"
        ("C11N19", "expoentes"):                  0.644,  # "exponents"
        ("C11N22", "interessa: o r"):             0.883,  # "matters: r"
        ("C11N23", "informação do r"):            0.800,  # "information about r"
        ("C11N24", "potência de dois"):           0.599,  # "power of two"
        ("C11N25", "expoentes que sobreviveram"): 0.458,  # "exponents that survived"
        ("C11N25", "pergunta"):                   0.794,  # "question"
        ("C11N27", "a ordem"):                    0.486,  # "the order"
        ("C11N28", "fim do registrador"):         0.758,  # "end of the register"
        ("C11N34", "múltiplos"):                  0.377,  # "multiples"
        ("C11N34", "ordem"):                      0.901,  # "order"
        ("C11N36", "oitenta e cinco"):            0.542,  # "eighty-five"
        ("C11N37", "tamanho do registrador"):     0.168,  # "register size"
        ("C11N37", "a ordem"):                    0.713,  # "the order"
        ("C11N38", "fração reduzida"):            0.683,  # "reduced fraction"
        ("C11N38", "ali"):                        0.903,  # "there"
        ("C11N39", "denominador"):                0.164,  # "denominator"
        ("C11N39", "ordem que faltava"):          0.624,  # "missing order"
        ("C11N40", "potência"):                   0.387,  # "power"
        ("C11N40", "devolve um"):                 0.458,  # "gives back one"
        ("C11N42", "fração"):                     0.184,  # "fraction"
        ("C11N42", "denominador"):                0.579,  # "denominator"
        ("C11N42", "da ordem"):                   0.861,  # "of the order"
        ("C11N46", "o número"):                   0.484,  # "the number"
        ("V4N02", "o exemplo"):                   0.047,  # "number we just factored" — estimada
        ("V4N02", "dois dígitos"):                0.212,  # "two digits" — estimada
        ("V4N02", "centenas"):                    0.382,  # "hundreds" — estimada
        ("V4N02", "milhares de qubits"):          0.612,  # "thousands of stable qubits" — estimada
        # vídeo 4, capítulo 10 — medidas no audio/en com faster-whisper
        ("C10N01", "número do RSA"):              0.190,  # "RSA number"
        ("C10N01", "dois primos"):                0.580,  # "two primes"
        ("C10N02", "uma base"):                   0.455,  # "any base"
        ("C10N03", "pela base"):                  0.683,  # "by the base"
        ("C10N04", "Quatro passos"):              0.175,  # "four steps"
        ("C10N04", "ordem é quatro"):             0.648,  # "order is four"
        ("C10N06", "Diminuindo um"):              0.000,  # "Subtracting one"
        ("C10N06", "a ordem"):                    0.439,  # "the order"
        ("C10N06", "múltiplo do número"):         0.668,  # "multiple of the number"
        ("C10N07", "potência menos um"):          0.251,  # "power minus one"
        ("C10N07", "35"):                         0.637,  # "thirty-five"
        ("C10N07", "vezes x"):                    0.771,  # "times x"
        ("C10N08", "tronco"):                     0.559,  # "trunk"
        ("C10N08", "os fatores"):                 0.799,  # "the factors"
        ("C10N09", "o x"):                        0.042,  # "find x"
        ("C10N10", "potência menos um"):          0.304,  # "power minus one"
        ("C10N11", "ordem r"):                    0.398,  # "order r"
        ("C10N12", "mesmo número"):               0.262,  # "same number"
        ("C10N13", "fatores de 35"):              0.268,  # "factors of thirty-five"
        ("C10N13", "os de 117"):                  0.618,  # "one hundred seventeen"
        ("C10N15", "p e q"):                      0.679,  # "p and q"
        ("C10N16", "dois números"):               0.201,  # "two numbers"
        ("C10N16", "número que queremos fatorar"):0.750,  # "number we want to factor"
        ("C10N18", "p e q"):                      0.345,  # "p and q"
        ("C10N19", "O número"):                   0.000,  # "The number"
        ("C10N20", "a base"):                     0.680,  # "the base"
        ("C10N20", "ordem ímpar"):                0.837,  # "odd order"
        ("C10N22", "ordem par"):                  0.818,  # "even order"
        ("C10N24", "dois primos"):                0.185,  # "two primes"
        ("C10N25", "esse número"):                0.264,  # "this number"
        ("C10N25", "de 35"):                      0.833,  # "thirty-five"
        ("C10N26", "35"):                         0.512,  # "thirty-five"
        ("C10N27", "número do outro lado"):       0.175,  # "number on the other side"
        ("C10N27", "nenhum fator"):               0.546,  # "no factor"
        ("C10N28", "dois fatores triviais"):      0.105,  # "two trivial factors"
        ("C10N28", "de 35"):                      0.333,  # "thirty-five"
        ("C10N29", "a base"):                     0.215,  # "the base"
        ("C10N30", "dois primos"):                0.098,  # "both primes"
        ("C10N30", "contagem de Euler"):          0.699,  # "Euler's count"
        ("C10N31", "a chave privada"):            0.220,  # "the private key"
        ("C10N31", "chave pública"):              0.657,  # "public key"
        ("C10N32", "módulo"):                     0.302,  # "modulus"
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
