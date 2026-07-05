from typing import Optional
from sqlmodel import SQLModel


class MetaCreate(SQLModel):
    nombre: str
    objetivo: float
    ahorrado: float
    usuario_id: int


class MetaUpdate(SQLModel):
    nombre: Optional[str] = None
    objetivo: Optional[float] = None
    ahorrado: Optional[float] = None
    usuario_id: Optional[int] = None


class MetaRead(SQLModel):
    id: int
    nombre: str
    objetivo: float
    ahorrado: float
    usuario_id: int