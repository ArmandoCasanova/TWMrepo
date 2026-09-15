# Comparacion y conclusión

Casanova Lemus Armando
Figueroa Merino Cesar
Murillo Rivera Annatar Armando
Rodriguez Reyna Kelly Merali
Roque Cortes Daniel Adrian

Despues de analizar por separado la Implementacion 1 y la Implementacion 2, tanto en sus versiones de Java como de Python notamos que ambos programas resuelven exactamente el mismo problema y muestran exactamente los mismos resultados en la consola, pero la forma en que estan estructurados es totalmente diferente.

---

## 2. Comparativa

| Aspecto | Implementacion 1 | Implementacion 2 |
| :--- | :--- | :--- |
| Organizacion del codigo | Dividido en varios archivos y modulos ordenados | Todo metido en un solo archivo largo |
| Repeticion de codigo | Las formulas de cada transporte se escriben una sola vez | Se repiten las mismas formulas para cada proveedor |
| Facilidad para agregar un nuevo transporte | solo se crea un archivo nuevo para ese transporte | hay que modificar varios if y else en el archivo principal |
| Facilidad para agregar un nuevo proveedor | se crea un nuevo traductor sin tocar los transportes | hay que alargar la funcion principal con mas condiciones |
| Manejo de datos | Usa objetos claros (como Pedido y Plan) que agrupan la informacion | Pasa 8 parametros sueltos a una sola funcion |
| Trabajo en equipo | Facil, cada integrante puede editar archivos distintos | Dificil, todos los integrantes chocarian en el mismo archivo |
| Facilidad para una prueba rapida | Requiere navegar entre varias clases y archivos | Solo se abre y corre un unico archivo |

---

## 3. Puntos clave analizados por el equipo

### A. Que pasa cuando hay que hacer un cambio
- En la Implementacion 1: Si queremos cambiar el costo por kilometro de la camioneta, vamos directo al archivo de la camioneta, cambiamos un numero y listo. El resto del sistema sigue funcionando igual.
- En la Implementacion 2: Tenemos que buscar donde esta la camioneta dentro del bloque de OpenAI y luego volver a buscarla dentro del bloque de XML. Si cambiamos uno y olvidamos el otro, el programa tendra errores.

### B. Como se manejan las respuestas externas
- En la Implementacion 1: Hay un paso intermedio que convierte las respuestas raras de los proveedores a nombres estandar que todo el programa conoce.
- En la Implementacion 2: El codigo revisa directamente cadenas de texto dentro de la misma funcion que calcula los costos, mezclando todo en un solo lugar.

### C. Claridad y orden de las funciones
- En la Implementacion 1: Las funciones son cortas y hacen una tarea concreta (una calcula el costo, otra fabrica el objeto, otra muestra los datos).
- En la Implementacion 2: Una sola funcion hace todo el trabajo de principio a fin, lo que la vuelve pesada y dificil de corregir si algo falla.

---

## 4. Conclusion 

**La implementacion 1 es la mejor opcion ya que:**

1. Aunque al principio toma mas tiempo crear varios archivos, a largo plazo ahorra tiempo y evita dolores de cabeza al corregir errores

2. Evita la duplicacion de codigoy  se garantiza que el sistema siempre calcule los mismos precios y tiempos sin importar de donde venga la sugerencia

3. Permite que el proyecto crezca y así la empresa puede sumar nuevos tipos de entregas o nuevos proveedores sin tener que rehacer lo que ya funciona

4. En un equipo de desarrollo, varios programadores pueden trabajar en diferentes partes del proyecto sin tener conflictos por el mismo archivo
