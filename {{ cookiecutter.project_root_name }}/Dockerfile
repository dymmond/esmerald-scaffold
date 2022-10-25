FROM python:3.9

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        libatlas-base-dev gfortran nginx supervisor nginx-extras

WORKDIR /src

COPY ./requirements.txt /src/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt

COPY ./{{ cookiecutter.project_src_name }} /src/app

COPY deployment/nginx.conf /etc/nginx/conf.d/
COPY deployment/nginx.conf /etc/nginx/sites-enabled/default
COPY deployment/supervisord.conf /etc/

CMD ["/usr/bin/supervisord"]
