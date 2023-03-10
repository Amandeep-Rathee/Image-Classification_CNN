# Image-Classification_CNN

This is a CNN based deep learning model for image classification, with an API built using flask-ngrok framework. The model uses a dataset with 3 classes namely Sofa, Bed and Chair.

## Pre-Requisites
To create your own Image Classification model follow the steps.
- The dataset containing raw images in JPG format. To convert them into CSV format use the  _Image_to_csv.py_  script. Before that make sure all images are in same folder and the names of all images containing  _Sofa_  should start with **S**, _Chair_ images with **C** and, and _Bed_ images with **B**.
- Once CSV is made use the _ _fulhaus.py_ _ file to create model.
- A Small frontend UI is available in _ _frontend_ _ folder and contains _ _frontend.html_ _ and _ _main.js_ _ file.

## Installation

Clone the repository to your local machine.
Install the necessary dependencies using the requirements.txt file:
```
pip install -r requirements.txt
```
## Usage

- Run the Flask app to start the API server:
```
python app.py
```

- Make a POST request to the API endpoint with the image file you want to classify:
```
import requests

url = 'http://localhost:5000/classify'

image_path = 'path/to/image.jpg'
files = {'image': open(image_path, 'rb')}

response = requests.post(url, files=files)

print(response.json())
```

## Docker Image

- Build the Image using Docker file.
```
docker build -t image-classification-api .
```
- Run the image in a container:
```
docker run -p 5000:5000 image-classification-api
```
## CI\CD Pipeline

This project uses a CI/CD pipeline with Github Actions to automatically build and test the code every time a new commit is pushed to the repository. The pipeline runs the following steps:

- Install dependencies
- Build the Docker image
- Run tests
- Push the Docker image to Docker Hub

To use the pipeline for your own repository, simply add the following files to your repository:

- .github/workflows/build-and-deploy.yml (with your Docker Hub credentials)
- Dockerfile
- requirements.txt
- app.py
- test.py (if applicable)

## Model Architecture
```
Model: "sequential"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 conv2d (Conv2D)                (None, 30, 30, 32)        896       
                                                                 
 max_pooling2d (MaxPooling2D)   (None, 15, 15, 32)        0         
                                                             
                                                                 
 conv2d_1 (Conv2D)               (None, 13, 13, 64)       18496     
                                                                 
 max_pooling2d_1 (MaxPooling2D)  (None, 6, 6, 64)         0         
                                                              
                                                                 
 flatten (Flatten)                (None, 2304)            0         
                                                                 
 dense (Dense)                    (None, 64)              147520    
                                                                 
 dense_1 (Dense)                  (None, 10)              650       
                                                                 
=================================================================
Total params: 167,562
Trainable params: 167,562
Non-trainable params: 0
_________________________________________________________________
```
