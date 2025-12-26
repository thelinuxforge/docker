FROM ubuntu
RUN apt-get update && apt-get install python
RUN pip install flask flask-mysql
COPY . /opt/source-code/
ENV COLOR=blue
RUN wget http://w3schools.com
#ENTRYPOINT FLASK_APP=/opt/source-code/app.py flask run
ENTRYPOINT python app.py
