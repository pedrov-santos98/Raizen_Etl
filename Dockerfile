FROM ${AIRFLOW_IMAGE_NAME:-apache/airflow:2.3.4}

USER root

ENV AIRFLOW_HOME=${AIRFLOW_HOME}

RUN apt-get update -yqq && \
    apt-get install -y --no-install-recommends libreoffice
    
USER airflow

RUN pip install xlrd

EXPOSE 5432/TCP
EXPOSE 5432/UDP
