from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
import requests  # Para comunicarse con el microservicio de asignación

# Instancia de FastAPI
ingreso_incidencias = FastAPI()

# Modelo para validar la entrada de datos
class TicketInput(BaseModel):
    user_id: int
    description: str

# Endpoint raíz para verificar el estado del microservicio
@ingreso_incidencias.get("/")
def root():
    return {"message": "Microservicio funcionando correctamente"}

# Endpoint para recibir los datos del ticket y enviarlos para asignar categoría y guardar
@ingreso_incidencias.post("/tickets/")
def process_ticket(ticket: TicketInput):
    try:
        # Enviar datos al microservicio de asignación y registro
        response = requests.post(
            "http://127.0.0.1:8001/assign_and_register/",
            json=ticket.dict()
        )
        if response.status_code != 200:
            raise Exception(f"Error al procesar el ticket: {response.text}")
        return response.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al enviar el ticket: {e}")