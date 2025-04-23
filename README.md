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



Here I cd into the accelerator subdir of the repo, give a namespace and point to my override values

```
kubectl create namespace accelerator-dev

helm install -f ../../accel-values/accel-values.yaml -n accelerator-dev accelerator .


```

here i have alias k="kubectl" and am setting the default namespace as above

```
k config set-context --current --namespace=accelerator-dev

```

Be sure to port-forward 27017 (the mongodb service) and then you should be able to connect to the mongodb using a client
such as MongoDB Compass

