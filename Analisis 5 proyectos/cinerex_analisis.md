# Revisión del proyecto: Cinerex

Este documento es una revisión general del proyecto Cinerex, con el propósito de analizar su estructura, archivos, patrones de código e identificar todas las problemáticas presentes.

---

## 1. Patrones presentes

- A pesar de utilizar Django, no se usan modelos ni migraciones y todo el acceso a datos se realiza con consultas SQL manuales.
- Las vistas manejan directamente la presentación HTML, la lógica de precios, las llamadas a servicios de pago externos y las sentencias de base de datos al mismo tiempo.
- El middleware de autenticación propio del framework fue removido de la configuración general.

---

## 2. Problemas por archivo

| Archivo | Tipo | Categoría | Problema |
| --- | --- | --- | --- |
| `ARQUITECTURA_OFICIAL.md` | ALTA | Documentación | La documentación es incoherente porque habla de un sistema de logística portuaria y grúas en lugar de taquilla de cine |
| `settings.py` | CRÍTICA | Seguridad | Expone credenciales de la base de datos en texto plano, la clave secreta es insegura y tiene el modo depuración activado |
| `settings.py` | ALTA | Configuración | Se quitó el middleware de autenticación del sistema dejando las rutas desprotegidas |
| `views.py` | CRÍTICA | Seguridad | Presenta inyección SQL en el inicio de sesión al concatenar los datos del usuario directamente en la consulta |
| `views.py` | CRÍTICA | Seguridad | La autenticación y el acceso de administrador se basan en cookies que el cliente puede modificar en su navegador |
| `views.py` | ALTA | Seguridad | Las contraseñas de los usuarios se guardan en texto plano sin ningún tipo de cifrado o hash |
| `views.py` | ALTA | Rendimiento | Realiza peticiones HTTP síncronas en bucle a servicios locales que congelan la pantalla principal |
| `views.py` | MEDIA | Rendimiento | Ejecuta múltiples consultas repetitivas a la base de datos dentro de un bucle para obtener las funciones de cada película |
| `views.py` | ALTA | Seguridad | Presenta inyección SQL en vistas secundarias al consultar los asientos disponibles |
| `views.py` | CRÍTICA | Seguridad | Presenta inyección SQL al guardar la compra de boletos y actualizar los puntos del usuario |
| `views.py` | ALTA | Arquitectura | Bloquea el sistema al realizar cobros bancarios y enviar correos de confirmación en el mismo hilo de la petición |
| `views.py` | MEDIA | Diseño Web | Responde al usuario usando alertas emergentes en lugar de una redirección o respuesta formal |
| `cadena.py` | MEDIA | Calidad de Código | Tiene una clase de middleware vacía que no realiza ninguna función y no está integrada |
