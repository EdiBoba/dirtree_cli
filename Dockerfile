FROM python:3.9-alpine

LABEL maintainer="viachaslau_ryneiski@epam.com"
LABEL description="Demonstrates dirtree cli client opportunities"

COPY . /app

WORKDIR /app

RUN apk update && apk upgrade

ENTRYPOINT ["python", "run_client.py"]

