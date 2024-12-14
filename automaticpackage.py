import os
import re
from pynput import keyboard

# Ruta al archivo de configuración de Minecraft
MINECRAFT_OPTIONS_PATH = os.path.expanduser(r'~\AppData\Roaming\.minecraft\options.txt')
RESOURCE_PACK_NAME = 'file/my_custom_pack'  # Nombre de tu paquete de recursos

def toggle_resource_pack():
    """Activa o desactiva el paquete de recursos en options.txt"""
    try:
        # Leer el archivo options.txt
        with open(MINECRAFT_OPTIONS_PATH, 'r') as file:
            content = file.read()

        # Buscar la línea que contiene resourcePacks
        match = re.search(r'resourcePacks:\[(.*?)\]', content)
        
        if match:
            # Obtener la lista de paquetes de recursos actuales
            current_packs = match.group(1).split(',')

            if f'"{RESOURCE_PACK_NAME}"' in current_packs:
                print(f"Desactivando el paquete de recursos: {RESOURCE_PACK_NAME}")
                current_packs.remove(f'"{RESOURCE_PACK_NAME}"')
            else:
                print(f"Activando el paquete de recursos: {RESOURCE_PACK_NAME}")
                current_packs.append(f'"{RESOURCE_PACK_NAME}"')
            
            # Crear la nueva línea de resourcePacks
            new_resource_packs = f'resourcePacks:[{",".join(current_packs)}]'
            
            # Reemplazar la línea de resourcePacks en el contenido
            new_content = re.sub(r'resourcePacks:\[(.*?)\]', new_resource_packs, content)
            
            # Guardar los cambios en el archivo options.txt
            with open(MINECRAFT_OPTIONS_PATH, 'w') as file:
                file.write(new_content)
            
            print("El archivo options.txt se ha actualizado correctamente.")
        else:
            print("No se encontró la línea resourcePacks en options.txt.")
    except Exception as e:
        print(f"Error al actualizar options.txt: {e}")

def on_activate():
    """Acción cuando se presiona la tecla de acceso rápido"""
    print("Tecla presionada, cambiando el paquete de recursos...")
    toggle_resource_pack()

def for_canonical(f):
    """Convierte la tecla a un formato canónico"""
    return lambda k: f(l.canonical(k))

if __name__ == "__main__":
    # Define la tecla de acceso rápido (Ctrl + Shift + R)
    HOTKEY = {keyboard.Key.ctrl_l, keyboard.Key.shift, keyboard.KeyCode(char='r')}
    current_keys = set()

    def on_press(key):
        """Se activa al presionar una tecla"""
        current_keys.add(key)
        if all(k in current_keys for k in HOTKEY):
            on_activate()

    def on_release(key):
        """Se activa al soltar una tecla"""
        if key in current_keys:
            current_keys.remove(key)

    print("Presiona CTRL + SHIFT + R para cambiar el paquete de recursos.")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as l:
        l.join()
        
