# 06. Solución Propuesta

Para el desarrollo de **Findrix** se propone una solución integral que combina herramientas prácticas de gestión financiera con un sistema de educación gamificada. La arquitectura del sistema sigue un enfoque de tipo **cliente-servidor** basado en tres capas, lo que facilita la organización, el mantenimiento y el crecimiento escalable del proyecto.

## Arquitectura del Sistema

### Capa de Presentación (Frontend)

Corresponde a la interfaz gráfica con la que interactúan los usuarios. Su función principal es ofrecer una experiencia intuitiva, moderna y responsive para la gestión financiera y el aprendizaje.

**Tecnologías sugeridas:** HTML, CSS, JavaScript, y frameworks como React.js o Vue.js. Se utilizará Tailwind CSS para un diseño limpio y profesional.

**Funciones principales:**
- Dashboard financiero con gráficos y resúmenes
- Registro e inicio de sesión de usuarios
- Gestión de transacciones, presupuestos y metas
- Módulo educativo (lecciones, quizzes y progreso)
- Perfil de usuario y visualización de niveles/rachas

### Capa de Lógica de Negocio (Backend)

Se encarga de procesar todas las solicitudes del usuario, aplicar las reglas de negocio, realizar cálculos financieros y gestionar la comunicación entre el frontend y la base de datos.

**Tecnologías sugeridas:** Python (con Flask o Django) mediante una API REST.

**Funciones principales:**
- Validación y procesamiento de transacciones financieras
- Gestión de usuarios, niveles educativos y progreso
- Cálculo automático de presupuestos, balances y estadísticas
- Sistema de gamificación (puntos, rachas y desbloqueo de lecciones)
- Autenticación segura y control de acceso
- Generación de reportes

### Capa de Datos (Base de Datos)

Es la encargada de almacenar toda la información del sistema de manera organizada, segura y eficiente.

**Tecnología sugerida:** PostgreSQL.

**Funciones principales:**
- Almacenamiento seguro de datos financieros y educativos
- Consultas rápidas para dashboards y reportes
- Mantenimiento de la integridad y consistencia de los datos

## Flujo de Funcionamiento del Sistema

1. El usuario accede a la aplicación mediante la interfaz web.
2. Realiza una acción (ejemplo: registrar un gasto, completar una lección o consultar su presupuesto).
3. La solicitud es enviada al servidor a través de la API.
4. El backend procesa la información, aplica las reglas de negocio y consulta o actualiza la base de datos.
5. La respuesta es enviada de vuelta al frontend y se muestra al usuario en tiempo real.

## Patrón de Arquitectura Adicional

Se recomienda implementar el patrón **MVC (Modelo-Vista-Controlador)** en el backend para organizar mejor el código, separar responsabilidades y facilitar el mantenimiento y futuras expansiones.

## Diferenciadores de la Solución

- Combinación única de **gestión financiera real** + **educación gamificada**.
- Adaptación automática según el nivel del usuario (principiante, intermedio, experto).
- Enfoque en la simplicidad y la motivación continua del usuario.
- Escalabilidad para futuras integraciones (open banking, IA para recomendaciones, etc.).

Esta arquitectura garantiza un sistema robusto, mantenible y preparado para crecer según las necesidades del proyecto.
