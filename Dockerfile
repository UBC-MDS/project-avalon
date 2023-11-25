FROM quay.io/jupyter/minimal-notebook:2023-11-22

WORKDIR /home/jovyan

COPY environment.yaml .

RUN conda env update --file environment.yaml
