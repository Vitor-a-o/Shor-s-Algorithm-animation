# -*- coding: utf-8 -*-
"""Lê audio/*.wav e regenera shor/duracoes.py com as durações reais."""
import json, pathlib, subprocess

AUDIO = pathlib.Path("audio")
SAIDA = pathlib.Path("shor/duracoes.py")

d = {}
for f in sorted(AUDIO.glob("*.wav")):
    s = subprocess.run(
        ["ffprobe", "-v", "quiet", "-show_entries", "format=duration",
         "-of", "csv=p=0", str(f)],
        capture_output=True, text=True).stdout.strip()
    if s:
        d[f.stem] = round(float(s), 2)

SAIDA.write_text("# gerado por medir.py — não editar à mão\n"
                 "DUR = " + json.dumps(d, indent=4, ensure_ascii=False) + "\n",
                 encoding="utf-8")
print(f"{len(d)} locuções — {sum(d.values()):.1f} s de áudio")