from fastapi import FastAPI, HTTPException

# Instancia de FastAPI
priority_service = FastAPI()

# Base de datos simulada para guardar prioridades asignadas (puedes reemplazar esto con una base de datos real)
priority_db = []

# Endpoint raíz para verificar el estado del microservicio
@priority_service.get("/")
def root():
    return {"message": "Microservicio para asignar prioridades funcionando correctamente"}

# Endpoint para asignar prioridad
@priority_service.post("/assign_priority/")
def assign_priority(data: dict):
    try:
        category = data.get("category", "")
        description = data.get("description", "").lower()

        # Asignación de prioridad basada en categoría y descripción
        if category in ["Seguridad", "Soporte técnico"] or "urgente" in description:
            priority = "Alta"
        elif category == "Finanzas":
            priority = "Media"
        else:
            priority = "Baja"

        # Simular almacenamiento en una lista
        priority_db.append({
            "description": description,
            "category": category,
            "priority": priority
        })

        return {"priority": priority}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al asignar prioridad: {e}")

# Endpoint para obtener todas las prioridades asignadas
@priority_service.get("/priorities/")
def get_priorities():
    if not priority_db:
        raise HTTPException(status_code=404, detail="No se encontraron prioridades asignadas.")
    return {"priorities": priority_db}