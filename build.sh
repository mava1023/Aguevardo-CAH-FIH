#!/usr/bin/env bash
# Builds a standalone executable for this game using PyInstaller.
set -euo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")"

VENV_DIR=".venv-build"

if [ ! -d "$VENV_DIR" ]; then
    echo "Creating build virtualenv in $VENV_DIR..."
    python3 -m venv "$VENV_DIR"
    "$VENV_DIR/bin/pip" install --upgrade pip -q
fi

"$VENV_DIR/bin/pip" install -q pyinstaller pillow

args=(--name Aguevardo --onefile --console --noconfirm)
for f in *.png; do
    args+=(--add-data "${f}:.")
done

"$VENV_DIR/bin/pyinstaller" "${args[@]}" main.py

rm -rf build Aguevardo.spec

echo
echo "Build complete: dist/Aguevardo"
