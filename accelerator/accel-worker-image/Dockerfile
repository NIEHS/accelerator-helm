FROM apache/airflow:3.0.2
USER root
COPY requirements.txt /
COPY cacert.pem /home/airflow/.local/lib/python3.12/site-packages/certifi/
COPY NIH-FULL.pem /etc/ssl/certs
ENV  REQUESTS_CA_BUNDLE=/home/airflow/.local/lib/python3.12/site-packages/certifi/cacert.pem

RUN apt-get update && apt-get install -y git nano wget
USER airflow
RUN pip install --no-cache-dir -r /requirements.txt

