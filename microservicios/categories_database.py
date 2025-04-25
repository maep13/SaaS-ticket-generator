from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import Ticket, SessionLocal
import requests  # Para comunicarse con el microservicio de prioridades
from pydantic import BaseModel

# Instancia de FastAPI
asignar_categorias = FastAPI()

# Función para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Modelo para recibir los datos del ticket
class TicketInput(BaseModel):
    user_id: int
    description: str

# Endpoint raíz para verificar el estado del microservicio
@asignar_categorias.get("/")
def root():
    return {"message": "Microservicio de categorías funcionando correctamente"}

# Endpoint para asignar categoría, enviar a prioridades y guardar el ticket
@asignar_categorias.post("/assign_and_register/")
def assign_and_register(ticket: TicketInput, db: Session = Depends(get_db)):
    try:
        # Asignación automática de categoría
        description = ticket.description
        if "error" in description.lower():
            category = "Soporte técnico"
        elif "pago" in description.lower():
            category = "Finanzas"
        elif "seguridad" in description.lower():
            category = "Seguridad"
        else:
            category = "General"

        # Enviar datos al microservicio de prioridades
        try:
            response = requests.post(
                "http://127.0.0.1:8002/assign_priority/",
                json={"description": description, "category": category}
            )
            if response.status_code != 200:
                raise Exception(f"Error en el microservicio de prioridad: {response.text}")
            priority = response.json().get("priority", "Sin prioridad")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"No se pudo conectar con priority_database: {e}")

        # Registrar el ticket con la categoría y prioridad asignadas
        new_ticket = Ticket(
            user_id=ticket.user_id,
            description=description,
            category=category,
            priority=priority  # Ahora incluye prioridad
        )
        db.add(new_ticket)
        db.commit()
        db.refresh(new_ticket)

        return {
            "message": "¡Ticket registrado con categoría y prioridad asignadas!",
            "ticket": {
                "id": new_ticket.id,
                "user_id": new_ticket.user_id,
                "description": new_ticket.description,
                "category": new_ticket.category,
                "priority": new_ticket.priority,
                "created_at": new_ticket.created_at
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al registrar el ticket: {e}")