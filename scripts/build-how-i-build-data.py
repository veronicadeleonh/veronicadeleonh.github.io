#!/usr/bin/env python3
"""Regenerate the snapshot static/data/how-i-build-commits.json for /how-i-build/.

The page reads commits live from the GitHub API; this snapshot is only the
fallback when GitHub is unreachable or rate-limited.

Reads the git history of the sibling project repos (../<repo>) and tags each
commit with a phase from its message. The tagging is a keyword heuristic, so
the page labels it as automatic.

    python3 scripts/build-how-i-build-data.py
"""
import json, re, subprocess, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent

import yaml  # pip install pyyaml

# project id -> folder next to this repo, from data/how_i_build.yaml
REPOS = {p["id"]: p["folder"] for p in yaml.safe_load((ROOT / "data" / "how_i_build.yaml").read_text())["projects"]}
# First match wins, so order matters.
RULES = [
    ("a11y", r"a11y|accessib|wcag|contrast|keyboard|focus|wave\b|axe\b|lighthouse|aria|reflow|screen reader|color blind|without colou?r|reduced.motion|teclado|foco|sr-only|landmark|skip link|zoom"),
    ("tokens", r"token|styleguide|design system|type scale|spacing scale|escala|radii"),
    ("data", r"data|dataset|pipeline|fetch|scraper|geocod|geograph|\bapi\b|louvre|\bmet\b|\bbm\b|quai|piezas|pbdb|fossil|volcanoes|eruption|csv|json|translat|traduc|layer [123]|investig|batch|ronda|research|wikidata|tavily|provenance|hallazgo"),
    ("docs", r"readme|seo|metadata|screenshot|image|\bog\b|analytics|docs|credits|cr[eé]dit"),
]

out = {}
for key, folder in REPOS.items():
    log = subprocess.run(
        ["git", "-C", str(ROOT.parent / folder), "log", "--reverse", "--format=%ad\t%s", "--date=short"],
        capture_output=True, text=True, check=True,
    ).stdout.strip().split("\n")
    rows = []
    for line in log:
        date, msg = line.split("\t", 1)
        phase = "ui"
        for name, pattern in RULES:
            if re.search(pattern, msg.lower()):
                phase = name
                break
        rows.append([date, phase, msg[:140]])
    out[key] = rows

dest = ROOT / "static" / "data" / "how-i-build-commits.json"
dest.write_text(json.dumps(out, ensure_ascii=False, separators=(",", ":")))
for k, v in out.items():
    print(k, len(v))
