from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from ..conexion_bd import get_session
from ..modelos.ingreso import Ingreso
from ..modelos.usuarios import Usuario
from ..modelos.categorias import Categoria
from ..schemas.ingresos import (IngresoCreate,IngresoUpdate,IngresoRead)

router_ingresos = APIRouter(prefix="/ingresos",tags=["Ingresos"])


@router_ingresos.get("/", response_model=list[IngresoRead])
def listar(session: Session = Depends(get_session)):
    return session.exec(select(Ingreso)).all()


@router_ingresos.get("/{id}", response_model=IngresoRead)
def obtener(id: int, session: Session = Depends(get_session)):
    ingreso = session.get(Ingreso, id)
    if not ingreso:
        raise HTTPException(404, "Ingreso no encontrado")
    return ingreso


@router_ingresos.post("/", response_model=IngresoRead, status_code=201)
def crear(datos: IngresoCreate,session: Session = Depends(get_session)):
    if datos.monto <= 0:
        raise HTTPException(400,"El monto debe ser mayor que cero")
    usuario = session.get(Usuario, datos.usuario_id)
    if not usuario:
        raise HTTPException(404,"Usuario no existe")
    categoria = session.get(Categoria, datos.categoria_id)
    if not categoria:
        raise HTTPException(404,"Categoría no existe")
    ingreso = Ingreso.model_validate(datos)
    session.add(ingreso)
    session.commit()
    session.refresh(ingreso)
    return ingreso


@router_ingresos.put("/{id}", response_model=IngresoRead)
def actualizar( id: int, datos: IngresoUpdate, session: Session = Depends(get_session)
):
    ingreso = session.get(Ingreso, id)
    if not ingreso:
        raise HTTPException(404, "Ingreso no encontrado")
    cambios = datos.model_dump(exclude_unset=True)
    for campo, valor in cambios.items():
        setattr(ingreso, campo, valor)
    session.add(ingreso)
    session.commit()
    session.refresh(ingreso)
    return ingreso


@router_ingresos.delete("/{id}")
def eliminar(id: int, session: Session = Depends(get_session)):
    ingreso = session.get(Ingreso, id)
    if not ingreso:
        raise HTTPException(404, "Ingreso no encontrado")
    session.delete(ingreso)
    session.commit()
    return {"mensaje": "Ingreso eliminado correctamente"}