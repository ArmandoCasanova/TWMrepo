# Analisis de la Implementacion 1

El objetivo del programa es recibir los datos de un pedido (origen, destino, peso, distancia) y consultar un recomendador externo (IA con formato JSON o XML) y con esa sugerencia el sistema elige el transporte mas adecuado (dron, bicicleta, motocicleta o camioneta) y calcula el tiempo, costo y si el paquete cabe en ese transporte.

A grandes razgos notamos que esta implementacion todo el codigo se dividio en diferentes archivos y carpetas y se le asigna a cada parte una tarea especifica

---

## 2. Estructura

### Version en Java

- Clases de datos: Pedido.java, ContextoViaje.java, Sugerencia.java y Plan.java

- Conexiones con proveedores: ClienteOpenAI.java, ClienteXml.java, AdaptadorOpenAI.java, AdaptadorXml.java y la interfaz RecomendadorIA.java, los cuales se encargan de pedir la recomendacion y traducirla a un formato que el sistema entienda

- MedioDeEntrega.java (la base) y las clases EntregaDron.java, EntregaBicicleta.java, EntregaMotocicleta.java y EntregaCamioneta.java, cada una con sus propias reglas de peso, tiempo y costo

- Logistica.java y sus variantes (LogisticaAerea, LogisticaCorta, LogisticaUrbana, LogisticaTerrestre) se encargan de la logistica del transporte

- RegistrarPedido.java coordina el flujo y Main.java ejecuta las pruebas

### Version en Python
En Python la estructura es igual de limpia y se agrupo en modulos

- dominio.py: Define los datos basicos del pedido, viaje y plan
- ia.py: Contiene a los clientes externos y a los adaptadores que traducen las respuestas
- medios.py: Contiene las clases de cada medio de transporte con sus reglas de calculo
- logistica.py: Define la logica para seleccionar y fabricar el transporte
- registrar.py: Contiene la funcion que une todo el proceso
- __main__.py: Archivo que arranca el programa y muestra los resultados

---

## 3. Buenas practicas encontradas

1. Separacion de responsabilidades en archivos individuales
   Cada archivo hace solo una cosa, por ejemplo, si necesitamos cambiar la forma en que se calcula el costo de una bicicleta, solo abrimos el archivo de la bicicleta y no tocamos nada de los demas transportes ni de la inteligencia artificial

2. No hay codigo repetido
   Las formulas para calcular el tiempo y costo de cada vehiculo estan escritas una sola vez

3. Facilidad para agregar cosas nuevas

4. Manejo limpio de los datos
   En lugar de pasar 8 variables sueltas por todos lados, se usan objetos ordenados como Pedido y ContextoViaje. Esto evita confusiones con el orden de los datos

5. Traduccion clara de formatos externos

---

## 4. Malas practicas o aspectos a mejorar


1. Muchos archivos, a pesar de tener buena fragmentacion por modulos o componentes, estaría bien organizarlo de mejor manera ya que al ser escalable podría hacerle una lista de +20 archivos en una sola carpeta.

2. Mensajes de error simples como cuando se recibe un medio de transporte no reconocido, el sistema lanza un error generico en lugar de intentar una alternativa

---

## 5. Conclusion implementacion 1

Es un codigo bien estructurado y organizado, que facilita el trabajo en equipo y el mantenimiento a largo plazo