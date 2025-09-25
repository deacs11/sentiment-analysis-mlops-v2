# Immagine ufficiale e aggiornata
FROM jenkins/jenkins:latest

# Si passa a root per installare software
USER root

# Installazione Docker (client) e altri tool utili
RUN apt-get update && apt-get install -y lsb-release curl gnupg
RUN mkdir -p /etc/apt/keyrings
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg
RUN echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian \
  $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null
RUN apt-get update && apt-get install -y docker-ce-cli


    # 1. Creo il gruppo 'docker' se non esiste. Uso un GID fisso (es. 999) per coerenza.
RUN groupadd -g 999 docker
# Aggiungo l'utente 'jenkins' al gruppo 'docker' per dargli i permessi
# sul docker.sock montato.
RUN usermod -aG docker jenkins

# Torno all'utente jenkins per l'esecuzione normale
USER jenkins