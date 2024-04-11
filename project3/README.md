# Project 3: Performance Evaluation of CNN and ANN Models on Building Damage Prediction

## Introduction

This project focuses on using three different model architectures to develop a neural network for damage prediction. The models developed are ANN, Lenet-5 CNN, and Alternate Lenet-5 CNN. The three models were trained on a Hurrican Harvey data set that included images with building damage and no damage. More info can be found [here](https://github.com/pranjaladhi/coe-379l/blob/main/project3/COE_379L_Project_3.pdf). From developing and evaluating the three models, it was found that the Alternate Lenet-5 performed the best in accurately clasifying the images to the two categories. The model was then packaged in an inference server for execution over a network. The following includes instructions to setup and utilize the developed Lenet-5 Model to run predictions on any input image. 

## File Structure

### *[Dockerfile](https://github.com/pranjaladhi/coe-379l/blob/main/project3/Dockerfile)*
Contains important commands for building the image. Includes the installation of specific Python libraries that the script utilizes.

### *[configs.json](https://github.com/pranjaladhi/coe-379l/blob/main/project3/configs.json)*
Specifies the path for the data used in the model, and defines the URL of the inference server.

### *[docker-compose.yaml](https://github.com/pranjaladhi/coe-379l/blob/main/project3/docker-compose.yaml)*
Configures the application container, which can then be created and ran with the configuration via a single command.

### *[inference_runner.py](https://github.com/pranjaladhi/coe-379l/blob/main/project3/inference_runner.py)*
Script that interacts with the running server that includes the developed Alternate Lenet-5 model.

### *[inference_server.py](https://github.com/pranjaladhi/coe-379l/blob/main/project3/inference_server.py)*
Script that includes the server in which the requests can be made.


## Installation

Docker installation is required to build and run the Docker image provided. The image includes all requirements needed to succesfully setup and utilize the model provided. Docker installation information can be found [here](https://docs.docker.com/engine/install/ubuntu/). 

## Setup & Deployment

First, the repository will needed to cloned to include all files needed for the setup. This can be done with the command:
```
$ git clone git@github.com:pranjaladhi/coe-379l.git
```
Next, change into the `project3` directory with the line:
```
$ cd ./project3
```
As mentioned previously, the model is packaged within an inference server. The following are instructions to either retrieve or build the image to run the containzerized server. 

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
* Note: the `project3.ipynb` file will first have to be ran to create and save the models. To do this, the files to train the model will be needed as well, which can be found [here](https://github.com/joestubbs/coe379L-sp24/tree/master/datasets/unit03/Project3/data_all_modified) Otherwise, the `docker-compose.yaml` will not build the image and return an error.

Either of the methods described above will start and run the container for the inference server. Requests to the server can now be made. 

## Usage

With the container running in the first shell, a new shell will be required to make requests to the inference server.

Requests supported:
|   | Route | Method | Returns |
| - | ----- | ------ | ------- |
| 1 | `/`   | GET | Information about the API |
| 2 | `/info` | GET | Metadata regarding the model |
| 3 | `/predict` | POST | Prediction of an input image utilizing the model |

Requests can be made either using the `curl localhost:5000` command, or with the included `inference_runner.py` file. The file allows for the requests to be made easily, and the instructions can be seen with the command:
```
$ python3 inference_runner.py -h
```

To utilize the model for image assessing, the input image has to be included within the `/data` subdirectory. Otherwise, errors will be returned. Example outputs with the setup process followed above can be found below.

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
1
</td>
    
<td> 

`python3 inference_runner.py -r` 

</td>
<td>
    
```
==================== WELCOME ====================
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
2
</td>

<td>

`python3 inference_runner.py -i` 

</td>
<td>
    
```
==================== METADATA ====================
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
3
</td>

<td>

`python3 inference_runner.py -p` 

</td>
<td>
    
```
==================== PREDICTIONS ====================
'-95.6316_29.861296000000003.jpeg': no damage
'-93.7432_30.072399.jpeg': damage
```

</td>
</tr>
</table>



