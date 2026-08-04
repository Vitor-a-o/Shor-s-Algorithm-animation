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
| C8N01 | O problema que o RSA resolve nasce com duas pessoas que nunca se falaram precisando trocar uma mensagem por um caminho público. | 9,2 | **Animação nova — não existe nada disso hoje no `capitulo8.py`.** Uma `DashedLine` cinza atravessa a tela em y ≈ −0,4, rotulada "canal público" em cinza 20; nas pontas, dois pontos pretos ("quem envia" e "quem recebe"), sem nomes próprios. A caixa da mensagem entra **legível**: `_caixa_msg("SEGREDO", CARTAO_ESCURO, BRANCO, 28)`. Ela desliza de uma ponta à outra e, no meio, um olho vermelho abre acima da linha; uma **cópia** da caixa sobe até uma prateleira ao lado dele e fica lá, legível, sem nenhuma alteração |
| C8N02 | Aplicar uma criptografia de chave simétrica resolve metade do problema: a mensagem que trafega deixa de fazer sentido para terceiros. | 8,3 | **Animação nova.** A viagem recomeça da esquerda. Antes de partir, uma chave amarela desce sobre a caixa e o `cadeado()` fecha com o flash seco do `V1N01`; **no mesmo `play`** as sete letras se embaralham no lugar (`Transform` letra a letra com `lag_ratio` pequeno, `SEGREDO → Xk9#R2q`) e o fundo vira o verde da cifra. A cópia que sobe à prateleira do olho agora é a embaralhada, e um ✗ vermelho nasce sobre ele. Vale isolar isso num `_trancar(caixa)`/`_abrir(caixa)`: o par é usado quatro vezes na fase 0 |
| C8N03 | Só que quem tranca e quem abre a mensagem usam a mesma chave, e ela também tem que atravessar o canal. | 8,8 | **Animação nova.** A mesma chave amarela sai da ponta esquerda e entra no canal, atrás da cifra — o segundo objeto a fazer o percurso, com o mesmo movimento e a mesma velocidade da caixa. A prateleira do olho já tem a cifra esperando |
| C8N04 | Um intruso ouvindo o canal pega as duas coisas juntas, e abre a mensagem com a própria chave que a trancou. | 8,8 | **Animação nova — é o beat que justifica o capítulo.** No meio do canal, uma cópia da chave sobe e pousa **ao lado** da cifra na prateleira: os dois objetos capturados, juntos, em cena. O olho aplica a chave, o cadeado abre, as letras desembaralham (`_abrir`) e a caixa da prateleira volta a ser a escura com `SEGREDO` legível. O ✗ vermelho sai e a tela pisca vermelho uma vez |
| C8N05 | O RSA é uma das saídas para isso ele usa duas chaves diferentes, uma que tranca e outra que abre. | 8,3 | **Animação nova.** Sobra a chave amarela, agora sozinha e **na ponta direita** — quem recebe é quem manda no par. Ela se **parte em duas** e as metades pousam como dois cartões **vazios**: `tranca` em cinza e `abre` em amarelo, o mesmo `RoundedRectangle` com `stroke_color` CINZA/AMARELO dos cartões `pubS` e `privS`. São as molduras que o `C8N22` e o `C8N24` preenchem com `(e, n)` e `(d, n)` |
| C8N06 | Quem vai receber a mensagem envia pelo canal sua chave que tranca. Ela pode ser vista por todo mundo, porque com ela só é possível trancar, por isso ela é chamada de chave pública. | 14,0 | **Animação nova.** O cartão cinza percorre o canal **da direita para a esquerda**: é o único objeto do capítulo que anda ao contrário, e é o gesto inteiro da assimetria. O olho copia e guarda na prateleira, à vista, sem nenhuma consequência — nada pisca vermelho |
| C8N07 | Quem envia tranca a mensagem com ela — e nem ele mesmo consegue voltar atrás. A chave que fecha não abre. | 8,3 | **Animação nova.** Na ponta esquerda, o cartão cinza fecha o cadeado sobre `SEGREDO` e as letras se embaralham (`_trancar`, o mesmo movimento do `C8N02`). Em seguida o próprio remetente tenta reabrir com o cinza: `Wiggle` e ✗. Quem trancou também ficou de fora |
| C8N08 | O intruso pega tudo o que atravessou o canal, a chave pública e a mensagem trancada, e nada disso é suficiente para abrir. | 9,5 | **Animação nova — a rima com o `C8N04`, mesmo enquadramento e desfecho oposto.** A cifra atravessa e o olho captura a cópia: a prateleira fica com os **mesmos dois objetos** de antes, cifra e chave. Ele aplica o cinza, o cadeado chacoalha e não abre, as letras continuam embaralhadas, ✗ vermelho |
| C8N09 | A chave que abre nunca entra no canal, por isso ela também é chamada de chave privada. | 7,0 | **Animação nova.** O cartão amarelo, parado na ponta direita desde o `C8N05`, acende sozinho — sublinhar que ele nunca se moveu vale mais que qualquer rótulo. Ele abre o cadeado, as letras desembaralham e `SEGREDO` reaparece legível, do lado certo. Flash verde |
| C8N10 | Na aritmética, isso é um par de operações: uma que qualquer um faz, e outra que ninguém desfaz sem uma informação que a primeira não entrega. | 10,8 | **Animação nova.** Tudo esmaece menos o canal, e sobre ele nascem duas setas: a de ida, verde e sólida; a de volta, vermelha, que se despedaça no meio do caminho — o mesmo gesto do `V1N01`. É a promessa que o `C8N36` vai cobrar. Os dois cartões continuam nas pontas, apagados (opacidade ~0,3) |
| C8N11 | Vamos começar com o Teorema de Euler e mostrar como essas operações surgem dele. Para isso, fazemos algumas manipulações na congruência. | 8,8 | `Write(L)` nascendo **de dentro** da seta de ida, em [0, 1,6, 0], com o canal, o olho e os dois cartões apagados saindo em `FadeOut` no mesmo `play`. A fase 0 fecha e a fórmula assume a tela — um movimento só, sem corte no meio |
| C8N12 | Esse número a é a mensagem — todo texto vira número antes de entrar aqui. Multiplicamos os dois lados por ele. | 8,3 | `L → L2`, precedido de um `Indicate` curto no `a` do lado direito. É a primeira e única vez que a dedução para para dizer o que a letra é, e agora também é onde a ponte texto→número é feita — a caixa `SEGREDO` da fase 0 nunca virou número em cena |
| C8N13 | Do lado esquerdo, os expoentes se somam. | 2,9 | `L2 → L3` |
| C8N14 | E aqui está a peça central, o expoente pode ser reescrito como módulo fi de ene. | 6,7 | `L3 → L4`. Os dois `mod` ficam na tela ao mesmo tempo, e é esse o conteúdo do beat: `Indicate` no `(mod n)` do rodapé e, no mesmo `play`, no `(mod φ(n))` que acabou de nascer no expoente. A hierarquia tem que ser vista, não dita |
| C8N15 | Qualquer expoente que deixe resto um nesse módulo devolve a mesma mensagem. É dessa liberdade que o RSA inteiro é feito. | 8,8 | `so_fala` — linha sem animação, o `L4` fica parado em cena |
| C8N16 | Voltamos à tabela de multiplicação, mas agora ela vale para o expoente. | 5,0 | `FadeIn(tabela)` |
| C8N17 | Cada círculo verde é um par de inversos. É isso que procuramos: dois números cujo produto dê um, no módulo do expoente. | 9,2 | `LaggedStart(uns)` + `Write(ed)` emendados com `FadeIn(nota)` + os dois `Indicate` |
| C8N18 | Esse par pode então substituir o expoente. | 2,9 | `L4 → L5` + `Indicate(ed)` |
| C8N19 | E um produto no expoente é o mesmo que uma potência de outra potência: duas operações encadeadas, uma desfazendo a outra. | 8,8 | `L5 → L6` emendado com o `FadeOut(tabela, uns, nota, ed)`. É aqui que o par de setas do `C8N10` vira álgebra — vale um `Indicate` curto nos dois expoentes, um de cada vez |
| C8N20 | Cada peça da fórmula ganha um papel, começando pela mensagem. | 4,2 | `Indicate(L6[2])` emendado com `msgA` + `rotA` + `fA` |
| C8N21 | A primeira potência junto com o módulo embaralham a mensagem, e o resultado é a cifra. | 6,6 | `GrowArrow(s1)` + `Write(f1s)` emendados com `cifA` + `rotC` |
| C8N22 | Estes são a chave pública que circulou. | 2,9 | `pubS`, com o `e` e o `n` sendo puxados de `f1s`. **Ajuste da fase 0**: o `rpub` não é criado do zero — é o cartão cinza vazio do `C8N05` voltando à cena e se preenchendo |
| C8N23 | A segunda potência desfaz a primeira e devolve a mensagem original. | 4,6 | `GrowArrow(s2)` + `Write(f2s)` emendados com `msgB` + `rotB` |
| C8N24 | E o expoente que desfaz junto com o módulo é a chave privada — essa não sai da mão de quem recebe. | 9,1 | `privS`, com o `d` e o `n` sendo puxados de `f2s`. Mesmo ajuste: o `rpriv` é o cartão amarelo vazio do `C8N05` |
| C8N25 | O esquema está montado. Falta ver ele rodar com números. | 4,2 | `FadeOut` do esquema inteiro + `L6` |
| C8N26 | Quem vai receber escolhe o módulo de uma maneira específica, que vai ser mostrada mais para frente. | 7,1 | `Write(esc)` + `Write(E1)` emendados. O `33` continua aparecendo sem origem, mas agora a linha marca isso como dívida — e o `C8N42` paga |
| C8N27 | Com o módulo na mão, ele calcula fi de ene — o módulo do expoente. | 5,8 | `Write(phi)` + `E1 → E2` emendados |
| C8N28 | E procura ali um par de inversos. | 2,9 | `Write(ed2)` + `ed2 → edn` emendados |
| C8N29 | As duas chaves nascem desse par: uma leva cada expoente, e as duas levam o mesmo módulo. | 7,1 | `pub` e `priv`, com os expoentes puxados de `edn` e o módulo de `esc` |
| C8N30 | A fórmula geral se preenche com os números escolhidos. | 3,8 | `E2 → E3` + `E3 → E4` emendados |
| C8N31 | Falta a mensagem, que deve ser um número menor que o módulo. | 5,0 | `FadeOut(phi, edn)` + `Write(msg_esc)` emendados. A condição `a < n` não é decorativa: com a mensagem maior que o módulo, a volta devolve o resto e o exemplo da tela para de fechar |
| C8N32 | E ela entra no lugar da letra. | 2,9 | `E4 → L7` + `Indicate(msg_esc)` |
| C8N33 | Quem envia a mensagem usa a chave pública para trancá-la. | 4,6 | `msg1`, `GrowArrow(s1)` + `pub_mini`, `Write(f1)` + `cifra` — os três `play` num bloco só |
| C8N34 | Somente quem tem a chave privada desfaz a cifra. Mais ninguém. | 4,6 | `GrowArrow(s2)` + `priv_mini` e `Write(f2)` + `msg2` num bloco só |
| C8N35 | A verificação é a dedução do começo do capítulo, com números no lugar das letras. | 6,3 | `Write(fim2)` + `fim2 → fim3` emendados |
| C8N36 | Falta a pergunta que decide tudo: se a chave pública e a privada são inversas módulo fi de ene, não seria fácil encontrar a privada a partir da pública? | 12,1 | `FadeOut` do exemplo inteiro, sozinho. A seta vermelha despedaçada do `C8N10` pisca uma vez no centro e sai — a tela fica limpa para o argumento final |
| C8N37 | Inverter é fácil para quem conhece o módulo. E o módulo, aqui, é fi de ene. | 6,7 | `Write(c1)`. A fala não repete a equação que está sendo escrita — o `c1` diz "achar chave privada = achar φ(n)" sozinho. Vale um `Indicate` no `φ(n)` no fim da escrita: ele é o sujeito das próximas seis linhas |
| C8N38 | E fi de ene é uma contagem: quantos números abaixo do módulo não compartilham fator com ele. | 7,1 | **Animação nova, primeira metade.** A lista do capítulo 7 volta abaixo do `c1`: os restos em linha, os que compartilham fator sendo riscados um a um |
| C8N39 | Para um módulo grande, contar um por um é impossível. | 4,2 | **Animação nova, segunda metade.** A contagem do que sobrou colapsa dentro do `φ(n)` do `c1`. Sem esse retorno, o espectador não tem por que achar que fi de ene é difícil |
| C8N40 | Se o módulo fosse primo, a contagem sairia de graça — nenhum número abaixo de um primo compartilha fator com ele — e qualquer um teria a chave privada. | 11,2 | `Write(c2)`, com o `n − 1` chegando por último e um `Indicate` nele. O ✗ vermelho já existe no código |
| C8N41 | Com o produto de dois primos, os únicos que compartilham fator são os múltiplos de p e os de q. | 8,3 | `Write(c3)`, só o lado esquerdo: `n = p × q`. O `p` rosa e o `q` verde-claro são os mesmos dois primos do `V1N02` |
| C8N42 | Dá para descontar todos de uma vez com uma fórmula, sem ter que contar um por um. | 7,0 | O lado direito do `c3` nascendo: o `(p − 1)` e o `(q − 1)` saem do `p` e do `q` do lado esquerdo, um de cada vez. **Mudança de código**: entra também a segunda linha instanciada, `33 = 3 × 11 ⇒ φ(33) = 2 × 10 = 20`, que paga a dívida aberta no `C8N26` — o `20` é o mesmo valor solto que o `C8N27` mostrou sem justificar |
| C8N43 | Mas o atalho só serve para quem conhece p e q. Quem só possui o produto dos dois teria que fatorar para descobrir. | 9,6 | **Animação nova, pequena.** Uma seta vermelha tenta o caminho de volta no `c3`, do `n` para o `p × q`, e se despedaça no meio — a mesma seta do `C8N10` e do `V1N01`, agora sobre números |
| C8N44 | E a série se fecha em cima de si mesma: quebrar o RSA é fatorar esse número. | 7,1 | `Write(c4)` + `Create(caixa)` |

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

1. **A fase 0 inteira é código novo.** Hoje o `parte8` começa direto no `Write(L)`. Entram:
   o canal (`DashedLine` rotulada + duas pontas), o olho vermelho do interceptador com a
   prateleira onde as capturas se acumulam, o `cadeado()` do `cadeado.py`, a caixa de texto
   legível, a chave amarela que percorre o canal e depois se parte em duas, e os dois
   cartões vazios `tranca`/`abre`. São onze locuções, ~68 s de fala. Vale isolar num
   `_fase0(cena)` no topo do arquivo: é a única parte figurativa do capítulo e não divide
   objeto nenhum com a álgebra que vem depois — só os cartões.
   1.1. **Duas funções carregam a fase quase inteira**: `_trancar(caixa)` (cadeado fecha,
   letras embaralham em `lag_ratio` curto, fundo vira verde) e `_abrir(caixa)`, o inverso
   exato. São chamadas quatro vezes — `C8N02`, `C8N04`, `C8N07` e `C8N09` — e é a
   repetição literal do mesmo movimento que faz a segunda volta ler como resposta à
   primeira. Se as duas voltas forem animadas com gestos diferentes, a rima morre.
   1.2. **O trajeto também é uma função**: `_atravessar(mobj, sentido, captura=True)`, com
   a cópia subindo para a prateleira no ponto médio. Chamado cinco vezes, e uma delas
   (`C8N06`) com `sentido=LEFT` — é o único percurso invertido do capítulo, e o único que
   não acende o ✗.
2. **Os cartões da fase 0 sobrevivem até a fase A2.** O `rpub` do `C8N22` e o `rpriv` do
   `C8N24` deixam de ser criados no lugar e passam a ser os mesmos mobjects nascidos no
   `C8N05`, voltando à cena e se preenchendo com `(e, n)` e `(d, n)`. Se forem recriados,
   a fase 0 vira enfeite e a promessa não fecha. Mesma lógica do `geral` que sobrevive à
   limpeza nos capítulos 6 e 7.
3. **A seta de volta despedaçada do `C8N10` também precisa sobreviver** — ela volta por
   meio segundo atrás do `c1`, no `C8N36`. Guardar o mobject, não redesenhar.
   3.1. O texto legível é o mesmo nos dois atos (`SEGREDO`) e o embaralhado também
   (`Xk9#R2q`): sete glifos dos dois lados, para o `Transform` casar um a um sem sobra.
4. `so_fala(cena, "C8N15", 9.2)` novo, logo depois do `L4` — linha sem animação embaixo.
5. `LaggedStart(uns)` + `Write(ed)` emendados com `FadeIn(nota)` + os `Indicate` (`C8N17`).
6. `L5 → L6` emendado com o `FadeOut` da tabela (`C8N19`).
7. `Indicate(L6[2])` emendado com a entrada de `msgA` (`C8N20`); `s1`+`f1s` com `cifA`
   (`C8N21`); `s2`+`f2s` com `msgB` (`C8N23`).
8. Emendas da fase B, todas de dois `play` em um: `esc`+`E1` (`C8N26`), `phi`+`E2`
   (`C8N27`), `ed2`+`edn` (`C8N28`), `E3`+`E4` (`C8N30`), `FadeOut(phi,edn)`+`msg_esc`
   (`C8N31`), `fim2`+`fim3` (`C8N35`), `FadeOut`+`c1` (`C8N36`).
9. `msg1` + `s1`/`pub_mini` + `f1`/`cifra` num bloco só (`C8N33`), e `s2`/`priv_mini` +
   `f2`/`msg2` num bloco só (`C8N34`).
10. **O fecho ganhou duas animações novas** (`C8N38`/`C8N39` e `C8N43`): o retorno da
   contagem do capítulo 7 sob o `c1`, em duas metades — a lista sendo riscada e a contagem
   colapsando dentro do `φ(n)` —, e a seta que tenta voltar de `n` para `p × q` no `c3`. As
   quatro fórmulas `c1`–`c4` continuam as mesmas; o que mudou é que agora são nove falas
   sobre elas, e não quatro, e o `c3` passa a ser escrito em dois tempos (`C8N41` o lado
   esquerdo, `C8N42` o direito).
   10.1. **O `c3` ganha uma segunda linha, instanciada** (`C8N42`): abaixo do
   `n = p × q ⇒ φ(n) = (p − 1) × (q − 1)` entra `33 = 3 × 11 ⇒ φ(33) = 2 × 10 = 20`, nas
   mesmas cores (`p` rosa, `q` verde-claro, `33` laranja). É o que fecha a dívida que o
   `C8N26` abre: o `33` aparece sem origem na fase B, e o `20` do `C8N27` aparece como
   valor solto. Aqui os dois se explicam de uma vez, com números que o espectador já viu.
11. Os sete `cena.wait(1.0)` da fase A saem — quem dá o respiro é o `PAD`.

## Pendências de código da costura (vídeo 3)

- Reaproveitar os quatro símbolos do `V2N00` (`+`, `×`, `xⁿ`, `a⁻¹`) e o `cadeado.py`
  pedido no roteiro do vídeo 1. A abertura, o encerramento **e a fase 0 do capítulo 8**
  dependem dos dois: sem o `cadeado()` com arco separado do corpo não há como fechar a
  mensagem no `C8N02`, abrir a cópia interceptada no `C8N03`, gravar "fatorar n" no corpo
  dele no `V3N01` nem abrir a rachadura parcial do `V3N02`.
