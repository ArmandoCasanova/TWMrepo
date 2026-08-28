
## 1. Whatsapp con LoRa

- Para el software que corre dentro del dispositivo de radio, se recomienda C++, porque es el lenguaje en el que está construido Meshtastic, un proyecto de código abierto que ya resuelve el envío de mensajes en red usando LoRa. En vez de programar desde cero cómo viajan los mensajes entre dispositivos, te apoyas en un sistema que ya existe, ya funciona y ya fue probado por muchos usuarios en el mundo real

- Para crear la app usaría Meshtastic el es un proyecto abierto y probado que ya usa LoRa y puede implementarse en apps, y ya que está escrito en C++ sería este el lenguaje que usaría en la app

- La app la crearía en Kotlin y Swift para asegurar el funcionamiento optimo en ambas, aunque podría usar algun lenguaje que funione para ambos no es tan recomendable y es más compatible de forma separada para usar junto con Meshtastic


## 2. Identificar carros en estacionamiento

- Para el lenguaje principal, se recomienda Python, porque es el más usado en el mundo para trabajar con cámaras e inteligencia artificial, y tiene más herramientas ya hechas para este tipo de proyecto

- De lenguaje principal usaría python ya que es más usado para este tipo de tecnologias y ya contiene muchas herramientas para la IA de detección que usaría para los carros

- YOLO podría usarlo como la IA de detección la cual ya está entrenada para detectar objetos en videos

- Para enviar la información usaría FastAPI, ya que ya lo conozco, y es rapido y simple para la creación de API's y fucniona con pyhton