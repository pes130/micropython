# micropython

## Pasos iniciales

* Te bajas el firmware de http://micropython.org/download#esp8266

* Instalamos el firmware, para ello:
* * Instalamos módulo esptool:
    ```sh
    pip install esptool
    ```

* * Flasheamos nodemcu
    ```sh
    esptool.py --port /dev/ttyUSB0 erase_flash
    ```

* * Desplegamos el nuevo firmware
    ```sh
    esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 esp8266-20190125-v1.10.bin 
    ```

* Se crea un punto de acceso ESSID MicroPython-xxxx, pass micropythoN. IP 192.168.4.1.

* Instalar picocom
    ```sh
    sudo apt install picocom
    ```

* Acceder al dispositivo vía REPL (Read Evaluate Print Loop)
* *  Vía puerto serie 
    ```sh
    picocom /dev/ttyUSB0 -b115200
    ```


## Ciclo de desarrollo
tenemos 2 ficheros:
 - boot.py --> se ejecuta al encender y tras resetear. Contiene código que configura el dispositivo para finalizar el arranque. No vas a necesitar cambiarlo
 - main.py --> Si existe, se ejecuta automáticamente tras boot.py, y es donde vas a poner tus cosillas.

 El ciclo para editar y pasar este main.py a la tarjeta sería el siguiente:
 * Escribes tu main.py
 * Ejecutar el main.py en la placa:
    ```sh
    ampy --port /dev/ttyUSB0 run main.py
    ```

 * Copiar el main.py en la placa:
    ```sh
    ampy --port /dev/ttyUSB0 run main.py
    ```




