# space to keep production to-dos

# see https://airflow.apache.org/docs/helm-chart/stable/production-guide.html


redis error (see worker logs)

[2025-04-25 15:59:48,287: ERROR/MainProcess] consumer: Cannot connect to redis://:**@accelerator-redis:6379/0: invalid username-password pair or user is disabled..                                                                                                                                                                    │
│ Trying again in 2.00 seconds... (1/100)


* ingres web and api server
* postgres (volumes, backup, config into airflow)
* mongo (volumes, backup, sharding?)
* logging/prometheus
* worker types 
* config -> accelerator framework
* login/user provisioning
* provider for mongo from airflow? add package?
* python reqs for dags?
* fernet key encryption

# cons and props
* temp files (volumes?)
* accel config
* cedar conn
* mongo conn