# Glossário — versão em inglês

A referência de toda tradução da série. Os roteiros em inglês (`roteiros/en/`) e os textos de
tela (`shor/textos.py`) seguem este arquivo. Quando um termo mudar aqui, ele muda nos dois.

---

## 1. Regras da tradução

1. **Mesmas tags, mesma ordem, mesmo número de linhas.** Tradução não funde nem divide fala.
   Se uma frase não cabe na batida em inglês, reescreve-se a frase, não a estrutura.
2. **A ordem dos itens nomeados dentro de uma fala é preservada** quando a animação depende
   dela. A lista está em `roteiros/sincronias.md` (vídeo 1, C11N10 e encerramento do vídeo 4,
   por fração) e na seção "Outras sincronias por ordem de palavra" do mesmo arquivo
   (capítulos 8, 10 e 11, por ordem de `play`). Exemplo: no `C8N31`, a fala tem de terminar
   em "smaller than the modulus", porque o `<` e o 33 entram por último.
3. **A fala não lê a tela**, em inglês também (`diretriz_fala_vs_animacao.md`). E, como a
   tela agora está em inglês, a fala usa os mesmos termos dela: se a tela diz `gcd`, a fala
   não diz "highest common factor".
4. **A tela e a fala usam o termo deste glossário.** Sinônimos variam o ritmo, mas aqui
   confundem: quem aprendeu "remainder" no capítulo 1 não pode encontrar "residue" no 5.
5. **Pessoa do discurso:** "we" para a matemática que se faz junto ("we add", "we get");
   "you" para falar com o espectador; "I" só onde o português tem "eu" (o autor no vídeo 1).
6. **Inglês americano** na grafia e na leitura de números (sem "and" em "five hundred twelve").
7. **A coluna "Entra em" não se traduz.** Ela é especificação do código, que é o mesmo nos
   dois idiomas; no roteiro em inglês ela fica como no português.

## 2. Decisões de tela

| Texto | Inglês | Por quê |
|---|---|---|
| Título da série | **From 0 to Shor's Quantum Algorithm** | O V1N05 remonta o título com os cacos do cadeado e exige 29 a 31 glifos sem espaço, com o "S" de Shor como primeiro "S" maiúsculo. Este tem 29 (o apóstrofo conta), e o "0" repete o nome do projeto. "From Zero to Shor's Quantum Algorithm" tem 32 e quebra o `assert`. |
| `SEGREDO` (capítulo 8) | **SECRETS** | O `_glifos()` troca letra a letra com `Xk9#R2q`: são exatamente 7 caracteres. "SECRET" tem 6. |
| `mdc(` | **gcd(** | Notação usual em inglês. |
| `TQF` | **QFT** | Quantum Fourier transform. |
| `fim` | **the end** | |

Os 83 textos de tela já estão preenchidos em `shor/textos.py`. Antes do primeiro render em
inglês, rode `python checar_textos.py`.

## 3. Terminologia

### Aritmética modular (vídeo 2)

| Português | Inglês |
|---|---|
| aritmética modular | modular arithmetic |
| o módulo (o número n) | the modulus |
| "módulo n", lido depois de uma congruência | "modulo n" |
| é congruente a | is congruent to |
| congruência | congruence |
| classe | class |
| representante | representative |
| resto | remainder |
| reta numérica | number line |
| dar a volta | wrap around |
| adição / multiplicação / exponenciação modular | modular addition / multiplication / exponentiation |
| Double and Add, Square and Multiply | iguais (já são os nomes em inglês) |
| binário | binary |
| inverso multiplicativo | multiplicative inverse |
| inversível | invertible |
| tabela multiplicativa | multiplication table |
| célula, linha, coluna | cell, row, column |
| mdc, máximo divisor comum | gcd, greatest common divisor (por extenso na primeira vez) |
| algoritmo de Euclides estendido | extended Euclidean algorithm |

### Teoremas e RSA (vídeo 3)

| Português | Inglês |
|---|---|
| Pequeno Teorema de Fermat | Fermat's little theorem |
| Teorema de Euler | Euler's theorem |
| função totiente de Euler | Euler's totient function |
| fi de ene, φ(n) | phi of n |
| a contagem de Euler | Euler's count |
| primo | prime |
| comutativa | commutative |
| chave pública / chave privada | public key / private key |
| quem envia / quem recebe | sender / receiver |
| canal público | public channel |
| cifrar / decifrar | encrypt / decrypt |
| mensagem | message |
| par de inversos | inverse pair |
| quebrar o RSA | break RSA |

### Ordem e Shor (vídeo 4)

| Português | Inglês |
|---|---|
| ordem modular | **order** (na definição: "the multiplicative order of a modulo n"; daí em diante, só "order") |
| fatorar / fatoração | factor / factoring |
| fatores triviais | trivial factors |
| ciclo | cycle |
| período | period |
| computação clássica / quântica | classical / quantum computing |
| computador quântico | quantum computer |
| bit, qubit | bit, qubit |
| superposição | superposition |
| emaranhamento | entanglement |
| registrador | register |
| fios de cima / de baixo (do circuito) | top wires / bottom wires |
| medir, a medida | measure, the measurement |
| colapso | collapse |
| transformada de Fourier quântica (TQF) | quantum Fourier transform (QFT) |
| ondas, picos, vales | waves, peaks, troughs |
| se cancelam / se reforçam | cancel out / reinforce each other |
| frações contínuas | continued fractions |

**Decisão a confirmar:** "ordem modular" não é termo usual em inglês. O padrão é "the order
of a modulo n" ou "multiplicative order". Por isso o título do capítulo 9 ficou
"Multiplicative Order", e os rótulos de tela usam "order of" e "finding the order of". Se você
preferir manter o paralelo com o português ("Modular Order"), a troca está em quatro chaves
de `textos.py` (`geral.titulo_cap9`, `geral.titulo_cap10`, `c9.ordem_modular_de`,
`c10.ordem_modular`) e não toca em nenhuma fala ainda.

## 4. Como a fala lê a notação

No roteiro em inglês, **números vão por extenso**, como no português: a contagem de palavras
e a leitura na gravação dependem disso. Letras de variável ficam como letras.

| Na tela | Fala |
|---|---|
| `x ≡ y (mod n)` | "x is congruent to y, modulo n" |
| `a²`, `a³` | "a squared", "a cubed" |
| `aʳ`, `2⁶` | "a to the r", "two to the sixth" |
| `φ(n)` | "phi of n" |
| `gcd(a, b)` | "the gcd of a and b" |
| `a⁻¹` | "the inverse of a" |
| `85/512` | "eighty-five over five hundred twelve" |
| `≈` | "about" |
| `101₂` | "one zero one in binary" |
| `729` | "seven hundred twenty-nine" |
| 1994 | "nineteen ninety-four" |
| `(e, n)` como chave | "the pair e, n" |

## 5. Ritmo e coluna Est.

A gravação do vídeo 1 em português mediu **2,79 palavras/s**, contra os 2,4 usados nas
estimativas: o `est=` do português está uns 14% acima da fala real. No roteiro em inglês, a
coluna Est. usa **2,6 palavras/s** até haver gravação em inglês para calibrar. Depois do
primeiro lote, `python medir.py en` dá a taxa real, e as estimativas dos vídeos ainda não
gravados são corrigidas.
