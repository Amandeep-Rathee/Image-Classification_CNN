# Image-Classification_CNN

This is a CNN based deep learning model for image classification, with an API built using flask-ngrok framework. The model uses a dataset with 3 classes namely Sofa, Bed and Chair.

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
docker run -p 5000:5000 image-classification-api

## CI\CD Pipeline

This project uses a CI/CD pipeline with Github Actions to automatically build and test the code every time a new commit is pushed to the repository. The pipeline runs the following steps:

- Install dependencies
- Build the Docker image
- Run unit tests
- Push the Docker image to Docker Hub

## Model Architecture

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
