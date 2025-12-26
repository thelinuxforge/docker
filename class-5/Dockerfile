FROM python:3.9
WORKDIR /app
RUN pip install flask
COPY app2.py /opt/app2.py
ENTRYPOINT FLASK_APP=/opt/app2.py flask run --host=0.0.0.0
