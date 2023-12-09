FROM quay.io/jupyter/minimal-notebook:2023-11-22

USER root

RUN apt update && apt install -y make

USER $NB_USER

WORKDIR /home/jovyan

COPY environment.yaml .

RUN conda env update --file environment.yaml