from gpiozero import LED #importa la libreria LED
from time import sleep   #importa la libreria sleep
ledv = LED(13)
ledr = LED(19)
leda = LED(26) #declara los 3 led y les asigna un pin
while True:
 ledv.on()
 sleep(0.25)
 leda.off()
 ledr.on()
 sleep(1)
 ledv.off()
 leda.on()
 sleep(0.5)
 ledr.off()
#crea un bucle en el que el led verde apaga al azul, el rojo al verde y el azul al rojo
