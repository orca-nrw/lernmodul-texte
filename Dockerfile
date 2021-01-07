FROM python:3.7-slim

RUN pip install --no-cache --upgrade pip && \ 
    pip install --no-cache ipywidgets matplotlib nltk notebook pandas wordcloud

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

USER root
COPY . ${HOME}
RUN chown -R ${NB_UID} ${HOME}

USER ${NB_USER}