# This Repo Is Part of My [DevOps Project](https://github.com/arieluchka/DevOps-Portfolio#k8s-development-and-production-space)

> [!IMPORTANT]
> No AI tool was used during the work on these Porjects.

## Python application, pipelines and image building
### Introduction 
This repo contains 3 important Branches (main, feature and dev).

MAIN will have the latest version of the production app. currently a static http server for display (soon will move to a front-end back-end configuration using FastAPI and psycopg2).

FEATURE (or STAGING) will have a stable version of the app with new features.

DEV will have new features under development.


### Features
⚡️ [Python app](https://github.com/arieluchka/aks-cluster-project/tree/main/terraform%20file%20for%20cluster%20creation)
that builds a k8s cluster on Azure with autoscaling (to save costs while working on the project).

⚡️ [Helm charts](https://github.com/arieluchka/aks-cluster-project/tree/main/helm-charts)
with custom settings and ingress configurations, for an easy deployment on any cluster (includes: Ingress Controller, Jenkins, ArgoCD, Prometheus, Grafana etc.). 

⚡️ [Jenkins](https://github.com/arieluchka/aks-cluster-project-app/tree/feature) 
CI pipelines for building, testing and pushing Docker Images with tag tracking.

⚡️ [ArgoCD](https://github.com/arieluchka/aks-cluster-project-deployment) 
configuration for creating and maintaining the Dev, Staging and Production environments.

⚡️ Prometheus and Grafana.

⚡️ Ingress Controller.



> [!NOTE]
> The project is still under development and the readme files are still under construction. Feel free to contact me on 
[LinkedIn](https://www.linkedin.com/in/ariel-agranovich-990629264 "my linkedin porfile :)")
 for any question :) 


