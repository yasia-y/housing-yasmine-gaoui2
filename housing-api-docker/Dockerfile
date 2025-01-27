# Étape de base
FROM python:3.10-slim AS base

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Étape de production
FROM base AS prod
COPY . .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
