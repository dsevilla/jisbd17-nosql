FROM jupyter/all-spark-notebook

MAINTAINER dsevilla@um.es

EXPOSE 8888

USER root

RUN apt-get update && \
    apt-get install -y docker.io
    
