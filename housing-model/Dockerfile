# Étape de base
FROM python:3.10-slim AS base

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Étape de production (optionnelle si multi-étages)
FROM base AS prod
COPY . .
EXPOSE 5000
CMD ["python", "train_model.py"]
