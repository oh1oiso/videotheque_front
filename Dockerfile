# Image Python 3.8 sur Alpine
FROM python:3.8-alpine

# Copie des fichiers nécessaire dans le répertoire de travail
COPY ./requirements.txt /app/requirements.txt

# Repertoire de travail
WORKDIR /app

# Création et activation d'un environnement virtuel
RUN python -m venv venv

# Installation des dépendances
RUN pip install -r requirements.txt

# Copie le contenu du repertoire actuel dans /app du conteneur
COPY ./app /app

# Expose port 5000 for Flask to listen on
EXPOSE 5000

# Define environment variable for Flask
ENV FLASK_APP=app.py

# Démarrez l'application Flash
CMD ["python", "app.py"]
