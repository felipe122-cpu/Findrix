from typing import Optional

from sqlmodel import SQLModel
from sqlmodel import Field


class Curso(SQLModel, table=True):

    __tablename__ = "cursos"

    id: Optional[int] = Field(
        default=None,
        primary_key=True
    )

    titulo: str

    descripcion: str

    nivel: str