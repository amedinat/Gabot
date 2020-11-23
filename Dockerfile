FROM python:3.7.9-slim

#install dependencies inside Docker container
USER root 

WORKDIR /app

ADD ./models /app/models/
ADD ./config /app/config/
ADD ./actions /app/actions/
ADD ./scripts /app/scripts/
ADD ./data /app/data/
ADD ./domain.yml /app/
ADD ./config.yml /app/

RUN python -m pip install --upgrade pip

# Copy as early as possible so we can cache ...
COPY requirements.txt .

RUN pip install -r requirements.txt --use-feature=2020-resolver --no-cache-dir

VOLUME ["/app/model", "/app/config", "/app/project", "/app/dialogue"]


# Make sure the default group has the same permissions as the owner
RUN chgrp -R 0 . && chmod -R g=u .

# Don't run as root
USER 1001
EXPOSE 5005
ENTRYPOINT ["./entrypoint.sh"]
CMD ["start", "-d", "./dialogue"]
