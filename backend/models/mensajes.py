from sqlalchemy import String, DateTime, Text
from sqlalchemy.orm import Mapped, mapped_column
from database import Base
import uuid
from datetime import datetime

class MensajeLog(Base):
    __tablename__ = "mensajes_log"
    
    # Campos de la clave primaria
    id: Mapped[uuid.UUID] = mapped_column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    
    # Campos de la tabla
    mensaje: Mapped[str] = mapped_column(Text, nullable=False)
    status: Mapped[str] = mapped_column(String, default='sent')
    
    # Datos de fecha auto agragadas
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)