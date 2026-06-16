# 05. Arquitectura

Para el desarrollo de **Findrix** se propone una arquitectura de tipo **cliente-servidor** basada en tres capas, la cual facilita la organización del sistema, mejora su mantenimiento y permite su escalabilidad a futuro.

## Arquitectura del Sistema

### Capa de Presentación (Frontend)

Corresponde a la interfaz gráfica con la que interactúan los usuarios del sistema. Su función principal es permitir la visualización de la información financiera y la interacción con las funcionalidades de gestión y aprendizaje.

**Tecnologías sugeridas:** HTML, CSS, JavaScript y frameworks como React.js o Vue.js. Se recomienda el uso de Tailwind CSS para un diseño moderno y responsive.

**Funciones principales:**
- Dashboard financiero con gráficos y resúmenes
- Registro e inicio de sesión de usuarios
- Gestión de transacciones, presupuestos y metas
- Módulo educativo gamificado (lecciones, quizzes y progreso)
- Visualización de niveles, rachas y estadísticas personales

### Capa de Lógica de Negocio (Backend)

Se encarga de procesar las solicitudes realizadas por los usuarios, aplicar las reglas de negocio y gestionar la comunicación entre la interfaz y la base de datos.

**Tecnologías sugeridas:** Python (con Flask o Django) mediante una API REST.

**Funciones principales:**
- Validación de datos y cálculos financieros
- Gestión de usuarios, niveles educativos y progreso
- Procesamiento de transacciones y control de presupuestos
- Sistema de gamificación (puntos, rachas y desbloqueos)
- Autenticación, seguridad y generación de reportes

### Capa de Datos (Base de Datos)

Es la encargada de almacenar toda la información del sistema de manera organizada y segura.

**Tecnología sugerida:** PostgreSQL.

**Funciones principales:**
- Almacenamiento seguro de datos financieros y educativos
- Consultas eficientes para dashboards y reportes
- Mantenimiento de la integridad y consistencia de los datos

## Flujo de Funcionamiento del Sistema

1. El usuario accede a la aplicación a través de la interfaz web.
2. Realiza una solicitud (por ejemplo: registrar un gasto, completar una lección o consultar su balance).
3. La solicitud es enviada al servidor mediante la API.
4. El backend procesa la información, aplica las reglas de negocio y consulta o actualiza la base de datos.
5. La respuesta es enviada de vuelta al frontend y se muestra al usuario en tiempo real.

## Patrón de Arquitectura Adicional

Se recomienda implementar el patrón **MVC (Modelo-Vista-Controlador)** en el backend con el fin de organizar mejor el código, separar responsabilidades y facilitar el mantenimiento y futuras expansiones del proyecto.

Esta arquitectura garantiza un sistema robusto, mantenible y preparado para crecer según las necesidades del proyecto Findrix.
