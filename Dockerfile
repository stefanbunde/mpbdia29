FROM ubuntu:latest

RUN apt update && apt install -y python3-pip

RUN pip3 install flask requests uwsgi

COPY app.py /app/

WORKDIR /app

EXPOSE 8000

CMD ["uwsgi", "--http", "0.0.0.0:8000", "--module", "app:app"]
