#!/usr/bin/env bash
# ─────────────────────────────────────────────────────────────
#  ZER0 Installer — Arch Linux
# ─────────────────────────────────────────────────────────────

R="\033[38;5;196m"
G="\033[38;5;46m"
Y="\033[38;5;226m"
C="\033[38;5;51m"
W="\033[97m"
DIM="\033[2m"
B="\033[1m"
RST="\033[0m"

INSTALL_DIR="$HOME/.local/bin"
SCRIPT_NAME="zer0"
SOURCE="$(cd "$(dirname "$0")" && pwd)/zer0.py"

echo ""
echo -e "${C}  ╭──────────────────────────────────╮${RST}"
echo -e "${C}  │${RST}  ${B}Instalando ZER0...${RST}             ${C}│${RST}"
echo -e "${C}  ╰──────────────────────────────────╯${RST}"
echo ""

# ── 1. Verificar Python 3.10+ ─────────────────────────────────
if ! command -v python3 &>/dev/null; then
    echo -e "  ${R}✘${RST}  Python 3 no encontrado. Instálalo con: ${W}sudo pacman -S python${RST}\n"
    exit 1
fi

PY_VERSION=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
PY_MAJOR=$(python3 -c "import sys; print(sys.version_info.major)")
PY_MINOR=$(python3 -c "import sys; print(sys.version_info.minor)")

if [[ "$PY_MAJOR" -lt 3 || ("$PY_MAJOR" -eq 3 && "$PY_MINOR" -lt 10) ]]; then
    echo -e "  ${R}✘${RST}  Se requiere Python 3.10+. Versión actual: ${W}$PY_VERSION${RST}\n"
    exit 1
fi

echo -e "  ${G}✔${RST}  Python ${W}$PY_VERSION${RST} detectado"

# ── 2. Crear ~/.local/bin si no existe ────────────────────────
mkdir -p "$INSTALL_DIR"
echo -e "  ${G}✔${RST}  Directorio: ${DIM}$INSTALL_DIR${RST}"

# ── 3. Copiar el script ───────────────────────────────────────
cp "$SOURCE" "$INSTALL_DIR/$SCRIPT_NAME"
chmod +x "$INSTALL_DIR/$SCRIPT_NAME"
echo -e "  ${G}✔${RST}  Instalado en: ${DIM}$INSTALL_DIR/$SCRIPT_NAME${RST}"

# ── 4. Verificar PATH ─────────────────────────────────────────
PATH_UPDATED=false
SHELLS_UPDATED=()

add_to_shell() {
    local RC="$1"
    local LINE='export PATH="$HOME/.local/bin:$PATH"'
    if [[ -f "$RC" ]] && ! grep -q '\.local/bin' "$RC"; then
        echo "" >> "$RC"
        echo "# ZER0 — agregado por el instalador" >> "$RC"
        echo "$LINE" >> "$RC"
        SHELLS_UPDATED+=("$RC")
        PATH_UPDATED=true
    fi
}

if [[ ":$PATH:" != *":$HOME/.local/bin:"* ]]; then
    add_to_shell "$HOME/.bashrc"
    add_to_shell "$HOME/.zshrc"
    add_to_shell "$HOME/.config/fish/config.fish"
fi

if [[ "$PATH_UPDATED" == true ]]; then
    echo -e "  ${G}✔${RST}  PATH actualizado en:"
    for rc in "${SHELLS_UPDATED[@]}"; do
        echo -e "       ${DIM}$rc${RST}"
    done
else
    echo -e "  ${G}✔${RST}  ${DIM}~/.local/bin ya está en PATH${RST}"
fi

# ── 5. Listo ──────────────────────────────────────────────────
echo ""
echo -e "${G}  ╭──────────────────────────────────────╮${RST}"
echo -e "${G}  │${RST}  ${B}ZER0 instalado correctamente.${RST}       ${G}│${RST}"
echo -e "${G}  ╰──────────────────────────────────────╯${RST}"
echo ""

if [[ "$PATH_UPDATED" == true ]]; then
    echo -e "  ${Y}!${RST}  Reinicia tu terminal o ejecuta:"
    echo -e "     ${W}source ~/.bashrc${RST}  ${DIM}(o tu shell correspondiente)${RST}"
    echo ""
fi

echo -e "  Luego ejecuta:  ${C}zer0${RST}"
echo ""