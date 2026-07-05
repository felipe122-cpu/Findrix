from typing import Optional
from datetime import date
from sqlmodel import SQLModel


class GastoCreate(SQLModel):
    descripcion: str
    monto: float
    fecha: date
    usuario_id: int
    categoria_id: int


class GastoUpdate(SQLModel):
    descripcion: Optional[str] = None
    monto: Optional[float] = None
    fecha: Optional[date] = None
    usuario_id: Optional[int] = None
    categoria_id: Optional[int] = None


class GastoRead(SQLModel):
    id: int
    descripcion: str
    monto: float
    fecha: date
    usuario_id: int
    categoria_id: int