FROM python:3.9-slim

WORKDIR /app
COPY . .

RUN pip install requests flask uuid # Flask to serve as a wrapper if needed by Knative/OpenFaaS

ENV PORT 8080
CMD ["python", "app.py"]
