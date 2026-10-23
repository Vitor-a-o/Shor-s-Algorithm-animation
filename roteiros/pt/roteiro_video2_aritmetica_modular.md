# Corpo — Vídeo 2: Aritmética modular, as quatro operações

Capítulos 1 a 5, na ordem de montagem.

---

## Abertura

Só a apresentação do autor, por cima do cartão. O vídeo entra direto pelo cartão e cai no capítulo 1.

| Tag | Fala | Est. | Entra em |
|---|---|---|---|
| — | *(cartão, ~17 s, com a apresentação)* | — | "Do Zero ao Algoritmo de Shor Quântico" nasce no centro e "Vídeo 2 de 4 — Aritmética modular" embaixo dele. O subtítulo sai primeiro e o título encolhe e some por último, já com o `CAP01` entrando por baixo — os dois cartões precisam se emendar num movimento só, senão a sequência lê como dois começos. Durante o cartão roda a apresentação do autor (`V0N00`, em `roteiro_video0_apresentacao.md`). |

**Subtotal: ~17,1 s** (só a apresentação do autor, que segura o cartão)

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
| C1N06 | O onze não é o único elemento dessa classe. | 3,8 | realce (seção **Realces**) |
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
| C2N07 | Agora, o que acontece se o módulo cresce. | 2,9 | realce do módulo (seção **Realces**), com a reta parada em n = 7 |
| — | *(sem fala — o laço roda mudo)* | — | n = 8, 9, 10 e 11 — os quatro `ReplacementTransform` do laço, em silêncio, fora de qualquer `with narra`, logo depois do `C2N07`. A tela mostra sozinha o laranja avançando, o amarelo junto e o verde encolhendo (~4 s) |
| C2N08 | Com doze algo muda de qualidade: o amarelo ultrapassa o vermelho, e o teste dá verdadeiro. | 6,7 | n = 12 + `Indicate(tst12)` |
| C2N09 | Agora o módulo não ultrapassou a soma: então o resto é a própria soma. Seis mais cinco, onze. | 9,6 | `Write(f2ab)` → `bc12` → `f2n` |
| C2N10 | Onze é congruente a onze, módulo doze. E é o teste "x maior que b" que decide entre os dois casos, ainda sem fazer divisão. | 10,4 | `eqc → eq12` |
| C2N11 | Guarde o padrão: comparar e subtrair no lugar de dividir. | 4,2 | — |

**Subtotal: 82,6 s** (cartão + 11 locuções) + ~4 s do laço mudo

---

## Capítulo 3 — Multiplicação modular (*Double and Add*)

| Tag | Fala | Est. | Entra em |
|---|---|---|---|
| CAP03 | Com a soma pronta, a segunda operação é a multiplicação modular. | 4,6 | cartão |
| C3N01 | A multiplicação pode ser representada por somas sucessivas. | 3,8 | `Write(eq)` e os cinco blocos "4" nascendo em cadeia correm emendados, num bloco só. Os quatro `+` nascem entre os "4", na mesma altura dos rótulos, em "somas sucessivas" — a fila se lê como `4 + 4 + 4 + 4 + 4`. Os `+` crescem e encolhem com a fila no `C3N03` e são eles que vão para os lugares dos `+` do `C3N04` |
| C3N02 | O produto bruto é vinte: cabem duas vezes o sete, e o que sobra é o resto. | 7,1 | `baixo` + `rb` |
| C3N03 | Só que o custo desse caminho é proporcional ao tamanho do multiplicador. Quando ele fica muito grande a quantidade de somas cresce também, o que é computacionalmente pesado. | 10,4 | Animação nova, não existe hoje no `capitulo3.py`. Em "o tamanho do multiplicador", `Indicate` no cinco vermelho do `eq`. Em "quando ele fica muito grande", o valor do multiplicador cresce em cena e a fila de blocos "4" se multiplica junto, encolhendo de escala até escapar pelas bordas do quadro; os blocos de sete da linha de baixo se multiplicam no mesmo movimento. É o eco do laço de módulos crescentes do capítulo 2 — quem cresce lá é o módulo, aqui é o multiplicador |
| C3N04 | A saída é reagrupar as parcelas em duplas, duplas de duplas e assim por diante. | 9,2 | Animação nova. Nada desce para uma segunda linha: os agrupamentos nascem em volta dos próprios "4" azuis, sobre a reta. Em "duplas", os parênteses abraçam o 1º com o 2º e o 3º com o 4º; em "duplas de duplas", os colchetes fecham os dois parênteses; em "até sobrar o que não fecha dupla", o quinto "4" fica sozinho, sem nada em volta. Os quatro `+` do `C3N01` deslizam para os lugares dos `+` da expressão agrupada — nenhum `+` nasce do vazio. A saída de `baixo`/`rb` corre no começo desta linha |
| C3N05 | Assim dá para simplificar dentro de cada agrupamento. Somar duas vezes vira multiplicar por dois — o que da o nome *double* ao algoritmo. | 8,3 | Nos dois parênteses, `4 + 4` vira `2 · 4`; o quinto "4" ganha coeficiente e vira `1 · 4`. Tudo ainda em cima da reta, com os colchetes intactos |
| C3N06 | Subindo mais um nível, juntamos os dobros numa potência de dois, e até o termo que sobrou ganha a sua. | 7,2 | Tudo **no lugar**, na mesma altura em que a expressão já está — nada desce agora. Em "juntamos", `[2·4 + 2·4] → 2²·4`, no ponto onde estava o colchete; em "termo que sobrou", `1·4 → 2⁰·4`, onde estava o quinto "4". O `+` do avulso fica entre os dois. Só esses dois termos ficam em cena — o `2¹·4` ainda não existe |
| C3N07 | Essas potências de dois têm uma correspondência com os bits do multiplicador. | 5,0 | `origina_binario`, que acontece **depois** das potências. No mesmo `play` em que os bits nascem do 5, `2²·4`, o `+` e `2⁰·4` descem juntos para a faixa central, abrindo um vão no meio onde o `2¹·4` vai nascer — a expressão só sai do lugar quando os bits chegam |
| C3N08 | O bit do meio está desligado, e portanto, o termo dele nasce apagado. | 4,6 | o `p2` é criado agora, no vão que o `C3N07` abriu entre os dois, já esmaecido, puxado do `digs[1]` |
| C3N09 | E aqui está o ponto: cada parcela pode ser reduzida módulo sete em paralelo, antes de qualquer soma. | 7,1 | `e1/e2/e3`, e em seguida `bits_cx` + `setas_b` — os três blocos correm emendados, sem pausa |
| C3N10 | No caso do bit desligado, o que avança é o zero — o elemento nulo da adição. | 6,7 | `setas` + `res` |
| C3N11 | Só então as três se somam, ainda módulo sete. | 3,8 | `setas2` + `soma` |
| C3N12 | O resultado final é seis. | 1,7 | `seis` + `eq → eq2` no mesmo bloco |
| C3N13 | Então temos o algoritmo *Double and Add*, que utiliza dobrar e somar no lugar de multiplicar. E o custo deixou de ser o tamanho do multiplicador e agora é o número de bits dele. | 11,3 | realce (seção **Realces**) |

**Subtotal: 90,8 s** (cartão + 13 locuções)

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
| C4N07 | Subindo mais um nível, juntamos os quadrados de novo, e os expoentes passam a ser potências de dois. | 6,5 | Tudo **no lugar**, na mesma altura em que a expressão já está — nada desce agora. Em "juntamos", `[3² × 3²] → 3^2²` e `[3²] → 3^2¹`, cada um no ponto onde estava o seu colchete; o `×` entre os colchetes fica entre os dois. A corrente antiga sai quando os dois termos se condensam. Só esses dois ficam em cena — o `3^2⁰` ainda não existe |
| C4N08 | Essas potências de dois têm uma correspondência com os bits do expoente. | 5,0 | `origina_binario`, que acontece **depois** das potências. No mesmo `play` em que os bits nascem do 6, `3^2²`, o `×` e `3^2¹` descem juntos para a faixa central, já deixando à direita o lugar do `3^2⁰` — a expressão só sai do lugar quando os bits chegam |
| C4N09 | O último bit está desligado, e portanto, o termo dele nasce apagado. | 5,0 | o `p3` é criado agora, na ponta direita, já esmaecido, puxado do `digs[2]` |
| C4N10 | E aqui está o ponto: cada fator pode ser reduzido módulo sete em paralelo, antes de qualquer multiplicação. | 7,5 | `e1/e2/e3`, e em seguida `bits_cx` + `setas_b` — os três blocos correm emendados, sem pausa |
| C4N11 | No caso do bit desligado, o que avança é o um — o elemento neutro da multiplicação. | 5,8 | `setas` + `res` |
| C4N12 | Só então os três se multiplicam, ainda módulo sete. | 3,8 | `setas2` + `soma` |
| C4N13 | O resultado final é um. | 1,7 | `um` + `eq → eq2` no mesmo bloco |
| C4N14 | Então temos o algoritmo *Square and Multiply*, que eleva ao quadrado e multiplica no lugar de exponenciar. E o custo deixou de ser o tamanho do expoente e agora é o número de bits dele. | 12,9 | realce (seção **Realces**) |
| C4N15 | É essa a operação que o circuito quântico de Shor executa em superposição — o capítulo quatro é, literalmente, o motor do algoritmo. | 8,8 | — |

**Subtotal: 107,5 s** (cartão + 15 locuções)

---

## Capítulo 5 — Inverso multiplicativo modular

*Reescrito no padrão dos capítulos 1–4: a fala diz o movimento geral, os números e as
substituições foram para a coluna **Entra em**, e as filas de teste passaram a correr em
bloco sob uma locução só (o `with narra` envolve o laço inteiro). O capítulo ganhou o quarto elo da
corrente de custo — no 2 cresce o módulo, no 3 o multiplicador, no 4 o expoente, aqui
cresce a busca.*

| Tag | Fala | Est. | Entra em |
|---|---|---|---|
| CAP05 | Com a potência pronta, falta a quarta operação: dividir. | 4,2 | cartão |
| C5N01 | As outras três se construíram repetindo a operação anterior. Com a divisão isso não acontece. | 6,7 | `Write(eq)` |
| C5N02 | Numa reta feita só de inteiros não existe meio número — e sem meio número não existe divisão. | 7,1 | — (a reta do capítulo 1 volta em cena por um instante; nenhum corte cabe entre ela e o `eq`) |
| C5N03 | O que existe é a pergunta invertida: qual número desfaz a multiplicação. É ele que faz o papel da divisão. | 7,9 | `eq → eq2` |
| C5N04 | Ele tem nome: é o inverso multiplicativo. | 3,3 | realce (seção **Realces**) |
| C5N05 | Dá para procurar na mão: testar candidatos, um por um, até algum deixar resto um. | 6,3 | as **três filas** (`2·3`, `2·4`, `2·5`) correm emendadas, sem pausa entre elas — hoje são nove `cena.play` em três iterações; o `with narra` precisa envolver o `for` inteiro, não cada passo. A sobra verde e o ✓ da última fila fecham a linha |
| C5N06 | Cinco é o inverso de dois, módulo nove. | 3,3 | `eq2 → eq3` |
| C5N07 | E vale nos dois sentidos: inverso é sempre um par. Multiplicar por um é dividir pelo outro. | 6,7 | `Write(par)` |
| C5N08 | Só que procurar assim custa o tamanho do módulo. E o módulo, na criptografia, é justamente o número grande da história inteira. | 8,8 | Animação nova, não existe hoje no `capitulo5.py`. É o **quarto elo** da corrente: em "o tamanho do módulo", `Indicate` no nove laranja do `eq`; a reta laranja se estica e as filas vermelhas se multiplicam para baixo, encolhendo de escala até escaparem pela borda inferior do quadro. Mesmo gesto do laço do capítulo 2 e da fila crescente do 3 — aqui quem cresce é a busca |
| C5N09 | Existe um jeito melhor do que testar um a um que é o algoritmo de Euclides estendido, porém não vamos nos aprofundar nele nessa série. | 6,3 | Animação nova. Um exemplo do algoritmo correndo por baixo, **sem que a fala comente nada dele** — a escada de segmentos do capítulo 1: o módulo laranja medido pelo vermelho, a sobra virando a régua do passo seguinte, e assim até o pedaço de tamanho um. Roda rápido e sai. A fala acaba antes da animação; o que resta corre em silêncio |
| C5N10 | Uma pergunta que devemos fazer para essa operação é, o inverso sempre existe? | 7,1 | `eq3 → eq4` |
| C5N11 | Vamos tentar inverter o três módulo nove dessa vez. | 3,8 | as **seis filas** do `for` (`3·1` a `3·6`) correm emendadas, num bloco só — dezoito `cena.play` sob uma locução. O `with narra` envolve o laço inteiro |
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

## Realces — número ou variável nomeado na fala

Regra do vídeo inteiro: **quando a fala nomeia um número ou uma variável que está na tela, a
peça é realçada na palavra.** O gesto é um só, em todos os capítulos:
`Indicate(peça, color=<a cor da própria peça>, scale_factor=1.25)`, `run_time=0.6 * VEL`,
disparado pela âncora (`_ate` de `shor/sincronias.py`, chave `(tag, âncora em pt)`). A cor
é sempre a da peça — o amarelo padrão do `Indicate` é o papel do `x` e não pode aparecer
como destaque genérico.

- **Nascimento conta como realce.** Quando a peça nasce na própria palavra, ela não ganha
  `Indicate` extra; o que muda é o instante do nascimento, que passa a cair na âncora.
- **Todas as cópias juntas.** Quando o mesmo valor está na equação e na reta (o token e a
  barra com o rótulo), as duas realçam no mesmo `play`.
- **O realce corre em paralelo**, nunca empurra a animação da linha para fora da locução. Se
  a âncora cai no meio de outro `play`, o realce entra nele por um `Succession(_ate(…),
  realce)`. Âncora que já passou dispara na hora (o `_ate` nunca é negativo).
- Os `so_fala` das linhas que ganham realce viram `narra`.
- As frações começam estimadas por caracteres (pt e en) e entram em `roteiros/sincronias.md`
  marcadas "a medir na gravação", como as do vídeo 1.

| Tag | Âncora (pt) | Palavra em en | Realça | Observação |
|---|---|---|---|---|
| C1N04 | dois | two | `s2` + `r2` | |
| C1N05 | Dois é | Two is | `eq[0]` nasce de `r2`; `eq[1]`, `eq[3]` e `eq[5]` entram junto | a `eq` deixa de nascer num bloco só: cada número nasce na sua palavra |
| C1N05 | onze | eleven | `eq[2]` nasce de `r11` | |
| C1N05 | três | three | `eq[4]` nasce de `r3s[0]` | |
| C1N06 | onze | Eleven | `r11` + `b11` + `eq[2]` | `so_fala` vira `narra` |
| C1N07 | resto | remainder | `s2` + `r2` | o `b8` segue nascendo no começo, que já cai no "oito" |
| C1N08 | cinco | five | `b5` + `r5` nascem na palavra | em inglês é a última palavra da fala |
| C1N09 | dois | two | `b2` + `r2b` nascem na palavra; `eq[0]` realça junto | |
| C1N10 | três | three | `eq[4]` | antes da cadeia, junto do `FadeOut(eq[0], eq[1])` |
| C1N10 | quatro números | four numbers | `cadeia[0]`, `[2]`, `[4]`, `[6]` com `b11`, `b8`, `b5`, `b2`, em cascata | |
| C2N01 | números | numbers | `eq[2]` + `eq[4]` | |
| C2N01 | resto | remainder | `eq[0]` | |
| C2N03 | um x | x as | `Write(ex0)` começa na palavra | |
| C2N03 | por n | n minus | `ex0[2]` + `n7` + `rn` | |
| C2N03 | menos a | minus a | `ex0[4]` + `a5` + `r5` | |
| C2N03 | Sete | Seven | `ex0[2:] → exf[2:5]` na palavra, `exf[2]` realça | |
| C2N03 | cinco | five | `exf[4]` | |
| C2N03 | a dois | is two | `exf[5]` e `exf[6]` nascem na palavra | |
| C2N03 | traço amarelo | yellow segment | o `Flash(x2)` + `rx → rx2` que já existem, agora na palavra | |
| C2N04 | x é | is x | `tst0[0]` + `x2` | o `Write(tst0)` começa em "comparação" |
| C2N04 | que b | than b | `tst0[2]` + `b6` + `r6` | |
| C2N04 | módulo | modulus | `n7` + `rn` | |
| C2N04 | soma | sum | `b6` + `a5` | |
| C2N05 | resto | remainder | `t2s[0]` + `cver` + `rc` | |
| C2N05 | a b | is b | `t2s[2]` + `b6` + `r6` | |
| C2N05 | menos x | minus x | `t2s[4]` + `x2` + `rx2` | |
| C2N05 | Seis | Six | `t2s[2:] → t2f[2:5]` na palavra | |
| C2N05 | dois | two | `t2f[4]` | |
| C2N05 | quatro | four | `t2f[5]`, `t2f[6]` nascem, com o `Flash` + `rc → rc4` | |
| C2N06 | seis | six | `eq2[2]` | o `eq → eq2` corre no começo |
| C2N06 | cinco | five | `eq2[4]` | |
| C2N06 | quatro | four | `eq2[0]` + `rc4` | |
| C2N06 | sete | seven | `eq2[6]` + `rn` | |
| C2N07 | módulo | modulus | `rn` + `n7` + `eq2[6]` | `so_fala` vira `narra`; o laço mudo segue depois |
| C2N08 | doze | twelve | `ln12` + `eqc[6]` + `fx12[2]` | o salto para n = 12 continua no começo |
| C2N08 | amarelo | yellow | `bx12` + `lx12` | |
| C2N08 | vermelho | red | `b6` + `r6` | |
| C2N08 | teste | test | o `Flash` + `Indicate(tst12[3])` que já existem, agora na palavra | |
| C2N09 | módulo | modulus | `bn12` + `ln12` | |
| C2N09 | resto | remainder | `TransformFromCopy(b6, a5 → bc12)` + `lc12` na palavra | |
| C2N09 | Seis | Six | `f2ab → f2n` na palavra, `f2n[2]` realça | |
| C2N09 | cinco | five | `f2n[4]` | |
| C2N09 | onze | eleven | `f2n[6]` | |
| C2N10 | Onze é | Eleven is | `eqc → eq12`, `Flash(bc12)` e `lc12 → lc11` na palavra | |
| C2N10 | a onze | to eleven | `eq12[2:5]` (o 6 + 5) | |
| C2N10 | doze | twelve | `eq12[6]` + `ln12` | |
| C2N10 | x maior | is x | `tst12[0]` + `bx12` | |
| C2N10 | que b | than b | `tst12[2]` + `b6` | |
| C3N01 | somas sucessivas | repeated addition | os quatro `+` nascem entre os "4" na palavra | |
| C3N02 | vinte | twenty | a fila de cima inteira (blocos, "4" e `+`) | o vinte não está escrito: é o comprimento da fila |
| C3N02 | o sete | seven fits | `baixo[1]`, `baixo[2]`, `rb[1]`, `rb[2]` em cascata | |
| C3N02 | resto | remainder | `baixo[0]` + `rb[0]` | |
| C3N03 | multiplicador | multiplier | o `Indicate(eq[2])` que já existe, agora na palavra | |
| C3N05 | por dois | by two | `d1[0]` + `d2[0]` | |
| C3N06 | juntamos | merge | `grupoA → p1` na palavra | |
| C3N06 | termo que sobrou | leftover term | `d3 → p3` na palavra | |
| C3N07 | potências de dois | powers of two | o `2²` de `p1` e o `2⁰` de `p3` (sem o `· 4`) | |
| C3N07 | multiplicador | multiplier | `eq[2]` (o 5) | em paralelo ao nascimento dos bits |
| C3N08 | bit do meio | middle bit | `digs[1]` | |
| C3N08 | termo dele | its term | `p2` nasce de `digs[1]` na palavra | |
| C3N09 | sete | seven | os três `7` de `e1`, `e2`, `e3` | |
| C3N10 | bit desligado | bit is off | `bits_cx[1]` | |
| C3N10 | zero | zero | `res[1]` | |
| C3N11 | as três | the three | `res`, em cascata | |
| C3N11 | sete | seven | `soma_f[8]` | |
| C3N12 | seis | six | o `seis` nasce na palavra; `eq → eq2` logo depois | |
| C3N13 | multiplicador | multiplier | `eq2[2]` | `so_fala` vira `narra` |
| C3N13 | bits | bits | `bits_cx`, em cascata | |
| C4N02 | setecentos | seven hundred | `segs` (a reta tracejada do resultado) | o número não está escrito: é o comprimento da reta |
| C4N02 | setes | sevens | `baixo[1]`, `baixo[2]`, `rb[1]`, `rb[2]` em cascata | |
| C4N02 | resto | remainder | `baixo[0]` + `rb[0]` | |
| C4N03 | expoente | exponent | o `Indicate(tre[1])` que já existe, agora na palavra | |
| C4N05 | quadrado | squaring | os expoentes `2` de `q1`, `q2`, `q3` | |
| C4N07 | juntamos | merge | `grupoA → p1` e `grupoB → p2` na palavra | |
| C4N07 | potências de dois | powers of two | os expoentes `2²` de `p1` e `2¹` de `p2` | |
| C4N08 | potências de dois | powers of two | os expoentes `2²` de `p1` e `2¹` de `p2` | |
| C4N08 | expoente | exponent | `tre[1]` (o 6) | em paralelo ao nascimento dos bits |
| C4N09 | último bit | last bit | `digs[2]` | |
| C4N09 | termo dele | its term | `p3` nasce de `digs[2]` na palavra | |
| C4N10 | sete | seven | os três `7` de `e1`, `e2`, `e3` | |
| C4N11 | bit desligado | bit is off | `bits_cx[2]` | |
| C4N11 | é o um | is one | `res[2]` | |
| C4N12 | os três | the three | `res`, em cascata | |
| C4N12 | sete | seven | `soma_f[8]` | |
| C4N13 | um | one | o `um` nasce na palavra; `eq → eq2` logo depois | |
| C4N14 | expoente | exponent | `tre2[1]` (o 6 do `eq2`) | `so_fala` vira `narra` |
| C4N14 | bits | bits | `bits_cx`, em cascata | |
| C5N02 | meio número | half a number | `meio` + `rmeio` nascem na palavra (a primeira das duas) | |
| C5N03 | qual número | which number | `eq2[2]` (o x) | |
| C5N04 | inverso | inverse | `eq2[2]` | `so_fala` vira `narra` |
| C5N05 | resto um | is one | o `1` verde, a sobra e o ✓ da última fila nascem na palavra | |
| C5N06 | Cinco | Five | `eq3[2]` | |
| C5N06 | dois | two | `eq3[0]` | |
| C5N06 | nove | nine | `eq3[6]` | |
| C5N08 | módulo | modulus | o `Indicate(eq3[6])` que já existe, na primeira das duas ocorrências | |
| C5N10 | inverso | inverse | `eq4[2]` (o x) | |
| C5N11 | três | three | `eq4[0]` | em paralelo com as filas |
| C5N11 | nove | nine | `eq4[6]` | em paralelo com as filas |
| C5N12 | O um | One is | `eq4[4]` | |
| C5N13 | três | three | `eq4[0]` | |
| C5N13 | nove | nine | `eq4[6]` | |
| C5N14 | módulo | modulus | `mdc3[3]` (o 9) | |
| C5N14 | um fator | a factor | `mdc3[4]` (o "= 3") | |
| C5N15 | módulo | modulus | `como[6]` (o 9) | depois do `Write(como)` |
| C5N17 | dá um | is one | os `circulos` nascem na palavra | |
| C5N17 | linha | row | `inv1[0]` (o a) + `head_l` | |
| C5N17 | coluna | column | `inv1[2]` (o b) + `head_c` | |
| C5N19 | números sem inverso | numbers with no inverse | `m_rot[0]` ("0, 3, 6") + `head_l[0]`, `[3]`, `[6]` | |
| C5N20 | módulo | modulus | `c1[3]` (o 9) | |

**Ficam sem realce**, porque o que a fala nomeia não é um número nem uma variável em cena:
contagens ("duas subtrações e uma comparação" no `C2N06`, "as outras três" no `C5N01`),
operações (`C1N11`, `C2N02`, `C3N04`, `C4N04`, `C4N06`), números de capítulo e de vídeo
(`C4N15`, `V2N01`), o "um" pronome do `C5N07`, o "um" do `C5N19` (o ponto ali é a ausência
dele nas linhas) e o encerramento `V2N00`.

---

## Projeção de duração

| Bloco | Locuções | Fala |
|---|---|---|
| Cartão de abertura | — | — |
| Capítulo 1 | 12 | 59,8 s |
| Capítulo 2 | 12 | 89,7 s |
| Capítulo 3 | 14 | 90,8 s |
| Capítulo 4 | 16 | 107,5 s |
| Capítulo 5 | 21 | 132,4 s |
| Encerramento | 2 | 19,6 s |
| **Total** | **77** | **499,8 s** |

Somando o `PAD` de 0,35 s por locução (27,0 s), os dois cartões silenciosos (~7 s) e os
`limpar()` entre capítulos (~20 s), a projeção é de **cerca de 9 min 15 s**. O capítulo 5
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
- [ ] Capítulo 3 — C3N01 a C3N13 *(regravar `C3N06`, texto novo; renomear os áudios `C3N12`–`C3N14` para `C3N11`–`C3N13`)*
- [ ] Capítulo 4 — C4N01 a C4N15 *(regravar `C4N07`, texto novo; renomear os áudios `C4N13`–`C4N16` para `C4N12`–`C4N15`)*
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
