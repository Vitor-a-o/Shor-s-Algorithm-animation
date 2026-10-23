# Sincronias por ordem de palavra

As âncoras abaixo marcam **onde, dentro de uma fala, cai a palavra que
dispara um gesto**. A tabela `SINC` é a de `shor/sincronias.py`: as do
vídeo 1 moram em `shor/videos/sincronias_v1.py` e entram nela inteiras; as
do `C11N10` e do encerramento do vídeo 4 estão no próprio
`shor/sincronias.py`. Em inglês a ordem das palavras muda, então cada
fração precisa ser medida de novo no áudio em inglês.

**Como preencher o inglês:** para cada linha, escolha na fala em inglês a
palavra que corresponde à palavra-alvo em pt. Depois da gravação, meça em
que fração da locução ela cai e escreva em `SINC["en"]` (no
`sincronias_v1.py` para as do vídeo 1, no `sincronias.py` para as outras)
com **a mesma chave** (tag, âncora em pt), por exemplo
`("V1N04", "RSA"): 0.31`. Âncora que faltar em `"en"` usa a fração do pt, e
o render avisa uma vez por âncora (`sincronia V1N04 "RSA": sem fração em en…`).
Traduzir é só trocar números: o `video1.py`, o `video4.py` e o
`capitulo10.py` não mudam.

As frações do pt foram estimadas pela contagem de caracteres da fala, menos
as do V1N10, que são o começo de cada trecho da decupagem do roteiro, em
segundos dos 20,3 s estimados.

## Âncoras do vídeo 1 (68)

As 19 linhas com "estimativa por caracteres, a medir na gravação" são as âncoras do
redesenho do V1N00 ao V1N08 (seção "Fios do redesenho" do roteiro do vídeo 1). O
`video1.py` já usa todas (sessões 2 a 7 do redesenho, conferidas na sessão 8); a lista do
que falta medir no áudio está logo abaixo da tabela. As outras linhas descrevem o gesto que
o código faz hoje.

| tag | âncora | palavra-alvo em pt | fração pt | fala pt completa |
|---|---|---|---|---|
| V1N00 | `protege` | "protege quase tudo" [começa o empurrão] | 0,137 | Existe uma aposta que protege quase tudo que você faz na internet, e ela não é uma senha forte que você possa escolher. E talvez ela esteja perto de ser perdida. |
| V1N00 | `internet` | fim de "internet" [o pacote para] | 0,404 | Existe uma aposta que protege quase tudo que você faz na internet, e ela não é uma senha forte que você possa escolher. E talvez ela esteja perto de ser perdida. |
| V1N00 | `e ela não é` | "e ela não é" [o envelope vira o campo de senha] | 0,416 | Existe uma aposta que protege quase tudo que você faz na internet, e ela não é uma senha forte que você possa escolher. E talvez ela esteja perto de ser perdida. |
| V1N00 | `senha forte` | "uma senha forte" [os pontos digitados] | 0,516 | Existe uma aposta que protege quase tudo que você faz na internet, e ela não é uma senha forte que você possa escolher. E talvez ela esteja perto de ser perdida. |
| V1N00 | `que você possa` | "que você possa" [o risco vermelho] | 0,590 | Existe uma aposta que protege quase tudo que você faz na internet, e ela não é uma senha forte que você possa escolher. E talvez ela esteja perto de ser perdida. |
| V1N00 | `escolher` | "escolher" [o campo some] | 0,683 | Existe uma aposta que protege quase tudo que você faz na internet, e ela não é uma senha forte que você possa escolher. E talvez ela esteja perto de ser perdida. |
| V1N00 | `talvez` | "E talvez ela esteja" [os qubits apagados piscam nas bordas e derivam] | 0,758 (estimativa por caracteres, a medir na gravação) | Existe uma aposta que protege quase tudo que você faz na internet, e ela não é uma senha forte que você possa escolher. E talvez ela esteja perto de ser perdida. |
| V1N00 | `perdida` | "perto de ser perdida" [a fissura corre pelo arco e some] | 0,950 | Existe uma aposta que protege quase tudo que você faz na internet, e ela não é uma senha forte que você possa escolher. E talvez ela esteja perto de ser perdida. |
| V1N01 | `compras online` | "compras online" [2º item] | 0,234 | Essa aposta está por trás de contas bancárias, compras online e mensagens privadas. E o que se aposta é que existem operações fáceis de fazer numa direção e impraticáveis de desfazer, até onde se sabe. |
| V1N01 | `mensagens privadas` | "mensagens privadas" [3º item] | 0,318 | Essa aposta está por trás de contas bancárias, compras online e mensagens privadas. E o que se aposta é que existem operações fáceis de fazer numa direção e impraticáveis de desfazer, até onde se sabe. |
| V1N01 | `o que se aposta` | "o que se aposta" [a ficha salta em arco até a faixa das setas] | 0,428 (estimativa por caracteres, a medir na gravação) | Essa aposta está por trás de contas bancárias, compras online e mensagens privadas. E o que se aposta é que existem operações fáceis de fazer numa direção e impraticáveis de desfazer, até onde se sabe. |
| V1N01 | `fáceis de fazer` | "fáceis de fazer numa direção" [seta de ida] | 0,627 | Essa aposta está por trás de contas bancárias, compras online e mensagens privadas. E o que se aposta é que existem operações fáceis de fazer numa direção e impraticáveis de desfazer, até onde se sabe. |
| V1N01 | `impraticáveis` | "impraticáveis de desfazer" [seta de volta] | 0,781 | Essa aposta está por trás de contas bancárias, compras online e mensagens privadas. E o que se aposta é que existem operações fáceis de fazer numa direção e impraticáveis de desfazer, até onde se sabe. |
| V1N01 | `até onde se sabe` | "até onde se sabe" [uma interrogação vai para a fechadura e pisca] | 0,915 (estimativa por caracteres, a medir na gravação) | Essa aposta está por trás de contas bancárias, compras online e mensagens privadas. E o que se aposta é que existem operações fáceis de fazer numa direção e impraticáveis de desfazer, até onde se sabe. |
| V1N02 | `multiplicar` | "Multiplicar dois primos grandes" [o bloco reabre] | 0,297 | A operação mais conhecida desse tipo é a fatoração. Multiplicar dois primos grandes é fácil, mas voltar do produto para os primos é o que ninguém sabe fazer em tempo razoável. |
| V1N02 | `grandes` | "primos grandes" [os dois primos crescem em dígitos] | 0,434 (estimativa por caracteres, a medir na gravação) | A operação mais conhecida desse tipo é a fatoração. Multiplicar dois primos grandes é fácil, mas voltar do produto para os primos é o que ninguém sabe fazer em tempo razoável. |
| V1N02 | `é fácil` | "é fácil" [a ida rápida; a parede de dígitos] | 0,480 (estimativa por caracteres, a medir na gravação) | A operação mais conhecida desse tipo é a fatoração. Multiplicar dois primos grandes é fácil, mas voltar do produto para os primos é o que ninguém sabe fazer em tempo razoável. |
| V1N02 | `voltar do produto` | "voltar do produto para os primos" [a volta se despedaça] | 0,554 | A operação mais conhecida desse tipo é a fatoração. Multiplicar dois primos grandes é fácil, mas voltar do produto para os primos é o que ninguém sabe fazer em tempo razoável. |
| V1N02 | `tempo razoável` | "em tempo razoável" [a barra de progresso quase não enche] | 0,914 (estimativa por caracteres, a medir na gravação) | A operação mais conhecida desse tipo é a fatoração. Multiplicar dois primos grandes é fácil, mas voltar do produto para os primos é o que ninguém sabe fazer em tempo razoável. |
| V1N03 | `computador comum` | "Um computador comum" [o chip cinza e a fila de divisões riscadas] | 0,018 (estimativa por caracteres, a medir na gravação) | Um computador comum levaria bilhões de anos para fatorar os números utilizados atualmente. Quem conseguisse fatorar rápido teria acesso a tudo que essa aposta protege. |
| V1N03 | `bilhões de anos` | "bilhões de anos" [o contador; teto em 5,6 s antes de "teria acesso", que hoje não morde] | 0,168 | Um computador comum levaria bilhões de anos para fatorar os números utilizados atualmente. Quem conseguisse fatorar rápido teria acesso a tudo que essa aposta protege. |
| V1N03 | `teria acesso` | "teria acesso a tudo" [o arco sobe e volta a travar] | 0,737 | Um computador comum levaria bilhões de anos para fatorar os números utilizados atualmente. Quem conseguisse fatorar rápido teria acesso a tudo que essa aposta protege. |
| V1N03 | `tudo que essa aposta protege` | "tudo que essa aposta protege" [fantasmas das três palavras pela fresta] | 0,826 (estimativa por caracteres, a medir na gravação) | Um computador comum levaria bilhões de anos para fatorar os números utilizados atualmente. Quem conseguisse fatorar rápido teria acesso a tudo que essa aposta protege. |
| V1N04 | `RSA` | "é o RSA" [cresce e grava as letras] | 0,219 | O algoritmo que se apoia justamente na fatoração é o RSA, e é ele que esta série vai desmontar, peça por peça. É o mais direto de construir do zero, mas não é o único que vive de uma aposta assim, nem vai ser o único a cair. |
| V1N04 | `peça por peça` | "peça por peça" [a vista explodida e os quatro rótulos] | 0,429 (estimativa por caracteres, a medir na gravação) | O algoritmo que se apoia justamente na fatoração é o RSA, e é ele que esta série vai desmontar, peça por peça. É o mais direto de construir do zero, mas não é o único que vive de uma aposta assim, nem vai ser o único a cair. |
| V1N04 | `do zero` | "do zero" [as peças voltam, o arco trava, os rótulos somem] | 0,625 (estimativa por caracteres, a medir na gravação) | O algoritmo que se apoia justamente na fatoração é o RSA, e é ele que esta série vai desmontar, peça por peça. É o mais direto de construir do zero, mas não é o único que vive de uma aposta assim, nem vai ser o único a cair. |
| V1N04 | `não é o único` | "não é o único" [a rede se desenha] | 0,683 | O algoritmo que se apoia justamente na fatoração é o RSA, e é ele que esta série vai desmontar, peça por peça. É o mais direto de construir do zero, mas não é o único que vive de uma aposta assim, nem vai ser o único a cair. |
| V1N04 | `único a cair` | "nem vai ser o único a cair" [todos pulsam] | 0,879 | O algoritmo que se apoia justamente na fatoração é o RSA, e é ele que esta série vai desmontar, peça por peça. É o mais direto de construir do zero, mas não é o único que vive de uma aposta assim, nem vai ser o único a cair. |
| V1N05 | `Peter Shor` | "Peter Shor" [as interrogações voltam onde pararam] | 0,226 (estimativa por caracteres, a medir na gravação) | Em mil novecentos e noventa e quatro, Peter Shor mostrou que um computador quântico consegue fazer isso: fatorar esses números em horas ou dias, não em bilhões de anos. |
| V1N05 | `computador quântico` | "um computador quântico" [o chip volta e passa de cinza a ciano] | 0,381 (estimativa por caracteres, a medir na gravação) | Em mil novecentos e noventa e quatro, Peter Shor mostrou que um computador quântico consegue fazer isso: fatorar esses números em horas ou dias, não em bilhões de anos. |
| V1N05 | `fatorar esses números` | "fatorar esses números" [os "?", de volta desde o começo da fala, se desfazem nos primos] | 0,625 | Em mil novecentos e noventa e quatro, Peter Shor mostrou que um computador quântico consegue fazer isso: fatorar esses números em horas ou dias, não em bilhões de anos. |
| V1N05 | `horas ou dias` | "em horas ou dias" [o contador volta cheio e despenca até "horas"] | 0,774 (estimativa por caracteres, a medir na gravação) | Em mil novecentos e noventa e quatro, Peter Shor mostrou que um computador quântico consegue fazer isso: fatorar esses números em horas ou dias, não em bilhões de anos. |
| V1N06 | `não serve só para o RSA` | "não serve só para o RSA" [os anônimos piscam] | 0,077 | E o truque não serve só para o RSA. Era teoria, mas nos últimos anos a máquina vem saindo do papel, e talvez a aposta tenha prazo de validade. |
| V1N06 | `Era teoria` | "Era teoria" [a folha de papel sobre o ponto 1994] | 0,254 (estimativa por caracteres, a medir na gravação) | E o truque não serve só para o RSA. Era teoria, mas nos últimos anos a máquina vem saindo do papel, e talvez a aposta tenha prazo de validade. |
| V1N06 | `últimos anos` | "nos últimos anos" [a linha do tempo] | 0,394 | E o truque não serve só para o RSA. Era teoria, mas nos últimos anos a máquina vem saindo do papel, e talvez a aposta tenha prazo de validade. |
| V1N06 | `saindo do papel` | "saindo do papel" [a folha encolhe e some atrás do 1994] | 0,585 (estimativa por caracteres, a medir na gravação) | E o truque não serve só para o RSA. Era teoria, mas nos últimos anos a máquina vem saindo do papel, e talvez a aposta tenha prazo de validade. |
| V1N06 | `talvez` | "e talvez a aposta" [a linha segue tracejada rumo ao "?"] | 0,718 (estimativa por caracteres, a medir na gravação) | E o truque não serve só para o RSA. Era teoria, mas nos últimos anos a máquina vem saindo do papel, e talvez a aposta tenha prazo de validade. |
| V1N06 | `prazo de validade` | "prazo de validade" [a quebra; hoje capada em 3,29 s antes do fim] | 0,873 | E o truque não serve só para o RSA. Era teoria, mas nos últimos anos a máquina vem saindo do papel, e talvez a aposta tenha prazo de validade. |
| V1N07 | `contas bancárias` | "contas bancárias" [as três palavras saem do cadeado quebrado] | 0,070 | Nesse dia, contas bancárias, compras online e mensagens privadas ficam abertas para quem tiver a máquina. E o que for gravado hoje já pode ser aberto depois. |
| V1N07 | `ficam abertas` | "ficam abertas" [os três cadeados mini abrem em cascata] | 0,414 (estimativa por caracteres, a medir na gravação) | Nesse dia, contas bancárias, compras online e mensagens privadas ficam abertas para quem tiver a máquina. E o que for gravado hoje já pode ser aberto depois. |
| V1N07 | `quem tiver a máquina` | "quem tiver a máquina" [os qubits de "hoje" acendem e ligam as palavras] | 0,535 (estimativa por caracteres, a medir na gravação) | Nesse dia, contas bancárias, compras online e mensagens privadas ficam abertas para quem tiver a máquina. E o que for gravado hoje já pode ser aberto depois. |
| V1N07 | `gravado hoje` | "gravado hoje" [o envelope fechado desliza] | 0,752 | Nesse dia, contas bancárias, compras online e mensagens privadas ficam abertas para quem tiver a máquina. E o que for gravado hoje já pode ser aberto depois. |
| V1N07 | `aberto depois` | "aberto depois" [a aba do envelope abre] | 0,911 | Nesse dia, contas bancárias, compras online e mensagens privadas ficam abertas para quem tiver a máquina. E o que for gravado hoje já pode ser aberto depois. |
| V1N08 | `algoritmo de Shor` | "do algoritmo de Shor" ["Shor" pisca em ciano no título] | 0,350 (estimativa por caracteres, a medir na gravação) | Essa é a promessa, ou a ameaça, do algoritmo de Shor. E é exatamente o que esta série vai construir. |
| V1N08 | `esta série` | "esta série" [os quatro vídeos saem do título] | 0,750 | Essa é a promessa, ou a ameaça, do algoritmo de Shor. E é exatamente o que esta série vai construir. |
| V1N09 | `neles eu passo` | "neles eu passo por cada peça" [o 1 acende; piso de 85% da fala] | 0,263 | São quatro vídeos no total, e neles eu passo por cada peça necessária para entender como se chega nesse algoritmo. |
| V1N10 | `somar` | "É somar" — trecho 2 da decupagem (cap. 2, parcelas 6 + 5) | 0,276 (5,6 s / 20,3) | No vídeo dois vou mostrar a aritmética modular, que é a base matemática de toda a série. É somar, multiplicar e elevar a potências num mundo onde os números dão a volta, e só o que sobra importa. No fim aparece até um jeito de dividir, sem dividir de verdade. |
| V1N10 | `multiplicar` | "multiplicar" — trecho 3 (cap. 3, os cinco 4) | 0,355 (7,2 s / 20,3) | No vídeo dois vou mostrar a aritmética modular, que é a base matemática de toda a série. É somar, multiplicar e elevar a potências num mundo onde os números dão a volta, e só o que sobra importa. No fim aparece até um jeito de dividir, sem dividir de verdade. |
| V1N10 | `potências` | "elevar a potências" — trecho 4 (cap. 4, a corrente de 3) | 0,424 (8,6 s / 20,3) | No vídeo dois vou mostrar a aritmética modular, que é a base matemática de toda a série. É somar, multiplicar e elevar a potências num mundo onde os números dão a volta, e só o que sobra importa. No fim aparece até um jeito de dividir, sem dividir de verdade. |
| V1N10 | `num mundo` | "num mundo onde os números" — trecho 5 (cap. 2, o n laranja cresce) | 0,498 (10,1 s / 20,3) | No vídeo dois vou mostrar a aritmética modular, que é a base matemática de toda a série. É somar, multiplicar e elevar a potências num mundo onde os números dão a volta, e só o que sobra importa. No fim aparece até um jeito de dividir, sem dividir de verdade. |
| V1N10 | `dão a volta` | "dão a volta" — trecho 6 (cap. 2, os estados n = 8…11) | 0,571 (11,6 s / 20,3) | No vídeo dois vou mostrar a aritmética modular, que é a base matemática de toda a série. É somar, multiplicar e elevar a potências num mundo onde os números dão a volta, e só o que sobra importa. No fim aparece até um jeito de dividir, sem dividir de verdade. |
| V1N10 | `só o que sobra` | "só o que sobra importa" — trecho 7 (cap. 1, sobra o 2 verde) | 0,631 (12,8 s / 20,3) | No vídeo dois vou mostrar a aritmética modular, que é a base matemática de toda a série. É somar, multiplicar e elevar a potências num mundo onde os números dão a volta, e só o que sobra importa. No fim aparece até um jeito de dividir, sem dividir de verdade. |
| V1N10 | `no fim` | "No fim aparece" — trecho 8 (cap. 5, a fila 2·5 passa com ✓) | 0,719 (14,6 s / 20,3) | No vídeo dois vou mostrar a aritmética modular, que é a base matemática de toda a série. É somar, multiplicar e elevar a potências num mundo onde os números dão a volta, e só o que sobra importa. No fim aparece até um jeito de dividir, sem dividir de verdade. |
| V1N10 | `jeito de dividir` | "um jeito de dividir" — trecho 9 (cap. 5, seis filas com ✗) | 0,798 (16,2 s / 20,3) | No vídeo dois vou mostrar a aritmética modular, que é a base matemática de toda a série. É somar, multiplicar e elevar a potências num mundo onde os números dão a volta, e só o que sobra importa. No fim aparece até um jeito de dividir, sem dividir de verdade. |
| V1N10 | `sem dividir` | "sem dividir de verdade" — trecho 10 (tabela mod 9, ÷ riscado → a⁻¹) | 0,887 (18,0 s / 20,3) | No vídeo dois vou mostrar a aritmética modular, que é a base matemática de toda a série. É somar, multiplicar e elevar a potências num mundo onde os números dão a volta, e só o que sobra importa. No fim aparece até um jeito de dividir, sem dividir de verdade. |
| V1N11 | `teoremas` | "teoremas" [a elipse e a linha 1; 2,2 s da decupagem] | 0,182 | O vídeo três começa pelos teoremas, e é onde entram Fermat e Euler, dois nomes que parecem abstratos até você ver que é neles que o RSA se apoia. |
| V1N12 | `RSA` | "RSA" ["Euler" vira "RSA" no rótulo] | 0,236 | Enfim, ainda no vídeo três, explico o RSA, com duas chaves, uma pública e uma privada, nascendo de um par de números primos. E quebrar isso é, no fundo, fatorar. |
| V1N13 | `ordem modular` | "a ordem modular" [o último arco fecha o ciclo] | 0,525 | No quarto e último vídeo, demonstro como os conceitos básicos e os teoremas nos levam até uma última propriedade, a ordem modular. Depois, mostro como descobri-la é essencialmente fatorar, e quebrar a criptografia do RSA. |
| V1N13 | `Depois` | "Depois" [a tabela sai, entram as árvores] | 0,593 | No quarto e último vídeo, demonstro como os conceitos básicos e os teoremas nos levam até uma última propriedade, a ordem modular. Depois, mostro como descobri-la é essencialmente fatorar, e quebrar a criptografia do RSA. |
| V1N13 | `quebrar` | "quebrar" [o cadeado RSA reaparece e racha] | 0,864 | No quarto e último vídeo, demonstro como os conceitos básicos e os teoremas nos levam até uma última propriedade, a ordem modular. Depois, mostro como descobri-la é essencialmente fatorar, e quebrar a criptografia do RSA. |
| V1N14 | `computador quântico` | "computador quântico" [o que sobrou do V1N13 sai] | 0,089 | Por último, mostro como o computador quântico usa a lógica incomum da física quântica. A superposição põe todos os valores em jogo ao mesmo tempo, o emaranhamento amarra cada valor ao seu resultado, e a interferência apaga as respostas erradas até sobrar a ordem. E esse é o algoritmo de Shor. |
| V1N14 | `lógica incomum` | "lógica incomum" [o circuito se monta] | 0,177 | Por último, mostro como o computador quântico usa a lógica incomum da física quântica. A superposição põe todos os valores em jogo ao mesmo tempo, o emaranhamento amarra cada valor ao seu resultado, e a interferência apaga as respostas erradas até sobrar a ordem. E esse é o algoritmo de Shor. |
| V1N14 | `superposição` | "superposição" [os cartões-qubit] | 0,304 | Por último, mostro como o computador quântico usa a lógica incomum da física quântica. A superposição põe todos os valores em jogo ao mesmo tempo, o emaranhamento amarra cada valor ao seu resultado, e a interferência apaga as respostas erradas até sobrar a ordem. E esse é o algoritmo de Shor. |
| V1N14 | `emaranhamento` | "emaranhamento" [o par colapsando] | 0,509 | Por último, mostro como o computador quântico usa a lógica incomum da física quântica. A superposição põe todos os valores em jogo ao mesmo tempo, o emaranhamento amarra cada valor ao seu resultado, e a interferência apaga as respostas erradas até sobrar a ordem. E esse é o algoritmo de Shor. |
| V1N14 | `interferência` | "interferência" [as ondas se somam na curva] | 0,693 | Por último, mostro como o computador quântico usa a lógica incomum da física quântica. A superposição põe todos os valores em jogo ao mesmo tempo, o emaranhamento amarra cada valor ao seu resultado, e a interferência apaga as respostas erradas até sobrar a ordem. E esse é o algoritmo de Shor. |
| V1N14 | `apaga` | "apaga as respostas erradas" [os vales achatam] | 0,741 | Por último, mostro como o computador quântico usa a lógica incomum da física quântica. A superposição põe todos os valores em jogo ao mesmo tempo, o emaranhamento amarra cada valor ao seu resultado, e a interferência apaga as respostas erradas até sobrar a ordem. E esse é o algoritmo de Shor. |
| V1N14 | `até sobrar` | "até sobrar a ordem" [os picos crescem] | 0,833 | Por último, mostro como o computador quântico usa a lógica incomum da física quântica. A superposição põe todos os valores em jogo ao mesmo tempo, o emaranhamento amarra cada valor ao seu resultado, e a interferência apaga as respostas erradas até sobrar a ordem. E esse é o algoritmo de Shor. |
| V1N14 | `algoritmo de Shor` | "E esse é o algoritmo de Shor" [a seta no pico] | 0,939 | Por último, mostro como o computador quântico usa a lógica incomum da física quântica. A superposição põe todos os valores em jogo ao mesmo tempo, o emaranhamento amarra cada valor ao seu resultado, e a interferência apaga as respostas erradas até sobrar a ordem. E esse é o algoritmo de Shor. |

### Âncoras novas do redesenho a medir no áudio (19)

As 19 âncoras do redesenho, com a fração do pt ainda estimada por caracteres. Medir cada
palavra-alvo na locução (início da palavra, em fração da duração do `.wav`) e trocar o
número: o pt em `SINC["pt"]`, o inglês em `SINC["en"]`, os dois em
`shor/videos/sincronias_v1.py`, com a mesma chave. Depois de medir, tirar o "(estimativa
por caracteres…)" da linha na tabela acima.

- **pt:** cinco já podem ser medidas, porque a fala tem `.wav` (V1N01, V1N04, V1N08). As
  outras 14 esperam a gravação de V1N00, V1N02, V1N03, V1N05, V1N06 e V1N07.
- **en:** as 19 já podem ser medidas — as dez primeiras falas estão gravadas em
  `audio/en/` e medidas em `duracoes_en.py`. A tabela `SINC["en"]` do vídeo 1 está
  inteira vazia, então as outras 49 âncoras do vídeo 1 também caem no pt, com aviso, e
  entram na mesma rodada de medição (palavras-alvo em inglês em
  `roteiros/en/roteiro_video1_introducao.md`, seção "Âncoras de sincronia em inglês").

| tag | âncora | gesto | palavra-alvo em pt | palavra-alvo em inglês | pt: dá para medir já? |
|---|---|---|---|---|---|
| V1N00 | `talvez` | os qubits apagados piscam nas bordas e derivam | "E talvez ela esteja" | "may" (em "it may be close") | não — falta gravar |
| V1N01 | `o que se aposta` | a ficha salta para a faixa das setas | "o que se aposta" | "the bet is" | sim |
| V1N01 | `até onde se sabe` | um "?" vai para a fechadura e pisca | "até onde se sabe" | "as far as anyone knows" | sim |
| V1N02 | `grandes` | os primos crescem em dígitos | "primos grandes" | "large" | não — falta gravar |
| V1N02 | `é fácil` | a ida rápida, a parede de dígitos | "é fácil" | "is easy" | não — falta gravar |
| V1N02 | `tempo razoável` | a barra de progresso | "em tempo razoável" | "a reasonable time" | não — falta gravar |
| V1N03 | `computador comum` | o chip cinza e a fila de divisões | "Um computador comum" | "An ordinary computer" | não — falta gravar |
| V1N03 | `tudo que essa aposta protege` | os fantasmas pela fresta | "tudo que essa aposta protege" | "everything this bet protects" | não — falta gravar |
| V1N04 | `peça por peça` | a vista explodida e os quatro rótulos | "peça por peça" | "piece by piece" | sim |
| V1N04 | `do zero` | as peças voltam, o arco trava | "do zero" | "from zero" | sim |
| V1N05 | `Peter Shor` | as interrogações voltam | "Peter Shor" | "Peter Shor" | não — falta gravar |
| V1N05 | `computador quântico` | o chip volta e passa a ciano | "um computador quântico" | "a quantum computer" | não — falta gravar |
| V1N05 | `horas ou dias` | o contador despenca até "horas" | "em horas ou dias" | "hours or days" | não — falta gravar |
| V1N06 | `Era teoria` | a folha sobre o ponto 1994 | "Era teoria" | "It was only theory" | não — falta gravar |
| V1N06 | `saindo do papel` | a folha encolhe e some | "saindo do papel" | "come off the drawing board" | não — falta gravar |
| V1N06 | `talvez` | o tracejado rumo ao "?" | "e talvez a aposta" | "may" (em "the bet may have") | não — falta gravar |
| V1N07 | `ficam abertas` | os cadeados mini abrem | "ficam abertas" | "are open" | não — falta gravar |
| V1N07 | `quem tiver a máquina` | os qubits de "hoje" ligam as palavras | "quem tiver a máquina" | "whoever has the machine" | não — falta gravar |
| V1N08 | `algoritmo de Shor` | "Shor" pisca em ciano | "do algoritmo de Shor" | "Shor's algorithm" | sim |

Depois de medir, rodar a conferência de novo nos dois idiomas (quadros por âncora e folga
de cada `narra()`): os tetos do V1N03 ("bilhões de anos"), do V1N04 ("do zero"), do V1N06
("prazo de validade") e do V1N07 ("gravado hoje", "aberto depois") dependem das frações
medidas.

### O que a tabela não cobre

- **Tetos e pisos, que não dependem do idioma.** No V1N03 ("bilhões") e no
  V1N06 ("prazo de validade") a palavra só vale se cair antes do teto, que
  é o último instante em que o resto do bloco ainda cabe — antes de "teria
  acesso" no V1N03 (5,6 s antes dela), antes do fim da fala no V1N06 (3,29 s
  antes). Hoje, em pt, o teto só vale no V1N06; no V1N03 a palavra cai
  antes dele, mas só por 0,3 s. No V1N09
  o gesto nunca começa antes de 85% da fala menos a duração dele. Esses
  números ficam no código.
- **Gestos que caem numa palavra só pela soma dos `run_time` anteriores**,
  sem âncora própria. Em inglês eles acompanham a âncora anterior, ou o
  começo da fala, e não a palavra:
  - V1N01: "contas bancárias", ao fim do cadeado que desce e abre (2,0 s × k);
  - V1N02: "fatoração", imediata, de propósito ("logo nos primeiros segundos");
  - V1N05: as interrogações voltam no começo da fala ("Em mil novecentos e
    noventa e quatro"), paradas, para o quadro não ficar parado até `fatorar
    esses números`;
  - V1N08: "Essa é a promessa", o começo da fala — os cacos reacendem e sobem;
  - V1N09: "São quatro vídeos", no começo da fala;
  - V1N11: "Fermat" → "Euler" (5,4 s) e o resto da decupagem, em sequência
    depois de `teoremas`;
  - V1N12: o resto da decupagem, em sequência depois de `RSA`;

  No redesenho do V1N00 ao V1N08 (sessões 2 a 7), entram na lista:
  - V1N01: a ficha rola e para ao pé do cadeado em "Essa aposta", no mesmo
    movimento do cadeado que desce;
  - V1N02: a ficha volta ao pé do cadeado junto com "fatoração";
  - V1N05: o ponto e o rótulo "1994" aparecem no começo da fala ("Em mil
    novecentos e noventa e quatro"); as interrogações deixam o começo e
    passam a voltar na âncora `Peter Shor`;
  - V1N06: o chip ciano e o "horas" do V1N05 saem no começo da fala.

## Âncoras do C11N10 e do encerramento do vídeo 4 (8)

Antes eram `Wait` em segundos fixos dentro de `Succession`. Agora o `Wait`
é `_ate()` (`shor/sincronias.py`): o instante da âncora (fração × duração
da fala) menos o tempo já corrido desde o começo do `narra`, nunca
negativo. A fração pt é o instante que o comentário do código dava,
dividido pelo `est=` da tag; com o `est=`, o gesto cai exatamente onde o
`Wait` fixo o punha. A palavra em inglês é a da tabela "Ordem das palavras
que a animação exige" de `roteiros/en/roteiro_video4_algoritmo_de_shor.md`.

| tag | âncora | palavra-alvo em pt | palavra em inglês | fração pt | `Wait` que substituiu |
|---|---|---|---|---|---|
| C11N10 | `outro exemplo` | "Agora vamos a outro exemplo" [o `Write` da congruência com o 21] | "another example" | 0,280 (4,2 s / 15,0) | `Wait(4.2)`, no começo do play |
| V4N01 | `vencer a aposta` | "consegue vencer a aposta" [a fissura chega às pontas, o arco estala] | "win the bet" | 0,521 (6,2 s / 11,9) | `Wait(4.8)`, depois da descida de 1,4 s |
| V4N03 | `a aposta continua de pé` | "a aposta continua de pé" [a rede volta ao fundo] | "the bet still stands" | 0,228 (3,7 s / 16,2) | `Wait(3.7)` |
| V4N03 | `prazo de validade` | "ela só ganhou um prazo de validade" [os cacos reacendem e sobem] | "expiration date" | 0,364 (5,9 s / 16,2) | `Wait(1.0)`, depois de 3,7 + 1,2 s |
| V4N03 | `a resposta já está` | "E a resposta já está sendo preparada" [os cacos viram a armação nova] | "the answer is already being prepared" | 0,556 (9,0 s / 16,2) | `Wait(0.5)`, depois de 4,9 + 1,0 + 2,6 s |
| V4N03 | `não depende de fatorar` | "uma criptografia que não depende de fatorar" [a armação fecha] | "cryptography that doesn't depend on factoring" | 0,759 (12,3 s / 16,2) | `Wait(0.9)`, depois de 9,0 + 2,4 s |
| V4N04 | `o caminho foi seu` | "O caminho foi seu" [a trilha pulsa] | "The path was yours" | 0,639 (11,7 s / 18,3) | `Wait(8.5)`, depois de 0,8 + 2,4 s |
| V4N04 | `obrigado` | "Obrigado por ter vindo até o fim" [o título pousa] | "Thanks for coming all the way to the end" | 0,847 (15,5 s / 18,3) | `Wait(2.6)`, depois de 3,2 + 8,5 + 1,2 s |

Falas pt completas:

- **C11N10:** De física é só isso, e mais nada. Agora vamos a outro exemplo, com um n que caiba no registrador, e a conta que o circuito faz é a exponenciação modular do capítulo quatro.
- **V4N01:** Era essa a promessa do primeiro vídeo: um computador quântico consegue vencer a aposta que protege a internet. E agora a gente sabe como.
- **V4N03:** Então, por enquanto, pode ficar tranquilo: a aposta continua de pé, ela só ganhou um prazo de validade. E a resposta já está sendo preparada: uma criptografia que não depende de fatorar.
- **V4N04:** Quatro vídeos atrás, a gente começou com o resto de uma divisão. Hoje você entende o algoritmo que pode mudar a segurança da internet. O caminho foi seu, eu só mostrei as peças. Obrigado por ter vindo até o fim.

Gestos dessas falas **sem âncora própria**, que em inglês acompanham a
âncora anterior ou o começo da fala: no V4N01, "E agora a gente sabe como"
cai sobre o cadeado já quebrado, sem animação; no V4N04, a saída da cena e
a trilha ("Quatro vídeos atrás") abrem a fala.

## Outras sincronias por ordem de palavra

Fora do vídeo 1, nos capítulos. São comentários que amarram a animação à
ordem das palavras dentro de uma fala. **Nada disso usa fração:** a ordem
está nos próprios `play` em sequência (o único `Wait` em segundos, o do
`C11N10`, virou âncora — tabela acima). Nenhum código mudou. Os comentários estão aqui para conferir quando a fala em inglês for
gravada.

| arquivo:linha | tag | trecho do comentário |
|---|---|---|
| shor/capitulos/capitulo8.py:579 | C8N20 em diante (fase A2) | "a metamorfose acontece no play em que a fala nomeia a peça, depois de ela já ter feito o serviço" |
| shor/capitulos/capitulo8.py:729 | C8N29 | "a fala tem ordem — "uma leva cada expoente, e as duas levam o mesmo módulo" — então os dois cartões nascem um de cada vez" |
| shor/capitulos/capitulo8.py:764 | C8N31 | "a fala termina em "menor que o módulo": o < e o 33 chegam por último" |
| shor/capitulos/capitulo8.py:979 | C8N40 | "o n − 1 chega por último, e chega da contagem que a grade acabou de entregar de graça" |
| shor/capitulos/capitulo9b.py:136 | C10N04 | "a fala tem dois tempos — os quatro passos, depois o valor — e a animação acompanha: os ×8 acendem em cascata, e só então o r nasce" |
| shor/capitulos/capitulo9b.py:155 | C10N06 | "O passeio cumpriu o papel e sai no COMEÇO desta fala (r = 4 fica, sobe para o canto); a congruência só se move depois" |
| shor/capitulos/capitulo9b.py:176 | C10N06 | "a nota escreve a frase que a fala acaba de dizer" |
| shor/capitulos/capitulo9b.py:206 | C10N08 | ""o tronco em cima" e "os fatores embaixo": a árvore que reparte" (dois `Indicate`, nessa ordem) |
| shor/capitulos/capitulo9b.py:347 | C10N13 | "cada galho acende JUNTO do que pende dele: "fatores de 35" são os dois primos (…), "os de 117" são os dois batizados" (dois `play`, nessa ordem) |
| shor/capitulos/capitulo9b.py:369 | C10N14 | ""como isso é uma igualdade": o sinal de igual do meio" (1º `play`) |
| shor/capitulos/capitulo9b.py:372 | C10N14 | ""os mesmos fatores do outro lado também": o lado direito do j2 voa inteiro (…)" (2º `play`) |
| shor/capitulos/capitulo9b.py:403 | C10N16 | ""os dois números que acabamos de calcular"" (1º `play`) |
| shor/capitulos/capitulo9b.py:406 | C10N16 | ""o número que queremos fatorar": o n do topo, herdado do C10N15" (2º `play`) |
| shor/capitulos/capitulo9b.py:429 | C10N18 | ""os fatores p e q"" (último `play` da fala) |
| shor/capitulos/capitulo9b.py:540 | C10N29 | "animação curta sob fala longa: o cartão da solução aparece exatamente quando ela é dita, e o quadro fica parado no ✗ vermelho o resto da linha" |
| shor/capitulos/capitulo9b.py:562 | C10N30 | ""a contagem de Euler": o 24 que a conta acabou de entregar" (2º `play`) |
| shor/capitulos/capitulo9b.py:572 | C10N31 | ""a chave privada" é o d; "o inverso da chave pública" é o e com o módulo da contagem" (dois `Indicate`, nessa ordem) |
| shor/capitulos/capitulo9b.py:586 | C10N32 | "o sinal de igual é literalmente "são a mesma coisa"" (2º `play`) |
| shor/capitulos/capitulo10.py:199 | C11N10 | (docstring) "o `FadeOut` de fim pertence ao `C11N10` e roda (…) logo no começo da fala, em "De física é só isso" — o `Write(eqc)` só entra depois, atrasado" |
| shor/capitulos/capitulo10.py:307 | C11N10 | (docstring) "O `Write(eqc)` vem no mesmo `play`, mas atrasado por `Succession` até "outro exemplo" (~4,2 s)" |
| shor/capitulos/capitulo10.py:320 | C11N10 | ""De física é só isso": a limpeza abre a fala" |
| shor/capitulos/capitulo10.py:322 | C11N10 | ""outro exemplo" (~4,2 s): a congruência com o 21 entra quando a fala anuncia o exemplo novo" — hoje âncora `("C11N10", "outro exemplo")`, na tabela acima |
| shor/capitulos/capitulo10.py:548 | C11N22 | "a medida HIPOTÉTICA do C11N22, em cinco batidas na ordem da frase" |
| shor/capitulos/capitulo10.py:652 | C11N23 | ""nos fios de cima": eles estão em cena desde o C11N13 e a fala os nomeia ANTES de nomear a TQF" |
| shor/capitulos/capitulo10.py:1015 | C11N30 | "(1) o cursor, com um ponto em cada onda: "em cada ponto"" |
| shor/capitulos/capitulo10.py:1020 | C11N30 | "(2) o círculo: "cada onda vira uma seta"" |
| shor/capitulos/capitulo10.py:1033 | C11N30 | "(3) "emendadas uma na outra": a corrente ponta com cauda e, do centro até o fim dela, a seta grossa — a soma" |
| shor/capitulos/capitulo10.py:1312 | C11N38 | ""que se esconde ali" fecha a frase, e o "ali" é o 85/512 da PRIMEIRA linha" (2º `play`, o `Circumscribe`) |


## Âncora do V0N00 (1)

| tag | âncora | palavra-alvo em pt | palavra em inglês | fração pt | fração en | fala pt completa |
|---|---|---|---|---|---|---|
| V0N00 | `descrição` | "descrição" [a seta ↓ nasce no rodapé] | "description" | 0,957 | 0,942 (estimativa por caracteres, a ser medida na gravação) | Olá! Meu nome é Vitor, sou aluno de ciência da computação na Universidade Federal de Pelotas, e gosto de transformar matemática difícil em algo que dá para ver. Todas as minhas redes sociais e formas de contato estão aqui na descrição. |
