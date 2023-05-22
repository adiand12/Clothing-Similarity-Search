# Clothing Similarity Search 

Welcome to the Clothing Similarity Search website! This application allows users to find clothing items similar to a given prompt. By providing a description , the website will fetch a specified number of links to products that are  similar to the provided prompt.

## Features

- Find  similar clothing items based on a prompt
- Fetch a specified number of links to related products
- Easy to deploy on the Google Cloud Platform (GCP)

## Installation

To run the Clothing Similarity Search website locally or deploy it on GCP, follow these instructions:

1. Clone the repository:
```
git clone https://github.com/adiand12/Clothing-Similarity-Search.git
```

2. Install the required dependencies. Make sure you have Python and pip installed. Then, run:
```
pip install -r requirements.txt
```
3. Run the application:
```
streamlit run app.py
```


## Deployment on GCP

To deploy the Clothing Similarity Search website on the Google Cloud Platform, follow these instructions:

1. Create a new project on GCP.

2. Enable the necessary APIs:

- App Engine Admin API

3. Set up a GCP project in the  Shell:

Command to build the application.
```
gcloud builds submit --tag gcr.io/<Project id>/<Application Name>  --project=<Project id>
```

Command to deploy the application
```
gcloud run deploy --image gcr.io/<Project id>/<Application Name> --platform managed --project=<Project id> --allow-unauthenticated
```
