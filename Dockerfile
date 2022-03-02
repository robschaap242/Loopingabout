FROM python:latest

ENV PYTHONUNBUFFERED=1

COPY . .

CMD ["python3", "./main.py"]