# Restaurante App — Semana 13

## Propósito
Esta aplicación constituye la base estructural y funcional de un sistema de escritorio para la gestión de un restaurante, desarrollada en Python utilizando Tkinter para la interfaz gráfica. Se adapta la arquitectura del proyecto docente "Biblioteca App", sustituyendo el modelo Libro por Producto y manteniendo el modelo Usuario para la simulación del control de acceso al sistema.

## Estructura de Carpetas y Archivos
restaurante_app/

├── datos/

│ ├── productos.json → Archivo con el listado de productos del restaurante

│ └── usuarios.json → Archivo con los usuarios autorizados para acceder al sistema

├── modelos/

│ ├── __init__.py

│ ├── producto.py → Define la entidad Producto y sus atributos

│ └── usuario.py → Define la entidad Usuario con validación de contraseña

├── servicios/

│ ├── __init__.py

│ ├── archivo_servicio.py → Encargado de leer y escribir archivos JSON

│ └── restaurante_servicio.py → Contiene la lógica: carga datos, valida acceso, entrega listados

├── ui/

│ ├── __init__.py

│ ├── login_view.py → Pantalla de inicio de sesión

│ └── main_view.py → Panel principal tras acceso exitoso

├── main.py → Punto de entrada: crea ventana única y controla el flujo

└── README.md

## Responsabilidades de Cada Capa

- **Modelos**: Representan las entidades del dominio (Producto y Usuario), encapsulando sus atributos y métodos de conversión desde y hacia diccionarios.
- **Servicios**: Gestionan el acceso a la información y contienen la lógica de negocio. Las vistas **no leen directamente los archivos JSON**, sino que solicitan toda la información a través de `RestauranteServicio`.
- **Interfaz de Usuario (ui/)**: Se encarga únicamente de presentar información gráficamente y capturar las acciones del usuario, sin incluir lógica de negocio ni lectura directa de archivos.
- **main.py**: Prepara los servicios, crea una única ventana de aplicación y controla el cambio entre la pantalla de inicio de sesión y el panel principal.

## Flujo de la Aplicación

1. Al ejecutar `main.py`, se abre la **pantalla de inicio de sesión**.
2. Se ingresan las credenciales; si están vacías se muestra advertencia.
3. Las credenciales se validan a través de `RestauranteServicio`.
4. Si son correctas → se muestra el **panel principal** con pestañas:
   - **Productos**: Muestra el listado cargado desde `productos.json` a través del servicio
   - **Usuarios**: Muestra el listado cargado desde `usuarios.json` a través del servicio
   - **Ventas**: Identificada como funcionalidad pendiente de implementación
5. Al pulsar **Cerrar Sesión** → se regresa a la pantalla de inicio de sesión, manteniendo la misma ventana.

## Credenciales de Prueba

| Usuario | Contraseña | Nombre Completo | Rol |
|---|---|---|---|
| admin | 123 | Administrador | Administrador |
| empleado | abcd | Juan Pérez | Empleado |

## Requisitos Previos

- Python 3 instalado
- Tkinter (incluido en la instalación estándar de Python)

## Pasos para Ejecutar la Aplicación

1. Ubícate dentro de la carpeta `restaurante_app` en tu terminal.
2. Ejecuta el archivo principal:
   ```bash
   python main.py

Se abrirá la ventana de la aplicación.
1.  Ingresa las credenciales indicadas para acceder.

Consideraciones Importantes
1. El sistema de acceso funciona como simulación pedagógica y no representa un sistema de autenticación seguro.

2. Se utiliza una sola ventana y un solo bucle principal de Tkinter durante toda la ejecución.
3. Las funcionalidades que aún no se han desarrollado se identifican como pendientes dentro de la interfaz.

4. Toda la información se carga desde los archivos JSON a través de los servicios; las vistas no acceden directamente a los archivo
