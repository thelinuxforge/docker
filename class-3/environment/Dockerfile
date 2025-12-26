FROM python:3.9
WORKDIR /app
RUN pip install flask
COPY app.py /opt/app.py
ENV APP_COLOR=blue
ENTRYPOINT FLASK_APP=/opt/app.py flask run --host=0.0.0.0
