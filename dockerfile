FROM python:3.8
COPY . /app
WORKDIR /app
RUN apt update

CMD python3 ./main.py
