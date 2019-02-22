# micropython

h1. Pasos iniciales

1. Te bajas el firmware de http://micropython.org/download#esp8266

2. Instalamos el firmware, para ello:
2.1. Instalamos módulo esptool:
    pip install esptool

2.2. Flasheamos nodemcu
    esptool.py --port /dev/ttyUSB0 erase_flash

2.3. Desplegamos el nuevo firmware
    esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 esp8266-20190125-v1.10.bin 


3. Se crea un punto de acceso ESSID MicroPython-xxxx, pass micropythoN. IP 192.168.4.1.

4. Instalar picocom
    sudo apt install picocom

5. Acceder al dispositivo vía REPL (Read Evaluate Print Loop)
5.1. Vía puerto serie 
    picocom /dev/ttyUSB0 -b115200


h2. Ciclo de desarrollo
tenemos 2 ficheros:
 - boot.py --> se ejecuta al encender y tras resetear. Contiene código que configura el dispositivo para finalizar el arranque. No vas a necesitar cambiarlo
 - main.py --> Si existe, se ejecuta automáticamente tras boot.py, y es donde vas a poner tus cosillas.

 El ciclo para editar y pasar este main.py a la tarjeta sería el siguiente:
 1. Escribes tu main.py
 2. Ejecutar el main.py en la placa:
    ampy --port /dev/ttyUSB0 run main.py
 3. Copiar el main.py en la placa:
    ampy --port /dev/ttyUSB0 run main.py

    


