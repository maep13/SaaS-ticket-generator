from fastapi import FastAPI
from microservicios.ingreso_incidencias import ingreso_incidencias
from microservicios.categories_database import asignar_categorias
from microservicios.priority_database import priority_service  

# Instancia principal de FastAPI
app = FastAPI(
    title="Sistema de Tickets",
    description="Aplicación que integra los microservicios de ingreso de incidencias, asignación de categorías y prioridades.",
    version="1.0.0"
)

# Montar el microservicio de ingreso de incidencias
app.mount("/ingreso_incidencias", ingreso_incidencias)

# Montar el microservicio de asignación de categorías
app.mount("/asignar_categorias", asignar_categorias)

# Montar el microservicio de asignación de prioridades
app.mount("/prioridades", priority_service)

# Punto de entrada para ejecutar el servidor
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)