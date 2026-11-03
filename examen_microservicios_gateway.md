# Examen Microservicios, Gateway y el Monolito con API

**Nombre:** Armando Casanova Lemus

## 1 — La frase del compañero

**a)** el compañero asume que usar una API ya esta separando el cliente del servidor y hay un poco de razon porque ya queda separada la lofica pero esta equivocado si asume que ya con meter a docker es un microservicio, ya que los contenedores de docker solo empaquetan el programa pero no quita que se sigue corriendo todo junto en un bloque y se comparten los mismos recursos



**b)** si pones un proyecto en django dentro de un contenedor de docker que ofrece distintos servicios y se usa una sola base de datos sigue siendo un monolito y si algo falla todo se cae y para cambiar esto se tendría que separar en programas diferentes y que cada uno tuviera su contenedor y se comunicran por red

**c)** habla de los limites de proceso y de depsliegue y no de tecnologías, porque ya vimos que el docker o rest son herramientas que podemos usar pero no necesariamente ya con hacerlo es un microservicio, si no que depende si los componentes son independientes y que tengan su propio despliegue y base de datos y se se pueden reiniciar o apagar sin hacerlo con los otros


## 2 — Tres rutas, una trampa

**a)** mezclaron las rutas con las replicas que sería la escalabilidad o copias del servidor, las rutas lo que resuelven es la organizacion del codigo en la misma aplicacion, ordena todas las funciones, separa los endpoints etc, y las replicas lo que hacen es poder atender mas peticiones haciendo que el proceso se duplique, pero esto sigue sin significar que sea microservicio porque todo el codigo sigue junto


**b)** sigue siendo monolito porque las otras replicas que hay son identicas o sea que siguen contiendo todo junto, lo unico ue pasa es que se atienden mas peticiones repartiendolas en las replicas, si cae una quedan las otras


**c)** Para que de verdad sean microservicios yo definiría en el archivo un servicio llamado `gateway-service` que reciba las peticiones de entrada, otro servicio llamado `usuarios-service` que maneje las cuentas, otro llamado `pedidos-service` que guarde las compras y otro llamado `recomendar-service` que calcule el envío, usando como mínimo cuatro imágenes distintas porque cada una debe empaquetar únicamente el código y las librerías que necesita su propia tarea para poder desplegarse por su cuenta.

se requieren minimo cuatro imagenes para poder separar cada tarea y empaquetar solo las librerías de cada una, como yo lo dividira seria




## 3 — El gateway que «hace de más»

**a)** no es gateway es un monolito, y la analogía sería que un recepcionista recibe al visitante, verifica su identificacion y lo lleva al area que va, lo que sería el validar el jwt (recepcionista), con el que analiza la logica (la librería), el archivista que gaurda en sqlite, el mensaje que envia correos y el diseñador (el html)


**b)** La primera consecuencia es que cada semana que reentrenen y suban el modelo pesado se tendrá que reiniciar todo el contenedor y se dejara a los usuarios sin poder entrar ni hacer pedidos, la segunda es que cuando el servidor de correo tarde o falle se van a quedar colgadas las peticiones y el cliente creerá que su compra no se hizo, y la tercera es que si el cálculo del modelo consume toda la memoria se va a morir también la entrada principal del sistema

**c)** Yo dividiria ese contenedor dejando en el borde únicamente al gateway con nginx para que valide el permiso y redirija el tráfico, y detrás pondría un servicio de pedidos con su base de datos para guardar la compra, otro servicio aparte con el modelo para que solo calcule el medio de transporte y finalmente un servicio de notificaciones detrás para mandar el correo sin bloquear al usuario

## 4 — localhost, la trampa favorita

**a)** falla porque dentro de un contenedor la dirección local apunta al propio contenedor de pedidos y no a la laptop ni a los demás contenedores, entonces cuando pedidos intenta llamar a esa dirección se está buscando a sí mismo en un puerto donde donde no hay nada

**b)** usar el nombre del servicio si funciona porque Docker Compose crea una red con su propio directorio y toma el nombre que se le pone al servicio en el archivo de configuración y lo traduce automáticamente a la dirección interna real que tenga asignada ese contenedor

**c)** Si se muda a la otra laptop yo pondría la dirección `http://192.168.0.57:8002` y para que funcione de verdad tienen que cumplirse dos cosas 
1. en la red, primero que la laptop del compañero tenga abierto el puerto permitiendo conexiones externas
2. que su servicio esté escuchando a toda la red y no solo a su propio dispositivo, porque si solo cambiamos la dirección pero la red del salón bloquea la comunicación entre alumnos o el puerto sigue cerrado entonces la conexión va a seguir siendo rechazada

## 5 — Fallo parcial con números

**a)**el cliente espera alrededor de 204 ms en total, el tiempo dominante lo pone el servicio de recomendar con 200ms mientras que el gateway y pedidos apenas suman unos 4ms extra al flujo

**b)** gracias al plan B que es la mentira util el cliente no ve ningún error sino que recibe su pedido creado tras esperar algunos ms, aceptando la mentira de asignarle una moto por defecto para no perder la venta aunque quizás para ese paquete hubiera sido mejor otro transporte

**c)** Si pedidos se pone a reintentar diez veces seguidas cuando recomendar lleva diez minutos caído, cada petición se va a quedar atrapada esperando y luego se van a agotar todas las conexiones disponibles tanto en pedidos como en el gateway, y todo el sistema va a colapsar para todos los usuarios, por lo que el plan de respaldo es mucho mejor que reintentar a ciegas cuando sabemos que es preferible entregar un pedido con transporte aceptable que tirar toda la tienda

## 6 — Apagan el «edificio equivocado»

**1)** cuando apagas el gateway el navegador muestra que no se puede conectar al sitio y no carga ni la página ni deja crear pedidos, aunque por dentro tanto pedidos como recomendar siguen vivos y podrían responder si alguien les hablara directo desde la red interna

**2)** Cuando apagas pedidos el navegador sí logra cargar la página inicial porque el gateway sigue vivo, pero al intentar crear un pedido devuelve un error de puerta de enlace porque no hay quién procese la compra, mientras que por dentro el servicio de recomendar sigue encendido esperando llamadas que nunca le van a llegar

**3)** cuando se apaga recomendar el navegador carga la página normal y además sí deja crear el pedido, tarda un poco mas porque entra el plan b que asigna moto, de manera que por dentro el gateway y pedidos siguen trabajando juntos para sacar el trabajo adelante

Con esto veo que en el primer experimento el sistema parece totalmente muerto hacia afuera aunque la mayoría de las piezas de negocio siguen encendidas por dentro, y esto enseña que el borde es un punto imiportante porque si se cierra la puerta principal de nada sirve que todas las oficinas de adentro estén trabajando

## 7 — WiFi del salón, conflicto de roles

**a)** el problema que metió Diana es que rompió la idea de tener una sola puerta de entrada controlada y ahora hay dos gateways sin coordinación, por lo que las reglas de acceso, los logs o los límites de peticiones quedan divididos dependiendo de a qué IP le mande la petición el cliente

**b)** lo que falla es que la laptop de Beto busca a Recomendar en su propio localhost y ahí ya no hay nada corriendo, y para corregirlo sin juntar otra vez los servicios solo tiene que cambiar RECOMENDAR_URL poniendo la IP de la laptop de Carla con el puerto 8002

**c)** si la WiFi tiene AP isolation no se puede hacer la práctica así porque las laptops no se ven entre ellas, y mi plan B para mantener los procesos separados sería que alguien prenda el hotspot de su celular y nos conectemos todos ahí, o correr cada servicio en contenedores o puertos distintos dentro de una misma laptop

## 8 — El front que conoce demasiado

**a)** el primer problema es de seguridad porque el HTML expone las IPs internas y cualquiera puede pegarle directo a los servicios, el segundo es que si cambia la IP de un contenedor hay que editar el front, y el tercero es la consistencia o el CORS porque si el primer fetch a Recomendar pasa pero falla el de Pedidos la operación queda a medias

**b)** lo correcto es que el navegador haga un solo fetch al gateway, luego el gateway manda la petición a Pedidos y es Pedidos quien llama por dentro a Recomendar antes de guardar y responder, y no lo hace el navegador porque la comunicación entre servicios debe ir por la red interna del servidor sin depender del internet del cliente

**c)** quien debe crear el folio es únicamente Pedidos porque es el encargado de registrar la compra, ya que si Recomendar y Pedidos crean folios por separado se rompe la consistencia de que exista un solo ID único por pedido y quedarían registros diferentes que no coinciden

## 9 — El LLM vendedor

**a)** el nombre cerebro está mal porque es muy ambiguo y no dice qué hace, además mezclaron el oficio de logística que elige el transporte con el .joblib y el de ventas que genera el pitch con el LLM, entonces cuando el LLM tarda 8s se queda bloqueada toda la petición y el envío ya no puede responder en menos de 500ms

**b)** yo pondría dos endpoints o servicios separados, uno de /recomendar-envio con el .joblib que use el flujo de pedido/envío para responder rápido al comprar, y otro de /pitch-ventas con el LLM que consuma el front de tienda mientras el cliente ve el producto

**c)** el front de tienda debe apuntar siempre al gateway y no a la GPU, porque si mañana cambiamos de proveedor o de host del LLM solo tenemos que cambiar la URL una sola vez en la configuración del gateway sin tocar el front

## 10 — El inversionista y la semana imposible

**a)** Yo le diría al inversionista que nuestra aplicación de clientes ya funciona con microservicios donde realmente importa para vender y escalar, pero negarnos a mover todo a ciegas porque es para cuidar su dinero, porque si intentamos despedazar el panel interno y meter inteligencia artificial en siete días con solo cinco personas vamos a tirar la tienda en producción, podemos arruinar los datos de los pedidos actuales y nos quedaremos sin sistema para mostrarle a los clientes ni para operar

**b)** Primero pondría meter autenticación y límite de peticiones en el gateway público porque la tienda ya está expuesta y sin eso cualquiera nos tira o roba datos

en segundo lugar sacaría el reentrenamiento del modelo a un proceso separado para que cada actualización semanal deje de tumbar las ventas activas


y en tercer lugar dejaría subir el modelo de ventas pero le pondría tiempos límite para no congelar la tienda, y en último lugar dejaría partir el panel interno de Django porque ya funciona bien, tiene poco tráfico y dividirlo no da nada extra

**c)** Una métrica clara que yo mediría para decidir partir una pieza del monolito es contar cuántas veces al mes un despliegue provoca que el tiempo de respuesta del resto de las rutas supere los dos segundos o deje sin servicio a los demás usuarios del panel

**d)** Para mí los microservicios no son el objetivo de que terminamos un proyecto, solo una herramienta de trabajo que uso cuando un programa ya es muy grande y el tamaño del equipo o la escala del sistema lo requiere

