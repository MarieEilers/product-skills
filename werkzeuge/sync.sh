#!/usr/bin/env bash
# Holt einen Skill aus dem privaten Marketplace und macht ihn öffentlich tauglich.
#
#   werkzeuge/sync.sh <pfad-zum-privaten-marketplace> <tabu-datei>
#
# 1. kopiert plugins/coaching-suite/skills/product-coach aus der privaten Quelle
#    nach plugins/product-coach (die private Quelle bleibt die einzige Quelle),
# 2. ersetzt in den Vorlagen jeden Abschnitt ab „## Beispiel“ durch die
#    erfundenen Beispiele aus beispiele/product-coach/,
# 3. bricht ab, wenn danach ein Begriff aus der Tabu-Datei vorkommt.
#    Die Tabu-Datei liegt bewusst nicht in diesem Repo.

set -euo pipefail

QUELLE="${1:?Pfad zum privaten Marketplace angeben}"
TABU="${2:?Pfad zur Tabu-Datei angeben}"
HIER="$(cd "$(dirname "$0")/.." && pwd)"
ZIEL="$HIER/plugins/product-coach"

mkdir -p "$ZIEL"
rsync -a --delete "$QUELLE/plugins/coaching-suite/skills/product-coach/" "$ZIEL/"

python3 - "$ZIEL/templates" "$HIER/beispiele/product-coach" <<'PY'
import sys, pathlib
vorlagen, beispiele = map(pathlib.Path, sys.argv[1:])
for beispiel in sorted(beispiele.glob("*.md")):
    ziel = vorlagen / beispiel.name
    text = ziel.read_text(encoding="utf-8")
    marke = "\n## Beispiel"
    if marke not in text:
        sys.exit(f"Kein Abschnitt „## Beispiel“ in {ziel.name} — Quelle hat sich geändert, bitte prüfen.")
    kopf = text[: text.index(marke)].rstrip() + "\n\n"
    ziel.write_text(kopf + beispiel.read_text(encoding="utf-8"), encoding="utf-8")
    print(f"Beispiel ersetzt: {ziel.name}")
PY

treffer=0
while IFS= read -r begriff; do
  [[ -z "$begriff" || "$begriff" == \#* ]] && continue
  if grep -rniF -- "$begriff" "$ZIEL" >/dev/null; then
    echo "Tabu-Begriff gefunden: $begriff" >&2
    grep -rniF -- "$begriff" "$ZIEL" >&2 || true
    treffer=1
  fi
done < "$TABU"

if [[ $treffer -ne 0 ]]; then
  echo "Abbruch: nichts committen, erst die Fundstellen klären." >&2
  exit 1
fi
echo "ok — plugins/product-coach ist aktuell und frei von Tabu-Begriffen."
