# MC-AutomaticPackage

Un programa que activa y desactiva automáticamente un paquete de recursos de Minecraft con una tecla. La idea general es que el programa modifique el archivo de configuración de Minecraft (options.txt) y controle la lista de resource packs activos.

## 📁 ¿Dónde están los archivos de configuración de Minecraft?

En Minecraft, los paquetes de recursos se activan desde el archivo `options.txt`, que se encuentra en:
- **Windows:** `C:\Users\[TuNombreDeUsuario]\AppData\Roaming\.minecraft\options.txt`
- **Linux:** `/home/[TuNombreDeUsuario]/.minecraft/options.txt`
- **MacOS:** `/Users/[TuNombreDeUsuario]/Library/Application Support/minecraft/options.txt`

Dentro de `options.txt`, hay una línea que se parece a esta:

```txt
resourcePacks:["vanilla","file/my_custom_pack"]
```

Donde `file/my_custom_pack` se refiere al nombre de tu paquete de recursos.

## ⚙️ Lógica del programa

1. **Leer `options.txt`:** Detectar la lista de paquetes de recursos activos.
2. **Activar o desactivar el paquete:** Añadir o eliminar tu paquete de la lista `resourcePacks`.
3. **Guardar el archivo:** Actualizar el archivo `options.txt`.
4. **Tecla de acceso rápido:** Usar una tecla global para activar/desactivar el paquete.

## 📝 Explicación del código

### Archivo de opciones:

El programa abre el archivo `options.txt`, busca la línea que contiene `resourcePacks` y lee los paquetes de recursos actuales.
- Si tu paquete (`file/my_custom_pack`) está en la lista, se elimina; de lo contrario, se añade.
- Guarda los cambios de vuelta en `options.txt`.

### Tecla de acceso rápido:

Se usa la librería `pynput` para escuchar combinaciones de teclas.
- La combinación predeterminada es `CTRL + SHIFT + R`, pero se puede cambiar.

### Control de errores:

El programa detecta errores (por ejemplo, si el archivo no se encuentra) e imprime mensajes de error.

## 🔄 Personalización

### Cambiar la tecla de acceso rápido:
Cambia la combinación de teclas editando esta parte:

```python
HOTKEY = {keyboard.Key.ctrl_l, keyboard.Key.shift, keyboard.KeyCode(char='r')}
```

Puedes usar teclas especiales de la librería `keyboard.Key` (por ejemplo, `Key.alt`, `Key.esc`, etc.).
Para usar letras o números, usa `keyboard.KeyCode(char='x')`, donde `x` es la tecla.

### Cambiar el nombre del paquete de recursos:
Cambia el nombre aquí:

```python
RESOURCE_PACK_NAME = 'file/my_custom_pack'
```

## 🚀 Cómo ejecutar
1. Asegúrate de que tu paquete de recursos esté en la carpeta `.minecraft/resourcepacks`.
2. Cambia `RESOURCE_PACK_NAME` por el nombre de tu paquete de recursos.
3. Ejecuta el script de Python.
4. Presiona `CTRL + SHIFT + R` para activar o desactivar el paquete de recursos.

## 🔐 Notas de seguridad
- Modificar `options.txt` no afecta la integridad del juego ni los servidores, pero realiza siempre una copia de seguridad antes de hacer cambios.
- El programa no accede a servidores externos, solo controla tu configuración local.

## Problemas comunes y soluciones
| Problema                              | Causa                                       | Solución                                               |
|---------------------------------------|---------------------------------------------|--------------------------------------------------------|
| No encuentra el archivo `options.txt` | Ruta incorrecta de `MINECRAFT_OPTIONS_PATH` | Verifica la ruta del archivo y corrígela.              |
| El script no detecta la combinación de teclas | Conflicto de teclado o permisos de teclado | Ejecuta el script con permisos de administrador.       |
| No actualiza el paquete de recursos   | El nombre del paquete es incorrecto         | Verifica el nombre de tu paquete de recursos.          |
| Error de lectura/escritura            | El archivo está en uso por Minecraft        | Cierra Minecraft antes de ejecutar el script.          |

## 🚀 Futuras mejoras
- **Interfaz gráfica (GUI)**: Usar `tkinter` para crear una interfaz que permita seleccionar los paquetes de recursos disponibles.
- **Soporte para múltiples paquetes**: Cambiar varios paquetes de recursos a la vez.
- **Detección automática de la carpeta de Minecraft**: Usar `os.path.expanduser('~/.minecraft')` para hacer la ruta compatible con Windows, Linux y MacOS.
