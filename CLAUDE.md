# Do Zero ao Algoritmo de Shor Quântico — manual do repositório

Série de vídeos em Manim sobre aritmética modular, RSA e o algoritmo de Shor.
Cada vídeo tem um roteiro em markdown; o código do filme está no pacote `shor/`.

---

## Estrutura

```
filme_shor.py              ponto de entrada do Manim (FilmeCompleto, Parte1…Parte11)
medir.py                   lê audio/*.wav e REGENERA shor/duracoes.py
conferir.py                confere roteiro × código (rodar sempre ao terminar)
audio/                     TAG.wav, uma locução por arquivo (namespace global)
media/                     saída do Manim — nunca editar, nunca versionar
roteiros/                  os roteiros e a diretriz — a especificação do que animar
shor/
  paleta.py                cores e parâmetros globais (VEL, COR_TEXTO, …)
  ferramentas.py           T, formula, MOD, traco, limpar, narra, so_fala, PAD
  duracoes.py              GERADO pelo medir.py — nunca editar à mão
  montagem.py              ordem dos capítulos, TITULOS, CARTOES, abertura do filme
  cadeado.py               o cadeado da série
  capitulos/capituloN.py   um capítulo por arquivo (1–8, 9, 9b, 10)
  videos/videoN.py         abertura e encerramento próprios de cada vídeo da série
```

Imports dentro de `shor/capitulos/` e `shor/videos/`: `from ..paleta import *`
e `from ..ferramentas import *`. Dentro de `shor/`: `from .paleta import …`.

**Dois níveis de montagem.** `montagem.py` monta o filme inteiro (`FilmeCompleto`);
`shor/videos/videoN.py` monta um vídeo da série, com abertura e encerramento
próprios, reaproveitando os mesmos capítulos. O vídeo 2 (`video2.py`, cena
`VideoOperacoes`) é o modelo a seguir para o vídeo 3.

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
- **`est=` é provisório.** Depois da gravação, `python medir.py` regenera
  `shor/duracoes.py` com as durações reais e o `est=` vira só fallback. Não
  preencher `duracoes.py` na mão.
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

Quando o roteiro e o código divergirem, **o roteiro manda**. Se algo no roteiro
for impossível ou inconsistente, **relate — não conserte por conta própria, e
nunca reescreva uma fala.**

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
| 6, 7, 8 | Código existe, ainda sem `narra()`. É o trabalho do vídeo 3. |
| 9, 9b, 10 | Vídeos futuros. **Não tocar.** |

As pendências por capítulo estão listadas no fim do
`roteiro_video3_do_teorema_ao_rsa.md`. Elas são a lista de tarefas.

---

## Como rodar

```bash
cd ~/Desktop/Algoritmos_quanticos/animação
source ../meu_ambiente_quantico/bin/activate

python conferir.py 8          # confere o capítulo 8 contra o roteiro
python conferir.py            # confere tudo

manim -pql filme_shor.py Parte8       # preview de um capítulo
manim -pqh filme_shor.py FilmeCompleto  # final 1080p60
```

Para preview sem as pausas de narração, `NARRA = False` em `ferramentas.py`
(lembrar de voltar para `True`).

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
