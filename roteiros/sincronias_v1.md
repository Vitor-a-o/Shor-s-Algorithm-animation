# Vídeo 1 — sincronias por ordem de palavra

As âncoras abaixo marcam **onde, dentro de uma fala, cai a palavra que
dispara um gesto** do vídeo 1. Estão em `shor/videos/sincronias_v1.py`,
na tabela `SINC`. Em inglês a ordem das palavras muda, então cada fração
precisa ser medida de novo no áudio em inglês.

**Como preencher o inglês:** para cada linha, escolha na fala em inglês a
palavra que corresponde à palavra-alvo em pt. Depois da gravação, meça em
que fração da locução ela cai e escreva em `SINC["en"]` com **a mesma
chave** (tag, âncora em pt), por exemplo
`("V1N03", "RSA"): 0.31`. Âncora que faltar em `"en"` usa a fração do pt, e
o render avisa uma vez por âncora (`sincronia V1N03 "RSA": sem fração em en…`).
Traduzir é só trocar números: o `video1.py` não muda.

As frações do pt foram estimadas pela contagem de caracteres da fala, menos
as do V1N07, que são o começo de cada trecho da decupagem do roteiro, em
segundos dos 20,3 s estimados.

## Âncoras do vídeo 1 (45)

| tag | âncora | palavra-alvo em pt | fração pt | fala pt completa |
|---|---|---|---|---|
| V1N00 | `protege` | "protege quase tudo" [começa o empurrão] | 0,185 | Existe uma aposta que protege quase tudo que você faz na internet, e ela não é uma senha forte que você possa escolher. |
| V1N00 | `internet` | fim de "internet" [o pacote para] | 0,546 | Existe uma aposta que protege quase tudo que você faz na internet, e ela não é uma senha forte que você possa escolher. |
| V1N00 | `e ela não é` | "e ela não é" [o envelope vira o campo de senha] | 0,563 | Existe uma aposta que protege quase tudo que você faz na internet, e ela não é uma senha forte que você possa escolher. |
| V1N00 | `senha forte` | "uma senha forte" [os pontos digitados] | 0,664 | Existe uma aposta que protege quase tudo que você faz na internet, e ela não é uma senha forte que você possa escolher. |
| V1N00 | `que você possa` | "que você possa" [o risco vermelho] | 0,798 | Existe uma aposta que protege quase tudo que você faz na internet, e ela não é uma senha forte que você possa escolher. |
| V1N00 | `escolher` | "escolher" [o campo some] | 0,924 | Existe uma aposta que protege quase tudo que você faz na internet, e ela não é uma senha forte que você possa escolher. |
| V1N01 | `compras online` | "compras online" [2º item] | 0,202 | Ela está por trás de contas bancárias, compras online e mensagens privadas. E o que se aposta é que existem operações fáceis de fazer numa direção e impraticáveis de desfazer, até onde se sabe. |
| V1N01 | `mensagens privadas` | "mensagens privadas" [3º item] | 0,290 | Ela está por trás de contas bancárias, compras online e mensagens privadas. E o que se aposta é que existem operações fáceis de fazer numa direção e impraticáveis de desfazer, até onde se sabe. |
| V1N01 | `fáceis de fazer` | "fáceis de fazer numa direção" [seta de ida] | 0,611 | Ela está por trás de contas bancárias, compras online e mensagens privadas. E o que se aposta é que existem operações fáceis de fazer numa direção e impraticáveis de desfazer, até onde se sabe. |
| V1N01 | `impraticáveis` | "impraticáveis de desfazer" [seta de volta] | 0,772 | Ela está por trás de contas bancárias, compras online e mensagens privadas. E o que se aposta é que existem operações fáceis de fazer numa direção e impraticáveis de desfazer, até onde se sabe. |
| V1N02 | `multiplicar` | "Multiplicar dois primos grandes" [o bloco reabre] | 0,195 | A operação mais conhecida desse tipo é a fatoração. Multiplicar dois primos grandes é fácil, mas voltar do produto para os primos é o que ninguém sabe fazer em tempo razoável. Um computador comum levaria bilhões de anos para fatorar os números utilizados atualmente. |
| V1N02 | `voltar do produto` | "voltar do produto para os primos" [a volta se despedaça] | 0,365 | A operação mais conhecida desse tipo é a fatoração. Multiplicar dois primos grandes é fácil, mas voltar do produto para os primos é o que ninguém sabe fazer em tempo razoável. Um computador comum levaria bilhões de anos para fatorar os números utilizados atualmente. |
| V1N02 | `bilhões de anos` | "bilhões de anos" [o contador; hoje capado em 5,6 s antes do fim da fala] | 0,765 (14,0 s / 18,3) | A operação mais conhecida desse tipo é a fatoração. Multiplicar dois primos grandes é fácil, mas voltar do produto para os primos é o que ninguém sabe fazer em tempo razoável. Um computador comum levaria bilhões de anos para fatorar os números utilizados atualmente. |
| V1N03 | `RSA` | "é o RSA" [cresce e grava as letras] | 0,219 | O algoritmo que se apoia justamente na fatoração é o RSA, e é ele que esta série vai desmontar, peça por peça. É o mais direto de construir do zero, mas não é o único que vive de uma aposta assim, nem vai ser o único a cair. |
| V1N03 | `não é o único` | "não é o único" [a rede se desenha] | 0,683 | O algoritmo que se apoia justamente na fatoração é o RSA, e é ele que esta série vai desmontar, peça por peça. É o mais direto de construir do zero, mas não é o único que vive de uma aposta assim, nem vai ser o único a cair. |
| V1N03 | `único a cair` | "nem vai ser o único a cair" [todos pulsam] | 0,879 | O algoritmo que se apoia justamente na fatoração é o RSA, e é ele que esta série vai desmontar, peça por peça. É o mais direto de construir do zero, mas não é o único que vive de uma aposta assim, nem vai ser o único a cair. |
| V1N04 | `vence essa aposta` | "vence essa aposta" [os "?" voltam nos primos] | 0,368 | Em mil novecentos e noventa e quatro, Peter Shor mostrou que um computador quântico vence essa aposta, e não só a do RSA. Era teoria, mas nos últimos anos a máquina vem saindo do papel, e talvez a aposta tenha prazo de validade. |
| V1N04 | `não só a do RSA` | "não só a do RSA" [os anônimos piscam] | 0,461 | Em mil novecentos e noventa e quatro, Peter Shor mostrou que um computador quântico vence essa aposta, e não só a do RSA. Era teoria, mas nos últimos anos a máquina vem saindo do papel, e talvez a aposta tenha prazo de validade. |
| V1N04 | `últimos anos` | "nos últimos anos" [a linha do tempo] | 0,605 | Em mil novecentos e noventa e quatro, Peter Shor mostrou que um computador quântico vence essa aposta, e não só a do RSA. Era teoria, mas nos últimos anos a máquina vem saindo do papel, e talvez a aposta tenha prazo de validade. |
| V1N04 | `prazo de validade` | "prazo de validade" [a quebra; hoje capada em 3,31 s antes do fim] | 0,921 | Em mil novecentos e noventa e quatro, Peter Shor mostrou que um computador quântico vence essa aposta, e não só a do RSA. Era teoria, mas nos últimos anos a máquina vem saindo do papel, e talvez a aposta tenha prazo de validade. |
| V1N05 | `esta série` | "esta série" [os quatro vídeos saem do título] | 0,750 | Essa é a promessa, ou a ameaça, do algoritmo de Shor. E é exatamente o que esta série vai construir. |
| V1N06 | `neles eu passo` | "neles eu passo por cada peça" [o 1 acende; piso de 85% da fala] | 0,263 | São quatro vídeos no total, e neles eu passo por cada peça necessária para entender como se chega nesse algoritmo. |
| V1N07 | `somar` | "É somar" — trecho 2 da decupagem (cap. 2, parcelas 6 + 5) | 0,276 (5,6 s / 20,3) | No vídeo dois vou mostrar a aritmética modular, que é a base matemática de toda a série. É somar, multiplicar e elevar a potências num mundo onde os números dão a volta, e só o que sobra importa. No fim aparece até um jeito de dividir, sem dividir de verdade. |
| V1N07 | `multiplicar` | "multiplicar" — trecho 3 (cap. 3, os cinco 4) | 0,355 (7,2 s / 20,3) | No vídeo dois vou mostrar a aritmética modular, que é a base matemática de toda a série. É somar, multiplicar e elevar a potências num mundo onde os números dão a volta, e só o que sobra importa. No fim aparece até um jeito de dividir, sem dividir de verdade. |
| V1N07 | `potências` | "elevar a potências" — trecho 4 (cap. 4, a corrente de 3) | 0,424 (8,6 s / 20,3) | No vídeo dois vou mostrar a aritmética modular, que é a base matemática de toda a série. É somar, multiplicar e elevar a potências num mundo onde os números dão a volta, e só o que sobra importa. No fim aparece até um jeito de dividir, sem dividir de verdade. |
| V1N07 | `num mundo` | "num mundo onde os números" — trecho 5 (cap. 2, o n laranja cresce) | 0,498 (10,1 s / 20,3) | No vídeo dois vou mostrar a aritmética modular, que é a base matemática de toda a série. É somar, multiplicar e elevar a potências num mundo onde os números dão a volta, e só o que sobra importa. No fim aparece até um jeito de dividir, sem dividir de verdade. |
| V1N07 | `dão a volta` | "dão a volta" — trecho 6 (cap. 2, os estados n = 8…11) | 0,571 (11,6 s / 20,3) | No vídeo dois vou mostrar a aritmética modular, que é a base matemática de toda a série. É somar, multiplicar e elevar a potências num mundo onde os números dão a volta, e só o que sobra importa. No fim aparece até um jeito de dividir, sem dividir de verdade. |
| V1N07 | `só o que sobra` | "só o que sobra importa" — trecho 7 (cap. 1, sobra o 2 verde) | 0,631 (12,8 s / 20,3) | No vídeo dois vou mostrar a aritmética modular, que é a base matemática de toda a série. É somar, multiplicar e elevar a potências num mundo onde os números dão a volta, e só o que sobra importa. No fim aparece até um jeito de dividir, sem dividir de verdade. |
| V1N07 | `no fim` | "No fim aparece" — trecho 8 (cap. 5, a fila 2·5 passa com ✓) | 0,719 (14,6 s / 20,3) | No vídeo dois vou mostrar a aritmética modular, que é a base matemática de toda a série. É somar, multiplicar e elevar a potências num mundo onde os números dão a volta, e só o que sobra importa. No fim aparece até um jeito de dividir, sem dividir de verdade. |
| V1N07 | `jeito de dividir` | "um jeito de dividir" — trecho 9 (cap. 5, seis filas com ✗) | 0,798 (16,2 s / 20,3) | No vídeo dois vou mostrar a aritmética modular, que é a base matemática de toda a série. É somar, multiplicar e elevar a potências num mundo onde os números dão a volta, e só o que sobra importa. No fim aparece até um jeito de dividir, sem dividir de verdade. |
| V1N07 | `sem dividir` | "sem dividir de verdade" — trecho 10 (tabela mod 9, ÷ riscado → a⁻¹) | 0,887 (18,0 s / 20,3) | No vídeo dois vou mostrar a aritmética modular, que é a base matemática de toda a série. É somar, multiplicar e elevar a potências num mundo onde os números dão a volta, e só o que sobra importa. No fim aparece até um jeito de dividir, sem dividir de verdade. |
| V1N08 | `teoremas` | "teoremas" [a elipse e a linha 1; 2,2 s da decupagem] | 0,182 | O vídeo três começa pelos teoremas, e é onde entram Fermat e Euler, dois nomes que parecem abstratos até você ver que é neles que o RSA se apoia. |
| V1N09 | `RSA` | "RSA" ["Euler" vira "RSA" no rótulo] | 0,236 | Enfim, ainda no vídeo três, explico o RSA, com duas chaves, uma pública e uma privada, nascendo de um par de números primos. E quebrar isso é, no fundo, fatorar. |
| V1N10 | `ordem modular` | "entra a ordem modular" [o zigue-zague] | 0,319 | No quarto e último vídeo, o maior da série, entra a ordem modular. Com ela, fatorar deixa de ser caçar divisores e vira procurar um ciclo. |
| V1N10 | `com ela` | "Com ela" [as árvores] | 0,473 | No quarto e último vídeo, o maior da série, entra a ordem modular. Com ela, fatorar deixa de ser caçar divisores e vira procurar um ciclo. |
| V1N10 | `divisores` | "caçar divisores" [a tabela volta; 8,4 s da decupagem] | 0,764 | No quarto e último vídeo, o maior da série, entra a ordem modular. Com ela, fatorar deixa de ser caçar divisores e vira procurar um ciclo. |
| V1N10 | `procurar` | "procurar um ciclo" [o ciclo fecha] | 0,870 | No quarto e último vídeo, o maior da série, entra a ordem modular. Com ela, fatorar deixa de ser caçar divisores e vira procurar um ciclo. |
| V1N11 | `quântico` | "computador quântico" segundo o código [o ciclo sai] — pela contagem de caracteres, 0,332 cai em "Então" | 0,332 | Só que, num computador comum, achar esse ciclo é tão lento quanto fatorar. Então entra o computador quântico, que segue uma lógica diferente, em que as respostas erradas se cancelam e as certas se reforçam. E esse é o algoritmo de Shor. |
| V1N11 | `lógica diferente` | "uma lógica diferente" [o circuito; 9,4 s da decupagem] | 0,503 | Só que, num computador comum, achar esse ciclo é tão lento quanto fatorar. Então entra o computador quântico, que segue uma lógica diferente, em que as respostas erradas se cancelam e as certas se reforçam. E esse é o algoritmo de Shor. |
| V1N11 | `respostas erradas` | "as respostas erradas" [as ondas; 12,6 s da decupagem] | 0,674 | Só que, num computador comum, achar esse ciclo é tão lento quanto fatorar. Então entra o computador quântico, que segue uma lógica diferente, em que as respostas erradas se cancelam e as certas se reforçam. E esse é o algoritmo de Shor. |
| V1N11 | `se cancelam` | "se cancelam" [os vales achatam] | 0,737 | Só que, num computador comum, achar esse ciclo é tão lento quanto fatorar. Então entra o computador quântico, que segue uma lógica diferente, em que as respostas erradas se cancelam e as certas se reforçam. E esse é o algoritmo de Shor. |
| V1N11 | `se reforçam` | "se reforçam" [os picos crescem] | 0,817 | Só que, num computador comum, achar esse ciclo é tão lento quanto fatorar. Então entra o computador quântico, que segue uma lógica diferente, em que as respostas erradas se cancelam e as certas se reforçam. E esse é o algoritmo de Shor. |
| V1N11 | `algoritmo de Shor` | "E esse é o algoritmo de Shor" [a seta no pico] | 0,866 | Só que, num computador comum, achar esse ciclo é tão lento quanto fatorar. Então entra o computador quântico, que segue uma lógica diferente, em que as respostas erradas se cancelam e as certas se reforçam. E esse é o algoritmo de Shor. |
| V1N11 | `Shor` | "Shor", fim da fala [a trilha acende] | 0,950 | Só que, num computador comum, achar esse ciclo é tão lento quanto fatorar. Então entra o computador quântico, que segue uma lógica diferente, em que as respostas erradas se cancelam e as certas se reforçam. E esse é o algoritmo de Shor. |
| V1N12 | `resto` | "o resto de uma divisão" [tudo vira "resto"; piso de 85% da fala] | 0,414 | Começamos do jeito mais simples possível, com o resto de uma divisão. É tudo o que você precisa saber até aqui. |

### O que a tabela não cobre

- **Tetos e pisos, que não dependem do idioma.** No V1N02 ("bilhões") e no
  V1N04 ("prazo de validade") a palavra só vale se cair antes do teto, que
  é o último instante em que o resto do bloco ainda cabe na fala (5,6 s e
  3,31 s antes do fim). Hoje, em pt, o teto vale nos dois. No V1N06 e no
  V1N12 o gesto nunca começa antes de 85% da fala menos a duração dele. Esses
  números ficam no código.
- **Gestos que caem numa palavra só pela soma dos `run_time` anteriores**,
  sem âncora própria. Em inglês eles acompanham a âncora anterior, ou o
  começo da fala, e não a palavra:
  - V1N01: "contas bancárias", ao fim do cadeado que desce e abre (2,0 s × k);
  - V1N02: "fatoração", imediata, de propósito ("logo nos primeiros segundos");
  - V1N05: "a promessa, ou a ameaça, do algoritmo de Shor", os cacos subindo;
  - V1N06: "São quatro vídeos", no começo da fala;
  - V1N08: "Fermat" → "Euler" (5,4 s) e o resto da decupagem, em sequência
    depois de `teoremas`;
  - V1N09: o resto da decupagem, em sequência depois de `RSA`;
  - V1N11: os qubits ("Então"), logo depois de `quântico`.

## Outras sincronias por ordem de palavra

Fora do vídeo 1, nos capítulos. São comentários que amarram a animação à
ordem das palavras dentro de uma fala. **Nada disso usa fração:** a ordem
está nos próprios `play` em sequência, ou num `Wait` fixo. Nenhum código
mudou. Os comentários estão aqui para conferir quando a fala em inglês for
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
| shor/capitulos/capitulo10.py:197 | C11N10 | (docstring) "o `FadeOut` de fim pertence ao `C11N10` e roda (…) logo no começo da fala, em "De física é só isso" — o `Write(eqc)` só entra depois, atrasado" |
| shor/capitulos/capitulo10.py:305 | C11N10 | (docstring) "O `Write(eqc)` vem no mesmo `play`, mas atrasado por `Succession` até "outro exemplo" (~4,2 s)" |
| shor/capitulos/capitulo10.py:316 | C11N10 | ""De física é só isso": a limpeza abre a fala" |
| shor/capitulos/capitulo10.py:318 | C11N10 | ""outro exemplo" (~4,2 s): a congruência com o 21 entra quando a fala anuncia o exemplo novo" — **`Wait(4.2 * VEL)` fixo**, a única destas em segundos |
| shor/capitulos/capitulo10.py:542 | C11N22 | "a medida HIPOTÉTICA do C11N22, em cinco batidas na ordem da frase" |
| shor/capitulos/capitulo10.py:646 | C11N23 | ""nos fios de cima": eles estão em cena desde o C11N13 e a fala os nomeia ANTES de nomear a TQF" |
| shor/capitulos/capitulo10.py:1009 | C11N30 | "(1) o cursor, com um ponto em cada onda: "em cada ponto"" |
| shor/capitulos/capitulo10.py:1014 | C11N30 | "(2) o círculo: "cada onda vira uma seta"" |
| shor/capitulos/capitulo10.py:1027 | C11N30 | "(3) "emendadas uma na outra": a corrente ponta com cauda e, do centro até o fim dela, a seta grossa — a soma" |
| shor/capitulos/capitulo10.py:1306 | C11N38 | ""que se esconde ali" fecha a frase, e o "ali" é o 85/512 da PRIMEIRA linha" (2º `play`, o `Circumscribe`) |

