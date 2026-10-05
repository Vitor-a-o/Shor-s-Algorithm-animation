# -*- coding: utf-8 -*-
"""Idioma ativo do filme. Todo o resto (áudio, durações, roteiros) importa
daqui — para mudar de idioma, mude a variável de ambiente IDIOMA."""
import os

IDIOMA = os.environ.get("IDIOMA", "pt")

if IDIOMA not in ("pt", "en"):
    raise ValueError(f'IDIOMA inválido: {IDIOMA!r} — use "pt" ou "en"')
