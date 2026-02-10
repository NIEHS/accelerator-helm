FROM apache/airflow:3.0.2
USER root
COPY requirements.txt /
COPY NIH-FULL.pem /etc/ssl/certs

RUN apt-get update && apt-get install -y git
USER airflow
RUN pip install --no-cache-dir -r /requirements.txt

