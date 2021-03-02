# API для соц сети

## **Структура проекта**

### APYDOC -> index.html документация к API в формате веб-страницы ( библиотека apidocjs )
### django_social_app -> api проекта

## **Технологии для проекта**
- requests
- postgresql
- DJANGO
- DJANGO Rest Framework
    - django rest-corsheaders
    - django rest-silk
    
- APIDOCJS ( npm install apidoc )

## **Запуск проекта**
(сначала првоерить настройки подключения к бд)
windows:
```
python -m venv venv
venv\scripts\activate
pip install -r requirements.txt
cd django_social_test
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
linux:
```
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
cd django_social_test
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```