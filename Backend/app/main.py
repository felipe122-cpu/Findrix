from fastapi import FastAPI
from .conexion_bd import crear_bd
from .enrutadores import categorias,cursos,gastos,ingresos,presupuesto,usuarios,metaAhorro
from .enrutadores.categorias import router_categorias
from .enrutadores.cursos import router_cursos
from .enrutadores.gastos import router_gastos
from .enrutadores.ingresos import router_ingresos
from .enrutadores.presupuesto import router_presupuestos
from .enrutadores.usuarios import router_usuarios
from .enrutadores.metaAhorro import router_metasAhorro

app = FastAPI(title="Findrix API")

@app.on_event("startup")
def startup():
    crear_bd()

app.include_router(usuarios.router_usuarios)
app.include_router(metaAhorro.router_metasAhorro)
app.include_router(presupuesto.router_presupuestos)
app.include_router(ingresos.router_ingresos)
app.include_router(gastos.router_gastos)
app.include_router(cursos.router_cursos)
app.include_router(categorias.router_categorias)


