  GNU nano 8.7.1                                  Dockerfile                                            FROM python:3.12-slim

WORKDIR /app

COPY . .

CMD ["python", "library.py"]
