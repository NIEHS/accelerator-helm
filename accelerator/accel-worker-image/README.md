# Docker Airflow Custom Image for Accelerator

## Description


## Links

* GitHub Container Registry - https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry




## Procedure

* requirements.txt file holds requirements that will be packaged into the container
* github action to build and push - https://github.com/marketplace/actions/docker-build-push-action

### Logging in to publish a package

```sh
export CR_PAT=YOUR_TOKEN
```

Using the CLI for your container type, sign in to the Container registry service at ghcr.io.

```sh
$ echo $CR_PAT | docker login ghcr.io -u USERNAME --password-stdin

```

This example pushes the latest version of IMAGE_NAME.

```sh   
docker push ghcr.io/NAMESPACE/IMAGE_NAME:latest

```

Replace NAMESPACE with the name of the personal account or organization to which you want the image to be scoped.


This example pushes the 2.5 version of the image.

```sh
docker push ghcr.io/NAMESPACE/IMAGE_NAME:2.5
```