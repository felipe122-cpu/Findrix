# Findrix
# 👥 Integrantes
- Jhoan Felipe Hernandez Murcia
- Juan Sebastián Angulo Pérez
- María Camila Niño Salamanca
- Yeimy Alejandra Padilla 



---
# 🎯 Descripción
Aplicativo web full stack para para la gestión de finanzas personales, que permite optimizar el control de ingresos, gastos y ahorros mediante una aplicación cliente-servidor con acompañamiento de un bot financiero.

# 🧩 Problema
A algunas personas se les dificulta organizar sus finanzas personales, lo cual genera:
- Inestabilidad económica.
- Falta de control sobre ingresos, gastos y ahorros.
- Desorden o pérdida de información financiera.
- Dificultad para tomar decisiones económicas. 

# 💡 Solución Propuesta
Se propone el desarrollo de un aplicativo web full stack denominado "Findrix" , el cual permitirá gestionar tareas de manera centralizada mediante:
- Frontend: Interfaz basada en WhatsApp como canal de apoyo e interacción complementaria, junto con una página web informativa que explica el funcionamiento del proyecto.
- Backend: API REST desarrollada en Node.js con Express para la lógica del sistema y gestión del bot como asistente financiero.
- Base de Datos: PGSQL para el almacenamiento y administración de la información financiera de los usuarios. 

# ⚙️ Tecnologías
# Frontend
React
HTML5 / CSS3
JavaScript
# Backend
Node.js
Express
# Base de Datos
PgSQL

# 🗄️ Modelo de Datos


# 🧱 Arquitectura
Monolítico de 3 capas 
1. Capa de Presentación (Interfaz)
Es la parte que ve y utiliza el usuario.

• Formularios para registrar ingresos y gastos.
• Pantallas para ver el presupuesto disponible.
• Tablas con los movimientos financieros.
• Botones para agregar, editar o eliminar registros.

2. Capa de Lógica de Negocio
Aquí se procesan las reglas del sistema.

• Validar que el monto sea mayor que cero.
• Calcular el saldo disponible.
• Determinar si el usuario excedió su presupuesto.
• Generar estadísticas de gastos e ingresos.

3. Capa de Datos
Es la encargada de almacenar y recuperar información de la base de datos.

• Guardar usuarios.
• Guardar ingresos y gastos.
• Consultar movimientos registrados.
• Actualizar o eliminar registros.



# 🚀 Instalación
1. Clonar repositorio
git clone https://github.com/[usuario]/[repositorio].git

2. Backend
cd backend
npm install
npm run dev

3. Frontend
cd frontend
npm install
npm start

# 🔐 Variables de Entorno
Crear archivo .env en /backend:
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=
DB_NAME=nombre_db
JWT_SECRET=secret_key

# 📂 Estructura del Proyecto
/docs → documentación  
/backend → API REST  
/frontend → aplicación React  
/database → scripts SQL  

# 📄 Documentación
- La documentación se encuentra en la carpeta /docs:
- Contexto
- Problema
- Inpacto del problema
- Solucción
- Impacto de la solución
- Alcance
- Requisitos
- Modelo de datos
- Arquitectura

# 📈 Estado del Proyecto
## 🚧 En desarrollo
..

## 🚀 Futuras Mejoras
Roles avanzados
Seguridad (JWT)
Despliegue en la nube
---
# 📜 Licencia
Uso académico - SENA
