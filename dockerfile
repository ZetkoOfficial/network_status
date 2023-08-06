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

FROM base AS test
CMD ["python3", "manage.py", "test"]

FROM base AS run
RUN python3 manage.py migrate
RUN python3 manage.py collectstatic --noinput

EXPOSE 8000
CMD ["gunicorn", "network_status_django.wsgi", "--bind", "0.0.0.0:8000"]