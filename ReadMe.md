# ZER0

Gestor de alias de comandos para Arch Linux. Escribe menos, haz más.

## Instalación

```bash
git clone <repo>
cd zer0
chmod +x install.sh
./install.sh
```

Reinicia tu terminal y ejecuta:

```bash
zer0
```

En la primera ejecución ZER0 te preguntará tu nombre y lo recordará siempre.

---

## Uso

| Comando                    | Acción                          |
|----------------------------|---------------------------------|
| `zer0`                     | Pantalla de bienvenida          |
| `zer0 list`                | Listar todos los atajos         |
| `zer0 add <atajo> <cmd>`   | Agregar o actualizar un atajo   |
| `zer0 rm  <atajo>`         | Eliminar un atajo               |
| `zer0 <atajo> [args…]`     | Ejecutar un atajo               |
| `zer0 help`                | Mostrar ayuda                   |
| `zer0 version`             | Mostrar versión                 |

### Ejemplos

```bash
# Agregar atajos
zer0 add upd  "sudo pacman -Syu"
zer0 add cls  "clear"
zer0 add gs   "git status"
zer0 add gp   "git push origin main"
zer0 add py   "python3"

# Ejecutarlos
zer0 upd            # → sudo pacman -Syu
zer0 gp             # → git push origin main
zer0 py script.py   # → python3 script.py  (pasa argumentos extra)

# Listar
zer0 list

# Eliminar
zer0 rm cls
```

---

## Configuración

El archivo de configuración se guarda en:

```
~/.config/zer0/config.json
```

Ejemplo:

```json
{
  "name": "Nombre",
  "aliases": {
    "upd": "sudo pacman -Syu",
    "gs": "git status",
    "gp": "git push origin main"
  }
}
```

---

## Invocaciones equivalentes

Todas estas formas abren la bienvenida:

```bash
zer0
zer0 open
zer0 start
zer0 -z
```

---

## Requisitos

- Python 3.10+
- Arch Linux (compatible con bash / zsh / fish)