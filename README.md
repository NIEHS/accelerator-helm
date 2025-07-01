# accelerator-helm
Helm charts and support for Navigator/Accelerator infrastructure

## Author: Mike Conway and Deep Patel


## Links:

* Helm Docs - https://helm.sh/docs/


## Basic usage

### Development

Can run on Rancher, set up a values.yaml file with overrides in a separate location (outside of git repo)


At a minimum, you should set the passwords you need externally, see this sample for your local values.yaml overrides

```yaml
mongodb:
  auth:
    rootPassword: somepassword 
    # you set for the 'root' user in mongodb


```

Here I cd into the accelerator subdir of the repo, give a namespace and point to my override values. I then `cd accelerator` under the repo root. If I've just pulled the chart I need to bring in the dependencies in our Helm chart, so I run the `helm dependency build` command.

```sh
kubectl create namespace accelerator-dev

helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo add airflow https://airflow.apache.org/

cd accelerator

helm dependency build 

helm install -f ../../accel-values/accel-values.yaml -n accelerator-dev accelerator .


```

here i have alias k="kubectl" and am setting the default namespace as above

```sh
k config set-context --current --namespace=accelerator-dev

```

Be sure to port-forward 27017 (the mongodb service) and then you should be able to connect to the mongodb using a client
such as MongoDB Compass

Here we're uninstalling

```sh
helm uninstall accelerator -ns accelerator-dev
```

## Custom Accelerator Worker

This repo contains a custom airflow container for workers that includes some additional system and python dependencies.
See the [accel-worker-image](./accelerator/accel-worker-image/README.md)

The build of the custom container is automated by a GitHub action and the image is stored at: ghcr.io/niehs/accel-airflow:TAG, with latest being the default

## Accelerator Variables

For development environments, an example Accelerator variable set looks like this:

```json

{
    "accelerator.xcom.tempfiles.supported": true,
    "accelerator.xcom.tempfile.path": "/opt/xcom"
}


```

## Connections

A connection to Mongo needs to be created as follows

![image](https://github.com/user-attachments/assets/c81343c1-2f2a-4f3c-ad53-eaef30ba169d)

Suggested values for local:


connection id: mongo_default
connection type: http
description: local rancher accel
host: mongo-service
schema: admin
login: root
password: ---password as set in helm values.yaml---
port: 27017


# Notes


If you run into an error where you cannot see connections in Airflow, it may be due to the fernet key, you can follow these steps:

1) Shell into the web container
2) Shell into the database running ```sh airflow db shell ```
3) Delete the connections from the db: ```sh delete from connection; ```


you should now be able to go in and edit connections



