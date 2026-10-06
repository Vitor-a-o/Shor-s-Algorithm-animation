# Corpo — Vídeo 2: Aritmética modular, as quatro operações

Capítulos 1 a 5, na ordem de montagem.

---

## Abertura

Sem narração. O vídeo entra direto pelo cartão e cai no capítulo 1.

| Tag | Fala | Est. | Entra em |
|---|---|---|---|
| — | *(cartão silencioso, ~4 s)* | — | "Do Zero ao Algoritmo de Shor Quântico" nasce no centro e "Vídeo 2 de 4 — Aritmética modular" embaixo dele. O subtítulo sai primeiro e o título encolhe e some por último, já com o `CAP01` entrando por baixo — os dois cartões precisam se emendar num movimento só, senão a sequência lê como dois começos |

**Subtotal: ~4 s** (nenhuma locução)

---

## Capítulo 1 — Aritmética modular na reta segmentada

| Tag | Fala | Est. | Entra em |
|---|---|---|---|
| CAP01 | Começamos pelo objeto mais simples de toda a construção: o módulo. | 4,6 | cartão |
| C1N01 | Tudo o que vem a seguir acontece na aritmética modular. | 4,2 | `Create(reta)` |
| C1N02 | A linguagem visual do vídeo vai lidar com números como comprimentos de reta. | 5,4 | `Create(b11)` |
| C1N03 | O módulo é dado pelo resto da divisão de inteiros. | 4,2 | Todo o encaixe corre por baixo desta linha, sem pausa entre as etapas: os três blocos laranja nascem em cadeia da direita para a esquerda (`LaggedStart`), o quarto (`tenta`) avança e estoura o zero, e fecha com `Flash` + ✗ + `Wiggle` |
| C1N04 | Esse é o resto: dois. | 2,1 | `tenta → s2` |
| C1N05 | Dois é congruente a onze, módulo três. E o sinal de congruência, diferente da igualdade, é o aviso de que estamos falando de classes, não de números. | 11,3 | equação nasce |
| C1N06 | O onze não é o único elemento dessa classe. | 3,8 | — |
| C1N07 | O oito deixa o mesmo resto. | 2,5 | `b8` |
| C1N08 | O cinco também. | 1,3 | `b5` |
| C1N09 | E o dois é o próprio representante. | 2,9 | `b2` |
| C1N10 | Módulo três, esses quatro números são equivalentes. É isso que faz a aritmética modular funcionar: soma, produto e potência ficam todos bem definidos nas classes. | 10,4 | cadeia |
| C1N11 | Os próximos capítulos são exatamente isso: soma, produto e potência — e, no fim, um jeito de dividir. | 7,1 | — |

**Subtotal: 59,8 s** (cartão + 11 locuções)

---

## Capítulo 2 — Adição modular

| Tag | Fala | Est. | Entra em |
|---|---|---|---|
| CAP02 | Com o módulo definido, a primeira operação é a soma modular. | 4,6 | cartão |
| C2N01 | Seria possível resolver simplesmente somando os números e tirando o resto da divisão. Mas fazer uma divisão num circuito quântico é muito caro. | 9,6 | `Write(eq)` + `Create(reta)` |
| C2N02 | Então vamos chegar no mesmo resultado só com comparações, subtrações e somas. | 5,0 | as duas parcelas, o módulo medido da ponta direita para trás com o `x2` amarelo nascendo, e o verde desconhecido — `b6`, `a5`, `n7` + `x2`, rótulos e `cver` correndo emendados, sem pausa |
| C2N03 | Para isso declaramos um x, dado por n menos a. Sete menos cinco igual a dois — representado pelo traço amarelo. | 7,9 | `Write(ex0)` → `exf` → `rx → rx2` |
| C2N04 | Aí vem a comparação: x é maior que b? Podemos ver que não — o módulo coube inteiro dentro da soma. | 9,6 | `Write(tst0)` → `tst` → ✗ |
| C2N05 | Então o resto é igual a b menos x. Seis menos dois é igual a quatro. | 5,0 | `Write(t2s)` → `t2f` → `rc → rc4` |
| C2N06 | Portanto seis mais cinco é congruente a quatro, módulo sete. Fizemos duas subtrações e uma comparação. Nenhuma divisão. | 7,1 | `eq → eq2` |
| C2N07 | Agora, o que acontece se o módulo cresce. Com o módulo igual a oito, o laranja avança, o amarelo avança junto, o verde encolhe e assim por diante. | 10,0 | n = 8, 9, 10 e 11 — os quatro `ReplacementTransform` do laço correm num bloco só |
| C2N08 | Com doze algo muda de qualidade: o amarelo ultrapassa o vermelho, e o teste dá verdadeiro. | 6,7 | n = 12 + `Indicate(tst12)` |
| C2N09 | Agora o módulo não ultrapassou a soma: então o resto é a própria soma. Seis mais cinco, onze. | 9,6 | `Write(f2ab)` → `bc12` → `f2n` |
| C2N10 | Onze é congruente a onze, módulo doze. E é o teste "x maior que b" que decide entre os dois casos, ainda sem fazer divisão. | 10,4 | `eqc → eq12` |
| C2N11 | Guarde o padrão: comparar e subtrair no lugar de dividir. | 4,2 | — |

**Subtotal: 89,7 s** (cartão + 11 locuções)

---

## Capítulo 3 — Multiplicação modular (*Double and Add*)

| Tag | Fala | Est. | Entra em |
|---|---|---|---|
| CAP03 | Com a soma pronta, a segunda operação é a multiplicação modular. | 4,6 | cartão |
| C3N01 | A multiplicação pode ser representada por somas sucessivas. | 3,8 | `Write(eq)` e os cinco blocos "4" nascendo em cadeia correm emendados, num bloco só |
| C3N02 | O produto bruto é vinte: cabem duas vezes o sete, e o que sobra é o resto. | 7,1 | `baixo` + `rb` |
| C3N03 | Só que o custo desse caminho é proporcional ao tamanho do multiplicador. Quando ele fica muito grande a quantidade de somas cresce também, o que é computacionalmente pesado. | 10,4 | Animação nova, não existe hoje no `capitulo3.py`. Em "o tamanho do multiplicador", `Indicate` no cinco vermelho do `eq`. Em "quando ele fica muito grande", o valor do multiplicador cresce em cena e a fila de blocos "4" se multiplica junto, encolhendo de escala até escapar pelas bordas do quadro; os blocos de sete da linha de baixo se multiplicam no mesmo movimento. É o eco do laço de módulos crescentes do capítulo 2 — quem cresce lá é o módulo, aqui é o multiplicador |
| C3N04 | A saída é reagrupar as parcelas em duplas, duplas de duplas e assim por diante. | 9,2 | Animação nova. Nada desce para uma segunda linha: os agrupamentos nascem em volta dos próprios "4" azuis, sobre a reta. Em "duplas", os parênteses abraçam o 1º com o 2º e o 3º com o 4º; em "duplas de duplas", os colchetes fecham os dois parênteses; em "até sobrar o que não fecha dupla", o quinto "4" fica sozinho, sem nada em volta. Saem do capítulo o `toks`, os `fios` e a cópia para baixo. A saída de `baixo`/`rb` corre no começo desta linha |
| C3N05 | Assim dá para simplificar dentro de cada agrupamento. Somar duas vezes vira multiplicar por dois — o que da o nome *double* ao algoritmo. | 8,3 | Nos dois parênteses, `4 + 4` vira `2 · 4`; o quinto "4" ganha coeficiente e vira `1 · 4`. Tudo ainda em cima da reta, com os colchetes intactos |
| C3N06 | E de novo, um nível acima. | 1,7 | `[2·4 + 2·4] → 2²·4` e `1·4 → 2⁰·4`; `segs` e `rots` saem quando os dois termos se condensam. Só esses dois ficam em cena — o `2¹·4` ainda não existe |
| C3N07 | Essas potências de dois têm uma correspondência com os bits do multiplicador. | 5,0 | `origina_binario`, que passa a acontecer **depois** das potências e não antes |
| C3N08 | O bit do meio está desligado, e portanto, o termo dele nasce apagado. | 4,6 | o `p2` é criado agora, entre os dois, já esmaecido, puxado do `digs[1]` |
| C3N09 | E aqui está o ponto: cada parcela pode ser reduzida módulo sete em paralelo, antes de qualquer soma. | 7,1 | `e1/e2/e3`, e em seguida `bits_cx` + `setas_b` — os três blocos correm emendados, sem pausa |
| C3N10 | No caso do bit desligado, o que avança é o zero — o elemento nulo da adição. | 6,7 | `setas` + `res` |
| C3N11 | Como da pra ver nenhuma dessas caixas passou de dezesseis. | 2,1 | — |
| C3N12 | Só então as três se somam, ainda módulo sete. | 3,8 | `setas2` + `soma` |
| C3N13 | O resultado final é seis. | 1,7 | `seis` + `eq → eq2` no mesmo bloco |
| C3N14 | Então temos o algoritmo *Double and Add*, que utiliza dobrar e somar no lugar de multiplicar. E o custo deixou de ser o tamanho do multiplicador e agora é o número de bits dele. | 11,3 | — |

**Subtotal: 87,4 s** (cartão + 14 locuções)

---

## Capítulo 4 — Exponenciação modular (*Square and Multiply*)

| Tag | Fala | Est. | Entra em |
|---|---|---|---|
| CAP04 | Com o produto pronto, a terceira operação é a exponenciação modular. | 5,0 | cartão |
| C4N01 | A potência pode ser representada por multiplicações sucessivas. | 4,6 | `Write(eq)` e os seis "3" nascendo em cadeia correm emendados, num bloco só |
| C4N02 | A potência bruta é setecentos e vinte e nove: cabem muitos setes aí, e o que sobra é o resto. | 6,7 | `segs` e, emendado, `baixo` + `rb` |
| C4N03 | Só que aqui o crescimento é de outra natureza: cada passo no expoente multiplica o número inteiro. Com os expoentes da criptografia, isso não caberia no universo observável. | 12,1 | Animação nova, não existe hoje no `capitulo4.py`. Em "cada passo no expoente", `Indicate` no seis vermelho do `eq`; o valor do expoente cresce em cena e a corrente de trêses cresce junto, encolhendo de escala. A diferença com o capítulo 3 é o ponto da linha: lá a fila cresce **proporcional**, aqui a fila cresce devagar e é a **reta tracejada do resultado** que estoura, esticando para fora dos dois lados do quadro e engolindo o "…". É o terceiro elo da mesma corrente — no capítulo 2 cresce o módulo, no 3 o multiplicador, aqui o expoente |
| C4N04 | A saída é a mesma manobra do capítulo anterior: reagrupar os fatores em duplas, e duplas de duplas. | 7,1 | Animação nova. Nada desce para uma segunda linha: os agrupamentos nascem em volta dos próprios "3" da corrente. Em "duplas", os parênteses abraçam o 1º com o 2º, o 3º com o 4º e o 5º com o 6º; em "duplas de duplas", os colchetes fecham os dois primeiros parênteses e o terceiro par fica sozinho no colchete dele. Saem do capítulo o `toks`, os `fios` e a cópia para baixo. A saída de `segs`, `baixo` e `rb` corre no começo desta linha |
| C4N05 | Assim dá para simplificar dentro de cada agrupamento. Multiplicar duas vezes vira elevar ao quadrado — o que da o nome *square* do algoritmo. | 8,8 | Nos três parênteses, `3 × 3` vira `3²`. Tudo ainda no lugar, com os colchetes intactos |
| C4N06 | Então subimos um degrau: somas sucessivas dão o produto, produtos sucessivos dão a potência. | 6,2 | — |
| C4N07 | E de novo, um nível acima. | 1,7 | `[3² × 3²] → 3^2²` e `[3²] → 3^2¹`; a corrente antiga sai quando os dois termos se condensam, e a expressão desce para a faixa central para abrir espaço aos bits. Só esses dois ficam em cena — o `3^2⁰` ainda não existe |
| C4N08 | Essas potências de dois têm uma correspondência com os bits do expoente. | 5,0 | `origina_binario`, que passa a acontecer **depois** das potências e não antes |
| C4N09 | O último bit está desligado, e portanto, o termo dele nasce apagado. | 5,0 | o `p3` é criado agora, na ponta direita, já esmaecido, puxado do `digs[2]` |
| C4N10 | E aqui está o ponto: cada fator pode ser reduzido módulo sete em paralelo, antes de qualquer multiplicação. | 7,5 | `e1/e2/e3`, e em seguida `bits_cx` + `setas_b` — os três blocos correm emendados, sem pausa |
| C4N11 | No caso do bit desligado, o que avança é o um — o elemento neutro da multiplicação. | 5,8 | `setas` + `res` |
| C4N12 | Como dá pra ver, nenhuma dessas caixas passou de oitenta e um. | 4,2 | — |
| C4N13 | Só então os três se multiplicam, ainda módulo sete. | 3,8 | `setas2` + `soma` |
| C4N14 | O resultado final é um. | 1,7 | `um` + `eq → eq2` no mesmo bloco |
| C4N15 | Então temos o algoritmo *Square and Multiply*, que eleva ao quadrado e multiplica no lugar de exponenciar. E o custo deixou de ser o tamanho do expoente e agora é o número de bits dele. | 12,9 | — |
| C4N16 | É essa a operação que o circuito quântico de Shor executa em superposição — o capítulo quatro é, literalmente, o motor do algoritmo. | 8,8 | — |

**Subtotal: 106,9 s** (cartão + 16 locuções)

---

## Capítulo 5 — Inverso multiplicativo modular

*Reescrito no padrão dos capítulos 1–4: a fala diz o movimento geral, os números e as
substituições foram para a coluna **Entra em**, e as filas de teste passaram a correr em
bloco sob uma locução só (mesma lógica do `C2N07`). O capítulo ganhou o quarto elo da
corrente de custo — no 2 cresce o módulo, no 3 o multiplicador, no 4 o expoente, aqui
cresce a busca.*

| Tag | Fala | Est. | Entra em |
|---|---|---|---|
| CAP05 | Com a potência pronta, falta a quarta operação: dividir. | 4,2 | cartão |
| C5N01 | As outras três se construíram repetindo a operação anterior. Com a divisão isso não acontece. | 6,7 | `Write(eq)` |
| C5N02 | Numa reta feita só de inteiros não existe meio número — e sem meio número não existe divisão. | 7,1 | — (a reta do capítulo 1 volta em cena por um instante; nenhum corte cabe entre ela e o `eq`) |
| C5N03 | O que existe é a pergunta invertida: qual número desfaz a multiplicação. É ele que faz o papel da divisão. | 7,9 | `eq → eq2` |
| C5N04 | Ele tem nome: é o inverso multiplicativo. | 3,3 | — |
| C5N05 | Dá para procurar na mão: testar candidatos, um por um, até algum deixar resto um. | 6,3 | as **três filas** (`2·3`, `2·4`, `2·5`) correm emendadas, sem pausa entre elas — hoje são nove `cena.play` em três iterações; o `with narra` precisa envolver o `for` inteiro, não cada passo. A sobra verde e o ✓ da última fila fecham a linha |
| C5N06 | Cinco é o inverso de dois, módulo nove. | 3,3 | `eq2 → eq3` |
| C5N07 | E vale nos dois sentidos: inverso é sempre um par. Multiplicar por um é dividir pelo outro. | 6,7 | `Write(par)` |
| C5N08 | Só que procurar assim custa o tamanho do módulo. E o módulo, na criptografia, é justamente o número grande da história inteira. | 8,8 | Animação nova, não existe hoje no `capitulo5.py`. É o **quarto elo** da corrente: em "o tamanho do módulo", `Indicate` no nove laranja do `eq`; a reta laranja se estica e as filas vermelhas se multiplicam para baixo, encolhendo de escala até escaparem pela borda inferior do quadro. Mesmo gesto do laço do capítulo 2 e da fila crescente do 3 — aqui quem cresce é a busca |
| C5N09 | Existe um jeito melhor do que testar um a um que é o algoritmo de Euclides estendido, porém não vamos nos aprofundar nele nessa série. | 6,3 | Animação nova. Um exemplo do algoritmo correndo por baixo, **sem que a fala comente nada dele** — a escada de segmentos do capítulo 1: o módulo laranja medido pelo vermelho, a sobra virando a régua do passo seguinte, e assim até o pedaço de tamanho um. Roda rápido e sai. A fala acaba antes da animação; o que resta corre em silêncio |
| C5N10 | Uma pergunta que devemos fazer para essa operação é, o inverso sempre existe? | 7,1 | `eq3 → eq4` |
| C5N11 | Vamos tentar inverter o três módulo nove dessa vez. | 3,8 | as **seis filas** do `for` (`3·1` a `3·6`) correm emendadas, num bloco só — dezoito `cena.play` sob uma locução. Mesma correção do `C2N07`: o `with narra` envolve o laço inteiro |
| C5N12 | Os restos fecham um ciclo e voltam ao começo, para sempre. O um não está nele. | 5,8 | `ciclo` |
| C5N13 | Dividir por três módulo nove, é uma operação que simplesmente não existe. | 5,4 | `FadeIn(xis)` — separado do `Write(mdc3)`, que hoje roda no mesmo `play` |
| C5N14 | E o motivo cabe numa linha: ele e o módulo compartilham um fator. | 5,0 | `Write(mdc3)` |
| C5N15 | Vale ver a coisa toda de uma vez: toda multiplicação possível dentro deste módulo, numa tabela só. | 7,5 | `titulo_tab` + cabeçalhos + eixos e, emendado, `Write(como)` — o `como` sai de dentro do bloco do `Indicate` e acontece antes dele |
| C5N16 | O par que a gente achou nas retas está aqui dentro, e as outras células obedecem à mesma regra. | 7,1 | `Indicate` dos cabeçalhos + `ex25`, a célula nascendo da equação e o `LaggedStart(demais)` correm emendados, num bloco só |
| C5N17 | Agora a tabela inteira se lê de um jeito só: onde a célula dá um, linha e coluna são inversas. Cada círculo verde é uma divisão que existe. | 10,4 | `circulos` + `inv1`, depois `inv2` |
| C5N18 | O nosso par aparece duas vezes, espelhado na diagonal. | 3,8 | `rec1` + `Indicate` nas duas células |
| C5N19 | Do mesmo jeito que nos testes, aparecem os ciclos que nunca passam pelo um. Essas linhas e colunas são os números sem inverso. | 9,2 | `mortos` (opacidade cai + retângulos vermelhos) + `m_rot` e, emendado, `rec2` + `Indicate(mortos[1])` — os dois blocos correm sob esta linha |
| C5N20 | E o critério é o mesmo do começo: só tem inverso quem não compartilha fator com o módulo. | 6,7 | `concl` + `caixa` |

**Subtotal: 132,4 s** (cartão + 20 locuções)

---

## Encerramento

| Tag | Fala | Est. | Entra em |
|---|---|---|---|
| V2N00 | Fecha o conjunto. Um módulo, e em cima dele as quatro operações: somar, multiplicar, elevar a uma potência e dividir — todas sem nunca fazer uma divisão. | 11,3 | Os quatro símbolos `+`, `×`, `xⁿ` e `÷` entram em fila, um a cada operação nomeada. Em "sem nunca fazer uma divisão", o `÷` é **riscado** e o `a⁻¹` nasce ao lado — o risco não sai, porque a divisão continua não existindo |
| V2N01 | O vídeo três pega essas quatro operações e monta com elas o RSA — a criptografia que protege a internet hoje. | 8,3 | Os quatro símbolos saem e o cadeado do vídeo 1 reaparece no centro, **fechado e intacto** |
| — | *(cartão final, ~3 s)* | — | "Vídeo 3 de 4 — Do teorema ao RSA" |

**Subtotal: 19,6 s** (2 locuções) + cartão ~3 s

---

## Projeção de duração

| Bloco | Locuções | Fala |
|---|---|---|
| Cartão de abertura | — | — |
| Capítulo 1 | 12 | 59,8 s |
| Capítulo 2 | 12 | 89,7 s |
| Capítulo 3 | 15 | 87,4 s |
| Capítulo 4 | 17 | 106,9 s |
| Capítulo 5 | 21 | 132,4 s |
| Encerramento | 2 | 19,6 s |
| **Total** | **79** | **495,8 s** |

Somando o `PAD` de 0,35 s por locução (27,7 s), os dois cartões silenciosos (~7 s) e os
`limpar()` entre capítulos (~20 s), a projeção é de **cerca de 9 min 10 s**. O capítulo 5
saiu de 194,7 s para 132,4 s e deixou de ser o bloco mais pesado do vídeo — agora é o
capítulo 4.

Duas linhas do capítulo 5 têm animação mais longa que a fala e vão correr um trecho em
silêncio: `C5N05` (as três filas de teste) e `C5N09` (a passagem do Euclides). Isso não
entra na conta acima — some uns 6 a 8 s ao render real, dependendo do `run_time` que a
escada de segmentos receber.

---

## Checklist de gravação

- [ ] Cartões — CAP01 a CAP05
- [ ] Capítulo 1 — C1N01 a C1N11
- [ ] Capítulo 2 — C2N01 a C2N11
- [ ] Capítulo 3 — C3N01 a C3N14
- [ ] Capítulo 4 — C4N01 a C4N16
- [ ] Capítulo 5 — C5N01 a C5N20 *(regravação completa: as tags antigas C5N21 a C5N30 deixam de existir e as demais mudaram de texto)*
- [ ] Encerramento — V2N00 e V2N01
- [ ] `python medir.py`
- [ ] Render de conferência com `NARRA = True`

---

## Pendências de código do capítulo 5 (`parte5`)

1. `with narra` envolvendo o `for fila, x in enumerate((3, 4, 5))` **inteiro** — hoje são
   três `cena.play` por iteração, e a narração nova cobre as três filas com uma fala só
   (`C5N05`).
2. O mesmo para o `for fila, x in enumerate((1, 2, 3, 4, 5, 6))` do contra-exemplo
   (`C5N11`).
3. Separar `FadeIn(xis)` de `Write(mdc3)` em dois blocos (`C5N13` e `C5N14`).
4. Tirar o `Write(como)` de dentro do bloco do `Indicate` dos cabeçalhos, para que ele
   aconteça antes (`C5N15`).
5. Emendar `Indicate` + `ex25` + `ReplacementTransform` da célula + `LaggedStart(demais)`
   num bloco só (`C5N16`).
6. Animação nova do custo (`C5N08`): `Indicate` no módulo laranja, a reta se esticando e
   as filas se multiplicando até escaparem pela borda de baixo. É a irmã das animações
   novas do `C3N03` e do `C4N03`.
7. Animação nova do Euclides (`C5N09`): a escada de segmentos — o módulo medido pelo
   vermelho, a sobra virando régua do passo seguinte, até o pedaço unitário. Reaproveita o
   `traco()` e a mesma unidade `u` das filas de teste, só empilhando três linhas curtas.
   Roda solta, sem locução por cima, e sai antes do `eq3 → eq4`.
8. Emendar `mortos` + `m_rot` com `rec2` + `Indicate(mortos[1])` num bloco só (`C5N19`).
   O capítulo termina no `concl` + `caixa` — a troca do módulo de 9 para 7 no fim saiu.
