#!/bin/bash
#A script for pushing updates to our docker image to ECR
echo please input AWS region

read region

echo please input the URI of your ECR container

read URI
#Login to ECR
aws ecr get-login-password --region $region | docker login --username AWS --password-stdin $URI
#Tag docker image
docker tag action $URI
#Push to ECR
docker push $URI
