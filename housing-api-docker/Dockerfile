# Utiliser une image de base Python
FROM python:3.11-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt requirements.txt
COPY . .

# Installer les dépendances
RUN python -m venv /opt/venv && \
    . /opt/venv/bin/activate && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

# Exposer le port de l'API
EXPOSE 8000

# Commande de démarrage
CMD ["/opt/venv/bin/python", "main.py"]
