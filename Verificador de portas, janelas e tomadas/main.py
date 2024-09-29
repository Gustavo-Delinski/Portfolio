from machine import Pin
from utime import sleep

print("Hello, ESP32!")

lingueta_da_porta = Pin(15, Pin.OUT)
trinco_da_porta = Pin(18, Pin.OUT)
janela = Pin(27, Pin.OUT)
tomada = Pin(32, Pin.OUT)
while True:
  lingueta_da_porta.on()
  trinco_da_porta.on()
  janela.on()
  tomada.on()

