FROM quay.io/jupyter/minimal-notebook:2023-11-22

WORKDIR /app

COPY environment.yaml .

RUN conda env update --file environment.yaml
