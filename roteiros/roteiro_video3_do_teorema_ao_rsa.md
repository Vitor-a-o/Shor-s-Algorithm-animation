# Corpo — Vídeo 3: Do teorema ao RSA

Capítulos 6 a 8, na ordem de montagem.

---

## Abertura

| Tag | Fala | Est. | Entra em |
|---|---|---|---|
| — | *(cartão silencioso, ~4 s)* | — | "Do Zero ao Algoritmo de Shor Quântico" nasce no centro e "Vídeo 3 de 4 — Do teorema ao RSA" embaixo dele. Mesma emenda do vídeo 2: o subtítulo sai primeiro e o título encolhe por último, já com o `CAP06` entrando por baixo |
| V3N00 | O vídeo anterior montou quatro operações dentro de um módulo. Este constrói com elas o RSA — passando antes por dois teoremas. | 8,8 | Os quatro símbolos do `V2N00` voltam em fila, acesos. Em "constrói com elas o RSA", eles se fecham em volta do cadeado do vídeo 1, que entra no centro **intacto**. Em "dois teoremas", duas lacunas vazias se abrem entre a fila e o cadeado — os lugares que os capítulos 6 e 7 vão ocupar |

**Subtotal: 8,8 s** (1 locução) + cartão ~4 s

---

## Capítulo 6 — Pequeno Teorema de Fermat

| Tag | Fala | Est. | Entra em |
|---|---|---|---|
| CAP06 | Com as quatro operações prontas, entra o primeiro teorema da série. | 4,6 | cartão |
| C6N01 | Essa é a mesma tabela mostrada no capítulo anterior, agora com módulo sete. | 5,4 | `head_c` + `head_l` + `lin_h` + `lin_v` e o `LaggedStart(linhas_cel)` correm emendados, num bloco só |
| C6N02 | Podemos notar que a primeira linha são os possíveis restos não nulos da divisão por sete. | 6,7 | `Create(el1)` e o `TransformFromCopy(linhas_cel[0] → A)` emendados |
| C6N03 | Agora multiplicamos cada um deles por um mesmo número qualquer. | 4,2 | `prods` — cada `3·j` nascendo do vermelho de `head_l[2]` e do próprio `A[j]` |
| C6N04 | E reduzimos cada produto pelo módulo. | 2,5 | `FadeIn(mod_rot)` + `TransformFromCopy(prods → B)` |
| C6N05 | O resultado é o mesmo que a linha do multiplicador que utilizamos. | 5,0 | `Create(el3)` + `Indicate(head_l[2])`, as `copias` caindo exatamente em cima de `B`, e o `FadeOut(copias)` + `Indicate(B)` — os três `play` num bloco só |
| C6N06 | Os números são os mesmos mas em outra ordem. E isso vale para qualquer multiplicador: ele só reordena a linha. | 8,3 | `LaggedStart(Create(arcos))` |
| C6N07 | Como a ordem não importa na multiplicação, podemos fazer a seguinte congruência. | 5,0 | `eq0` e, emendados, o `FadeIn(nota)` com o `ReplacementTransform(eq0 → eq)`; a `nota` sai no mesmo movimento |
| C6N08 | Como vimos no capítulo anterior, restos que não têm fator comum com o módulo possuem inverso. | 6,7 | `FadeIn(nota2)` |
| C6N09 | Como o módulo é primo, todo fator dessa lista tem inverso: podemos dividir o produto inteiro dos dois lados e simplificar. | 8,8 | `Write(div_e)` + `Write(div_d)` |
| C6N10 | O que sobra é uma potência congruente a um módulo sete. | 4,6 | `resultado` |
| C6N11 | Quando o módulo é primo, essa equivalência é generalizada para um valor a que não seja zero ou múltiplo do módulo. | 8,8 | `Write(geral)`, ainda no rodapé ([0, −3,35, 0]) e no tamanho de hoje |
| C6N12 | Esse é o Pequeno Teorema de Fermat. | 2,9 | **A virada.** Um `play` só: a tabela inteira, `el1`, `el3`, `A`, `B`, `prods`, `mod_rot` e `arcos` saem em `FadeOut`, e **no mesmo bloco** o `geral` sobe para [0, −0,5, 0] e cresce de 28 para 40 — ele não é reposicionado depois da limpeza, ele **sobrevive** a ela. O `resultado` sai meio segundo atrasado em relação ao resto (`lag_ratio` ou `FadeOut` próprio), para que o caso particular seja a última coisa a desaparecer debaixo do geral. Fechando o bloco, `titulo = T("Pequeno Teorema de Fermat", 40)` nasce em [0, 0,9, 0] por `Write` |
| C6N13 | Repare na condição: o módulo precisa ser primo. É ela que vai quebrar no próximo capítulo. | 6,7 | Título e equação parados em cena. Em "precisa ser primo", `Indicate` no `(n primo)` cinza que o `geral` já carrega |

**Subtotal: 80,2 s** (cartão + 13 locuções)

---

## Capítulo 7 — A generalização de Euler: φ(n)

| Tag | Fala | Est. | Entra em |
|---|---|---|---|
| CAP07 | O Teorema de Euler é uma generalização do teorema visto no capítulo anterior. | 5,4 | cartão |
| C7N01 | Vamos tentar fazer os mesmos passos, porém agora com a tabela do módulo nove, que não é primo. | 7,5 | headers + `linhas_cel` num bloco só |
| C7N02 | Escolhemos um multiplicador para a lista de restos. | 3,3 | `Create(el2)` + `Indicate(head_l[1])` emendados com `Write(eq)` |
| C7N03 | E aqui vem o passo que fez Fermat funcionar: cancelar a lista dos dois lados. | 6,2 | `Write(div_e)` + `Write(div_d)` |
| C7N04 | Só que cancelar é multiplicar pelo inverso, e dois desses fatores não têm inverso, pois compartilham fator com o módulo. | 8,3 | `FadeIn(exp1)` + `Write(exp2)` emendados |
| C7N05 | São exatamente as linhas que o capítulo cinco já tinha marcado como mortas. Então o cancelamento não é permitido, e a congruência não vale. | 10,0 | as linhas 3 e 6 apagando + os `Indicate`, o `Wiggle` e o `Transform(eq[1] → neq)` — os três `play` num bloco só |
| C7N06 | A saída de Euler é simplesmente não incluir os números que não têm inverso. | 5,8 | `Create(cruzes)` + `Create(cruzes_eq)` + saída de `exp1`/`exp2` |
| C7N07 | Assim sobram só os números que não compartilham fator com o módulo. | 5,0 | `FadeIn(sobr)` — `play` próprio |
| C7N08 | E a contagem deles é dada pela função totiente de Euler, que se escreve fi de ene. | 7,1 | `Write(phi)` — `play` próprio. É aqui, e só aqui, que o símbolo ganha nome falado: o capítulo 8 diz "fi de ene" sete vezes e depende desta emenda |
| C7N09 | Com a lista refeita, a mesma conta roda de novo. | 4,2 | `ReplacementTransform(eq → eq2)` + `FadeOut(cruzes_eq)` |
| C7N10 | Agora todo fator tem inverso, e o cancelamento é legítimo. | 4,2 | `div2_e` + `div2_d` |
| C7N11 | Sobra outra vez uma potência congruente a um, desta vez módulo nove. | 5,0 | `res` |
| C7N12 | Ele vale para qualquer módulo, e o expoente deixou de ser o módulo menos um: agora é a função totiente. | 8,3 | `Write(geral)`, ainda no rodapé e no tamanho de hoje. **Sem** o `Create(caixa)` |
| C7N13 | Esse é o Teorema de Euler. | 2,5 | **A virada, espelhando o `C6N12`.** Um `play` só: `head_c`, `head_l`, `lin_h`, `lin_v`, `linhas_cel`, `el2`, `cruzes`, `sobr`, `phi`, `eq2`, `div2_e` e `div2_d` saem em `FadeOut`, e no mesmo bloco o `geral` sobe para [0, −0,5, 0] e cresce de 28 para 40. O `res` sai meio segundo atrasado, como o `resultado` no capítulo 6. Fechando, `titulo = T("Teorema de Euler", 40)` nasce em [0, 0,9, 0] por `Write` |
| C7N14 | Guarde essa fórmula: o próximo capítulo sai inteiro dela. | 3,8 | Título e equação parados em cena. Em "sai inteiro dela", `Indicate` no `φ(n)` do expoente — é exatamente a peça que o capítulo 8 vai consumir |

**Subtotal: 86,6 s** (cartão + 14 locuções)

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

| Tag | Fala | Est. | Entra em |
|---|---|---|---|
| CAP08 | Com os dois teoremas prontos, falta ver o que o RSA precisa resolver. | 5,4 | cartão |
| C8N01 | O problema que o RSA resolve nasce com duas pessoas que nunca se falaram precisando trocar uma mensagem por um caminho público. | 9,2 | `FadeIn(p['cenario'])` + `FadeIn(olho)` emendados — a `DashedLine` cinza com as duas pontas e os rótulos "quem envia"/"canal público"/"quem recebe" nasce junto com o olho vermelho, achatado e fechado. Depois `FadeIn(caixa)`, a caixa `SEGREDO` legível subindo de baixo. Por fim `atravessar(caixa, RIGHT)`: desliza até o centro e dali até a ponta direita — no meio do caminho uma cópia sobe até a prateleira (vaga 0) e, por ser a primeira captura, o olho se abre e a `prat` nasce por `Create`, tudo dentro dos dois `play` da própria função |
| C8N02 | Aplicar uma criptografia de chave simétrica resolve metade do problema: a mensagem que trafega deixa de fazer sentido para terceiros. | 8,3 | `FadeOut(caixa)` + `esvaziar()` da prateleira + `FadeIn(pacote[0])` emendados — a caixa legível dá lugar à caixa-pacote vazia. Depois `FadeIn(chave, shift=DOWN)` + `FadeIn(pacote[1])`, o cadeado aberto, emendados. Em seguida `trancar(pacote, ...)`: um único `play` gira o arco, dispara o `Flash` seco, embaralha as sete letras (`SEGREDO → Xk9#R2q`) e vira o fundo verde. Depois `atravessar(pacote, RIGHT)` (dois `play`) e, por fim, `FadeIn(xis)` sozinho |
| C8N03 | Só que quem tranca e quem abre a mensagem usam a mesma chave, e ela também tem que atravessar o canal. | 8,8 | `chave.animate.move_to(canal)` sozinho, descendo até a linha. Depois `atravessar(chave, RIGHT, vaga=1)` (dois `play`), parando antes da ponta — a cifra já ocupa a marca. Por fim `chave.animate.move_to(...)`, descendo até o ponto médio entre as duas marcas onde o par do `C8N05` vai pousar |
| C8N04 | Um intruso ouvindo o canal pega as duas coisas juntas, e abre a mensagem com a própria chave que a trancou. | 8,8 | `Indicate(prateleira[1], color=AMARELO)` sozinho — os dois objetos capturados, juntos, na prateleira. Depois a chave sobe até ficar ao lado do cadeado capturado (`prateleira[1].animate.next_to(...)`), `abrir(prateleira[0], ...)` destrava e desembaralha as letras num `play` só, a chave volta para a vaga, `FadeOut(xis)` e, fechando, `piscar(VERMELHO)` (dois `play`: preenche e some) |
| C8N05 | O RSA é uma das saídas para isso ele usa duas chaves diferentes, uma que tranca e outra que abre. | 8,3 | `FadeOut` do que restou na prateleira e do pacote, sozinho. Depois `Indicate(chave, color=AMARELO)`. Por fim, num único `play`, a chave amarela vira duas cópias e cada uma sofre `ReplacementTransform`: uma para `ch_pub` (chave cinza) e outra para `ch_priv` (chave amarela) — ela se parte em duas **chaves**, não em cartões. São essas duas chaves, não retângulos vazios, que voltam para virar os cartões `(e, n)` e `(d, n)` no `C8N22` e no `C8N24` |
| C8N06 | Quem vai receber a mensagem envia pelo canal sua chave que tranca. Ela pode ser vista por todo mundo, porque com ela só é possível trancar, por isso ela é chamada de chave pública. | 14,0 | `ch_pub.animate.move_to(canal)` sozinho. Depois `atravessar(ch_pub, LEFT)` — dois `play`, o único percurso da fase 0 no sentido contrário, e mais lento (`rt=2.8`) que qualquer outro. Por fim `ch_pub.animate.move_to(...)`, pousando na ponta esquerda |
| C8N07 | Quem envia tranca a mensagem com ela — e nem ele mesmo consegue voltar atrás. A chave que fecha não abre. | 8,3 | `FadeIn(pacote[0])` + `FadeIn(pacote[1])` emendados — a caixa e o cadeado aberto nascem na ponta esquerda. `ch_pub.animate.move_to(mão)` sozinho, depois `trancar(pacote, ...)` num `play`. Em seguida o arco tenta ceder no sentido de abrir e volta, em dois `Rotate` opostos e curtos — a chave cinza tentando voltar atrás. Fechando, `Wiggle(pacote[1])` + `FadeIn(x2)` emendados e, por fim, `FadeOut(x2)` sozinho: quem trancou também ficou de fora |
| C8N08 | O intruso pega tudo o que atravessou o canal, a chave pública e a mensagem trancada, e nada disso é suficiente para abrir. | 9,5 | `atravessar(pacote, RIGHT)` (dois `play`) — a mesma vaga do `C8N04`. Depois `Indicate(prateleira[1], color=CINZA)` sozinho. Por fim `Wiggle(prateleira[0][1])` + `FadeIn(xis)` emendados: o intruso aplica a chave cinza, o cadeado chacoalha e não abre |
| C8N09 | A chave que abre nunca entra no canal, por isso ela também é chamada de chave privada. | 7,0 | `Indicate(ch_priv, color=AMARELO)` sozinho — ela está parada na ponta direita desde o `C8N05` e nunca se moveu. Depois `ch_priv.animate.move_to(mão)`, `abrir(pacote, ...)` num `play` (letras desembaralham, `SEGREDO` reaparece legível) e, fechando, `piscar(VERDE)` (dois `play`) |
| C8N10 | Na aritmética, isso é um par de operações: uma que qualquer um faz, e outra que ninguém desfaz sem uma informação que a primeira não entrega. | 10,8 | Um `play` só apaga o pacote, a prateleira e o `prat`, some com o `xis`, e ao mesmo tempo o `olho`, `ch_pub` e `ch_priv` caem para opacidade 0,3 e voltam para as marcas de pouso, nas duas pontas. Depois `GrowArrow(ida)` verde sozinho, `GrowArrow(volta)` vermelha sozinha — o mesmo gesto do `V1N01` — e por fim `LaggedStart(FadeIn(cacos))`, os "?" que despedaçam a seta de volta. É a promessa que o `C8N36` vai cobrar |
| C8N11 | Vamos começar com o Teorema de Euler e mostrar como essas operações surgem dele. Para isso, fazemos algumas manipulações na congruência. | 8,8 | `ReplacementTransform(fase0['ida'] → L)` — o `L` nasce de dentro da seta verde —, emendado com o `FadeOut` do `cenario`, do `olho`, da seta despedaçada (`fase0['volta']`) e das duas chaves (`fase0['pub']`, `fase0['priv']`), tudo num só `play`. Depois, sozinho, `Indicate(L[0][1], color=LARANJA)` no `φ(n)` do expoente — o gancho que o `C7N14` deixou |
| C8N12 | Esse número a é a mensagem — todo texto vira número antes de entrar aqui. Multiplicamos os dois lados por ele. | 8,3 | `FadeIn(msg_fig)` sozinho — a caixa `SEGREDO` figurativa volta pequena, ao lado do `L`. Depois, num `play` só, os sete glifos somem em `LaggedStart(FadeOut(..., target_position=L[0][0], scale=0.3))`, voando para dentro do `a`, enquanto o fundo da caixa se apaga por trás — é a única vez que a mensagem figurativa vira número. Depois `Indicate(L[0][0], color=ROXO)` sozinho, no `a` — a única parada da dedução para dizer o que a letra é. Por fim `ReplacementTransform(L → L2)` |
| C8N13 | Do lado esquerdo, os expoentes se somam. | 2,9 | `ReplacementTransform(L2 → L3)`, sozinho |
| C8N14 | E aqui está a peça central, o expoente pode ser reescrito como módulo fi de ene. | 6,7 | `ReplacementTransform(L3 → L4)` sozinho. Depois, emendados num `play` só, `Indicate(L4[3], color=LARANJA)` no `(mod n)` do rodapé e `Indicate(L4[0][1], color=LARANJA)` no `(mod φ(n))` que acabou de nascer no expoente — os dois módulos têm que ser vistos juntos |
| C8N15 | Qualquer expoente que deixe resto um nesse módulo devolve a mesma mensagem. É dessa liberdade que o RSA inteiro é feito. | 8,8 | `so_fala` — linha sem animação, o `L4` fica parado em cena |
| C8N16 | Voltamos à tabela de multiplicação, mas agora ela vale para o expoente. | 5,0 | `FadeIn(tabela)` — a grade módulo `φ(n)` com a legenda — emendado com `FadeOut(dir4)`: o `≡ a (mod n)` do lado direito do `L4` sai da tela no mesmo `play` e só volta no `C8N18` |
| C8N17 | Cada círculo verde é um par de inversos. É isso que procuramos: dois números cujo produto dê um, no módulo do expoente. | 9,2 | `LaggedStart(Create(uns))` + `Write(ed)` emendados com `FadeIn(nota)` e os dois `Indicate(celulas[2][5])`/`Indicate(celulas[5][2])` — tudo num `play` só |
| C8N18 | Esse par pode então substituir o expoente. | 2,9 | Um `play` só: `ReplacementTransform(L4[0] → L5[0])` — a potência ganha o produto `e·d` no expoente — emendado com `FadeIn(VGroup(L5[1], L5[2], L5[3]), shift=RIGHT)`, o lado direito guardado no `C8N16` voltando, e `Indicate(ed, color=VERDE)` |
| C8N19 | E um produto no expoente é o mesmo que uma potência de outra potência: duas operações encadeadas, uma desfazendo a outra. | 8,8 | `ReplacementTransform(L5 → L6)` emendado com o `FadeOut` da `tabela`, dos `uns`, da `nota` e do `ed`, num `play` só. Depois `Indicate(L6[0][0][1][1], color=VERMELHO)` sozinho, no expoente `e`. Por fim, depois de meio segundo de silêncio, `Indicate(L6[0][1], color=AZUL)` no expoente `d` — o par de setas do `C8N10` virando álgebra, um de cada vez, com pausa entre as duas |
| C8N20 | Cada peça da fórmula ganha um papel, começando pela mensagem. | 4,2 | Um `play` só: `Indicate(L6[2], color=ROXO)` no `a`, emendado com `FadeIn(p['cenario'])`, `FadeIn(p['olho'])` (opacidade de volta a 1), `FadeIn(p['prat'])` e `FadeIn(pacA)` — a caixa com o `a` roxo dentro, na ponta esquerda. Depois, sozinho, `FadeIn(ch_pub)` + `FadeIn(ch_priv)`: as duas chaves da fase 0 (`fase0['pub']`/`fase0['priv']`) voltam com a opacidade restaurada, na mão de quem recebe — nenhuma das duas nasce do zero |
| C8N21 | A primeira potência junto com o módulo embaralham a mensagem, e o resultado é a cifra. | 6,6 | `ch_pub.animate.move_to(canal)` + `ch_priv.animate.move_to(Y_POUSO)` emendados. Depois `atravessar(ch_pub, LEFT)` (dois `play`) — o mesmo percurso invertido do `C8N06`. Em seguida `ch_pub.animate.move_to(mão)` + `Write(f1s)` (`aᵉ (mod n)`) emendados. Por fim `trancar(pacA, pot('a', 'e', BRANCO, BRANCO))` sozinho: a primeira potência é o próprio embaralhamento |
| C8N22 | Estes são a chave pública que circulou. | 2,9 | Um `play` só: `ReplacementTransform(ch_pub → rpub)` — a mesma chave cinza da fase 0 vira o retângulo, não um cartão novo — emendado com o `FadeIn` dos parênteses e vírgula de `pública(e, n)` e o `e`/`n` chegando por `ReplacementTransform` de cópias de `f1s`. Depois `pubS.animate.move_to(pouso)` sozinho. A identidade se mantém: `fase0['pub']` é o mesmo objeto que se torna `rpub` |
| C8N23 | A segunda potência desfaz a primeira e devolve a mensagem original. | 4,6 | `atravessar(pacA, RIGHT)` (dois `play`). Depois, emendados, `FadeIn(p['xis'])` + `ch_priv.animate.move_to(mão)` + `Write(f2s)` (`(aᵉ)ᵈ (mod n)`). Por fim `abrir(pacA, T('a', ROXO))` sozinho — a segunda potência devolve o `a` |
| C8N24 | E o expoente que desfaz junto com o módulo é a chave privada — essa não sai da mão de quem recebe. | 9,1 | Um `play` só: `ReplacementTransform(ch_priv → rpriv)` — a chave amarela da fase 0 virando o retângulo — emendado com o `FadeIn` de `privada(d, n)` e o `d`/`n` chegando de cópias de `f2s`. Depois `piscar(VERDE)` (dois `play`) e, por fim, `privS.animate.move_to(pouso)` sozinho |
| C8N25 | O esquema está montado. Falta ver ele rodar com números. | 4,2 | Um `play` só: `FadeOut` de `pacA`, `f1s`, `f2s`, `pubS`, `privS` e `L6`, junto com `FadeOut` do `cenario`, do `olho`, do `prat`, do `xis` e do que sobrou na prateleira |
| C8N26 | Quem vai receber escolhe o módulo de uma maneira específica, que vai ser mostrada mais para frente. | 7,1 | `Write(esc)` + `Write(E1)` emendados. Depois `FadeIn(inter, shift=DOWN)` sozinho — o "?" cinza nasce colado no `33`, marcando a dívida que o `C8N42` paga |
| C8N27 | Com o módulo na mão, ele calcula fi de ene — o módulo do expoente. | 5,8 | `Write(phi)` + `ReplacementTransform(E1 → E2)` emendados, num `play` só |
| C8N28 | E procura ali um par de inversos. | 2,9 | Dois `play` separados: `Write(ed2)` primeiro, depois `ReplacementTransform(ed2 → edn)` |
| C8N29 | As duas chaves nascem desse par: uma leva cada expoente, e as duas levam o mesmo módulo. | 7,1 | Dois `play`, um por cartão: primeiro `Create(pub[0])` com `pública(3, 33)` se preenchendo, o `3` puxado de `edn` e o `33` de `esc` por `ReplacementTransform`; depois o mesmo para `priv[0]` e `privada(7, 33)` |
| C8N30 | A fórmula geral se preenche com os números escolhidos. | 3,8 | Dois `play` separados: `ReplacementTransform(E2 → E3)` emendado com `Indicate(edn, color=VERDE)`, depois `ReplacementTransform(E3 → E4)` sozinho |
| C8N31 | Falta a mensagem, que deve ser um número menor que o módulo. | 5,0 | `FadeOut(phi)` + `FadeOut(edn)` + `LaggedStart(Write(msg_esc))` (em duas partes: "mensagem: a = 5" e, por último, "< 33"), tudo num `play` só. A condição `a < n` não é decorativa: com a mensagem maior que o módulo, a volta devolve o resto e o exemplo da tela para de fechar |
| C8N32 | E ela entra no lugar da letra. | 2,9 | `ReplacementTransform(E4 → L7)` + `Indicate(msg_esc, color=ROXO)`, num `play` só |
| C8N33 | Quem envia a mensagem usa a chave pública para trancá-la. | 4,6 | Um `play` grande: `inter` desliza até o `33` do módulo (a dívida se transfere), `FadeOut(esc)`, `FadeIn` do `cenario`/`olho`/`prat`/`pacB` (a caixa com `5` roxo), `pub` encolhe e desce até a mão, uma cópia dela (`pub_olho`) encolhe mais e sobe direto para a prateleira — o intruso já fica com a pública à vista —, `priv` encolhe e pousa na ponta direita, e `Write(f1)` (`5³ ≡ 26 (mod 33)`) — tudo junto. Depois `trancar(pacB, T('26', BRANCO))` sozinho e, por fim, `atravessar(pacB, RIGHT)` (dois `play`) |
| C8N34 | Somente quem tem a chave privada desfaz a cifra. Mais ninguém. | 4,6 | `FadeIn(p['xis'])` + `pub.animate.move_to(pouso)` + `priv.animate.move_to(mão)` + `Write(f2)` (`26⁷ ≡ 5 (mod 33)`), emendados num `play` só. Depois `abrir(pacB, T('5', ROXO))` sozinho, `piscar(VERDE)` (dois `play`) e, por fim, `priv.animate.move_to(pouso)` sozinho |
| C8N35 | A verificação é a dedução do começo do capítulo, com números no lugar das letras. | 6,3 | Dois `play` separados: `Write(fim2)` primeiro (a cadeia `(5³)⁷ = 5²¹ = 5²⁰·5 ≡ 1·5 ≡ 5 (mod 33)`), depois `ReplacementTransform(fim2 → fim3)`, a versão enxuta com `✓` |
| C8N36 | Falta a pergunta que decide tudo: se a chave pública e a privada são inversas módulo fi de ene, não seria fácil encontrar a privada a partir da pública? | 12,1 | Um `play` grande apaga o exemplo inteiro — `pacB`, `f1`, `f2`, `pub`, `priv`, `L7`, `fim3`, `msg_esc`, `inter` — junto com `cenario`, `olho`, `prat`, `xis` e o que sobrar na prateleira. Depois `FadeIn(volta)` sozinho — a seta despedaçada do `C8N10`, recentrada — e `FadeOut(volta)` sozinho, cobrando e fechando a promessa. Em seguida `FadeIn(leg)` + `FadeIn(tab)` emendados: a grade módulo 9 nasce com a legenda "tabela multiplicativa (mod φ(n))" em cima. Depois `FadeIn(eixo_e, shift=RIGHT)` + `FadeIn(eixo_d, shift=DOWN)` emendados, nomeando os dois eixos. Por fim `LaggedStart(Create(uns))` — os círculos verdes, um por linha invertível |
| C8N37 | Inverter é fácil para quem conhece o módulo. E o módulo, aqui, é fi de ene. | 6,7 | `FadeIn(faixa)` + `Indicate(_tab_lin(tab, 2), color=VERMELHO)` emendados — a faixa amarela entra pela linha do `e`. Depois `ReplacementTransform(faixa → alvo)` + `Indicate(_tab_cel(tab, 2, 5), color=VERDE)` emendados — a faixa encolhe até parar na célula com `1`. Depois `Indicate(_tab_col(tab, 5), color=AZUL)` sozinho, saindo pela coluna do `d`. Depois `Write(c1)` sozinho (`achar d ⇒ achar φ(n)`). Por fim `Indicate(phin, color=LARANJA)` + `Indicate(VGroup(lphi[1], lphi[2], lphi[3]), color=LARANJA)` emendados — o `φ(n)` da fórmula e o da legenda acendem juntos |
| C8N38 | E fi de ene é uma contagem: quantos números abaixo do módulo não compartilham fator com ele. | 7,1 | Um `play` grande: a legenda perde o `φ(` e o `)` enquanto o resto vira `(mod n)` por `ReplacementTransform`, `FadeIn(l2)` traz `n = 15`, e a grade módulo 9 (`tab`, `eixo_e`, `eixo_d`, `uns`, `alvo`) some enquanto `tab15` nasce — tudo junto. Depois `LaggedStart(Create(uns15))` sozinho. Depois `LaggedStart(Create(riscos))` sozinho — as linhas que compartilham fator com 15 riscadas uma a uma. Por fim `LaggedStart(Indicate(vivas, color=VERDE))` + `FadeIn(conta)` emendados — as linhas sobreviventes acendem enquanto `φ(15) = 8` aparece embaixo |
| C8N39 | Para um módulo grande, contar um por um é impossível. | 4,2 | Três `play`: primeiro a malha cresce de `tab15` para `malha35` (`ReplacementTransform`), os dígitos e riscos da grade de 15 somem, e a legenda e a contagem viram `n = 35`/`φ(35) = ?`, tudo emendado. Depois o mesmo salto de `malha35` para `malha77`, com `n = 77`/`φ(77) = ?`. Por fim `conta77` encolhe, apaga e viaja até dentro do `φ(n)` do `c1`, emendado com `Indicate(phin, color=LARANJA)` — a contagem que ninguém faz à mão colapsa na fórmula |
| C8N40 | Se o módulo fosse primo, a contagem sairia de graça — nenhum número abaixo de um primo compartilha fator com ele — e qualquer um teria a chave privada. | 11,2 | `FadeOut(malha77)` + `FadeIn(tab11)` + `ReplacementTransform(l2c → l2d)` emendados — a grade vira módulo 11, primo. Depois `LaggedStart(Create(uns11))` sozinho. Depois `LaggedStart(Indicate(tab11[2], color=VERDE))` + `FadeIn(conta11)` emendados — todas as linhas acendem, nenhuma riscada, e `φ(11) = 10` aparece. Depois `Write(c2[0:6])` sozinho (`n primo: φ(n) = n`). Depois `ReplacementTransform(conta11[3].copy() → VGroup(c2[6], c2[7]))` sozinho — o `− 1` chega puxado da própria contagem. Depois `Indicate(VGroup(c2[6], c2[7]), color=LARANJA)` sozinho. Depois `FadeIn(c2[8], scale=1.6)` sozinho — o `✗` que já existe no código. Por fim `Indicate(c1[1], color=AZUL)` sozinho, no `d` — com `φ(n)` de graça, ele sai da pública na mão de qualquer um |
| C8N41 | Com o produto de dois primos, os únicos que compartilham fator são os múltiplos de p e os de q. | 8,3 | `FadeOut(tab11)` + `FadeOut(uns11)` + `FadeIn(tab15b)` + `FadeIn(uns15b)` + `ReplacementTransform(l2d → l2e)` + `ReplacementTransform(conta11 → conta15)` emendados — a grade volta ao módulo 15 do `C8N38`. Depois `Write(c3[0:5])` sozinho (`n = p × q`). Depois `LaggedStart(Create(r_p))` + `Indicate(c3[2], color=ROSA)` emendados — as linhas 3, 6, 9 e 12 riscadas de rosa. Por fim `LaggedStart(Create(r_q))` + `Indicate(c3[4], color=VERDE2)` emendados — as linhas 5 e 10 riscadas de verde-claro |
| C8N42 | Dá para descontar todos de uma vez com uma fórmula, sem ter que contar um por um. | 7,0 | `Write(c3[5:10])` sozinho (`⇒ φ(n) =`). Depois `FadeIn(c3[10])` + `FadeIn(c3[12])` + `ReplacementTransform(c3[2].copy() → c3[11])` emendados — o `(p − 1)` nasce do `p`. Depois o mesmo para o `q`, formando `(q − 1)`. Depois `FadeIn(c3[17], scale=1.5)` + `Indicate(conta15, color=VERDE)` emendados — o `✓` e a contagem da grade fecham juntos. Por fim `LaggedStart(FadeIn(c3b, shift=UP))` sozinho: a linha instanciada `33 = 3 × 11 ⇒ φ(33) = 2 × 10 = 20`, que paga as dívidas abertas no `C8N26` e no `C8N27` |
| C8N43 | Mas o atalho só serve para quem conhece p e q. Quem só possui o produto dos dois teria que fatorar para descobrir. | 9,6 | `ReplacementTransform(l2e → l2f)` + `FadeOut(r_p)` + `FadeOut(r_q)` emendados — a fatoração some da legenda e os riscos somem da grade. Depois `ReplacementTransform(conta15 → conta_q)` sozinho — a contagem volta a ser `φ(15) = ?`. Depois `Indicate(c3[0], color=LARANJA)` sozinho, no `n`. Depois `GrowArrow(volta3)` sozinho — a mesma seta do `C8N10` e do `V1N01`, agora tentando o caminho de volta do `n` para `p × q`. Por fim `LaggedStart(FadeIn(cacos3, shift=UP))` sozinho — ela se despedaça no meio do caminho |
| C8N44 | E a série se fecha em cima de si mesma: quebrar o RSA é fatorar esse número. | 7,1 | Um `play` só: `FadeOut(VGroup(tab15b, uns15b, lpre, ln, l2f, conta_q))` — a coluna da grade sai inteira — emendado com `VGroup(c1, c2, c3, c3b, volta3, cacos3).animate.shift(LEFT)`, a coluna das fórmulas deslizando para o centro. Depois `Write(c4)` + `Create(caixa)` emendados — a tese `quebrar RSA = fatorar n` se desenha devagar dentro do retângulo verde |

**Subtotal: 314,8 s** (cartão + 44 locuções)

---

## Encerramento

| Tag | Fala | Est. | Entra em |
|---|---|---|---|
| V3N01 | Toda a segurança do RSA está apoiada numa única frase: ninguém sabe fatorar um número grande em tempo razoável. | 7,9 | A `caixa` verde do capítulo 8 continua em cena. O cadeado do vídeo 1 volta por cima dela, fechado, e "fatorar n" se grava no corpo dele com o mesmo flash seco do `V1N01` |
| V3N02 | O último vídeo mostra como o algoritmo de Shor faz exatamente isso — e a frase deixa de ser verdade. | 7,9 | Uma rachadura fina corre pelo arco do cadeado e **para no meio**. Ele não quebra: a quebra é o pagamento do vídeo 4 |
| — | *(cartão final, ~3 s)* | — | "Vídeo 4 de 4 — O algoritmo de Shor" |

**Subtotal: 15,8 s** (2 locuções) + cartão ~3 s

---

## Projeção de duração

| Bloco | Locuções | Fala |
|---|---|---|
| Abertura | 1 | 8,8 s |
| Capítulo 6 | 13 | 81,0 s |
| Capítulo 7 | 15 | 86,6 s |
| Capítulo 8 | 45 | 314,8 s |
| Encerramento | 2 | 15,8 s |
| **Total** | **74** | **506,2 s** |

Somando o `PAD` de 0,35 s por locução (25,9 s), os dois cartões silenciosos
(~7 s) e os `limpar()` entre capítulos (~10 s), a projeção é de **cerca de 9 min 09 s** —
passa um pouco da faixa de 8–9 min que a estimativa por `cena.play` previa, puxada pelas
falas reescritas da fase 0 e do fecho. A fase 0 do capítulo 8
responde por ~93,0 s desse total; as fases B e C continuam somando vinte e quatro `play`
sob catorze locuções curtas, porque a tela faz as contas sozinha.

O capítulo 8 sozinho passa de 5 minutos de fala, e a fase 0 segue perto de um quinto do vídeo.
Duas linhas já foram enxugadas ali — a moral do fracasso saiu inteira, e a premissa que o
`C8N03` e o `C8N04` diziam duas vezes agora é dita uma. O que sobrou não tem gordura: o
`C8N06` é o mais longo do bloco porque é ele que carrega a justificativa da fase inteira
(a chave que viaja só fecha), e sem ela o ato 2 vira asserção. Se o vídeo precisar
encurtar, o lugar é o exemplo numérico, não a fase 0 nem a dedução.

Cinco trechos têm animação mais longa que a fala e vão correr um pedaço em silêncio:
`C6N07` (o produto se escrevendo e se condensando sob uma linha só), `C8N04` e `C8N08` (as
duas capturas no meio do canal, com a caixa desembaralhando de um lado e travando do
outro) e `C8N33` e `C8N34` (as duas metades do trânsito da mensagem). Some uns 12 a 15 s
ao render real, mais o que sobrar dos `wait` que não forem absorvidos pelo `PAD`.

---

## Convenção de tags

As tags de cada capítulo são sempre contíguas: começam em `01`, sobem de um em um, sem
buraco e sem repetição. Quando uma linha sai, as seguintes descem; quando uma linha se
parte em duas, as seguintes sobem. A numeração é posição na sequência, não identidade da
fala — o `medir.py` e o checklist de gravação varrem a faixa inteira e uma tag ausente
passa como áudio faltando.

---

## Checklist de gravação

- [ ] Abertura — V3N00
- [ ] Cartões — CAP06 a CAP08
- [ ] Capítulo 6 — C6N01 a C6N13
- [ ] Capítulo 7 — C7N01 a C7N14
- [ ] Capítulo 8 — C8N01 a C8N44
- [ ] Encerramento — V3N01 e V3N02
- [ ] `python medir.py`
- [ ] Render de conferência com `NARRA = True`

---

## Pendências de código do capítulo 6 (`parte6`)

1. `with narra` envolvendo os headers e o `LaggedStart(linhas_cel)` num bloco só
   (`C6N01`).
2. `Create(el1)` emendado com o `TransformFromCopy` da linha 1 (`C6N02`).
3. `Create(el3)` + `Indicate`, o movimento das `copias` e o `FadeOut(copias)` +
   `Indicate(B)` num bloco só (`C6N05`).
4. `eq0` emendado com o `FadeIn(nota)` e o `ReplacementTransform(eq0 → eq)` (`C6N07`).
5. **Separar** `FadeIn(nota2)` de `Write(div_e)`/`Write(div_d)` em dois `play`: hoje rodam
   juntos e a narração precisa de dois tempos (`C6N08` e `C6N09`).
6. **Final novo (`C6N12`)** — o pouso do teorema, em um `play` único:
   - `FadeOut` de `head_c`, `head_l`, `lin_h`, `lin_v`, `linhas_cel`, `el1`, `el3`, `A`,
     `B`, `prods`, `mod_rot` e `arcos`;
   - no mesmo `play`, `geral.animate.move_to([0, -0.5, 0]).scale(40/28)`;
   - `resultado` com `FadeOut` atrasado (~0,5 s) em relação ao resto;
   - `Write(titulo)` fechando o bloco, com `titulo = T("Pequeno Teorema de Fermat", 40)`
     em [0, 0.9, 0].

   Não precisa de ferramenta nova — é `T()`, um `FadeOut` em grupo e um `.animate`. O que
   precisa é que o `geral` **não** seja recriado no centro: tem que ser o mesmo mobject
   viajando, senão a limpeza lê como corte e a equação perde a continuidade.
7. O `(n primo)` cinza que o `geral` já carrega **sobrevive** à limpeza — ele é a hipótese,
   e é o alvo do `Indicate` do `C6N13`.
8. Os `cena.wait(0.5)` entre `prods`/`mod_rot` e entre `mod_rot`/`el3` saem: o respiro
   passa a ser o `PAD` da locução. O `cena.wait(1.6)` final também sai — quem sustenta o
   título em cena agora é o `C6N13`.
9. A saída do título para o cartão `CAP07` precisa ser **um movimento só**, com o
   `limpar()` emendado no cartão. São dois momentos tipográficos de tela cheia em
   sequência, e o mesmo risco que o cartão de abertura do vídeo 2 já tinha: separados,
   leem como dois fins.

## Pendências de código do capítulo 7 (`parte7`)

1. Headers + `linhas_cel` num bloco só (`C7N01`).
2. `Create(el2)` + `Indicate` emendados com `Write(eq)` (`C7N02`).
3. `FadeIn(exp1)` + `Write(exp2)` num bloco só (`C7N04`).
4. As opacidades das linhas 3 e 6, o `Wiggle` e o `Transform(eq[1] → neq)` num bloco só —
   hoje são três `play` (`C7N05`).
5. **Quebrar em três** o `play` que hoje é único: `Create(cruzes)` + `Create(cruzes_eq)` +
   saída de `exp1`/`exp2` (`C7N06`), depois `FadeIn(sobr)` sozinho (`C7N07`), depois
   `Write(phi)` sozinho (`C7N08`). Quem sobrevive e como se chama a contagem são dois
   beats, e a definição de φ é a carga do capítulo — não pode dividir tempo com a saída
   das cruzes.
6. **`Create(caixa)` sai.** O título do `C7N13` assume a função que o retângulo verde
   tinha, e manter os dois deixa a tela com duas molduras concorrendo.
7. **Final novo (`C7N13`)** — mesmo pouso do `C6N12`, em um `play` único:
   - `FadeOut` de `head_c`, `head_l`, `lin_h`, `lin_v`, `linhas_cel`, `el2`, `cruzes`,
     `sobr`, `phi`, `eq2`, `div2_e` e `div2_d`;
   - no mesmo `play`, `geral.animate.move_to([0, -0.5, 0]).scale(40/28)`;
   - `res` com `FadeOut` atrasado (~0,5 s) em relação ao resto;
   - `Write(titulo)` fechando o bloco, com `titulo = T("Teorema de Euler", 40)` em
     [0, 0.9, 0].

   Vale extrair isso e o `C6N12` numa função só em `ferramentas.py` — algo como
   `pousar_teorema(cena, formula, texto, resto)` — já que os dois capítulos fazem
   exatamente o mesmo movimento com objetos diferentes.
8. O `cena.wait(1.6)` final sai: quem sustenta o título em cena agora é o `C7N14`.
9. A saída do título para o cartão `CAP08` precisa ser **um movimento só**, com o
   `limpar()` emendado no cartão — mesma nota do fim do capítulo 6.

## Pendências de código do capítulo 8 (`parte8`)

1. `Write(ed2)` e `ReplacementTransform(ed2 → edn)` ainda são dois `play` separados no
   `C8N28` — falta emendar num só.
2. `ReplacementTransform(E2 → E3)` e `ReplacementTransform(E3 → E4)` ainda são dois `play`
   separados no `C8N30` — falta emendar num só.
3. `Write(fim2)` e `ReplacementTransform(fim2 → fim3)` ainda são dois `play` separados no
   `C8N35` — falta emendar num só.

## Pendências de código da costura (vídeo 3)

- Reaproveitar os quatro símbolos do `V2N00` (`+`, `×`, `xⁿ`, `a⁻¹`) e o `cadeado.py`
  pedido no roteiro do vídeo 1. A abertura, o encerramento **e a fase 0 do capítulo 8**
  dependem dos dois: sem o `cadeado()` com arco separado do corpo não há como fechar a
  mensagem no `C8N02`, abrir a cópia interceptada no `C8N03`, gravar "fatorar n" no corpo
  dele no `V3N01` nem abrir a rachadura parcial do `V3N02`.
