# Docker Airflow Custom Image for Accelerator

## Description


## Links

* GitHub Container Registry - https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry




## Procedure

* requirements.txt file holds requirements that will be packaged into the container


### Logging in to publish a package

```
export CR_PAT=YOUR_TOKEN
```

Using the CLI for your container type, sign in to the Container registry service at ghcr.io.
```
$ echo $CR_PAT | docker login ghcr.io -u USERNAME --password-stdin

```
