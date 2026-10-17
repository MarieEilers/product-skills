#!/usr/bin/env bash
# Packt jeden Skill aus plugins/ als ZIP nach dist/ – zum Hochladen in die Claude-App.
#
#   werkzeuge/pakete.sh
#
# Aufbau je ZIP: ein Ordner mit dem Skill-Namen, darin SKILL.md und die Vorlagen.
# Die ZIPs hängen an den GitHub-Releases, nicht im Repo.

set -euo pipefail

HIER="$(cd "$(dirname "$0")/.." && pwd)"
mkdir -p "$HIER/dist"
cd "$HIER/plugins"

for skill in */; do
  skill="${skill%/}"
  [[ -f "$skill/SKILL.md" ]] || continue
  rm -f "$HIER/dist/$skill.zip"
  zip -qr -X "$HIER/dist/$skill.zip" "$skill" -x '*.DS_Store'
  echo "gepackt: dist/$skill.zip"
done
