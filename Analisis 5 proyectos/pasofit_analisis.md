# Revisión del proyecto: PasoFit

Este documento es una revisión general del proyecto PasoFit, con el propósito de analizar su estructura, archivos, patrones de código e identificar todas las problemáticas presentes.

---

## 1. Patrones presentes

- Uso de buses de eventos estáticos con listas de escuchas que nunca se liberan, provocando fugas de memoria.
- Mezcla de la interfaz de usuario con la capa de datos al ejecutar llamadas a servidor y a SQLite directamente en las pantallas.
- Invocaciones a controladores de navegación durante la inicialización de widgets que rompen su ciclo de vida.

---

## 2. Problemas por archivo

| Archivo | Tipo | Categoría | Problema |
| --- | --- | --- | --- |
| `ARQUITECTURA.md` | ALTA | Documentación | La documentación es incoherente porque habla de una banca móvil corporativa en lugar de la aplicación de fitness |
| `oyentes.dart` | CRÍTICA | Rendimiento | Utiliza buses de eventos estáticos con listas de escuchas que nunca se liberan provocando fugas de memoria |
| `login.dart` | ALTA | Seguridad | Envía credenciales a través de peticiones HTTP no seguras y sin cifrado |
| `inicio.dart` | ALTA | Desarrollo | Invoca datos de navegación durante la inicialización de la pantalla provocando fallos en el ciclo de vida |
| `inicio.dart` | MEDIA | Seguridad | Realiza una comprobación de sesión ineficiente que permite ingresar a la pantalla sin estar autenticado |
| `rutina.dart` | CRÍTICA | Seguridad | Ejecuta consultas a la base de datos SQLite con variables concatenadas expuesto a inyección SQL local |
| `rutina.dart` | MEDIA | Arquitectura | Tiene cálculos de calorías hardcodeados con condicionales dentro de la interfaz gráfica |
| `cronometro.dart` | ALTA | Rendimiento | El temporizador se ejecuta de forma continua en segundo plano y nunca se detiene al salir de la pantalla |
| `peso.dart` | MEDIA | Calidad de Código | Resta peso de forma automática en código cada vez que se guarda un registro |
| `logros.dart` | ALTA | Rendimiento | Ejecuta múltiples consultas a SQLite dentro de un bucle para calcular los logros del usuario |
| `rutina_old.dart` | BAJA | Código Muerto | Es un archivo en desuso que solo contiene un texto informativo sin funcionalidad real |
