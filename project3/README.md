# Project 3: Neural Network Models

## Installation

Docker installation is required to build and run the Docker image provided. The image includes all requirements needed to succesfully setup and utilize the model provided. Docker installation information can be found [here](https://docs.docker.com/engine/install/ubuntu/). 

## Setup & Deployment

### 1. Existing Image

The existing image to run the container can be pulled from Docker Hub, executing the line:
```
$ docker pull kelach/lenet5a_model:1.0
```
Starting and running the container can be done with the line:
```
$ docker run -it --rm -p 5000:5000 kelach/lenet5a_model:1.0
```

### 2. Using `docker-compose`

Manually building the image to run the container is also possible. With all source files within one directory, execute the command:
```
$ docker-compose up
```
*Note: the `project3.ipynb` file will first have to be ran to create and save the models. Otherwise, the `docker-compose.yaml` will not build the image. 

Either of the methods described above will start and run the container for the inference server. Requests to the server can now be made. 

## Usage

With the container running in the first shell, a new shell will be required to make requests to the inference server.

Requests supported:
| Route | Method | Returns |
| ----- | ------ | ------- |
| `/`   | GET | Information about the API |
| `/info` | GET | Metadata regarding the model |
| `/predict` | POST | Prediction of an input image utilizing the model |


### Example Outputs
<table>
<tr>
<td> 

### Route 

</td>
<td> 

### Returns

</td>
</tr>
<tr>
<td> 

`curl localhost:5000/` 

</td>
<td>
    
```
Welcome! You've reached the home endpoint for the building damage prediction machine learning inference server. Here's a brief description of each route:

- /predict: POST request that accepts a JSON object with an image key containing a list of images. The images are processed and predictions are returned.
- /info: GET request that returns metadata about the model.
- /: GET request that returns this message :)

For more information, please refer to the documentation (https://github.com/pranjaladhi/coe-379l/tree/main/project3).
Happy inferencing!
```
</td>
</tr>

<tr>
<td>

`curl localhost:5000/info` 

</td>
<td>
    
```json
{
    "accuracy":0.983587,
    "description":"A convolutional neural network model trained to predict building damage from images. The model was trained on     satalite image data of buildings after the Texas Hurricane Harvey.",
    "model_name":"lenet5a",
    "trainable_parameters_count":2601666,
    "version":"1.0"
}
```

</td>
</tr>

<tr>
<td>

` curl -X POST -F "json={"image": image}" localhost:500
0/predict` 

</td>
<td>
    
```


```

</td>
</tr>
</table>



