# 🖼️ Detección de Imagen y Pulsación de Tecla en Python

Este script detecta una imagen en la pantalla y, cuando la encuentra, presiona la tecla `F1` automáticamente. Se ejecuta en un bucle infinito, revisando periódicamente si la imagen está presente.

## 📌 Requisitos
Antes de ejecutar el script, asegúrate de tener instaladas las siguientes dependencias:

```bash
pip install pyautogui pynput opencv-python-headless
```

## 🚀 Uso
1. **Guarda la imagen** que deseas detectar en la misma carpeta del script y nómbrala como `pasarturno.PNG`. Puedes cambiar el nombre en la configuración del script.
2. **Ejecuta el script** con Python:

   ```bash
   python script.py
   ```

3. **El script buscará la imagen en la pantalla** y presionará `F1` cada vez que la detecte.
4. **Para detener el script**, presiona `CTRL + C` en la terminal.

## ⚙️ Configuración
Puedes modificar estos parámetros en el código:

- `image_path = "pasarturno.PNG"` → Cambia esto si el nombre de la imagen es diferente.
- `detection_interval = 1` → Intervalo en segundos entre cada intento de detección.
- `confidence = 0.7` → Nivel de confianza para la detección de imagen (ajusta entre `0.6` y `0.8` si no detecta bien).
- `time.sleep(2)` → Tiempo de espera después de presionar `F1` para evitar múltiples pulsaciones.

## 🛠 Código
```python
import pyautogui
import time
from pynput.keyboard import Controller, Key

# Configuración
image_path = "pasarturno.PNG"  # Ruta de la imagen a detectar
detection_interval = 1  # Intervalo de tiempo entre detecciones
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
                time.sleep(2)  # Espera para evitar pulsaciones repetidas
            else:
                print("❌ Imagen no detectada. Reintentando...")

        except Exception as e:
            print(f"⚠️ Error en la detección: {e}")

        time.sleep(detection_interval)

if __name__ == "__main__":
    print("🔍 Iniciando detección de imagen... (Presiona CTRL+C para detener)")
    detect_and_press()
```

## 🛡️ Notas
- Si la imagen **no se detecta**, prueba reduciendo el `confidence` (`0.6` o `0.5`).
- Si `pyautogui` da un error de OpenCV, instala `opencv-python-headless`.
- Funciona en **Windows, Mac y Linux**.

## ✨ Contribuciones
Si quieres mejorar el script o añadir más funcionalidades, ¡eres bienvenido a colaborar!

📩 **Autor:** Juan Gómez 🚀

