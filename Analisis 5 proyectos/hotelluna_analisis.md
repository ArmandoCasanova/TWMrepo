# Revisión del proyecto: Hotel Luna

Este documento es una revisión general del proyecto Hotel Luna, con el propósito de analizar su estructura, archivos, patrones de código e identificar todas las problemáticas presentes.

---

## 1. Patrones presentes

- Interferencia de Servlet casero que captura las peticiones antes de que Spring MVC pueda procesarlas normalmente.
- Omisión de la capa de servicio y repositorios, ejecutando sentencias SQL manuales directamente desde los controladores.
- Generación de tablas HTML concatenadas dentro del código backend de Java.

---

## 2. Problemas por archivo

| Archivo | Tipo | Categoría | Problema |
| --- | --- | --- | --- |
| `README_ARQ.txt` | ALTA | Documentación | La documentación habla de un almacén de piezas de la NASA cuando el proyecto es para reservación de hotel |
| `application.properties` | CRÍTICA | Seguridad | Las credenciales de acceso a la base de datos están expuestas en texto plano en la configuración |
| `FrontControllerServlet.java` | CRÍTICA | Arquitectura | Tiene un servlet casero que intercepta todas las peticiones y bloquea el funcionamiento normal de Spring |
| `LoginCtrl.java` | CRÍTICA | Seguridad | Presenta inyección SQL en el inicio de sesión al concatenar correo y clave en la consulta a la base de datos |
| `LoginCtrl.java` | CRÍTICA | Seguridad | Realiza la validación de administrador basada en una cookie del navegador que cualquiera puede alterar |
| `LoginCtrl.java` | ALTA | Seguridad | Las claves de los empleados se almacenan en la base de datos sin ningún cifrado |
| `HomeCtrl.java` | ALTA | Rendimiento | Realiza peticiones HTTP locales repetitivas en bucle que retrasan la carga de la página principal |
| `HomeCtrl.java` | MEDIA | Calidad de Código | Lanza excepciones genéricas no controladas que muestran pantallas de error al usuario |
| `ReservaCtrl.java` | CRÍTICA | Seguridad | Presenta inyección SQL al registrar la reservación y actualizar el estado de las habitaciones |
| `ReservaCtrl.java` | ALTA | Arquitectura | El proceso de cobro bancario y envío de correos se ejecuta de forma síncrona afectando la respuesta |
| `ReservaCtrl.java` | ALTA | Arquitectura | Carece de control transaccional por lo que puede dejar datos incompletos en la base de datos si ocurre un error |
| `FacturaSql.java` | MEDIA | Rendimiento | Ejecuta consultas repetitivas a la base de datos dentro de un bucle para obtener datos de cortesía y genera HTML en backend |
