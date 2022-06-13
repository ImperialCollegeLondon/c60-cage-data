FROM mambaorg/micromamba:0.24.0

COPY --chown=$MAMBA_USER:$MAMBA_USER environment.yml environment.yml
RUN micromamba install -y -f environment.yml

COPY . /usr/src/app

WORKDIR /usr/src/app

CMD gunicorn website.app:server -b :8050
EXPOSE 8050
