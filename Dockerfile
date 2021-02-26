FROM python:3.7-slim

COPY ./requirements.txt /opt/app/requirements.txt
WORKDIR /opt/app

RUN pip install --no-cache --upgrade pip \
  && pip install --no-cache -r requirements.txt

ARG NB_USER=hsd
ARG NB_UID=1000
ENV USER ${NB_USER}
ENV NB_UID ${NB_UID}
ENV HOME /home/${NB_USER}

RUN echo "$PWD"
RUN echo "c.NotebookApp.max_buffer_size = 1073741824" >> ../../etc/jupyter/jupyter_notebook_config.py

RUN adduser --disabled-password \
  --gecos "Default user" \
  --uid ${NB_UID} \
  ${NB_USER}

WORKDIR ${HOME}
RUN chown -R ${NB_UID} ${HOME}
COPY . ${HOME}
RUN rm -rf ./requirements.txt
RUN rm -rf ./Dockerfile

USER ${NB_USER}
EXPOSE 8888
CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]
