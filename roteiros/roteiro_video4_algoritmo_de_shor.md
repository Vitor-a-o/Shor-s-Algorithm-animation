# Corpo — Vídeo 4: O algoritmo de Shor

Capítulos 9 a 11, na ordem de montagem. É o último vídeo da série: o cadeado que rachou
no fim do vídeo 3 quebra aqui.

Atenção à numeração dos arquivos: o **capítulo 10** em tela é o `capitulo9b.py` e o
**capítulo 11** é o `capitulo10.py`. As tags acompanham o número **de tela** —
`C9N`, `C10N`, `C11N`.

---

## Abertura

| Tag | Fala | Est. | Entra em |
|---|---|---|---|
| V4N00 | A série inteira levou a uma frase: quebrar o RSA é fatorar um número grande. Este vídeo mostra o algoritmo que faz isso — e ele começa longe daí. | 13,1 | O cadeado do fim do vídeo 3 volta ao centro **no estado em que ficou**: `cadeado("fechado")`, "fatorar n" gravado no corpo e a rachadura já parada no meio do arco. `gravar()` e `rachar()` rodam antes da locução, em silêncio, para que o primeiro quadro do vídeo 4 seja o último quadro do vídeo 3. Em "quebrar o RSA é fatorar", `Indicate` no rótulo gravado. Em "o algoritmo que faz isso", a rachadura tenta avançar dois segmentos e **para de novo** — ela só termina no encerramento. Em "começa longe daí", o cadeado encolhe e sai por cima do ombro do quadro, já com o cartão de marca entrando por baixo |
| — | *(cartão silencioso, ~4 s)* | — | "Do Zero ao Algoritmo de Shor Quântico" nasce no centro e "Vídeo 4 de 4 — O algoritmo de Shor" embaixo dele. Mesma emenda dos vídeos 2 e 3: o subtítulo sai primeiro e o título encolhe por último, já com o `CAP09` entrando por baixo |

**Subtotal: 13,1 s** (1 locução) + cartão ~4 s

---

## Capítulo 9 — Ordem Modular

O capítulo é uma pergunta só, feita na tabela que o capítulo 5 já ensinou a ler: subir no
expoente é pular de linha, e a caminhada volta ao ponto de partida. A fala nunca lê o
zigue-zague — ela diz o movimento, e a tela faz os números.

| Tag | Fala | Est. | Entra em |
|---|---|---|---|
| CAP09 | O caminho até a fatoração começa por uma pergunta sobre expoentes. | 5,0 | cartão |
| C9N01 | A exponenciação modular volta, com a mesma equação do capítulo quatro. Só que a pergunta agora é outra. | 8,3 | `Write(eq)` |
| C9N02 | A base e o módulo ficam parados; quem anda é o expoente. E a base tem inverso, como o capítulo cinco pedia. | 9,6 | `FadeIn(escolha)`. Em "tem inverso", `Indicate` na palavra `inversível` cinza que a `escolha` já carrega |
| C9N03 | A tabela de multiplicação do módulo volta, e é nela que a caminhada vai acontecer. | 6,7 | `head_c` + `head_l` + `lin_h` + `lin_v` e o `LaggedStart(linhas_cel)` correm emendados, num bloco só |
| C9N04 | Só uma linha dela interessa: a da base. | 3,8 | `GrowArrow(seta4)` + `Indicate(head_l[4])` |
| C9N05 | A caminhada parte do expoente zero, que vale um. | 4,2 | `Create(c00)` + `Write(f0)` |
| C9N06 | E subir um degrau no expoente é multiplicar pela base — ou seja, pular para a linha dela. | 8,3 | `FadeIn(nota)` |
| C9N07 | Cada passo desce até a linha da base, e o resultado vira a coluna do passo seguinte. | 7,5 | As **duas primeiras voltas do laço** inteiras — seis `play`: `desce`/`alvo`, `Write(fs[0])`, `sobe`/`topo`, `desce`/`alvo`, `Write(fs[1])`, `sobe`/`topo`. O `with narra` envolve o `for`, não cada iteração dele: mesma correção do `C2N07` e do `C5N11` |
| C9N08 | Até que a caminhada devolve o um de onde saiu. | 4,6 | O terceiro passo do laço: `desce`/`alvo`, `Write(fs[2])` com o ✓, e o `Flash(ponto(4, 7))` — os três `play` sob esta linha |
| C9N09 | O caminho é um ciclo fechado. Daqui em diante, ele só se repete. | 5,8 | `Create(fecha)` + `Indicate(c00)` |
| C9N10 | Escrito como congruência, é isto: existe um expoente que devolve um. | 5,0 | `Write(VGroup(mult[0], mult[1], mult[2]))` |
| C9N11 | E cada volta completa no ciclo devolve outro, e outro, para sempre. | 5,4 | Os quatro `play` das duas voltas extras num bloco só: `volta_no_ciclo()`, o `4⁶` nascendo por `TransformFromCopy`, `volta_no_ciclo()` de novo e o `4⁹` com o `(mod 9)`. É a irmã do "e assim por diante" do `C2N07` |
| C9N12 | O menor deles é o que interessa. | 3,3 | `Write(rdef[0])` + `Write(rdef[1])` + `TransformFromCopy(mult[2][1], rdef[2])` — o `3` amarelo nasce do expoente que fechou o ciclo, não de um `Write` do vazio |
| C9N13 | Ele é a ordem modular da base. | 3,3 | **A virada, igual à do `C6N12` e à do `C7N13`.** Um `play` só: a tabela (`head_c`, `head_l`, `lin_h`, `lin_v`, `linhas_cel`, `seta4`, `zig`) e a coluna direita inteira (`eq`, `escolha`, `f0`, `nota`, `fs`, `mult`) saem em `FadeOut`, e no mesmo bloco `caixa_d` e `borda` nascem já centrados. O `rdef` sai meio segundo atrasado em relação ao resto, e o `r` amarelo dele chega ao `r` do `d2`/`d3` por `TransformFromCopy` — o caso particular é a última coisa a desaparecer debaixo do geral. O `d1` já diz "ordem modular de a módulo n", então **não** entra título separado aqui |
| C9N14 | E ela pode ser enorme: no pior caso, do tamanho da contagem de Euler. Procurar testando um expoente por vez custa tanto quanto atacar o RSA de frente. | 12,6 | `Write(d4)` sozinho, num `play` próprio. Em "a contagem de Euler", `Indicate` no `φ(` `n` `)` cinza do próprio `d4` — é a peça que o capítulo 7 definiu e o 8 gastou |
| C9N15 | Guarde a pergunta: qual é o menor expoente que devolve um. O próximo capítulo mostra que ela é a fatoração disfarçada. | 9,6 | `so_fala` — a caixa parada em cena. Em "o menor expoente", `Indicate` no `r` amarelo do `d3` |

**Subtotal: 103,0 s** (cartão + 15 locuções)

---

## Capítulo 10 — Da Ordem Modular à fatoração

O capítulo tem três fases e uma coda. A **fatoração que dá certo** (`C10N01`–`C10N24`) roda
o método inteiro num alvo pequeno: acha a ordem, parte a potência em diferença de
quadrados, e o mdc pesca os dois primos. O **caso inútil** (`C10N25`–`C10N32`) roda o mesmo
método com outra base e falha — é a fase que impede o algoritmo de virar mágica, e a fala
dela é seca de propósito, porque a tela repete um trajeto que o espectador acabou de ver.
A **coda** (`C10N33`–`C10N36`) cobra a dívida do capítulo 8: com os primos na mão, a chave
privada sai por um inverso.

As duas árvores de fatores são o coração visual do capítulo e correm quase mudas: elas
mostram o mesmo número aberto de dois jeitos, e dizer isso em palavras é tudo o que a fala
precisa fazer.

| Tag | Fala | Est. | Entra em |
|---|---|---|---|
| CAP10 | Com a ordem modular na mão, ela vira uma ferramenta de fatoração. | 5,4 | cartão |
| C10N01 | Voltamos ao número do RSA: um produto de dois primos que ninguém entrega. | 5,8 | `Write(obj)` — o `p × q ?` com os primos ainda como letras |
| C10N02 | E escolhemos uma base qualquer — qualquer mesmo, porque os primos a gente não tem. | 6,7 | `Write(base)` |
| C10N03 | Dela procuramos a ordem, do mesmo jeito do capítulo anterior: multiplicando pela base até o um voltar. | 7,5 | Sete `play` num bloco só: `Write(rotulo)`, `FadeIn(caixas[0])`, as três iterações do `for` (`seta` + `rot` + `caixas[i+1]`), `Create(volta)` + `rv` e o `Flash`. O `with narra` envolve o laço inteiro |
| C10N04 | Quatro passos, e ela está achada. | 2,9 | `Write(rper)` com os `Indicate` nos quatro rótulos `×8` |
| C10N05 | Escrita como congruência, ela é o começo de tudo o que vem. | 5,4 | `Write(e1)` + `Indicate(rper)` |
| C10N06 | Basta passar o um para o outro lado. | 3,8 | A saída da cadeia (`caixas`, `setas_o`, `volta`, `rv`, `base`, `rotulo`) com o `rper` subindo para o canto corre no **começo** desta linha; em seguida, `ReplacementTransform(e1, e2)` |
| C10N07 | E o que a ordem entrega é um múltiplo do número que queremos fatorar. | 6,3 | `FadeIn(nota)` |
| C10N08 | Todo múltiplo é esse número vezes alguma coisa. | 3,8 | `ReplacementTransform(e2, e3)` + `FadeOut(nota)` |
| C10N09 | Isso já é uma fatoração: de um lado o que procuramos, do outro o que sobrou. | 7,1 | Os dois `play` da primeira árvore sob esta linha: o tronco `rb` nascendo por `ReplacementTransform` de uma cópia da própria conta, e `Create(linB)` com o `35` e o `x` descendo dos termos de `e3` |
| C10N10 | O que sobrou sai de uma divisão, e o valor dele não importa. | 5,4 | `Write(ex)` e, em seguida, `ReplacementTransform(e3, e4)` com `FadeOut(ex)` e `fBx → fB117` — dois `play` sob esta linha |
| C10N11 | Agora a condição que o método precisa: a ordem tem que ser par. | 5,8 | `Write(d0)` |
| C10N12 | Sendo par, a potência menos um é uma diferença de quadrados — e diferença de quadrados sempre se abre em dois fatores. | 9,6 | `ReplacementTransform(d0, d1)` |
| C10N13 | Dois fatores que saem direto da base, sem passar pelo número grande. | 5,4 | `ReplacementTransform(d1, d2)` |
| C10N14 | É a segunda fatoração do mesmo número. | 3,3 | Os dois `play` da segunda árvore num bloco só: o tronco `ra` e `Create(linA)` com `fA65`/`fA63` nascendo dos termos de `d2` |
| C10N15 | O mesmo número, aberto de dois jeitos diferentes. | 3,8 | `ReplacementTransform(d2, junta)` + `Indicate(e4, color=CINZA)` — a linha de cima acende para dizer de onde a igualdade veio |
| C10N16 | Do lado que a gente já conhecia, os dois primos estão lá dentro. | 5,8 | `Create(linB2)` + `FadeIn(nB)` + `junta → j2` |
| C10N17 | E como a ordem dos fatores não altera o produto, eles têm que reaparecer do outro lado também. | 8,3 | `FadeIn(comut)` e, em seguida, `Create(linA2)` + `FadeIn(nA)` + `j2 → j3` — dois `play` sob esta linha |
| C10N18 | Um deles mora nos dois. | 2,5 | `Indicate(nA[0])` + `Indicate(nB[0])` |
| C10N19 | O outro também. | 1,7 | `Indicate(nA[3])` + `Indicate(nB[1])` |
| C10N20 | Ou seja: os dois números que acabamos de calcular compartilham fator com o número que queremos fatorar. | 7,5 | `ReplacementTransform(comut, expl)` |
| C10N21 | E achar fator comum é rápido: é o algoritmo de Euclides, o mesmo que apareceu de passagem no capítulo cinco. | 9,2 | `Write(m1)` com os `Indicate` no par verde-claro |
| C10N22 | Um de cada lado. | 2,1 | `Write(m2)` com os `Indicate` no par rosa |
| C10N23 | E os primos caem. | 2,1 | `ReplacementTransform(VGroup(m1, m2), fim)` + `Create(cxa)` |
| C10N24 | O número que abriu o capítulo está fatorado. | 3,8 | `ReplacementTransform(obj, obj2)` — o `p × q ?` do topo vira os dois primos com ✓ |
| C10N25 | Só que nem toda base serve. | 2,9 | O `FadeOut` das duas árvores e das contas emendado com `FadeIn(cap5)`, num `play` só. O `fim` dentro da moldura verde **fica em cena** o resto do capítulo: o sucesso segue à vista enquanto a falha roda |
| C10N26 | Outra escolha, outra ordem — e essa também é par. | 4,2 | `Write(u0)` |
| C10N27 | O caminho roda inteiro, sem nenhum erro. | 3,3 | `Write(u1a)` e `ReplacementTransform(u1a, u1)` — dois `play` sob esta linha |
| C10N28 | Só que desta vez os dois primos caem juntos, do mesmo lado. | 5,4 | Os três `play` da árvore do azar num bloco só: tronco `ru`, `Create(linU)` com `fu1`/`fu2`, e `Create(linU2)` + `FadeIn(nU)` |
| C10N29 | E esse lado é múltiplo do número inteiro. | 3,8 | `FadeIn(multi)` + `GrowArrow(setam)` + os `Indicate` em `nU[0]`/`nU[1]` |
| C10N30 | Então um mdc devolve o próprio número... | 3,3 | `Write(m3)` |
| C10N31 | ...e o outro não tem nada em comum com ele. | 4,2 | `Write(m4)` |
| C10N32 | São os dois fatores que a gente já tinha. Quando dá nisso, troca-se a base e roda de novo — e cada tentativa nova tem pelo menos meia chance de acertar. | 13,4 | `Write(triv)` + `FadeIn(sol)`. Animação curta sob fala longa: o quadro fica parado no ✗ vermelho durante a segunda metade da linha, e é essa parada que faz a falha pesar |
| C10N33 | Com os dois primos na mão, a contagem de Euler sai da fórmula do capítulo oito. | 7,1 | O `FadeOut` do caso inútil emendado com `ReplacementTransform(fim.copy(), r1)` — a contagem **nasce de dentro** dos dois primos que ficaram na moldura verde, num `play` só |
| C10N34 | E com ela, a chave privada é só um inverso — a mesma conta que quem montou o RSA fez. | 8,8 | `Write(r2)`. Em "só um inverso", `Indicate` no `(mod φ(n))` — é a tabela de inversos do `C8N17` sendo cobrada |
| C10N35 | Fatorar o módulo e descobrir a chave privada são a mesma coisa. | 5,4 | `Write(r3)` + `Create(cxa2)` |
| C10N36 | Falta uma peça só: achar a ordem sem testar um expoente por vez. É o que o computador quântico faz. | 9,2 | `so_fala` — a moldura parada em cena. Em "achar a ordem", `Indicate` no `r` amarelo que sobreviveu do `C9N15`, se ele ainda estiver na tela; senão, no `n` laranja do `r3` |

**Subtotal: 202,0 s** (cartão + 36 locuções)

---

## Capítulo 11 — Shor Quântico: a QFT encontra o período

O capítulo mais longo do vídeo e o único quântico da série. São seis blocos:
**fundamentos** (`C11N01`–`C11N05`) mostra superposição e emaranhamento sem uma única
fórmula — é a fase figurativa deste capítulo, e a fala deixa claro que é só isso de física.
O **circuito** (`C11N06`–`C11N14`) monta a conta do capítulo 4 em cima de todos os
expoentes de uma vez e mede o registrador de baixo. O **pente** (`C11N15`–`C11N19`) é a
virada conceitual: o que sobrou tem a ordem escrita no espaçamento, e medir direto não
serve. As **ondas** (`C11N20`–`C11N25`) e a **roleta** (`C11N26`–`C11N33`) explicam a
interferência duas vezes, primeiro pelo resultado e depois pelo mecanismo — a segunda
passagem é o trecho em que a animação é longa e a fala é curta, propositalmente. A
**cascata** (`C11N34`–`C11N44`) devolve tudo para o capítulo 10 e fecha a série.

| Tag | Fala | Est. | Entra em |
|---|---|---|---|
| CAP11 | Falta achar a ordem depressa. É a única coisa que o quântico faz aqui. | 5,8 | cartão |
| C11N01 | Um bit clássico é zero ou um. Um qubit pode estar nos dois, com um peso para cada. | 8,3 | `FadeIn(t1)` + `FadeIn(q1, scale=0.8)` — o cartão em gradiente é a imagem inteira da ideia |
| C11N02 | E dois qubits podem ficar amarrados um ao outro. | 4,2 | `FadeIn(t2)` + `FadeIn(qa)` e, emendado, `Create(fio)` + `FadeIn(no)` + `FadeIn(qb)` — os dois `play` num bloco só |
| C11N03 | Amarrados assim, nenhum dos dois tem resposta própria. | 3,8 | `FadeIn(nota)` |
| C11N04 | Medir um decide o outro na mesma hora. | 3,8 | `Flash(qa)` + `ReplacementTransform(VGroup(qa, qb), par_1)` |
| C11N05 | E a resposta podia ter sido a outra, com a mesma facilidade. | 5,4 | `ReplacementTransform(par_1, par_0)` |
| C11N06 | São esses dois fenômenos, e mais nada. A conta que o circuito faz é a mesma do capítulo nove. | 8,8 | O `FadeOut` que fecha o `p10_fundamentos` emendado com o `Write(eqc)` que abre o circuito, num `play` só — a limpeza pertence a esta fala, não ao silêncio entre blocos |
| C11N07 | Os fios de cima carregam o expoente; o de baixo guarda o resultado. | 5,8 | `Create(fios)` + `FadeIn(kets)` + `FadeIn(keta)` + `FadeIn(vd)` |
| C11N08 | Pondo os de cima em superposição, o expoente deixa de ser um número e passa a ser todos eles de uma vez. | 9,6 | `LaggedStart(FadeIn(inis, scale=0.7))` — os mesmos cartões em gradiente do `C11N01`, agora em fila |
| C11N09 | As caixas são a exponenciação modular do capítulo quatro, montada bit a bit do expoente. | 6,7 | As quatro iterações do `for` das portas — `FadeIn(px)` + `Create(lig)` + `FadeIn(dot)` — num bloco só |
| C11N10 | Como a entrada era todo mundo, a saída também é. | 4,6 | `FadeIn(retic)` |
| C11N11 | Só que medir devolve um número só. | 3,3 | `FadeIn(med)` |
| C11N12 | Um resto sorteado entre os possíveis. | 2,9 | `Flash(med)` + `FadeIn(c4, scale=1.4)` |
| C11N13 | Nos fios de cima entra a transformada de Fourier quântica, que é onde o algoritmo mora. | 7,1 | `FadeIn(tqf)` + `Write(rot_tqf)` |
| C11N14 | Ela trabalha num tamanho fixo, uma potência de dois grande o bastante. | 5,4 | `FadeIn(nq)` |
| C11N15 | E o que ficou nos fios de cima não é um expoente: são todos os expoentes que dão aquele resto. | 9,2 | O `FadeOut` que fecha o circuito emendado com `Write(sub)`, num `play` só |
| C11N16 | Na reta, eles não estão espalhados: aparecem de tempos em tempos, sempre com a mesma distância entre um e o seguinte. | 9,6 | Seis `play` num bloco só: `Create(retaZ)` + `FadeIn(rotZ)` e as cinco iterações do `for` dos dentes (`GrowFromEdge` + rótulo) |
| C11N17 | E essa distância é exatamente a ordem que estamos procurando. | 4,6 | `LaggedStart(FadeIn(chaves))` + `Write(legenda_r)` — as chaves `+6` e o `r` amarelo nascendo juntos. É a frase que o capítulo inteiro existe para dizer |
| C11N18 | Afastando a câmera, o padrão se repete até o fim do registrador. | 5,4 | Três `play` sob esta linha: a saída de `rotulos_b`/`chaves`/`rotZ`, o `retaZ → retaF` com os dentes viajando, e o `LaggedStart(resto)` com o pente inteiro brotando |
| C11N19 | Só que medir agora não adianta: sairia um dente sorteado, e um dente sozinho não diz nada sobre o espaçamento. | 9,6 | `FadeOut(sub, legenda_r, rotF)` com o `pente_grupo` encolhendo para o topo, num `play` só. O pente fica lá em cima o resto do capítulo — é a referência que a curva vai responder |
| C11N20 | É aqui que a transformada entra: cada dente do pente vira uma onda. | 5,8 | `FadeIn(titulo)` |
| C11N21 | A posição do dente decide a frequência da onda dele. | 4,6 | As três iterações do `for` das ondas — `Create(o)` + `FadeIn(r)` — num bloco só |
| C11N22 | São centenas delas, uma por dente. | 2,9 | `FadeIn(mais)` + `FadeIn(tres_pontos)` |
| C11N23 | E o que sai é a soma de todas. | 3,8 | `GrowArrow(seta)` + `FadeIn(rot_s)` |
| C11N24 | Na maior parte do caminho elas se cancelam entre si. | 4,6 | `Create(soma)` — a curva de interferência se desenhando |
| C11N25 | Sobra sinal em poucos lugares, e a distância entre eles é o inverso do espaçamento do pente. | 7,5 | `LaggedStart(FadeIn(picos))` |
| C11N26 | Vale ver de perto por que o cancelamento acontece. | 4,2 | O `FadeOut` que fecha as ondas emendado com `FadeIn(giro)`, num `play` só |
| C11N27 | Em cada posição da saída, cada dente vira uma seta, e as setas se somam ponta a ponta. | 8,3 | `Create(guia)` + `FadeIn(roleta)` + `FadeIn(leitura_k)` + `FadeIn(leitura_mag)` + `Create(barra_fundo)` + `FadeIn(barra)` |
| C11N28 | Quando elas apontam para lados diferentes, o caminho se enrola e não sai do lugar. | 6,7 | `k_tr → 3` com `FadeIn(m2)` — a corrente azul enrolando dentro do círculo-guia |
| C11N29 | E isso vale para quase toda posição. | 3,3 | `FadeOut(m2)` + `FadeIn(m2b)` |
| C11N30 | A soma segue perto de zero enquanto a leitura sobe. | 4,6 | `k_tr → 82`, quatro segundos de varredura contínua. A fala acaba antes; o resto corre em silêncio, e é assim que tem que ser |
| C11N31 | Até chegar perto de um múltiplo daquela distância. | 3,8 | `FadeOut(m2b)` + `FadeIn(m3)` |
| C11N32 | Aí todas apontam para o mesmo lado, e o caminho vira uma reta. | 5,8 | `k_tr → 85` com `rate_func` de desaceleração — a cadeia se desenrolando até a linha reta |
| C11N33 | É onde a probabilidade se junta. | 2,9 | `Flash(roleta[2])` |
| C11N34 | Percorrendo todas as leituras possíveis, isso desenha a distribuição de saída. | 5,0 | `FadeOut(textos_ato2)` + `Create(eixos)` + os dois rótulos e, emendado, `Create(ja_visto)` — dois `play` sob esta linha |
| C11N35 | E o resto do caminho é sempre a mesma coisa: quase nada entre um pico e outro. | 7,5 | `k_tr → N − 1`, dez segundos de curva nascendo com a roleta girando junto. **É a animação mais longa da série e a mais longa que a fala**: sobram dois segundos e meio de silêncio, e eles são o clímax visual do vídeo |
| C11N36 | Os picos caem nos múltiplos de um mesmo valor, e é esse valor que carrega a ordem. | 7,5 | `FadeOut` da roleta inteira (`grupo_vivo` + `grupo_roleta`) e, emendado, `LaggedStart(Create(marcas))` — as tracejadas laranja em `1·N/r`, `2·N/r` e assim por diante |
| C11N37 | Agora medir vale a pena: o que sai é um pico. | 5,0 | `GrowArrow(seta)` + `Write(med)` + `Flash` |
| C11N38 | A leitura é uma fração do tamanho do registrador, e a ordem está escondida nela. | 6,7 | O `FadeOut` do pente, da curva, das marcas e dos eixos emendado com `Write(linhas[0])`, num `play` só |
| C11N39 | Um método antigo, de frações contínuas, devolve a fração pequena que se esconde ali. | 6,3 | `Write(linhas[1])` |
| C11N40 | E o denominador é a ordem. | 2,9 | `Write(linhas[2])` |
| C11N41 | Vale conferir: a potência devolve um, como tinha que devolver. | 4,6 | `Write(linhas[3])` — a congruência com o ✓ verde |
| C11N42 | Daqui em diante é o capítulo anterior inteiro, sem nada de quântico. | 5,4 | `Write(linhas[4])` — a diferença de quadrados, a mesma manobra do `C10N12` |
| C11N43 | Diferença de quadrados, dois máximos divisores comuns... | 3,3 | `Write(linhas[5])` |
| C11N44 | ...e o número está fatorado. | 2,5 | `Write(linhas[6])` + `Create(caixa)` emendados, num `play` só — os três números grandes e coloridos que a série inteira estava devendo |

**Subtotal: 249,4 s** (cartão + 44 locuções)

---

## Encerramento

O último bloco da série. O cadeado volta pela quarta vez e é a única vez em que ele quebra
de verdade.

| Tag | Fala | Est. | Entra em |
|---|---|---|---|
| V4N01 | Foi isso que a série prometeu no primeiro vídeo: a aposta que protege a internet tem uma saída, e ela tem nome. | 9,6 | Mesma composição do `V3N01`, invertida no resultado. A `caixa` verde do `C11N44` desce e vira o pedestal; o cadeado do `V4N00` volta por cima dela, com "fatorar n" gravado e a rachadura parada onde o vídeo 3 deixou. Em "tem uma saída", a rachadura **termina de correr** pelo arco inteiro, o arco estala em dois e os pedaços caem — a quebra que o `V3N02` prometeu |
| V4N02 | Só que o exemplo que acabou de rodar tem dois dígitos. Os números do RSA têm centenas, e para eles seriam necessários milhares de qubits estáveis. Nenhuma máquina de hoje chega perto disso. | 14,6 | Em "tem dois dígitos", o número da moldura verde cresce em quantidade de dígitos até estourar as bordas do quadro. Em "milhares de qubits", um punhado de cartões-qubit do `C11N01` entra ao lado e **continua do mesmo tamanho** enquanto os dígitos correm — a desproporção é o argumento, e nenhuma legenda precisa dizê-la |
| V4N03 | A aposta não caiu: ela ganhou prazo. E a resposta já está sendo construída — uma criptografia que não vive de fatorar. | 9,6 | A rede de cadeados anônimos do `V1N03` volta ao fundo, apagada e **intacta**. Os cacos do cadeado quebrado sobem e se remontam num cadeado de outra forma, que fecha inteiro no lugar dele — sem letras gravadas, porque ainda não é assunto desta série |
| V4N04 | Do resto de uma divisão até aqui foram quatro vídeos. Obrigado por ter chegado até o fim. | 7,1 | A rede sai e os quatro títulos voltam na trilha vertical do `V1N06`, agora todos acesos; o título da série pousa por cima deles |
| — | *(cartão final, ~3 s)* | — | "Do Zero ao Algoritmo de Shor Quântico" e, embaixo, "fim" |

**Subtotal: 40,9 s** (4 locuções) + cartão ~3 s

---

## Projeção de duração

| Bloco | Locuções | Fala |
|---|---|---|
| Abertura | 1 | 13,1 s |
| Capítulo 9 | 16 | 103,0 s |
| Capítulo 10 | 37 | 202,0 s |
| Capítulo 11 | 45 | 249,4 s |
| Encerramento | 4 | 40,9 s |
| **Total** | **103** | **608,4 s** |

Somando o `PAD` de 0,35 s por locução (36,1 s), os dois cartões silenciosos (~7 s) e os
`limpar()` entre capítulos (~10 s), a projeção é de **cerca de 11 min 02 s** — abaixo da
faixa de 13–14 min que a estimativa por `cena.play` previa. A diferença vem de onde era
esperado: os 118 `play` do bloco não pedem 118 falas, porque as duas árvores do capítulo 10
e as varreduras do capítulo 11 são animações que se explicam sozinhas.

Uma única linha tem animação mais longa que a fala: `C11N35`, a curva de interferência
nascendo em dez segundos sob sete e meio de locução. Some uns 3 s ao render real. Os
demais trechos longos (`C11N30`, `C11N32`, `C10N32`) cabem dentro da fala com folga, e a
folga é silêncio com imagem correndo — o padrão da série.

Com o vídeo em 11 minutos, a costura para abrir o capítulo 11 num quinto vídeo **não
precisa ser usada**: a fronteira clássico/quântico fica dentro do mesmo upload, como
decidido no plano.

---

## Checklist de gravação

- [ ] Abertura — V4N00
- [ ] Cartões — CAP09 a CAP11
- [ ] Capítulo 9 — C9N01 a C9N15
- [ ] Capítulo 10 — C10N01 a C10N36
- [ ] Capítulo 11 — C11N01 a C11N44
- [ ] Encerramento — V4N01 a V4N04
- [ ] `python medir.py`
- [ ] Render de conferência com `NARRA = True`

---

## Convenção de tags

As tags de cada capítulo são contíguas: começam em `01`, sobem de um em um, sem buraco e
sem repetição. O número da tag é o número **de tela** do capítulo, não o do arquivo — o
`capitulo9b.py` recebe `C10N` e o `capitulo10.py` recebe `C11N`. O `conferir.py` lê o
número direto da tag, então uma tag `C10N` dentro do `capitulo10.py` seria reportada como
capítulo 10 fora de ordem.

---

## Pendências de código do capítulo 9 (`parte9`)

1. Headers + `LaggedStart(linhas_cel)` num bloco só (`C9N03`).
2. `with narra` envolvendo o `for k in range(3)` do zigue-zague: as duas primeiras
   iterações inteiras sob `C9N07` (seis `play`) e a terceira mais o `Flash` sob `C9N08`
   (três `play`). Hoje o laço roda solto — mesma correção do `C2N07` e do `C5N11`.
3. `with narra` envolvendo os quatro `play` das voltas extras — as duas chamadas de
   `volta_no_ciclo()` e os dois crescimentos do `mult` (`C9N11`).
4. Os `cena.wait(0.8)` depois do `mult` e depois do `rdef` saem: quem dá o respiro é o
   `PAD`.
5. **Final novo (`C9N13`)** — o pouso da definição, em um `play` único:
   - `FadeOut` de `head_c`, `head_l`, `lin_h`, `lin_v`, `linhas_cel`, `seta4`, `zig`,
     `eq`, `escolha`, `f0`, `nota`, `fs` e `mult`;
   - no mesmo `play`, `caixa_d` e `borda` nascem **centrados** — hoje o `caixa_d` está em
     `[-2.9, -0.5, 0]`, posição herdada de dividir a tela com a tabela; sem a tabela e sem
     a coluna direita, ele vai para o centro;
   - `rdef` com `FadeOut` atrasado (~0,5 s) em relação ao resto, e o `r` amarelo dele
     chegando ao `r` do `d2`/`d3` por `TransformFromCopy`.

   É exatamente o movimento do `C6N12` e do `C7N13`. Se o `pousar_teorema(cena, formula,
   texto, resto)` foi extraído para `ferramentas.py` no vídeo 3, é ele aqui também, com o
   `texto` vazio: o `d1` já é o título.
6. **Separar `Write(d4)`** do `Write(caixa_d)` — o pior caso é a fala `C9N14` e precisa de
   tempo próprio. O `borda` continua construído em volta do `caixa_d` inteiro (com o `d4`
   dentro) para que o layout não se mexa quando ele entrar.
7. O `cena.wait(1.8)` final sai: quem sustenta a caixa em cena é o `C9N15`.
8. A saída da caixa para o cartão `CAP10` precisa ser **um movimento só**, com o `limpar()`
   emendado no cartão — mesma nota do fim dos capítulos 6 e 7.

## Pendências de código do capítulo 10 (`parte9b`)

1. `with narra` envolvendo `Write(rotulo)`, `FadeIn(caixas[0])`, o `for i in range(3)`
   inteiro, `Create(volta)` e o `Flash` — sete `play` sob `C10N03`.
2. Os onze `cena.wait()` do arquivo saem, todos.
3. Blocos que precisam de um `with narra` cobrindo mais de um `play`, sem emendar os
   `play` entre si: `C10N06` (saída da cadeia + `e1 → e2`), `C10N09` (tronco + ramos da
   primeira árvore), `C10N10` (`ex` + `e3 → e4`), `C10N14` (tronco + ramos da segunda),
   `C10N17` (`comut` + reagrupamento), `C10N27` (`u1a` + `u1a → u1`) e `C10N28` (os três
   `play` da árvore do azar).
4. Blocos que precisam ser **emendados num `play` só**: `C10N25` (o `FadeOut` das árvores
   com o `FadeIn(cap5)`) e `C10N33` (o `FadeOut` do caso inútil com o
   `ReplacementTransform(fim.copy(), r1)`). Nos dois, a limpeza pertence à fala seguinte —
   separada, ela lê como fim de capítulo.
5. `C10N36` é `so_fala` com o `r3`/`cxa2` parados em cena; o `cena.wait(1.8)` final sai.
6. A saída para o cartão `CAP11` em um movimento só, com o `limpar()` emendado.

## Pendências de código do capítulo 11 (`parte10`)

1. Todos os `cena.wait()` das sete funções saem.
2. **Três `FadeOut` de fim de bloco mudam de dono.** O `FadeOut` que fecha
   `p10_fundamentos` pertence ao `C11N06`, o que fecha `p10_circuito` pertence ao
   `C11N15` e o que fecha `p10_ondas` pertence ao `C11N26` — em cada caso emendado, num
   `play` só, com a primeira animação do bloco seguinte. Como as funções são separadas, o
   jeito mais simples é mover cada `FadeOut` para o topo da função seguinte.
3. `with narra` envolvendo laços inteiros: as quatro portas do circuito (`C11N09`), os
   cinco dentes do zoom (`C11N16`, junto com `Create(retaZ)`) e as três ondas (`C11N21`).
4. `with narra` cobrindo mais de um `play`: `C11N02` (emaranhamento em dois `play`),
   `C11N18` (saída dos rótulos + zoom-out + `resto`), `C11N34` (eixos + `ja_visto`) e
   `C11N36` (`FadeOut` da roleta + `marcas`).
5. **Desenrolar o `for i, linha in enumerate(linhas)` do `p10_ato4`** em sete blocos
   nomeados, `C11N38` a `C11N44`, e tirar o `cena.wait` de dentro dele. O `Create(caixa)`
   entra emendado no último `play`, não sozinho.
6. `C11N35` é a única linha da série em que a animação estoura a locução de propósito
   (dez segundos de `k_tr` contra sete e meio de fala). Não encurtar o `run_time` para
   fazer caber: o excedente é o efeito.

## Pendências de código da costura (vídeo 4)

1. **`quebrar(cena, cad, run_time)` em `cadeado.py`** — a função que o docstring do
   `rachar()` já promete. Ela recebe um `cad` que **já carrega** a `rachadura` do
   `rachar()`, estende a fissura até as duas pontas do arco, parte o arco em dois pedaços
   e deixa os dois caírem com rotação. É a mesma peça que o `V1N04` pede no vídeo 1, então
   ela nasce uma vez e serve aos dois.
2. **A abertura do vídeo 4 reconstrói o estado final do vídeo 3.** Como cada vídeo é
   renderizado separado, o `V4N00` chama `cadeado("fechado")`, `gravar(..., "fatorar n")`
   e `rachar()` **em silêncio**, antes da locução, para que o primeiro quadro case com o
   último quadro do vídeo 3. A rachadura tem perfil fixo no `cadeado.py`, então os dois
   renders batem exatamente.
3. A rede de cadeados anônimos do `V1N03` volta no `V4N03`. Ela é a mesma construção
   (pontos + arestas + `cadeado()` de corpo vazio em opacidade ~0,3) e vale extrair para
   `cadeado.py` quando o código do vídeo 1 for escrito, em vez de duplicar aqui.
4. A trilha vertical dos quatro títulos do `V1N06` volta acesa no `V4N04` — mesma nota:
   ela nasce no vídeo 1 e é reaproveitada aqui.
5. `CARTOES` em `montagem.py` ganha as entradas que faltam: `9: 5.0`, `10: 5.4`,
   `11: 5.8`.
6. `shor/videos/video4.py` com `abertura()` e `encerramento(cena, caixa)`, no molde do
   `video3.py`: a `abertura()` também toca o `CAP09` (quem a chama não deve chamar
   `abre_capitulo(cena, 9)`), e o `encerramento()` recebe a moldura verde do `C11N44`
   ainda em cena, sem `limpar()` entre os dois.
