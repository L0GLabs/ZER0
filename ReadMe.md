
<div align="center">

```
  ██████╗ ███████╗██████╗  ██████╗ 
  ╚════██╗██╔════╝██╔══██╗██╔═████╗
   █████╔╝█████╗  ██████╔╝██║██╔██║
  ██╔═══╝ ██╔══╝  ██╔══██╗████╔╝██║
  ███████╗███████╗██║  ██║╚██████╔╝
  ╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ 
```

**Gestor de alias de comandos para Arch Linux.**  
Escribe menos. Haz más.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python)
![Platform](https://img.shields.io/badge/Platform-Arch%20Linux-1793d1?style=flat-square&logo=arch-linux)
![Version](https://img.shields.io/badge/Version-1.0.0-red?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

</div>

---

## ¿Qué es ZER0?

ZER0 es una herramienta de línea de comandos que te permite guardar alias personalizados para tus comandos más usados. En lugar de escribir `sudo pacman -Syu` cada vez, simplemente defines `zer0 add upd "sudo pacman -Syu"` y desde ese momento ejecutas `zer0 upd`.

Al iniciar, ZER0 te pregunta tu nombre y lo recuerda en cada sesión. Cada vez que lo abras verás el banner con tu nombre y el branding de LogLabs.

---

## Instalación

### Requisitos

- Arch Linux
- Python 3.10 o superior
- `bash`, `zsh` o `fish`

### Pasos

```bash
# 1. Clona el repositorio
git clone https://github.com/L0GLabs/ZER0.git
cd ZER0

# 2. Dale permisos al instalador
chmod +x install.sh

# 3. Instala
./install.sh

# 4. Recarga tu shell
source ~/.bashrc   # bash
source ~/.zshrc    # zsh
```

El instalador se encarga de todo:

- Copia `zer0` y `zero` a `~/.local/bin/` (siempre en tu PATH)
- Agrega los alias `-Z` y `Z` a tu shell
- Configura `.bashrc`, `.zshrc` y `config.fish` automáticamente

---

## Uso

Una vez instalado, puedes invocar ZER0 de cualquiera de estas formas desde **cualquier carpeta**:

```bash
zer0
zero
Z
-Z
```

Todas abren la pantalla de bienvenida.

---

## Comandos

| Comando | Descripción |
|---|---|
| `zer0` / `zero` / `Z` / `-Z` | Pantalla de bienvenida |
| `zer0 list` | Listar todos los atajos guardados |
| `zer0 add <atajo> <comando>` | Agregar o actualizar un atajo |
| `zer0 rm <atajo>` | Eliminar un atajo |
| `zer0 <atajo> [args…]` | Ejecutar un atajo |
| `zer0 help` | Mostrar ayuda |
| `zer0 version` | Mostrar versión |

---

## Ejemplos

```bash
# Guardar atajos
zer0 add upd  "sudo pacman -Syu"
zer0 add cls  "clear"
zer0 add gs   "git status"
zer0 add gp   "git push origin main"
zer0 add py   "python3"

# Ejecutarlos
zer0 upd             # → sudo pacman -Syu
zer0 gs              # → git status
zer0 py script.py    # → python3 script.py  (pasa argumentos extra)

# Ver todos los atajos
zer0 list

# Eliminar uno
zer0 rm cls
```

---

## Configuración

ZER0 guarda todo en un archivo JSON en:

```
~/.config/zer0/config.json
```

Ejemplo del archivo:

```json
{
  "name": "Tu Nombre",
  "aliases": {
    "upd": "sudo pacman -Syu",
    "gs": "git status",
    "gp": "git push origin main"
  }
}
```

Puedes editarlo manualmente si lo prefieres.

---

## Estructura del proyecto

```
ZER0/
├── zer0.py       # Programa principal
├── install.sh    # Instalador
└── README.md     # Este archivo
```

---

## Desinstalar

```bash
rm ~/.local/bin/zer0
rm ~/.local/bin/zero
rm -rf ~/.config/zer0
```

Y elimina manualmente el bloque `# ─── ZER0 ───` de tu `.bashrc` / `.zshrc`.

---

## Desarrollado por

<div align="center">

**LogLabs**

[![GitHub](https://img.shields.io/badge/GitHub-L0GLabs-181717?style=flat-square&logo=github)](https://github.com/L0GLabs)
[![Repo](https://img.shields.io/badge/Repo-ZER0-red?style=flat-square&logo=github)](https://github.com/L0GLabs/ZER0)

</div>
