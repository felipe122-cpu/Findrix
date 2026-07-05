from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from ..conexion_bd import get_session
from ..modelos.gasto import Gasto
from ..modelos.usuarios import Usuario
from ..modelos.categorias import Categoria
from ..schemas.gastos import (GastoCreate,GastoUpdate,GastoRead)

router_gastos = APIRouter(prefix="/gastos",tags=["Gastos"])


@router_gastos.get("/", response_model=list[GastoRead])
def listar(session: Session = Depends(get_session)):
    return session.exec(select(Gasto)).all()


@router_gastos.get("/{id}", response_model=GastoRead)
def obtener(id: int, session: Session = Depends(get_session)):
    gasto = session.get(Gasto, id)
    if not gasto:
        raise HTTPException(404, "Gasto no encontrado")
    return gasto


@router_gastos.post("/", response_model=GastoRead, status_code=201)
def crear(datos: GastoCreate,session: Session = Depends(get_session)):
    if datos.monto <= 0:
        raise HTTPException(400,"El monto debe ser mayor que cero")
    usuario = session.get(Usuario, datos.usuario_id)
    if not usuario:
        raise HTTPException(404,"Usuario no encontrado")
    categoria = session.get(Categoria, datos.categoria_id)
    if not categoria:
        raise HTTPException(404,"Categoría no encontrada")
    gasto = Gasto.model_validate(datos)
    session.add(gasto)
    session.commit()
    session.refresh(gasto)
    return gasto


@router_gastos.put("/{id}", response_model=GastoRead)
def actualizar(id: int,datos: GastoUpdate,session: Session = Depends(get_session)):
    gasto = session.get(Gasto, id)
    if not gasto:
        raise HTTPException(404,"Gasto no encontrado")
    cambios = datos.model_dump(exclude_unset=True)
    for campo, valor in cambios.items():
        setattr(gasto, campo, valor)
    session.add(gasto)
    session.commit()
    session.refresh(gasto)
    return gasto


@router_gastos.delete("/{id}")
def eliminar(id: int,session: Session = Depends(get_session)):
    gasto = session.get(Gasto, id)
    if not gasto:
        raise HTTPException(404,"Gasto no encontrado")
    session.delete(gasto)
    session.commit()
    return {"mensaje": "Gasto eliminado correctamente"}