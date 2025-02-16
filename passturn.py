import pyautogui
import time
from pynput.keyboard import Controller, Key

# Configuración
image_path = "pasarturno.PNG"  # Ruta de la imagen a detectar
detection_interval = 1  # Intervalo de tiempo entre cada búsqueda (en segundos)
keyboard = Controller()

def detect_and_press():
    while True:
        try:
            # Intentar localizar la imagen en pantalla
            location = pyautogui.locateOnScreen(image_path, confidence=0.7)

            if location:
                print("✅ Imagen detectada. Presionando F1...")
                keyboard.press(Key.f1)
                keyboard.release(Key.f1)
                time.sleep(2)  # Espera para evitar spam de F1
            else:
                print("❌ Imagen no detectada. Reintentando...")

        except Exception as e:
            print(f"⚠️ Error en la detección: {e}")

        time.sleep(detection_interval)

if __name__ == "__main__":
    print("🔍 Iniciando detección de imagen... (Presiona CTRL+C para detener)")
    detect_and_press()
