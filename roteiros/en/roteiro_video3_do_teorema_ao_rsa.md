# Script — Video 3: From theorem to RSA (English)

Tradução de `roteiros/pt/roteiro_video3_do_teorema_ao_rsa.md`. Mesmas tags, mesma ordem; a
coluna "Entra em" é a do português, porque a animação é a mesma. Termos:
`roteiros/glossario.md`. Est. a 2,6 palavras/s até haver gravação em inglês.

Capítulos 6 a 8, na ordem de montagem.

---

## Abertura

| Tag | Speech | Est. | Entra em |
|---|---|---|---|
| — | *(cartão silencioso, ~4 s)* | — | "Do Zero ao Algoritmo de Shor Quântico" nasce no centro e "Vídeo 3 de 4 — Do teorema ao RSA" embaixo dele. Mesma emenda do vídeo 2: o subtítulo sai primeiro e o título encolhe por último, já com o `CAP06` entrando por baixo |
| V3N00 | The previous video built four operations on top of a modulus. This one uses them to build RSA — by way of two theorems. | 9,2 | Os quatro símbolos do `V2N00` voltam em fila, acesos. Em "constrói com elas o RSA", eles se fecham em volta do cadeado do vídeo 1, que entra no centro **intacto**. Em "dois teoremas", duas lacunas vazias se abrem entre a fila e o cadeado — os lugares que os capítulos 6 e 7 vão ocupar |

**Subtotal: 9,2 s** (1 locução) + cartão ~4 s

---

## Capítulo 6 — Pequeno Teorema de Fermat

| Tag | Speech | Est. | Entra em |
|---|---|---|---|
| CAP06 | With the four operations in place, it's time for the series' first theorem. | 5,0 | cartão |
| C6N01 | This is the same table shown in the previous chapter, now with modulus seven. | 5,4 | `head_c` + `head_l` + `lin_h` + `lin_v` e o `LaggedStart(linhas_cel)` correm emendados, num bloco só |
| C6N02 | Notice that the first row is all the possible nonzero remainders of division by seven. | 5,8 | `Create(el1)` e o `TransformFromCopy(linhas_cel[0] → A)` emendados |
| C6N03 | Now we multiply each of them by the same number, any number. | 4,6 | `prods` — cada `3·j` nascendo do vermelho de `head_l[2]` e do próprio `A[j]` |
| C6N04 | And we reduce each product modulo seven. | 2,7 | `FadeIn(mod_rot)` + `TransformFromCopy(prods → B)` |
| C6N05 | The result is the same as the row of the multiplier we used. | 5,0 | `Create(el3)` + `Indicate(head_l[2])`, as `copias` caindo exatamente em cima de `B`, e o `FadeOut(copias)` + `Indicate(B)` — os três `play` num bloco só |
| C6N06 | The numbers are the same, just in a different order. And that holds for any multiplier: it only reorders the row. | 8,1 | `LaggedStart(Create(arcos))` |
| C6N07 | Since order doesn't matter in multiplication, we can write the following congruence. | 4,6 | `eq0` e, emendados, o `FadeIn(nota)` com o `ReplacementTransform(eq0 → eq)`; a `nota` sai no mesmo movimento |
| C6N08 | As we saw in the previous chapter, remainders that share no factor with the modulus have an inverse. | 6,9 | `FadeIn(nota2)` |
| C6N09 | Since the modulus is prime, every factor in this list has an inverse: we can divide both sides by the whole product and simplify. | 9,2 | `Write(div_e)` + `Write(div_d)` |
| C6N10 | What's left is a power congruent to one, modulo seven. | 3,8 | `resultado` |
| C6N11 | When the modulus is prime, this congruence generalizes to any value a that isn't zero or a multiple of the modulus. | 8,1 | `Write(geral)`, ainda no rodapé ([0, −3,35, 0]) e no tamanho de hoje |
| C6N12 | This is Fermat's little theorem. | 1,9 | **A virada.** Um `play` só: a tabela inteira, `el1`, `el3`, `A`, `B`, `prods`, `mod_rot` e `arcos` saem em `FadeOut`, e **no mesmo bloco** o `geral` sobe para [0, −0,5, 0] e cresce de 28 para 40 — ele não é reposicionado depois da limpeza, ele **sobrevive** a ela. O `resultado` sai meio segundo atrasado em relação ao resto (`lag_ratio` ou `FadeOut` próprio), para que o caso particular seja a última coisa a desaparecer debaixo do geral. Fechando o bloco, `titulo = T("Pequeno Teorema de Fermat", 40)` nasce em [0, 0,9, 0] por `Write` |
| C6N13 | Notice the condition: the modulus has to be prime. That's what breaks in the next chapter. | 6,2 | Título e equação parados em cena. Em "precisa ser primo", `Indicate` no `(n primo)` cinza que o `geral` já carrega |

**Subtotal: 77,3 s** (cartão + 13 locuções)

---

## Capítulo 7 — A generalização de Euler: φ(n)

| Tag | Speech | Est. | Entra em |
|---|---|---|---|
| CAP07 | Euler's theorem is a generalization of the theorem from the previous chapter. | 4,6 | cartão |
| C7N01 | Let's try the same steps, but now with the table for modulus nine, which isn't prime. | 6,2 | headers + `linhas_cel` num bloco só |
| C7N02 | We pick a multiplier for the list of remainders. | 3,5 | `Create(el2)` + `Indicate(head_l[1])` emendados com `Write(eq)` |
| C7N03 | And here comes the step that made Fermat work: canceling the list on both sides. | 5,8 | `Write(div_e)` + `Write(div_d)` |
| C7N04 | But canceling is multiplying by the inverse, and two of these factors have no inverse, because they share a factor with the modulus. | 8,8 | `FadeIn(exp1)` + `Write(exp2)` emendados |
| C7N05 | They're exactly the rows that chapter five had already marked as dead. So the cancellation isn't allowed, and the congruence fails. | 8,1 | as linhas 3 e 6 apagando + os `Indicate`, o `Wiggle` e o `Transform(eq[1] → neq)` — os três `play` num bloco só |
| C7N06 | Euler's way out is simply to leave out the numbers that have no inverse. | 5,4 | `Create(cruzes)` + `Create(cruzes_eq)` + saída de `exp1`/`exp2` |
| C7N07 | That leaves only the numbers that share no factor with the modulus. | 4,6 | `FadeIn(sobr)` — `play` próprio |
| C7N08 | And how many there are is given by Euler's totient function, written phi of n. | 5,8 | `Write(phi)` — `play` próprio. É aqui, e só aqui, que o símbolo ganha nome falado: o capítulo 8 diz "fi de ene" sete vezes e depende desta emenda |
| C7N09 | With the new list, we run the same computation again. | 3,8 | `ReplacementTransform(eq → eq2)` + `FadeOut(cruzes_eq)` |
| C7N10 | Now every factor has an inverse, and the cancellation is legitimate. | 4,2 | `div2_e` + `div2_d` |
| C7N11 | Once again what's left is a power congruent to one, this time modulo nine. | 5,4 | `res` |
| C7N12 | It holds for any modulus, and the exponent is no longer the modulus minus one: now it's the totient function. | 7,7 | `Write(geral)`, ainda no rodapé e no tamanho de hoje. **Sem** o `Create(caixa)` |
| C7N13 | This is Euler's theorem. | 1,5 | **A virada, espelhando o `C6N12`.** Um `play` só: `head_c`, `head_l`, `lin_h`, `lin_v`, `linhas_cel`, `el2`, `cruzes`, `sobr`, `phi`, `eq2`, `div2_e` e `div2_d` saem em `FadeOut`, e no mesmo bloco o `geral` sobe para [0, −0,5, 0] e cresce de 28 para 40. O `res` sai meio segundo atrasado, como o `resultado` no capítulo 6. Fechando, `titulo = T("Teorema de Euler", 40)` nasce em [0, 0,9, 0] por `Write` |
| C7N14 | Keep this formula in mind: the whole next chapter is built on it. | 5,0 | Título e equação parados em cena. Em "sai inteiro dela", `Indicate` no `φ(n)` do expoente — é exatamente a peça que o capítulo 8 vai consumir |

**Subtotal: 80,4 s** (cartão + 14 locuções)

---

## Capítulo 8 — O algoritmo RSA

O capítulo mais longo do vídeo, e o único com quatro fases. O **objetivo**
(`C8N01`–`C8N10`) abre o capítulo antes de qualquer fórmula e é a única fase inteiramente
figurativa da série: canal, cadeado e chaves, sem uma equação em cena. Ele roda **duas
vezes o mesmo trajeto** — primeiro com uma chave só, que falha (`C8N01`–`C8N04`), depois
com o par do RSA, que resiste (`C8N05`–`C8N10`). O enquadramento é idêntico nas duas
voltas de propósito: o que muda é só quem consegue abrir a caixa no fim. A **dedução**
(`C8N11`–`C8N19`) é onde a fala trabalha: é o
trecho conceitualmente difícil da série inteira, e ganha as únicas linhas longas do
capítulo. O **esquema simbólico** (`C8N20`–`C8N25`) nomeia as peças em frases curtas — e
é onde os dois cartões vazios da fase 0 finalmente se preenchem. O **exemplo numérico**
(`C8N26`–`C8N35`) roda quase em silêncio — a tela já está fazendo todas as contas, e ler
número por número seria legenda. O fecho (`C8N36`–`C8N44`) abre com a pergunta que a fase 0 deixou em aberto — se os dois
expoentes são inversos um do outro, por que a privada não sai da pública? — e é onde mora
a explicação da escolha do módulo: as quatro fórmulas do `parte8` já estavam na tela, mas a fala passava
por elas sem dizer por que valem. Agora ela diz — inclusive que fi de ene é uma contagem,
que é o fato de onde a dificuldade inteira vem e que o capítulo 7 define sem nomear.

| Tag | Speech | Est. | Entra em |
|---|---|---|---|
| CAP08 | With both theorems ready, it's time to see what RSA needs to solve. | 5,0 | cartão |
| C8N01 | The problem RSA solves starts with two people who have never met and need to exchange a message over a public channel. | 8,5 | `FadeIn(p['cenario'])` + `FadeIn(olho)` emendados — a `DashedLine` cinza com as duas pontas e os rótulos "quem envia"/"canal público"/"quem recebe" nasce junto com o olho vermelho, achatado e fechado. Depois `FadeIn(caixa)`, a caixa `SEGREDO` legível subindo de baixo. Por fim `atravessar(caixa, RIGHT)`: desliza até o centro e dali até a ponta direita — no meio do caminho uma cópia sobe até a prateleira (vaga 0) e, por ser a primeira captura, o olho se abre e a `prat` nasce por `Create`, tudo dentro dos dois `play` da própria função |
| C8N02 | Using symmetric-key encryption solves half the problem: the message in transit stops making sense to outsiders. | 6,2 | `FadeOut(caixa)` + `esvaziar()` da prateleira + `FadeIn(pacote[0])` emendados — a caixa legível dá lugar à caixa-pacote vazia. Depois `FadeIn(chave, shift=DOWN)` + `FadeIn(pacote[1])`, o cadeado aberto, emendados. Em seguida `trancar(pacote, ...)`: um único `play` gira o arco, dispara o `Flash` seco, embaralha as sete letras (`SEGREDO → Xk9#R2q`) e vira o fundo verde. Depois `atravessar(pacote, RIGHT)` (dois `play`) e, por fim, `FadeIn(xis)` sozinho |
| C8N03 | But whoever locks the message and whoever opens it use the same key, and that key has to cross the channel too. | 8,5 | `chave.animate.move_to(canal)` sozinho, descendo até a linha. Depois `atravessar(chave, RIGHT, vaga=1)` (dois `play`), parando antes da ponta — a cifra já ocupa a marca. Por fim `chave.animate.move_to(...)`, descendo até o ponto médio entre as duas marcas onde o par do `C8N05` vai pousar |
| C8N04 | An intruder listening on the channel grabs both together, and opens the message with the very key that locked it. | 7,7 | `Indicate(prateleira[1], color=AMARELO)` sozinho — os dois objetos capturados, juntos, na prateleira. Depois a chave sobe até ficar ao lado do cadeado capturado (`prateleira[1].animate.next_to(...)`), `abrir(prateleira[0], ...)` destrava e desembaralha as letras num `play` só, a chave volta para a vaga, `FadeOut(xis)` e, fechando, `piscar(VERMELHO)` (dois `play`: preenche e some) |
| C8N05 | RSA is one way out of this: it uses two different keys, one that locks and another that opens. | 7,3 | `FadeOut` do que restou na prateleira e do pacote, sozinho. Depois `Indicate(chave, color=AMARELO)`. Por fim, num único `play`, a chave amarela vira duas cópias e cada uma sofre `ReplacementTransform`: uma para `ch_pub` (chave cinza) e outra para `ch_priv` (chave amarela) — ela se parte em duas **chaves**, não em cartões. São essas duas chaves, não retângulos vazios, que voltam para virar os cartões `(e, n)` e `(d, n)` no `C8N22` e no `C8N24` |
| C8N06 | The receiver sends their locking key over the channel. Anyone can see it, because all it can do is lock, which is why it's called the public key. | 10,8 | `ch_pub.animate.move_to(canal)` sozinho. Depois `atravessar(ch_pub, LEFT)` — dois `play`, o único percurso da fase 0 no sentido contrário, e mais lento (`rt=2.8`) que qualquer outro. Por fim `ch_pub.animate.move_to(...)`, pousando na ponta esquerda |
| C8N07 | The sender locks the message with it — and not even the sender can undo that. The key that locks doesn't unlock. | 8,5 | `FadeIn(pacote[0])` + `FadeIn(pacote[1])` emendados — a caixa e o cadeado aberto nascem na ponta esquerda. `ch_pub.animate.move_to(mão)` sozinho, depois `trancar(pacote, ...)` num `play`. Em seguida o arco tenta ceder no sentido de abrir e volta, em dois `Rotate` opostos e curtos — a chave cinza tentando voltar atrás. Fechando, `Wiggle(pacote[1])` + `FadeIn(x2)` emendados e, por fim, `FadeOut(x2)` sozinho: quem trancou também ficou de fora |
| C8N08 | The intruder grabs everything that crossed the channel, the public key and the locked message, and none of it is enough to open it. | 9,2 | `atravessar(pacote, RIGHT)` (dois `play`) — a mesma vaga do `C8N04`. Depois `Indicate(prateleira[1], color=CINZA)` sozinho. Por fim `Wiggle(prateleira[0][1])` + `FadeIn(xis)` emendados: o intruso aplica a chave cinza, o cadeado chacoalha e não abre |
| C8N09 | The key that opens never enters the channel, which is why it's also called the private key. | 6,5 | `Indicate(ch_priv, color=AMARELO)` sozinho — ela está parada na ponta direita desde o `C8N05` e nunca se moveu. Depois `ch_priv.animate.move_to(mão)`, `abrir(pacote, ...)` num `play` (letras desembaralham, `SEGREDO` reaparece legível) e, fechando, `piscar(VERDE)` (dois `play`) |
| C8N10 | In arithmetic, this is a pair of operations: one that anyone can do, and its reverse, which no one can do without a piece of information the first one doesn't give away. | 12,3 | Um `play` só apaga o pacote, a prateleira e o `prat`, some com o `xis`, e ao mesmo tempo o `olho`, `ch_pub` e `ch_priv` caem para opacidade 0,3 e voltam para as marcas de pouso, nas duas pontas. Depois `GrowArrow(ida)` verde sozinho, `GrowArrow(volta)` vermelha sozinha — o mesmo gesto do `V1N01` — e por fim `LaggedStart(FadeIn(cacos))`, os "?" que despedaçam a seta de volta. É a promessa que o `C8N36` vai cobrar |
| C8N11 | Let's start from Euler's theorem and show how these operations come out of it. For that, we'll do a bit of algebra on the congruence. | 9,6 | `ReplacementTransform(fase0['ida'] → L)` — o `L` nasce de dentro da seta verde —, emendado com o `FadeOut` do `cenario`, do `olho`, da seta despedaçada (`fase0['volta']`) e das duas chaves (`fase0['pub']`, `fase0['priv']`), tudo num só `play`. Depois, sozinho, `Indicate(L[0][1], color=LARANJA)` no `φ(n)` do expoente — o gancho que o `C7N14` deixou |
| C8N12 | This number a is the message — every text becomes a number before it gets here. We multiply both sides by it. | 8,5 | `FadeIn(msg_fig)` sozinho — a caixa `SEGREDO` figurativa volta pequena, ao lado do `L`. Depois, num `play` só, os sete glifos somem em `LaggedStart(FadeOut(..., target_position=L[0][0], scale=0.3))`, voando para dentro do `a`, enquanto o fundo da caixa se apaga por trás — é a única vez que a mensagem figurativa vira número. Depois `Indicate(L[0][0], color=ROXO)` sozinho, no `a` — a única parada da dedução para dizer o que a letra é. Por fim `ReplacementTransform(L → L2)` |
| C8N13 | On the left side, the exponents add up. | 3,1 | `ReplacementTransform(L2 → L3)`, sozinho |
| C8N14 | And here's the central piece: the exponent can be rewritten modulo phi of n. | 5,4 | `ReplacementTransform(L3 → L4)` sozinho. Depois, emendados num `play` só, `Indicate(L4[3], color=LARANJA)` no `(mod n)` do rodapé e `Indicate(L4[0][1], color=LARANJA)` no `(mod φ(n))` que acabou de nascer no expoente — os dois módulos têm que ser vistos juntos |
| C8N15 | Any exponent that leaves a remainder of one in this modulus gives back the same message. RSA is built entirely out of that freedom. | 9,2 | `so_fala` — linha sem animação, o `L4` fica parado em cena |
| C8N16 | We go back to the multiplication table, but now it applies to the exponent. | 5,4 | `FadeIn(tabela)` — a grade módulo `φ(n)` com a legenda — emendado com `FadeOut(dir4)`: o `≡ a (mod n)` do lado direito do `L4` sai da tela no mesmo `play` e só volta no `C8N18` |
| C8N17 | Each green circle is an inverse pair. That's what we're looking for: two numbers whose product is one, in the modulus of the exponent. | 9,2 | `LaggedStart(Create(uns))` + `Write(ed)` emendados com `FadeIn(nota)` e os dois `Indicate(celulas[2][5])`/`Indicate(celulas[5][2])` — tudo num `play` só |
| C8N18 | This pair can then replace the exponent. | 2,7 | Um `play` só: `ReplacementTransform(L4[0] → L5[0])` — a potência ganha o produto `e·d` no expoente — emendado com `FadeIn(VGroup(L5[1], L5[2], L5[3]), shift=RIGHT)`, o lado direito guardado no `C8N16` voltando, e `Indicate(ed, color=VERDE)` |
| C8N19 | And a product in the exponent is the same as a power of a power: two chained operations, one undoing the other. | 8,5 | `ReplacementTransform(L5 → L6)` emendado com o `FadeOut` da `tabela`, dos `uns`, da `nota` e do `ed`, num `play` só. Depois `Indicate(L6[0][0][1][1], color=VERMELHO)` sozinho, no expoente `e`. Por fim, depois de meio segundo de silêncio, `Indicate(L6[0][1], color=AZUL)` no expoente `d` — o par de setas do `C8N10` virando álgebra, um de cada vez, com pausa entre as duas |
| C8N20 | Each piece of the formula gets a role, starting with the message. | 4,6 | Um `play` só: `Indicate(L6[2], color=ROXO)` no `a`, emendado com `FadeIn(p['cenario'])`, `FadeIn(p['olho'])` (opacidade de volta a 1), `FadeIn(p['prat'])` e `FadeIn(pacA)` — a caixa com o `a` roxo dentro, na ponta esquerda. Depois, sozinho, `FadeIn(ch_pub)` + `FadeIn(ch_priv)`: as duas chaves da fase 0 (`fase0['pub']`/`fase0['priv']`) voltam com a opacidade restaurada, na mão de quem recebe — nenhuma das duas nasce do zero |
| C8N21 | The first power, together with the modulus, scrambles the message, and the result is the ciphertext. | 6,2 | `ch_pub.animate.move_to(canal)` + `ch_priv.animate.move_to(Y_POUSO)` emendados. Depois `atravessar(ch_pub, LEFT)` (dois `play`) — o mesmo percurso invertido do `C8N06`. Em seguida `ch_pub.animate.move_to(mão)` + `Write(f1s)` (`aᵉ (mod n)`) emendados. Por fim `trancar(pacA, pot('a', 'e', BRANCO, BRANCO))` sozinho: a primeira potência é o próprio embaralhamento |
| C8N22 | These form the public key that went across. | 3,1 | Um `play` só: `ReplacementTransform(ch_pub → rpub)` — a mesma chave cinza da fase 0 vira o retângulo, não um cartão novo — emendado com o `FadeIn` dos parênteses e vírgula de `pública(e, n)` e o `e`/`n` chegando por `ReplacementTransform` de cópias de `f1s`. Depois `pubS.animate.move_to(pouso)` sozinho. A identidade se mantém: `fase0['pub']` é o mesmo objeto que se torna `rpub` |
| C8N23 | The second power undoes the first and gives back the original message. | 4,6 | `atravessar(pacA, RIGHT)` (dois `play`). Depois, emendados, `FadeIn(p['xis'])` + `ch_priv.animate.move_to(mão)` + `Write(f2s)` (`(aᵉ)ᵈ (mod n)`). Por fim `abrir(pacA, T('a', ROXO))` sozinho — a segunda potência devolve o `a` |
| C8N24 | And the exponent that undoes it, together with the modulus, is the private key — it never leaves the receiver's hands. | 8,1 | Um `play` só: `ReplacementTransform(ch_priv → rpriv)` — a chave amarela da fase 0 virando o retângulo — emendado com o `FadeIn` de `privada(d, n)` e o `d`/`n` chegando de cópias de `f2s`. Depois `piscar(VERDE)` (dois `play`) e, por fim, `privS.animate.move_to(pouso)` sozinho |
| C8N25 | The scheme is set up. All that's left is to see it run with numbers. | 5,8 | Um `play` só: `FadeOut` de `pacA`, `f1s`, `f2s`, `pubS`, `privS` e `L6`, junto com `FadeOut` do `cenario`, do `olho`, do `prat`, do `xis` e do que sobrou na prateleira |
| C8N26 | The receiver picks the modulus in a specific way, which we'll show further on. | 5,4 | `Write(esc)` + `Write(E1)` emendados. Depois `FadeIn(inter, shift=DOWN)` sozinho — o "?" cinza nasce colado no `33`, marcando a dívida que o `C8N42` paga |
| C8N27 | With the modulus in hand, they compute phi of n — the modulus of the exponent. | 6,2 | `Write(phi)` + `ReplacementTransform(E1 → E2)` emendados, num `play` só |
| C8N28 | And they look there for an inverse pair. | 3,1 | Dois `play` separados: `Write(ed2)` primeiro, depois `ReplacementTransform(ed2 → edn)` |
| C8N29 | Both keys come from this pair: each takes one of the exponents, and both share the same modulus. | 6,9 | Dois `play`, um por cartão: primeiro `Create(pub[0])` com `pública(3, 33)` se preenchendo, o `3` puxado de `edn` e o `33` de `esc` por `ReplacementTransform`; depois o mesmo para `priv[0]` e `privada(7, 33)` |
| C8N30 | The general formula gets filled in with the numbers we chose. | 4,2 | Dois `play` separados: `ReplacementTransform(E2 → E3)` emendado com `Indicate(edn, color=VERDE)`, depois `ReplacementTransform(E3 → E4)` sozinho |
| C8N31 | The message is still missing, and it has to be a number smaller than the modulus. | 6,2 | `FadeOut(phi)` + `FadeOut(edn)` + `LaggedStart(Write(msg_esc))` (em duas partes: "mensagem: a = 5" e, por último, "< 33"), tudo num `play` só. A condição `a < n` não é decorativa: com a mensagem maior que o módulo, a volta devolve o resto e o exemplo da tela para de fechar |
| C8N32 | And it takes the place of the letter. | 3,1 | `ReplacementTransform(E4 → L7)` + `Indicate(msg_esc, color=ROXO)`, num `play` só |
| C8N33 | The sender uses the public key to lock the message. | 3,8 | Um `play` grande: `inter` desliza até o `33` do módulo (a dívida se transfere), `FadeOut(esc)`, `FadeIn` do `cenario`/`olho`/`prat`/`pacB` (a caixa com `5` roxo), `pub` encolhe e desce até a mão, uma cópia dela (`pub_olho`) encolhe mais e sobe direto para a prateleira — o intruso já fica com a pública à vista —, `priv` encolhe e pousa na ponta direita, e `Write(f1)` (`5³ ≡ 26 (mod 33)`) — tudo junto. Depois `trancar(pacB, T('26', BRANCO))` sozinho e, por fim, `atravessar(pacB, RIGHT)` (dois `play`) |
| C8N34 | Only the holder of the private key can decrypt it. No one else. | 5,0 | `FadeIn(p['xis'])` + `pub.animate.move_to(pouso)` + `priv.animate.move_to(mão)` + `Write(f2)` (`26⁷ ≡ 5 (mod 33)`), emendados num `play` só. Depois `abrir(pacB, T('5', ROXO))` sozinho, `piscar(VERDE)` (dois `play`) e, por fim, `priv.animate.move_to(pouso)` sozinho |
| C8N35 | The check is the derivation from the start of the chapter, with numbers in place of letters. | 6,5 | Dois `play` separados: `Write(fim2)` primeiro (a cadeia `(5³)⁷ = 5²¹ = 5²⁰·5 ≡ 1·5 ≡ 5 (mod 33)`), depois `ReplacementTransform(fim2 → fim3)`, a versão enxuta com `✓` |
| C8N36 | One question is left, and it decides everything: if the public and private keys are inverses modulo phi of n, wouldn't it be easy to find the private one from the public one? | 12,7 | Um `play` grande apaga o exemplo inteiro — `pacB`, `f1`, `f2`, `pub`, `priv`, `L7`, `fim3`, `msg_esc`, `inter` — junto com `cenario`, `olho`, `prat`, `xis` e o que sobrar na prateleira. Depois `FadeIn(volta)` sozinho — a seta despedaçada do `C8N10`, recentrada — e `FadeOut(volta)` sozinho, cobrando e fechando a promessa. Em seguida `FadeIn(leg)` + `FadeIn(tab)` emendados: a grade módulo 9 nasce com a legenda "tabela multiplicativa (mod φ(n))" em cima. Depois `FadeIn(eixo_e, shift=RIGHT)` + `FadeIn(eixo_d, shift=DOWN)` emendados, nomeando os dois eixos. Por fim `LaggedStart(Create(uns))` — os círculos verdes, um por linha invertível |
| C8N37 | Inverting is easy if you know the modulus. And the modulus, here, is phi of n. | 6,2 | `FadeIn(faixa)` + `Indicate(_tab_lin(tab, 2), color=VERMELHO)` emendados — a faixa amarela entra pela linha do `e`. Depois `ReplacementTransform(faixa → alvo)` + `Indicate(_tab_cel(tab, 2, 5), color=VERDE)` emendados — a faixa encolhe até parar na célula com `1`. Depois `Indicate(_tab_col(tab, 5), color=AZUL)` sozinho, saindo pela coluna do `d`. Depois `Write(c1)` sozinho (`achar d ⇒ achar φ(n)`). Por fim `Indicate(phin, color=LARANJA)` + `Indicate(VGroup(lphi[1], lphi[2], lphi[3]), color=LARANJA)` emendados — o `φ(n)` da fórmula e o da legenda acendem juntos |
| C8N38 | And phi of n is a count: how many numbers below the modulus share no factor with it. | 6,9 | Um `play` grande: a legenda perde o `φ(` e o `)` enquanto o resto vira `(mod n)` por `ReplacementTransform`, `FadeIn(l2)` traz `n = 15`, e a grade módulo 9 (`tab`, `eixo_e`, `eixo_d`, `uns`, `alvo`) some enquanto `tab15` nasce — tudo junto. Depois `LaggedStart(Create(uns15))` sozinho. Depois `LaggedStart(Create(riscos))` sozinho — as linhas que compartilham fator com 15 riscadas uma a uma. Por fim `LaggedStart(Indicate(vivas, color=VERDE))` + `FadeIn(conta)` emendados — as linhas sobreviventes acendem enquanto `φ(15) = 8` aparece embaixo |
| C8N39 | For a large modulus, counting one by one is impossible. | 3,8 | Três `play`: primeiro a malha cresce de `tab15` para `malha35` (`ReplacementTransform`), os dígitos e riscos da grade de 15 somem, e a legenda e a contagem viram `n = 35`/`φ(35) = ?`, tudo emendado. Depois o mesmo salto de `malha35` para `malha77`, com `n = 77`/`φ(77) = ?`. Por fim `conta77` encolhe, apaga e viaja até dentro do `φ(n)` do `c1`, emendado com `Indicate(phin, color=LARANJA)` — a contagem que ninguém faz à mão colapsa na fórmula |
| C8N40 | If the modulus were prime, the count would come for free — no number below a prime shares a factor with it — and anyone would have the private key. | 11,5 | `FadeOut(malha77)` + `FadeIn(tab11)` + `ReplacementTransform(l2c → l2d)` emendados — a grade vira módulo 11, primo. Depois `LaggedStart(Create(uns11))` sozinho. Depois `LaggedStart(Indicate(tab11[2], color=VERDE))` + `FadeIn(conta11)` emendados — todas as linhas acendem, nenhuma riscada, e `φ(11) = 10` aparece. Depois `Write(c2[0:6])` sozinho (`n primo: φ(n) = n`). Depois `ReplacementTransform(conta11[3].copy() → VGroup(c2[6], c2[7]))` sozinho — o `− 1` chega puxado da própria contagem. Depois `Indicate(VGroup(c2[6], c2[7]), color=LARANJA)` sozinho. Depois `FadeIn(c2[8], scale=1.6)` sozinho — o `✗` que já existe no código. Por fim `Indicate(c1[1], color=AZUL)` sozinho, no `d` — com `φ(n)` de graça, ele sai da pública na mão de qualquer um |
| C8N41 | With a product of two primes, the only ones that share a factor are the multiples of p and those of q. | 8,5 | `FadeOut(tab11)` + `FadeOut(uns11)` + `FadeIn(tab15b)` + `FadeIn(uns15b)` + `ReplacementTransform(l2d → l2e)` + `ReplacementTransform(conta11 → conta15)` emendados — a grade volta ao módulo 15 do `C8N38`. Depois `Write(c3[0:5])` sozinho (`n = p × q`). Depois `LaggedStart(Create(r_p))` + `Indicate(c3[2], color=ROSA)` emendados — as linhas 3, 6, 9 e 12 riscadas de rosa. Por fim `LaggedStart(Create(r_q))` + `Indicate(c3[4], color=VERDE2)` emendados — as linhas 5 e 10 riscadas de verde-claro |
| C8N42 | We can subtract them all at once with a formula, without counting one by one. | 5,8 | `Write(c3[5:10])` sozinho (`⇒ φ(n) =`). Depois `FadeIn(c3[10])` + `FadeIn(c3[12])` + `ReplacementTransform(c3[2].copy() → c3[11])` emendados — o `(p − 1)` nasce do `p`. Depois o mesmo para o `q`, formando `(q − 1)`. Depois `FadeIn(c3[17], scale=1.5)` + `Indicate(conta15, color=VERDE)` emendados — o `✓` e a contagem da grade fecham juntos. Por fim `LaggedStart(FadeIn(c3b, shift=UP))` sozinho: a linha instanciada `33 = 3 × 11 ⇒ φ(33) = 2 × 10 = 20`, que paga as dívidas abertas no `C8N26` e no `C8N27` |
| C8N43 | But the shortcut only works for whoever knows p and q. Anyone who only has their product would have to factor it to find out. | 9,6 | `ReplacementTransform(l2e → l2f)` + `FadeOut(r_p)` + `FadeOut(r_q)` emendados — a fatoração some da legenda e os riscos somem da grade. Depois `ReplacementTransform(conta15 → conta_q)` sozinho — a contagem volta a ser `φ(15) = ?`. Depois `Indicate(c3[0], color=LARANJA)` sozinho, no `n`. Depois `GrowArrow(volta3)` sozinho — a mesma seta do `C8N10` e do `V1N01`, agora tentando o caminho de volta do `n` para `p × q`. Por fim `LaggedStart(FadeIn(cacos3, shift=UP))` sozinho — ela se despedaça no meio do caminho |
| C8N44 | And the series comes full circle: breaking RSA means factoring this number. | 4,6 | Um `play` só: `FadeOut(VGroup(tab15b, uns15b, lpre, ln, l2f, conta_q))` — a coluna da grade sai inteira — emendado com `VGroup(c1, c2, c3, c3b, volta3, cacos3).animate.shift(LEFT)`, a coluna das fórmulas deslizando para o centro. Depois `Write(c4)` + `Create(caixa)` emendados — a tese `quebrar RSA = fatorar n` se desenha devagar dentro do retângulo verde |

**Subtotal: 304,5 s** (cartão + 44 locuções)

---

## Encerramento

| Tag | Speech | Est. | Entra em |
|---|---|---|---|
| V3N01 | All of RSA's security rests on a single statement: nobody knows how to factor a large number in a reasonable time. | 8,1 | A `caixa` verde do capítulo 8 continua em cena. O cadeado do vídeo 1 volta por cima dela, fechado, e "fatorar n" se grava no corpo dele com o mesmo flash seco do `V1N01` |
| V3N02 | The final video shows how Shor's algorithm does exactly that — and that statement stops being true. | 6,5 | Uma rachadura fina corre pelo arco do cadeado e **para no meio**. Ele não quebra: a quebra é o pagamento do vídeo 4 |
| — | *(cartão final, ~3 s)* | — | "Vídeo 4 de 4 — O algoritmo de Shor" |

**Subtotal: 14,6 s** (2 locuções) + cartão ~3 s

---

## Projeção de duração

| Bloco | Locuções | Fala |
|---|---|---|
| Abertura | 1 | 9,2 s |
| Capítulo 6 | 14 | 77,3 s |
| Capítulo 7 | 15 | 80,4 s |
| Capítulo 8 | 45 | 304,5 s |
| Encerramento | 2 | 14,6 s |
| **Total** | **77** | **486,0 s** |

Somando o `PAD` de 0,35 s por locução (26,9 s), os dois cartões silenciosos (~7 s) e os `limpar()` entre capítulos (~10 s), a projeção é de **cerca de 8 min 49 s**. Como no português, `C6N07`, `C8N04`, `C8N08`, `C8N33` e `C8N34` têm animação mais longa que a fala e somam uns 12 a 15 s ao render real.

---

## Ordem das palavras que a animação exige

Falas em que a tradução manteve a ordem porque a coluna "Entra em" ou o código amarram um gesto a um trecho:

| Tag | Ordem mantida |
|---|---|
| V3N00 | "uses them to build RSA" antes de "two theorems" |
| C6N13 | "has to be prime" (o `Indicate` no `(n prime)`) |
| C7N08 | "phi of n" nomeado aqui pela primeira vez; o capítulo 8 repete o nome |
| C7N14 | "is built on it" no fim (o `Indicate` no `φ(n)`) |
| C8N19 | o `e` antes do `d`: "one undoing the other" fecha a frase |
| C8N29 | "each takes one of the exponents" antes de "both share the same modulus" (os cartões nascem um de cada vez) |
| C8N31 | a fala termina em "smaller than the modulus" (o `<` e o 33 chegam por último) |
| C8N41 | "multiples of p" antes de "those of q" (riscos rosa, depois verde-claro) |

---

## Checklist de gravação

- [ ] Abertura — V3N00
- [ ] Cartões — CAP06 a CAP08
- [ ] Capítulo 6 — C6N01 a C6N13
- [ ] Capítulo 7 — C7N01 a C7N14
- [ ] Capítulo 8 — C8N01 a C8N44
- [ ] Encerramento — V3N01 e V3N02
- [ ] `python medir.py en`
- [ ] Render de conferência: `IDIOMA=en manim -pqh --media_dir media/en filme_shor.py VideoTeoremaRSA`
