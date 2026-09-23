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
| V4N00 | A série inteira levou a uma frase: quebrar o RSA é fatorar um número grande. Este vídeo mostra o algoritmo que faz isso — e ele percorre um caminho longo até lá. | 13,1 | O cadeado do fim do vídeo 3 volta ao centro **no estado em que ficou**: `estado_v3()` monta o `cadeado("fechado")` com "fatorar n" gravado no corpo e a rachadura já parada no meio do arco, e ele entra com `cena.add`, **sem animação nenhuma** — o primeiro quadro do vídeo 4 é o último quadro do vídeo 3. Enquanto a série é recapitulada, uma aproximação lenta no cadeado, como o Ken Burns do `ABN01`. Em "quebrar o RSA é fatorar", `Indicate` no rótulo gravado. Em "o algoritmo que faz isso", `avancar()` de dois segmentos: a fissura corre e **para de novo** — ela só termina no encerramento. Em "percorre um caminho longo até lá", o cadeado encolhe e sai por cima do ombro do quadro, já com o cartão de marca entrando por baixo |
| — | *(cartão silencioso, ~4 s)* | — | "Do Zero ao Algoritmo de Shor Quântico" nasce no centro e "Vídeo 4 de 4 — O algoritmo de Shor" embaixo dele. Mesma emenda dos vídeos 2 e 3: o subtítulo sai primeiro e o título encolhe por último, já com o `CAP09` entrando por baixo |

**Subtotal: 13,1 s** (1 locução) + cartão ~4 s

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

| Tag | Fala | Est. | Entra em |
|---|---|---|---|
| CAP09 | O caminho até a fatoração se baseia em uma propriedade muito importante da exponenciação modular. | 7,2 | cartão |
| C9N01 | A mesma equação do capítulo quatro do segundo vídeo volta. Mas a pergunta agora não é mais descobrir o resto. | 8,5 | `Write(eq)` |
| C9N02 | O módulo e a base não mudam; quem anda é o expoente. E a base tem inverso, como o capítulo cinco pedia. | 8,2 | `FadeIn(escolha)`. Em "tem inverso", `Indicate` na palavra `inversível` cinza que a `escolha` já carrega |
| C9N03 | A tabela de multiplicação do módulo volta, e é nela que a caminhada vai acontecer. | 6,1 | `head_c` + `head_l` + `lin_h` + `lin_v` e o `LaggedStart(linhas_cel)` correm emendados, num bloco só |
| C9N04 | Somente a linha da base interessa. | 2,6 | `GrowArrow(seta4)` + `Indicate(head_l[4])` |
| C9N05 | A caminhada parte do expoente zero, que vale um. | 3,6 | `Create(c00)` + `Write(f0)` |
| C9N06 | E subir um degrau no expoente é o mesmo que multiplicar pela base — ou seja, pular para a linha dela. | 7,5 | `FadeIn(nota)` |
| C9N07 | Cada passo desce até a linha da base, e o resultado vira a coluna do passo seguinte. | 6,2 | As **duas primeiras voltas do laço** inteiras — seis `play`: `desce`/`alvo`, `Write(fs[0])`, `sobe`/`topo`, `desce`/`alvo`, `Write(fs[1])`, `sobe`/`topo`. O `with narra` envolve o `for`, não cada iteração dele: mesma correção do `C2N07` e do `C5N11`. **Seis `play` em 6,2 s** — ver a pendência 9 do capítulo |
| C9N08 | Até que a caminhada devolve o um que é o mesmo ponto de partida. | 4,7 | O terceiro passo do laço: `desce`/`alvo`, `Write(fs[2])` com o ✓, e o `Flash(ponto(4, 7))` — os três `play` sob esta linha |
| C9N09 | O caminho é um ciclo fechado. Daqui em diante, ele só se repete. | 5,1 | Dois `play` sob esta linha: `Create(fecha)` + `Indicate(c00)` e, em seguida, `Write(VGroup(mult[0], mult[1], mult[2]))`. **A congruência mudou de dono**: ela era a fala cortada e agora entra sob "ele só se repete" — sem isso o `mult` nunca nasce e os `TransformFromCopy` do `C9N10` e do `C9N11` ficam sem origem |
| C9N10 | E cada volta completa no ciclo devolve potências congruentes ao mesmo resto. | 5,6 | Os quatro `play` das duas voltas extras num bloco só: `volta_no_ciclo()`, o `4⁶` nascendo por `TransformFromCopy`, `volta_no_ciclo()` de novo e o `4⁹` com o `(mod 9)`. É a irmã do "e assim por diante" do `C2N07` |
| C9N11 | O menor deles é o que interessa. | 2,4 | Um `play` só: `Write(rdef[0])` + `Write(rdef[1])` + `TransformFromCopy(mult[2][1], rdef[2])` — o `3` amarelo nasce do expoente que fechou o ciclo, não de um `Write` do vazio. Cabe com folga nos 2,4 s da fala |
| C9N12 | Ele é a ordem modular dessa base. | 2,4 | **A virada, igual à do `C6N12` e à do `C7N13`.** Um `play` só: a tabela (`head_c`, `head_l`, `lin_h`, `lin_v`, `linhas_cel`, `seta4`, `zig`) e a coluna direita inteira (`eq`, `escolha`, `f0`, `nota`, `fs`, `mult`) saem em `FadeOut`, e no mesmo bloco `caixa_d` e `borda` nascem já centrados. O `rdef` sai meio segundo atrasado em relação ao resto, e o `r` amarelo dele chega ao `r` do `d2`/`d3` por `TransformFromCopy` — o caso particular é a última coisa a desaparecer debaixo do geral. O `d1` já diz "ordem modular de a módulo n", então **não** entra título separado aqui. **É a linha mais apertada do capítulo**: 2,4 s de fala para o movimento mais complexo dele — ver a pendência 9 |
| C9N13 | E ela pode ser enorme: no pior caso, do tamanho da contagem de Euler. | 5,3 | **O pior caso ACONTECENDO, na mesma tabela e com outra base.** Quatro `play`: (1) `Write(d4)`; (2) a definição encolhe para a coluna da direita (`bloco.animate.scale(0.8).move_to([3.3, 0, 0])`) e por baixo dela a tabela mod 9 volta — `FadeIn(tab9)` + `lin_h` + `lin_v`, a legenda `a = 5` `(mod 9)` e o `GrowArrow(seta5)` na linha 5, com o `Create(ini5)` no 1 de partida; (3) o ciclo do 5 inteiro num `LaggedStart(*degraus, lag_ratio=0.8)` — `1 → 5 → 7 → 8 → 4 → 2 → 1`, seis degraus, um por resto invertível, a ida atravessando a tabela para a direita e a volta descendo pela esquerda até o `ini5`, que só pisca (`Indicate`) porque já está lá; (4) `Write(cont9)` (`r = 6 = φ(9)`) com o `Indicate` no `φ(` `n` `)` cinza do `d4` em "a contagem de Euler" — a peça que o capítulo 7 definiu e o 8 gastou. **A fala não lê nenhum degrau**: aqui não entra congruência escrita, o que a tela mostra é o comprimento do caminho. Base 5 é raiz primitiva mod 9, então o ciclo passa pelos seis invertíveis e `r` bate exatamente em `φ(9)` — é o `d4` virando exemplo. **Quatro `play` em 5,3 s** — ver a pendência 9 |
| C9N14 | Procurar testando um expoente por vez custa muito caro para módulos grandes. | 5,9 | **O módulo cresce, como no `C8N39`.** Cinco `play`: (1) `tab9`, `caminho5`, `ini5` e `seta5` saem e as duas linhas da tabela mod 9 se desdobram na malha inteira — `ReplacementTransform(VGroup(lin_h, lin_v), malha21)`, a legenda vira `n = 21` e a contagem vira `φ(21) = 12`; (2) `malha21 → malha39` com `n = 39` e `φ(39) = 24`; (3) `malha39 → malha77` com `n = 77` e `φ(77) = ?`; (4) a contagem COLAPSA dentro do `φ(n)` do `d4` (`move_to(phi4).scale(0.2).set_opacity(0)` + `Indicate(phi4)`) — a conta que ninguém faz à mão; (5) a malha e a legenda saem e a definição retoma o centro em `scale(1 / 0.8)`. O quadrado do miolo é **fixo**: quem cresce é o número de células, por isso os dígitos saem e sobra só malha. **Cinco `play` em 5,9 s** — ver a pendência 9 |
| C9N15 | Guarde a pergunta: qual é o menor expoente que devolve um. O próximo capítulo mostra que ela leva à fatoração. | 8,6 | `so_fala` — a caixa parada em cena. Em "o menor expoente", `Indicate` no `r` amarelo do `d3` |

**Subtotal: 89,9 s** (cartão + 15 locuções)

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

| Tag | Fala | Est. | Entra em |
|---|---|---|---|
| CAP10 | Como a ordem modular vira uma ferramenta de fatoração. | 4,3 | cartão |
| C10N01 | Voltamos ao número do RSA: um produto de dois primos muito difícil de fatorar. | 6,3 | `Write(obj)` — o `p × q ?` com os primos ainda como letras |
| C10N02 | E escolhemos uma base qualquer. | 2,3 | `Write(base)` |
| C10N03 | Dela procuramos a ordem modular, do mesmo jeito do capítulo anterior: multiplicando pela base até acontecer um loop. | 8,3 | Sete `play` num bloco só: `Write(rotulo)`, `FadeIn(caixas[0])`, as três iterações do `for` (`seta` + `rot` + `caixas[i+1]`), `Create(volta)` + `rv` e o `Flash`. O `with narra` envolve o laço inteiro |
| C10N04 | Quatro passos foram dados, então o valor da ordem é quatro. | 4,9 | `Write(rper)` com os `Indicate` nos quatro rótulos `×8` |
| C10N05 | Podemos então escrever a seguinte congruência. | 3,0 | `Write(e1)` + `Indicate(rper)` |
| C10N06 | Diminuindo um de ambos os lados, podemos notar que a ordem entrega um múltiplo do número que queremos fatorar. | 8,4 | **Três `play` num bloco só.** A saída da cadeia (`caixas`, `setas_o`, `volta`, `rv`, `base`, `rotulo`) com o `rper` subindo para o canto; `ReplacementTransform(e1, e2)`; `FadeIn(nota)` em "um múltiplo do número" — a `nota` escreve a frase que a fala acaba de dizer |
| C10N07 | Em outras palavras, a potência menos um é igual a 35 vezes x. | 5,3 | `ReplacementTransform(e2, e3)` + `FadeOut(nota)` |
| C10N08 | Aqui essa árvore não junta, ela reparte: o tronco em cima e os fatores embaixo. | 6,9 | Os dois `play` da primeira árvore sob esta linha: o tronco `rb` nascendo por `ReplacementTransform` de uma cópia da própria conta, e `Create(linB)` com o `35` e o `x` descendo dos termos de `e3` |
| C10N09 | Para descobrir o x é só isolar a variável na equação, mas isso não é tão importante. | 7,9 | Três `play` sob esta linha: `Write(ex)`; `ReplacementTransform(e3, e4)` com `FadeOut(ex)` e `fBx → fB117`; e `ReplacementTransform(e4, eqB_a)`, que desce a conta para `eqB_a` em `[3.5, 0.62, 0]` — só a cabeça nasce agora, com o espaço da cauda (`eqB_b`) reservado à direita; ela chega no `C10N13` |
| C10N10 | Para encontrar outros fatores dessa potência menos um, podemos utilizar a diferença de quadrados dos produtos notáveis. | 8,8 | Dois `play` sob esta linha: `Indicate(eqB_a)`; e `Write(dgen)`, num traço lento (2,0), a identidade GENÉRICA `x² − 1 = (x − 1)(x + 1)` aparecendo **direto** — o nome "diferença de quadrados" fica só na fala, nunca escrito na tela, e nunca um número por extenso. A linha `d0` + `dgen` já nasce diagramada e centrada em `[0, 2.15, 0]`: `dgen` entra no lugar definitivo e o espaço do `r par ⇒` fica reservado à esquerda, para nada refluir no `C10N11` |
| C10N11 | Para isso, note que a ordem r precisa ser par. | 4,6 | **Um `play` só, a linha inteira para ele.** `TransformFromCopy(rper[0], d0[0])` + `Write(d0[1:3])` — o `r par ⇒` crescendo **na frente** do que já está escrito, com o `r` amarelo nascendo do `rper` parado no canto (mesmo gesto do `C9N11`). Sem mais nenhuma manobra competindo pelo tempo, a condição "r precisa ser par" pesa sozinha antes de a álgebra continuar |
| — | *(sem fala — a substituição roda muda, como a segunda árvore do `C10N12`)* | — | Três `play` em silêncio, fora de qualquer `with narra`, logo depois do `C10N11`, todos folgados de propósito — é a passagem mais suave do capítulo: primeiro o `FadeOut` do `r par ⇒` sozinho (já cumpriu o papel), para que a troca de token não dispute a atenção; depois o `x → 8²` token a token (1,6) — `FadeOut` no `x²`/`− 1 =` genéricos, `TransformFromCopy(eqB_a[0:2], d1[0:2])` trazendo o `8⁴ − 1 =` de volta como cópia da conta que já está em cena, e um `ReplacementTransform` por token (`dgen[2:7] → d1[2:7]`) mostrando o `x` virando `8²` nos dois parênteses; por fim `ReplacementTransform(d1, d2)` (1,3), que fecha a manobra em `65 · 63`. Nem `C10N10` nem `C10N11` dizem "oito" em voz alta — por isso a conta pode ficar muda até aqui |
| C10N12 | Portanto, ficamos com o mesmo número aberto de dois jeitos diferentes. | 5,5 | Antes desta linha, **em silêncio** (os dois `play` fora de qualquer `with narra`, depois da substituição acima): o tronco `ra` por `ReplacementTransform` de uma cópia de `d2[0:2]`, e `Create(linA)` com `fA65`/`fA63` descendo de `d2[2]`/`d2[4]`. Sob esta linha, dois `play`: `ReplacementTransform(d2, eqA_a)`, que desce a conta para `eqA_a` em `[-3.5, 0.62, 0]` — espelhando `eqB_a`, cauda `eqA_b` também reservada à direita; e o nascimento de `junta`, que não é mais um `ReplacementTransform` de `d2`: ela nasce por `TransformFromCopy(eqA_a[2:5], junta[0])` e `TransformFromCopy(eqB_a[2:5], junta[2:4])`, um lado direito voando de cada equação, com só o `Write(junta[1])` (o sinal de igual) sendo escrito |
| C10N13 | Por definição, os dois primos são fatores de 35 — e os de 117 a gente só batiza. | 8,3 | Quatro `play` sob esta linha. `Create(linB2)` + `FadeIn(nB)` — `nB` na ordem `z, y, q, p`, z e y pendurados no `fB117`, q e p pendurados no `fB35`; depois `Write(eqB_b)` + `ReplacementTransform(junta, j2)`, que preenche a cauda reservada de `eqB_a` com os mesmos quatro fatores. Por fim os dois destaques, cada um acendendo o galho **junto** do que pende dele: `Indicate(fB35)` com `nB[2]`/`nB[3]` em "fatores de 35", e `Indicate(fB117)` com `nB[0]`/`nB[1]` em "os de 117" — o galho e os filhos piscando juntos dizem de onde cada par veio, que é exatamente o que a fala afirma |
| C10N14 | Como isso é uma igualdade, os mesmos fatores têm que aparecer do outro lado também. | 6,7 | Dois `play` sob esta linha: `Indicate(j2[1])`, o sinal de igual do meio; e `TransformFromCopy(j2[2:7], eqA_b)`, o lado direito do `j2` inteiro atravessando a igualdade e preenchendo a cauda reservada de `eqA_a`. **Nada comuta aqui:** o `j2` fica exatamente como está e `eqA_b` nasce na MESMA ordem da cauda da direita (`= (z · y) · (q · p)`) — são os mesmos fatores do outro lado, e só isso |
| C10N15 | A multiplicação é comutativa, então os fatores se reagrupam — e com sorte p e q caem um em cada lado. | 8,7 | Quatro `play` sob esta linha. O primeiro é a COMUTATIVIDADE, nos dois lugares ao mesmo tempo e emendados: `j2[0] → j3[0:5]` (só o **lado esquerdo** do `j2`, o `65 · 63`, vira o reagrupamento; o lado direito só acompanha o deslocamento, token a token) junto de `eqA_b → eqA_b2`, a cauda da equação da árvore comutando no mesmo gesto. Depois `Create(linA2)` + `FadeIn(nA)`, os fatores já reagrupados descendo para a árvore da esquerda — `nA` na ordem `p, y, z, q`, espelhando `nB`. Por fim os dois `Indicate` do par que se separou: `nA[0]` + `nB[3]` no rosa, `nA[3]` + `nB[2]` no verde-claro |
| C10N16 | Então podemos perceber que os dois números que acabamos de calcular compartilham fator com o número que queremos fatorar. | 8,4 | Dois `play` sob esta linha. `Indicate(fA65)` + `Indicate(fA63)` — quem compartilha fator com o `35` são os dois números da árvore da esquerda, e o gesto é o de apontar para eles. Depois `Indicate(obj[0], color=LARANJA)` em "o número que queremos fatorar", herdado do `C10N15` quando aquela linha perdeu a cauda. Nenhum texto na tela: a frase inteira fica na fala |
| C10N17 | E achar fator comum é fácil, utilizando o algoritmo de Euclides, o mesmo que apareceu de passagem no capítulo cinco. | 9,6 | **Dois `play` num bloco só:** `Write(m1)` com os `Indicate` no par verde-claro, depois `Write(m2)` com os `Indicate` no par rosa |
| C10N18 | Finalmente conseguimos descobrir os fatores p e q, o que parecia uma tarefa impossível. | 7,3 | `ReplacementTransform(VGroup(m1, m2), fim)` + `Create(cxa)` |
| C10N19 | O número que abriu o capítulo está fatorado. | 3,8 | `ReplacementTransform(obj, obj2)` — o `p × q ?` do topo vira os dois primos com ✓ |
| C10N20 | Como nem tudo são flores, existe a chance de coisas darem errado — por exemplo, a base pode resultar em uma ordem ímpar. | 9,6 | O `FadeOut` das duas árvores e das contas emendado com `FadeIn(cap5)`, num `play` só. O `fim` dentro da moldura verde **fica em cena** o resto do capítulo: o sucesso segue à vista enquanto a falha roda |
| C10N21 | Ou a ordem pode não dar informações úteis. | 3,3 | `so_fala` — o quadro parado. `Indicate(cap5)`, que é exatamente a frase que a fala diz |
| C10N22 | Para ver isso acontecer, vamos a outro exemplo, também com a ordem par. | 5,8 | Dois `play` sob esta linha: `Write(u0)` e `Indicate(u0[6], color=AMARELO)` — o `6` da ordem, em "também com a ordem par" |
| C10N23 | O caminho roda inteiro, sem nenhum erro. | 3,3 | `Write(u1a)` e `ReplacementTransform(u1a, u1)` — dois `play` sob esta linha. `u1a` já nasce como `24⁶ − 1 = (24³ − 1)(24³ + 1)` em tokens coloridos (`pot` para as duas potências de base 24), a mesma manobra do `C10N10`–`C10N11` com o `x` já substituído — sem texto corrido nem cor fora da paleta |
| C10N24 | Só que desta vez os dois primos não se separam: caem juntos, do mesmo lado. | 5,5 | Quatro `play` num bloco só: tronco `ru`, `Create(linU)` com `fu1`/`fu2`, `Create(linU2)` + `FadeIn(nU)`, e por fim `Indicate(nU[0], color=ROSA)` + `Indicate(nU[1], color=VERDE2)` — o p e o q lado a lado sob o mesmo galho, que é o que a fala afirma |
| C10N25 | Isso acontece porque esse número acabou sendo múltiplo de 35. | 5,5 | Dois `play` sob esta linha: `FadeIn(multi)` + `GrowArrow(setam)` + `Indicate(fu1, color=PRETO)`, e depois `Indicate(multi[1], color=LARANJA)` — o `35` do rótulo, em "múltiplo de 35" |
| C10N26 | Então um mdc devolve o próprio 35... | 3,5 | Dois `play` sob esta linha: `Write(m3)` e `Indicate(m3[5], color=LARANJA)`. O destaque vai em `play` próprio pela razão do `C10N04`: dentro do `Write` ele guardaria o estado sem preenchimento do começo e o devolveria no fim, deixando o resultado invisível o resto do capítulo |
| C10N27 | ...e consequentemente o número do outro lado não tem nenhum fator em comum com ele. | 5,7 | Dois `play` sob esta linha: `Write(m4)` e `Indicate(m4[5], color=PRETO)` — o `1`, mesma razão do `C10N26` |
| C10N28 | São os dois fatores triviais de 35, que a gente já conhecia sem precisar fazer tudo isso. | 7,7 | Dois `play` sob esta linha: `Write(triv)` e `Indicate(m3[5], color=LARANJA)` + `Indicate(m4[5], color=PRETO)`. O `FadeIn(sol)` **não entra aqui** — ele foi para a linha seguinte, junto da fala que o explica |
| C10N29 | Quando dá nisso, troca-se a base e roda de novo — e cada tentativa nova tem pelo menos cinquenta por cento de chance de acertar. | 10,4 | Dois `play` sob esta linha: `FadeIn(sol)` e `Indicate(sol, color=CINZA)`. O destaque vai em `play` próprio pela razão do `C10N26`: junto do `FadeIn`, o `Indicate` guardaria o `sol` ainda invisível (o `FadeIn` zera a opacidade antes) e devolveria esse estado no fim, deixando o cartão invisível o resto do capítulo. Animação curta sob fala longa: o cartão da solução aparece exatamente quando ela é dita, e o quadro fica parado no ✗ vermelho durante os ~9 s seguintes — é essa parada que faz a falha pesar |
| C10N30 | Com os dois primos na mão, encontramos a contagem de Euler. | 4,3 | Dois `play`. O `FadeOut` do caso inútil emendado com `ReplacementTransform(fim.copy(), r1)` num `play` só — a contagem **nasce de dentro** dos dois primos que ficaram na moldura verde. Depois `Indicate(r1[12], color=PRETO)`, o `24` |
| C10N31 | E com ela, a chave privada é só o inverso da chave pública, fácil de encontrar. | 6,7 | Três `play`: `Write(r2)`; `Indicate(r2[2], color=AZUL)` em "a chave privada"; e `Indicate(r2[0], color=VERMELHO)` + `Indicate(VGroup(r2[5], r2[6], r2[7]), color=LARANJA)` em "o inverso da chave pública" — é a tabela de inversos do `C8N17` sendo cobrada |
| C10N32 | Ou seja, fatorar o módulo e descobrir a chave privada são a mesma coisa. | 5,9 | Dois `play`: `Write(r3)` + `Create(cxa2)`, e `Indicate(r3[2], color=VERDE)` — o sinal de igual, que é literalmente "são a mesma coisa" |
| C10N33 | Agora falta uma peça só: acelerar a busca da ordem modular. É isso que o computador quântico faz. | 8,3 | `with narra` com um `play` só: `Indicate(r3[1], color=LARANJA)`, o `n`. Não é `so_fala` — `so_fala` não roda `play` nenhum. O `r` amarelo do `C9N15` não serve aqui: o `rper` sai no `FadeOut` do `C10N20` |

**Subtotal: 214,8 s** (cartão + 33 locuções)

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

| Tag | Fala | Est. | Entra em |
|---|---|---|---|
| CAP11 | Como o computador quântico encontra a ordem modular depressa. | 5,8 | cartão |
| C11N01 | A computação que a gente usa todo dia, a computação clássica, é feita de lógica sobre bits. | 7,9 | `LaggedStart` de nove cartões chapados do `_fila_classica`, alternando `0` laranja e `1` verde, mais o rótulo `computação clássica`. A fila é ímpar de propósito: o cartão do meio é um `0` e cai no centro do quadro, que é onde o bloco inteiro vai acontecer |
| C11N02 | E um bit só tem dois estados possíveis: ou ele é zero, ou ele é um. | 5,8 | `Succession` de dois `ReplacementTransform` no cartão do meio, que cresce em `scale(1.5)`: `0 → 1 → 0`. O repertório do bit se esgota à vista, e é esse esgotamento que dá sentido ao gradiente que vem depois |
| C11N03 | Só que a física quântica descobriu que a realidade é mais complicada do que isso. | 7,0 | `FadeOut(resto_fila)` + `FadeOut(rot_cl)`. Sai a fila **menos** o cartão do meio, que já foi consumido pelo `ReplacementTransform` — um `FadeOut(fila)` inteiro o traria de volta piscando. A tela esvazia na linha da virada |
| C11N04 | Existem outros estados primitivos, e é deles que a computação quântica tira proveito. | 7,4 | `ReplacementTransform(bit_0, qub)`: o cartão sólido **vira** o cartão em gradiente, no lugar em que já estava. Regra 4 da gramática visual — o qubit não entra em cena, ele nasce do bit |
| C11N05 | No lugar de um bit que só carrega zero ou um, a computação quântica usa um qubit. | 7,0 | `FadeIn(t1)` + `ReplacementTransform(qub, q1)` — o cartão viaja do centro para `[-4.0, 1.3, 0]` e o rótulo `superposição` entra por cima. O `q1` chega por movimento, não por `FadeIn` |
| C11N06 | E o que o qubit carrega é a probabilidade de a medida devolver cada um dos dois. | 7,0 | `TransformFromCopy(q1[0], b)` para as duas barras do `_barras_peso`, verde e laranja, nascendo do próprio gradiente. Alturas diferentes de propósito: o qubit não é meio a meio, e essa é a única imagem de probabilidade do capítulo |
| C11N07 | E dois qubits podem ainda ficar emaranhados. | 3,8 | `FadeIn(qa)` e, emendado, `Create(fio)` + `FadeIn(no)` + `FadeIn(qb)` — os dois `play` num bloco só. **O `t2` não entra aqui**: a palavra emaranhamento passou para a fala, e escrevê-la no mesmo `play` em que ela é dita seria legenda. O par sobe sem título por estes quatro segundos, e é a fala que o nomeia |
| C11N08 | Desse jeito, nenhum dos dois tem mais uma resposta própria. | 5,5 | `FadeIn(t2)` + `FadeIn(nota)`, num `play` só — **o rótulo `emaranhamento` entra aqui**, uma fala depois de a palavra ter sido dita. Escrito assim ele não legenda, ele confirma, e a metade direita do quadro recupera o título que faz par com a `superposição` da esquerda. A `nota` cinza, essa sim, diz na tela a frase que a locução seguinte fala — o mesmo par deliberado do `C10N21` com o `cap5` |
| C11N09 | Então medir um deles já decide o valor do outro na mesma hora. | 5,4 | `Flash(qa)` + `ReplacementTransform(VGroup(qa, qb), par_1)` e, emendado, `ReplacementTransform(par_1, par_0)` — os dois colapsam juntos, primeiro em `1` e `1` e depois em `0` e `0`. **O segundo colapso não tem locução própria, e isso é decisão de roteiro, não descuido**: ele corre no fim da fala, dizendo sem palavra nenhuma que o par podia ter caído do outro lado. O que fica em cena espera em `cena.grupo_fundamentos`; a limpeza é do `C11N10` |
| C11N10 | De física é só isso, e mais nada. Agora vamos a outro exemplo, com um n que caiba no registrador, e a conta que o circuito faz é a exponenciação modular do capítulo quatro. | 15,0 | Um `play` só. `FadeOut(cena.grupo_fundamentos)` logo no começo, em "De física é só isso" — a limpeza pertence a esta fala, não ao silêncio entre blocos. Em "outro exemplo", atrasado por `Succession` no mesmo padrão do `C11N35`, o `Write(eqc)` da congruência `c ≡ 2ᵇ (mod 21)`: o `21` entra quando o exemplo novo é anunciado, e a fala não o lê. "Vamos a outro exemplo" é o mesmo gesto do `C10N22`: marca em voz alta a troca do n do capítulo 10 (35) para o n deste capítulo (21) |
| C11N11 | E ela já tinha um desenho no final daquele capítulo: cada bit do expoente liga ou desliga uma potência. | 9,0 | Dois `play` emendados: `LaggedStart` das quatro caixas de bit `bᵢ` com o `…`, e depois `LaggedStart` de `GrowArrow` + `FadeIn` das quatro caixas cinzas `2^(2ⁱ) (mod 21)`. Tudo genérico, sem exemplo numérico — o circuito não vai rodar um expoente, vai rodar todos, e um número aqui diria o contrário |
| C11N12 | O produto de tudo que sai das caixas é a potência inteira, e ela devolve o resto. | 7,0 | Três `play` emendados: as quatro `setas2` convergindo, o `FadeIn(prod)` da caixa do produto — que é a própria fórmula do alto do quadro — e o `GrowArrow(seta3)` + `TransformFromCopy(eqc[0], saida)`, com o `c` da saída nascendo do `c` da congruência |
| C11N13 | O circuito quântico é esse mesmo desenho, com cada peça trocada pela equivalente quântica. | 7,8 | Quatro `play` emendados, na ordem em que a tradução precisa acontecer: a metade de baixo do esquema se recolhe e o `c` atravessa para a ponta do fio alvo; as caixas cinzas descem já virando `_caixa_porta`; as caixas de bit atravessam para a esquerda e as setas esticam virando as ligações de controle; e só então os fios ligam tudo. Nada sai por `FadeOut` — o esquema **vira** o circuito |
| C11N14 | Os fios de cima carregam o expoente b, e o de baixo guarda o resto c. | 6,0 | `FadeIn` dos dois fundos de painel primeiro e, no `play` seguinte, `TransformFromCopy(eqc[2][1], letra_b)` mais o `c` deslizando para dentro do painel de baixo. Fundo e conteúdo nunca no mesmo `play`: no Manim 0.20.1 o conteúdo fica atrás do preenchimento e some |
| C11N15 | Só que agora cada bit do expoente é um qubit. | 3,9 | `LaggedStart` de `ReplacementTransform` das quatro caixas de bit nos cartões-gradiente do fio, `lag_ratio=0.15` — cada bit vira qubit em cascata, na ordem em que estava no esquema. É o primeiro dos dois `play` do bloco antigo |
| C11N16 | E aí o expoente deixa de ser um número só: passa a ser todos eles de uma vez. Essa é a superposição que vimos. | 9,6 | A letra `b` abrindo na coluna dos expoentes com o `⋮` embaixo — o segundo `play` do bloco antigo, agora com locução própria. A superposição ganha nome na fala e conteúdo na tela ao mesmo tempo, em vez de as duas coisas correrem sob uma locução de treze segundos. A animação é curta para a fala, e aqui isso é aceito: o painel que acaba de se montar precisa de tempo parado para ser lido |
| C11N17 | Como o expoente carrega todas as possibilidades, o resto c deve carregar também. | 7,0 | `ReplacementTransform(saida_circ, carta_c[1])` + `FadeIn(carta_c[2])` — o `c` genérico abre na coluna dos restos possíveis |
| C11N18 | Medindo o fio de baixo. | 2,0 | `FadeIn(med)` — a caixinha `M` no fio alvo |
| C11N19 | Obtemos um resto possível, e com ele o sistema inteiro colapsa: sobram só os expoentes que devolvem esse mesmo resto. | 10,2 | `Flash(med)` + os dois `ReplacementTransform` do colapso, num `play` só: o painel de baixo vira um número, e o de cima perde os expoentes que não devolvem aquele número. O de cima **não** vira um expoente — continua em superposição, agora só dos que sobreviveram |
| C11N20 | Podia ter sido qualquer um dos restos do ciclo, e cada um deles deixa vivo um conjunto diferente de expoentes. | 9,2 | O laço do `rodizio` inteiro dentro do bloco: quatro `ReplacementTransform` de resto e de coluna, terminando de volta no resto com que o capítulo vai trabalhar. Um `with narra` cobrindo o `for`, nunca um por volta |
| C11N21 | Voltamos então para o problema do capítulo nove: podemos ver que a superposição possui as informações necessárias para resolvê-lo. | 11,3 | **Animação nova, pequena.** `Indicate(lista_b, color=AZUL)` — a coluna que sobreviveu ao colapso acende — e, emendado, um `r = ?` em laranja nascendo ao lado do painel de cima. A interrogação é o ponto: a informação está ali e ainda não dá para lê-la. O `r` usa a cor e o corpo do `r = 6` da cascata (`linhas[2]` do `C11N39`), porque é nele que esta peça vai se transformar: a pergunta atravessa o capítulo inteiro e só é respondida lá. Não mostrar espaçamento nem distância aqui — isso é do `C11N26`, e antecipar gastaria a virada do pente |
| C11N22 | Apesar de a superposição possuir os valores necessários, eles são apenas probabilidades, e uma medida devolveria um valor só, levando junto a informação que interessa: o r. | 15,0 | **Animação nova — a medida hipotética.** Cinco batidas, na ordem exata da frase. (1) `_barras_peso` em miniatura ao lado de cada entrada do `lista_b`, nascendo por `TransformFromCopy`: é a peça do `C11N06` voltando, e ela é o vocabulário que o capítulo já tem para probabilidade. (2) Um `M` **fantasma** nasce sobre os fios de cima — traço tracejado e `opacity` baixa —, e no mesmo `play` todo o resto da cena cai para uns 30% de opacidade. É esse escurecimento que marca o trecho como hipótese, e não como evento. (3) `Flash` no `M` fantasma e o `lista_b` colapsando num valor só, um dos que estavam ali. (4) O `pergunta_r` vira `VERMELHO` — que já é a cor de *isto não funciona* no `C11N38` — e é aqui que a fala diz "o r", pela única vez na série. A letra está na tela desde o `C11N21` sem ninguém a pronunciar; ela ganha nome no instante em que perde a resposta, e o `r = 6` do `C11N39` vira a resposta desta pergunta. (5) Tudo desfaz — opacidade de volta, coluna de volta, `M` fantasma sai, `pergunta_r` volta ao amarelo. O desfazer é o argumento, não um detalhe: a medida **não** aconteceu, e por isso o `C11N23` encontra a cena como o `C11N21` a deixou. Nada aqui pode reaproveitar o `med` do `C11N18`: aquele é o `M` de verdade, no fio de baixo, e confundir os dois desfaz a distinção que a batida inteira existe para fazer |
| C11N23 | Por isso, antes de medir, aplicamos aos fios de cima a transformada de Fourier quântica: é ela que resgata a informação do r. | 10,9 | `Indicate(VGroup(*fios[:4]), color=AZUL, scale_factor=1.0)` **antes** do `FadeIn(tqf)` — a fala nomeia os fios de cima antes de nomear a transformada, e o destaque acompanha a palavra. `scale_factor=1.0` porque um fio esticado sai do quadro. Depois `FadeIn(tqf)` + `Write(rot_tqf)` |
| C11N24 | Ela trabalha sempre num tamanho fixo: uma potência de dois grande o bastante. | 6,7 | `FadeIn(nq)` — a igualdade `N = 2⁹ = 512` em cima da caixa. O que fica em cena espera em `cena.grupo_circuito`, com o painel de cima desmontado em fundo, `⋮` e coluna viva |
| C11N25 | Vamos então entrar na transformada, levando com a gente apenas os expoentes que sobreviveram ao colapso, e a pergunta que ainda não sabemos responder. | 13,0 | **Animação reescrita — a entrada na transformada.** Três coisas num `play` só. (1) O `tqf` cresce até ser o quadro inteiro e só então o cinza abre: não é um `FadeOut` da caixa em cima do fio, é a câmera entrando nela — o espectador tem de entender que o que vem a seguir acontece dentro dela. O `rot_tqf` **não** cresce junto: ele vai para o canto superior esquerdo e fica de título até o `C11N29`, dizendo que tudo ali é dentro da transformada. (2) Todo o resto do `cena.grupo_circuito` sai: `eqc`, `fios`, `kets`, `keta`, `vd`, `inis`, `portas`, `plugues`, `retic`, `med`, `cartao_c[0]`, `cnum` e o fundo `carta_b[0]`. (3) Quatro peças **não** saem: o `lista_b` — a coluna viva de expoentes —, o `carta_b[2]` — o `⋮` embaixo dela, que o `C11N26` transforma no quinto dente —, o `pergunta_r` e o `nq`. Os três primeiros atravessam a expansão e pousam no centro do quadro, a coluna com o `⋮` embaixo e o `r = ?` acima dela; o `nq` encolhe para um canto, porque ele é o tamanho do registrador e o `C11N28` vai precisar dele quando a reta chegar a 512. **O `sub` deixa de existir**: a implicação `2^b ≡ 4 (mod 21) ⇒ b ∈ {2, 8, 14, 20, …}` era a ponte entre o circuito e a reta, e a coluna virando pente faz essa ponte sozinha, com o mesmo conteúdo e sem texto nenhum. Isso apaga o `Write(sub)` daqui e o `Circumscribe(sub[5])` do `C11N26` |
| C11N26 | Na reta, podemos notar que eles não estão espalhados: aparecem de tempos em tempos, sempre à mesma distância. | 9,6 | `Create(retaZ)` + `FadeIn(rotZ)` abrindo o bloco — a reta nasce debaixo da coluna que já está em cena desde o `C11N25`. Depois **o pente nasce da coluna, e é essa a mudança**: cada número do `lista_b` viaja por `ReplacementTransform` até a sua posição na reta e vira o `rotulos_b` de lá, com o dente crescendo por baixo dele em `GrowFromEdge(d, DOWN)` no mesmo `play`. São quatro números do painel para quatro dentes; o quinto dente, o do 26, nasce do `⋮` da coluna — o "e assim por diante" do painel vira o primeiro dente que ninguém tinha escrito, e é ele que autoriza o `C11N28` a estender o pente. **Não há mais `Circumscribe`**: o "eles" da fala é a própria coluna se transformando, que é o antecedente mais forte que a tela pode dar. Os dentes são **azuis**: cada dente é um expoente, e um pente verde diria que ali é uma fila de restos |
| C11N27 | E essa distância é justamente a ordem que procuramos. | 4,6 | `LaggedStart` das chaves laranjas entre dentes consecutivos, e o rótulo de cada chave é um `r` amarelo nascendo por `TransformFromCopy` do `r` do `pergunta_r` — **não** um `+6`. O `pergunta_r` fica em cena como está: `r = ?`. **Esta linha não revela o valor de r, e isso é a correção de conceito mais importante do capítulo.** O pente é o estado *dentro* da transformada, e nada ali é observável: se a tela escrever `r = 6` aqui, o espectador entende que a transformada entrega a ordem, e o resto do capítulo — ondas, interferência, medida, frações contínuas — vira enfeite. O que esta linha diz é *onde* a ordem está escrita (no espaçamento), não *quanto* ela vale. O valor só aparece no `C11N38`, depois da medida, e é lá que o `r = ?` vira `r = 6` |
| C11N28 | Afastando a câmera, podemos ver que o padrão se repete até o fim do registrador. | 6,8 | Três `play` emendados: saem os rótulos e as chaves **antes** da compressão, para nada se sobrepor; a reta curta vira a reta inteira levando os cinco dentes junto; e o resto do pente cresce num `LaggedStart` de lag baixíssimo. No terceiro `play`, `Indicate(nq)` — o `N = 2⁹ = 512` está guardado no canto desde o `C11N25` e "o fim do registrador" é exatamente ele. Sem esse destaque o número fica em cena sem nunca ser cobrado |
| C11N29 | O que a transformada faz é trocar cada um desses expoentes por uma cossenoide, e cada expoente dá uma frequência diferente. | 10,7 | **Bloco reescrito — o instrumento das ondas, na estrutura do `qft_shor_ondas_N512.html`.** Primeiro `play`, como está: saem as peças de dentro da caixa, o pente sobe para o alto e o `r = ?` encolhe para a borda direita. **O `titulo` "cada b vira uma onda em k" sai do capítulo** — era uma frase solta que ninguém sabia ler, e a fala já diz a mesma coisa. Depois, no lado direito do quadro, quatro linhas de onda, uma por expoente (`b` = 2, 8, 14, 20), empilhadas: cada uma é `cos(2π·b·k/N)` com `k` de 0 a 512 no eixo horizontal, em `AZUL`. **Cada onda nasce por `TransformFromCopy` do dente correspondente do pente lá em cima** — os quatro primeiros dentes são exatamente esses quatro `b` —, com o rótulo `b = 2` etc. à esquerda da linha. É aí que a frase "cada expoente dá uma frequência diferente" se vê: a de `b = 2` faz duas oscilações no quadro, a de `b = 20` faz vinte. Embaixo das quatro, `⋮` e `+81 ondas` em `CINZA`: o pente tem 85 dentes. O lado esquerdo do quadro fica vazio de propósito — é onde o círculo entra no `C11N30` |
| C11N30 | Depois ela soma todas essas ondas: em cada ponto, cada onda vira uma seta, e as setas são emendadas uma na outra. | 9,8 | Entram três peças, todas atadas a um `ValueTracker` `k_tr` em `k = 0`. (1) O **cursor**: uma linha vertical tracejada `LARANJA` atravessando as quatro ondas na posição `k`, com um ponto em cada onda na altura em que ela está ali. (2) O **círculo**, no lado esquerdo: um raio por expoente saindo do centro, girado de `2π·b·k/N` — os 85 fracos, e os quatro dos `b` mostrados fortes e rotulados na ponta (`2`, `8`, `14`, `20`). **Os quatro raios fortes nascem por `TransformFromCopy` dos quatro pontos do cursor** — é o "cada onda vira uma seta" da fala; os outros 81 entram por `FadeIn`. Depois, em "emendadas uma na outra", a corrente: as 85 setas em miniatura, ponta com cauda, e a **seta grossa** do centro até a ponta da corrente, que é a soma (`CIANO` quando o módulo passa de 0,6, `LARANJA` abaixo — a convenção da roleta antiga). Em `k = 0` todas apontam para o mesmo lado, então a corrente sai reta e a seta grossa tem o tamanho do raio. (3) O **traço da soma**, embaixo das ondas: uma linha de base com o rótulo `soma` em `CINZA` e, por cima, a curva do tamanho da seta grossa desenhada de 0 até o cursor (`always_redraw`, `CIANO`). Em `k = 0` ela é só um ponto no alto. **Saem do capítulo** a leitura `k = …`, a leitura `|soma| = …`, a barra e os três rótulos de texto da roleta antiga: o traço da soma já mostra o que eles mostravam |
| C11N31 | Na maior parte dos pontos, as ondas se desencontram e a soma quase desaparece. | 6,8 | `k_tr` de 0 a 70 em `linear`, quatro segundos. Tudo anda junto: o cursor corre pelas ondas e os quatro pontos ficam em alturas diferentes; os raios giram cada um num ritmo; a corrente se enrola e a seta grossa encolhe quase a nada; o traço da soma cai do alto e fica rente à base |
| C11N32 | Mas em alguns pontos todas elas se encontram, e a soma cresce de uma vez. | 6,3 | `k_tr` de 70 a 85 em `ease_out_sine`, três segundos — a desaceleração é o que faz o alinhamento ser lido como chegada. Em `k = 85` os quatro pontos do cursor estão **na mesma altura** (todos perto de −0,47, e não no alto: é o "se encontram" da fala, e ele não é óbvio sem ajuda), então, **depois** do `play`, quatro `DashedLine` horizontais curtas, uma em cada onda, passando pelo ponto dela — entram juntas (`lag_ratio=0`) e saem no mesmo bloco. São quatro e não uma porque as ondas estão empilhadas: uma horizontal só não passa pelos quatro pontos. No mesmo momento, `Flash` na ponta da seta grossa, que está esticada e `CIANO`, e o traço da soma subiu num pico |
| C11N33 | E seguindo até o fim do registrador, esses picos se repetem sempre à mesma distância. | 7,4 | `k_tr` de 85 a 511 em `linear`. **A única linha da série em que a animação estoura a locução de propósito**: dez segundos de varredura contra sete e meio de fala. O excedente é o efeito — o traço da soma termina de se desenhar, com os picos surgindo um a um, enquanto a locução seguinte já está para entrar. Não encurtar o `run_time` para caber |
| C11N34 | Então podemos ver que os picos caem nos múltiplos de um mesmo valor, e é ele que carrega a ordem. | 8,9 | Os updaters param. Saem o círculo inteiro (raios, rótulos, corrente, seta grossa), o cursor com os pontos e as quatro ondas com rótulos, `⋮` e `+81 ondas`. No mesmo `play`, o traço da soma com a base e o rótulo **cresce** para a faixa larga da parte de baixo do quadro — é a mesma peça ficando grande, não uma curva nova. Depois `LaggedStart` das **seis** marcas tracejadas `LARANJA` nos múltiplos de `N/r`, com os rótulos `0` e `1·N/r` a `5·N/r`. **A marca do 0 é obrigatória**: o traço da soma tem um pico em `k = 0` tão alto quanto o de 256 e mais alto que o de 85 (amplitude 1,00 contra 0,83), o espectador acabou de vê-lo se desenhar, e o `C11N35` transforma os rótulos no registrador de saída — sem a marca, o pico some na passagem |
| C11N35 | De volta ao circuito, o registrador de cima agora guarda só esses picos, e medir finalmente vale a pena. | 9,0 | **Bloco reescrito — a câmera sai da transformada.** É o `C11N25` ao contrário e com a MESMA peça: o cinza da TQF fecha sobre o instrumento, encolhe até ser de novo a caixa no fio (`rush_from`, que é o `rush_into` de lá lido ao contrário) e o circuito aparece em volta dela. A caixa volta **recuada**, no lugar que era do painel de entrada: aquele painel foi consumido pelo `C11N26` — virou o pente — e é depois da TQF que o registrador de saída precisa caber, coisa que no lugar antigo dela não cabia (os fios acabam em 6,6 e a caixa ia até 6,38). Por baixo do cinza sai tudo o que era de dentro da transformada: pente, traço, base, rótulo e as linhas das marcas. **Os seis rótulos `0` e `1·N/r` a `5·N/r` atravessam o cinza** — estão por cima dele em `z` — e no `play` seguinte viram as entradas do registrador de saída: um `_carta_super` `LARANJA` depois da TQF, alto o bastante para cobrir os quatro fios de cima, no mesmo vocabulário dos outros dois registradores. **Sem o `⋮`** do helper: ali a lista é completa, são esses seis picos e mais nenhum — e é por isso que o `0` tem de estar nela. No terceiro `play`, `_troca_coluna` põe os inteiros — `0`, `85`, `171`, `256`, `341`, `427` —, que é o que a medida devolve e o que a aritmética do fim usa: enquanto a tela disser `N/r`, o `85` da cascata não tem de onde vir. O `pergunta_r` volta para cima do registrador que vai respondê-lo, como ficava em cima do painel de entrada no circuito |
| C11N36 | Digamos que saia oitenta e cinco. | 2,9 | **Linha nova — a medida que vale a pena.** `FadeIn` do `M` cinza no fio, **depois** do registrador de saída: mesmo `caixa_cinza` do `C11N18`, e na linha e no corpo em que o `M` fantasma do `C11N22` ensaiou esta medida e a desfez. No `play` seguinte, `Flash` no `M` e o colapso do `C11N19`: o fundo do painel **fica** — o registrador continua sendo os quatro fios — e a coluna vira um número só. O quadro fecha com os dois registradores lado a lado, cada um com o seu `M` e o seu valor medido: `4` embaixo, `85` em cima. A fala continua sendo uma batida de resposta (exceção 2 da diretriz), e é a única vez que o número é dito — mas o "digamos que" marca a medida como **sorteio** entre os picos, e não como resultado garantido. É ele que prepara o parêntese do `C11N41`: "podia ter caído em outro pico" só faz sentido se a fala daqui não tiver prometido o 85 |
| C11N37 | A leitura é uma fração do tamanho do registrador, e a ordem está escondida nela. | 6,7 | Dois `play`. No primeiro, `FadeOut` do circuito inteiro — com a caixa da TQF, o `M` e o fundo do registrador de saída — emendado com o nascimento de `85 ≈ x · N/r`: o `85` **sai do registrador** e vira o `85` da equação por `ReplacementTransform`, e o resto entra por `Write`. É a equação que os rótulos das marcas já diziam, agora com o valor medido dentro. No segundo, ela vira `85/512 ≈ x/r` — dividir os dois lados pelo tamanho do registrador é exatamente o que a fala diz, e é aí que o `N` vira `512`. Os dois têm sete tokens, então o `85` cai no `85` e o `r` cai no `r`. **Os dois sinais são `≈`, nunca `=`**: `N/r` vale 85,33, e o 85 é o inteiro mais perto. É essa diferença que torna as frações contínuas necessárias no `C11N38` — se fosse igualdade, bastava simplificar a fração |
| C11N38 | Então usamos as frações contínuas, um método antigo, para achar a fração reduzida escondida ali. | 8,3 | `Write(linhas[1])` e, depois, `Circumscribe(linhas[0][0:3], color=LARANJA)` — o "ali" que fecha a frase é a leitura da **primeira** linha, em cena desde o `C11N37`; a de baixo começa igual mas nasce agora, e por isso fica fora. Laranja é a cor da leitura `k` no ato inteiro |
| C11N39 | E o denominador dela é a ordem que faltava. | 3,5 | `ReplacementTransform(pergunta_r, linhas[2])` — o `r = ?` que está no canto desde o `C11N29` (e que nasceu no `C11N21`) **vira** o `r = 6` da cascata. É o único lugar do capítulo em que o valor de r aparece, e é o lugar certo: depois da medida e das frações contínuas, que é quando o algoritmo de fato o conhece. A pergunta e a resposta são o mesmo objeto na tela |
| C11N40 | Vale conferir: a potência devolve um, como tinha que devolver. | 5,4 | `Write(linhas[3])` |
| C11N41 | Mas a medida podia ter caído em outro pico. | 4,2 | **Linha nova — o parêntese da medida que não serve.** A cascata inteira cai para 30% de opacidade, que é o device do `C11N22`: marca o trecho como o que **podia** ter acontecido. No mesmo `play`, `TransformFromCopy(linhas[1], …)` — a outra leitura nasce da linha da leitura que valeu, porque é a mesma conta com outro pico dentro: `171/512 ≈ 2/6`. Cada linha escurece sozinha, nunca num `VGroup` novo por cima delas. As três linhas da falha pousam nos lugares que as três últimas da cascata vão ocupar — o espaço está vazio, e o desfazer devolve ele |
| C11N42 | Aí a fração já vem simplificada, e o denominador é só um pedaço da ordem. | 6,6 | Dois `play`. O `2/6` se copia e se reduz a `= 1/3` — **é a linha inteira do argumento**: o pico medido é `x·N/r`, e as frações contínuas só sabem devolver `x/r` na forma reduzida, então quando `x` e `r` têm fator comum (aqui `x = 2`, `r = 6`) o que volta é `r` dividido por ele. O `6` é `AMARELO` porque é a ordem de verdade e o `3` é `VERMELHO` porque é o impostor: a cor conta a redução sozinha. Depois o `r = 3` nasce por `TransformFromCopy` do `r = 6` |
| C11N43 | A conferência pega isso na hora, e o jeito é medir de novo. | 5,8 | Dois `play`. A mesma conferência do `C11N40` nasce dela por `TransformFromCopy` e chega com o resto trocado e o visto virado: `2³ ≡ 8 (mod 21)` `✗`. **É para isto que aquela linha existe** — dos seis picos só o `1·N/r` e o `5·N/r` devolvem 6; o `0` não devolve nada (zero sobre 512 não tem denominador para ler), e os outros três caem aqui. Depois o parêntese fecha: a falha sai e a cascata reacende. O desfazer é o argumento, como no `C11N22`: medir de novo é o que o algoritmo faz, e a medida que vale continua sendo a de 85 |
| C11N44 | Daqui em diante é o capítulo anterior inteiro, começando pela diferença de quadrados. | 7,4 | `Write(linhas[4])` |
| C11N45 | Dois máximos divisores comuns depois... | 3,4 | `Write(linhas[5])` |
| C11N46 | ...e finalmente o número está fatorado. | 3,5 | `Write(linhas[6])` + `Create(caixa)`. A moldura verde sobrevive ao capítulo: o `V4N01` pousa o cadeado em cima dela, sem `limpar()` no meio |

**Subtotal: 343,8 s** (cartão + 46 locuções)

---

## Encerramento

O último bloco da série. O cadeado volta pela quarta vez e é a única vez em que ele quebra
de verdade.

| Tag | Fala | Est. | Entra em |
|---|---|---|---|
| V4N01 | Foi isso que a série prometeu no primeiro vídeo: a aposta que protege a internet tem uma saída, e ela tem nome. | 9,6 | Mesma composição do `V3N01`, invertida no resultado. A `caixa` verde do `C11N46` desce e vira o pedestal; o cadeado do `V4N00` volta por cima dela, com "fatorar n" gravado e a rachadura parada onde o vídeo 3 deixou. Em "tem uma saída", a rachadura **termina de correr** pelo arco inteiro, o arco estala em dois e os pedaços caem — a quebra que o `V3N02` prometeu |
| V4N02 | Só que o exemplo que acabou de rodar tem dois dígitos. Os números do RSA têm centenas, e para eles seriam necessários milhares de qubits estáveis. Nenhuma máquina de hoje chega perto disso. | 14,6 | Em "tem dois dígitos", o número da moldura verde cresce em quantidade de dígitos até estourar as bordas do quadro. Em "milhares de qubits", um punhado de cartões-qubit do `C11N05` entra ao lado e **continua do mesmo tamanho** enquanto os dígitos correm — a desproporção é o argumento, e nenhuma legenda precisa dizê-la. O cadeado quebrado e a moldura **ficam onde estão, intactos**: nada apaga, nada é empurrado — a faixa dos dígitos corre acima dos cotos e as cartas entram pelo flanco direito, e no fim sai só o que este bloco pôs em cena, para o `V4N03` receber o quadro do `V4N01` sem uma vírgula de diferença |
| V4N03 | A aposta não caiu: ela ganhou prazo. E a resposta já está sendo construída — uma criptografia que não vive de fatorar. | 9,6 | A rede de cadeados anônimos do `V1N03` volta ao fundo, apagada e **intacta**. Os cacos do cadeado quebrado sobem e se remontam num cadeado de outra forma, que fecha inteiro no lugar dele — sem letras gravadas, porque ainda não é assunto desta série |
| V4N04 | Do resto de uma divisão até aqui foram quatro vídeos. Obrigado por ter chegado até o fim. | 7,1 | A rede sai e os quatro títulos voltam na trilha vertical do `V1N06`, agora todos acesos; o título da série pousa por cima deles |
| — | *(cartão final, ~3 s)* | — | "Do Zero ao Algoritmo de Shor Quântico" e, embaixo, "fim" |

**Subtotal: 40,9 s** (4 locuções) + cartão ~3 s

---

## Projeção de duração

| Bloco | Locuções | Fala |
|---|---|---|
| Abertura | 1 | 13,1 s |
| Capítulo 9 | 15 | 89,9 s |
| Capítulo 10 | 33 | 214,8 s |
| Capítulo 11 | 46 | 343,8 s |
| Encerramento | 4 | 40,9 s |
| **Total** | **99** | **702,5 s** |

Somando o `PAD` de 0,35 s por locução (34,7 s), os dois cartões silenciosos (~7 s) e os
`limpar()` entre capítulos (~10 s), a projeção é de **cerca de 12 min 34 s** — abaixo da
faixa de 13–14 min que a estimativa por `cena.play` previa. A diferença vem de onde era
esperado: os 118 `play` do bloco não pedem 118 falas, porque as duas árvores do capítulo 10
e as varreduras do capítulo 11 são animações que se explicam sozinhas.

Uma única linha tem animação mais longa que a fala: `C11N33`, a varredura até o fim do
registrador, dez segundos sob sete e meio de locução. Some uns 3 s ao render real. Os
demais trechos longos (`C11N31`, `C11N32`, `C10N10`, `C10N28`) cabem dentro da fala com folga, e a
folga é silêncio com imagem correndo — o padrão da série.

Com o vídeo perto de 12 min 34 s, a costura para abrir o capítulo 11 num quinto vídeo
continua **sem precisar ser usada** — a fronteira clássico/quântico fica dentro do mesmo
upload, como decidido no plano. A margem, porém, acabou: o bloco de fundamentos cresceu de
5 para 10 locuções e paga 35 s; a medida no circuito (`C11N36`) e o parêntese da medida que
não serve (`C11N41`–`C11N43`) somam outros 19,5 s. O capítulo 11 tem hoje 46 locuções e é
sozinho metade da fala do vídeo. **Da próxima vez que ele crescer, a decisão não é mais de
roteiro: é reabrir a costura e fazer o quinto vídeo.**

---

## Checklist de gravação

- [ ] Abertura — V4N00
- [ ] Cartões — CAP09 a CAP11
- [ ] Capítulo 9 — C9N01 a C9N15
- [ ] Capítulo 10 — C10N01 a C10N33
- [ ] Capítulo 11 — C11N01 a C11N46
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

1. ~~Headers + `LaggedStart(linhas_cel)` num bloco só (`C9N03`).~~ **Resolvida.** É um
   único `LaggedStart` (headers em `AnimationGroup` + `linhas_cel` em `LaggedStart`
   aninhado) dentro de um só `cena.play`.
2. ~~`with narra` envolvendo o `for k in range(3)` do zigue-zague: as duas primeiras
   iterações inteiras sob `C9N07` (seis `play`) e a terceira mais o `Flash` sob `C9N08`
   (três `play`).~~ **Resolvida.** `_passo(k)` roda dentro do `with narra` das duas tags,
   com o `for k in range(2)` sob `C9N07` (seis `play`) e o terceiro `_passo` + `Flash`
   sob `C9N08` (três `play`).
3. ~~`with narra` envolvendo os quatro `play` das voltas extras — as duas chamadas de
   `volta_no_ciclo()` e os dois crescimentos do `mult` (`C9N10`).~~ **Resolvida.** Os
   quatro `play` (duas `volta_no_ciclo()`, dois `FadeIn`/`TransformFromCopy` do `mult`)
   estão dentro de um único `with narra(cena, "C9N10", …)`.
4. ~~Os `cena.wait(0.8)` depois do `mult` e depois do `rdef` saem: quem dá o respiro é o
   `PAD`.~~ **Resolvida.** Não há nenhum `cena.wait()` solto no capítulo — conferido, o
   `PAD` do `narra()` é quem sustenta o respiro em toda parte.
5. ~~**Final novo (`C9N12`)** — o pouso da definição, em um `play` único:~~ **Resolvida.**
   O `saida = AnimationGroup(...)` faz o `FadeOut` de todas as peças da tabela e do
   exemplo, escreve `corpo` (o `caixa_d` sem o `d4`) e cria a `borda`, já centrados em
   `ORIGIN`; o `LaggedStart(saida, FadeOut(rdef, ...), lag_ratio=0.4)` atrasa o `FadeOut`
   do `rdef` em relação ao resto, e os dois `TransformFromCopy(rdef[0], …)` levam o `r`
   amarelo até o `d2` e o `d3`.

   (O `pousar_teorema()` citado como possível extração nunca foi criado em
   `ferramentas.py` — o capítulo 9 refaz o movimento inline, o que está de acordo com a
   condição posta aqui.)
6. ~~**Separar `Write(d4)`** do `Write(caixa_d)` — o pior caso é a fala `C9N13` e precisa de
   tempo próprio.~~ **Resolvida.** `corpo` (escrito no `C9N12`) exclui o `d4`; o
   `Write(d4)` é o primeiro `play` do `C9N13`, e a `borda` já nasce em volta do `caixa_d`
   inteiro (com o `d4` dentro), então o layout não se mexe quando ele entra.
6b. ~~**O ciclo do 5 e as malhas (`C9N13`/`C9N14`) — animação nova.**~~ **Resolvida.**
   `_TAM`, `_CANTO`, `_MEIO_X` e `_LADO` estão no topo do arquivo e `parte9` lê
   `tam, canto = _TAM, _CANTO`; `_malha(m, w)` existe e é a grade inscrita no quadrado do
   miolo da tabela mod 9; `bloco = VGroup(borda, caixa_d)` viaja para `[3.3, 0, 0]` no
   `C9N13` e volta a `ORIGIN` no fim do `C9N14`, com o `d3[0][1]` sobrevivendo à ida e
   volta; o zigue-zague da base 5 roda em laço próprio sobre `ciclo5 = [1, 5, 7, 8, 4, 2,
   1]`, com `Indicate(ini5, …)` (não `Create`) fechando o ciclo no `C9N13`. A tabela mod 9
   volta por `FadeIn` dos mesmos `head_c`/`head_l`/`lin_h`/`lin_v`/`linhas_cel` que saíram
   no `C9N12`.
7. ~~O `cena.wait(1.8)` final sai: quem sustenta a caixa em cena é o `C9N15`.~~
   **Resolvida.** Não há nenhum `cena.wait()` no arquivo.
8. ~~A saída da caixa para o cartão `CAP10` precisa ser **um movimento só**, com o
   `limpar()` emendado no cartão — mesma nota do fim dos capítulos 6 e 7.~~ **Resolvida.**
   `parte9` devolve a caixa da definição viva (como o `parte8` devolve a tese) e o
   `cartao_capitulo(..., sai=)` apaga a peça recebida **dentro** do mesmo `cena.play` de
   1,3 s em que "Capítulo 10", o título e a linha entram — sem `limpar()` e sem quadro
   vazio entre os dois.
9. ~~**Orçamento de `run_time` do capítulo.** As estimativas novas são de fala, e três
   blocos ficaram com mais animação do que locução. Como o `narra()` roda o `play` inteiro
   e só depois completa o silêncio, o que estoura entra por cima do áudio da linha
   seguinte. Ajuste o `run_time`, nunca a fala:~~ **Resolvida.** Os cinco subitens estão
   fechados — nenhuma animação do capítulo estoura a locução dela:
   - ~~`C9N07` — seis `play` em 6,2 s: ~0,85 s cada, contra os ~1,0 s de hoje;~~
     **Resolvida.** Os seis `play` de `_passo(0)` e `_passo(1)` estão em 0,7 s cada
     (4,2 s ao todo), dentro do orçamento de 6,2 s.
   - ~~`C9N11` — a tabela pedia os dois `Write` do `rdef` emendados num `play` e o
     `TransformFromCopy` sobrando à parte (dois `play`), e o código junta os três num
     `cena.play` só.~~ **Resolvida.** Aqui quem cedeu foi o roteiro: a célula "Entra em"
     do `C9N11` passou a descrever o `play` único do código
     (`shor/capitulos/capitulo9.py:214-216`), de 0,9 s, que cabe com folga nos 2,4 s da
     fala.
   - ~~`C9N12` — 2,4 s para a virada inteira.~~ **Resolvida.** É um `play` só
     (`LaggedStart(saida, FadeOut(rdef, ...), lag_ratio=0.4)`) com o `FadeOut` do `rdef`
     atrasado; a duração total fica em torno de 1,2 s, bem dentro dos 2,4 s.
   - ~~`C9N13` — quatro `play` em 5,3 s: 0,8 + 1,2 + 2,2 + 0,9 = 5,1 s.~~ **Resolvida.**
     Os quatro `run_time` do código batem exatamente com esses números, e o
     `LaggedStart(*degraus, lag_ratio=0.8)` tem doze animações.
   - ~~`C9N14` — cinco `play` em 5,9 s: 1,5 + 1,1 + 1,0 + 1,0 + 1,0 = 5,6 s.~~
     **Resolvida.** Os cinco `run_time` do código batem exatamente com esses números.
10. ~~**O `Write(VGroup(mult[0], mult[1], mult[2]))` mudou de dono** e agora é o segundo
   `play` do `C9N09`.~~ **Resolvida.** É o segundo `play` de `C9N09`
   (`shor/capitulos/capitulo9.py:169`), e o `mult` já está em cena quando o
   `TransformFromCopy` do `C9N10` e o `TransformFromCopy(mult[2][1], rdef[2])` do `C9N11`
   o cobram.

## Pendências de código do capítulo 10 (`parte9b`)

O `capitulo9b.py` já tem `narra()`/`so_fala()` em todas as linhas, um por tag, sem nenhum
`cena.wait()` sobrando, com o passeio inteiro do `C10N03` num único `with narra` de sete
`play`, e com os blocos multi-`play` e os blocos emendados num `play` só já implementados
na maioria das linhas. O que falta é só o delta contra a tabela acima:

1. ~~**Renumeração `C10N01`–`C10N35` → `C10N01`–`C10N32`.**~~ **Resolvida** — com um
   número final diferente do que este item previa. O código hoje usa `C10N01`–`C10N33`
   (33 tags), e é exatamente esse o intervalo que a tabela atual do roteiro também usa
   (a tabela foi revisada depois deste item ter sido escrito: a realocação do item 4
   virou um trecho mudo, e não a fusão numa fala existente, o que muda a conta de "35 → 32"
   original para "35 → 33"). Conferida a numeração inteira, tag a tag, contra a tabela —
   bate.
2. ~~**`est=` de toda tag revisada** para o valor em segundos da coluna da tabela.~~
   **Resolvida.** Os 33 `est=` de `capitulo9b.py` batem, um a um, com a coluna "Est." da
   tabela — inclusive os três exemplos citados aqui (`C10N03` 8,3, `C10N05` 3,0, `C10N06`
   8,4).
3. ~~**As três fusões de bloco.**~~ **Resolvida.** O `FadeIn(nota)` é o quarto `play` do
   bloco `C10N06` (a saída da cadeia, o `e1 → e2` e o `Indicate` do sinal entram antes) e a
   tag isolada não existe mais — `C10N07` de hoje é a fala seguinte (`e2 → e3`). O par de
   `Indicate` rosa/verde-claro em `nA`/`nB` já está dentro do bloco `C10N15` (quatro `play`
   na mesma fala), sem tag própria. E os dois `Write`+`Indicate` de mdc (`m1`, depois `m2`)
   estão num único `with narra` — a tag `C10N17` de hoje —, com o nome `C10N21` livre para
   a locução do item 5.
4. ~~**Realocação do `ReplacementTransform(d1, d2)`.**~~ **Resolvida**, mas por um caminho
   diferente do que este item descreve: a tabela atual não bota o `d1 → d2` dentro do
   `with narra` do `C10N11` — ela manda a substituição inteira (`x → 8²` token a token e o
   `ReplacementTransform(d1, d2)` que fecha em `65 · 63`) rodar **muda**, fora de qualquer
   `with narra`, logo depois do `C10N11`. É exatamente o que o código faz
   (`capitulo9b.py:278-289`), e bate com a linha "—" que a tabela tem entre `C10N11` e
   `C10N12`.
5. ~~**Locução nova `C10N21`.**~~ **Resolvida.** `C10N21` é `so_fala` com
   `Indicate(cap5, color=CINZA)`, entre o `C10N20` (saída das árvores + `FadeIn(cap5)`) e
   o `C10N22` (`Write(u0)`).
6. ~~**O `so_fala` final vira `narra` com destaque.**~~ **Resolvida.** A última linha
   (`C10N33`) é `with narra` com `cena.play(Indicate(r3[1], color=LARANJA), ...)`, não
   `so_fala`.
7. ~~**Passada de destaques (`Indicate`/`Flash`) nos objetos que a tabela cita e o código
   ainda não anima.**~~ **Resolvida.** O exemplo citado — o `Indicate` no `(mod φ(n))` —
   está em `capitulo9b.py:575-577` (`Indicate(VGroup(r2[5], r2[6], r2[7]), color=LARANJA)`,
   hoje no bloco `C10N31`, não mais `C10N30`: a numeração deste item também está com um
   passo de atraso). Conferência linha a linha do restante da tabela contra o arquivo não
   achou nenhum `Indicate`/`Flash` pedido e ausente.
8. **A segunda árvore já roda fora de qualquer `with narra`** (o tronco `ra` e as ligações
   `linA`/`fA65`/`fA63`, logo antes do bloco que vira `C10N12`) — isso é o comportamento
   correto, não uma pendência: quem dá o respiro para esses dois `play` mudos é o `PAD` do
   `with narra` anterior (`C10N11`, o `d1 → d2`). Não existe nenhum `cena.wait()` ali nem em
   nenhum outro lugar do arquivo — não adicionar um "para dar tempo". **Confirmado**: é
   exatamente o que o código faz hoje.

## Pendências de código do capítulo 11 (`parte10`)

As sessões estruturais rodaram e o `capitulo10.py` está com as 46 locuções, a renumeração,
a divisão do `C11N15`/`C11N16`, as duas locuções novas antes da TQF, a medida hipotética do
`C11N22`, a entrada na transformada, o r escondido até a cascata, a passada de destaques e
os `est=` até a pendência 5, o instrumento das ondas, a saída da transformada e o parêntese
da medida que não serve. Não sobra nenhuma.

1. ~~`est=` a aplicar.~~ **Resolvida.** Conferido bloco a bloco: os 54 `est=` do
   `capitulo10.py` batiam com a coluna "Est." da tabela antes da pendência 5, que corta uma
   linha e muda um número.
2. **O número do exemplo muda no meio do vídeo e ninguém avisa.** O capítulo 10 fatora 35;
   o `capitulo10.py` fatora 21, com base 2, ordem 6 e registrador de 512. A troca é
   necessária — a ordem precisa ser par e o registrador precisa caber no quadro —, mas hoje
   o espectador atravessa a fronteira sem nenhuma frase que a marque, e o capítulo 10 já tem
   o gesto pronto no `C10N22` ("vamos a outro exemplo"). Ou o `C11N10` ganha uma frase e o
   `est=` sobe, ou o capítulo 10 passa a fatorar 21. As duas saídas mexem em roteiro.

   ~~**Decisão (2026-09-21): a primeira saída.** O `C11N10` ganha a frase "Vamos a outro
   exemplo, com um n que caiba no registrador: n = 21." antes da fala que já existia, e o
   `est=` sobe de 9,0 para 12,5 — já ajustado na linha da tabela acima. **Falta só o
   código**: o `run_time` do `play` de `C11N10` em `capitulo10.py` (hoje `FadeOut(...)` +
   `Write(eqc)` num `play` só, `run_time=1.0 * VEL`) precisa de folga para a locução mais
   longa, ou de um segundo `play`/gesto próprio para a frase nova — decisão de código, para
   a próxima sessão. Não mexi em `capitulo10.py` nesta auditoria.~~

   **Resolvida.** A fala foi reescrita com a física fechando antes de o exemplo novo abrir
   e sem o número dito ("um n que caiba no registrador", e o `21` só na congruência), o
   `est=` passou a 15,0 e o `Write(eqc)` cai em "outro exemplo" (~4,2 s), atrasado por
   `Succession` dentro do mesmo `play` do `FadeOut`.
3. ~~O `C11N22` deixa de ser `so_fala`.~~ **Resolvida.** As cinco batidas estão no código,
   com o `M` fantasma como peça nova e o bloco devolvendo a cena ao quadro do `C11N21`. Uma
   consequência que a pendência 4 precisa saber: depois do bloco, `lista_b` e `pergunta_r`
   passam a apontar para **cópias** (`coluna_volta` e `pergunta_amarela`), e são essas
   cópias que estão em cena e no `cena.grupo_circuito`.
4. ~~A entrada na transformada.~~ **Resolvida**, com uma diferença em relação ao que a
   célula antiga do `C11N25` pedia: o `rot_tqf` não cresce e some junto com a caixa — ele vai
   para o canto e fica de título até o `C11N29`. É melhor que a especificação, e a célula foi
   atualizada para descrever o que o código faz.
5. ~~O r deixa de ser revelado dentro da transformada, e o antigo `C11N29` é cortado.~~
   **Resolvida.** As chaves têm `r` como rótulo, o `r = ?` atravessa o capítulo e vira
   `r = 6` na cascata.
6. ~~O instrumento das ondas — `p10_ondas`, `p10_ato2` e `p10_ato3` viram um trecho só.~~
   **Resolvida.** Os onze blocos entre o `C11N29` e o `C11N45` viraram seis (`C11N29` a
   `C11N34`), as duas funções sumiram dentro do `p10_ondas` e a cascata subiu onze casas.
   O instrumento está na estrutura do `qft_shor_ondas_N512.html`, com uma diferença
   deliberada: o traço de baixo é o TAMANHO da seta grossa (a `amplitude`), e não a parte
   real da soma, que tem picos de alturas e sinais diferentes. Duas notas do que o render
   cobrou: os quatro pontos do cursor não partilham altura de tela — as ondas estão
   empilhadas —, então o "mesma altura" do `C11N32` são quatro traços curtos, um na onda de
   cada um, no mesmo lugar relativo; e as peças que entram soltas num `LaggedStart` ou num
   `TransformFromCopy` precisam sair uma a uma do `cena.remove`, porque tirar só o `VGroup`
   deixa as estáticas de `k = 0` em cena o trecho inteiro.
7. ~~A saída da transformada ganha corpo, e a medida ganha fala.~~ **Resolvida**, junto com
   o parêntese da medida que não serve (`C11N41`–`C11N43`). O `C11N35` deixa de
   apontar uma seta no pico: a câmera sai da transformada, o circuito volta inteiro e os
   rótulos das marcas viram, depois da TQF, o registrador de saída em `_carta_super`, que
   então vira os inteiros. A caixa da TQF volta recuada para o lugar do painel de entrada,
   porque no lugar antigo dela não sobrava fio depois. A medida passa a ter locução própria
   (`C11N36`, a linha nova) e acontece no fio, com o colapso do `C11N19`. A cascata desceu
   mais uma casa, e a aritmética começa uma linha antes: `85 ≈ x · N/r` nasce do registrador
   e vira o `85/512 ≈ x/r` que a cascata já tinha.
8. ~~**O pico em zero, o `≈` e três falas.** Tudo em `p10_ondas` e `p10_ato4`:
   - **O pico em `k = 0`.** Hoje as marcas são cinco (`1·N/r` a `5·N/r`) e o registrador de
     saída tem cinco entradas, com um comentário dizendo que a lista é completa. Não é: o
     traço tem um pico em 0 com amplitude 1,00, o mais alto junto com o de 256. Passa a haver
     seis marcas, a primeira em `k = 0` com rótulo `0` (e não `0·N/r`), seis rótulos em
     `cena.rots_marca`, seis entradas no `_carta_super` e seis inteiros no `_troca_coluna`:
     `0`, `85`, `171`, `256`, `341`, `427`. Confira que a coluna de seis cabe no painel sem
     sair dos quatro fios; se não couber, reduzir o `passo`, não a lista. Corrigir o
     comentário "a lista é COMPLETA — são esses os picos" e o "Dos cinco picos" do bloco do
     `C11N43`.
   - **`≈` no lugar de `=`** no `eq_k` (`85 ≈ x · N/r`) e no `linhas[0]` (`85/512 ≈ x/r`).
     Continuam com sete tokens cada, então o `ReplacementTransform` entre os dois não muda.
   - **`est=`**: `C11N35` 5.4 → 9.0, `C11N36` 1.8 → 2.9, `C11N38` 7.0 → 8.3. Nenhuma
     animação muda por causa deles — os três só ganham folga.~~ **FEITO.** As seis marcas
   (`range(6)`, rótulo `0` em `mlt == 0`) e os seis inteiros `0, 85, 171, 256, 341, 427`
   estão em `capitulo10.py:1109-1125` e `:1221`; os dois comentários já dizem "seis picos"
   (`:1181` e `:1317`), sem sobra do "cinco". Os dois `≈` estão em `eq_k` e `linhas[0]`
   (`:1241-1270`). Os três `est=` batem: `C11N35` 9.0 (`:1189`), `C11N36` 2.9 (`:1234`),
   `C11N38` 8.3 (`:1295`).

## Pendências de código da costura (vídeo 4)

1. ~~**`quebrar(cena, cad, run_time)` em `cadeado.py`** — a função que o docstring do
   `rachar()` já promete. Ela recebe um `cad` que **já carrega** a `rachadura` do
   `rachar()`, estende a fissura até as duas pontas do arco, parte o arco em dois pedaços
   e deixa os dois caírem com rotação. É a mesma peça que o `V1N04` pede no vídeo 1, então
   ela nasce uma vez e serve aos dois.~~ **FEITO** — `quebrar()` está em `cadeado.py:211`,
   com exatamente esse comportamento, e o `V4N01` a chama sobre o `cad` que já saiu do
   `rachar()` (via `estado_v3()`). Continua servindo aos dois vídeos: quando o `V1N04` for
   escrito, chama a mesma função.
2. ~~**A abertura do vídeo 4 reconstrói o estado final do vídeo 3.**~~ **FEITO** —
   `estado_v3()` no `cadeado.py` monta o cadeado já gravado e já rachado de uma vez, sem
   animação, e o `V4N00` o põe em cena com `cena.add`. O primeiro quadro do vídeo 4 foi
   comparado com o último do vídeo 3: mesma escala, mesmo rótulo, mesma fissura (só a
   posição muda, porque aqui não há tese embaixo).
3. ~~A rede de cadeados anônimos do `V1N03` volta no `V4N03`. Ela é a mesma construção
   (pontos + arestas + `cadeado()` de corpo vazio em opacidade ~0,3) e vale extrair para
   `cadeado.py` quando o código do vídeo 1 for escrito, em vez de duplicar aqui.~~ **FEITO**
   — `rede()` já mora em `cadeado.py:281`, com exatamente essa construção, e o `V4N03`
   chama essa função diretamente (`from ..cadeado import … rede`). Não há duplicação para
   desfazer quando o vídeo 1 for escrito: ele vai reaproveitar a mesma `rede()`.
4. ~~A trilha vertical dos quatro títulos do `V1N06` volta acesa no `V4N04` — mesma nota:
   ela nasce no vídeo 1 e é reaproveitada aqui.~~ **FEITO** — `trilha_videos(acesos=…)` em
   `shor/videos/comum.py`, o arquivo das peças que servem a mais de um vídeo. A versão
   apagada existe porque o `V1N06` precisa dela (`acesos=(1,)`); o `V4N04` chama
   `acesos=(1, 2, 3, 4)`. Os quatro nomes batem com os cartões de marca do `video2.py`,
   do `video3.py` e do `video4.py`, e com o cartão do vídeo 1 no roteiro dele.
5. ~~`CARTOES` em `montagem.py` ganha as entradas que faltam: `9: 7.2`, `10: 5.4`,
   `11: 5.8`.~~ **FEITO** — o `CARTOES` seguiu a tabela: a linha do `CAP10` na tabela do
   capítulo 10 diz 4,3 s, que é o que a fala do cartão dá na taxa daquele capítulo, e o
   `CARTOES[10]` passou a 4.3 para bater com ela. O `conferir.py` não acusa mais divergência.
6. ~~`shor/videos/video4.py` com `abertura()` e `encerramento(cena, caixa)`, no molde do
   `video3.py`: a `abertura()` também toca o `CAP09` (quem a chama não deve chamar
   `abre_capitulo(cena, 9)`), e o `encerramento()` recebe a moldura verde do `C11N46`
   ainda em cena, sem `limpar()` entre os dois.~~ **FEITO** — estão prontos a `abertura()`
   (V4N00 + cartão de marca + emenda no `CAP09`), o `V4N01` (a moldura desce e vira
   pedestal, o `estado_v3()` pousa em cima dela e o `quebrar()` derruba o arco), o `V4N03`
   (a `rede()` volta ao fundo e os cacos se remontam no `_cadeado_novo()`, que fecha com
   flash) e o `V4N04` + cartão final (a `trilha_videos()` acesa, o título por cima e o
   "fim" embaixo). A classe `VideoShor` do `filme_shor.py` monta o vídeo inteiro.
   O `V4N02` também está **FEITO**: o "21" da moldura sobe por cópia para uma faixa
   acima do cadeado e cresce, um dígito de cada lado por vez, até a fila ser cortada
   pelas duas bordas do quadro; as cartas-qubit do `C11N05` entram pelo flanco no
   tamanho de sempre enquanto os dígitos ainda correm, e no fim tudo o que o bloco pôs
   sai sem tocar no cadeado nem na moldura. **O encerramento inteiro está animado.**

