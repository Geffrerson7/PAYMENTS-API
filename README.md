# API SERVICIO DE PAGOS

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

## API Reference

### Documentation
```sh
https://payments-api-2fqe.onrender.com/swagger
```

