# Especificación de Requisitos del Sistema - Findrix

## 1. Introducción
Findrix es un aplicativo web diseñado para ayudar a las personas a gestionar sus finanzas personales de manera efectiva. Incluye herramientas para el registro de transacciones, presupuestos, reportes financieros y un módulo educativo gamificado para aprender sobre finanzas personales, con niveles adaptados a principiantes, usuarios intermedios y expertos.

## 2. Descripción General del Sistema
El sistema permite a los usuarios autenticados gestionar ingresos y gastos, establecer metas financieras, visualizar análisis y progresar en su educación financiera a través de lecciones interactivas y desafíos.

## 3. Requisitos Funcionales
Los requisitos funcionales están redactados en lenguaje preciso, sin ambigüedades, con identificador único (RF-001, RF-002...) y descripción de lo que el sistema debe hacer.

- **RF-001**: El sistema debe permitir el registro de nuevos usuarios mediante correo electrónico y contraseña.
- **RF-002**: El sistema debe permitir el inicio de sesión con credenciales válidas y recuperación de contraseña.
- **RF-003**: El sistema debe permitir registrar ingresos y gastos con detalles como monto, categoría, fecha y descripción.
- **RF-004**: El sistema debe calcular automáticamente el balance neto del usuario.
- **RF-005**: El sistema debe permitir la creación y edición de presupuestos mensuales por categoría.
- **RF-006**: El sistema debe generar reportes visuales de gastos e ingresos (gráficos de pastel, barras).
- **RF-007**: El sistema debe permitir establecer metas de ahorro con seguimiento de progreso.
- **RF-008**: El módulo de aprendizaje debe ofrecer lecciones en niveles: Principiante, Intermedio y Experto.
- **RF-009**: El sistema debe desbloquear niveles progresivamente según el rendimiento del usuario en lecciones.
- **RF-010**: El sistema debe proporcionar quizzes y desafíos interactivos en el módulo educativo.
- **RF-011**: El sistema debe rastrear el progreso del usuario en el aprendizaje financiero.
- **RF-012**: El sistema debe permitir la exportación de reportes en formato PDF o CSV.
- **RF-013**: El sistema debe enviar notificaciones sobre gastos excesivos o logros alcanzados.
- **RF-014**: El sistema debe permitir la categorización automática sugerida de transacciones.
- **RF-015**: El sistema debe soportar múltiples monedas con conversión.

## 4. Requisitos No Funcionales
Los requisitos no funcionales están presentes y cubren al menos tres categorías: desempeño, seguridad y usabilidad, cada uno con su identificador (RNF-001...).

- **RNF-001 (Desempeño)**: El sistema debe responder a las consultas del usuario en menos de 2 segundos.
- **RNF-002 (Desempeño)**: El sistema debe soportar al menos 1000 usuarios concurrentes sin degradación significativa.
- **RNF-003 (Seguridad)**: Todos los datos de usuarios y transacciones deben estar encriptados usando HTTPS y estándares modernos.
- **RNF-004 (Seguridad)**: Implementar autenticación de dos factores (2FA) opcional.
- **RNF-005 (Usabilidad)**: La interfaz debe ser responsive y accesible en dispositivos móviles y desktop.
- **RNF-006 (Usabilidad)**: El diseño debe seguir principios de accesibilidad WCAG 2.1.
