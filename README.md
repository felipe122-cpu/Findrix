# Findrix
# 👥 Integrantes
- Jhoan Felipe Hernandez Murcia
- 
- 
- 

# 🎯 Descripción
Breve descripción clara del sistema.
Ejemplo:
Sistema web full stack para la gestión de [inventarios / logística / usuarios], que permite optimizar procesos mediante una aplicación cliente-servidor.

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
MySQL

# 🗄️ Modelo de Datos


# 🧱 Arquitectura


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
La documentación se encuentra en la carpeta /docs:
Contexto
Problema
Requisitos
Modelo de datos
Arquitectura

# 📈 Estado del Proyecto
# 🚧 En desarrollo

# 🚀 Futuras Mejoras
Roles avanzados
Seguridad (JWT)
Despliegue en la nube

# 📜 Licencia
Uso académico - SENA

---
# 📄 PLANTILLA docs/03_requisitos.md

# 📋 Requisitos del Sistema

## ✅ Requisitos Funcionales

- RF01: El sistema debe permitir el registro de usuarios  
- RF02: El sistema debe permitir iniciar sesión  
- RF03: El sistema debe gestionar información  

---

## ⚙️ Requisitos No Funcionales

- RNF01: El sistema debe ser responsive  
- RNF02: Tiempo de respuesta menor a 3 segundos  
- RNF03: Seguridad en autenticación
