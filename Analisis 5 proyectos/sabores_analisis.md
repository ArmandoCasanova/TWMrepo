# Revisión del proyecto: Sabores

Este documento es una revisión general del proyecto Sabores, con el propósito de analizar su estructura, archivos, patrones de código e identificar todas las problemáticas presentes.

---

## 1. Patrones presentes

- Duplicación del sistema de ruteador oficial de Laravel mediante un controlador casero que intenta procesar peticiones manualmente.
- Existencia de middlewares de autorización creados pero huérfanos sin asignación en la configuración o rutas.
- Inserción masiva de SQL crudo e impresión directa de código JavaScript en las respuestas del servidor.

---

## 2. Problemas por archivo

| Archivo | Tipo | Categoría | Problema |
| --- | --- | --- | --- |
| `LEAME_ARQUITECTO.txt` | ALTA | Documentación | La documentación es incoherente porque habla de un sistema de censo bovino y ganado en lugar de pedidos de comida |
| `.env` | CRÍTICA | Seguridad | Expone credenciales de la base de datos en texto plano en el archivo de configuración del entorno |
| `FrontController.php` | MEDIA | Arquitectura | Contiene un controlador casero que intenta procesar las rutas manualmente duplicando el sistema propio de Laravel |
| `LoginController.php` | CRÍTICA | Seguridad | Presenta inyección SQL en la consulta de autenticación por concatenación de parámetros del usuario |
| `LoginController.php` | CRÍTICA | Seguridad | Otorga permisos de administración a través de una cookie editable desde el cliente |
| `HomeController.php` | ALTA | Rendimiento | Realiza lectura síncrona de archivos HTTP locales en bucle lo que ralentiza la carga del sistema |
| `HomeController.php` | MEDIA | Rendimiento | Hace una consulta SQL individual para contar platillos por cada restaurante dentro de un bucle |
| `PedidoController.php` | CRÍTICA | Seguridad | Presenta inyección SQL al calcular precios y guardar el pedido además de obtener el identificador mediante el valor máximo |
| `PedidoController.php` | ALTA | Arquitectura | Envía correos y peticiones a pasarelas de pago de manera síncrona durante la petición web |
| `PedidoController.php` | MEDIA | Diseño Web | Envía respuestas al navegador mediante mensajes emergentes de JavaScript en lugar de redirecciones |
| `SoloRepartidor.php` | MEDIA | Configuración | El middleware de restricción de rol fue creado pero no se asignó a ninguna ruta de la aplicación |
| `ResenaController.php` | ALTA | Seguridad | Presenta inyección SQL al insertar comentarios y calificaciones en la base de datos |
