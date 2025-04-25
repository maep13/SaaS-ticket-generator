# Generador de Tickets con Microservicios

## Descripción
Este proyecto implementa un sistema generador de tickets utilizando arquitectura de microservicios. El objetivo es garantizar la escalabilidad, mantenibilidad y automatización del proceso, además de integrar funcionalidades de asignación de prioridades y clasificación de categorías.

## Componentes del Proyecto
- **Microservicio de Generación de Tickets**: Maneja la creación de tickets, incluyendo campos esenciales como descripción, prioridad y categoría.
- **Microservicio de Gestión de Prioridades**: Asigna prioridades mediante algoritmos dinámicos y comunica datos al microservicio de generación.
- **Microservicio de Asignación de Categorías**: Permite asignar categorías a los tickets basándose en la información almacenada en la base de datos. Proporciona endpoints para obtener y asociar categorías.
- **Base de Datos**: Utiliza PostgreSQL para almacenamiento de categorías y detalles de los tickets.
- **Integración**: Los microservicios se comunican mediante endpoints API, diseñados con FastAPI y probados con Postman.

## Pasos Implementados
1. **Diseño de la Arquitectura**: Planeación de la interacción entre los microservicios.
2. **Configuración de la Base de Datos**: Instalación y setup de PostgreSQL para la gestión de categorías.
3. **Desarrollo con FastAPI**: Creación de endpoints para operaciones CRUD en los microservicios.
4. **Validación de Datos**: Uso de Pydantic para asegurar la consistencia en las entradas del sistema.
5. **Pruebas y Debugging**: Implementación de pruebas con Postman y solución de problemas de conectividad entre microservicios y la base de datos.
6. **Documentación**: Elaboración de README.md detallado para la presentación y uso del proyecto.

## Cómo Usar
1. Instalar dependencias:
    ```bash
    pip install -r requirements.txt
    ```
2. Configurar la base de datos PostgreSQL.
3. Iniciar los microservicios con:
    ```bash
    uvicorn nombre_microservicio:app --reload
    ```
4. Probar los endpoints con Postman o similar.

## Tecnologías Utilizadas
- **Lenguaje**: Python
- **Framework**: FastAPI
- **Base de Datos**: PostgreSQL
- **Validación**: Pydantic
- **Pruebas**: Postman

## Próximos Pasos
- Incorporar autenticación para la seguridad del sistema.
- Implementar orquestación con herramientas como Airflow para procesos más complejos.
- Evaluar opciones de procesamiento en tiempo real con Kafka.