# MC-AutomaticPackage (3Steps-Edition)

Un programa que activa y desactiva automáticamente un paquete de recursos de Minecraft con una tecla. La idea general es que el programa modifique el archivo de configuración de Minecraft (options.txt) y controle la lista de resource packs activos.

## 🔥 Script completo (3 pasos)

Este script realiza los siguientes pasos:
1️⃣ **Actualiza la línea** `resourcePacks:` en `options.txt` para activar el paquete de texturas.
2️⃣ **Renombra temporalmente el archivo de textura y lo restaura** para forzar a Minecraft a detectar el cambio.
3️⃣ **Simula la tecla F3 + T** para recargar los recursos sin cerrar Minecraft.

## 🔧 Explicación del script

### 1️⃣ Actualización de options.txt:

- Busca la línea que contiene `resourcePacks`: en `options.txt` y la cambia a:

```txt
resourcePacks:["file/MiPaquete.zip"]
```
Aquí debes asegurarte de que **MiPaquete.zip** sea el nombre exacto de tu paquete de texturas.
**Nota**: Asegúrate de que esta línea esté bien escrita, ya que Minecraft no cargará el paquete si hay errores de sintaxis.

### 2️⃣ Renombrado del paquete de texturas:

- Se renombra el archivo de `MiPaquete.zip` a `TempPack.zip` y luego se vuelve a su nombre original.
- Esto fuerza a Minecraft a "ver" un cambio en la carpeta de `resourcepacks`.
- El comando `os.rename` mueve o renombra un archivo de forma instantánea.

### 3️⃣ Simulación de la combinación de teclas F3 + T:

- Usa **pyautogui** para enviar la combinación de teclas `F3 + T`, lo que fuerza a Minecraft a recargar texturas.
- El script espera 5 segundos para que puedas volver a la ventana de Minecraft.
- **pyautogui** simula esta combinación de teclas, como si la presionaras manualmente.

## 📦 Requisitos de instalación

1. **Instalar Python** (si no lo tienes).
2. Instalar la biblioteca **pyautogui**:
```bash
pip install pyautogui
```
## 🧪 Pruebas y diagnóstico

1. **Error en `options.txt`**:

    - Asegúrate de que la línea resourcePacks: esté bien escrita.
    - Revisa que la ruta de options.txt sea correcta.
2. **Error al renombrar archivos**:

    - Asegúrate de que no esté abierto el paquete de texturas en ningún programa.
    - Revisa la ruta de la carpeta de resourcepacks.
3. **F3 + T no funciona**:

    - Asegúrate de que Minecraft esté en la ventana activa (puedes añadir más tiempo de espera).
    - Revisa si pyautogui está simulando la tecla correctamente.

## ⚠️ Personalización
- **Ruta de archivos**: Cambia las rutas para que se adapten a tu sistema operativo.
- **Tiempo de espera**: Ajusta los `time.sleep(5)` para dar más o menos tiempo antes de simular las teclas.
- **Nombre del paquete**: Cambia el nombre `MiPaquete.zip` por el nombre de tu paquete de texturas.

## 📋 Resumen
1. **Modifica `options.txt`** para activar el paquete.
2. **Renombra el paquete de texturas** para que Minecraft detecte cambios.
3. **Simula F3 + T** para recargar los recursos.

Con este script, no necesitarás reiniciar Minecraft cada vez que quieras actualizar el paquete de texturas. 🚀