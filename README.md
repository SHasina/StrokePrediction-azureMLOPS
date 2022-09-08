### Problem Definition
A model to predict if a person have stroke or not. Machine Learning Algorithms and Deep Learning Techniques were used to build this model.

### Cloud Architecture used
![stroke drawio](https://user-images.githubusercontent.com/74520811/185895372-13a55b6b-04e3-4a5d-82b5-0b408b38d1d6.png)

### GCP Services Used
* Container Registry
* Service Account
* Storage Bucket
* Log Analytics
* API Gateway
* CloudBuild
* CloudRun

### Other services
* docker
**Note** The script to deploy this module on Google cloud does not contain `API_Gateway` deployment configuration. This is because I already have one API Gateway I used for my Machine Learning, Deep Learning and Natural Language Processing Endpoint. This means all services will be deployed except the apigateway. After successful deployment, A Url will be displayed in your terminal then access the api docs using `THE_URL/docs`.

### Algorithms used
* GradientBoostingClassifier
* LinearDiscriminantAnalysis
* Random Forest Classifier.
* Support Vector Machine.
* ExtraTreesClassifier
* Logistic Regression.
* k-Nearest Neighbors.
* AdaBoostClassifier
* MLPClassifier
* Decision Tree.
* Naive Bayes.

* Deep Learning Technique
    * Tensorflow

### Deployment Of Application
**Note:** This instructions assume you already have a `Google Cloud` Account.
* Install gcloud cli.
* Log into your account using the following command
   * gcloud init
   * gcloud auth application-default login
