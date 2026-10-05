# -*- coding: utf-8 -*-
"""Todo texto em língua natural que aparece NA TELA, num lugar só.

Cada entrada tem o português e o inglês; o inglês vazio (None) cai no
português, então nada muda na tela enquanto a tradução não for feita.
Números, símbolos, letras de variável e notação ("(mod ", "φ(") ficam no
código — aqui só mora o que muda de idioma.

Chaves com o prefixo do arquivo, pelo número DE TELA do capítulo (como nas
tags): c1..c11 para shor/capitulos (capitulo9b.py é c10, capitulo10.py é
c11), v1..v4 para shor/videos e geral. para montagem, comum, ferramentas,
cadeado e para o que se repete em mais de um arquivo.

As entradas marcadas "token de formula" / "token de VGroup" são um pedaço
de uma fórmula colorida por tokens: o código conta e indexa as peças, então
a tradução tem de manter UM token por chave — não juntar duas chaves numa
string, nem quebrar uma em duas.

Modelos com {placeholder} são formatados no uso (str.format).

Para listar tudo em tabela: python listar_textos.py
"""

from .idioma import IDIOMA

TEXTOS = {
    # ------------------------------------------------------------- geral
    # glifos — video1.py:874-877 remonta o título com os cacos dos cadeados:
    # o "S" de Shor sai do arco grande e as demais letras, de 3 em 3, dos
    # 10 arcos pequenos (assert). A tradução precisa de um "S" maiúsculo
    # (o de Shor deve ser o primeiro) e de 29 a 31 letras sem os espaços.
    "geral.titulo_serie": {"pt": "Do Zero ao Algoritmo de Shor Quântico", "en": "From 0 to Shor's Quantum Algorithm"},
    # modelo — {n} e {nome} preenchidos no uso (nome = VIDEOS de comum.py)
    "geral.video_n_de_4": {"pt": "Vídeo {n} de 4 — {nome}", "en": "Video {n} of 4 — {nome}"},
    # modelo — {i} preenchido no uso
    "geral.capitulo": {"pt": "Capítulo {i}", "en": "Chapter {i}"},
    "geral.fim": {"pt": "fim", "en": "the end"},
    "geral.binario": {"pt": "binário", "en": "binary"},
    "geral.fatorar_n": {"pt": "fatorar n", "en": "factor n"},
    # também é o nome do vídeo 2 (VIDEOS em videos/comum.py)
    "geral.titulo_cap1": {"pt": "Aritmética modular", "en": "Modular Arithmetic"},
    "geral.titulo_cap2": {"pt": "Adição modular", "en": "Modular Addition"},
    "geral.titulo_cap3": {"pt": "Multiplicação modular — Double and Add", "en": "Modular Multiplication — Double and Add"},
    "geral.titulo_cap4": {"pt": "Exponenciação modular — Square and Multiply", "en": "Modular Exponentiation — Square and Multiply"},
    "geral.titulo_cap5": {"pt": "Inverso multiplicativo modular", "en": "Modular Multiplicative Inverse"},
    # também é o título em tela no fim do capítulo 6
    "geral.titulo_cap6": {"pt": "Pequeno Teorema de Fermat", "en": "Fermat's Little Theorem"},
    "geral.titulo_cap7": {"pt": "A generalização de Euler: φ(n)", "en": "Euler's Generalization: φ(n)"},
    "geral.titulo_cap8": {"pt": "O algoritmo RSA", "en": "The RSA Algorithm"},
    "geral.titulo_cap9": {"pt": "Ordem Modular", "en": "Multiplicative Order"},
    "geral.titulo_cap10": {"pt": "Da Ordem Modular à fatoração", "en": "From Order to Factoring"},
    "geral.titulo_cap11": {"pt": "Shor Quântico: a QFT encontra o período", "en": "Quantum Shor: the QFT Finds the Period"},
    "geral.video1": {"pt": "Introdução", "en": "Introduction"},
    "geral.video3": {"pt": "Do teorema ao RSA", "en": "From Theorem to RSA"},
    "geral.video4": {"pt": "O algoritmo de Shor", "en": "Shor's Algorithm"},
    # modelo — {n} preenchido no uso
    "geral.tabela_mult_mod": {"pt": "Tabela multiplicativa (mod {n})", "en": "Multiplication table (mod {n})"},
    # token de formula — indexado em capitulo7.py:87; capitulo9.py:50
    #   (também token, sem índice direto, em capitulo5.py:88)
    "geral.e": {"pt": "e", "en": "and"},
    # token de formula — indexado em capitulo9.py:50
    #   (também token, sem índice direto, em capitulo5.py:314)
    "geral.inversivel": {"pt": "inversível", "en": "invertible"},
    # token de formula — indexado em capitulo9b.py:523, 527, 537
    #   (também token, sem índice direto, em capitulo10.py:1263, 1266; capitulo5.py:212, 311; capitulo9b.py:410, 413)
    "geral.mdc": {"pt": "mdc(", "en": "gcd("},
    # token de formula — sem índice direto, em capitulo9.py:220; capitulo9b.py:86
    "geral.modulo": {"pt": "módulo", "en": "modulo"},
    # token de formula — indexado em capitulo9b.py:587, 592
    #   (também token, sem índice direto, em capitulo8.py:1068)
    "geral.fatorar": {"pt": "fatorar", "en": "factoring"},
    # token de formula — indexado em capitulo8.py:621, 622, 623, 624, 731, 732, 733, 734, 735
    "geral.publica": {"pt": "pública", "en": "public"},
    # token de formula — indexado em capitulo8.py:655, 656, 657, 658, 737, 738, 739, 740, 741
    "geral.privada": {"pt": "privada", "en": "private"},

    # ---------------------------------------------------- c5 (capitulo5.py)
    "c5.euclides_estendido": {"pt": "Algoritmo de Euclides estendido", "en": "Extended Euclidean Algorithm"},
    # token de formula — sem índice direto, em capitulo5.py:239
    "c5.celula": {"pt": "célula", "en": "cell"},
    # token de formula — sem índice direto, em capitulo5.py:239
    "c5.linha": {"pt": "linha", "en": "row"},
    # token de formula — sem índice direto, em capitulo5.py:240
    "c5.coluna": {"pt": "coluna", "en": "column"},
    "c5.a_e_b_inversos": {"pt": "⇒ a e b são inversos", "en": "⇒ a and b are inverses"},
    # token de formula — sem índice direto, em capitulo5.py:284
    "c5.seta_inversos": {"pt": "→ inversos", "en": "→ inverses"},
    # token de formula — sem índice direto, em capitulo5.py:296
    "c5.nao_inversiveis": {"pt": ": não inversíveis", "en": ": not invertible"},
    # token de formula — sem índice direto, em capitulo5.py:298
    "c5.nunca_congruente": {"pt": "nunca ≡", "en": "never ≡"},

    # ---------------------------------------------------- c6 (capitulo6.py)
    "c6.comutativa": {"pt": "multiplicação é comutativa", "en": "multiplication is commutative"},
    "c6.dividir_os_dois_lados": {"pt": "dividir os dois lados pela mesma multiplicação", "en": "divide both sides by the same product"},
    # token de VGroup — indexado em capitulo6.py:179
    "c6.n_primo": {"pt": "(n primo)", "en": "(n prime)"},

    # ---------------------------------------------------- c7 (capitulo7.py)
    "c7.dividir_e_multiplicar": {"pt": "dividir = multiplicar pelo inverso", "en": "dividing = multiplying by the inverse"},
    # token de formula — indexado em capitulo7.py:87
    "c7.nao_existem": {"pt": "não existem", "en": "don't exist"},
    "c7.teorema_euler": {"pt": "Teorema de Euler", "en": "Euler's Theorem"},

    # ---------------------------------------------------- c8 (capitulo8.py)
    # glifos — _glifos() casa letra a letra com CIFRADO ("Xk9#R2q") em
    # capitulo8.py:44: a tradução tem de ter exatamente 7 caracteres.
    "c8.segredo": {"pt": "SEGREDO", "en": "SECRETS"},
    "c8.quem_envia": {"pt": "quem envia", "en": "sender"},
    "c8.canal_publico": {"pt": "canal público", "en": "public channel"},
    "c8.quem_recebe": {"pt": "quem recebe", "en": "receiver"},
    # em capitulo8.py:516 entra como token de formula, com + " " no fim
    # token de formula — sem índice direto, em capitulo8.py:516
    "c8.tabela_multiplicativa": {"pt": "tabela multiplicativa", "en": "multiplication table"},
    # token de formula — sem índice direto, em capitulo8.py:534
    "c8.par_de_inversos": {"pt": "= par de inversos", "en": "= inverse pair"},
    # token de formula — indexado em capitulo8.py:766, 767
    "c8.mensagem": {"pt": "mensagem:", "en": "message:"},
    # token de formula — indexado em capitulo8.py:978, 982, 984, 986
    "c8.primo_dois_pontos": {"pt": "primo:", "en": "prime:"},
    # token de formula — sem índice direto, em capitulo8.py:967
    "c8.primo": {"pt": "primo", "en": "prime"},
    # token de formula — sem índice direto, em capitulo8.py:1068
    "c8.quebrar_rsa": {"pt": "quebrar RSA", "en": "breaking RSA"},

    # ---------------------------------------------------- c9 (capitulo9.py)
    "c9.somar_1_em_b": {"pt": "somar 1 em b = multiplicar por 4", "en": "adding 1 to b = multiplying by 4"},
    # token de formula — sem índice direto, em capitulo9.py:219
    "c9.ordem_modular_de": {"pt": "ordem modular de", "en": "order of"},
    # token de formula — indexado em capitulo9.py:243, 250
    "c9.o_menor": {"pt": "o menor", "en": "the smallest"},
    # token de formula — indexado em capitulo9.py:243, 250
    "c9.tal_que": {"pt": "tal que", "en": "such that"},
    # token de formula — indexado em capitulo9.py:266
    "c9.pior_caso": {"pt": "pior caso:", "en": "worst case:"},

    # -------------------------------------------------- c10 (capitulo9b.py)
    # token de formula — sem índice direto, em capitulo9b.py:78
    "c10.base": {"pt": "base:", "en": "base:"},
    # token de formula — sem índice direto, em capitulo9b.py:85
    "c10.encontrando_a": {"pt": "encontrando a", "en": "finding the"},
    # token de formula — sem índice direto, em capitulo9b.py:85
    "c10.ordem_modular": {"pt": "ordem modular", "en": "order"},
    # token de formula — sem índice direto, em capitulo9b.py:86
    "c10.de": {"pt": "de", "en": "of"},
    # token de formula — indexado em capitulo9b.py:178
    "c10.e_multiplo_de": {"pt": "é múltiplo de", "en": "is a multiple of"},
    # token de formula — indexado em capitulo9b.py:269, 278
    "c10.par": {"pt": "par", "en": "even"},
    "c10.as_vezes_inutil": {"pt": "às vezes a ordem modular não dá informação útil", "en": "sometimes the order gives no useful information"},
    # token de formula — indexado em capitulo9b.py:509
    "c10.multiplo_de": {"pt": "múltiplo de", "en": "multiple of"},
    # token de formula — sem índice direto, em capitulo9b.py:529
    "c10.fatores_triviais": {"pt": "fatores triviais", "en": "trivial factors"},
    "c10.solucao_outro_a": {"pt": "solução: escolher outro a e recomeçar", "en": "fix: pick another a and start over"},
    # token de formula — indexado em capitulo9b.py:574, 575, 576
    "c10.encontrado": {"pt": "encontrado", "en": "found"},
    # token de formula — indexado em capitulo9b.py:587, 592
    "c10.descobrir_chave_privada": {"pt": "descobrir a chave privada", "en": "recovering the private key"},

    # -------------------------------------------------- c11 (capitulo10.py)
    "c11.computacao_classica": {"pt": "computação clássica", "en": "classical computing"},
    "c11.superposicao": {"pt": "superposição", "en": "superposition"},
    "c11.emaranhamento": {"pt": "emaranhamento", "en": "entanglement"},
    "c11.medir_um_decide_o_outro": {"pt": "medir um decide o outro", "en": "measuring one decides the other"},
    "c11.tqf": {"pt": "TQF", "en": "QFT"},
    "c11.mais_81_ondas": {"pt": "+ 81 ondas", "en": "+ 81 waves"},
    "c11.soma": {"pt": "soma", "en": "sum"},
    # token de formula — sem índice direto, em capitulo10.py:1255
    "c11.fracoes_continuas": {"pt": "(frações contínuas)", "en": "(continued fractions)"},

    # ------------------------------------------------------ v1 (video1.py)
    # token de VGroup — indexado em video1.py:477, 478, 479, 511, 513, 517
    "v1.contas_bancarias": {"pt": "contas bancárias", "en": "bank accounts"},
    # token de VGroup — indexado em video1.py:477, 478, 479, 511, 513, 517
    "v1.compras_online": {"pt": "compras online", "en": "online shopping"},
    # token de VGroup — indexado em video1.py:477, 478, 479, 511, 513, 517
    "v1.mensagens_privadas": {"pt": "mensagens privadas", "en": "private messages"},
    "v1.fatoracao": {"pt": "fatoração", "en": "factoring"},
    "v1.hoje": {"pt": "hoje", "en": "today"},
    "v1.resto": {"pt": "resto", "en": "remainder"},
}


def tx(chave):
    """O texto de tela `chave` no idioma ativo; sem tradução, o português."""
    entrada = TEXTOS[chave]
    texto = entrada.get(IDIOMA)
    return entrada["pt"] if texto is None else texto
