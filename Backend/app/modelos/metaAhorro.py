from typing import Optional
from sqlmodel import SQLModel
from sqlmodel import Field


class Meta(SQLModel, table=True):

    __tablename__ = "metas"

    id: Optional[int] = Field(
        default=None,
        primary_key=True
    )

    nombre: str

    objetivo: float

    ahorrado: float = 0

    usuario_id: int