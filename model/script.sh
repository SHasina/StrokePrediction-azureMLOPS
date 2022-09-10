
# #!/bin/bash

PORT=8080
MEMORY=4Gi
INGRESS=all
RUNTIME=python38
PROJECT=bright-ai
REGION=us-central1
BUCKET_CLASS=standard
CLOUDRUN_NAME=stroke-prediction
SERVICE_ACCOUNT=$CLOUDRUN_NAME-svc
BUCKET_NAME="${PROJECT}-strokeprediction"
IMAGE_NAME=gcr.io/$PROJECT/stroke-prediction:latest

#ENABLE CLOUD API SERVICES
echo "START TO ENABLE APIS"
gcloud services enable containerregistry.googleapis.com --project=$PROJECT
gcloud services enable storage-component.googleapis.com --project=$PROJECT
gcloud services enable storage.googleapis.com --project=$PROJECT
gcloud services enable run.googleapis.com --project=$PROJECT
echo "AFTER SUCCESSFULLY ENABLING APIS"

