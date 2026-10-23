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
        ("V1N00", "protege"): 0.137,           # o empurrão começa
        ("V1N00", "internet"): 0.404,          # fim da palavra: o escolhido para
        ("V1N00", "e ela não é"): 0.416,       # o envelope vira o campo
        ("V1N00", "senha forte"): 0.516,       # os pontos digitados
        ("V1N00", "que você possa"): 0.590,    # o risco vermelho
        ("V1N00", "escolher"): 0.683,          # o campo some
        ("V1N00", "talvez"): 0.758,            # os qubits apagados derivam
        ("V1N00", "perdida"): 0.950,           # a fissura corre pelo arco
        # V1N01
        ("V1N01", "compras online"): 0.234,
        ("V1N01", "mensagens privadas"): 0.318,
        ("V1N01", "o que se aposta"): 0.428,   # a ficha salta para as setas
        ("V1N01", "fáceis de fazer"): 0.627,   # a seta de ida
        ("V1N01", "impraticáveis"): 0.781,     # a seta de volta
        ("V1N01", "até onde se sabe"): 0.915,  # o "?" vai para a fechadura
        # V1N02
        ("V1N02", "multiplicar"): 0.297,       # o bloco se reabre
        ("V1N02", "grandes"): 0.434,           # os primos crescem
        ("V1N02", "é fácil"): 0.480,           # a ida rápida, a parede
        ("V1N02", "voltar do produto"): 0.554,  # a volta se despedaça
        ("V1N02", "tempo razoável"): 0.914,    # a barra de progresso
        # V1N03
        ("V1N03", "computador comum"): 0.018,  # o chip cinza e as divisões
        # o contador; a fração só conta se cair ANTES do teto (o rabo do
        # bloco tem de caber antes de "teria acesso")
        ("V1N03", "bilhões de anos"): 0.168,
        ("V1N03", "teria acesso"): 0.737,      # o arco sobe e volta a travar
        ("V1N03", "tudo que essa aposta protege"): 0.826,  # os fantasmas
        # V1N04
        ("V1N04", "RSA"): 0.219,               # cresce e grava as letras
        ("V1N04", "peça por peça"): 0.429,     # a vista explodida
        ("V1N04", "do zero"): 0.625,           # as peças voltam, o arco trava
        ("V1N04", "não é o único"): 0.683,     # a rede se desenha
        ("V1N04", "único a cair"): 0.879,      # todos pulsam
        # V1N05: o 1994 entra no começo da fala, sem âncora
        ("V1N05", "Peter Shor"): 0.226,        # as interrogações voltam
        ("V1N05", "computador quântico"): 0.381,  # o chip passa a ciano
        ("V1N05", "fatorar esses números"): 0.625,  # os "?" voltam nos primos
        ("V1N05", "horas ou dias"): 0.774,     # o contador despenca
        # V1N06
        ("V1N06", "não serve só para o RSA"): 0.077,  # os anônimos piscam
        ("V1N06", "Era teoria"): 0.254,        # a folha sobre o 1994
        ("V1N06", "últimos anos"): 0.394,      # a linha do tempo
        ("V1N06", "saindo do papel"): 0.585,   # a folha some
        ("V1N06", "talvez"): 0.718,            # o tracejado rumo ao "?"
        # a quebra; capada como o "bilhões" do V1N03
        ("V1N06", "prazo de validade"): 0.873,
        # V1N07
        ("V1N07", "contas bancárias"): 0.070,  # as palavras saem do cadeado
        ("V1N07", "ficam abertas"): 0.414,     # os cadeados mini abrem
        ("V1N07", "quem tiver a máquina"): 0.535,  # os qubits de "hoje"
        ("V1N07", "gravado hoje"): 0.752,      # o envelope desliza
        ("V1N07", "aberto depois"): 0.911,     # a aba abre
        # V1N08: "Essa é a promessa" é o começo da fala, sem âncora
        ("V1N08", "algoritmo de Shor"): 0.350,  # "Shor" pisca em ciano
        ("V1N08", "esta série"): 0.750,        # os quatro vídeos saem do título
        # V1N09: com piso de 85% da fala no código (é o último gesto)
        ("V1N09", "neles eu passo"): 0.263,
        # V1N10 — o começo de cada trecho da decupagem do roteiro, em
        # segundos da estimativa de 20,3 s
        ("V1N10", "somar"): 5.6 / 20.3,
        ("V1N10", "multiplicar"): 7.2 / 20.3,
        ("V1N10", "potências"): 8.6 / 20.3,
        ("V1N10", "num mundo"): 10.1 / 20.3,
        ("V1N10", "dão a volta"): 11.6 / 20.3,
        ("V1N10", "só o que sobra"): 12.8 / 20.3,
        ("V1N10", "no fim"): 14.6 / 20.3,
        ("V1N10", "jeito de dividir"): 16.2 / 20.3,
        ("V1N10", "sem dividir"): 18.0 / 20.3,
        # V1N11
        ("V1N11", "teoremas"): 0.182,          # a elipse e a linha 1 (2,2 s)
        # V1N12
        ("V1N12", "RSA"): 0.236,               # "Euler" vira "RSA"
        # V1N13
        ("V1N13", "ordem modular"): 0.525,     # o arco fecha o ciclo, o flash
        ("V1N13", "Depois"): 0.593,            # a tabela sai, as árvores
        ("V1N13", "quebrar"): 0.864,           # o cadeado RSA volta e racha
        # V1N14
        ("V1N14", "computador quântico"): 0.089,  # o que o V1N13 deixou sai
        ("V1N14", "lógica incomum"): 0.177,    # o circuito
        ("V1N14", "superposição"): 0.304,      # os qubits
        ("V1N14", "emaranhamento"): 0.509,     # o par colapsa
        ("V1N14", "interferência"): 0.693,     # as ondas se somam na curva
        ("V1N14", "apaga"): 0.741,             # os vales achatam
        ("V1N14", "até sobrar"): 0.833,        # os picos crescem
        ("V1N14", "algoritmo de Shor"): 0.939,  # a seta no pico
    },
    "en": {},
}
