# Script — Video 2: Modular arithmetic, the four operations (English)

Tradução de `roteiros/pt/roteiro_video2_aritmetica_modular.md`. Mesmas tags, mesma ordem; a
coluna "Entra em" é a do português, porque a animação é a mesma. Termos:
`roteiros/glossario.md`. Est. a 2,6 palavras/s até haver gravação em inglês.

Capítulos 1 a 5, na ordem de montagem.

---

## Abertura

Sem narração. O vídeo entra direto pelo cartão e cai no capítulo 1.

| Tag | Speech | Est. | Entra em |
|---|---|---|---|
| — | *(cartão silencioso, ~4 s)* | — | "Do Zero ao Algoritmo de Shor Quântico" nasce no centro e "Vídeo 2 de 4 — Aritmética modular" embaixo dele. O subtítulo sai primeiro e o título encolhe e some por último, já com o `CAP01` entrando por baixo — os dois cartões precisam se emendar num movimento só, senão a sequência lê como dois começos |

**Subtotal: ~4 s** (nenhuma locução)

---

## Capítulo 1 — Aritmética modular na reta segmentada

| Tag | Speech | Est. | Entra em |
|---|---|---|---|
| CAP01 | We start with the simplest object in the whole construction: the modulus. | 4,6 | cartão |
| C1N01 | Everything that follows happens in modular arithmetic. | 2,7 | `Create(reta)` |
| C1N02 | The visual language of this video will treat numbers as lengths on a line. | 5,4 | `Create(b11)` |
| C1N03 | Working modulo a number means keeping only the remainder of integer division. | 4,6 | Todo o encaixe corre por baixo desta linha, sem pausa entre as etapas: os três blocos laranja nascem em cadeia da direita para a esquerda (`LaggedStart`), o quarto (`tenta`) avança e estoura o zero, e fecha com `Flash` + ✗ + `Wiggle` |
| C1N04 | That's the remainder: two. | 1,5 | `tenta → s2` |
| C1N05 | Two is congruent to eleven, modulo three. And the congruence sign, unlike the equals sign, tells us we're talking about classes, not individual numbers. | 9,2 | equação nasce |
| C1N06 | Eleven isn't the only member of this class. | 3,1 | — |
| C1N07 | Eight leaves the same remainder. | 1,9 | `b8` |
| C1N08 | So does five. | 1,2 | `b5` |
| C1N09 | And two is the representative itself. | 2,3 | `b2` |
| C1N10 | Modulo three, these four numbers are equivalent. That's what makes modular arithmetic work: sums, products and powers are all well defined on the classes. | 9,2 | cadeia |
| C1N11 | The next chapters are exactly that: sum, product and power — and, at the end, a way to divide. | 7,3 | — |

**Subtotal: 53,0 s** (cartão + 11 locuções)

---

## Capítulo 2 — Adição modular

| Tag | Speech | Est. | Entra em |
|---|---|---|---|
| CAP02 | With the modulus defined, the first operation is modular addition. | 3,8 | cartão |
| C2N01 | We could simply add the numbers and take the remainder of the division. But division in a quantum circuit is very expensive. | 8,5 | `Write(eq)` + `Create(reta)` |
| C2N02 | So we'll reach the same result using only comparisons, subtractions and additions. | 4,6 | as duas parcelas, o módulo medido da ponta direita para trás com o `x2` amarelo nascendo, e o verde desconhecido — `b6`, `a5`, `n7` + `x2`, rótulos e `cver` correndo emendados, sem pausa |
| C2N03 | To do that, we define x as n minus a. Seven minus five is two — shown by the yellow segment. | 8,1 | `Write(ex0)` → `exf` → `rx → rx2` |
| C2N04 | Then comes the comparison: is x greater than b? We can see it isn't — the modulus fit entirely inside the sum. | 8,5 | `Write(tst0)` → `tst` → ✗ |
| C2N05 | So the remainder is b minus x. Six minus two is four. | 4,6 | `Write(t2s)` → `t2f` → `rc → rc4` |
| C2N06 | Therefore six plus five is congruent to four, modulo seven. We did two subtractions and one comparison. No division. | 7,3 | `eq → eq2` |
| C2N07 | Now let's see what happens as the modulus grows. At eight, the orange segment moves forward, the yellow one moves with it, the green one shrinks, and so on. | 11,2 | n = 8, 9, 10 e 11 — os quatro `ReplacementTransform` do laço correm num bloco só |
| C2N08 | At twelve, something different happens: the yellow overtakes the red, and the test comes out true. | 6,2 | n = 12 + `Indicate(tst12)` |
| C2N09 | This time the modulus doesn't fit inside the sum, so the remainder is the sum itself. Six plus five, eleven. | 7,7 | `Write(f2ab)` → `bc12` → `f2n` |
| C2N10 | Eleven is congruent to eleven, modulo twelve. And it's the test "is x greater than b" that decides between the two cases, still without any division. | 10,0 | `eqc → eq12` |
| C2N11 | Keep the pattern in mind: compare and subtract instead of dividing. | 4,2 | — |

**Subtotal: 84,7 s** (cartão + 11 locuções)

---

## Capítulo 3 — Multiplicação modular (*Double and Add*)

| Tag | Speech | Est. | Entra em |
|---|---|---|---|
| CAP03 | With addition done, the second operation is modular multiplication. | 3,5 | cartão |
| C3N01 | Multiplication can be represented as repeated addition. | 2,7 | `Write(eq)` e os cinco blocos "4" nascendo em cadeia correm emendados, num bloco só |
| C3N02 | Unreduced, the product is twenty: seven fits in twice, and what's left over is the remainder. | 6,2 | `baixo` + `rb` |
| C3N03 | But the cost of this approach grows with the size of the multiplier. When it gets very large, so does the number of additions, which is computationally expensive. | 10,8 | Animação nova, não existe hoje no `capitulo3.py`. Em "o tamanho do multiplicador", `Indicate` no cinco vermelho do `eq`. Em "quando ele fica muito grande", o valor do multiplicador cresce em cena e a fila de blocos "4" se multiplica junto, encolhendo de escala até escapar pelas bordas do quadro; os blocos de sete da linha de baixo se multiplicam no mesmo movimento. É o eco do laço de módulos crescentes do capítulo 2 — quem cresce lá é o módulo, aqui é o multiplicador |
| C3N04 | The way out is to regroup the terms into pairs, pairs of pairs, and so on. | 6,2 | Animação nova. Nada desce para uma segunda linha: os agrupamentos nascem em volta dos próprios "4" azuis, sobre a reta. Em "duplas", os parênteses abraçam o 1º com o 2º e o 3º com o 4º; em "duplas de duplas", os colchetes fecham os dois parênteses; em "até sobrar o que não fecha dupla", o quinto "4" fica sozinho, sem nada em volta. Saem do capítulo o `toks`, os `fios` e a cópia para baixo. A saída de `baixo`/`rb` corre no começo desta linha |
| C3N05 | That lets us simplify inside each group. Adding twice becomes multiplying by two — which is where the *double* in the name comes from. | 9,2 | Nos dois parênteses, `4 + 4` vira `2 · 4`; o quinto "4" ganha coeficiente e vira `1 · 4`. Tudo ainda em cima da reta, com os colchetes intactos |
| C3N06 | And again, one level up. | 1,9 | `[2·4 + 2·4] → 2²·4` e `1·4 → 2⁰·4`; `segs` e `rots` saem quando os dois termos se condensam. Só esses dois ficam em cena — o `2¹·4` ainda não existe |
| C3N07 | These powers of two correspond to the bits of the multiplier. | 4,2 | `origina_binario`, que passa a acontecer **depois** das potências e não antes |
| C3N08 | The middle bit is off, so its term shows up faded. | 4,2 | o `p2` é criado agora, entre os dois, já esmaecido, puxado do `digs[1]` |
| C3N09 | And here's the point: each term can be reduced modulo seven in parallel, before any addition. | 6,2 | `e1/e2/e3`, e em seguida `bits_cx` + `setas_b` — os três blocos correm emendados, sem pausa |
| C3N10 | Where the bit is off, what moves on is zero — the identity element of addition. | 6,2 | `setas` + `res` |
| C3N11 | As you can see, none of these boxes went past sixteen. | 4,2 | — |
| C3N12 | Only then are the three added, still modulo seven. | 3,5 | `setas2` + `soma` |
| C3N13 | The final result is six. | 1,9 | `seis` + `eq → eq2` no mesmo bloco |
| C3N14 | So we have the *Double and Add* algorithm, which doubles and adds instead of multiplying. And the cost is no longer the size of the multiplier, but the number of bits in it. | 12,7 | — |

**Subtotal: 83,6 s** (cartão + 14 locuções)

---

## Capítulo 4 — Exponenciação modular (*Square and Multiply*)

| Tag | Speech | Est. | Entra em |
|---|---|---|---|
| CAP04 | With the product done, the third operation is modular exponentiation. | 3,8 | cartão |
| C4N01 | A power can be represented as repeated multiplication. | 3,1 | `Write(eq)` e os seis "3" nascendo em cadeia correm emendados, num bloco só |
| C4N02 | Unreduced, the power is seven hundred twenty-nine: lots of sevens fit in there, and what's left over is the remainder. | 7,7 | `segs` e, emendado, `baixo` + `rb` |
| C4N03 | But here the growth is of a different kind: each step in the exponent multiplies the entire result. With the exponents used in cryptography, it wouldn't fit in the observable universe. | 11,9 | Animação nova, não existe hoje no `capitulo4.py`. Em "cada passo no expoente", `Indicate` no seis vermelho do `eq`; o valor do expoente cresce em cena e a corrente de trêses cresce junto, encolhendo de escala. A diferença com o capítulo 3 é o ponto da linha: lá a fila cresce **proporcional**, aqui a fila cresce devagar e é a **reta tracejada do resultado** que estoura, esticando para fora dos dois lados do quadro e engolindo o "…". É o terceiro elo da mesma corrente — no capítulo 2 cresce o módulo, no 3 o multiplicador, aqui o expoente |
| C4N04 | The way out is the same move as in the previous chapter: regroup the factors into pairs, and pairs of pairs. | 8,1 | Animação nova. Nada desce para uma segunda linha: os agrupamentos nascem em volta dos próprios "3" da corrente. Em "duplas", os parênteses abraçam o 1º com o 2º, o 3º com o 4º e o 5º com o 6º; em "duplas de duplas", os colchetes fecham os dois primeiros parênteses e o terceiro par fica sozinho no colchete dele. Saem do capítulo o `toks`, os `fios` e a cópia para baixo. A saída de `segs`, `baixo` e `rb` corre no começo desta linha |
| C4N05 | That lets us simplify inside each group. Multiplying twice becomes squaring — which is where the *square* in the name comes from. | 8,5 | Nos três parênteses, `3 × 3` vira `3²`. Tudo ainda no lugar, com os colchetes intactos |
| C4N06 | So we've climbed one step: repeated additions give the product, repeated products give the power. | 5,8 | — |
| C4N07 | And again, one level up. | 1,9 | `[3² × 3²] → 3^2²` e `[3²] → 3^2¹`; a corrente antiga sai quando os dois termos se condensam, e a expressão desce para a faixa central para abrir espaço aos bits. Só esses dois ficam em cena — o `3^2⁰` ainda não existe |
| C4N08 | These powers of two correspond to the bits of the exponent. | 4,2 | `origina_binario`, que passa a acontecer **depois** das potências e não antes |
| C4N09 | The last bit is off, so its term shows up faded. | 4,2 | o `p3` é criado agora, na ponta direita, já esmaecido, puxado do `digs[2]` |
| C4N10 | And here's the point: each factor can be reduced modulo seven in parallel, before any multiplication. | 6,2 | `e1/e2/e3`, e em seguida `bits_cx` + `setas_b` — os três blocos correm emendados, sem pausa |
| C4N11 | Where the bit is off, what moves on is one — the identity element of multiplication. | 6,2 | `setas` + `res` |
| C4N12 | As you can see, none of these boxes went past eighty-one. | 4,2 | — |
| C4N13 | Only then are the three multiplied, still modulo seven. | 3,5 | `setas2` + `soma` |
| C4N14 | The final result is one. | 1,9 | `um` + `eq → eq2` no mesmo bloco |
| C4N15 | So we have the *Square and Multiply* algorithm, which squares and multiplies instead of exponentiating. And the cost is no longer the size of the exponent, but the number of bits in it. | 12,7 | — |
| C4N16 | This is the operation that Shor's quantum circuit runs in superposition — chapter four is, literally, the engine of the algorithm. | 8,1 | — |

**Subtotal: 102,0 s** (cartão + 16 locuções)

---

## Capítulo 5 — Inverso multiplicativo modular


| Tag | Speech | Est. | Entra em |
|---|---|---|---|
| CAP05 | With the power done, one operation is left: division. | 3,5 | cartão |
| C5N01 | The other three were built by repeating the previous operation. Division doesn't work that way. | 5,8 | `Write(eq)` |
| C5N02 | On a line made only of integers, there's no such thing as half a number — and without half a number there's no division. | 9,2 | — (a reta do capítulo 1 volta em cena por um instante; nenhum corte cabe entre ela e o `eq`) |
| C5N03 | What we can do is flip the question around: which number undoes the multiplication? That number plays the role of division. | 8,1 | `eq → eq2` |
| C5N04 | It has a name: the multiplicative inverse. | 2,7 | — |
| C5N05 | We can search by hand: try candidates one at a time until the remainder is one. | 6,2 | as **três filas** (`2·3`, `2·4`, `2·5`) correm emendadas, sem pausa entre elas — hoje são nove `cena.play` em três iterações; o `with narra` precisa envolver o `for` inteiro, não cada passo. A sobra verde e o ✓ da última fila fecham a linha |
| C5N06 | Five is the inverse of two, modulo nine. | 3,1 | `eq2 → eq3` |
| C5N07 | And it works both ways: inverses always come in pairs. Multiplying by either one is dividing by the other. | 7,3 | `Write(par)` |
| C5N08 | But the cost of searching like this grows with the modulus. And in cryptography, the modulus is exactly the huge number at the heart of the whole story. | 10,8 | Animação nova, não existe hoje no `capitulo5.py`. É o **quarto elo** da corrente: em "o tamanho do módulo", `Indicate` no nove laranja do `eq`; a reta laranja se estica e as filas vermelhas se multiplicam para baixo, encolhendo de escala até escaparem pela borda inferior do quadro. Mesmo gesto do laço do capítulo 2 e da fila crescente do 3 — aqui quem cresce é a busca |
| C5N09 | There's a better way than testing one by one, the extended Euclidean algorithm, but we won't go into it in this series. | 8,5 | Animação nova. Um exemplo do algoritmo correndo por baixo, **sem que a fala comente nada dele** — a escada de segmentos do capítulo 1: o módulo laranja medido pelo vermelho, a sobra virando a régua do passo seguinte, e assim até o pedaço de tamanho um. Roda rápido e sai. A fala acaba antes da animação; o que resta corre em silêncio |
| C5N10 | One question we should ask about this operation: does the inverse always exist? | 5,0 | `eq3 → eq4` |
| C5N11 | Let's try to invert three modulo nine this time. | 3,5 | as **seis filas** do `for` (`3·1` a `3·6`) correm emendadas, num bloco só — dezoito `cena.play` sob uma locução. Mesma correção do `C2N07`: o `with narra` envolve o laço inteiro |
| C5N12 | The remainders form a closed cycle and keep coming back to the start, forever. One is never in it. | 7,3 | `ciclo` |
| C5N13 | Dividing by three modulo nine is an operation that simply doesn't exist. | 4,6 | `FadeIn(xis)` — separado do `Write(mdc3)`, que hoje roda no mesmo `play` |
| C5N14 | And the reason fits in one line: it shares a factor with the modulus. | 5,4 | `Write(mdc3)` |
| C5N15 | It's worth seeing the whole thing at once: every possible multiplication within this modulus, in a single table. | 6,9 | `titulo_tab` + cabeçalhos + eixos e, emendado, `Write(como)` — o `como` sai de dentro do bloco do `Indicate` e acontece antes dele |
| C5N16 | The pair we found on the number lines is in here, and the other cells follow the same rule. | 7,3 | `Indicate` dos cabeçalhos + `ex25`, a célula nascendo da equação e o `LaggedStart(demais)` correm emendados, num bloco só |
| C5N17 | Now the whole table can be read with a single rule: wherever a cell is one, its row and column are inverses. Each green circle is a division that exists. | 11,5 | `circulos` + `inv1`, depois `inv2` |
| C5N18 | Our pair shows up twice, mirrored across the diagonal. | 3,5 | `rec1` + `Indicate` nas duas células |
| C5N19 | Just like when we tested by hand, cycles that never pass through one show up. Those rows and columns are the numbers with no inverse. | 9,6 | `mortos` (opacidade cai + retângulos vermelhos) + `m_rot` e, emendado, `rec2` + `Indicate(mortos[1])` — os dois blocos correm sob esta linha |
| C5N20 | And the criterion is the same as at the start: only numbers that share no factor with the modulus have an inverse. | 8,5 | `concl` + `caixa` |

**Subtotal: 138,3 s** (cartão + 20 locuções)

---

## Encerramento

| Tag | Speech | Est. | Entra em |
|---|---|---|---|
| V2N00 | That completes the set. One modulus, and on top of it the four operations: adding, multiplying, raising to a power and dividing — all without ever doing a division. | 11,2 | Os quatro símbolos `+`, `×`, `xⁿ` e `÷` entram em fila, um a cada operação nomeada. Em "sem nunca fazer uma divisão", o `÷` é **riscado** e o `a⁻¹` nasce ao lado — o risco não sai, porque a divisão continua não existindo |
| V2N01 | Video three takes these four operations and builds RSA out of them — the cryptography that protects the internet today. | 7,7 | Os quatro símbolos saem e o cadeado do vídeo 1 reaparece no centro, **fechado e intacto** |
| — | *(cartão final, ~3 s)* | — | "Vídeo 3 de 4 — Do teorema ao RSA" |

**Subtotal: 18,9 s** (2 locuções) + cartão ~3 s

---

## Projeção de duração

| Bloco | Locuções | Fala |
|---|---|---|
| Cartão de abertura | — | — |
| Capítulo 1 | 12 | 53,0 s |
| Capítulo 2 | 12 | 84,7 s |
| Capítulo 3 | 15 | 83,6 s |
| Capítulo 4 | 17 | 102,0 s |
| Capítulo 5 | 21 | 138,3 s |
| Encerramento | 2 | 18,9 s |
| **Total** | **79** | **480,5 s** |

Somando o `PAD` de 0,35 s por locução (27,6 s), os dois cartões silenciosos (~7 s) e os `limpar()` entre capítulos (~20 s), a projeção é de **cerca de 8 min 55 s**. Como no português, `C5N05` e `C5N09` têm animação mais longa que a fala e somam uns 6 a 8 s ao render real.

---

## Checklist de gravação

- [ ] Cartões — CAP01 a CAP05
- [ ] Capítulo 1 — C1N01 a C1N11
- [ ] Capítulo 2 — C2N01 a C2N11
- [ ] Capítulo 3 — C3N01 a C3N14
- [ ] Capítulo 4 — C4N01 a C4N16
- [ ] Capítulo 5 — C5N01 a C5N20
- [ ] Encerramento — V2N00 e V2N01
- [ ] `python medir.py en`
- [ ] Render de conferência: `IDIOMA=en manim -pqh --media_dir media/en filme_shor.py VideoOperacoes`
