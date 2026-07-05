from typing import Optional

from sqlmodel import SQLModel
from sqlmodel import Field


class Presupuesto(SQLModel, table=True):

    __tablename__ = "presupuestos"

    id: Optional[int] = Field(
        default=None,
        primary_key=True
    )

    nombre: str

    limite: float

    usuario_id: int