from typing import Optional

from sqlmodel import SQLModel
from sqlmodel import Field


class Categoria(SQLModel, table=True):

    __tablename__ = "categorias"

    id: Optional[int] = Field(
        default=None,
        primary_key=True
    )

    nombre: str

    tipo: str