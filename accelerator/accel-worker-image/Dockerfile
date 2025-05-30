FROM apache/airflow:2.10.5
USER root
COPY requirements.txt /

RUN apt-get update && apt-get install -y git
USER airflow
RUN pip install --no-cache-dir -r /requirements.txt

