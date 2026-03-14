FROM python:3.9-slim

WORKDIR /app
COPY . .

RUN pip install requests flask kubernetes prometheus-client

ENV PORT 8080
CMD ["python", "app.py"]
