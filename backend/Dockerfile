FROM python:latest

WORKDIR /

ENV FLASK_APP "app.py"
ENV FLASK_DEBUG "1"
ENV FN_FLASK_SECRET_KEY "RANDOM"
ENV DB_USER_NAME "postgres"
ENV DB_PASSWORD "postgres"
ENV DB_HOST "database"
ENV DB_NAME "postgres"

ADD requirements.txt requirements.txt

RUN pip install -r requirements.txt

ADD . .

EXPOSE 3000

CMD ["python", "app.py"]
