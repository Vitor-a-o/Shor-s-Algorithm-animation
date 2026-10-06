# -*- coding: utf-8 -*-
"""As âncoras do vídeo 1 DENTRO de cada fala: em que fração da locução cai
a palavra que dispara cada gesto. Elas dependem da ordem das palavras, então
mudam de um idioma para o outro — o resto do video1.py não muda.

Cada âncora é (tag, palavra-alvo em pt). A chave é a mesma nos dois
idiomas; em "en" o valor é a fração em que a palavra CORRESPONDENTE cai na
locução em inglês (roteiros/sincronias.md). Âncora que falta em
"en" usa a do pt, com um aviso por âncora.

Aqui só ficam os números: shor/sincronias.py junta esta tabela à dos
outros trechos e é dele o _f() que o video1.py usa.

Traduzir é trocar números aqui, nunca código no video1.py."""

SINC = {
    "pt": {
        # V1N00 — a abertura
        ("V1N00", "protege"): 0.185,           # o empurrão começa
        ("V1N00", "internet"): 0.546,          # fim da palavra: o escolhido para
        ("V1N00", "e ela não é"): 0.563,       # o envelope vira o campo
        ("V1N00", "senha forte"): 0.664,       # os pontos digitados
        ("V1N00", "que você possa"): 0.798,    # o risco vermelho
        ("V1N00", "escolher"): 0.924,          # o campo some
        # V1N01
        ("V1N01", "compras online"): 0.202,
        ("V1N01", "mensagens privadas"): 0.290,
        ("V1N01", "fáceis de fazer"): 0.611,   # a seta de ida
        ("V1N01", "impraticáveis"): 0.772,     # a seta de volta
        # V1N02
        ("V1N02", "multiplicar"): 0.195,       # o bloco se reabre
        ("V1N02", "voltar do produto"): 0.365,  # a volta se despedaça
        # o contador; hoje capado antes da palavra (o rabo do bloco não
        # caberia), então a fração só conta se cair ANTES do teto
        ("V1N02", "bilhões de anos"): 14.0 / 18.3,
        # V1N03
        ("V1N03", "RSA"): 0.219,               # cresce e grava as letras
        ("V1N03", "não é o único"): 0.683,     # a rede se desenha
        ("V1N03", "único a cair"): 0.879,      # todos pulsam
        # V1N04
        ("V1N04", "vence essa aposta"): 0.368,  # os "?" voltam nos primos
        ("V1N04", "não só a do RSA"): 0.461,   # os anônimos piscam
        ("V1N04", "últimos anos"): 0.605,      # a linha do tempo
        # a quebra; capada como o "bilhões" do V1N02
        ("V1N04", "prazo de validade"): 0.921,
        # V1N05
        ("V1N05", "esta série"): 0.750,        # os quatro vídeos saem do título
        # V1N06: com piso de 85% da fala no código (é o último gesto)
        ("V1N06", "neles eu passo"): 0.263,
        # V1N07 — o começo de cada trecho da decupagem do roteiro, em
        # segundos da estimativa de 20,3 s
        ("V1N07", "somar"): 5.6 / 20.3,
        ("V1N07", "multiplicar"): 7.2 / 20.3,
        ("V1N07", "potências"): 8.6 / 20.3,
        ("V1N07", "num mundo"): 10.1 / 20.3,
        ("V1N07", "dão a volta"): 11.6 / 20.3,
        ("V1N07", "só o que sobra"): 12.8 / 20.3,
        ("V1N07", "no fim"): 14.6 / 20.3,
        ("V1N07", "jeito de dividir"): 16.2 / 20.3,
        ("V1N07", "sem dividir"): 18.0 / 20.3,
        # V1N08
        ("V1N08", "teoremas"): 0.182,          # a elipse e a linha 1 (2,2 s)
        # V1N09
        ("V1N09", "RSA"): 0.236,               # "Euler" vira "RSA"
        # V1N10
        ("V1N10", "ordem modular"): 0.319,     # o zigue-zague
        ("V1N10", "com ela"): 0.473,           # as árvores
        ("V1N10", "divisores"): 0.764,         # a tabela volta
        ("V1N10", "procurar"): 0.870,          # o ciclo fecha
        # V1N11
        ("V1N11", "quântico"): 0.332,          # o ciclo sai
        ("V1N11", "lógica diferente"): 0.503,  # o circuito
        ("V1N11", "respostas erradas"): 0.674,  # as ondas
        ("V1N11", "se cancelam"): 0.737,
        ("V1N11", "se reforçam"): 0.817,
        ("V1N11", "algoritmo de Shor"): 0.866,  # a seta no pico
        ("V1N11", "Shor"): 0.950,              # a trilha acende
        # V1N12: com piso de 85% da fala no código (é o único gesto)
        ("V1N12", "resto"): 0.414,
    },
    "en": {},
}
