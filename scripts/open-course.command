#!/usr/bin/env bash

# One-click launcher Android course:
# 1) rebuild HTML
# 2) open browser on localhost
# 3) keep local server running in this terminal

set -euo pipefail

export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:${PATH:-}"

SCRIPT_SOURCE="${BASH_SOURCE[0]}"
if [[ "${SCRIPT_SOURCE}" == */* ]]; then
  SCRIPT_DIR="$(cd "${SCRIPT_SOURCE%/*}" && pwd)"
else
  SCRIPT_DIR="$(pwd)"
fi

REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
HOST="127.0.0.1"
START_PORT="${1:-4183}"

cd "${REPO_ROOT}"

if ! command -v python3 >/dev/null 2>&1; then
  echo "Error: python3 no está disponible en PATH."
  exit 1
fi

python3 scripts/build-html.py

PORT="$(python3 - <<'PY' "${START_PORT}" "${HOST}"
import socket
import sys

start_port = int(sys.argv[1])
host = sys.argv[2]

port = start_port
while port < start_port + 200:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            s.bind((host, port))
            print(port)
            break
        except OSError:
            port += 1
else:
    raise SystemExit("No se encontró puerto libre")
PY
)"

URL="http://${HOST}:${PORT}/dist/curso-stack-my-architecture-android.html?v=$(date +%s)"

echo "Abriendo curso en: ${URL}"
open "${URL}" || true
echo "Servidor local activo en ${HOST}:${PORT}"
echo "Pulsa Ctrl+C para detener."

exec python3 -m http.server "${PORT}" --bind "${HOST}" --directory "${REPO_ROOT}"

