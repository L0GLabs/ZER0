#!/usr/bin/env python3
"""
ZER0 — Command alias manager for Arch Linux
Desarrollado por LogLabs — https://github.com/L0GLabs
"""

import os
import sys
import json
import re
import subprocess
from pathlib import Path

# ─── Paths ────────────────────────────────────────────────────────────────────
CONFIG_DIR  = Path.home() / ".config" / "zer0"
CONFIG_FILE = CONFIG_DIR / "config.json"

# ─── ANSI Colors ──────────────────────────────────────────────────────────────
R   = "\033[38;5;196m"
O   = "\033[38;5;208m"
Y   = "\033[38;5;226m"
C   = "\033[38;5;51m"
W   = "\033[97m"
G   = "\033[38;5;46m"
DIM = "\033[2m"
B   = "\033[1m"
RST = "\033[0m"

# ─── Meta ─────────────────────────────────────────────────────────────────────
VERSION = "1.0.0"
AUTHOR  = "LogLabs"
GITHUB  = "https://github.com/L0GLabs"
REPO    = "https://github.com/L0GLabs/ZER0"

# ─── Banner ───────────────────────────────────────────────────────────────────
BANNER = f"""
{R}  ██████╗ ███████╗██████╗  ██████╗ {RST}
{O}  ╚════██╗██╔════╝██╔══██╗██╔═████╗{RST}
{Y}   █████╔╝█████╗  ██████╔╝██║██╔██║{RST}
{O}  ██╔═══╝ ██╔══╝  ██╔══██╗████╔╝██║{RST}
{R}  ███████╗███████╗██║  ██║╚██████╔╝{RST}
{DIM}  ╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ {RST}"""

_ANSI = re.compile(r"\033\[[0-9;]*m")

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

def _raw_len(s: str) -> int:
    return len(_ANSI.sub("", s))

def box(lines: list, color: str = C) -> None:
    width = max(_raw_len(l) for l in lines) + 2
    print(f"{color}  ╭{'─' * width}╮{RST}")
    for line in lines:
        pad = width - _raw_len(line) - 1
        print(f"{color}  │{RST} {line}{' ' * pad}{color}│{RST}")
    print(f"{color}  ╰{'─' * width}╯{RST}")

def success(msg: str) -> None:
    print(f"\n  {G}✔{RST}  {msg}\n")

def error(msg: str) -> None:
    print(f"\n  {R}✘{RST}  {msg}\n")

def info(msg: str) -> None:
    print(f"  {DIM}{msg}{RST}")

def print_branding() -> None:
    print(f"  {DIM}Desarrollado por: {W}{AUTHOR}{RST}")
    print(f"  {DIM}GitHub  › {C}{GITHUB}{RST}")
    print(f"  {DIM}Repo    › {C}{REPO}{RST}")
    print()

def get_prompt() -> str:
    """Genera el prompt estilo [user@ZER0 dir]$"""
    user    = os.environ.get("USER", os.environ.get("LOGNAME", "user"))
    cwd     = Path.cwd()
    home    = Path.home()
    try:
        rel = "~" + str(cwd.relative_to(home)) if cwd != home else "~"
        rel = rel.replace("/", "/")
    except ValueError:
        rel = str(cwd)

    # Colores del prompt
    bracket = G
    at_sign = W
    zer0    = C
    path    = Y
    dollar  = W

    return (
        f"{bracket}[{RST}"
        f"{W}{user}{RST}"
        f"{bracket}@{RST}"
        f"{C}ZER0{RST}"
        f"{bracket} {RST}"
        f"{Y}{rel}{RST}"
        f"{bracket}]{RST}"
        f"{dollar}$ {RST}"
    )

# ─── First Run ────────────────────────────────────────────────────────────────

def first_run(config: dict) -> None:
    print(BANNER)
    print()
    box([
        "  Primera vez aquí. ¡Bienvenido!  ",
        f"  ZER0 v{VERSION} — Arch Linux         ",
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
    box([f"  Listo, {B}{name}{RST}{G}. ZER0 ya es tuyo.  "], color=G)
    print()
    info(f"Tip: escribe  {W}help{RST}{DIM}  dentro de ZER0 para ver los comandos.")
    print()
    print_branding()

# ─── Welcome ──────────────────────────────────────────────────────────────────

def show_welcome(config: dict) -> None:
    print(BANNER)
    print()
    box([
        f"  Hola, {B}{config['name']}{RST}{C}.             ",
        f"  ZER0 v{VERSION} está en línea.       ",
    ])
    print()
    print_branding()

# ─── Inner Commands (sin prefijo) ─────────────────────────────────────────────

def list_aliases(config: dict) -> None:
    aliases = config.get("aliases", {})
    if not aliases:
        info("No hay atajos guardados todavía.")
        print()
        info(f"Agrega uno con:  {W}add <atajo> <comando>{RST}")
        print()
        return
    print(f"\n  {B}{W}Atajos guardados:{RST}\n")
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
        return
    del config["aliases"][alias]
    save_config(config)
    success(f"Atajo eliminado:  {C}{alias}{RST}")

def run_alias(config: dict, alias: str, extra_args: list) -> None:
    aliases = config.get("aliases", {})
    if alias not in aliases:
        error(f"Comando o atajo '{alias}' no encontrado.")
        info(f"Escribe  {W}list{RST}{DIM}  para ver los atajos disponibles.")
        print()
        return
    cmd = aliases[alias]
    if extra_args:
        cmd += " " + " ".join(extra_args)
    subprocess.run(cmd, shell=True)

def show_help() -> None:
    print(f"\n  {B}{W}Comandos disponibles:{RST}\n")
    cmds = [
        ("list",                 "Listar todos los atajos"),
        ("add <atajo> <cmd>",    "Agregar o actualizar un atajo"),
        ("rm  <atajo>",          "Eliminar un atajo"),
        ("<atajo> [args…]",      "Ejecutar un atajo"),
        ("help",                 "Mostrar esta ayuda"),
        ("version",              "Mostrar versión"),
        ("exit / quit",          "Salir de ZER0"),
    ]
    max_c = max(len(c) for c, _ in cmds)
    for cmd, desc in cmds:
        print(f"  {C}  {cmd:<{max_c}}{RST}   {DIM}{desc}{RST}")
    print()

def show_version() -> None:
    print(f"\n  {B}ZER0{RST}  {DIM}v{VERSION}{RST}\n")
    print_branding()

# ─── REPL ─────────────────────────────────────────────────────────────────────

def repl(config: dict) -> None:
    """Modo interactivo: prompt estilo [user@ZER0 ~]$"""
    show_welcome(config)
    print(f"  {DIM}Escribe  {W}help{RST}{DIM}  para ver los comandos.  {W}exit{RST}{DIM}  para salir.{RST}\n")

    while True:
        try:
            prompt = get_prompt()
            line = input(prompt).strip()
        except (KeyboardInterrupt, EOFError):
            print(f"\n\n  {DIM}Hasta luego, {config['name']}. 👋{RST}\n")
            break

        if not line:
            continue

        parts = line.split()
        cmd   = parts[0].lower()
        args  = parts[1:]

        if cmd in ("exit", "quit", "q"):
            print(f"\n  {DIM}Hasta luego, {config['name']}. 👋{RST}\n")
            break

        elif cmd in ("list", "ls", "-l"):
            list_aliases(config)

        elif cmd in ("add", "a"):
            if len(args) < 2:
                error("Uso:  add <atajo> <comando completo>")
            else:
                add_alias(config, args[0], " ".join(args[1:]))

        elif cmd in ("rm", "remove", "del", "delete"):
            if not args:
                error("Uso:  rm <atajo>")
            else:
                remove_alias(config, args[0])

        elif cmd in ("help", "--help", "-h"):
            show_help()

        elif cmd in ("version", "--version", "-v"):
            show_version()

        else:
            run_alias(config, cmd, args)

# ─── Entry Point ──────────────────────────────────────────────────────────────

def main() -> None:
    config = load_config()

    if config.get("name") is None:
        first_run(config)
        # Después del first run, entrar al REPL directamente
        config = load_config()

    # ZER0 siempre abre el REPL interactivo
    repl(config)


if __name__ == "__main__":
    main()