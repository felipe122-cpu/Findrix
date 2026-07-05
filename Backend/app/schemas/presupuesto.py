from typing import Optional
from sqlmodel import SQLModel


class PresupuestoCreate(SQLModel):
    nombre: str
    limite: float
    usuario_id: int


class PresupuestoUpdate(SQLModel):
    nombre: Optional[str] = None
    limite: Optional[float] = None
    usuario_id: Optional[int] = None


class PresupuestoRead(SQLModel):
    id: int
    nombre: str
    limite: float
    usuario_id: int