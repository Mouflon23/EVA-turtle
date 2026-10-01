#!/usr/bin/env python3
"""Enveloppe le fragment publié comme Artifact dans un document HTML autonome.

Le fichier source (../eva-turtle.html par défaut) ne contient ni doctype ni
<head> : la plateforme Artifact les fournit. GitHub Pages, lui, sert le fichier
brut — sans enveloppe, le navigateur passerait en mode quirks.
"""
import sys, pathlib

src = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "../eva-turtle.html")
out = pathlib.Path(sys.argv[2] if len(sys.argv) > 2 else "index.html")

frag = src.read_text(encoding="utf-8")

# le fragment porte déjà <title> et <meta viewport> : on les remonte dans <head>
head_tags, body = [], []
for line in frag.split("\n"):
    if line.startswith("<title>") or line.startswith('<meta name="viewport"'):
        head_tags.append(line)
    else:
        body.append(line)

FAVICON = (
    "data:image/svg+xml,"
    "%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E"
    "%3Ctext y='.9em' font-size='90'%3E%F0%9F%90%A2%3C/text%3E%3C/svg%3E"
)

out.write_text(
    "<!doctype html>\n<html lang=\"fr\">\n<head>\n"
    "<meta charset=\"utf-8\">\n"
    + "\n".join(head_tags) + "\n"
    "<meta name=\"description\" content=\"Entraîneur de réflexe pour la décision de turtle sur EVA : "
    "combinaisons de scores, oui/non, temps de réponse et justesse mesurés.\">\n"
    "<meta name=\"color-scheme\" content=\"dark\">\n"
    f"<link rel=\"icon\" href=\"{FAVICON}\">\n"
    "</head>\n<body>\n"
    + "\n".join(body).strip() + "\n"
    "</body>\n</html>\n",
    encoding="utf-8",
)
print(f"{out} écrit — {out.stat().st_size} octets")
