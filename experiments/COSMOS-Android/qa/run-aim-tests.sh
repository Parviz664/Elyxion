#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TMP="$(mktemp -d)";trap 'rm -rf "$TMP"' EXIT
javac -encoding UTF-8 -d "$TMP" "$ROOT/app/src/main/java/com/elyxion/cosmos/AimMath.java" "$ROOT/qa/AimMathTest.java"
java -cp "$TMP" AimMathTest
