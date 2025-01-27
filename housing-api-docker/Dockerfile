# Utiliser une version de Python compatible avec ton projet
FROM python:3.11-slim

# Mettre à jour les sources et installer curl et git
RUN apt-get update && apt-get install -y curl git build-essential

# Télécharger et installer Poetry (version spécifique)
RUN curl -sSL https://install.python-poetry.org | python3 - --version 1.8.2

# Ajouter Poetry au PATH de manière persistante
ENV PATH="/root/.local/bin:$PATH"

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de configuration
COPY pyproject.toml poetry.lock /app/

# Installer les dépendances via Poetry
RUN poetry install --no-dev

# Copier le reste du code
COPY . /app/

# Exposer le port (si nécessaire)
EXPOSE 8000

# Commande pour démarrer l'API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
