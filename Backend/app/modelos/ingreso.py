from typing import Optional
from datetime import date

from sqlmodel import SQLModel
from sqlmodel import Field


class Ingreso(SQLModel, table=True):

    __tablename__ = "ingresos"

    id: Optional[int] = Field(
        default=None,
        primary_key=True
    )

    descripcion: str

    monto: float

    fecha: date

    usuario_id: int

    categoria_id: int