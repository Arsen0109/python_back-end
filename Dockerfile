FROM python:3.8.3

ENV FLASK_APP=python_backend

WORKDIR /opt

COPY requirements.txt /opt

RUN python -m pip install -r /opt/requirements.txt

COPY python_backend /opt/python_backend

CMD flask run --host 0.0.0.0 -p $PORT
