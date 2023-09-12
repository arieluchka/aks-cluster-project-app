# Python application, pipelines and image building (This Repo Is Part of My [DevOps Project](https://github.com/arieluchka/DevOps-Portfolio#k8s-development-and-production-space))


> No AI tool was used during the work on these Porjects.

<!-- ## Python application, pipelines and image building -->
## Introduction 
This repo contains 3 important Branches (main, feature and dev).

**MAIN** will have the latest version of the production app. currently a static http server for display (soon will move to a front-end back-end configuration using FastAPI and psycopg2).

**FEATURE** (or STAGING) will have a stable version of the app with new features.

**DEV** will have new features under development.


## Features
###  Python app 

Currently, the app on the [**main branch**](https://github.com/arieluchka/aks-cluster-project-app/tree/readme/application-files) is a simple static html page. On the [**dev branch**](https://github.com/arieluchka/aks-cluster-project-app/tree/dev/application-files), an entirely new app is being worked on. The app will include a front-end (no specifics yet) and a back-end api (using FastAPI that will handle different types of requests).

Some of the request will require sending queries to a Database (PostgreSQL), which will also be handled by the python app back-end (psycopg2).

### Packaging into an image

The app will be deployed in a K8S cluster, For that it needs to be packaged as an image using a [**Dockerfile**](https://github.com/arieluchka/aks-cluster-project-app/blob/dev/Dockerfile). The Dockerfile is currently based on a lightweight alpine image, where the app dependencies (such as python and some libraries) are installed using a [**dependencies script**](https://github.com/arieluchka/aks-cluster-project-app/blob/dev/dependencies.txt).

The image itself is built and pushed through a Jenkins Pipeline and tagged based on this GitHubs repo tag.


### Jenkins Pipeline 
> planned to be switched in the future to Azure DevOps.

The image construction is handled by a Jenkins Server running on the cluster itself (deployed with a custom helm configuration). 

Each branch in this repository is equiped with a [**Jenkinsfile**](https://github.com/arieluchka/aks-cluster-project-app/blob/dev/Jenkinsfile) which spins up a container with [docker daemon](https://hub.docker.com/_/docker) on the cluster using the [**build-pod.yaml**](https://github.com/arieluchka/aks-cluster-project-app/blob/dev/build-pod.yaml).

The repo is pulled into the container and the image is built. The tag that is used to create the image is based on the GitHubs tag. it is extracted using this command:

`TAGDESCRIPTION = sh(script: "git tag -l -n99 --format='%(contents)' ${env.TAGNAME}", returnStdout: true).trim()`

Dev and feature branches will tag the image as `{image-version}-{branch-name}`

In example: `1.0.1-dev or 1.0.1-staging`

The image will be pushed to dockerhub, where later it will be deployed through [**ArgoCD**](https://github.com/arieluchka/aks-cluster-project-deployment/tree/main) in the matching namespace. 





<!-- > [!NOTE]
> The project is still under development and the readme files are still under construction. Feel free to contact me on 
[LinkedIn](https://www.linkedin.com/in/ariel-agranovich-990629264 "my linkedin porfile :)")
 for any question :)  -->


