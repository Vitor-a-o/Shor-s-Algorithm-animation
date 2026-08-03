# Plano — reestruturação em série de 4 vídeos

*Documento de contexto do projeto. Suba este arquivo na base de conhecimento do projeto
Claude (botão "+" na página do projeto) para que qualquer chat novo já comece sabendo
onde o trabalho está.*

## Objetivo

Transformar o filme único "Do Zero ao Algoritmo de Shor Quântico" (11 capítulos, um
`FilmeCompleto` contínuo) em uma **série de 4 vídeos independentes para YouTube**.

## Mapa de vídeos decidido

| # | Vídeo | Capítulos | Arquivos | Situação da narração | Situação do roteiro novo |
|---|---|---|---|---|---|
| 1 | Introdução | — (100% novo) | — | não se aplica | ✅ `roteiro_video1_introducao.md` |
| 2 | Aritmética modular — as quatro operações | 1–5 | `capitulo1`–`capitulo5` | ✅ completa — `C1N`–`C5N` fechadas (`C1N16` mudou de texto e precisa ser regravada) | ✅ `roteiro_video2_aritmetica_modular.md` |
| 3 | Do teorema ao RSA | 6–8 | `capitulo6`–`capitulo8` | não escrita | pendente |
| 4 | O algoritmo de Shor | 9–11 | `capitulo9`, `capitulo9b`, `capitulo10` | não escrita | pendente — é o final da série |

Atenção à numeração dos arquivos: o **capítulo 10** em tela é o `capitulo9b.py` (Da Ordem
Modular à fatoração) e o **capítulo 11** é o `capitulo10.py` (Shor Quântico: a QFT
encontra o período). A lista `PARTES` em `montagem.py` já está na ordem certa.

## Decisões já tomadas

- **4 vídeos, não 5.** A divisão anterior separava o inverso modular (cap. 5) das outras
  operações e o punha junto com Fermat e Euler, agrupando-o pelo que ele *serve* e não
  pelo que ele *é*. O inverso é a divisão — ele fecha o conjunto soma, multiplicação,
  potência, inverso, e pertence ao vídeo das operações. Em troca, Fermat e Euler passam a
  dividir vídeo com o RSA, que é o único motivo de eles existirem na série: o vídeo monta
  o argumento e o gasta na mesma sessão, em vez de terminar em dois resultados abstratos
  sem pagamento. De quebra, resolve o problema do RSA sozinho render um upload curto
  demais.
- **Numeração em tela**: manter a numeração global dos capítulos nos cartões
  (`cartao_capitulo`) — "Capítulo 6" continua aparecendo mesmo estando no vídeo 3 — e
  indicar "Vídeo X de 4" na abertura de cada um. Os blocos ficam contíguos e legíveis:
  1–5, 6–8, 9–11.
- **Convenção de tags de áudio**: tags de capítulo continuam como estão (`C1N01`...); tags
  novas de costura de cada vídeo (abertura/recap/gancho) usam prefixo `V{n}N`. O vídeo 1
  vai de `V1N00` a `V1N11`, doze locuções.

## Projeção de duração

Os vídeos 1 e 2 já têm roteiro fechado, então a projeção deles vem da contagem real de
locuções, não mais de proxy. Os capítulos 6–11 ainda não têm narração escrita; a projeção
deles segue estimada por `cena.play`, calibrada pelos ~6,5 s de fala por `play` medidos no
`narracao.md` original (73 `play` → 467,8 s).

| Vídeo | Capítulos | `play` | Projeção |
|---|---|---|---|
| 1 Introdução | novo | — | ~2 min 45 s (roteiro fechado) |
| 2 Aritmética modular | 1–5 | 101 | ~11 min 45 s (roteiro fechado) |
| 3 Do teorema ao RSA | 6–8 | 74 | ~8–9 min |
| 4 O algoritmo de Shor | 9–11 | 118 | ~13–14 min |

O vídeo 2 veio ~45 s acima do teto da faixa estimada — o capítulo 5 (inverso modular)
saiu denso, com a leitura da tabela de multiplicação (`C5N19`–`C5N29`) sendo o trecho mais
caro. Se precisar encurtar, é ali ou nas variações de módulo do capítulo 2 (`C2N07`) que
sobra folga.

O vídeo 4 continua sendo o maior, com a fronteira clássico/quântico dentro dele (os
capítulos 9 e 10 são clássicos, só o 11 é quântico). A decisão foi **não** separar: quem
chega no quarto vídeo veio para ver a fatoração acontecer, e cortar entre "reduzi fatorar
a achar a ordem" e "o quântico acha a ordem" é interromper o clímax. Se o capítulo 11
crescer muito na escrita da narração, a costura para abrir ali já está identificada.

## Ordem de trabalho combinada

1. ~~Fechar a arquitetura da série (quantos vídeos, o que entra em cada um)~~ ✅ feito
2. **Escrever o roteiro de fala completo, ANTES de mexer no código** — mesma lógica do
   `narracao.md`: o texto com tags e estimativas de duração é o que dá o tempo real de
   cada animação. Vídeos 1 e 2 fechados (roteiro + costura). Faltam: a narração dos
   capítulos 6–11 e o roteiro de costura dos vídeos 3 e 4 (abertura/encerramento
   próprios, já que hoje só existe uma abertura/encerramento para o filme inteiro).
3. **Só então reestruturar o código** — via Claude Code (não no chat do projeto, que só
   enxerga uma cópia somente-leitura). Plano de arquitetura sugerido:
   - Manter `capitulo1.py`...`capitulo10.py`, `ferramentas.py`, `paleta.py` como estão
     (blocos reutilizáveis).
   - Trocar `montagem.py` único por um pacote `videos/` com um módulo por vídeo, cada um
     com sua própria `abertura()`/`encerramento()` e lista de capítulos.
   - Em `filme_shor.py`, criar uma `Scene` por vídeo (`VideoIntro`, `VideoOperacoes`,
     `VideoRSA`, `VideoShor`), mantendo as `Parte1`...`Parte11` existentes para debug
     isolado de capítulo.
   - `CARTOES` em `montagem.py` só tem estimativa para os cartões 1–4; preencher 5–11
     conforme a narração for escrita.
4. Gravar o áudio das tags novas, rodar `medir.py` (não precisa mudar — já varre
   `audio/*.wav` inteiro), renderizar cada vídeo separadamente.

## Arquivos já produzidos neste processo

- `roteiro_video1_introducao.md` — roteiro completo do vídeo 1, no formato do
  `narracao.md` (tags, fala, estimativa, sugestão de animação).
- `roteiro_video2_aritmetica_modular.md` — roteiro completo do vídeo 2 (capítulos 1–5),
  no mesmo formato: reaproveita `C1N`–`C4N` do `narracao.md` original (com uma linha
  reescrita, `C1N16`), escreve a narração inteira do capítulo 5 (`C5N01`–`C5N30`) e a
  costura própria do vídeo (`V2N00`–`V2N03`).

## Próximo passo em aberto

Vídeos 1 e 2 estão com roteiro fechado. Falta escolher entre escrever a narração dos
capítulos 6–8 (vídeo 3, teorema ao RSA) ou a dos capítulos 9–11 (vídeo 4, algoritmo de
Shor — o final da série). O que travar primeiro depende de qual vídeo vocês querem
produzir a seguir; nenhum dos dois tem narração escrita ainda.

## Pendências de código herdadas do roteiro do vídeo 1

- Um `cadeado.py` em `shor/`, com `cadeado(estado="fechado", rotulo=None)` devolvendo um
  `VGroup` com o arco separado do corpo — ele abre, fecha, chacoalha, se grava e quebra ao
  longo do vídeo 1.
- Uma função `previa(cena, titulo, cenas, dur)` para as miniaturas dos vídeos 2, 3 e 4.
  Ela exige quebrar `parte1`, `parte2`, `parte5`, `parte6`, `parte8` e `parte10` em
  sub-blocos nomeados, para extrair 3–4 segundos de cada um sem reanimar nada. **Decidir
  antes de escrever o código do vídeo 1**, porque muda a arquitetura dos capítulos.

## Pendências de código herdadas do roteiro do vídeo 2

- `capitulo1.py`: regravar o áudio de `C1N16` — o texto mudou ("os próximos capítulos"
  em vez de "os próximos três capítulos") porque o capítulo 5 passou a fechar o mesmo
  vídeo.
- `capitulo2.py`: o laço de módulos crescentes (`for n in (8, 9, 10, 11)`) hoje abre um
  `narra` por iteração; a narração nova (`C2N07`) cobre o laço inteiro com uma fala só
  ("e assim por diante"), então o `with narra(...)` precisa envolver o `for` de uma vez,
  não cada passo dele.
- `capitulo5.py` (`parte5`): duas divisões de `cena.play` que a narração exige e que hoje
  rodam junto —
  - separar `FadeIn(xis)` de `Write(mdc3)` em dois blocos (`C5N17` e `C5N18`);
  - tirar o `Write(como)` de dentro do bloco do `Indicate` dos cabeçalhos, para que ele
    aconteça antes (`C5N19` antes do `Indicate`, não junto).
