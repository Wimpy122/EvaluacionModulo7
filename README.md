Sistema de Gestión de Inventario (Django + MySQL)

Este proyecto es una aplicación web desarrollada con Django que permite gestionar un inventario de productos. Implementa operaciones CRUD completas, relaciones complejas de base de datos (Uno a Uno, Muchos a Uno, Muchos a Muchos) y un sistema de vistas personalizadas junto con el panel administrativo de Django.

📋 Características

Gestión de Productos: Crear, leer, actualizar y eliminar productos.

Categorización: Clasificación de productos en categorías (Relación 1:N).

Etiquetado: Asignación de múltiples etiquetas a productos (Relación N:M).

Detalles Técnicos: Gestión de especificaciones únicas como peso y dimensiones (Relación 1:1).

Búsqueda y Filtros: Búsqueda por nombre y filtrado por categorías.

Base de Datos: Persistencia de datos utilizando MySQL.

Interfaz: Diseño limpio y responsivo con CSS personalizado.

🛠️ Requisitos Previos

Antes de comenzar, asegúrate de tener instalado lo siguiente en tu sistema:

Python 3.8+: Descargar Python

Servidor MySQL: Puedes usar XAMPP, WAMP, MAMP o instalar MySQL Community Server directamente.

Git (Opcional, para clonar el repositorio).

🚀 Instalación y Configuración

Sigue estos pasos para ejecutar la aplicación en tu entorno local:

1. Clonar el repositorio (o descargar el código)

git clone <URL_DE_TU_REPOSITORIO>
cd nombre-del-proyecto


2. Crear y activar un entorno virtual

Es recomendable usar un entorno virtual para aislar las dependencias.

Windows:

python -m venv venv
venv\Scripts\activate


macOS / Linux:

python3 -m venv venv
source venv/bin/activate


3. Instalar dependencias

Instala Django y el conector de MySQL.

pip install django mysqlclient


(Nota: Si tienes problemas instalando mysqlclient en Windows, asegúrate de tener las herramientas de compilación de C++ instaladas o busca el archivo .whl correspondiente).

4. Configurar la Base de Datos

Abre tu gestor de base de datos (phpMyAdmin, MySQL Workbench, DBeaver, etc.).

Crea una nueva base de datos vacía llamada inventario_db.

Abre el archivo settings.py de tu proyecto y verifica la configuración de la base de datos:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'inventario_db',
        'USER': 'root',      # Tu usuario de MySQL (usualmente 'root')
        'PASSWORD': '',      # Tu contraseña de MySQL (a veces vacía en local)
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


5. Aplicar Migraciones

Esto creará las tablas necesarias en tu base de datos MySQL.

python manage.py makemigrations
python manage.py migrate


6. Crear un Superusuario (Administrador)

Para acceder al panel de administración de Django:

python manage.py createsuperuser


Sigue las instrucciones para establecer un nombre de usuario, correo y contraseña.

7. (Opcional) Cargar Datos de Prueba

Si deseas poblar la base de datos con productos, categorías y etiquetas de ejemplo, puedes usar el script incluido (asegúrate de tener el archivo populate_script.py o ejecutar los comandos en la shell):

python manage.py shell


8. Ejecutar el Servidor

Finalmente, inicia el servidor de desarrollo:

python manage.py runserver


Abre tu navegador y visita: http://127.0.0.1:8000/

📂 Estructura del Proyecto

app/models.py: Definición de tablas y relaciones.

app/views.py: Lógica del negocio (CRUD).

app/urls.py: Rutas de la aplicación.

app/forms.py: Formularios para validación de datos.

app/templates/: Archivos HTML organizados por carpetas (productos, categorias, etiquetas).

app/static/css/: Archivos de estilo (styles.css).
