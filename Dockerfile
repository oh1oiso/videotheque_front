# Image Python 3.8 sur Alpine
FROM python:3.8-alpine

# Copie des fichiers nécessaire dans le répertoire de travail
COPY ./requirements.txt /app/requirements.txt

# Repertoire de travail
WORKDIR /app

# Installation des dépendances
RUN pip install -r requirements.txt

# Copie le contenu du repertoire actuel dans /app du conteneur
COPY ./app /app

# Entrée par défaut lors de l'exécution du conteneur
ENTRYPOINT ["python"]

# Expose port 5000 for Flask to listen on
EXPOSE 5000

# Define environment variable for Flask
ENV FLASK_APP=app.py



# Démarrez l'application Flash
CMD ["app.py"]