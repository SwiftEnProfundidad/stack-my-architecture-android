#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

echo "╔══════════════════════════════════════════╗"
echo "║   FieldOps — Quality Gates (local)       ║"
echo "╚══════════════════════════════════════════╝"
echo ""

echo "=== Gate 1: assembleDebug ==="
./gradlew :app:assembleDebug --no-daemon
echo "✅ Gate 1 passed: assembleDebug"
echo ""

echo "=== Gate 2: Unit Tests ==="
./gradlew testDebugUnitTest --no-daemon
echo "✅ Gate 2 passed: testDebugUnitTest"
echo ""

echo "=== Gate 3: Lint ==="
./gradlew lintDebug --no-daemon
echo "✅ Gate 3 passed: lintDebug"
echo ""

echo "=== Gate 4: Instrumented Tests (si emulador disponible) ==="
if command -v adb &>/dev/null && adb devices 2>/dev/null | grep -q "device$"; then
    ./gradlew connectedDebugAndroidTest --no-daemon
    echo "✅ Gate 4 passed: connectedDebugAndroidTest"
else
    echo "⚠️  No emulador detectado — skipping instrumented tests"
    echo "    Ejecuta manualmente: ./gradlew connectedDebugAndroidTest"
fi
echo ""

echo "╔══════════════════════════════════════════╗"
echo "║   All quality gates passed ✅             ║"
echo "╚══════════════════════════════════════════╝"
