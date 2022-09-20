# name of tag
FROM python:3.9-alpine3.13
LABEL maintainer="ginnyyang"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

# Everytime when it run make different layer, therefore run once
RUN python -m venv /py && \
    /py/bin/pip intall --upgrade pip && \
    /py/bin/pip intall -r /tmp/requirements.txt && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \ 
        django-user

ENV PATH="/py/bin:$PATH"

USER dgango-user