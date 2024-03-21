from gpiozero import LED, Button #importa las librerias LED y Button
from signal import pause #importa la libreria pause

led = LED(19) #define al led como el pin 19
button = Button(18) #define el boton como el pin 18

button.when_pressed = led.on 
button.when_released = led.off 
#uso las funciones "button" que importe desde "gpiozero" pra declarar que cuando el boton este presionado, se prenda el LED, y que cuando no este presionado se apague

pause()
