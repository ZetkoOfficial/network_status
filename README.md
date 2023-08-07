# network_status
A django web application which displays internet connectivity and service availablility.
The docker image can be found hosted on docker at [zetkoofficial/network_status:latest](https://hub.docker.com/r/zetkoofficial/network_status).

## Running network_status
An example deployment of this application using docker is shown in [example_docker_deployment/](./example_docker_deployment/).
Before deployment, a config file should be mounted at the location `/config.json` in the docker container. It is **highly** recomended that the `secret_key` attribute is changed to a newly generated django secret key. The `csrf_trusted_origins` and `allowed_hosts` should also be ammended with the correct addresses. 

When running this docker image static files are collected at `/application/static/` in the container and are not served by the application, which uses `port 8000`. A reverse-proxy is therefore needed to serve them, as shown in the [example_deployment](./example_docker_deployment/). The persistent data, such as the database is located at `/application/persistent_data/`.

## Creating a superuser and populating the website/service list
When the image is running, a superuser can be created by running `docker exec -it <CONTAINER_ID> python manage.py createsuperuser`. 

The admin console, where the website/service list can be changed, is located at the URL `<ROOT_URL>/admin`(`example.com/admin` for example, if the app is hosted on the domain `example.com`).