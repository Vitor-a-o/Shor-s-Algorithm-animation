# -*- coding: utf-8 -*-
"""
============================================================================
 DO ZERO AO ALGORITMO DE SHOR QUÂNTICO — O FILME (versão "slides fiéis")
============================================================================
 Regras desta versão:
   1. SEM relógios: aritmética modular só com retas numéricas segmentadas
      (traços com folga entre os blocos, como nos slides).
   2. Passo a passo fiel aos slides: colchetes [(4+4)+(4+4)]+[4],
      árvores de bits com caixas cinzas, árvore dupla da fatoração.
   3. Paleta extraída dos slides (fundo branco): c verde, a azul-marinho,
      b vermelho, n laranja, x amarelo, bits 1 azul-claro / 0 amarelo,
      p rosa, q verde-claro, a roxo no RSA.
   4. Binário "nasce" do decimal (originação por cópias que se desdobram).
   5. Mínimo de texto: fórmulas coloridas que se transformam umas nas outras.

 ORGANIZAÇÃO DO CÓDIGO:
   Este arquivo é só o ponto de entrada para o Manim (mantém os comandos
   abaixo funcionando). O conteúdo do filme está no pacote shor/:
     shor/paleta.py           cores e parâmetros globais
     shor/ferramentas.py      funções auxiliares (T, formula, traco, ...)
     shor/capitulos/capituloN.py   um capítulo por arquivo
                                   (1 a 8, 9 = ordem modular,
                                    9b = fatoração, 10 = Shor quântico;
                                    total: 11 partes)
     shor/montagem.py         ordem dos capítulos, abertura e encerramento

 COMO RODAR:
   cd ~/Desktop/Algoritmos_quanticos/animação
   source ../meu_ambiente_quantico/bin/activate
   manim -pql filme_shor.py FilmeCompleto      # preview
   manim -pqh filme_shor.py FilmeCompleto      # final 1080p60
   manim -pql filme_shor.py Parte3             # um capítulo isolado
   manim -pql filme_shor.py VideoOperacoes     # vídeo 2 (preview)
   manim -pqh filme_shor.py VideoOperacoes     # vídeo 2 (final 1080p60)
============================================================================
"""

from manim import *

from shor.paleta import COR_FUNDO
from shor.ferramentas import limpar
from shor.montagem import TITULOS, PARTES, abertura, encerramento, abre_capitulo
from shor.videos import video2


class FilmeCompleto(Scene):
    def construct(self):
        self.camera.background_color = COR_FUNDO
        abertura(self)
        for i, fn in enumerate(PARTES, start=1):
            abre_capitulo(self, i)
            fn(self)
            limpar(self)
        encerramento(self)


class VideoOperacoes(Scene):
    """Vídeo 2 — Aritmética modular, as quatro operações (capítulos 1 a 5)."""
    def construct(self):
        self.camera.background_color = COR_FUNDO
        # a abertura já se emenda ao cartão do capítulo 1 (toca o CAP01),
        # então o capítulo 1 entra sem abre_capitulo
        video2.abertura(self)
        PARTES[0](self)
        limpar(self)
        for i in (2, 3, 4, 5):
            abre_capitulo(self, i)
            PARTES[i - 1](self)
            limpar(self)
        video2.encerramento(self)


def _construct_parte(cena, i):
    cena.camera.background_color = COR_FUNDO
    abre_capitulo(cena, i)
    PARTES[i - 1](cena)


class Parte1(Scene):
    def construct(self): _construct_parte(self, 1)

class Parte2(Scene):
    def construct(self): _construct_parte(self, 2)

class Parte3(Scene):
    def construct(self): _construct_parte(self, 3)

class Parte4(Scene):
    def construct(self): _construct_parte(self, 4)

class Parte5(Scene):
    def construct(self): _construct_parte(self, 5)

class Parte6(Scene):
    def construct(self): _construct_parte(self, 6)

class Parte7(Scene):
    def construct(self): _construct_parte(self, 7)

class Parte8(Scene):
    def construct(self): _construct_parte(self, 8)

class Parte9(Scene):
    def construct(self): _construct_parte(self, 9)

class Parte10(Scene):
    def construct(self): _construct_parte(self, 10)

class Parte11(Scene):
    def construct(self): _construct_parte(self, 11)
