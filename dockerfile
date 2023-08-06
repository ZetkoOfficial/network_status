FROM python:slim-bullseye AS base
RUN apt-get -y update && apt-get -y --no-install-recommends install iputils-ping

WORKDIR /application/
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

COPY requirements.txt .
COPY config.json /config.json
RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn
COPY ./network_status_django .
ENTRYPOINT ["python3", "manage.py"]

FROM base AS test
CMD ["test"]

FROM base AS run
RUN python3 manage.py migrate

EXPOSE 8000
ENTRYPOINT ["python3", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]