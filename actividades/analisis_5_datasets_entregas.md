# Analisis de los envios y pruebas con los modelos

En esta practica probe la plataforma de entregas entrenando tanto el arbol de decision como el random forest usando los seis archivos de datos que teniamos disponibles

El objetivo era ver como se comportaba la plataforma cuando le cambiabamos los datos de entrenamiento y entender que diferencias habia entre cada archivo

## Resultados generales

Al correr las pruebas con los dos modelos note diferencias claras en el porcentaje de aciertos dependiendo de que archivo cargaba

| Archivo | Aciertos Arbol | Aciertos Random Forest | Lo que note en los datos |
| :--- | :--- | :--- | :--- |
| envios1.csv | 99% | 99% | Los datos estan muy limpios y ordenados |
| envios2.csv | 76% | 80% | Aparece un nuevo transporte que es el eskuter |
| envios3.csv | 94% | 95% | La gran mayoria de los pedidos son en moto |
| envios4.csv | 91% | 92% | Tiene mas errores por lluvia y horas complicadas |
| envios5.csv | 92% | 93% | Es un reparto variado y mas normal de pedidos |
| envios6.csv | 95% | 94% | Casi no hay paquetes para dron ni para bici |

## Que paso con cada archivo

### envios1.csv
Fue el archivo mas sencillo de todos
Aqui los dos modelos sacaron casi todas las respuestas bien porque los paquetes vienen repartidos en partes iguales entre bicicleta, moto, camioneta y dron
Las reglas de peso y distancia son muy marcadas y el modelo casi no dudo

### envios2.csv
Este archivo fue el mas raro y donde peor les fue a los modelos
Revisando los datos me di cuenta de que metieron un transporte nuevo llamado eskuter
El problema es que un paquete que cabe en eskuter tambien cabe en moto o en bici
Por eso el modelo se equivoco bastante intentando adivinar entre moto y eskuter

### envios3.csv
En este archivo casi todos los paquetes se van en moto
Como casi todo era moto, el modelo aprendio a recomendar moto casi para cualquier cosa
Los drones casi no salieron y en varias ocasiones el modelo prefirio mandar moto aunque el paquete fuera ligero

### envios4.csv
Aqui note que el clima y el trafico afectaban mas la decision
Habia paquetes pequenos pero con lluvia o viento fuerte donde la bici o el dron ya no podian salir
Por eso los modelos fallaron un poco mas que en el primer archivo, pero tiene sentido con la situacion del clima

### envios5.csv
Este archivo se sintio como el mas equilibrado y parecido a un dia de trabajo real
La mayoria son motos, luego bicicletas para distancias cortas, algunas camionetas para cosas pesadas y pocos drones
Random forest saco una ligera ventaja aqui

### envios6.csv
En este archivo casi no existen los viajes en dron ni en bicicleta
La enorme mayoria son camionetas grandes y motos
Curiosamente el arbol de decision salio un poco mejor parado que el bosque porque no se complico con los pocos casos raros

## Diferencias entre usar el arbol y random forest

El arbol de decision es muy rapido para entrenar y para responder en la plataforma web
Ademas es facil entender el porque de las desiciones

Random forest casi siempre acerto mas paquetes porque junta muchos arboles a la vez
La desventaja es que el archivo que genera es mas pesado para guardarlo en la carpeta del proyecto y tarda un poco mas en procesar

## Conclusion

Cambiar de archivo cambia mucho la forma en que la plataforma recomienda los transportes
Si se entrena con datos donde domina un solo vehiculo como paso en el archivo tres, la plataforma no analiza bien y tiende a mandar todo en moto
El caso del archivo dos demuestra que si agregamos un vehiculo nuevo como el eskuter sin definir bien sus limites hace que el sistema se confunda mucho con la moto y la bicicleta
Para poner la plataforma a funcionar de forma confiable conviene entrenarla con un archivo balanceado como el cinco, usando random forest si queremos mayor precision o el arbol si queremos algo ligero
