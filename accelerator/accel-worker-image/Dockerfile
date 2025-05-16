FROM apache/airflow:2.10.5

USER root
COPY requirements.txt /

# Install dependencies
RUN apt-get update && apt-get install -y git

# Copy plugins
COPY plugins/ /opt/airflow/plugins/

USER airflow

# Install Python packages
RUN pip install --no-cache-dir -r /requirements.txt
RUN pip install pymongo
