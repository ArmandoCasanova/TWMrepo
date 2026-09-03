  # Actividad

  ## Mision 1

  | Problema | Capa | Patron | Por qué ese y no el vecino | Marco | Cuando no aplicaría |
  | --- | --- | --- | --- | --- | --- |
  | Cada trámite copia el bloque de sesión, la bitácora y el encabezado en archivos distintos | Políticas transversales | Front Controller y Chain of Responsibility | Front Controller ya que centraliza la recepción de rutas y la cadena ejecuta los filtros antes del trámite. Es Chain of Responsibility y no Decorator porque el objetivo es decidir si la petición continúa o se corta, añadir comportamiento a un objeto | El enrutador y el middleware de Spring, Laravel o Express ya cumplen | Con una sola ruta y un chequeo puntual basta una llamada directa |
  | El script de pago es un switch de doscientas líneas y mezcla el vocabulario del banco con el del reglamento | Aplicación y dominio, integración | Strategy con Adapter | Strategy da un contrato común para alternar el medio de cobro. Adapter traduce el vocabulario ajeno del banco al del dominio porque se trata de una interfaz externa que no controlamos, mientras que Facade simplificaría un subsistema propio | En Java se resuelve con interfaz e inyección, en JavaScript o Python una función cumple el rol de Strategy | Con una sola pasarela fija y estable no hay variación de algoritmo que justifique Strategy |
  | La plantilla del kardex y los reportes de constancias ejecutan SQL directo | Datos | Repository con Service Layer | Repository saca la consulta de la plantilla y presenta los datos como colección. Es distinto de Active Record porque ese patrón une la fila de la base con la lógica en la misma clase, lo que tiende a mezclar persistencia con presentación | La sesión del ORM ya funciona como Unit of Work, no hace falta escribirla aparte | Si el reporte es único y no se reutiliza ni se prueba fuera de HTTP, basta una consulta directa |
  | Si el correo falla no se registra el alta y si el alumno pulsa dos veces pagar se cobra doble | Aplicación y dominio, integración | Unit of Work con Observer y clave de idempotencia | Unit of Work confirma cobro y alta juntos en una sola transacción, Observer notifica el correo por separado para que un fallo de red no aborte esa transacción, ya que un Observer síncrono en el mismo hilo sí la afectarí, el doble cobro se resuelve con una clave de idempotencia, que es un patrón de integración distinto de los dos anteriore | La transacción del ORM cumple el papel de Unit of Work, y un emisor de eventos del lenguaje cumple el de Observer | Si la operación es de solo lectura o si nunca hay dos escrituras que coordinar, ninguno de los dos se justifica |
  | La app pide un JSON mínimo y el kiosco pide HTML completo, y la app hace doce peticiones para iniciar | Integración | Backend for Frontend | El BFF agrega los datos según el cliente que consulta. Un API Gateway resuelve políticas generales como autenticación y cuotas, no el grano de datos que necesita cada pantalla | Se escribe como servicio propio, ningún marco lo trae de fábrica | Con un solo tipo de cliente basta un endpoint bien diseñado |
  | Las caídas del banco y del validador de CURP bloquean incluso la consulta del kardex | Integración | Circuit Breaker con timeout | Circuit Breaker corta las llamadas tras fallos repetidos y sirve una respuesta degradada. Reintentar de forma indefinida como haría Retry agota conexiones y aumenta la espera del usuario en vez de resolver el problema | Bibliotecas de resiliencia como Resilience4j o Polly ya lo implementan | Ante un error de validación del cliente o una comunicación local en memoria no aplica |

  ## Mision 2

  1. **Enrutador del marco** Recibe el POST de pago, identifica la ruta y despacha sin meter reglas de negocio. Patrón: Front Controller.

  2. **Filtros de entrada** Validan la sesión y el token del formulario, y detienen una segunda petición si detectan un doble clic. Patrón: Chain of Responsibility.

  3. **Controlador de la petición** Toma los datos del formulario, verifica el formato y delega al servicio de aplicación, sin ejecutar SQL ni contener el reglamento de cobro. Patrón: Controller.

  4. **Servicio de aplicación** Orquesta el trámite de pago y alta de materias de forma independiente al canal, sea web, móvil o consola. Patrón: Service Layer.

  5. **Pasarela de cobro** Se elige el método de pago bajo un contrato común y se traduce el protocolo del banco al lenguaje del dominio, incluyendo los códigos de respuesta. Patrón: Strategy con Adapter.

  6. **Persistencia y confirmación** El repositorio gestiona cobro e inscripción como colecciones, y la transacción confirma juntos el cobro y el alta de materias, revirtiendo todo si algo falla. Patrón: Repository con Unit of Work.

  7. **Notificaciones posteriores** Una vez confirmada la transacción se publica el evento de pago acreditado, y el correo y el aviso a caja se procesan por separado sin afectar el alta ya persistida. Patrón: Observer.