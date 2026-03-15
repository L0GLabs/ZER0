#!/usr/bin/env bash
# ─────────────────────────────────────────────────────────────────────────────
#  ZER0 Installer — Arch Linux
#  Desarrollado por LogLabs — https://github.com/L0GLabs
# ─────────────────────────────────────────────────────────────────────────────

set -euo pipefail

R="\033[38;5;196m"
G="\033[38;5;46m"
Y="\033[38;5;226m"
C="\033[38;5;51m"
W="\033[97m"
DIM="\033[2m"
B="\033[1m"
RST="\033[0m"

INSTALL_DIR="$HOME/.local/bin"
SRC_DIR="$(cd "$(dirname "$0")" && pwd)"
SCRIPT_SRC="$SRC_DIR/zer0.py"

# ── Banner ────────────────────────────────────────────────────────────────────
echo ""
echo -e "${R}  ██████╗ ███████╗██████╗  ██████╗ ${RST}"
echo -e "${O-\033[38;5;208m}  ╚════██╗██╔════╝██╔══██╗██╔═████╗${RST}"
echo -e "${Y}   █████╔╝  ZER0   ██████╔╝██║██╔██║${RST}"
echo -e "${O-\033[38;5;208m}  ██╔═══╝ ██╔══╝  ██╔══██╗████╔╝██║${RST}"
echo -e "${R}  ███████╗███████╗██║  ██║╚██████╔╝${RST}"
echo ""
echo -e "${C}  ╭──────────────────────────────────────╮${RST}"
echo -e "${C}  │${RST}  ${B}Instalando ZER0 en tu sistema...${RST}   ${C}│${RST}"
echo -e "${C}  ╰──────────────────────────────────────╯${RST}"
echo ""

# ── 1. Verificar Python 3.10+ ─────────────────────────────────────────────────
if ! command -v python3 &>/dev/null; then
    echo -e "  ${R}✘${RST}  Python 3 no encontrado."
    echo -e "     Instálalo con: ${W}sudo pacman -S python${RST}\n"
    exit 1
fi

PY_VER=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
PY_MAJOR=$(python3 -c "import sys; print(sys.version_info.major)")
PY_MINOR=$(python3 -c "import sys; print(sys.version_info.minor)")

if [[ "$PY_MAJOR" -lt 3 || ( "$PY_MAJOR" -eq 3 && "$PY_MINOR" -lt 10 ) ]]; then
    echo -e "  ${R}✘${RST}  Se requiere Python 3.10+. Versión actual: ${W}$PY_VER${RST}\n"
    exit 1
fi
echo -e "  ${G}✔${RST}  Python ${W}$PY_VER${RST} detectado"

# ── 2. Crear ~/.local/bin ─────────────────────────────────────────────────────
mkdir -p "$INSTALL_DIR"
echo -e "  ${G}✔${RST}  Directorio: ${DIM}$INSTALL_DIR${RST}"

# ── 3. Instalar ejecutable: zero ──────────────────────────────────────────────
cp "$SCRIPT_SRC" "$INSTALL_DIR/zero"
chmod +x "$INSTALL_DIR/zero"
echo -e "  ${G}✔${RST}  Instalado: ${DIM}$INSTALL_DIR/zero${RST}"

# ── 4. Bloque ZER0 para bash / zsh ───────────────────────────────────────────
# 'zero'  → ejecutable real en PATH
# '-Z'    → alias de shell
# '$Z'    → export Z=zero, para que $Z expanda y ejecute 'zero'

ZER0_BLOCK='
# ─── ZER0 ────────────────────────────────────────────────
export PATH="$HOME/.local/bin:$PATH"
alias -- -Z="zero"
export Z="zero"
# ─────────────────────────────────────────────────────────'

inject_bash_zsh() {
    local RC="$1"
    [[ ! -f "$RC" ]] && return
    if grep -q '─── ZER0' "$RC" 2>/dev/null; then
        echo -e "  ${DIM}✓  $RC ya configurado${RST}"
        return
    fi
    echo "$ZER0_BLOCK" >> "$RC"
    echo -e "  ${G}✔${RST}  Configurado: ${DIM}$RC${RST}"
}

inject_fish() {
    local RC="$1"
    [[ ! -f "$RC" ]] && return
    if grep -q 'ZER0' "$RC" 2>/dev/null; then
        echo -e "  ${DIM}✓  $RC ya configurado${RST}"
        return
    fi
    {
        echo ""
        echo "# ─── ZER0 ────────────────────────────────────────────────"
        echo 'fish_add_path "$HOME/.local/bin"'
        echo 'alias -- -Z="zero"'
        echo 'set -x Z zero'
        echo "# ─────────────────────────────────────────────────────────"
    } >> "$RC"
    echo -e "  ${G}✔${RST}  Configurado: ${DIM}$RC${RST}"
}

[[ -f "$HOME/.bashrc" ]] && inject_bash_zsh "$HOME/.bashrc"
[[ -f "$HOME/.zshrc"  ]] && inject_bash_zsh "$HOME/.zshrc"
[[ -f "$HOME/.config/fish/config.fish" ]] && inject_fish "$HOME/.config/fish/config.fish"

# Si no existe ningún RC, crear .bashrc mínimo
if [[ ! -f "$HOME/.bashrc" && ! -f "$HOME/.zshrc" ]]; then
    echo "$ZER0_BLOCK" >> "$HOME/.bashrc"
    echo -e "  ${G}✔${RST}  Creado ~/.bashrc con configuración de ZER0"
fi

# Aplicar PATH en sesión actual
export PATH="$HOME/.local/bin:$PATH"

# ── 5. Verificar acceso ───────────────────────────────────────────────────────
echo ""
if command -v zero &>/dev/null; then
    echo -e "  ${G}✔${RST}  ${B}zero${RST} accesible desde el PATH"
else
    echo -e "  ${Y}!${RST}  Recarga tu shell para activar los comandos"
fi

# ── 6. Listo ──────────────────────────────────────────────────────────────────
echo ""
echo -e "${G}  ╭────────────────────────────────────────────────╮${RST}"
echo -e "${G}  │${RST}  ${B}ZER0 instalado correctamente.  ✓${RST}            ${G}│${RST}"
echo -e "${G}  │${RST}                                              ${G}│${RST}"
echo -e "${G}  │${RST}  Para abrir ZER0 escribe cualquiera de:      ${G}│${RST}"
echo -e "${G}  │${RST}                                              ${G}│${RST}"
echo -e "${G}  │${RST}    ${C}zero${RST}    ${C}-Z${RST}    ${C}\$Z${RST}                         ${G}│${RST}"
echo -e "${G}  │${RST}                                              ${G}│${RST}"
echo -e "${G}  ╰────────────────────────────────────────────────╯${RST}"
echo ""
echo -e "  ${DIM}Reinicia tu terminal o ejecuta:${RST}"
echo -e "    ${W}source ~/.bashrc${RST}  ${DIM}(bash)${RST}"
echo -e "    ${W}source ~/.zshrc${RST}   ${DIM}(zsh)${RST}"
echo ""
echo -e "  ${DIM}Desarrollado por: ${W}LogLabs${RST}"
echo -e "  ${DIM}Repo: ${C}https://github.com/L0GLabs/ZER0${RST}"
echo ""