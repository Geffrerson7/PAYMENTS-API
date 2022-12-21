# API SERVICE PAYMENTS

## Descripción
Es una API de pagos de servicios hecho con django rest framework.

## Autor
- [Gefferson Max Casasola Huamancusi](https://www.github.com/Geffrerson7)

## Setup

Crear un entorno virtual y lo activamos:

```sh
$ python virtualenv venv
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
Luego de hacer esos pasos, realizamos la migración.
```sh
python manage.py makemigrations users

python manage.py migrate
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
Para la versión 1 diríjase a la ruta:
```sh
http://127.0.0.1:8000/api/v1/payments/
```

Y para la versión 2 diríjase a las rutas:
```sh
http://127.0.0.1:8000/api/v2/payments/
http://127.0.0.1:8000/api/v2/payments-crud/
http://127.0.0.1:8000/api/v2/services/
http://127.0.0.1:8000/api/v2/services-crud/
http://127.0.0.1:8000/api/v2/expired/
http://127.0.0.1:8000/api/v2/expired-crud/
```