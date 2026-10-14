# Análisis del Dataset

## Actividad 1 — El retrato del dataset

### 1. Predicción
* Cuando llueve creo que va a dominar la camioneta porque protege las cosas del agua y evita que los repartidores se mojen
* Para el centro de la ciudad creo que dominará la bicicleta porque hay mucho tráfico y las distancias son cortas
* La distancia máxima de una bicicleta creo que rondará entre 5 y 8 km porque es lo normal para un recorrido pedaleando
* Creo que sí habrá envíos con etiquetas que rompan las reglas porque en los registros siempre se escapan errores o ruido

### 2. Comprobación
* Con lluvia dominó la moto con 74.83% mientras que la camioneta tuvo 16.68% y tanto bicicleta como dron quedaron casi o totalmente fuera con 8.49% y 0%
* En el centro dominó la bicicleta con 58.45% seguida de la moto con 28.03% y la camioneta con 13.52% mientras que el dron tuvo 0%
* En el resumen numérico la distancia máxima para bicicleta fue de 7.00 km al igual que 39.90 km para moto y 14.99 km para dron y 59.12 km para camioneta
* En la comparación fallé con la lluvia porque pensé que ganaría la camioneta pero la moto es más barata entonces la prefieren aunque llueva y acerté en que la bicicleta dominaría en el centro por ser ágil

### 3. Decisión (Preguntas)
1. El dron nunca aparece en el centro ni en la zona rural con 0% y tampoco aparece con lluvia o viento fuerte marcando 0% porque la regla prohíbe volar con clima que no sea despejado o en espacio aéreo restringido como el centro además de que a la zona rural no llega por distancia
2. La columna que explica por qué la bicicleta casi no va a la periferia es distancia_km porque las distancias allá casi siempre superan su límite máximo de 7.00 km
3. Mirando los máximos de los datos se pueden adivinar los topes físicos de bicicleta con 7 km y moto con 40 km y dron con 15 km pero no se puede adivinar el límite de la camioneta porque el negocio no le pone tope y su valor más alto solo depende de los paquetes que se generaron
4. Salieron 107 camionetas en viajes de menos de 2 km y la mayoría se justifica por llevar paquetes pesados de más de 25 kg o volúmenes mayores a 90 L o mercancía refrigerada mientras que las pocas que no cumplen eso se explican por lluvia o paquetes frágiles o ruido del generador
* Para pensar: solo con el archivo de datos se podrían reconstruir los topes máximos de distancia y peso pero no las prohibiciones de clima o zonas y dejar que un modelo aprenda las reglas solo con datos es peligroso porque puede inventar patrones falsos y mandar un dron con tormenta si nadie le programa las restricciones a mano

---

## Actividad 2 — La hora y el dron

### 1. Predicción
* A las 3:00 creo que saldrán 0 drones porque no tienen permitido volar en la oscuridad
* El porcentaje de envíos de noche creo que rondará entre 10% y 15% porque la mayor parte de las entregas se hacen de día

### 2. Comprobación
* A las 3:00 se registraron exactamente 0 envíos en dron
* Los envíos de noche antes de las 6 o desde las 21 suman 1053 que representan el 10.53%
* En la comparación acerté porque ningún dron vuela de madrugada y el volumen nocturno quedó dentro de lo que esperaba con 10.53%

### 3. Decisión (Preguntas)
1. Entre las 21:00 y las 5:00 no hay ningún envío en dron y esto coincide de forma exacta con la regla que prohíbe vuelos nocturnos desde las 21 hasta antes de las 6
2. Hay 1053 envíos nocturnos comparados con 8947 de día entonces el modelo recibe pocas muestras de noche y por eso le cuesta más aprender reglas sólidas para ese horario
3. Entre las 20:00 y las 21:00 las bicicletas caen de 115 a 20 mientras las motos suben de 160 a 240 porque el sistema aplica una penalización a la bicicleta cuando se hace de noche para proteger al ciclista
4. El árbol solo evalúa si una variable es menor o igual a un valor entonces necesita al menos dos preguntas sobre la hora para delimitar la noche porque las horas nocturnas abarcan dos extremos distintos del reloj
* Para pensar: crearía una columna llamada es_noche con un valor de 1 cuando la hora sea menor a 6 o mayor o igual a 21 y comprobaría que sirvió entrenando el modelo para ver si esa nueva columna recibe importancia mayor a cero y reduce los fallos nocturnos

---

## Actividad 3 — Anatomía de los errores

### 1. Predicción
* Creo que la confusión más habitual ocurrirá entre moto y bicicleta porque compiten por paquetes pequeños en distancias cortas
* Dudo mucho que el modelo confunda una bicicleta con una camioneta porque tienen diferencias de peso y volumen demasiado grandes

### 2. Comprobación
* El modelo tuvo 158 errores en los datos de prueba y las confusiones más altas fueron moto asignada a bicicleta con 46 casos luego camioneta a moto con 32 y moto a dron con 29
* El modelo nunca confundió una bicicleta con una camioneta registrando 0 casos
* En la comparación acerté porque la principal confusión se dio entre moto y bicicleta en viajes cortos y además nunca hubo confusión de bicicleta hacia camioneta

### 3. Decisión (Preguntas)
1. Hubo 158 errores y los fallos principales ocurren entre medios parecidos en capacidad y distancia lo que indica que el modelo duda principalmente en las fronteras intermedias
2. De las 29 motos que el modelo predijo como dron hay 26 que eran de noche y las reglas del negocio corrigen esos 26 casos descartando el dron mientras que los 3 restantes ocurrieron de día con paquetes ligeros que cabían en dron pero la moto costaba menos
3. Las 46 motos clasificadas como bicicleta tienen recorridos menores al límite de 7 km con un tope de 6.89 km y se diferencian de las bicicletas reales porque varias llevaban pesos mayores a 8 kg o lluvia donde la bicicleta no convenía
* Para pensar: elegiría resolver el error de mandar motos a dron aplicando las reglas de negocio porque desplegar un dron por error sale caro e inseguro mientras que las reglas duras lo descartan al instante sin necesidad de complicar el modelo

---

## Actividad 4 — ¿Qué columnas usa de verdad el modelo?

### 1. Predicción
* Creo que las columnas más importantes serán distancia_km y volumen_l y peso_kg junto con refrigerado
* Creo que el modelo casi no usará la zona_destino ni el id_envio ni el trafico porque su efecto ya queda cubierto por la distancia y el tiempo

### 2. Comprobación
* Las columnas con mayor importancia en el árbol fueron distancia_km con 0.322 y volumen_l con 0.193 y clima con 0.144 y refrigerado con 0.131 y peso_kg con 0.126
* Al retirar distancia_km la exactitud cayó de 0.921 a 0.793 mientras que al retirar zona_destino la exactitud se mantuvo idéntica en 0.921
* En la comparación acerté porque las características de tamaño y distancia tuvieron el mayor peso y la zona de destino no influyó en el árbol

### 3. Decisión (Preguntas)
1. Las cuatro columnas con mayor peso son distancia_km y volumen_l y clima y refrigerado y coinciden con las primeras preguntas del árbol porque definen las limitaciones básicas de cada vehículo
2. La columna que más tira la exactitud al quitarla es distancia_km con una baja de 0.128 mientras que zona_destino y trafico no causan ninguna variación en el resultado
3. La zona de destino tiene importancia cero porque el centro ya se deduce por sus distancias cortas y además la plataforma descarta el dron en el centro mediante sus reglas de negocio antes de confirmar el viaje
* Para pensar: la app debe seguir pidiendo datos como la zona de destino aunque el árbol no los use porque el sistema los necesita para trazar la ruta de reparto y calcular tarifas de entrega

---

## Actividad 5 — El dron es minoría: ¿hay que balancear el dataset?

### Parte A — Pensar antes de tocar los datos
1. Un modelo que nunca diga dron y acierte todo lo demás alcanzaría 90.5% de exactitud y uno que solo diga moto tendría 45.8% lo que comprueba que la exactitud no sirve para juzgar clases desbalanceadas entonces se debe evaluar con precision y recall
2. Hay pocos drones porque la empresa cuenta con pocos equipos y muchas restricciones de vuelo entonces no es una falla de captura sino el reflejo de la realidad operativa
3. El balanceo se debe hacer únicamente sobre los datos de entrenamiento y la prueba nunca se toca porque la prueba debe conservar las proporciones reales para medir el rendimiento verdadero

### Parte B — Probar estrategias

| Estrategia | Envíos entrenamiento | Exactitud | Precision dron | Recall dron | Veces que predice dron (Reales: 190) | Sugerencias imposibles |
| --- | --- | --- | --- | --- | --- | --- |
| Sin balancear | 8000 | 0.92 | 0.84 | 0.91 | 205 | 31 |
| Con balanceo (class_weight) | 8000 | 0.90 | 0.77 | 1.00 | 248 | 35 |
| Oversampling (repetir drones) | 10274 | 0.90 | 0.72 | 1.00 | 263 | 56 |

* Trampa de balanceo: al duplicar drones antes de separar el entrenamiento y la prueba la exactitud subió a 0.925 y la precisión a 0.97 pero esa mejora es falsa porque el modelo se aprendió de memoria registros que terminaron apareciendo en la evaluación

### Parte C — Interpretar
1. Al balancear el recall del dron subió a 1.00 pero la precisión bajó a 0.77 porque el árbol aprendió a arriesgarse más asignando drones ante la menor duda aumentando los falsos positivos
2. Si se balancea reduciendo las otras clases se tiran a la basura miles de ejemplos de motos y bicicletas perdiendo información valiosa sobre los medios más usados
3. Repetir drones y usar class_weight entregan números casi iguales porque persiguen el mismo principio matemático de castigar con más severidad cada fallo en los drones
4. Tras balancear la confianza reportada ya no significa lo mismo en el mundo real porque el modelo se entrenó con una proporción artificial que no refleja la demanda cotidiana

### Parte D — Decidir
* Para pensar: recomiendo no balancear el modelo en producción porque mandar un dron cuando no conviene representa un riesgo operativo alto y pérdidas económicas además de que el modelo balanceado eleva las sugerencias imposibles a 35 aumentando el trabajo de descarte y si la empresa llega a comprar el doble de drones los datos reales irán subiendo solos sin necesidad de trucar las proporciones
