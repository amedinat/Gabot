FROM python:3.7.9-slim

WORKDIR /app
#install dependencies inside Docker container
USER root 

RUN python -m pip install --upgrade pip

# Copy as early as possible so we can cache ...
COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir

COPY . .


RUN pip install -e . --no-cache-dir

VOLUME ["/app/model", "/app/config", "/app/project", "/app/dialogue"]


# Make sure the default group has the same permissions as the owner
RUN chgrp -R 0 . && chmod -R g=u .

# Don't run as root
USER 1001
EXPOSE 5005
ENTRYPOINT ["./entrypoint.sh"]
CMD ["start", "-d", "./dialogue"]
