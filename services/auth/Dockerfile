FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install fastapi uvicorn pydantic-settings PyJWT PyJWT "passlib[bcrypt]" python-multipart
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "3000"]
