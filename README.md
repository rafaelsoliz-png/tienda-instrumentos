# Sistema de Gestión de Inventario - Tienda de Instrumentos

## Descripción del Proyecto
Aplicación web desarrollada para gestionar el inventario de una tienda de instrumentos musicales. El sistema permite administrar el catálogo completo de productos mediante una arquitectura basada en Python, Flask y MongoDB, cumpliendo con todos los requerimientos funcionales y técnicos establecidos en el documento del proyecto.

## Tecnologías y Herramientas
* **Backend:** Python 3, Flask
* **Base de Datos:** MongoDB (PyMongo)
* **Frontend:** HTML5, Bootstrap 5, Jinja2
* **Control de Versiones:** Git, GitHub

## Requerimientos Implementados

### Sprint 1: Gestión Básica (CRUD)
* **[RS-1] Setup Inicial:** Configuración del entorno virtual, conexión a la base de datos MongoDB local y estructuración de rutas.
* **[RS-2] Creación de Producto:** Formulario validado para registrar nuevos instrumentos (nombre, descripción, precio, stock, categoría, URL de imagen).
* **[RS-3] Listado de Productos:** Visualización del inventario completo en una tabla dinámica con acciones integradas.
* **[RS-4] Detalle de Producto:** Vista individual en formato tarjeta con toda la información específica del instrumento seleccionado.
* **[RS-5] Actualización de Producto:** Carga de datos existentes en el formulario para su edición y actualización directa en la base de datos.
* **[RS-6] Eliminación con Confirmación:** Medida de seguridad implementada mediante una pantalla de advertencia antes de eliminar un registro definitivamente.

### Sprint 2: Funcionalidades Avanzadas
* **[RS-7] Lógica de Imágenes:** Asignación automática de una imagen por defecto (`default.jpg`) para productos registrados sin URL de imagen, evitando errores de interfaz.
* **[RS-8] Sistema de Búsqueda y Filtros Combinados:** * Búsqueda por coincidencia de texto en el nombre.
  * Filtrado exacto o parcial por categoría.
  * Filtrado por rango numérico (Precio Mínimo y Precio Máximo).
* **[RS-9] Ajustes de Interfaz:** Implementación de diseño limpio, barra de navegación estática y pie de página fijado en la parte inferior.
* **[RS-10] Documentación:** Elaboración de este archivo detallando el proyecto y sus instrucciones de ejecución.
* **[RS-11] Demostración en Video:** Demostración del funcionamiento completo del sistema (Enlace al video: ).

## Instrucciones de Despliegue Local

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/rafaelsoliz-png/tienda-instrumentos.git](https://github.com/rafaelsoliz-png/tienda-instrumentos.git)
   cd tienda-instrumentos