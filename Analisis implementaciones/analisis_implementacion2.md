# Analisis de la Implementacion 2

Casanova Lemus Armando
Figueroa Merino Cesar
Murillo Rivera Annatar Armando
Rodriguez Reyna Kelly Merali
Roque Cortes Daniel Adrian

El objetivo del programa es el mismo que en la primera implementacion que es procesar dos pedidos, consultar a un proveedor y calcular el medio de entrega, tiempo y costo correspondiente

Sin embargo, a diferencia del primer proyecto, aqui todo el funcionamiento fue metido dentro de un solo archivo y practicamente dentro de una sola funcion


## 2. Estructura

### Version en Java
Todo el programa vive dentro de un unico archivo llamado Despacho.java:
- No se crearon paquetes ni carpetas de apoyo
- No existen clases para representar un Pedido o un Plan
- Todo ocurre dentro del metodo estatico registrar Pedido, el cual recibe 8 datos sueltos
- Dentro de este metodo se usa un bloque gigante de if y else if para saber que proveedor usar y que transporte calcular

### Version en Python
En Python es lo mismo en despacho.py:
- Todo el codigo esta en un solo script de alrededor de 150 lineas
- Existe una sola funcion llamada registrar_pedido con 8 argumentos sueltos
- Las condiciones de OpenAI y del proveedor XML contienen bloques de codigo copiados y pegados

## 3. Buenas practicas encontradas

Como tal, no encontramos alguna buena practica, pero podríamos clasificar como "ventaja" lo siguiente:

1. Facilidad para ejecutarlo rapido:
   Como todo esta en un solo archivo, solo se necesita compilar y correr Despacho.java o ejecutar despacho.py directamente ya que no hay multiples carpetas ni configuraciones

2. Si una persona no conoce el codigo, le puede ser mas facil entender el flujo del programa de arriba hacia abajo

---

## 4. Malas practicas identificadas

Al revisar a detalle el codigo, nuestro equipo encontro varios problemas graves que dificultan su uso en un proyecto real:

1. Codigo duplicado:
   El problema mas grande es que las formulas para calcular costos, tiempos y capacidad de los transportes estan escritas dos veces exactamente iguales, una vez dentro de la seccion de OpenAI y otra vez dentro de la seccion de XML. 

   Si suben algun precio deberían de subirlo en cada seccion o podría haber problemas

2.  El metodo registrarPedido se encarga de recibir los datos, comunicarse con el proveedor, interpretar la respuesta, calcular las rutas, calcular los precios e imprimir en pantalla y cuando una sola funcion hace tantas cosas a la vez, se vuelve muy enredosa y confusa.

3.  La funcion recibe 8 parametros directos. Es muy facil equivocarse al llamarla si se confunde el orden de dos valores booleanos como trafico y lluvia.

4.  Si queremos agregar un nuevo transporte (por ejemplo un camion grande), tenemos que abrir el archivo principal y modificar multiples bloques de if y else if. Con cada cambio corremos el riesgo de descomponer lo que ya estaba funcionando.

5.  Para leer el XML, el codigo solo busca texto con condiciones simples (como xml.contains) en lugar de procesarlo y si el proveedor cambia un espacio o el orden de una palabra, el sistema puede fallar

6. Si dos o tres personas quieren trabajar en este proyecto a la vez tendrian que modificar el mismo archivo al mismo tiempo, lo que generaria conflictos

---

## 5. Conclusion 

Es un codigo rapido, de borrador, para entender la logica de funcionamiento pero no como implementacion real y escalable
