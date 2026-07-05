from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from ..conexion_bd import get_session
from ..modelos.presupuesto import Presupuesto
from ..modelos.usuarios import Usuario
from ..schemas.presupuesto import (PresupuestoCreate,PresupuestoUpdate,PresupuestoRead)

router_presupuestos = APIRouter(prefix="/presupuestos",tags=["Presupuestos"])


@router_presupuestos.get("/", response_model=list[PresupuestoRead])
def listar_presupuestos(session: Session = Depends(get_session)):
    return session.exec(select(Presupuesto)).all()


@router_presupuestos.get("/{id}", response_model=PresupuestoRead)
def obtener_presupuesto(id: int, session: Session = Depends(get_session)):
    presupuesto = session.get(Presupuesto, id)
    if presupuesto is None:
        raise HTTPException(status_code=404,detail="Presupuesto no encontrado")
    return presupuesto


@router_presupuestos.post("/", response_model=PresupuestoRead, status_code=status.HTTP_201_CREATED)
def crear_presupuesto(datos: PresupuestoCreate,session: Session = Depends(get_session)):
    usuario = session.get(Usuario, datos.usuario_id)
    if usuario is None:
        raise HTTPException(status_code=404,detail="El usuario no existe")
    if datos.limite <= 0:
        raise HTTPException(status_code=400,detail="El límite debe ser mayor que cero")
    presupuesto = Presupuesto.model_validate(datos)
    session.add(presupuesto)
    session.commit()
    session.refresh(presupuesto)
    return presupuesto


@router_presupuestos.put("/{id}", response_model=PresupuestoRead)
def actualizar_presupuesto(id: int,datos: PresupuestoUpdate,session: Session = Depends(get_session)):
    presupuesto = session.get(Presupuesto, id)
    if presupuesto is None:
        raise HTTPException(status_code=404,detail="Presupuesto no encontrado")
    cambios = datos.model_dump(exclude_unset=True)
    for campo, valor in cambios.items():
        setattr(presupuesto, campo, valor)
    session.add(presupuesto)
    session.commit()
    session.refresh(presupuesto)
    return presupuesto


@router_presupuestos.delete("/{id}")
def eliminar_presupuesto(id: int,session: Session = Depends(get_session)):
    presupuesto = session.get(Presupuesto, id)
    if presupuesto is None:
        raise HTTPException(status_code=404,detail="Presupuesto no encontrado")
    session.delete(presupuesto)
    session.commit()
    return {"mensaje": "Presupuesto eliminado correctamente"}