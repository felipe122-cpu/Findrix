# 04. Modelo de Datos

Para el desarrollo del sistema **Findrix** se propone un modelo de datos relacional implementado en **PostgreSQL**. Este modelo permite organizar, almacenar y gestionar de forma estructurada y segura toda la información relacionada con usuarios, finanzas personales, metas de ahorro, presupuestos y notificaciones.

A continuación se detallan las entidades principales extraídas del diagrama del modelo de datos:

### Entidad Usuarios
Almacena la información principal de los usuarios de la plataforma.

**Atributos:**
- `Id_Usuario` (PK - int)
- `Pnombre` (nvarchar(50))
- `Snombre` (nvarchar(50))
- `Papellido` (nvarchar(50))
- `Sapellido` (nvarchar(50))
- `Fecha_Nacimiento` (Date)
- `Correo` (nvarchar(80) - único)
- `Contraseña` (nvarchar(20))
- `Conocimiento_financiero` (Enum: "Bajo", "Intermedio", "Avanzado")
- `Contraseña` (nvarchar(20))

### Entidad Movimientos
Registra todos los ingresos y gastos del usuario.

**Atributos:**
- `Id_Gastos` (PK - int)
- `Cod_Usuario` (FK)
- `Cantidad` (Float)
- `Fecha` (Date)
- `Descripcion` (nvarchar(50))
- `Ingreso` (Float)
- `Gasto` (Float)
- `Cod_Categoria` (FK)

### Entidad Categorias
Catálogo de categorías para clasificar movimientos y presupuestos.

**Atributos:**
- `Id_Categoria` (PK - int)
- `Cod_Usuario` (FK)
- `Nombre` (nvarchar(50) - NOT NULL)
- `Descripcion` (nvarchar(100))

### Entidad Presupuesto
Gestiona los presupuestos mensuales del usuario.

**Atributos:**
- `Id_Presupuesto` (PK - int)
- `Cod_Usuario` (FK)
- `Cod_Categoria` (FK)
- `Nombre` (nvarchar(50))
- `Fecha_Inicio` (Date)
- `Fecha_Fin` (Date)

### Entidad Meta_Ahorro
Define las metas de ahorro del usuario.

**Atributos:**
- `Id_MetaAhorro` (PK - int)
- `Cod_Usuario` (FK)
- `Nombre_Meta` (nvarchar(50))
- `Fecha_Inicio` (Date)
- `Fecha_Limite` (Date)
- `Dinero_Acumulado` (Float)
- `Objetivo_Ahorro` (Float)
- `Activo` (BIT)

### Entidad Historial_Ahorro
Registra el historial de movimientos en las metas de ahorro.

**Atributos:**
- `Id_Historial` (PK - int)
- `Cod_MetaAhorro` (FK)
- `Fecha` (Date)
- `Movimientos` (nvarchar(100))
- `Cantidad_Ahorro` (Float)

### Entidad Ocupacion
Registra la ocupación laboral o profesional del usuario.

**Atributos:**
- `Id_Ocupacion` (PK - int)
- `Cod_Usuario` (FK)
- `Cargo` (nvarchar(20))

### Entidad Notificacion
Gestiona las notificaciones del sistema para el usuario.

**Atributos:**
- `Id_Notificacion` (PK - int)
- `Cod_Usuario` (FK)
- `Frecuencia` (nvarchar(20))
- `Gastos_Diarios` (nvarchar(50))
- `Hora` (Time)
- `Ultimo_Envio` (nvarchar(30))
- `Activo` (BIT)

## Relaciones Principales

- Un **Usuario** puede tener múltiples **Movimientos**, **Presupuestos**, **Meta_Ahorro**, **Notificaciones** y una **Ocupacion**.
- Un **Movimiento** pertenece a un **Usuario** y a una **Categoria**.
- Una **Meta_Ahorro** tiene un historial en **Historial_Ahorro**.
- Un **Presupuesto** está relacionado con un **Usuario** y una **Categoria**.
- Las **Categorias** pueden ser personales (por usuario).

Este modelo garantiza la integridad de los datos, soporta el control financiero y el seguimiento de metas, y permite escalabilidad futura del sistema Findrix.
