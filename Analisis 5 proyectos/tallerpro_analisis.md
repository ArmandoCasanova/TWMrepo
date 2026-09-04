# Revisión del proyecto: TallerPro

Este documento es una revisión general del proyecto TallerPro, con el propósito de analizar su estructura, archivos, patrones de código e identificar todas las problemáticas presentes.

---

## 1. Patrones presentes

- Definición manual de clases para aplicar el patrón Cadena de Responsabilidad al procesar peticiones en lugar de utilizar middlewares nativos de Express.
- Construcción y concatenación directa de cadenas HTML dentro de los controladores en Node.js sin usar plantillas.
- Parseo manual de encabezados de cookies sin firmas de seguridad y almacenamiento de contraseñas en texto claro.

---

## 2. Problemas por archivo

| Archivo | Tipo | Categoría | Problema |
| --- | --- | --- | --- |
| `SISTEMA.txt` | ALTA | Documentación | La documentación es incoherente porque menciona una clínica dental y citas médicas en lugar de un taller mecánico |
| `app.js` | CRÍTICA | Seguridad | Tiene la clave de sesión insegura y las credenciales de la base de datos expuestas en el código principal |
| `app.js` | CRÍTICA | Seguridad | Presenta inyección SQL en el inicio de sesión al concatenar correo y contraseña en la consulta |
| `app.js` | CRÍTICA | Seguridad | Asigna la sesión de administrador basándose en la lectura de una cookie del navegador |
| `app.js` | ALTA | Seguridad | Almacena las contraseñas del personal en texto plano sin aplicar técnicas de cifrado |
| `Handler.js` | MEDIA | Arquitectura | Usa clases caseras para manejar la cadena de responsabilidad en lugar de los middlewares estándar de Express |
| `app.js` | CRÍTICA | Seguridad | Presenta inyección SQL al procesar órdenes de trabajo, actualizar inventarios y asignar mecánicos |
| `app.js` | ALTA | Arquitectura | Ejecuta el proceso de cobro bancario y envío de correos de manera síncrona durante la petición |
| `app.js` | ALTA | Rendimiento | Realiza peticiones HTTP en bucle a endpoints locales para cargar datos de la página principal |
| `app.js` | MEDIA | Rendimiento | Ejecuta una consulta SQL individual dentro de un bucle para obtener el nombre de cada refacción en el inventario |
| `app.js` | CRÍTICA | Seguridad | Presenta inyección SQL en la entrega de órdenes mediante parámetros de la URL sin validar |
| `app.old.js` | BAJA | Código Muerto | Es una copia antigua del archivo principal abandonada en el proyecto |
