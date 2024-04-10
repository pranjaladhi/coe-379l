from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf
import json

with open("configs.json", "r") as file:
    config = json.load(file)

app = Flask(__name__)  # create an app instance
model_path = "model.keras" if config.get("debug", True) == False else "models/hurricane_lenet5a_model.keras"
model = tf.keras.models.load_model(model_path)  # load the model

@app.route('/predict', methods=['POST'])  # at the end point /predict
def predict():
    # check whether input is in json format with acceptable dimensions
    if request.is_json:
        data = request.json.get("image") # data is a list of images in json format (nested lists)

        # checking if the input is in the correct format
        if not data: return {"error": "Not data deteected from request data object: "+ str(request.json)}, 400

        # preprocess the images
        try:
            processed_data = [preprocess_image(image) for image in data] 
        except Exception as error:
            return {"An Error occured processing input images": str(error)}, 400
        
        # make predictions
        predictions = [model.predict(image).tolist() for image in processed_data]

        return predictions
    else:
        return {"error": "Invalid input format"}, 400


@app.route("/info", methods=["GET"])
def info():
    """
    Short summary providing metadata about the model
    """
    return {
        "model_name": "lenet5a",
        "version": "1.0",
        "accuracy": 0.983587,
        "description": "A convolutional neural network model trained to predict building damage from images. The model was trained on satalite image data of buildings after the Texas Hurricane Harvey.",
        "trainable_parameters_count": 2601666,    
    }

@app.route("/", methods=["GET"])
def home():
    """
    Introduction to the API
    """
    return f""""Welcome! You've the home endpoint for the building damage prediction machine learning inference server. Here's a brief description of each route:
- /predict: POST request that accepts a JSON object with an image key containing a list of images. The images are processed and predictions are returned.
- /info: GET request that returns metadata about the model.
- /: GET request that returns this message :)

For more information, please refer to the documentation (https://github.com/pranjaladhi/coe-379l/tree/main/project3).
Happy inferencing!
    """, 200

# HELPER FUNCTION
def preprocess_image(image):
    """
    Reshapes and rescales input image to correct dimensions
    """
    try:
        converted_image = np.array(image)
        converted_image = converted_image.reshape(1, 128, 128, 3) / 255.0
        return converted_image
    except Exception as error:
        raise Exception(f"Error converting image: {error}")

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=config.get("debug", False))  # run the flask app
