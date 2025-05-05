FROM apache/airflow:3.0.0
USER root
COPY requirements.txt /

RUN apt-get update -y && apt-get install -y git
USER airflow
RUN pip install --no-cache-dir "apache-airflow==${AIRFLOW_VERSION}" -r /requirements.txt

