#!/usr/bin/env python3
"""
ZER0 — Command alias manager for Arch Linux
"""

import os
import sys
import json
import subprocess
from pathlib import Path

# ─── Paths ────────────────────────────────────────────────────────────────────
CONFIG_DIR  = Path.home() / ".config" / "zer0"
CONFIG_FILE = CONFIG_DIR / "config.json"

# ─── ANSI Colors ──────────────────────────────────────────────────────────────
R   = "\033[38;5;196m"   # Red
O   = "\033[38;5;208m"   # Orange
Y   = "\033[38;5;226m"   # Yellow
C   = "\033[38;5;51m"    # Cyan
W   = "\033[97m"         # White
G   = "\033[38;5;46m"    # Green
DIM = "\033[2m"
B   = "\033[1m"
RST = "\033[0m"

# ─── Banner (estilo Claude Code) ──────────────────────────────────────────────
BANNER = f"""
{R}  ██████╗ ███████╗██████╗  ██████╗ {RST}
{O}  ╚════██╗██╔════╝██╔══██╗██╔═████╗{RST}
{Y}   █████╔╝█████╗  ██████╔╝██║██╔██║{RST}
{O}  ██╔═══╝ ██╔══╝  ██╔══██╗████╔╝██║{RST}
{R}  ███████╗███████╗██║  ██║╚██████╔╝{RST}
{DIM}  ╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ {RST}"""

VERSION = "1.0.0"
Create By: "LogLabs"
GitHub: "https://github.com/L0GLabs"

# ─── Config ───────────────────────────────────────────────────────────────────

def load_config() -> dict:
    if not CONFIG_FILE.exists():
        return {"name": None, "aliases": {}}
    try:
        with open(CONFIG_FILE) as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return {"name": None, "aliases": {}}

def save_config(config: dict) -> None:
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=2, ensure_ascii=False)

# ─── UI Helpers ───────────────────────────────────────────────────────────────

def box(lines: list[str], color: str = C) -> None:
    width = max(len(l) for l in lines) + 2
    print(f"{color}  ╭{'─' * width}╮{RST}")
    for line in lines:
        padding = width - len(line) - 1
        print(f"{color}  │{RST} {line}{' ' * padding}{color}│{RST}")
    print(f"{color}  ╰{'─' * width}╯{RST}")

def success(msg: str) -> None:
    print(f"\n  {G}✔{RST}  {msg}\n")

def error(msg: str) -> None:
    print(f"\n  {R}✘{RST}  {msg}\n")

def info(msg: str) -> None:
    print(f"  {DIM}{msg}{RST}")

# ─── First Run ────────────────────────────────────────────────────────────────

def first_run(config: dict) -> None:
    print(BANNER)
    print()
    box([
        "  Primera vez aquí. ¡Bienvenido!  ",
        f"  ZER0 v{VERSION} — Arch Linux          ",
    ])
    print()
    try:
        name = input(f"  {W}¿Cómo te llamas?{RST}  {DIM}›{RST} ").strip()
    except (KeyboardInterrupt, EOFError):
        print()
        sys.exit(0)

    if not name:
        name = "Usuario"

    config["name"] = name
    save_config(config)

    print()
    box([f"  Listo, {B}{name}{RST}. ZER0 ya es tuyo.  "], color=G)
    print()
    info("Tip: usa 'zer0 help' para ver todos los comandos.")
    print()

# ─── Welcome ──────────────────────────────────────────────────────────────────

def show_welcome(config: dict) -> None:
    print(BANNER)
    print()
    box([
        f"  Hola, {B}{config['name']}{RST}{C}.   ",
        f"  ZER0 v{VERSION} está en línea.  ",
    ])
    print()

# ─── Commands ─────────────────────────────────────────────────────────────────

def list_aliases(config: dict) -> None:
    aliases = config.get("aliases", {})
    if not aliases:
        info("No hay atajos guardados todavía.")
        print()
        info(f"Agrega uno con:  {W}zer0 add <atajo> <comando>{RST}")
        print()
        return

    print(f"  {B}{W}Atajos guardados:{RST}\n")
    max_k = max(len(k) for k in aliases)
    for key, val in sorted(aliases.items()):
        print(f"  {C}  {key:<{max_k}}{RST}  {DIM}→{RST}  {val}")
    print()

def add_alias(config: dict, alias: str, command: str) -> None:
    existed = alias in config["aliases"]
    config["aliases"][alias] = command
    save_config(config)
    verb = "actualizado" if existed else "guardado"
    success(f"Atajo {verb}:  {C}{alias}{RST}  {DIM}→{RST}  {command}")

def remove_alias(config: dict, alias: str) -> None:
    if alias not in config["aliases"]:
        error(f"El atajo '{alias}' no existe.")
        sys.exit(1)
    del config["aliases"][alias]
    save_config(config)
    success(f"Atajo eliminado:  {C}{alias}{RST}")

def run_alias(config: dict, alias: str, extra_args: list[str]) -> None:
    aliases = config.get("aliases", {})
    if alias not in aliases:
        error(f"Atajo '{alias}' no encontrado.")
        info(f"Usa 'zer0 list' para ver los disponibles.")
        print()
        sys.exit(1)
    cmd = aliases[alias]
    if extra_args:
        cmd += " " + " ".join(extra_args)
    sys.exit(subprocess.run(cmd, shell=True).returncode)

def show_help() -> None:
    print(f"\n  {B}{W}Uso:{RST}\n")
    cmds = [
        ("zer0",                    "Pantalla de bienvenida"),
        ("zer0 list",               "Listar todos los atajos"),
        ("zer0 add <atajo> <cmd>",  "Agregar o actualizar un atajo"),
        ("zer0 rm  <atajo>",        "Eliminar un atajo"),
        ("zer0 <atajo> [args…]",    "Ejecutar un atajo"),
        ("zer0 help",               "Mostrar esta ayuda"),
        ("zer0 version",            "Mostrar versión"),
    ]
    max_c = max(len(c) for c, _ in cmds)
    for cmd, desc in cmds:
        print(f"  {C}  {cmd:<{max_c}}{RST}   {DIM}{desc}{RST}")
    print()

def show_version() -> None:
    print(f"\n  ZER0  {DIM}v{VERSION}{RST}\n")

# ─── Entry Point ──────────────────────────────────────────────────────────────

def main() -> None:
    config = load_config()

    # Primera ejecución
    if config.get("name") is None:
        first_run(config)
        return

    args = sys.argv[1:]

    # Sin argumentos → bienvenida
    if not args or args[0].lower() in ("open", "start"):
        show_welcome(config)
        return

    cmd = args[0].lower()

    # Invocaciones equivalentes al modo bienvenida
    if cmd in ("-z", "--zero", "zero"):
        show_welcome(config)

    elif cmd in ("list", "ls", "-l"):
        show_welcome(config)
        list_aliases(config)

    elif cmd in ("add", "a"):
        if len(args) < 3:
            error("Uso:  zer0 add <atajo> <comando completo>")
            sys.exit(1)
        add_alias(config, args[1], " ".join(args[2:]))

    elif cmd in ("rm", "remove", "del", "delete"):
        if len(args) < 2:
            error("Uso:  zer0 rm <atajo>")
            sys.exit(1)
        remove_alias(config, args[1])

    elif cmd in ("help", "--help", "-h"):
        show_help()

    elif cmd in ("version", "--version", "-v"):
        show_version()

    else:
        # Intentar ejecutar como alias
        run_alias(config, cmd, args[1:])


if __name__ == "__main__":
    main()