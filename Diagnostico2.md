Armando Casanova Lemus 

1. Metodologías: ¿Cual es la diferencia principal entre una metodologia de desarrollo tradicional (como Cascada) y una metodologia agil (como Scrum) frente a los cambios en los requisitos?
Una metodologia agil deja las jerarquias o el paso a paso que siguen las metodologias tradicionales, y usan metodos más rapidos y decentralizados, es decir que se puede trabajar en simultaneo, y las correciones son mas inmediatas ya que no requeire pasar por muchos niveles para validaciones. 


2. Requerimientos: Explica la diferencia entre requerimientos funcionales y no funcionales, dando un ejemplo de cada uno aplicable a una plataforma web.
Los requerimientos funcionales describen acciones, por ejemplo: La app debe tener un boton para subir documento. Mientras ques que los no funcionales describen otras cosas como calidad, etc ejemplo: La web debe cargar rapidamente.

3. Arquitectura: Describe el modelo Cliente-Servidor y explica brevemente como se comunican el frontend y el backend en una aplicacion web moderna.
Es un modelo que divide las funciones que tiene el cliente, es decir, la parte del software que permite la interaccion con el humano, que sería el fron, y la parte que se encarga de procesar la información, verificarla etc, que es el back, esta comunicacion se lleva a cabo mediante peticiones API REST, y es como funcionan las apps actualemnte.


4. Bases de Datos: ¿En que escenarios recomendarias utilizar una base de datos relacional (SQL) frente a una no relacional (NoSQL) para el almacenamiento de datos en una aplicacion?
Una base SQL es recomendable cuando utilizaras datos establecidos que regfularmente no cambian ya que funiona con tablas, y cuando tienes la necesidad de relacionarlos entre ellos asi como con otros atributos, o entidades (relacionar un cliente con un centro de trabajo), ya que no relacional son principalmente conjuntos de datos que no permiten una comparacion directa.


5. APIs: ¿Que es una API REST y que papel fundamental juega en la integracion entre una aplicacion movil y los servidores (backend)?
Las API REST son aquellas que permiten la comunicacion entre la app y el servidor, trnasportan la informacion de un lugar a otro. En la integración de una app, el front no tiene acceso a los datos directamente, una API permite obtener datos de la base mediante la comunicación con el back.

6. Control de Versiones: Explica la importancia de utilizar Git en un equipo de desarrollo de software y describe brevemente que es un "merge conflict" (conflicto de fusion).
Git es importante ya que permite trabajar en un entorno colaborativo, actualizado, que lleva control de que se añade o elimina,ademas da facilidad de contar con diferentes versiones de un codigo y el poder de volver a cualquiera de ellas. Un merge conflict ocurre cuando quieres combinar tu entorno local con el de la nube u otra rama diferente y ambos codigos tienen diferencias criticas (en el orginal existe algo que en local ya no, o viceversa, así como lineas modificadas / remplazadas en uno de ambos), ocurre usualmente al trabajar en una verison anteriro del repo y querer subir al actual.

7. Pruebas: ¿Qué son las pruebas unitarias (unit testing) y por que son cruciales para asegurar la calidad del software antes de su paso a produccion?
Sirven para probar partes del codigo y que funcionen correctamente, son unitarias ya que se enfocan en partes especificas, y son importantes ya que permiten que, de manera automatizada, tengamos la certeza de que las funciones de nuestro software funcionan antes de pasar a produccion. A veces un fix que no tiene nada que ver puede romper una funcion crucial.

8. POO: Define los conceptos de encapsulamiento y polimorfismo de la Programación Orientada a Objetos, y menciona cómo ayudan a crear un código más mantenible.
El encapsulamiento significa controlar el acceso a los atributos de un objeto, haciendo que solo sean accesibles mediante metodos que nosotros elijamos. 
El polimorfismo permite que un mismo método funcione diferente dependiendo de que es lo que recibe. Por ejemplo, un metodo actuara diferente al recibir un objeto de la clase trabajador, que si recibe un objeto de la clase cliente.

9. Patrones de Diseño: ¿Que es el patron de arquitectura Modelo-Vista-Controlador (MVC) y como ayuda a organizar el codigo en el desarrollo de software?
Es una forma de desarrollo que divide las funcionalidades en tres partes separadas, es decir el codigo funcional, una interfaz y la comunicacion entre ellos que son los controladores, esto ayuda a tener un software más estructurado y adaptable, también si se necesitan hacer un cambio solo se modifica lo necesario, si se cambia la interfaz no interfiere en el codigo. Si se modifica un codigo no se toca la interfaz necesariamente, etc.

10. Seguridad: Explica la diferencia tecnica entre "autenticacion" y "autorizacion" en el contexto de seguridad de una aplicacion.
Autenticacion verifica a la persona, como un login. Autorizacion es la validacion de permisos de un objeto, por ejemplo si un cliente tiene acceso a crear nuevos clientes o no, o a entrar a diferentes modulos.