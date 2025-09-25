FROM python:3.9-slim

WORKDIR /app

# Copio tutto il progetto (app, tests, etc.) in una sottocartella, 
# così la struttura dei moduli viene mantenuta.
COPY . .

# Installo le dipendenze
RUN pip install --no-cache-dir -r app/requirements.txt

EXPOSE 5000

# Quando avvio, ci spostiamo nella cartella dell'app
CMD ["gunicorn", "--chdir", "app", "--bind", "0.0.0.0:5000", "main:app"]