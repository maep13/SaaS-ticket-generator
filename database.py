from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Base para definir modelos
Base = declarative_base()

# Modelo de la tabla Ticket
class Ticket(Base):
    __tablename__ = "tickets"  # Nombre de la tabla en la base de datos

    id = Column(Integer, primary_key=True, index=True)  # ID único
    user_id = Column(Integer, nullable=False)          # ID del usuario
    description = Column(String, nullable=False)       # Descripción del ticket
    created_at = Column(DateTime, default=datetime.utcnow)  # Fecha y hora automática

    # Nuevas columnas para futuros microservicios
    category = Column(String, nullable=True)           # Categoría del ticket (opcional)
    priority = Column(String, nullable=True)           # Prioridad del ticket (opcional)

# URL de conexión a la base de datos
DATABASE_URL = "postgresql://user:password@localhost:5432/soporte_tecnico"

# Motor de la base de datos
engine = create_engine(DATABASE_URL)

# Configuración de la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Creación de las tablas en la base de datos
def init_db():
    Base.metadata.create_all(bind=engine)
