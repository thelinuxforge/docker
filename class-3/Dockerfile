FROM python:3.9
RUN apt update
WORKDIR /app
RUN pip install flask
COPY app.py /opt/app.py
ENV APP_COLOR=blue
ENV PYTHONPATH=/opt
ENTRYPOINT FLASK_APP=/opt/app.py flask run --host=0.0.0.0
