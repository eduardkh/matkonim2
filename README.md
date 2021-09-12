# matkonim2
>go into the venv

```
source ../venv/bin/activate
```
>install latest packages

```
pip install django
pip install  django-storages
pip install  paramiko
```
>export to requirements file

```
pip freeze > requirements.txt
```
>start a project

```
django-admin startproject matkonim2 .
python manage.py migrate
python manage.py runserver 0:8000
```
