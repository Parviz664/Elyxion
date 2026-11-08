#!/usr/bin/env sh
set -eu
ROOT="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"
OUT="${TMPDIR:-/tmp}/elyxion_native_core_tests_$$"
mkdir -p "$OUT"
trap 'rm -rf "$OUT"' EXIT
SRC="$ROOT/app/src/main/java/com/elyxion/cosmos"
javac -encoding UTF-8 -d "$OUT" "$SRC/AxisMath.java" "$SRC/ProbeMath.java" "$SRC/InputBus.java" "$ROOT/qa/NativeCoreTest.java"
java -cp "$OUT" NativeCoreTest
