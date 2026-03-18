# accelerator-helm
Helm charts and support for Navigator/Accelerator infrastructure

## Author: Mike Conway and Deep Patel


## Links:

* Helm Docs - https://helm.sh/docs/
* Airflow Command Ref - https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html


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

```

Now set up secrets...

Postgres admin password

```sh

# Admin/superuser credentials
kubectl create secret generic postgres-credentials --from-literal=postgres-password=your-admin-password


```

This secret is expected in the default values.yaml.



```sh

cd accelerator

helm dependency build 

helm install -f ../../accel-values/accel-values.yaml -n accelerator accelerator .


```

here i have alias k="kubectl" and am setting the default namespace as above

```sh
k  config set-context --current --namespace accelerator

```

Be sure to port-forward 27017 (the mongodb service) and then you should be able to connect to the mongodb using a client
such as MongoDB Compass

Here we're uninstalling

```sh
helm uninstall accelerator -ns accelerator-dev
```


### Staging

For staging, the procedures are the same, with differing namespaces



```sh

k config set-context --current --namespace=ods-test

helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo add airflow https://airflow.apache.org/

cd accelerator

helm dependency build 

helm install -f ../../accel-values/accel-values-staging.yaml -n accelerator accelerator .


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
description: rs0 
host: mongo-service
schema: admin
login: root
password: ---password as set in helm values.yaml---
port:  


# Notes


## Connections page shows error

If you run into an error where you cannot see connections in Airflow, it may be due to the fernet key, you can follow these steps:

1) Shell into the web container
2) Shell into the database running ```sh airflow db shell ```
3) Delete the connections from the db: ```sh delete from connection; ```


you should now be able to go in and edit connections


## redis pod does not terminate

Forcefully delete it with:

```
k delete pod --grace-period=0 --force accelerator-redis-0
```

NB this uses the k alias for kubectl

## importing and exporting connections

See https://airflow.apache.org/docs/apache-airflow/stable/howto/usage-cli.html#cli-export-connections

## staging

Use 

```
helm install -f ../../accel-values/accel-values-staging.yaml -n ods-test accelerator .
```

## connection string tips
```
from pymongo import MongoClient

client = MongoClient(
    "mongodb://<username>:<password>@"
    "mongo-service-0.mongo-service-headless.accelerator-dev.svc.cluster.local:27017/"
    "?replicaSet=rs0&authSource=admin"
)

db = client["<your_database_name>"]
```
### If you don’t care about replica set behavior locally

You can simplify:

mongodb://root:PASSWORD@localhost:27017/admin


(no replicaSet, no directConnection)

###add In-cluster apps (no port-forward, running in Kubernetes)

Those should not use localhost. They should use the service DNS name and can omit directConnection=true, e.g.:

mongodb://root:PASSWORD@mongo-service.accelerator-dev.svc.cluster.local:27017/admin?replicaSet=rs0


(Or just mongo-service:27017 from same namespace.)

An example configuration as an airflow connection for mongo:

name: mongo_default
type: http

description: rs0
host: x
user: root
password: xxxx

port: 27017
schema: accelerator

# tunneling to Mongo

port forward mongodb pod on server using k9s

open ssh tunnel on local machine: ➜  ~ ssh -L 27017:localhost:27017 user@accelserver

update mongodb compass connection string to: mongodb://root:xxxxxxxx@127.0.0.1:27017/?directConnection=true&authSource=admin


