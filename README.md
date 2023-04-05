# API SERVICIO DE PAGOS

## Descripción
Es una API de pagos de servicios que permite en la condición de usuarios añadir pagos de los servicios de streaming y listarlos en realizados y vencidos. Y en el lado del admin adicionalmente puede crear y actualizar la información de un servicio.

## ERD

![ERD-PAYMENTS](https://user-images.githubusercontent.com/61089189/230167491-f999942a-3877-40ad-a799-a1c5b520e4a6.png)

## Setup

Crear un entorno virtual:

```sh
$ virtualenv venv
```

Activar el entorno virtual
```sh
# windows
$ source venv/Scripts/activate
# Linux
$ source venv/bin/activate
```

Luego instalar las librerias:

```sh
(env)$ pip install -r requirements.txt
```

Primero, dentro de settings.py comentamos la siguiente linea:  
```sh
INSTALLED_APPS = [
   ...
   #'django.contrib.admin',
   ...
]
```
Y en las rutas de nuestra carpeta principal(service_payments), comentamos lo siguiente:
```sh
urlpatterns = [
   ...
   #path('admin/', admin.site.urls) 
   ...
]
```
Luego de hacer esos pasos, realizamos la migración del modelo users.
```sh
(env) $ python manage.py makemigrations users

(env) $ python manage.py migrate
```
Luego de haber realizado la migración, descomentamos todo lo anterior y realizamos las otras migraciones.
```sh
(env) $ python manage.py makemigrations
(env) $ python manage.py migrate
```

Una vez concluido, procedemos a iniciar la app
```sh
(env)$ python manage.py runserver
```

## Documentación
Para la documentación del proyecto se utilizó Swagger por su capacidad para generar documentación dinámica y en tiempo real de los servicios web que se están construyendo.
La documentación del projecto en swagger está en este [Link](https://payments-api-2fqe.onrender.com/swagger/)

## Frontend
- El reposistorio del forntend está en este [enlace](https://www.github.com/Geffrerson7).

## Autor
- [Gefferson Max Casasola Huamancusi](https://www.github.com/Geffrerson7)
