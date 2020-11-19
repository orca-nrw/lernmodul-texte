FROM python:3.7-slim

RUN echo 'Launching Docker Container'

RUN pip install --no-cache --upgrade pip && \ 
    pip install --no-cache matplotlib nltk notebook pandas

ARG NB_USER
ARG NB_UID
ENV USER ${NB_USER}
ENV NB_UID ${NB_UID}
ENV HOME /home/${NB_USER}

RUN adduser --disabled-password \
    --gecos "Default user" \
    --uid ${NB_UID} \
    ${NB_USER}

WORKDIR ${HOME}
USER ${USER}

COPY README.md /home/${NB_USER}
COPY index.ipynb /home/${NB_USER}
COPY tweets/tweets_biden_small.csv /home/${NB_USER}/tweets