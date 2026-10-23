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
   manim -pql filme_shor.py VideoIntro         # vídeo 1 (preview)
   manim -pqh filme_shor.py VideoIntro         # vídeo 1 (final 1080p60)
   manim -pql filme_shor.py VideoOperacoes     # vídeo 2 (preview)
   manim -pqh filme_shor.py VideoOperacoes     # vídeo 2 (final 1080p60)
   manim -pql filme_shor.py VideoTeoremaRSA    # vídeo 3 (preview)
   manim -pqh filme_shor.py VideoTeoremaRSA    # vídeo 3 (final 1080p60)
   manim -pql filme_shor.py VideoShor          # vídeo 4 (preview)
   manim -pqh filme_shor.py VideoShor          # vídeo 4 (final 1080p60)
   IDIOMA=en manim -pql filme_shor.py VideoIntro   # em inglês → VideoIntro_en.mp4
============================================================================
"""

from manim import *

from shor.paleta import COR_FUNDO
from shor.ferramentas import limpar
from shor.montagem import (TITULOS, PARTES, EMENDA, abertura, encerramento,
                           abre_capitulo)
from shor.videos import video1, video2, video3, video4
from shor.idioma import IDIOMA


# Em inglês, o Manim grava na mesma pasta do português, com "_en" no nome:
# VideoIntro_en.mp4 (e .wav, .png) ao lado de VideoIntro.mp4. Os pedaços
# em cache vão para partial_movie_files/<Scene>_en/, para um idioma não
# expulsar o cache do outro. Um -o explícito na linha de comando prevalece.
if IDIOMA != "pt":
    from pathlib import Path
    from manim.scene.scene_file_writer import SceneFileWriter
    from manim.utils.file_ops import guarantee_existence

    _init_dirs = SceneFileWriter.init_output_directories

    def _init_dirs_idioma(self, scene_name):
        _init_dirs(self, scene_name)
        if config["dry_run"] or self.output_name != Path(scene_name):
            return
        self.output_name = Path(f"{scene_name}_{IDIOMA}")
        for attr in ("image_file_path", "movie_file_path"):
            if hasattr(self, attr):
                p = getattr(self, attr)
                setattr(self, attr, p.with_name(self.output_name.name + p.suffix))
        if hasattr(self, "partial_movie_directory"):
            self.partial_movie_directory = guarantee_existence(
                self.partial_movie_directory.with_name(self.output_name.name))

    SceneFileWriter.init_output_directories = _init_dirs_idioma


class FilmeCompleto(Scene):
    def construct(self):
        self.camera.background_color = COR_FUNDO
        abertura(self)
        sai = None
        for i, fn in enumerate(PARTES, start=1):
            abre_capitulo(self, i, sai=sai)
            peca = fn(self)
            # o capítulo que se emenda entrega viva a peça que sai no play do
            # cartão seguinte; os outros fecham com o limpar() de sempre
            sai = peca if i in EMENDA else None
            if sai is None:
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


class VideoTeoremaRSA(Scene):
    """Vídeo 3 — Do teorema ao RSA (capítulos 6 a 8)."""
    def construct(self):
        self.camera.background_color = COR_FUNDO
        # a abertura já se emenda ao cartão do capítulo 6 (toca o CAP06),
        # então o capítulo 6 entra sem abre_capitulo
        video3.abertura(self)
        PARTES[5](self)
        limpar(self)
        abre_capitulo(self, 7)
        PARTES[6](self)
        limpar(self)
        abre_capitulo(self, 8)
        # parte8 devolve a tese: o encerramento a reaproveita sem limpar()
        # entre os dois (o cadeado do V3N01 pousa em cima dela)
        tese = PARTES[7](self)
        video3.encerramento(self, tese)


class VideoShor(Scene):
    """Vídeo 4 — O algoritmo de Shor (capítulos 9 a 11)."""
    def construct(self):
        self.camera.background_color = COR_FUNDO
        # a abertura já se emenda ao cartão do capítulo 9 (toca o CAP09),
        # então o capítulo 9 entra sem abre_capitulo
        video4.abertura(self)
        # parte9 devolve a caixa da definição: ela sai DENTRO do play em que o
        # cartão do capítulo 10 entra, sem limpar() entre os dois
        caixa9 = PARTES[8](self)
        abre_capitulo(self, 10, sai=caixa9)
        PARTES[9](self)
        limpar(self)
        abre_capitulo(self, 11)
        # parte10 devolve a moldura verde: o encerramento a reaproveita sem
        # limpar() entre os dois (o cadeado do V4N01 pousa em cima dela)
        caixa = PARTES[10](self)
        video4.encerramento(self, caixa)


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


class VideoIntro(Scene):
    """Vídeo 1 — Introdução (não há capítulos por trás: o vídeo inteiro
    mora em shor/videos/video1.py)."""
    def construct(self):
        self.camera.background_color = COR_FUNDO
        cad, bloco, duvidas, ficha = video1.abertura(self)
        interrogacoes, primos, chip, contador, anos, ficha = \
            video1.corpo_fatoracao(self, cad, bloco, duvidas, ficha)
        # rotulos (p·q, mod n, φ(n), e·d, fora de cena) voltam no V1N08; os
        # nomes da rede ficam em cena até lá
        malha, rotulos, nomes = video1.corpo_rsa(self, cad, ficha)
        # tempo: a linha do tempo do V1N06, que fica em cena para o V1N07;
        # ficha: as duas metades da ficha rachada, que o V1N08 recolhe
        cacos, tempo, ficha = video1.corpo_shor(
            self, cad, malha, ficha, interrogacoes, duvidas, primos, chip,
            contador, anos)
        titulo, trilha, marca = video1.corpo_serie(self, cacos, tempo, ficha,
                                                   rotulos)
        titulo, trilha = video1.corpo_previa2(self, titulo, trilha, marca)
        titulo, trilha = video1.corpo_previa3(self, titulo, trilha)
        titulo, trilha, moldura = video1.corpo_previa4(self, titulo, trilha)
        video1.encerramento(self, titulo, trilha, moldura)
