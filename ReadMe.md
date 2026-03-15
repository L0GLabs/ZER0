# ZER0

<div align="center">

```
  ██████╗ ███████╗██████╗  ██████╗ 
  ╚════██╗██╔════╝██╔══██╗██╔═████╗
   █████╔╝█████╗  ██████╔╝██║██╔██║
  ██╔═══╝ ██╔══╝  ██╔══██╗████╔╝██║
  ███████╗███████╗██║  ██║╚██████╔╝
  ╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ 
```

**Command alias manager for Arch Linux.**  
Type less. Do more.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python)
![Platform](https://img.shields.io/badge/Platform-Arch%20Linux-1793d1?style=flat-square&logo=arch-linux)
![Version](https://img.shields.io/badge/Version-1.0.0-red?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

</div>

---

## What is ZER0?

ZER0 is a command-line tool with an **interactive mode (REPL)**. When you open it, you enter your own shell-like session where you run your shortcuts directly — no need to type `zero` every time.

```
[corona@ZER0 ~]$ upd
[corona@ZER0 ~]$ list
[corona@ZER0 ~]$ add gs "git status"
[corona@ZER0 ~]$ exit
```

The first time you launch it, ZER0 will ask for your **name** and **preferred language** — and remember both forever.

---

## Installation

### Requirements

- Arch Linux
- Python 3.10+
- `bash`, `zsh` or `fish`

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/LogLabsHQ/ZER0.git
cd ZER0

# 2. Give the installer permission
chmod +x install.sh

# 3. Run it
./install.sh

# 4. Reload your shell
source ~/.bashrc   # bash
source ~/.zshrc    # zsh
```

The installer handles everything automatically:

- Embeds and writes `zero` to `~/.local/bin/` (always in your PATH)
- Adds the `-Z` alias to your shell
- Exports `Z=zero` so `$Z` works as an invocation
- Supports bash, zsh and fish
- Asks for your preferred language (Español / English) with arrow keys

---

## How to open ZER0

From anywhere in your terminal, type any of these:

```bash
zero
-Z
$Z
```

All three open ZER0's interactive mode.

---

## Interactive mode

Once open, ZER0 gives you its own prompt:

```
[youruser@ZER0 ~]$
```

Type commands **without any prefix**:

| Command | Description |
|---|---|
| `list` | List all saved shortcuts |
| `add <shortcut> <cmd>` | Add or update a shortcut |
| `rm <shortcut>` | Delete a shortcut |
| `<shortcut> [args…]` | Run a shortcut |
| `lang` | Change language |
| `help` | Show help |
| `version` | Show version |
| `exit` / `quit` | Exit ZER0 |

You can also exit with `Ctrl+C`.

---

## Examples

```bash
# Open ZER0
zero

# Inside the ZER0 prompt:
[corona@ZER0 ~]$ add upd "sudo pacman -Syu"
[corona@ZER0 ~]$ add gs  "git status"
[corona@ZER0 ~]$ add gp  "git push origin main"
[corona@ZER0 ~]$ add py  "python3"

# Run shortcuts
[corona@ZER0 ~]$ upd
[corona@ZER0 ~]$ gs
[corona@ZER0 ~]$ py script.py

# List all shortcuts
[corona@ZER0 ~]$ list

# Change language
[corona@ZER0 ~]$ lang

# Exit
[corona@ZER0 ~]$ exit
```

---

## Language support

ZER0 supports **Español** and **English**.

- Selected during installation using arrow keys `↑↓ + Enter`
- Can be changed at any time with the `lang` command inside ZER0
- Saved permanently in `~/.config/zer0/config.json`

---

## Configuration

ZER0 stores everything in:

```
~/.config/zer0/config.json
```

Example:

```json
{
  "name": "Corona",
  "lang": "en",
  "aliases": {
    "upd": "sudo pacman -Syu",
    "gs":  "git status",
    "gp":  "git push origin main"
  }
}
```

You can edit this file manually if you prefer.

---

## Project structure

```
ZER0/
├── install.sh    ← installer (includes the program)
├── README.md
└── LICENSE
```

---

## Updating ZER0

When a new version is released, update with 3 commands:

```bash
cd ~/ZER0
git pull
./install.sh
```

That's it. The installer overwrites the old `zero` binary with the new version automatically. Your shortcuts, name and language preference are kept — they live in `~/.config/zer0/config.json` and are never touched by the installer.

> **Note:** If you moved or deleted the cloned folder, just clone it again and run the installer:
> ```bash
> git clone https://github.com/LogLabsHQ/ZER0.git
> cd ZER0
> ./install.sh
> ```

---

## Uninstall

```bash
rm ~/.local/bin/zero
rm -rf ~/.config/zer0
```

Then remove the `# ─── ZER0 ───` block from your `.bashrc` / `.zshrc`.

---

## Developed by

<div align="center">

**LogLabs**

[![GitHub](https://img.shields.io/badge/GitHub-LogLabsHQ-181717?style=flat-square&logo=github)](https://github.com/LogLabsHQ)
[![Repo](https://img.shields.io/badge/Repo-ZER0-red?style=flat-square&logo=github)](https://github.com/LogLabsHQ/ZER0)

</div>

---

---

# ZER0 — Español

<div align="center">

**Gestor de alias de comandos para Arch Linux.**  
Escribe menos. Haz más.

</div>

---

## ¿Qué es ZER0?

ZER0 es una herramienta de línea de comandos con **modo interactivo (REPL)**. Al abrirlo entras a una sesión propia con prompt estilo terminal donde ejecutas tus alias directamente, sin escribir `zero` cada vez.

```
[corona@ZER0 ~]$ upd
[corona@ZER0 ~]$ list
[corona@ZER0 ~]$ add gs "git status"
[corona@ZER0 ~]$ exit
```

La primera vez que lo abras, ZER0 te preguntará tu **nombre** e **idioma preferido** — y los recordará siempre.

---

## Instalación

### Requisitos

- Arch Linux
- Python 3.10 o superior
- `bash`, `zsh` o `fish`

### Pasos

```bash
# 1. Clona el repositorio
git clone https://github.com/LogLabsHQ/ZER0.git
cd ZER0

# 2. Dale permisos al instalador
chmod +x install.sh

# 3. Instala
./install.sh

# 4. Recarga tu shell
source ~/.bashrc   # bash
source ~/.zshrc    # zsh
```

El instalador se encarga de todo automáticamente:

- Embebe y escribe `zero` en `~/.local/bin/` (siempre en tu PATH)
- Agrega el alias `-Z` a tu shell
- Exporta `Z=zero` para que `$Z` funcione como invocación
- Soporta bash, zsh y fish
- Pregunta tu idioma preferido (Español / English) con flechas

---

## Cómo abrir ZER0

Desde cualquier carpeta escribe cualquiera de estos:

```bash
zero
-Z
$Z
```

Los tres abren el modo interactivo de ZER0.

---

## Modo interactivo

Al abrir ZER0 entras a una sesión con tu propio prompt:

```
[tuusuario@ZER0 ~]$
```

Escribe los comandos **sin prefijo**:

| Comando | Descripción |
|---|---|
| `list` | Listar todos los atajos guardados |
| `add <atajo> <cmd>` | Agregar o actualizar un atajo |
| `rm <atajo>` | Eliminar un atajo |
| `<atajo> [args…]` | Ejecutar un atajo |
| `lang` | Cambiar idioma |
| `help` | Mostrar ayuda |
| `version` | Mostrar versión |
| `exit` / `quit` | Salir de ZER0 |

También puedes salir con `Ctrl+C`.

---

## Idiomas

ZER0 soporta **Español** e **English**.

- Se elige al instalar con flechas `↑↓ + Enter`
- Se puede cambiar en cualquier momento con el comando `lang` dentro de ZER0
- Se guarda permanentemente en `~/.config/zer0/config.json`

---

## Actualizar ZER0

Cuando salga una nueva versión, actualiza con 3 comandos:

```bash
cd ~/ZER0
git pull
./install.sh
```

Eso es todo. El instalador sobreescribe el binario `zero` con la nueva versión automáticamente. Tus atajos, nombre e idioma se conservan — viven en `~/.config/zer0/config.json` y el instalador nunca los toca.

> **Nota:** Si moviste o borraste la carpeta clonada, solo clónala de nuevo y corre el instalador:
> ```bash
> git clone https://github.com/LogLabsHQ/ZER0.git
> cd ZER0
> ./install.sh
> ```

---

## Desinstalar

```bash
rm ~/.local/bin/zero
rm -rf ~/.config/zer0
```

Y elimina el bloque `# ─── ZER0 ───` de tu `.bashrc` / `.zshrc`.

---

<div align="center">

**Desarrollado con ♥ por LogLabs**

[![GitHub](https://img.shields.io/badge/GitHub-LogLabsHQ-181717?style=flat-square&logo=github)](https://github.com/LogLabsHQ)
[![Repo](https://img.shields.io/badge/Repo-ZER0-red?style=flat-square&logo=github)](https://github.com/LogLabsHQ/ZER0)

</div>
