import os
import time
import pyautogui

# ⚙️ Rutas de archivos (ajústalas según tu sistema)
options_path = r'C:\Users\TuUsuario\AppData\Roaming\.minecraft\options.txt'
resourcepacks_path = r'C:\Users\TuUsuario\AppData\Roaming\.minecraft\resourcepacks'
pack_name = 'MiPaquete.zip'  # Nombre exacto del paquete de texturas
temp_pack_name = 'TempPack.zip'  # Nombre temporal para forzar la actualización

# 📝 1️⃣ Actualizar options.txt
print("[1/3] Actualizando options.txt...")

try:
    with open(options_path, 'r') as file:
        lines = file.readlines()

    for i in range(len(lines)):
        if 'resourcePacks:' in lines[i]:
            # Cambia el paquete de texturas que se quiere activar
            lines[i] = f'resourcePacks:["file/{pack_name}"]\n'
            print(f"🔄 Línea actualizada: {lines[i].strip()}")

    with open(options_path, 'w') as file:
        file.writelines(lines)

    print("✅ options.txt actualizado correctamente.")
except Exception as e:
    print(f"❌ Error al actualizar options.txt: {e}")


# 📁 2️⃣ Renombrar el paquete de texturas para forzar la detección
print("[2/3] Forzando la detección del paquete de texturas...")

try:
    pack_path = os.path.join(resourcepacks_path, pack_name)
    temp_pack_path = os.path.join(resourcepacks_path, temp_pack_name)
    
    # Renombrar el paquete de texturas temporalmente
    os.rename(pack_path, temp_pack_path)
    print(f"🔄 Paquete de texturas renombrado a {temp_pack_name}")
    
    # Esperar 2 segundos para permitir la detección de cambios
    time.sleep(2)
    
    # Renombrar el paquete de vuelta a su nombre original
    os.rename(temp_pack_path, pack_path)
    print(f"✅ Paquete de texturas renombrado de vuelta a {pack_name}")
except Exception as e:
    print(f"❌ Error al renombrar el paquete de texturas: {e}")


# 🕹️ 3️⃣ Simular F3 + T para recargar texturas
print("[3/3] Simulando la combinación de teclas F3 + T...")

try:
    # Espera 5 segundos para que puedas volver a Minecraft
    print("⏳ Tienes 5 segundos para volver a la ventana de Minecraft...")
    time.sleep(5)

    # Simula la combinación de teclas F3 + T
    pyautogui.hotkey('f3', 't')
    print("✅ Combinación de teclas F3 + T ejecutada correctamente.")
except Exception as e:
    print(f"❌ Error al simular la combinación de teclas: {e}")

print("🎉 ¡El proceso ha terminado!")
