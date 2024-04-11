# Project 3: Neural Network Model

## Installation

Docker installation is required to build and run the Docker image provided. The image includes all requirements needed to succesfully setup and utilize the model provided. Docker installation information can be found [here](https://docs.docker.com/engine/install/ubuntu/). 

## Setup & Deployment

### Existing Image

The existing image to run the container can be pulled from Docker Hub, executing the line:
```
$ docker pull kelach/lenet5a_model:1.0
```
Running the container can be done with the line:
```
$ docker run -it --rm -p 5000:5000 kelach/lenet5a_model:1.0
```

### Using `docker-compose`

Manually building the image to run the container is also possible. With all source files within one directory, execute the command:
```
$ docker-compose -f docker/docker-compose.yaml up --build
```

## Usage

In a new terminal window, the requests can be executed.

Requests supported:
| Route | Method | Returns |
| ----- | ------ | ------- |
| `/`   | GET | Information about the API |
| `/info` | GET | Metadata regarding the model |
| `/predict` | POST | Prediction of an input image utilizing the model |


### Example Outputs
| Route | Returns |
| ----- | ------- |
| `curl localhost:5000/` | Welcome! You've reached the home endpoint for the building damage prediction machine learning inference server. Here's a brief description of each route:
- /predict: POST request that accepts a JSON object with an image key containing a list of images. The images are processed and predictions are returned.
- /info: GET request that returns metadata about the model.
- /: GET request that returns this message :)

For more information, please refer to the documentation (https://github.com/pranjaladhi/coe-379l/tree/main/project3).
Happy inferencing! |
| `curl localhost:5000/info` | {"accuracy":0.983587,"description":"A convolutional neural network model trained to predict building damage from images. The model was trained on satalite image data of buildings after the Texas Hurricane Harvey.","model_name":"lenet5a","trainable_parameters_count":2601666,"version":"1.0"} |
| `curl localhost:5000/predict` |  |
