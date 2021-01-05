# Extend the official Rasa SDK image
FROM rasa/rasa-sdk:latest
#install dependencies inside Docker container
USER root 

WORKDIR /app

RUN python -m pip install --upgrade pip
#Install  Sudo
RUN apt-get update && apt-get -y install sudo

#Permission to user docker to use sudo
RUN useradd -m docker_usr && echo "docker_usr:docker_usr" | chpasswd && adduser docker_usr sudo
ADD ./sudoers.txt /etc/sudoers
RUN chmod 440 /etc/sudoers
RUN chmod 447 /app

# Copy as early as possible so we can cache ...
COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

# Make sure the default group has the same permissions as the owner
RUN chgrp -R 0 . && chmod -R g=u .

# Don't run as root
USER docker_usr
# Create a volume for temporary data
VOLUME /tmp
ADD ./install.sh /app/

EXPOSE 5005
ENTRYPOINT /app/install.sh
CMD ["start", "-d", "./app/dialogue"]
