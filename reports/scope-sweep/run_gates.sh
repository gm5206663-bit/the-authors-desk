#!/usr/bin/env bash
# Run every gate/check script in the account and record what it actually does.
# Exit codes are read AFTER redirecting to a file — never through a pipe.
set -u
cd /tmp/all || exit 1
OUT=/home/user/scope-sweep/gate_runs.txt
: > "$OUT"

PAIRS=(
  "soul-land-1-fire-dragon-lizard|tools/chapter_gate.py"
  "pokemon-adaptation|tools/style_gate.py"
  "supergirl-adrian-vale|tools/verify.py"
  "supergirl-adrian-vale|tools/verify_foundation.py"
  "the-universal-storyline-creation|tools/foundation_gate.py"
  "the-universal-storyline-creation|tools/validate.py"
  "mcu_eternal_fanfic|tools/mcu_verify.py"
  "stark_heir|tools/mcu_verify.py"
  "qian-xunji-adaptation|tools/mcu_verify.py"
  "soul-library|tools/sentinel.py"
  "soul-library|tools/lint_continuity.py"
  "storyos-site|framework/scripts/verify_stage.py"
  "soul-land-projects/reference/sl3_lin_hao/Soul_Land_3_Project|checks/verify_locks.py"
  "soul-land-projects/reference/sl3_lin_hao/Soul_Land_3_Project|checks/sync_audit.py"
  "soul-land-projects/reference/sl3_lin_hao/Soul_Land_3_Project|checks/voice_check.py"
  "soul-land-projects/reference/sl3_lin_hao/Soul_Land_3_Project|checks/presence_audit.py"
  "soul-land-universal-kit/Miraculous_Project|checks/sync_audit.py"
  "soul-land-universal-kit/Miraculous_Project|checks/verify_locks.py"
  "soul-land-universal-kit/Miraculous_Project|checks/voice_check.py"
  "soul-land-universal-kit/soul_land_2_new|checks/verify.py"
  "soul-land-universal-kit/soul_land_3_new|checks/verify.py"
  "soul-land-universal-kit/soul_land_devouring_dragon|tools/style_gate.py"
  "soul-land-universal-kit/soul_land_holy_spirit|tools/style_gate.py"
  "soul-land-universal-kit/Soul_Land_2_Project|tools/style_gate.py"
  "soul_land_4_fire_phoenix|tools/validate_all.py"
  "lan_shen|tools/style_gate.py"
  "lan_shen|tools/verify.py"
)

for pair in "${PAIRS[@]}"; do
  repo="${pair%%|*}"; path="${pair##*|}"
  printf '\n=== %s :: %s\n' "$repo" "$path" >> "$OUT"
  if [ ! -f "$repo/$path" ]; then
    echo "MISSING FILE" >> "$OUT"; continue
  fi
  before=$( cd "$repo" && git status --porcelain < /dev/null | wc -l )
  ( cd "$repo" && timeout 120 python3 "$path" > /tmp/_gate.out 2>&1 < /dev/null )
  code=$?
  after=$( cd "$repo" && git status --porcelain < /dev/null | wc -l )
  {
    echo "exit=$code  tree_changed=$((after>before))  lines=$(wc -l < /tmp/_gate.out)"
    tail -7 /tmp/_gate.out
  } >> "$OUT"
done
echo "done -> $OUT"
