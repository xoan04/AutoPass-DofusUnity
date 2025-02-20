import pyautogui
import time
from pynput.keyboard import Controller, Key

# Configuración
image_paths = ["listo.PNG", "pasarturno.PNG"]  # Lista de imágenes a detectar
detection_interval = 1  # Intervalo de tiempo entre cada búsqueda (en segundos)
keyboard = Controller()

def detect_and_press():
    while True:
        detected = False  # Bandera para saber si alguna imagen fue detectada

        for image_path in image_paths:
            try:
                # Intentar localizar la imagen
                location = pyautogui.locateOnScreen(image_path, confidence=0.7, grayscale=True)

                if location:
                    print(f"✅ Imagen detectada ({image_path}). Presionando F1...")
                    keyboard.press(Key.f1)
                    keyboard.release(Key.f1)
                    detected = True
                    time.sleep(1)  # Pequeño delay para evitar múltiples detecciones instantáneas

            except pyautogui.ImageNotFoundException:
                # Capturamos específicamente la excepción de imagen no encontrada (solo si usáramos locateCenterOnScreen)
                pass  # Si no encuentra la imagen, no hacemos nada y seguimos con la siguiente

            except Exception as e:
                print(f"⚠️ Error al detectar {image_path}: {e}")

        if not detected:
            print("❌ Ninguna imagen detectada. Reintentando...")

        time.sleep(detection_interval)  # Espera antes de volver a buscar

if __name__ == "__main__":
    print("🔍 Iniciando detección de imágenes... (Presiona CTRL+C para detener)")
    detect_and_press()
