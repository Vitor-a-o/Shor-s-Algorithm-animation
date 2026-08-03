# -*- coding: utf-8 -*-
"""
Paleta de cores e parâmetros globais do filme "Do Zero ao Algoritmo de Shor
Quântico" — tons extraídos dos slides (fundo branco):
    c verde, a azul-marinho, b vermelho, n laranja, x amarelo,
    bits 1 azul-claro / 0 amarelo, p rosa, q verde-claro, a roxo no RSA.
"""

VEL = 1.0

BRANCO   = "#ffffff"   # fundo (igual aos slides)
PRETO    = "#111318"   # texto/estrutura
CINZA    = "#8a96a8"   # apoio
AZUL     = "#2b26c8"   # a (azul-marinho dos slides)
VERMELHO = "#f03535"   # b / base da potência
LARANJA  = "#ff9a3d"   # n (o módulo)
VERDE    = "#00a457"   # c (o resto)
AMARELO  = "#e0a500"   # x / expoentes destacados / r
CIANO    = "#2596d1"   # bits "1" (azul-claro dos slides)
ROSA     = "#f050b0"   # p
VERDE2   = "#58b32e"   # q (verde-claro dos slides)
ROXO     = "#8c52ff"   # a no RSA / Euler
CAIXA    = "#e3e3e3"   # caixas cinzas dos diagramas (slides 27 e 34)
CAIXA2   = "#c9c9c9"   # caixa do bit 0 (cinza mais escuro dos slides)

COR_FUNDO, COR_TEXTO, COR_APAGADO = BRANCO, PRETO, CINZA
# aliases do capítulo 10
COR_PENTE, COR_FASOR, COR_SOMA, COR_RUIM, COR_PICO = VERDE, AZUL, LARANJA, VERMELHO, CIANO

# --- parâmetros do Shor quântico (n = 21, a = 2, medimos c = 4) ---
N, R, B0 = 512, 6, 2
PENTE = list(range(B0, N, R))
M = len(PENTE)
