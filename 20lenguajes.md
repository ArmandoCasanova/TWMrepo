# Lenguajes de programación, sus paradigmas y patrones

##    1 Python: 
-   Paradigma: Multiparadigma (POO, imperativo, funcional)
-   Patrón: MVT (Model-View-Template) / Decorador
-   Frameworks derivados derivados: Django, Flask, FastAPI, Flet
##   2 JavaScript:
-   Paradigma: Multiparadigma (eventos, funcional, prototipos)
-   Patrón: Observer / Pub-Sub
-   Frameworks derivados: React, Angular, Vue, Express
##  3 Java:
-   Paradigma: POO, estructurado
-   Patrón: Singleton / Inyección de Dependencias
-   Frameworks derivados: Spring Boot, Jakarta EE, Quarkus
##   4 C##:
-   Paradigma: Multiparadigma (POO, funcional, reactivo)
-   Patrón: MVVM / Repository
-   Frameworks derivados: NET (ASPNET Core), Blazor, Unity
##   5 C++:
-   Paradigma: Multiparadigma (POO, procedural, genérico)
-   Patrón: RAII (Resource Acquisition Is Initialization)
-   Frameworks derivados: Qt, Unreal Engine, Boost
##   6 Go (Golang):
-   Paradigma: Concurrente, imperativo
-   Patrón: CSP (Communicating Sequential Processes)
-   Frameworks derivados: Gin, Fiber, Echo
##   7 Rust:
-   Paradigma: Multiparadigma (imperativo, funcional, concurrente seguro)
-   Patrón: Type State / Builder
-   Frameworks derivados: Actix-web, Axum, Tauri
##   8 PHP:
-   Paradigma: Multiparadigma (POO, imperativo)
-   Patrón: MVC / Active Record
-   Frameworks derivados: Laravel, Symfony, CodeIgniter
##   9 Ruby:
-   Paradigma: Multiparadigma (POO pura, funcional)
-   Patrón: Active Record / Convención sobre Configuración
-   Frameworks derivados: Ruby on Rails, Sinatra
##   10 Swift:
-   Paradigma: Multiparadigma (POO, orientado a protocolos)
-   Patrón: Delegation (Delegación<)
-   Frameworks derivados: SwiftUI, UIKit, vapor
##   11 Kotlin:
-   Paradigma: Multiparadigma (POO, funcional)
-   Patrón: Builder / Concurrencia Estructurada
-   Frameworks derivados: Ktor, Spring Boot, Compose
##   12 TypeScript:
-   Paradigma: Multiparadigma (POO estático, funcional)
-   Patrón: Inyección de Dependencias / Decorador
-   Frameworks derivados: NestJS, Angular, Nextjs
##   13 Scala:
-   Paradigma: Multiparadigma (POO pura + Funcional pura)
-   Patrón: Cake Pattern / Monad
-   Frameworks derivados: Play Framework, Akka, Apache Spark
##   14 Elixir:
-   Paradigma: Funcional, concurrente, distribuido
-   Patrón: Actor Model (Modelo de Actores)
-   Frameworks derivados: phoenix, nerves
##   15 Haskell:
-   Paradigma: Funcional puro, perezoso (lazy)
-   Patrón: Monads / Typeclasses
-   Frameworks derivados: yesod, servant, scotty
##   16 Dart:
-   Paradigma: Multiparadigma (POO basada en clases, funcional)
-   Patrón: BLoC (Business Logic Component)
-   Frameworks derivados: flutter, shelf
##   17 R:
-   Paradigma: Multiparadigma (funcional, procedural, arreglos)
-   Patrón: Pipeline (Tubería) / Vectorización
-   Frameworks derivados: shiny, tidyverse, plumber
##   18 C:
-   Paradigma: Imperativo, procedural
-   Patrón: Opaque Pointer / State Machine
-   Frameworks derivados: GTK, Kernel de Linux
##   19 Lua:
-   Paradigma: Procedural, funcional, orientado a prototipos
-   Patrón: Sandboxing / Coroutines
-   Frameworks derivados: Love2D, OpenResty
##   20 Clojure:
-   Paradigma: Funcional, concurrente (dialecto Lisp)
-   Patrón: STM (Software Transactional Memory) / Transducers
-   Frameworks derivados: ring, reagent, luminus


# Análisis de lenguajes
Los paradigmas más populares son los multiparadigma ya que nos permiten combinar programación orientada a objetos, imperativa y funcional según nuestras necesidades. Entre los patrones más utilizados son MVC/MVT, Observer, Inyección de Dependencias, Repository, Builder y Active Record, los cuales nos ayudan a organizar el código, separar responsabilidades y facilitar el mantenimiento, aunque su uso depende del problema que se quiera resolver y del lenguaje utilizado

- Necesidad de patrones de diseño 
No siempre es necesario aplicar un patrón de diseño, especialmente en proyectos pequeños donde puede hacer que el código sea más complicado, además algunos lenguajes tienen características que hacen que ciertos patrones tradicionales no encajen bien por ejemplo, Rust limita el estado mutable compartido, mientras que Go utiliza composición e interfaces en lugar de herencia tradicional


## Paradigmas que rompen 
Hay algunos lenguajes donde sus paradigmas rompen con muchos patrones de diseño tracionales como los siguientes
- Rust 
En rust, la regla estricta de una sola referencia mutable o múltiples inmutables rompe directamente patrones como Observer o arquitecturas con estado mutable compartido entre múltiples entidades, obligando a usar wrappers en tiempo de ejecución (Rc/Arc, RefCell/Mutex) para poder representarlos

- Go
No tiene herencia de clases tradicional y polimorfismo basado en subtipado así que se rompen patrones como Template Method, forzando el uso exclusivo de interfaces implícitas y composición estructural que alteran la mecánica del patrón original

- Haskell / Elixir / Clojure
La ausencia de mutación directa rompe patrones de comportamiento clásicos (como State, Command o Iterator basados en mutación in-place), exigiendo pasar y retornar explícitamente nuevos estados o recurrir a mónadas y actores aislados

- C
Ya que no cuenta con soporte sintáctico ni validación estática de encapsulamiento y polimorfismo, el emular patrones como Factory o Strategy exige el uso manual de punteros a funciones y void*, rompiendo la seguridad de tipos (type safety) en tiempo de compilación

- TypeScript
Dado que los tipos no existen en tiempo de ejecución, algunos contenedores no pueden resolver dependencias basándose en interfaces nativas y esto fuerza la dependencia de metadatos experimentales o decoradores propietarios para que el patrón funcione