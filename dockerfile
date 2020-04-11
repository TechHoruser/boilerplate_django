FROM python:3.6.9

# update package lists, fix broken system packages
RUN apt-get update && apt-get -f install && pip install --upgrade pip && pip install pipenv

COPY . /app/
WORKDIR /app

ENTRYPOINT [ "/app/run.sh" ]
