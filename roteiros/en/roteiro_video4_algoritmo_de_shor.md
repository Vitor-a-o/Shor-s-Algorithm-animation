# Script — Video 4: Shor's algorithm (English)

Tradução de `roteiros/pt/roteiro_video4_algoritmo_de_shor.md`. Mesmas tags, mesma ordem; a
coluna "Entra em" é a do português, porque a animação é a mesma. Termos:
`roteiros/glossario.md`. Est. a 2,6 palavras/s até haver gravação em inglês.

Capítulos 9 a 11, na ordem de montagem. É o último vídeo da série: o cadeado que rachou
no fim do vídeo 3 quebra aqui.

Atenção à numeração dos arquivos: o **capítulo 10** em tela é o `capitulo9b.py` e o
**capítulo 11** é o `capitulo10.py`. As tags acompanham o número **de tela** —
`C9N`, `C10N`, `C11N`.

---

## Abertura

| Tag | Speech | Est. | Entra em |
|---|---|---|---|
| V4N00 | The whole series has led to one statement: breaking RSA means factoring a large number. This video shows the algorithm that does it — and it's a long road to get there. | 12,3 | O cadeado do fim do vídeo 3 volta ao centro **no estado em que ficou**: `estado_v3()` monta o `cadeado("fechado")` com "fatorar n" gravado no corpo e a rachadura já parada no meio do arco, e ele entra com `cena.add`, **sem animação nenhuma** — o primeiro quadro do vídeo 4 é o último quadro do vídeo 3. Enquanto a série é recapitulada, uma aproximação lenta no cadeado, como o Ken Burns do `ABN01`. Em "quebrar o RSA é fatorar", `Indicate` no rótulo gravado. Em "o algoritmo que faz isso", `avancar()` de dois segmentos: a fissura corre e **para de novo** — ela só termina no encerramento. Em "percorre um caminho longo até lá", o cadeado encolhe e sai por cima do ombro do quadro, já com o cartão de marca entrando por baixo |
| — | *(cartão silencioso, ~4 s)* | — | "Do Zero ao Algoritmo de Shor Quântico" nasce no centro e "Vídeo 4 de 4 — O algoritmo de Shor" embaixo dele. Mesma emenda dos vídeos 2 e 3: o subtítulo sai primeiro e o título encolhe por último, já com o `CAP09` entrando por baixo |

**Subtotal: 12,3 s** (1 locução) + cartão ~4 s

---

## Capítulo 9 — Ordem Modular

O capítulo é uma pergunta só, feita na tabela que o capítulo 5 já ensinou a ler: subir no
expoente é pular de linha, e a caminhada volta ao ponto de partida. A fala nunca lê o
zigue-zague — ela diz o movimento, e a tela faz os números.

A tabela é usada **duas vezes**. Na primeira (`C9N03`–`C9N11`), base 4 mod 9: o ciclo fecha
em três passos e o `r = 3` nasce daí. Na segunda (`C9N13`), a mesma tabela recebe a base 5,
que é raiz primitiva mod 9: o ciclo passa pelos seis restos invertíveis antes de devolver o
1, e `r = 6` é exatamente `φ(9)` — o pior caso deixa de ser uma frase e passa a ser um
caminho longo na tela. O `C9N14` fecha o argumento do custo com o módulo crescendo, no
mesmo gesto do `C8N39` do vídeo 3.

| Tag | Speech | Est. | Entra em |
|---|---|---|---|
| CAP09 | The road to factoring rests on a very important property of modular exponentiation. | 5,0 | cartão |
| C9N01 | The same equation from chapter four of the second video comes back. But the question is no longer finding the remainder. | 8,1 | `Write(eq)` |
| C9N02 | The modulus and the base stay put; what moves is the exponent. And the base has an inverse, as chapter five required. | 8,5 | `FadeIn(escolha)`. Em "tem inverso", `Indicate` na palavra `inversível` cinza que a `escolha` já carrega |
| C9N03 | The multiplication table for the modulus comes back, and that's where the walk will take place. | 6,2 | `head_c` + `head_l` + `lin_h` + `lin_v` e o `LaggedStart(linhas_cel)` correm emendados, num bloco só |
| C9N04 | Only the base's row matters. | 1,9 | `GrowArrow(seta4)` + `Indicate(head_l[4])` |
| C9N05 | The walk starts at exponent zero, where the power is one. | 4,2 | `Create(c00)` + `Write(f0)` |
| C9N06 | And going up one step in the exponent is the same as multiplying by the base — that is, jumping to its row. | 8,8 | `FadeIn(nota)` |
| C9N07 | Each step goes down to the base's row, and the result becomes the column for the next step. | 6,9 | As **duas primeiras voltas do laço** inteiras — seis `play`: `desce`/`alvo`, `Write(fs[0])`, `sobe`/`topo`, `desce`/`alvo`, `Write(fs[1])`, `sobe`/`topo`. O `with narra` envolve o `for`, não cada iteração dele: mesma correção do `C2N07` e do `C5N11`. **Seis `play` em 6,2 s** — ver a pendência 9 do capítulo |
| C9N08 | Until the walk lands back on one — right where it started. | 4,6 | O terceiro passo do laço: `desce`/`alvo`, `Write(fs[2])` com o ✓, e o `Flash(ponto(4, 7))` — os três `play` sob esta linha |
| C9N09 | The path is a closed cycle. From here on, it just repeats. | 4,6 | Dois `play` sob esta linha: `Create(fecha)` + `Indicate(c00)` e, em seguida, `Write(VGroup(mult[0], mult[1], mult[2]))`. **A congruência mudou de dono**: ela era a fala cortada e agora entra sob "ele só se repete" — sem isso o `mult` nunca nasce e os `TransformFromCopy` do `C9N10` e do `C9N11` ficam sem origem |
| C9N10 | And each full lap around the cycle gives powers congruent to the same remainder. | 5,4 | Os quatro `play` das duas voltas extras num bloco só: `volta_no_ciclo()`, o `4⁶` nascendo por `TransformFromCopy`, `volta_no_ciclo()` de novo e o `4⁹` com o `(mod 9)`. É a irmã do "e assim por diante" do `C2N07` |
| C9N11 | The smallest of those exponents is the one that matters. | 3,8 | Um `play` só: `Write(rdef[0])` + `Write(rdef[1])` + `TransformFromCopy(mult[2][1], rdef[2])` — o `3` amarelo nasce do expoente que fechou o ciclo, não de um `Write` do vazio. Cabe com folga nos 2,4 s da fala |
| C9N12 | It's called the multiplicative order of this base. | 3,1 | **A virada, igual à do `C6N12` e à do `C7N13`.** Um `play` só: a tabela (`head_c`, `head_l`, `lin_h`, `lin_v`, `linhas_cel`, `seta4`, `zig`) e a coluna direita inteira (`eq`, `escolha`, `f0`, `nota`, `fs`, `mult`) saem em `FadeOut`, e no mesmo bloco `caixa_d` e `borda` nascem já centrados. O `rdef` sai meio segundo atrasado em relação ao resto, e o `r` amarelo dele chega ao `r` do `d2`/`d3` por `TransformFromCopy` — o caso particular é a última coisa a desaparecer debaixo do geral. O `d1` já diz "ordem modular de a módulo n", então **não** entra título separado aqui. **É a linha mais apertada do capítulo**: 2,4 s de fala para o movimento mais complexo dele — ver a pendência 9 |
| C9N13 | And it can be huge: in the worst case, as big as Euler's count. | 5,4 | **O pior caso ACONTECENDO, na mesma tabela e com outra base.** Quatro `play`: (1) `Write(d4)`; (2) a definição encolhe para a coluna da direita (`bloco.animate.scale(0.8).move_to([3.3, 0, 0])`) e por baixo dela a tabela mod 9 volta — `FadeIn(tab9)` + `lin_h` + `lin_v`, a legenda `a = 5` `(mod 9)` e o `GrowArrow(seta5)` na linha 5, com o `Create(ini5)` no 1 de partida; (3) o ciclo do 5 inteiro num `LaggedStart(*degraus, lag_ratio=0.8)` — `1 → 5 → 7 → 8 → 4 → 2 → 1`, seis degraus, um por resto invertível, a ida atravessando a tabela para a direita e a volta descendo pela esquerda até o `ini5`, que só pisca (`Indicate`) porque já está lá; (4) `Write(cont9)` (`r = 6 = φ(9)`) com o `Indicate` no `φ(` `n` `)` cinza do `d4` em "a contagem de Euler" — a peça que o capítulo 7 definiu e o 8 gastou. **A fala não lê nenhum degrau**: aqui não entra congruência escrita, o que a tela mostra é o comprimento do caminho. Base 5 é raiz primitiva mod 9, então o ciclo passa pelos seis invertíveis e `r` bate exatamente em `φ(9)` — é o `d4` virando exemplo. **Quatro `play` em 5,3 s** — ver a pendência 9 |
| C9N14 | Searching by testing one exponent at a time is very expensive for large moduli. | 5,4 | **O módulo cresce, como no `C8N39`.** Cinco `play`: (1) `tab9`, `caminho5`, `ini5` e `seta5` saem e as duas linhas da tabela mod 9 se desdobram na malha inteira — `ReplacementTransform(VGroup(lin_h, lin_v), malha21)`, a legenda vira `n = 21` e a contagem vira `φ(21) = 12`; (2) `malha21 → malha39` com `n = 39` e `φ(39) = 24`; (3) `malha39 → malha77` com `n = 77` e `φ(77) = ?`; (4) a contagem COLAPSA dentro do `φ(n)` do `d4` (`move_to(phi4).scale(0.2).set_opacity(0)` + `Indicate(phi4)`) — a conta que ninguém faz à mão; (5) a malha e a legenda saem e a definição retoma o centro em `scale(1 / 0.8)`. O quadrado do miolo é **fixo**: quem cresce é o número de células, por isso os dígitos saem e sobra só malha. **Cinco `play` em 5,9 s** — ver a pendência 9 |
| C9N15 | Hold on to the question: what's the smallest exponent that gives back one? The next chapter shows that it leads to factoring. | 8,5 | `so_fala` — a caixa parada em cena. Em "o menor expoente", `Indicate` no `r` amarelo do `d3` |

**Subtotal: 90,4 s** (cartão + 15 locuções)

---

## Capítulo 10 — Da Ordem Modular à fatoração

O capítulo tem três fases e uma coda. A **fatoração que dá certo** (`C10N01`–`C10N19`) roda
o método inteiro num alvo pequeno: acha a ordem, parte a potência em diferença de
quadrados, e o mdc pesca os dois primos. O **caso inútil** (`C10N20`–`C10N29`) roda o mesmo
método com outra base e falha — é a fase que impede o algoritmo de virar mágica, e a fala
dela é seca de propósito, porque a tela repete um trajeto que o espectador acabou de ver.
A **coda** (`C10N30`–`C10N33`) cobra a dívida do capítulo 8: com os primos na mão, a chave
privada sai por um inverso.

As duas árvores de fatores são o coração visual do capítulo e correm quase mudas: elas
mostram o mesmo número aberto de dois jeitos, e dizer isso em palavras é tudo o que a fala
precisa fazer. A ressalva é o `C10N08`: a árvore dos capítulos 3 e 4 **converge** — os
resultados sobem para a soma e para o produto — e aqui ela **reparte**. É a mesma forma com
o sentido invertido, e essa é a única linha do capítulo que gasta palavras com a imagem.

Que as duas árvores abrem o mesmo número é dito **uma vez só**, no `C10N12`, porque é ali
que a tela escreve `65 · 63 = 117 · 35` e ganha o direito de dizer. O `C10N10` fica na
manobra e a segunda árvore nasce muda: qualquer fala em cima dela adiantaria o `C10N12`.

O que a tela mostra é sempre `8⁴ − 1`, a **potência** menos um — nunca a ordem menos um. A
ordem é 4, e 4 − 1 não é nada do que está escrito. A distinção vale para o `C10N07` e para
o `C10N10`, que são as duas linhas que nomeiam esse número em voz alta.

A comutatividade também não é sorte: ela vale sempre, e é ela que autoriza o reagrupamento.
Por isso ela não roda no `C10N14`: ali a igualdade só carrega os mesmos fatores para o outro
lado, sem mexer na ordem deles. Quem reagrupa é o `C10N15`, e nos dois lugares ao mesmo
tempo. O que é sorte é p e q caírem em **lados diferentes** — é isso que o `C10N15` promete
e o `C10N24` quebra.

| Tag | Speech | Est. | Entra em |
|---|---|---|---|
| CAP10 | How the order becomes a factoring tool. | 2,7 | cartão |
| C10N01 | We go back to the RSA number: a product of two primes that's very hard to factor. | 6,5 | `Write(obj)` — o `p × q ?` com os primos ainda como letras |
| C10N02 | And we pick any base. | 1,9 | `Write(base)` |
| C10N03 | Then we look for its order, the same way as in the previous chapter: multiplying by the base until it loops back. | 8,5 | Sete `play` num bloco só: `Write(rotulo)`, `FadeIn(caixas[0])`, as três iterações do `for` (`seta` + `rot` + `caixas[i+1]`), `Create(volta)` + `rv` e o `Flash`. O `with narra` envolve o laço inteiro |
| C10N04 | It takes four steps, so the order is four. | 3,5 | `Write(rper)` com os `Indicate` nos quatro rótulos `×8` |
| C10N05 | So we can write the following congruence. | 2,7 | `Write(e1)` + `Indicate(rper)` |
| C10N06 | Subtracting one from both sides, we notice that the order hands us a multiple of the number we want to factor. | 8,1 | **Três `play` num bloco só.** A saída da cadeia (`caixas`, `setas_o`, `volta`, `rv`, `base`, `rotulo`) com o `rper` subindo para o canto; `ReplacementTransform(e1, e2)`; `FadeIn(nota)` em "um múltiplo do número" — a `nota` escreve a frase que a fala acaba de dizer |
| C10N07 | In other words, the power minus one equals thirty-five times x. | 4,2 | `ReplacementTransform(e2, e3)` + `FadeOut(nota)` |
| C10N08 | Here this tree doesn't join, it splits: the trunk on top and the factors below. | 5,8 | Os dois `play` da primeira árvore sob esta linha: o tronco `rb` nascendo por `ReplacementTransform` de uma cópia da própria conta, e `Create(linB)` com o `35` e o `x` descendo dos termos de `e3` |
| C10N09 | To find x you just isolate the variable in the equation, but that's not so important. | 6,2 | Três `play` sob esta linha: `Write(ex)`; `ReplacementTransform(e3, e4)` com `FadeOut(ex)` e `fBx → fB117`; e `ReplacementTransform(e4, eqB_a)`, que desce a conta para `eqB_a` em `[3.5, 0.62, 0]` — só a cabeça nasce agora, com o espaço da cauda (`eqB_b`) reservado à direita; ela chega no `C10N13` |
| C10N10 | To find other factors of this power minus one, we can use the difference of squares. | 6,2 | Dois `play` sob esta linha: `Indicate(eqB_a)`; e `Write(dgen)`, num traço lento (2,0), a identidade GENÉRICA `x² − 1 = (x − 1)(x + 1)` aparecendo **direto** — o nome "diferença de quadrados" fica só na fala, nunca escrito na tela, e nunca um número por extenso. A linha `d0` + `dgen` já nasce diagramada e centrada em `[0, 2.15, 0]`: `dgen` entra no lugar definitivo e o espaço do `r par ⇒` fica reservado à esquerda, para nada refluir no `C10N11` |
| C10N11 | For this to work, the order r has to be even. | 4,2 | **Um `play` só, a linha inteira para ele.** `TransformFromCopy(rper[0], d0[0])` + `Write(d0[1:3])` — o `r par ⇒` crescendo **na frente** do que já está escrito, com o `r` amarelo nascendo do `rper` parado no canto (mesmo gesto do `C9N11`). Sem mais nenhuma manobra competindo pelo tempo, a condição "r precisa ser par" pesa sozinha antes de a álgebra continuar |
| — | *(sem fala — a substituição roda muda, como a segunda árvore do `C10N12`)* | — | Três `play` em silêncio, fora de qualquer `with narra`, logo depois do `C10N11`, todos folgados de propósito — é a passagem mais suave do capítulo: primeiro o `FadeOut` do `r par ⇒` sozinho (já cumpriu o papel), para que a troca de token não dispute a atenção; depois o `x → 8²` token a token (1,6) — `FadeOut` no `x²`/`− 1 =` genéricos, `TransformFromCopy(eqB_a[0:2], d1[0:2])` trazendo o `8⁴ − 1 =` de volta como cópia da conta que já está em cena, e um `ReplacementTransform` por token (`dgen[2:7] → d1[2:7]`) mostrando o `x` virando `8²` nos dois parênteses; por fim `ReplacementTransform(d1, d2)` (1,3), que fecha a manobra em `65 · 63`. Nem `C10N10` nem `C10N11` dizem "oito" em voz alta — por isso a conta pode ficar muda até aqui |
| C10N12 | So we're left with the same number written as a product in two different ways. | 5,8 | Antes desta linha, **em silêncio** (os dois `play` fora de qualquer `with narra`, depois da substituição acima): o tronco `ra` por `ReplacementTransform` de uma cópia de `d2[0:2]`, e `Create(linA)` com `fA65`/`fA63` descendo de `d2[2]`/`d2[4]`. Sob esta linha, dois `play`: `ReplacementTransform(d2, eqA_a)`, que desce a conta para `eqA_a` em `[-3.5, 0.62, 0]` — espelhando `eqB_a`, cauda `eqA_b` também reservada à direita; e o nascimento de `junta`, que não é mais um `ReplacementTransform` de `d2`: ela nasce por `TransformFromCopy(eqA_a[2:5], junta[0])` e `TransformFromCopy(eqB_a[2:5], junta[2:4])`, um lado direito voando de cada equação, com só o `Write(junta[1])` (o sinal de igual) sendo escrito |
| C10N13 | By definition, the two primes are factors of thirty-five — and the factors of one hundred seventeen, we simply label. | 7,7 | Quatro `play` sob esta linha. `Create(linB2)` + `FadeIn(nB)` — `nB` na ordem `z, y, q, p`, z e y pendurados no `fB117`, q e p pendurados no `fB35`; depois `Write(eqB_b)` + `ReplacementTransform(junta, j2)`, que preenche a cauda reservada de `eqB_a` com os mesmos quatro fatores. Por fim os dois destaques, cada um acendendo o galho **junto** do que pende dele: `Indicate(fB35)` com `nB[2]`/`nB[3]` em "fatores de 35", e `Indicate(fB117)` com `nB[0]`/`nB[1]` em "os de 117" — o galho e os filhos piscando juntos dizem de onde cada par veio, que é exatamente o que a fala afirma |
| C10N14 | Since this is an equality, the same factors have to show up on the other side too. | 6,5 | Dois `play` sob esta linha: `Indicate(j2[1])`, o sinal de igual do meio; e `TransformFromCopy(j2[2:7], eqA_b)`, o lado direito do `j2` inteiro atravessando a igualdade e preenchendo a cauda reservada de `eqA_a`. **Nada comuta aqui:** o `j2` fica exatamente como está e `eqA_b` nasce na MESMA ordem da cauda da direita (`= (z · y) · (q · p)`) — são os mesmos fatores do outro lado, e só isso |
| C10N15 | Multiplication is commutative, so the factors regroup — and with luck p and q land one on each side. | 7,3 | Quatro `play` sob esta linha. O primeiro é a COMUTATIVIDADE, nos dois lugares ao mesmo tempo e emendados: `j2[0] → j3[0:5]` (só o **lado esquerdo** do `j2`, o `65 · 63`, vira o reagrupamento; o lado direito só acompanha o deslocamento, token a token) junto de `eqA_b → eqA_b2`, a cauda da equação da árvore comutando no mesmo gesto. Depois `Create(linA2)` + `FadeIn(nA)`, os fatores já reagrupados descendo para a árvore da esquerda — `nA` na ordem `p, y, z, q`, espelhando `nB`. Por fim os dois `Indicate` do par que se separou: `nA[0]` + `nB[3]` no rosa, `nA[3]` + `nB[2]` no verde-claro |
| C10N16 | So we can see that the two numbers we just computed share a factor with the number we want to factor. | 8,1 | Dois `play` sob esta linha. `Indicate(fA65)` + `Indicate(fA63)` — quem compartilha fator com o `35` são os dois números da árvore da esquerda, e o gesto é o de apontar para eles. Depois `Indicate(obj[0], color=LARANJA)` em "o número que queremos fatorar", herdado do `C10N15` quando aquela linha perdeu a cauda. Nenhum texto na tela: a frase inteira fica na fala |
| C10N17 | And finding a common factor is easy, using Euclid's algorithm, the same one that came up in passing in chapter five. | 8,1 | **Dois `play` num bloco só:** `Write(m1)` com os `Indicate` no par verde-claro, depois `Write(m2)` com os `Indicate` no par rosa |
| C10N18 | Finally we've found the factors p and q, which looked like an impossible task. | 5,4 | `ReplacementTransform(VGroup(m1, m2), fim)` + `Create(cxa)` |
| C10N19 | The number that opened the chapter is factored. | 3,1 | `ReplacementTransform(obj, obj2)` — o `p × q ?` do topo vira os dois primos com ✓ |
| C10N20 | But it's not all smooth sailing: things can go wrong — for example, the base can give an odd order. | 7,7 | O `FadeOut` das duas árvores e das contas emendado com `FadeIn(cap5)`, num `play` só. O `fim` dentro da moldura verde **fica em cena** o resto do capítulo: o sucesso segue à vista enquanto a falha roda |
| C10N21 | Or the order may give no useful information. | 3,1 | `so_fala` — o quadro parado. `Indicate(cap5)`, que é exatamente a frase que a fala diz |
| C10N22 | To see that happen, let's take another example, also with an even order. | 5,0 | Dois `play` sob esta linha: `Write(u0)` e `Indicate(u0[6], color=AMARELO)` — o `6` da ordem, em "também com a ordem par" |
| C10N23 | Everything runs all the way through without a hitch. | 3,5 | `Write(u1a)` e `ReplacementTransform(u1a, u1)` — dois `play` sob esta linha. `u1a` já nasce como `24⁶ − 1 = (24³ − 1)(24³ + 1)` em tokens coloridos (`pot` para as duas potências de base 24), a mesma manobra do `C10N10`–`C10N11` com o `x` já substituído — sem texto corrido nem cor fora da paleta |
| C10N24 | But this time the two primes don't split up: they land together, on the same side. | 6,2 | Quatro `play` num bloco só: tronco `ru`, `Create(linU)` com `fu1`/`fu2`, `Create(linU2)` + `FadeIn(nU)`, e por fim `Indicate(nU[0], color=ROSA)` + `Indicate(nU[1], color=VERDE2)` — o p e o q lado a lado sob o mesmo galho, que é o que a fala afirma |
| C10N25 | That happens because this number turned out to be a multiple of thirty-five. | 5,0 | Dois `play` sob esta linha: `FadeIn(multi)` + `GrowArrow(setam)` + `Indicate(fu1, color=PRETO)`, e depois `Indicate(multi[1], color=LARANJA)` — o `35` do rótulo, em "múltiplo de 35" |
| C10N26 | So a gcd gives back thirty-five itself... | 2,7 | Dois `play` sob esta linha: `Write(m3)` e `Indicate(m3[5], color=LARANJA)`. O destaque vai em `play` próprio pela razão do `C10N04`: dentro do `Write` ele guardaria o estado sem preenchimento do começo e o devolveria no fim, deixando o resultado invisível o resto do capítulo |
| C10N27 | ...and so the number on the other side has no factor in common with it. | 5,8 | Dois `play` sob esta linha: `Write(m4)` e `Indicate(m4[5], color=PRETO)` — o `1`, mesma razão do `C10N26` |
| C10N28 | Those are the two trivial factors of thirty-five, which we already knew without doing any of this. | 6,5 | Dois `play` sob esta linha: `Write(triv)` e `Indicate(m3[5], color=LARANJA)` + `Indicate(m4[5], color=PRETO)`. O `FadeIn(sol)` **não entra aqui** — ele foi para a linha seguinte, junto da fala que o explica |
| C10N29 | When that happens, you change the base and run it again — and each new try has at least a fifty percent chance of working. | 9,6 | Dois `play` sob esta linha: `FadeIn(sol)` e `Indicate(sol, color=CINZA)`. O destaque vai em `play` próprio pela razão do `C10N26`: junto do `FadeIn`, o `Indicate` guardaria o `sol` ainda invisível (o `FadeIn` zera a opacidade antes) e devolveria esse estado no fim, deixando o cartão invisível o resto do capítulo. Animação curta sob fala longa: o cartão da solução aparece exatamente quando ela é dita, e o quadro fica parado no ✗ vermelho durante os ~9 s seguintes — é essa parada que faz a falha pesar |
| C10N30 | With both primes in hand, we find Euler's count. | 3,5 | Dois `play`. O `FadeOut` do caso inútil emendado com `ReplacementTransform(fim.copy(), r1)` num `play` só — a contagem **nasce de dentro** dos dois primos que ficaram na moldura verde. Depois `Indicate(r1[12], color=PRETO)`, o `24` |
| C10N31 | And with it, the private key is just the inverse of the public key, easy to find. | 6,5 | Três `play`: `Write(r2)`; `Indicate(r2[2], color=AZUL)` em "a chave privada"; e `Indicate(r2[0], color=VERMELHO)` + `Indicate(VGroup(r2[5], r2[6], r2[7]), color=LARANJA)` em "o inverso da chave pública" — é a tabela de inversos do `C8N17` sendo cobrada |
| C10N32 | In other words, factoring the modulus and finding the private key are the same thing. | 5,8 | Dois `play`: `Write(r3)` + `Create(cxa2)`, e `Indicate(r3[2], color=VERDE)` — o sinal de igual, que é literalmente "são a mesma coisa" |
| C10N33 | Now just one piece is missing: speeding up the search for the order. That's where a quantum computer comes in. | 7,7 | `with narra` com um `play` só: `Indicate(r3[1], color=LARANJA)`, o `n`. Não é `so_fala` — `so_fala` não roda `play` nenhum. O `r` amarelo do `C9N15` não serve aqui: o `rper` sai no `FadeOut` do `C10N20` |

**Subtotal: 191,1 s** (cartão + 33 locuções)

---

## Capítulo 11 — Shor Quântico: a QFT encontra o período

O capítulo mais longo do vídeo e o único quântico da série. São **oito blocos**, e a
tabela abaixo foi refeita contra o `capitulo10.py` — o código está adiante do roteiro
anterior e é ele que manda aqui.

**Fundamentos** (`C11N01`–`C11N09`) parte do bit clássico, mostra que ele só sabe dois
estados, e daí abre para superposição e emaranhamento — sem uma única fórmula. É a fase
figurativa do capítulo e a única em que a série fala de física. A virada do bloco é o
`C11N04`, em que o cartão sólido **vira** o cartão em gradiente: o qubit não entra em cena,
ele nasce do bit.

O **esquema** (`C11N10`–`C11N12`) é bloco novo e é a peça que faltava: antes de qualquer
coisa quântica, a conta reaparece como o desenho de caixas cinzas do fim do capítulo 4, com a base
e o módulo deste capítulo. Tudo genérico, sem exemplo numérico — o circuito não vai rodar
um expoente, vai rodar todos, e um número na tela aqui diria o contrário. O **circuito**
(`C11N13`–`C11N24`) então **traduz** esse desenho peça por peça, sem nada sair por
`FadeOut`, mede o registrador de baixo e mostra o colapso: escolhido o resto, sobrevivem só
os expoentes que o devolvem. O rodízio do `C11N20` existe para que o resto medido não seja
lido como especial.

O **pente** (`C11N25`–`C11N28`) é a virada conceitual: o que sobrou tem a ordem escrita no
espaçamento. Escrita, não revelada: o pente é o estado dentro da transformada, e nada ali é
observável. Por isso o `r = ?` que nasce no `C11N21` atravessa o capítulo inteiro sem
resposta — as chaves do `C11N27` dizem que o espaçamento *é* o r, mas nunca quanto ele vale
— e só vira `r = 6` no `C11N39`, depois da medida e das frações contínuas. Ele **não** começa com a tela limpa: o `C11N25` entra
na caixa da transformada — ela cresce até passar das bordas do quadro enquanto o circuito
inteiro sai —, e a coluna de expoentes que sobreviveram ao colapso atravessa a expansão de
pé. No `C11N26` é essa mesma coluna que vira o pente, número por número. Não existe mais
nenhum passo de texto entre o circuito e a reta: o conjunto dos expoentes compatíveis nunca
é escrito por extenso, porque a transformação o mostra. É a regra 4 da gramática visual
aplicada ao trecho inteiro — o pente não entra em cena, ele nasce do painel. As **ondas** (`C11N29`–`C11N34`) são um instrumento só, na
estrutura do `qft_shor_ondas_N512.html`: à direita, uma cossenoide por expoente, nascida do
dente dele; à esquerda, o círculo em que cada onda é uma seta e as setas se emendam; um
cursor que percorre as ondas e move as setas junto; e embaixo o traço da soma, que se
desenha conforme o cursor anda e termina sendo a distribuição de saída. Antes eram três
trechos — as ondas, a roleta e a curva — que explicavam a interferência duas vezes e
desenhavam a mesma curva em dois lugares; com as três peças na tela ao mesmo tempo, uma
passagem basta, e as falas encolheram de dezessete para seis. A **cascata**
(`C11N35`–`C11N46`) devolve tudo para o capítulo 10 e fecha a série. Ela não começa pela
conta: a câmera sai da transformada pelo mesmo caminho por que entrou, o circuito volta
inteiro com a caixa da TQF recuada no fio, e os picos do traço viram, **depois** dela, o
registrador de saída — o mesmo painel em degradê dos outros dois. Só depois de a medida
cair em um dos valores é que a aritmética abre: `85 ≈ x · N/r`, dividido pelo tamanho do
registrador, e as frações contínuas. O gráfico vira registrador antes de virar número, e é
por isso que ele não pode ser medido flutuando sozinho: a medida é uma peça do circuito.

| Tag | Speech | Est. | Entra em |
|---|---|---|---|
| CAP11 | How a quantum computer finds the order quickly. | 3,1 | cartão |
| C11N01 | The computing we use every day, classical computing, is made of logic on bits. | 5,4 | `LaggedStart` de nove cartões chapados do `_fila_classica`, alternando `0` laranja e `1` verde, mais o rótulo `computação clássica`. A fila é ímpar de propósito: o cartão do meio é um `0` e cai no centro do quadro, que é onde o bloco inteiro vai acontecer |
| C11N02 | And a bit has only two possible states: it's either zero or one. | 5,0 | `Succession` de dois `ReplacementTransform` no cartão do meio, que cresce em `scale(1.5)`: `0 → 1 → 0`. O repertório do bit se esgota à vista, e é esse esgotamento que dá sentido ao gradiente que vem depois |
| C11N03 | But quantum physics found that reality is more complicated than that. | 4,2 | `FadeOut(resto_fila)` + `FadeOut(rot_cl)`. Sai a fila **menos** o cartão do meio, que já foi consumido pelo `ReplacementTransform` — um `FadeOut(fila)` inteiro o traria de volta piscando. A tela esvazia na linha da virada |
| C11N04 | There are other possible states, and quantum computing takes advantage of them. | 4,6 | `ReplacementTransform(bit_0, qub)`: o cartão sólido **vira** o cartão em gradiente, no lugar em que já estava. Regra 4 da gramática visual — o qubit não entra em cena, ele nasce do bit |
| C11N05 | Instead of a bit that carries only zero or one, quantum computing uses a qubit. | 5,8 | `FadeIn(t1)` + `ReplacementTransform(qub, q1)` — o cartão viaja do centro para `[-4.0, 1.3, 0]` e o rótulo `superposição` entra por cima. O `q1` chega por movimento, não por `FadeIn` |
| C11N06 | And what the qubit carries is the probability of the measurement returning each of the two. | 6,2 | `TransformFromCopy(q1[0], b)` para as duas barras do `_barras_peso`, verde e laranja, nascendo do próprio gradiente. Alturas diferentes de propósito: o qubit não é meio a meio, e essa é a única imagem de probabilidade do capítulo |
| C11N07 | And two qubits can also become entangled. | 2,7 | `FadeIn(qa)` e, emendado, `Create(fio)` + `FadeIn(no)` + `FadeIn(qb)` — os dois `play` num bloco só. **O `t2` não entra aqui**: a palavra emaranhamento passou para a fala, e escrevê-la no mesmo `play` em que ela é dita seria legenda. O par sobe sem título por estes quatro segundos, e é a fala que o nomeia |
| C11N08 | That way, neither of them has an answer of its own anymore. | 4,6 | `FadeIn(t2)` + `FadeIn(nota)`, num `play` só — **o rótulo `emaranhamento` entra aqui**, uma fala depois de a palavra ter sido dita. Escrito assim ele não legenda, ele confirma, e a metade direita do quadro recupera o título que faz par com a `superposição` da esquerda. A `nota` cinza, essa sim, diz na tela a frase que a locução seguinte fala — o mesmo par deliberado do `C10N21` com o `cap5` |
| C11N09 | So measuring one of them decides the other's value instantly. | 3,8 | `Flash(qa)` + `ReplacementTransform(VGroup(qa, qb), par_1)` e, emendado, `ReplacementTransform(par_1, par_0)` — os dois colapsam juntos, primeiro em `1` e `1` e depois em `0` e `0`. **O segundo colapso não tem locução própria, e isso é decisão de roteiro, não descuido**: ele corre no fim da fala, dizendo sem palavra nenhuma que o par podia ter caído do outro lado. O que fica em cena espera em `cena.grupo_fundamentos`; a limpeza é do `C11N10` |
| C11N10 | That's all the physics we need. Now for another example, with an n that fits in the register — and the computation the circuit performs is the modular exponentiation from chapter four. | 12,3 | Um `play` só. `FadeOut(cena.grupo_fundamentos)` logo no começo, em "De física é só isso" — a limpeza pertence a esta fala, não ao silêncio entre blocos. Em "outro exemplo", atrasado por `Succession` no mesmo padrão do `C11N35`, o `Write(eqc)` da congruência `c ≡ 2ᵇ (mod 21)`: o `21` entra quando o exemplo novo é anunciado, e a fala não o lê. "Vamos a outro exemplo" é o mesmo gesto do `C10N22`: marca em voz alta a troca do n do capítulo 10 (35) para o n deste capítulo (21) |
| C11N11 | And we already drew it at the end of that chapter: each bit of the exponent turns a power on or off. | 8,5 | Dois `play` emendados: `LaggedStart` das quatro caixas de bit `bᵢ` com o `…`, e depois `LaggedStart` de `GrowArrow` + `FadeIn` das quatro caixas cinzas `2^(2ⁱ) (mod 21)`. Tudo genérico, sem exemplo numérico — o circuito não vai rodar um expoente, vai rodar todos, e um número aqui diria o contrário |
| C11N12 | The product of everything coming out of the boxes is the whole power, and it gives back the remainder. | 7,3 | Três `play` emendados: as quatro `setas2` convergindo, o `FadeIn(prod)` da caixa do produto — que é a própria fórmula do alto do quadro — e o `GrowArrow(seta3)` + `TransformFromCopy(eqc[0], saida)`, com o `c` da saída nascendo do `c` da congruência |
| C11N13 | The quantum circuit is this same diagram, with each piece swapped for its quantum equivalent. | 5,8 | Quatro `play` emendados, na ordem em que a tradução precisa acontecer: a metade de baixo do esquema se recolhe e o `c` atravessa para a ponta do fio alvo; as caixas cinzas descem já virando `_caixa_porta`; as caixas de bit atravessam para a esquerda e as setas esticam virando as ligações de controle; e só então os fios ligam tudo. Nada sai por `FadeOut` — o esquema **vira** o circuito |
| C11N14 | The top wires carry the exponent b, and the bottom one holds the remainder c. | 5,8 | `FadeIn` dos dois fundos de painel primeiro e, no `play` seguinte, `TransformFromCopy(eqc[2][1], letra_b)` mais o `c` deslizando para dentro do painel de baixo. Fundo e conteúdo nunca no mesmo `play`: no Manim 0.20.1 o conteúdo fica atrás do preenchimento e some |
| C11N15 | Except now, each bit of the exponent is a qubit. | 3,8 | `LaggedStart` de `ReplacementTransform` das quatro caixas de bit nos cartões-gradiente do fio, `lag_ratio=0.15` — cada bit vira qubit em cascata, na ordem em que estava no esquema. É o primeiro dos dois `play` do bloco antigo |
| C11N16 | And then the exponent stops being a single number: it becomes all of them at once. That's the superposition we saw. | 8,1 | A letra `b` abrindo na coluna dos expoentes com o `⋮` embaixo — o segundo `play` do bloco antigo, agora com locução própria. A superposição ganha nome na fala e conteúdo na tela ao mesmo tempo, em vez de as duas coisas correrem sob uma locução de treze segundos. A animação é curta para a fala, e aqui isso é aceito: o painel que acaba de se montar precisa de tempo parado para ser lido |
| C11N17 | Since the exponent carries every possibility, the remainder c must carry them too. | 5,0 | `ReplacementTransform(saida_circ, carta_c[1])` + `FadeIn(carta_c[2])` — o `c` genérico abre na coluna dos restos possíveis |
| C11N18 | Now we measure the bottom wire. | 2,3 | `FadeIn(med)` — a caixinha `M` no fio alvo |
| C11N19 | We get one possible remainder, and with it the whole system collapses: only the exponents that give that same remainder are left. | 8,5 | `Flash(med)` + os dois `ReplacementTransform` do colapso, num `play` só: o painel de baixo vira um número, e o de cima perde os expoentes que não devolvem aquele número. O de cima **não** vira um expoente — continua em superposição, agora só dos que sobreviveram |
| C11N20 | It could have been any of the remainders in the cycle, and each one leaves a different set of exponents alive. | 8,1 | O laço do `rodizio` inteiro dentro do bloco: quatro `ReplacementTransform` de resto e de coluna, terminando de volta no resto com que o capítulo vai trabalhar. Um `with narra` cobrindo o `for`, nunca um por volta |
| C11N21 | So we're back to the problem from chapter nine: we can see that the superposition holds the information needed to solve it. | 8,5 | **Animação nova, pequena.** `Indicate(lista_b, color=AZUL)` — a coluna que sobreviveu ao colapso acende — e, emendado, um `r = ?` em laranja nascendo ao lado do painel de cima. A interrogação é o ponto: a informação está ali e ainda não dá para lê-la. O `r` usa a cor e o corpo do `r = 6` da cascata (`linhas[2]` do `C11N39`), porque é nele que esta peça vai se transformar: a pergunta atravessa o capítulo inteiro e só é respondida lá. Não mostrar espaçamento nem distância aqui — isso é do `C11N26`, e antecipar gastaria a virada do pente |
| C11N22 | Even though the superposition holds the values we need, they're only probabilities, and a measurement would return a single value, taking with it the information that matters: r. | 10,8 | **Animação nova — a medida hipotética.** Cinco batidas, na ordem exata da frase. (1) `_barras_peso` em miniatura ao lado de cada entrada do `lista_b`, nascendo por `TransformFromCopy`: é a peça do `C11N06` voltando, e ela é o vocabulário que o capítulo já tem para probabilidade. (2) Um `M` **fantasma** nasce sobre os fios de cima — traço tracejado e `opacity` baixa —, e no mesmo `play` todo o resto da cena cai para uns 30% de opacidade. É esse escurecimento que marca o trecho como hipótese, e não como evento. (3) `Flash` no `M` fantasma e o `lista_b` colapsando num valor só, um dos que estavam ali. (4) O `pergunta_r` vira `VERMELHO` — que já é a cor de *isto não funciona* no `C11N38` — e é aqui que a fala diz "o r", pela única vez na série. A letra está na tela desde o `C11N21` sem ninguém a pronunciar; ela ganha nome no instante em que perde a resposta, e o `r = 6` do `C11N39` vira a resposta desta pergunta. (5) Tudo desfaz — opacidade de volta, coluna de volta, `M` fantasma sai, `pergunta_r` volta ao amarelo. O desfazer é o argumento, não um detalhe: a medida **não** aconteceu, e por isso o `C11N23` encontra a cena como o `C11N21` a deixou. Nada aqui pode reaproveitar o `med` do `C11N18`: aquele é o `M` de verdade, no fio de baixo, e confundir os dois desfaz a distinção que a batida inteira existe para fazer |
| C11N23 | That's why, before measuring, we send the top wires through the quantum Fourier transform: it's what recovers the information about r. | 8,1 | `Indicate(VGroup(*fios[:4]), color=AZUL, scale_factor=1.0)` **antes** do `FadeIn(tqf)` — a fala nomeia os fios de cima antes de nomear a transformada, e o destaque acompanha a palavra. `scale_factor=1.0` porque um fio esticado sai do quadro. Depois `FadeIn(tqf)` + `Write(rot_tqf)` |
| C11N24 | It always works at a fixed size: a power of two that's large enough. | 5,4 | `FadeIn(nq)` — a igualdade `N = 2⁹ = 512` em cima da caixa. O que fica em cena espera em `cena.grupo_circuito`, com o painel de cima desmontado em fundo, `⋮` e coluna viva |
| C11N25 | So let's step into the transform, taking with us only the exponents that survived the collapse, and the question we still can't answer. | 8,8 | **Animação reescrita — a entrada na transformada.** Três coisas num `play` só. (1) O `tqf` cresce até ser o quadro inteiro e só então o cinza abre: não é um `FadeOut` da caixa em cima do fio, é a câmera entrando nela — o espectador tem de entender que o que vem a seguir acontece dentro dela. O `rot_tqf` **não** cresce junto: ele vai para o canto superior esquerdo e fica de título até o `C11N29`, dizendo que tudo ali é dentro da transformada. (2) Todo o resto do `cena.grupo_circuito` sai: `eqc`, `fios`, `kets`, `keta`, `vd`, `inis`, `portas`, `plugues`, `retic`, `med`, `cartao_c[0]`, `cnum` e o fundo `carta_b[0]`. (3) Quatro peças **não** saem: o `lista_b` — a coluna viva de expoentes —, o `carta_b[2]` — o `⋮` embaixo dela, que o `C11N26` transforma no quinto dente —, o `pergunta_r` e o `nq`. Os três primeiros atravessam a expansão e pousam no centro do quadro, a coluna com o `⋮` embaixo e o `r = ?` acima dela; o `nq` encolhe para um canto, porque ele é o tamanho do registrador e o `C11N28` vai precisar dele quando a reta chegar a 512. **O `sub` deixa de existir**: a implicação `2^b ≡ 4 (mod 21) ⇒ b ∈ {2, 8, 14, 20, …}` era a ponte entre o circuito e a reta, e a coluna virando pente faz essa ponte sozinha, com o mesmo conteúdo e sem texto nenhum. Isso apaga o `Write(sub)` daqui e o `Circumscribe(sub[5])` do `C11N26` |
| C11N26 | On the line, we notice they aren't scattered at random: they show up at regular intervals, always the same distance apart. | 8,1 | `Create(retaZ)` + `FadeIn(rotZ)` abrindo o bloco — a reta nasce debaixo da coluna que já está em cena desde o `C11N25`. Depois **o pente nasce da coluna, e é essa a mudança**: cada número do `lista_b` viaja por `ReplacementTransform` até a sua posição na reta e vira o `rotulos_b` de lá, com o dente crescendo por baixo dele em `GrowFromEdge(d, DOWN)` no mesmo `play`. São quatro números do painel para quatro dentes; o quinto dente, o do 26, nasce do `⋮` da coluna — o "e assim por diante" do painel vira o primeiro dente que ninguém tinha escrito, e é ele que autoriza o `C11N28` a estender o pente. **Não há mais `Circumscribe`**: o "eles" da fala é a própria coluna se transformando, que é o antecedente mais forte que a tela pode dar. Os dentes são **azuis**: cada dente é um expoente, e um pente verde diria que ali é uma fila de restos |
| C11N27 | And that distance is exactly the order we're looking for. | 3,8 | `LaggedStart` das chaves laranjas entre dentes consecutivos, e o rótulo de cada chave é um `r` amarelo nascendo por `TransformFromCopy` do `r` do `pergunta_r` — **não** um `+6`. O `pergunta_r` fica em cena como está: `r = ?`. **Esta linha não revela o valor de r, e isso é a correção de conceito mais importante do capítulo.** O pente é o estado *dentro* da transformada, e nada ali é observável: se a tela escrever `r = 6` aqui, o espectador entende que a transformada entrega a ordem, e o resto do capítulo — ondas, interferência, medida, frações contínuas — vira enfeite. O que esta linha diz é *onde* a ordem está escrita (no espaçamento), não *quanto* ela vale. O valor só aparece no `C11N38`, depois da medida, e é lá que o `r = ?` vira `r = 6` |
| C11N28 | Zooming out, we can see the pattern repeats all the way to the end of the register. | 6,5 | Três `play` emendados: saem os rótulos e as chaves **antes** da compressão, para nada se sobrepor; a reta curta vira a reta inteira levando os cinco dentes junto; e o resto do pente cresce num `LaggedStart` de lag baixíssimo. No terceiro `play`, `Indicate(nq)` — o `N = 2⁹ = 512` está guardado no canto desde o `C11N25` e "o fim do registrador" é exatamente ele. Sem esse destaque o número fica em cena sem nunca ser cobrado |
| C11N29 | What the transform does is swap each of these exponents for a cosine wave, and each exponent gives a different frequency. | 8,1 | **Bloco reescrito — o instrumento das ondas, na estrutura do `qft_shor_ondas_N512.html`.** Primeiro `play`, como está: saem as peças de dentro da caixa, o pente sobe para o alto e o `r = ?` encolhe para a borda direita. **O `titulo` "cada b vira uma onda em k" sai do capítulo** — era uma frase solta que ninguém sabia ler, e a fala já diz a mesma coisa. Depois, no lado direito do quadro, quatro linhas de onda, uma por expoente (`b` = 2, 8, 14, 20), empilhadas: cada uma é `cos(2π·b·k/N)` com `k` de 0 a 512 no eixo horizontal, em `AZUL`. **Cada onda nasce por `TransformFromCopy` do dente correspondente do pente lá em cima** — os quatro primeiros dentes são exatamente esses quatro `b` —, com o rótulo `b = 2` etc. à esquerda da linha. É aí que a frase "cada expoente dá uma frequência diferente" se vê: a de `b = 2` faz duas oscilações no quadro, a de `b = 20` faz vinte. Embaixo das quatro, `⋮` e `+81 ondas` em `CINZA`: o pente tem 85 dentes. O lado esquerdo do quadro fica vazio de propósito — é onde o círculo entra no `C11N30` |
| C11N30 | Then it adds up all these waves: at each point, each wave becomes an arrow, and the arrows are chained tip to tail. | 8,8 | Entram três peças, todas atadas a um `ValueTracker` `k_tr` em `k = 0`. (1) O **cursor**: uma linha vertical tracejada `LARANJA` atravessando as quatro ondas na posição `k`, com um ponto em cada onda na altura em que ela está ali. (2) O **círculo**, no lado esquerdo: um raio por expoente saindo do centro, girado de `2π·b·k/N` — os 85 fracos, e os quatro dos `b` mostrados fortes e rotulados na ponta (`2`, `8`, `14`, `20`). **Os quatro raios fortes nascem por `TransformFromCopy` dos quatro pontos do cursor** — é o "cada onda vira uma seta" da fala; os outros 81 entram por `FadeIn`. Depois, em "emendadas uma na outra", a corrente: as 85 setas em miniatura, ponta com cauda, e a **seta grossa** do centro até a ponta da corrente, que é a soma (`CIANO` quando o módulo passa de 0,6, `LARANJA` abaixo — a convenção da roleta antiga). Em `k = 0` todas apontam para o mesmo lado, então a corrente sai reta e a seta grossa tem o tamanho do raio. (3) O **traço da soma**, embaixo das ondas: uma linha de base com o rótulo `soma` em `CINZA` e, por cima, a curva do tamanho da seta grossa desenhada de 0 até o cursor (`always_redraw`, `CIANO`). Em `k = 0` ela é só um ponto no alto. **Saem do capítulo** a leitura `k = …`, a leitura `|soma| = …`, a barra e os três rótulos de texto da roleta antiga: o traço da soma já mostra o que eles mostravam |
| C11N31 | At most points, the waves fall out of step and the sum almost vanishes. | 5,4 | `k_tr` de 0 a 70 em `linear`, quatro segundos. Tudo anda junto: o cursor corre pelas ondas e os quatro pontos ficam em alturas diferentes; os raios giram cada um num ritmo; a corrente se enrola e a seta grossa encolhe quase a nada; o traço da soma cai do alto e fica rente à base |
| C11N32 | But at a few points they all line up, and the sum shoots up at once. | 6,2 | `k_tr` de 70 a 85 em `ease_out_sine`, três segundos — a desaceleração é o que faz o alinhamento ser lido como chegada. Em `k = 85` os quatro pontos do cursor estão **na mesma altura** (todos perto de −0,47, e não no alto: é o "se encontram" da fala, e ele não é óbvio sem ajuda), então, **depois** do `play`, quatro `DashedLine` horizontais curtas, uma em cada onda, passando pelo ponto dela — entram juntas (`lag_ratio=0`) e saem no mesmo bloco. São quatro e não uma porque as ondas estão empilhadas: uma horizontal só não passa pelos quatro pontos. No mesmo momento, `Flash` na ponta da seta grossa, que está esticada e `CIANO`, e o traço da soma subiu num pico |
| C11N33 | And going all the way to the end of the register, these peaks repeat, always the same distance apart. | 7,3 | `k_tr` de 85 a 511 em `linear`. **A única linha da série em que a animação estoura a locução de propósito**: dez segundos de varredura contra sete e meio de fala. O excedente é o efeito — o traço da soma termina de se desenhar, com os picos surgindo um a um, enquanto a locução seguinte já está para entrar. Não encurtar o `run_time` para caber |
| C11N34 | So we can see the peaks fall on multiples of a single value, and that's what carries the order. | 7,3 | Os updaters param. Saem o círculo inteiro (raios, rótulos, corrente, seta grossa), o cursor com os pontos e as quatro ondas com rótulos, `⋮` e `+81 ondas`. No mesmo `play`, o traço da soma com a base e o rótulo **cresce** para a faixa larga da parte de baixo do quadro — é a mesma peça ficando grande, não uma curva nova. Depois `LaggedStart` das **seis** marcas tracejadas `LARANJA` nos múltiplos de `N/r`, com os rótulos `0` e `1·N/r` a `5·N/r`. **A marca do 0 é obrigatória**: o traço da soma tem um pico em `k = 0` tão alto quanto o de 256 e mais alto que o de 85 (amplitude 1,00 contra 0,83), o espectador acabou de vê-lo se desenhar, e o `C11N35` transforma os rótulos no registrador de saída — sem a marca, o pico some na passagem |
| C11N35 | Back in the circuit, the top register now holds only these peaks, and measuring is finally worth it. | 6,9 | **Bloco reescrito — a câmera sai da transformada.** É o `C11N25` ao contrário e com a MESMA peça: o cinza da TQF fecha sobre o instrumento, encolhe até ser de novo a caixa no fio (`rush_from`, que é o `rush_into` de lá lido ao contrário) e o circuito aparece em volta dela. A caixa volta **recuada**, no lugar que era do painel de entrada: aquele painel foi consumido pelo `C11N26` — virou o pente — e é depois da TQF que o registrador de saída precisa caber, coisa que no lugar antigo dela não cabia (os fios acabam em 6,6 e a caixa ia até 6,38). Por baixo do cinza sai tudo o que era de dentro da transformada: pente, traço, base, rótulo e as linhas das marcas. **Os seis rótulos `0` e `1·N/r` a `5·N/r` atravessam o cinza** — estão por cima dele em `z` — e no `play` seguinte viram as entradas do registrador de saída: um `_carta_super` `LARANJA` depois da TQF, alto o bastante para cobrir os quatro fios de cima, no mesmo vocabulário dos outros dois registradores. **Sem o `⋮`** do helper: ali a lista é completa, são esses seis picos e mais nenhum — e é por isso que o `0` tem de estar nela. No terceiro `play`, `_troca_coluna` põe os inteiros — `0`, `85`, `171`, `256`, `341`, `427` —, que é o que a medida devolve e o que a aritmética do fim usa: enquanto a tela disser `N/r`, o `85` da cascata não tem de onde vir. O `pergunta_r` volta para cima do registrador que vai respondê-lo, como ficava em cima do painel de entrada no circuito |
| C11N36 | Say it comes out eighty-five. | 1,9 | **Linha nova — a medida que vale a pena.** `FadeIn` do `M` cinza no fio, **depois** do registrador de saída: mesmo `caixa_cinza` do `C11N18`, e na linha e no corpo em que o `M` fantasma do `C11N22` ensaiou esta medida e a desfez. No `play` seguinte, `Flash` no `M` e o colapso do `C11N19`: o fundo do painel **fica** — o registrador continua sendo os quatro fios — e a coluna vira um número só. O quadro fecha com os dois registradores lado a lado, cada um com o seu `M` e o seu valor medido: `4` embaixo, `85` em cima. A fala continua sendo uma batida de resposta (exceção 2 da diretriz), e é a única vez que o número é dito — mas o "digamos que" marca a medida como **sorteio** entre os picos, e não como resultado garantido. É ele que prepara o parêntese do `C11N41`: "podia ter caído em outro pico" só faz sentido se a fala daqui não tiver prometido o 85 |
| C11N37 | Divided by the register size, the reading gives a fraction, and the order is hidden in it. | 6,5 | Dois `play`. No primeiro, `FadeOut` do circuito inteiro — com a caixa da TQF, o `M` e o fundo do registrador de saída — emendado com o nascimento de `85 ≈ x · N/r`: o `85` **sai do registrador** e vira o `85` da equação por `ReplacementTransform`, e o resto entra por `Write`. É a equação que os rótulos das marcas já diziam, agora com o valor medido dentro. No segundo, ela vira `85/512 ≈ x/r` — dividir os dois lados pelo tamanho do registrador é exatamente o que a fala diz, e é aí que o `N` vira `512`. Os dois têm sete tokens, então o `85` cai no `85` e o `r` cai no `r`. **Os dois sinais são `≈`, nunca `=`**: `N/r` vale 85,33, e o 85 é o inteiro mais perto. É essa diferença que torna as frações contínuas necessárias no `C11N38` — se fosse igualdade, bastava simplificar a fração |
| C11N38 | So we use continued fractions, an old method, to find the reduced fraction hiding there. | 5,8 | `Write(linhas[1])` e, depois, `Circumscribe(linhas[0][0:3], color=LARANJA)` — o "ali" que fecha a frase é a leitura da **primeira** linha, em cena desde o `C11N37`; a de baixo começa igual mas nasce agora, e por isso fica fora. Laranja é a cor da leitura `k` no ato inteiro |
| C11N39 | And its denominator is the missing order. | 2,7 | `ReplacementTransform(pergunta_r, linhas[2])` — o `r = ?` que está no canto desde o `C11N29` (e que nasceu no `C11N21`) **vira** o `r = 6` da cascata. É o único lugar do capítulo em que o valor de r aparece, e é o lugar certo: depois da medida e das frações contínuas, que é quando o algoritmo de fato o conhece. A pergunta e a resposta são o mesmo objeto na tela |
| C11N40 | Worth checking: the power gives back one, as it should. | 3,8 | `Write(linhas[3])` |
| C11N41 | But the measurement could have landed on another peak. | 3,5 | **Linha nova — o parêntese da medida que não serve.** A cascata inteira cai para 30% de opacidade, que é o device do `C11N22`: marca o trecho como o que **podia** ter acontecido. No mesmo `play`, `TransformFromCopy(linhas[1], …)` — a outra leitura nasce da linha da leitura que valeu, porque é a mesma conta com outro pico dentro: `171/512 ≈ 2/6`. Cada linha escurece sozinha, nunca num `VGroup` novo por cima delas. As três linhas da falha pousam nos lugares que as três últimas da cascata vão ocupar — o espaço está vazio, e o desfazer devolve ele |
| C11N42 | Then the fraction comes out already reduced, and the denominator is only a factor of the order. | 6,5 | Dois `play`. O `2/6` se copia e se reduz a `= 1/3` — **é a linha inteira do argumento**: o pico medido é `x·N/r`, e as frações contínuas só sabem devolver `x/r` na forma reduzida, então quando `x` e `r` têm fator comum (aqui `x = 2`, `r = 6`) o que volta é `r` dividido por ele. O `6` é `AMARELO` porque é a ordem de verdade e o `3` é `VERMELHO` porque é o impostor: a cor conta a redução sozinha. Depois o `r = 3` nasce por `TransformFromCopy` do `r = 6` |
| C11N43 | The check catches it right away, and the fix is to measure again. | 5,0 | Dois `play`. A mesma conferência do `C11N40` nasce dela por `TransformFromCopy` e chega com o resto trocado e o visto virado: `2³ ≡ 8 (mod 21)` `✗`. **É para isto que aquela linha existe** — dos seis picos só o `1·N/r` e o `5·N/r` devolvem 6; o `0` não devolve nada (zero sobre 512 não tem denominador para ler), e os outros três caem aqui. Depois o parêntese fecha: a falha sai e a cascata reacende. O desfazer é o argumento, como no `C11N22`: medir de novo é o que o algoritmo faz, e a medida que vale continua sendo a de 85 |
| C11N44 | From here on it's the whole previous chapter, starting with the difference of squares. | 5,4 | `Write(linhas[4])` |
| C11N45 | Two gcd calculations later... | 1,5 | `Write(linhas[5])` |
| C11N46 | ...and at last the number is factored. | 2,7 | `Write(linhas[6])` + `Create(caixa)`. A moldura verde sobrevive ao capítulo: o `V4N01` pousa o cadeado em cima dela, sem `limpar()` no meio |

**Subtotal: 276,2 s** (cartão + 46 locuções)

---

## Encerramento

O último bloco da série. O cadeado volta pela quarta vez e é a única vez em que ele quebra
de verdade.

| Tag | Speech | Est. | Entra em |
|---|---|---|---|
| V4N01 | That was the promise of the first video: a quantum computer can win the bet that protects the internet. And now we know how. | 9,2 | Mesma composição do `V3N01`, invertida no resultado. A `caixa` verde do `C11N46` desce e vira o pedestal; o cadeado do `V4N00` volta por cima dela, com "fatorar n" gravado e a rachadura parada onde o vídeo 3 deixou. Até "vencer a aposta" ele espera parado no pedestal, enquanto a fala lembra a promessa do vídeo 1. Em "vencer a aposta", a rachadura **termina de correr** pelo arco inteiro, o arco estala em dois e os pedaços caem — a quebra que o `V3N02` prometeu. "E agora a gente sabe como" cai sobre o cadeado já quebrado, sem animação nova |
| V4N02 | But the number we just factored has two digits. RSA numbers have hundreds, and breaking them would take thousands of stable qubits. No machine today comes anywhere close. | 10,8 | Em "tem dois dígitos", o número da moldura verde cresce em quantidade de dígitos até estourar as bordas do quadro. Em "milhares de qubits", um punhado de cartões-qubit do `C11N05` entra ao lado e **continua do mesmo tamanho** enquanto os dígitos correm — a desproporção é o argumento, e nenhuma legenda precisa dizê-la. O cadeado quebrado e a moldura **ficam onde estão, intactos**: nada apaga, nada é empurrado — a faixa dos dígitos corre acima dos cotos e as cartas entram pelo flanco direito, e no fim sai só o que este bloco pôs em cena, para o `V4N03` receber o quadro do `V4N01` sem uma vírgula de diferença |
| V4N03 | So, for now, you can relax: the bet still stands, it just got an expiration date. And the answer is already being prepared: cryptography that doesn't depend on factoring. | 11,2 | A primeira frase ("pode ficar tranquilo") não tem imagem nova: é a fala se dirigindo a quem ouve, com o cadeado quebrado ainda diante dele. Em "a aposta continua de pé", a rede de cadeados anônimos do `V1N03` volta ao fundo, apagada e **intacta** — nenhum dos cadeados dela quebrou. Em "ela só ganhou um prazo de validade", os cacos reacendem e sobem. Em "E a resposta já está sendo preparada", eles se remontam na armação de um cadeado de outra forma, enquanto o velho sai. Em "uma criptografia que não depende de fatorar", ele fecha inteiro no lugar do antigo, com o flash seco do `fechar()` — sem letras gravadas, porque ainda não é assunto desta série |
| V4N04 | Four videos ago, we started with the remainder of a division. Today you understand the algorithm that could change internet security. The path was yours, I just showed you the pieces. Thanks for coming all the way to the end. | 15,4 | A rede, o cadeado novo e a moldura saem no começo. Em "Quatro vídeos atrás", os quatro títulos voltam na trilha vertical do `V1N06`, agora todos acesos. Em "O caminho foi seu", a trilha inteira pulsa uma vez (`Indicate`) — é o caminho que a fala nomeia, e ele já está na tela. Em "Obrigado por ter vindo até o fim", o título da série pousa por cima deles |
| — | *(cartão final, ~3 s)* | — | "Do Zero ao Algoritmo de Shor Quântico" e, embaixo, "fim" |

**Subtotal: 46,6 s** (4 locuções) + cartão ~3 s

---

## Projeção de duração

| Bloco | Locuções | Fala |
|---|---|---|
| Abertura | 1 | 12,3 s |
| Capítulo 9 | 16 | 90,4 s |
| Capítulo 10 | 34 | 191,1 s |
| Capítulo 11 | 47 | 276,2 s |
| Encerramento | 4 | 46,6 s |
| **Total** | **102** | **616,6 s** |

Somando o `PAD` de 0,35 s por locução (35,7 s), os dois cartões silenciosos (~7 s) e os `limpar()` entre capítulos (~10 s), a projeção é de **cerca de 11 min 09 s**. Como no português, `C11N33` tem animação mais longa que a fala e soma uns 3 s ao render real.

---

## Ordem das palavras que a animação exige

Falas em que a tradução manteve a ordem porque a coluna "Entra em" ou o código amarram um gesto a um trecho. As marcadas com ⏱ estão presas a **âncoras por fração** da fala (`shor/sincronias.py`, lista em `roteiros/sincronias.md`), não à ordem dos `play`: em inglês, essas frações precisam ser medidas no áudio e escritas em `SINC["en"]`.

| Tag | Ordem mantida |
|---|---|
| V4N00 | "breaking RSA means factoring" → "the algorithm that does it" → "a long road to get there" |
| C9N02 | "has an inverse" no fim da segunda frase |
| C9N09 | "it just repeats" fecha a fala (a congruência entra aí) |
| C9N13 | "Euler's count" no fim |
| C9N15 | "the smallest exponent" na primeira frase |
| C10N04 | os quatro passos antes do valor ("so the order is four") |
| C10N06 | "a multiple of the number" no fim |
| C10N08 | "the trunk on top" antes de "the factors below" |
| C10N13 | "factors of thirty-five" antes de "the factors of one hundred seventeen" |
| C10N14 | "equality" antes de "the other side" |
| C10N16 | "the two numbers we just computed" antes de "the number we want to factor" |
| C10N22, C10N25 | "also with an even order" e "a multiple of thirty-five" no fim |
| C10N30, C10N31, C10N32 | "Euler's count" no fim; "the private key" antes de "the inverse of the public key"; "the same thing" no fim |
| C11N10 ⏱ | "That's all the physics" no começo; "another example" (âncora `outro exemplo`) |
| C11N22 | as cinco batidas na ordem: probabilidades → uma medida → um valor só → "r" (a única vez que a letra é falada) |
| C11N23 | "the top wires" antes de "quantum Fourier transform" |
| C11N30 | "at each point" → "each wave becomes an arrow" → "chained tip to tail" |
| C11N38 | "there" fecha a frase (o `Circumscribe` no 85/512) |
| V4N01 ⏱ | "win the bet" (âncora `vencer a aposta`) |
| V4N02 | "has two digits" → "hundreds" → "thousands of stable qubits" → "No machine today" |
| V4N03 ⏱ | "the bet still stands" → "expiration date" → "the answer is already being prepared" → "cryptography that doesn't depend on factoring" (âncoras `a aposta continua de pé` / `prazo de validade` / `a resposta já está` / `não depende de fatorar`) |
| V4N04 ⏱ | "Four videos ago" → "The path was yours" → "Thanks for coming all the way to the end" (âncoras `o caminho foi seu` / `obrigado`) |

---

## Checklist de gravação

- [ ] Abertura — V4N00
- [ ] Cartões — CAP09 a CAP11
- [ ] Capítulo 9 — C9N01 a C9N15
- [ ] Capítulo 10 — C10N01 a C10N33
- [ ] Capítulo 11 — C11N01 a C11N46
- [ ] Encerramento — V4N01 a V4N04
- [ ] `python medir.py en`
- [ ] Render de conferência: `IDIOMA=en manim -pqh --media_dir media/en filme_shor.py VideoShor`
