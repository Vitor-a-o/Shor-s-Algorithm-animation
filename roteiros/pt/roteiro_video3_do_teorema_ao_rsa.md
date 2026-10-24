# Corpo — Vídeo 3: Do teorema ao RSA

Capítulos 6 a 8, na ordem de montagem.

---

## Abertura

| Tag | Fala | Est. | Entra em |
|---|---|---|---|
| V3N00 | O vídeo anterior montou quatro operações dentro de um módulo. Este constrói com elas o RSA — passando antes por dois teoremas. | 8,8 | Os quatro símbolos do `V2N00` voltam em fila, acesos. Em "constrói com elas o RSA", eles se fecham em volta do cadeado do vídeo 1, que entra no centro **intacto**. Em "dois teoremas", duas lacunas vazias se abrem entre a fila e o cadeado — os lugares que os capítulos 6 e 7 vão ocupar |
| — | *(cartão, ~17 s, com a apresentação)* | — | "Do Zero ao Algoritmo de Shor Quântico" nasce no centro e "Vídeo 3 de 4 — Do teorema ao RSA" embaixo dele. O cartão vem depois do gancho falado (`V3N00`), carrega a apresentação do autor e emenda no `CAP06`; mesma emenda do vídeo 2: o subtítulo sai primeiro e o título encolhe por último, já com o `CAP06` entrando por baixo. Durante o cartão roda a apresentação do autor (`V0N00`, em `roteiro_video0_apresentacao.md`). |

**Subtotal: 8,8 s** (1 locução) + cartão com a apresentação ~17,1 s

---

## Capítulo 6 — Pequeno Teorema de Fermat

| Tag | Fala | Est. | Entra em |
|---|---|---|---|
| CAP06 | Com as quatro operações prontas, entra o primeiro teorema da série. | 4,6 | cartão |
| C6N01 | Lembra da tabela multiplicativa que vimos no capítulo cinco? Aqui está ela de novo, agora com módulo sete. | 7,5 | A tabela entra **completa**, em dois tempos dentro de um `play` só (`Succession`): primeiro a moldura — `FadeIn(titulo_tab)`, `head_c` e `head_l` em `LaggedStart` (um número de cada vez) e `Create(lin_h)` + `Create(lin_v)`, ~1,5 s —, depois o `LaggedStart(linhas_cel)`, uma linha por vez, ~2,5 s. Ritmo calmo: a tabela é reapresentada, não despejada |
| C6N02 | Podemos notar que a primeira linha são os possíveis restos não nulos da divisão por sete. | 6,7 | `Create(el1)` e o `TransformFromCopy(linhas_cel[0] → A)` emendados |
| C6N03 | Vamos pegar um desses números, multiplicar por outro e reduzir o produto pelo módulo. | 5,8 | Animação nova — **um número só**. `Indicate(A[4])` e `Indicate(head_l[2])` (vermelho) emendados. Em seguida o produto `prods[4]` = `3·5` nasce na altura de `B`, embaixo do `A[4]`: o `3` vermelho por `TransformFromCopy` de `head_l[2]`, o `·5` por `TransformFromCopy` do `A[4]`. Emendado, `FadeIn(mod_rot)` e `ReplacementTransform(prods[4] → B[4])`: o produto vira o `1` vermelho no mesmo lugar. Os outros cinco produtos ainda não existem |
| C6N04 | O resultado é o número da mesma coluna, na linha do multiplicador. | 5,0 | `Create(circ)` — um círculo verde na célula (3, 5) da tabela, raio ~0,21, como os `circulos` do capítulo 5 — com `Indicate(head_l[2])` e `Indicate(head_c[4])` emendados: a linha do multiplicador e a mesma coluna. Depois, uma cópia de `linhas_cel[2][4]` sai da tabela e cai exatamente em cima de `B[4]`, ficando vermelha e no tamanho de `B` no caminho (o gesto das `copias`), e some num `Indicate(B[4])` |
| C6N05 | Fazendo isso com a linha inteira, obtemos exatamente a linha do multiplicador. | 5,0 | O mesmo processo nas outras cinco colunas, mais rápido, num bloco só: os `prods` restantes nascem como o do `C6N03` (`LaggedStart`) e cada um vira o próprio resto (`ReplacementTransform(prods[j] → B[j])`); `Create(el3)` + `FadeOut(circ)` + `Indicate(head_l[2])`; as `copias` da linha 3 inteira caem em cima de `B` e somem com `Indicate(B)`. Ao fim do bloco, à direita só existem `A`, `B` e `mod_rot` — nenhum produto |
| C6N06 | Os números são os mesmos mas em outra ordem. | 3,8 | `LaggedStart(Create(arcos))` — cada arco liga `A[j]` (embaixo) ao `B` igual a ele (em cima). Entre `A` e `B` não há mais nada: os arcos ligam dois números iguais |
| C6N07 | E isso vale para qualquer multiplicador: ele só reordena a linha. | 4,6 | Animação nova — **a varredura**, num `play` só (`Succession`, ~0,8 s por linha). Para cada linha r em 4, 5, 6 e 2: `el3` desliza até a linha r e `Indicate(head_l[r−1])`; as cópias da linha r caem em cima de `B`, cada `B[j]` se transforma no lugar no novo valor (vermelho, mesmo tamanho) e os `arcos` se transformam nos arcos do novo arranjo; as cópias somem. Fechando a sequência (~0,6 s), `el3`, `B` e `arcos` voltam à linha 3. Os valores de `B` seguem a tabela: 4 → 4 1 5 2 6 3; 5 → 5 3 1 6 4 2; 6 → 6 5 4 3 2 1; 2 → 2 4 6 1 3 5; 3 → 3 6 2 5 1 4 |
| C6N08 | Como a ordem não importa na multiplicação, podemos fazer a seguinte congruência. | 5,0 | `eq0` = `(3·1)(3·2)(3·3)(3·4)(3·5)(3·6) ≡ (1·2·3·4·5·6) (mod 7)` em [0, −2,4, 0]: cada `3` vermelho nasce de cópia de `head_l[2]` e cada número preto de cópia do `A[j]`, os parênteses por `Write`; o lado direito nasce de `TransformFromCopy(A → …)`, o `≡` e o `(mod 7)` por `FadeIn`. Emendado, `FadeIn(nota)` em [0, −1,75, 0]. A `nota` fica em cena até o começo do `C6N09` |
| C6N09 | Colocando o multiplicador em evidência, ficamos com uma potência vezes o mesmo produto de antes. | 6,3 | Animação nova — **a extração dos 3**, num `play` só e fluida (`Succession` de seis passos, ~0,5 s cada, sem pausa entre eles), com `FadeOut(nota)` no primeiro passo. O lado direito não se mexe. Passo 1: o `3` do primeiro parêntese sai para a frente do produto, os parênteses dele se desfazem e um parêntese grande se abre em volta do resto: `3·(1·(3·2)(3·3)(3·4)(3·5)(3·6))`. Passos 2 a 6: o `3` do parêntese seguinte voa e se funde ao `3` da frente — o expoente azul nasce como `2` no passo 2 e sobe para `3`, `4`, `5`, `6` —; os parênteses daquele par somem, o número preto entra na fila de dentro com um `·`, e o que sobra à direita desliza para fechar o buraco. Estado final: `3⁶·(1·2·3·4·5·6) ≡ (1·2·3·4·5·6) (mod 7)` — o `eq` (base vermelha, expoente azul), na mesma posição |
| C6N10 | Como vimos no capítulo anterior, restos que não têm fator comum com o módulo possuem inverso. | 6,7 | `FadeIn(nota2)` |
| C6N11 | Como o módulo é primo, todo fator dessa lista tem inverso: podemos dividir o produto inteiro dos dois lados e simplificar. | 8,8 | `Write(div_e)` + `Write(div_d)` |
| C6N12 | O que sobra é uma potência congruente a um módulo sete. | 4,6 | `resultado` |
| C6N13 | Quando o módulo é primo, essa equivalência é generalizada para um valor a que não seja zero ou múltiplo do módulo. | 8,8 | `Write(geral)`, ainda no rodapé ([0, −3,35, 0]) e no tamanho de hoje |
| C6N14 | Esse é o Pequeno Teorema de Fermat. | 2,9 | **A virada.** Um `play` só: a tabela inteira, `el1`, `el3`, `A`, `B`, `mod_rot` e `arcos` saem em `FadeOut`, e **no mesmo bloco** o `geral` sobe para [0, −0,5, 0] e cresce de 28 para 40 — ele não é reposicionado depois da limpeza, ele **sobrevive** a ela. O `resultado` sai meio segundo atrasado em relação ao resto (`lag_ratio` ou `FadeOut` próprio), para que o caso particular seja a última coisa a desaparecer debaixo do geral. Fechando o bloco, `titulo = T("Pequeno Teorema de Fermat", 40)` nasce em [0, 0,9, 0] por `Write` |
| C6N15 | Repare na condição: o módulo precisa ser primo. É ela que vai quebrar no próximo capítulo. | 6,7 | Título e equação parados em cena. Em "precisa ser primo", `Indicate` no `(n primo)` cinza que o `geral` já carrega |

**Subtotal: 92,8 s** (cartão + 15 locuções)

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
| C7N13 | Esse é o Teorema de Euler. | 2,5 | **A virada, espelhando o `C6N14`.** Um `play` só: `head_c`, `head_l`, `lin_h`, `lin_v`, `linhas_cel`, `el2`, `cruzes`, `sobr`, `phi`, `eq2`, `div2_e` e `div2_d` saem em `FadeOut`, e no mesmo bloco o `geral` sobe para [0, −0,5, 0] e cresce de 28 para 40. O `res` sai meio segundo atrasado, como o `resultado` no capítulo 6. Fechando, `titulo = T("Teorema de Euler", 40)` nasce em [0, 0,9, 0] por `Write` |
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
| C8N15 | Qualquer expoente que deixe resto um nesse módulo devolve a mesma mensagem. É dessa liberdade que o RSA inteiro é feito. | 8,8 | realce (seção **Realces**) — o `L4` fica parado em cena |
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

## Realces — número ou variável nomeado na fala

Mesma regra do vídeo 2: **quando a fala nomeia um número ou uma variável que está na tela,
a peça é realçada na palavra.** As ferramentas são as do vídeo 2: `realce(*peças)` em
`shor/ferramentas.py` (cada peça pulsa na própria cor, em volta do próprio centro) e
`na_palavra(cena, t0, tag, est, âncora, *anims)` em `shor/sincronias.py`, que dispara as
animações na âncora, no mesmo `play` da animação principal da linha, sem empurrar a linha
para fora da locução. A chave da âncora é `(tag, âncora em pt)`.

- **Nascimento conta como realce.** Quando a peça nasce na própria palavra, ela não ganha
  `Indicate` extra; o que muda é o instante do nascimento, que passa a cair na âncora.
- **Gesto que já existe vai para a palavra.** Os `Indicate` que o código já faz sobre a peça
  nomeada não ganham um segundo realce: passam a disparar na âncora.
- **Todas as cópias juntas.** Quando o mesmo valor está em mais de um lugar da tela, todas
  as cópias realçam no mesmo instante.
- O `so_fala` do `C8N15` vira `narra`.
- As frações começam estimadas por caracteres (pt e en) e entram em `roteiros/sincronias.md`
  marcadas "a medir na gravação".

| Tag | Âncora (pt) | Palavra em en | Realça | Observação |
|---|---|---|---|---|
| C6N01 | módulo sete | modulus seven | `titulo_tab` (o sete está escrito nele) | |
| C6N02 | sete | seven | `titulo_tab` | o `Create(el1)` e o `A` seguem no começo |
| C6N06 | Os números | The numbers | `A` + `B` | |
| C6N10 | restos | remainders | `eq[3]` (a lista `1·2·3·4·5·6`) | |
| C6N10 | módulo | modulus | o 7 de `eq[4]` | |
| C6N11 | módulo | modulus | o 7 de `eq[4]` | |
| C6N11 | produto inteiro | whole product | `div_e` + `div_d` nascem na palavra | |
| C6N12 | potência | power | `resultado[0]` (o `3⁶`) | o `ReplacementTransform` segue no começo |
| C6N12 | a um | to one | `resultado[2]` | |
| C6N12 | sete | seven | o 7 de `resultado[3]` | |
| C6N13 | módulo é primo | modulus is prime | `geral[3]` (o n) + o n do expoente | o `Write(geral)` segue no começo; o realce vem logo depois dele |
| C6N13 | valor a | value a | `geral[0][0]` (o a) | |
| C6N13 | múltiplo do módulo | multiple of the modulus | `geral[3]` + o n do expoente | |
| C6N15 | o módulo precisa | the modulus has | `geral[3]` + o n do expoente | |
| C6N15 | precisa ser primo | has to be prime | o `Indicate(geral[4])` que já existe, agora na palavra | |
| C7N02 | multiplicador | multiplier | o `Indicate(head_l[1])` que já existe, agora na palavra, junto do `2⁸` (`esq[0]`) | o `Write(eq)` e o `Create(el2)` seguem no começo |
| C7N02 | lista de restos | list of remainders | `esq[1:]` + `dir_[0:5]` | |
| C7N03 | cancelar a lista | canceling the list | `div_e` + `div_d` nascem na palavra | |
| C7N04 | dois desses fatores | two of these factors | os `3` e `6` roxos: `esq[2]`, `esq[4]`, `dir_[1]`, `dir_[3]`, `div_e[2]`, `div_e[4]`, `div_d[2]`, `div_d[4]` | |
| C7N04 | módulo | modulus | o 9 de `exp2` e o 9 de `dir_` (`dir_[6]`) | |
| C7N05 | linhas | rows | o primeiro `play` (linhas 3 e 6 apagando + os `Indicate` roxos) começa na palavra | o `Wiggle` e o `≢` vêm depois, como hoje |
| C7N06 | números que não têm inverso | numbers that have no inverse | `cruzes` + `cruzes_eq` nascem na palavra | |
| C7N07 | números | numbers | `sobr` nasce na palavra | |
| C7N07 | módulo | modulus | `dir_[6]` (o 9) | |
| C7N08 | contagem | how many | `Write(phi)` na palavra | |
| C7N08 | fi de ene | phi of n | `phi` | |
| C7N11 | potência | power | `res[0]` (o `2⁶`) | o `ReplacementTransform` segue no começo |
| C7N11 | a um | to one | `res[2]` | |
| C7N11 | nove | nine | `res[4]` | |
| C7N12 | qualquer módulo | any modulus | `geral[3]` (o n) + o n do expoente | o `Write(geral)` segue no começo |
| C7N12 | o expoente | the exponent | `geral[0][1]` (o `φ(n)`) | |
| C7N12 | totiente | totient | `geral[0][1]` | |
| C8N12 | número a | number a | o `Indicate(L[0][0])` que já existe, agora na palavra | a caixa `SEGREDO` e os glifos seguem antes |
| C8N12 | Multiplicamos | We multiply | `L → L2` na palavra | |
| C8N13 | se somam | add up | `L2 → L3` na palavra | |
| C8N14 | expoente | exponent | `L3[0][1]` | antes da troca |
| C8N14 | reescrito | rewritten | `L3 → L4` na palavra | |
| C8N14 | fi de ene | phi of n | os dois `Indicate` (`L4[3]` e `L4[0][1]`) que já existem, agora na palavra | |
| C8N15 | Qualquer expoente | Any exponent | `L4[0][1]` | `so_fala` vira `narra` |
| C8N15 | mensagem | message | `L4[2]` (o a) | |
| C8N16 | expoente | exponent | `legenda[1]`, `[2]`, `[3]` (o `(mod φ(n))` da legenda) | |
| C8N17 | dois números | two numbers | os `Indicate(celulas[2][5])` e `Indicate(celulas[5][2])` que já existem, agora na palavra | |
| C8N17 | dê um | is one | `ed[4]` | |
| C8N17 | módulo do expoente | modulus of the exponent | `ed[5]`, `ed[6]`, `ed[7]` | |
| C8N18 | par | pair | o `Indicate(ed)` que já existe, agora na palavra | |
| C8N18 | expoente | exponent | `L4[0] → L5[0]` + a volta do lado direito, na palavra | |
| C8N19 | produto no expoente | product in the exponent | `L5[0][1]` (o `e·d`) | antes da troca |
| C8N19 | potência de outra potência | power of a power | `L5 → L6` + a saída da tabela, na palavra | |
| C8N19 | uma desfazendo | one undoing | o `Indicate` do `e` que já existe, agora na palavra | |
| C8N19 | a outra | the other | o `Indicate` do `d` que já existe, agora na palavra | |
| C8N20 | mensagem | message | o `Indicate(L6[2])` que já existe, agora na palavra, junto do `a` do `pacA` | |
| C8N21 | primeira potência | first power | o `aᵉ` de `L6` (`L6[0][0][1]`) | |
| C8N21 | módulo | modulus | `L6[3]` (o n) | |
| C8N21 | mensagem | message | o `a` do `pacA` | |
| C8N21 | cifra | ciphertext | o `trancar(pacA)` na palavra | |
| C8N23 | segunda potência | second power | o `d` de `L6` (`L6[0][1]`) | |
| C8N23 | primeira | the first | o `aᵉ` de `L6` (`L6[0][0][1]`) | |
| C8N23 | mensagem original | original message | o `abrir(pacA)` na palavra | |
| C8N24 | expoente que desfaz | exponent that undoes | `fpriv[2]` + o `d` de `f2s` | |
| C8N24 | módulo | modulus | `fpriv[4]` + o n de `f2s` | |
| C8N26 | módulo | modulus | `Write(esc)` + `Write(E1)` na palavra | |
| C8N27 | módulo | modulus | `esc[2]` + os `33` de `E1` | |
| C8N27 | fi de ene | phi of n | `Write(phi)` na palavra | |
| C8N27 | módulo do expoente | modulus of the exponent | `E1 → E2` na palavra | |
| C8N28 | par de inversos | inverse pair | `ed2 → edn` na palavra | o `Write(ed2)` segue antes |
| C8N29 | desse par | this pair | `edn[0]` + `edn[2]` | |
| C8N29 | mesmo módulo | same modulus | o `33` dos dois cartões + `esc[2]` | |
| C8N30 | números escolhidos | numbers we chose | o `E2 → E3` + `Indicate(edn)` que já existem, agora na palavra | |
| C8N31 | mensagem | message | o `Write` de "mensagem: a = 5" na palavra | |
| C8N31 | menor que o módulo | smaller than the modulus | o `Write` de "< 33" na palavra, com o `33` de `E4` | |
| C8N32 | lugar da letra | place of the letter | o `E4 → L7` + `Indicate(msg_esc)` que já existem, agora na palavra | |
| C8N34 | cifra | decrypt it | o `26` de `f1` e o `26` de `f2` | |
| C8N35 | números | numbers | `Write(fim2)` na palavra | |
| C8N36 | fi de ene | phi of n | `lphi[1]`, `[2]`, `[3]` (o `φ(n)` da legenda) | se a legenda ainda não nasceu na palavra, o `FadeIn(leg)` cai nela |
| C8N36 | encontrar a privada | find the private one | `eixo_d` | se o eixo ainda não nasceu, o nascimento dele cai na palavra |
| C8N36 | a partir da pública | from the public one | `eixo_e` | idem |
| C8N37 | conhece o módulo | know the modulus | `lphi` inteiro | |
| C8N37 | fi de ene | phi of n | os dois `Indicate` (`phin` e o `φ(n)` da legenda) que já existem, agora na palavra | |
| C8N38 | fi de ene | phi of n | `phin` | |
| C8N38 | abaixo do módulo | below the modulus | `l2` (n = 15) + `ln[1]` | |
| C8N38 | não compartilham fator | share no factor | o `Indicate(vivas)` + `FadeIn(conta)` que já existem, agora na palavra | |
| C8N39 | módulo grande | large modulus | o salto para 35 começa na palavra | |
| C8N40 | fosse primo | were prime | o primeiro `play` (grade 11, `l2c → l2d`) começa na palavra | |
| C8N40 | contagem | the count | o `Indicate(tab11[2])` + `FadeIn(conta11)` que já existem, agora na palavra | |
| C8N40 | chave privada | private key | o `Indicate(c1[1])` que já existe, agora na palavra | |
| C8N41 | dois primos | two primes | `Write(c3[0:5])` na palavra | |
| C8N41 | múltiplos de p | multiples of p | os riscos `r_p` + `Indicate(c3[2])` que já existem, agora na palavra, com o `3` de `l2e` | |
| C8N41 | os de q | those of q | os riscos `r_q` + `Indicate(c3[4])` que já existem, agora na palavra, com o `5` de `l2e` | |
| C8N43 | p e q | p and q | `c3[2]`, `c3[4]`, `c3[11]`, `c3[15]` | |
| C8N43 | produto dos dois | their product | o `Indicate(c3[0])` que já existe, agora na palavra | |
| C8N44 | esse número | this number | o n de `c4` (`c4[3]`) + `c3[0]` | depois do `Write(c4)` |
| V3N01 | número grande | large number | o n da tese (`tese[0][3]`) | junto do fim do `gravar` |

**Ficam sem realce**, porque o que a fala nomeia não é um número nem uma variável em cena:
contagens e nomes ("quatro operações" e "dois teoremas" no `V3N00`, "primeiro teorema" no
`CAP06`), números de capítulo e de vídeo (`C7N05`, `V3N02`), o "módulo nove" do `C7N01` (o
nove não está escrito na tela), a fase figurativa do capítulo 8 (`C8N01`–`C8N11`: canal,
chaves e cadeado, sem número nem variável) e as linhas sem número nomeado (`C6N07`, `C6N08`, `C6N09`, `C6N14`,
`C7N09`, `C7N10`, `C7N13`, `C7N14`, `C8N22`, `C8N25`, `C8N33`, `C8N42`). No `C6N03`–`C6N05`, os realces de `A[4]`, `head_l[2]`, `head_c[4]` e `B` acompanham a animação desde o começo da linha, sem âncora.

---

## Projeção de duração

| Bloco | Locuções | Fala |
|---|---|---|
| Abertura | 1 | 8,8 s |
| Capítulo 6 | 16 | 92,8 s |
| Capítulo 7 | 15 | 86,6 s |
| Capítulo 8 | 45 | 314,8 s |
| Encerramento | 2 | 15,8 s |
| **Total** | **79** | **518,8 s** |

Somando o `PAD` de 0,35 s por locução (27,7 s), os dois cartões silenciosos
(~7 s) e os `limpar()` entre capítulos (~10 s), a projeção é de **cerca de 9 min 23 s** —
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

Quatro trechos têm animação mais longa que a fala e vão correr um pedaço em silêncio:
`C8N04` e `C8N08` (as
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
- [ ] Capítulo 6 — C6N01 a C6N15
- [ ] Capítulo 7 — C7N01 a C7N14
- [ ] Capítulo 8 — C8N01 a C8N44
- [ ] Encerramento — V3N01 e V3N02
- [ ] `python medir.py`
- [ ] Render de conferência com `NARRA = True`

---

## Pendências de código do capítulo 6 (`parte6`)

1. **Tabela em dois tempos (`C6N01`)** — moldura primeiro, linhas depois, num `play` só com
   `Succession`.
2. **Um número só (`C6N03`–`C6N04`)** — animação nova: o `3·5` nascendo embaixo do `A[4]` e
   virando o `B[4]`; o `circ` na célula (3, 5) com os dois cabeçalhos pulsando; a cópia da
   célula caindo sobre o `B[4]`.
3. **A linha inteira (`C6N05`)** — cada produto vira o próprio resto por
   `ReplacementTransform`, de modo que nenhum `prods` fica em cena depois desta linha. O
   `circ` sai quando a `el3` entra.
4. **Arcos (`C6N06`)** — cada arco liga `A[j]` ao `B` de mesmo valor.
5. **Varredura (`C6N07`)** — animação nova: linhas 4, 5, 6 e 2, com `el3`, `B` e `arcos` se
   transformando a cada linha, e a volta à linha 3.
6. **`eq0` (`C6N08`)** — os pares `(3·j)` nascem de `head_l[2]` e de `A`; o lado direito
   `(1·2·3·4·5·6)` nasce de `A`.
7. **Extração dos 3 (`C6N09`)** — animação nova e fluida, de `eq0` até o `eq`, um `3` por vez,
   com o expoente subindo de um em um.
8. **`C6N14`** — a lista do `FadeOut` não inclui `prods` nem `circ`, que já saíram antes.
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
7. **Final novo (`C7N13`)** — mesmo pouso do `C6N14`, em um `play` único:
   - `FadeOut` de `head_c`, `head_l`, `lin_h`, `lin_v`, `linhas_cel`, `el2`, `cruzes`,
     `sobr`, `phi`, `eq2`, `div2_e` e `div2_d`;
   - no mesmo `play`, `geral.animate.move_to([0, -0.5, 0]).scale(40/28)`;
   - `res` com `FadeOut` atrasado (~0,5 s) em relação ao resto;
   - `Write(titulo)` fechando o bloco, com `titulo = T("Teorema de Euler", 40)` em
     [0, 0.9, 0].

   Vale extrair isso e o `C6N14` numa função só em `ferramentas.py` — algo como
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
