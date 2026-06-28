FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --upgrade pip

RUN pip install --no-cache-dir \
    Flask==3.1.1 \
    psycopg2-binary==2.9.9

COPY . .

EXPOSE 5000

CMD ["python", "library.py"]
