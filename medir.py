# -*- coding: utf-8 -*-
"""Lê audio/<idioma>/*.wav e regenera shor/duracoes_<idioma>.py com as
durações reais.

Uso:
    python medir.py pt
    python medir.py en
"""
import json, pathlib, subprocess, sys

if len(sys.argv) != 2 or sys.argv[1] not in ("pt", "en"):
    print("uso: python medir.py pt|en")
    sys.exit(1)

IDIOMA = sys.argv[1]
AUDIO = pathlib.Path("audio") / IDIOMA
SAIDA = pathlib.Path(f"shor/duracoes_{IDIOMA}.py")

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
