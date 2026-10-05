# Do Zero ao Algoritmo de Shor Quântico — manual do repositório

Série de vídeos em Manim sobre aritmética modular, RSA e o algoritmo de Shor.
Cada vídeo tem um roteiro em markdown; o código do filme está no pacote `shor/`.

---

## Estrutura

```
filme_shor.py              ponto de entrada do Manim (FilmeCompleto, Parte1…Parte11)
medir.py                   lê audio/<idioma>/*.wav e REGENERA shor/duracoes_<idioma>.py
conferir.py                confere roteiro × código (rodar sempre ao terminar)
audio/<idioma>/            TAG.wav, uma locução por arquivo (namespace global por idioma)
media/                     saída do Manim — nunca editar, nunca versionar
roteiros/                  os roteiros em pt e a diretriz — a especificação do que animar
roteiros/en/               os mesmos roteiros em inglês, mesmos nomes de arquivo
shor/
  idioma.py                IDIOMA ativo (env var IDIOMA, "pt" ou "en") — tudo importa daqui
  paleta.py                cores e parâmetros globais (VEL, COR_TEXTO, …)
  ferramentas.py           T, formula, MOD, traco, limpar, narra, so_fala, PAD
  duracoes_pt.py           GERADO pelo medir.py pt — nunca editar à mão
  duracoes_en.py           GERADO pelo medir.py en — nunca editar à mão
  montagem.py              ordem dos capítulos, TITULOS, CARTOES, abertura do filme
  cadeado.py               o cadeado da série
  capitulos/capituloN.py   um capítulo por arquivo (1–8, 9, 9b, 10)
  videos/videoN.py         abertura e encerramento próprios de cada vídeo da série
                           (video2.py, video3.py, video4.py)
  videos/comum.py          peças que servem a mais de um vídeo (ex.: trilha_videos)
```

Imports dentro de `shor/capitulos/` e `shor/videos/`: `from ..paleta import *`
e `from ..ferramentas import *`. Dentro de `shor/`: `from .paleta import …`.

**Dois níveis de montagem.** `montagem.py` monta o filme inteiro (`FilmeCompleto`);
`shor/videos/videoN.py` monta um vídeo da série, com abertura e encerramento
próprios, reaproveitando os mesmos capítulos. O vídeo 3 (`video3.py`) é o
modelo a seguir para o vídeo 4.

---

## O contrato: a TAG

Cada linha da tabela de um roteiro tem uma tag (`C8N07`, `V3N01`, `CAP08`).
**A tag é o contrato entre roteiro e código.** Para cada tag do roteiro existe
exatamente uma chamada no capítulo correspondente, na mesma ordem da tabela:

```python
with narra(cena, "C8N07", 8.3):        # est= sai da coluna "Est." do roteiro
    cena.play(GrowArrow(s1), Write(f1s))

so_fala(cena, "C8N15", 8.8)            # linha de narração sem animação embaixo
```

`narra()` dispara o `.wav` da tag, roda as animações do `with` e completa em
silêncio o que faltar para a locução acabar, mais o `PAD` de 0,35 s.

Regras que caem daí:

- **A animação tem que caber dentro da locução.** Se ela estourar, o áudio da
  linha seguinte entra por cima. O roteiro marca os poucos trechos em que a
  animação é propositalmente mais longa que a fala.
- **Nada de `cena.wait()` solto para dar respiro.** Quem dá o respiro é o `PAD`.
  `wait()` só é aceitável para segurar um quadro final antes de um `limpar()`.
- **`est=` é provisório.** Depois da gravação, `python medir.py pt` (ou `en`)
  regenera `shor/duracoes_<idioma>.py` com as durações reais e o `est=` vira
  só fallback. Não preencher `duracoes_pt.py`/`duracoes_en.py` na mão. O `est=`
  no código é sempre o do pt — em inglês quem manda é o DUR medido.
- **Cartões de capítulo** (`CAP06`, `CAP07`, …) não são chamados com a tag
  literal: `montagem.py` monta com f-string e lê a duração de `CARTOES`. Ao
  fechar um capítulo, adicionar/ajustar a entrada em `CARTOES` com o valor do
  roteiro.

---

## A coluna "Entra em" é a especificação

A quarta coluna de cada tabela diz exatamente quais `play` pertencem àquela
fala. Vocabulário usado ali:

- **"emendados"** = um único `cena.play(...)` com as animações dentro, não dois
  `play` em sequência. Isso é ritmo, não detalhe.
- **"num bloco só"** = idem, para três ou mais.
- **`A → B`** = `ReplacementTransform(A, B)`.
- **"nasce de dentro de X"** = a origem do mobject é X (`X.copy()` transformado),
  não um `Write` do vazio.
- **"Animação nova"** = não existe nada equivalente no arquivo hoje.

---

## Gramática visual da série

Regras herdadas do cabeçalho do `filme_shor.py`, que valem para todo código novo:

1. **Sem relógios.** Aritmética modular é sempre reta numérica segmentada
   (traços com folga entre os blocos). Se aparecer um mostrador circular em
   qualquer proposta, está errado.
2. **Fiel aos slides**, passo a passo.
3. **Cores só da `paleta.py`.** Nada de hex solto no meio do capítulo.
   `c` verde, `a` azul-marinho, `b` vermelho, `n` laranja, `x` amarelo,
   bits 1 azul-claro / 0 amarelo, `p` rosa, `q` verde-claro, `a` roxo no RSA.
4. **Originação:** o binário nasce do decimal, por cópias que se desdobram.
   Vale para tudo — peça nova quase sempre nasce de uma peça em cena.
5. **Mínimo de texto:** fórmulas coloridas que se transformam umas nas outras.
   Se a solução envolve escrever uma frase na tela, provavelmente está errada.

A `diretriz_fala_vs_animacao.md` explica a divisão de trabalho entre fala e
imagem. Ler antes de mexer em qualquer capítulo.

---

## Estado atual

| Capítulos | Situação |
|---|---|
| 1–5 | **Prontos e gravados. Não tocar.** |
| 6, 7, 8 | Código com `narra()`/`so_fala()` em toda linha; pendências pontuais de agrupamento de `play` no fim do `roteiro_video3_do_teorema_ao_rsa.md`. É o trabalho do vídeo 3. |
| 9, 9b, 10 | Código com `narra()` em toda linha, costura do vídeo 4 (`video4.py`) pronta. Prontos em código, aguardando gravação. `capitulo10.py` é o capítulo 11 em tela. |

As pendências dos capítulos 6, 7 e 8 estão listadas no fim do
`roteiro_video3_do_teorema_ao_rsa.md`. As do trabalho corrente (capítulos 9, 9b e 10,
vídeo 4) estão no fim de `roteiros/roteiro_video4_algoritmo_de_shor.md`.
Elas são a lista de tarefas.

---

## Como rodar

```bash
cd ~/Desktop/Algoritmos_quanticos/animação
source ../meu_ambiente_quantico/bin/activate

python conferir.py 8          # confere o capítulo 8 contra o roteiro
python conferir.py            # confere tudo (pt)

manim -pql filme_shor.py Parte8       # preview de um capítulo
manim -pql filme_shor.py VideoShor    # preview do vídeo 4 inteiro
manim -pqh filme_shor.py FilmeCompleto  # final 1080p60
```

Para preview sem as pausas de narração, `NARRA = False` em `ferramentas.py`
(lembrar de voltar para `True`).

---

## Idiomas

O projeto é bilíngue (pt/en) só na camada de dados — nenhuma cena, `play` ou
duração muda entre os dois. O idioma ativo vem da variável de ambiente
`IDIOMA` (`shor/idioma.py`), lida por `shor/ferramentas.py` para escolher
`audio/<idioma>/` e `shor/duracoes_<idioma>.py`. Sem a variável, o padrão é
`pt` — então nada muda para quem não mexe nela.

- **Escolher o idioma:**
  - bash: `IDIOMA=en manim -pql filme_shor.py Parte1`
  - PowerShell: `$env:IDIOMA="en"; manim -pql filme_shor.py Parte1`
- **Áudio:** `audio/pt/TAG.wav` e `audio/en/TAG.wav` (mesmo nome de tag nos
  dois; `audio/` inteiro é ignorado pelo git).
- **Durações:** `shor/duracoes_pt.py` e `shor/duracoes_en.py`, cada um gerado
  por `python medir.py pt` / `python medir.py en`.
- **Roteiros:** `roteiros/*.md` (pt) e `roteiros/en/*.md` (en), mesmos nomes
  de arquivo. **O roteiro em inglês tem exatamente as mesmas tags, na mesma
  ordem, do português — tradução não funde nem divide fala.**
- **Conferir:** `python conferir.py` confere só o pt (como sempre);
  `python conferir.py --en` confere `roteiros/en/` contra o código (mesmas
  tags, mesma ordem; a coluna Est. do inglês não é comparada ao `est=` do
  código, que é sempre o do pt).
- **Largura dos textos em inglês:** `python checar_textos.py` (sem renderizar)
  mede pt × en no tamanho de fonte real de cada chave e sai com código 1 se
  algum "en" passar de 90% do quadro — rodar antes de cada render em inglês.
- **Render separado por idioma** (para não sobrescrever o pt):
  ```bash
  manim -pql filme_shor.py Parte1                              # pt → media/
  IDIOMA=en manim -pql --media_dir media/en filme_shor.py Parte1  # en → media/en/
  ```

---

## Como trabalhar aqui

- **Um bloco por sessão.** Um capítulo, ou uma fase de um capítulo. Não abrir
  frente em dois capítulos ao mesmo tempo.
- **Terminar com `python conferir.py N` limpo** e com um `-pql` renderizado.
- **Não reformatar** código que não faz parte da tarefa. Nada de renomear
  variáveis, reordenar imports ou "limpar" capítulos prontos.
- **Não criar helper novo em `ferramentas.py`** sem dizer por quê; se a função
  serve a um capítulo só, ela mora no capítulo, com nome começando por `_`.
- **Mudou a duração de alguma fala?** Não mude. Duração é decisão de roteiro.
