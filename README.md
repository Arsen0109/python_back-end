# python_back-end
Repository for back-end labworks created on Python Flask.

**Виконав:** студент групи ІО-04 Нерода Арсен


Для запуску проекту локально потрібно мати завантажений Docker aбо Python третьої версії або більше 

*Для Python:*

1. set FLASK_APP=python_backend(for Windows); export FLASK_APP=python_backend
2. flask run

*Для Docker:*

1. docker build --build-arg PORT=<your port> . -t <image_name>:latest

2. docker-compose build

3. docker-compose -up

**Deployment**

[View deployment](https://python-backend-on-flask.herokuapp.com)