from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

class Pantalla:
    def __init__(self, width=128, height=64):
        # Configuración I2C (usando GP20 y GP21)
        self.i2c = I2C(1, scl=Pin(27), sda=Pin(26), freq=200000)
        # Crear objeto para la pantalla OLED (128x64)
        self.oled = SSD1306_I2C(width, height, self.i2c)

    def mostrar_texto(self, texto, x=0, y=0):
        # Limpiar la pantalla
        self.oled.fill(0)
        # Mostrar texto en la posición especificada
        self.oled.text(texto, x, y)
        # Actualizar la pantalla
        self.oled.show()