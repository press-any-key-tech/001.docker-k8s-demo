# 1.docker-k8s-demo
Source files for docker and kubernetes training session.

## 01.starting-dockerfile

Only used during the demo. No source code.

## 02.basic-web

Basic docker web server.

## 03.k8s-basic-application

Basic kubernetes application for exploring deployments.

## 04.k8s-hpa

Horizontal Pod Autoscaling demo.

## 05.k8s-aws-cluster

Launch cluster in AWS and deploy application.


## 06.pod.network.config

Simple python application using redis. To learn about docker compose, docker networking, upload to docker registries and kubernetes configuration (configmaps and secrets).


### Build image

docker build -t basicweb:latest .

### Push to Docker hub

docker login --username=yourusername --password yourpassword
docker image tag basicweb:latest impalah/basicweb:latest

docker push yourhubusername/imagename

