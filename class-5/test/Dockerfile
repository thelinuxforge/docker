FROM python:3.9
WORKDIR /app
RUN pip install flask
COPY app1.py /opt/app1.py
ENTRYPOINT FLASK_APP=/opt/app1.py flask run --host=0.0.0.0
