import requests
import argparse
import json
import os 
from skimage import io

# GLOBAL VARIABLES
with open("configs.json", "r") as file:
    config = json.load(file)

# checks if the data path is provided
if config.get("data_path", "").strip() == "": raise Exception("ERROR: A data path has not been provided in configs.json")

def init():
    # argument parsing
    parser = argparse.ArgumentParser()

    # add an argument
    parser.add_argument("-p", "--predict", action='store_true', help=f"Predicts image(s) in {config.get('data_path')} path")
    parser.add_argument("-r", "--root", action='store_true', help="Home page")
    parser.add_argument("-i", "--info", action='store_true', help="The input file")

    # parse the arguments
    args = vars(parser.parse_args()) # returns dictionary with the arguments parsed

    # make requestions based on the arguments
    if args.get("predict"): predict()
    if args.get("root"): root()
    if args.get("info"): info()
    if not any(args.values()): print("No arguments provided")

def predict():
    """
    Predicts the image(s) in the data path
    """
    data = {
        "image": []
    }

    # obtains image paths from data path (only consider .jpg, .png and .jpeg files)
    image_files = os.listdir(config.get("data_path"))
    image_filter_function = lambda path : path.endswith(".jpg") or path.endswith(".png") or path.endswith(".jpeg")
    image_files = list(filter(image_filter_function, image_files))

    if len(image_files) == 0: print("ERROR: No images found in the data path")

    # reads all images, then converts them into a list
    data["image"] = [io.imread(f"{config.get('data_path')}/{image}").tolist() for image in image_files]
    try:
        # sending request
        response = requests.post(config.get("url"), json=data).json()
    except Exception as error:
        print(f"An error occured while trying to complete request: {error}")
        return
    
    # prints response error message if unsuccessful
    if response.status_code != 200: print(response.json())

    # format response
    print(f"{"="*20} PREDICTIONS {"="*20}")
    for i, prediction in enumerate(response):
        print(f"{image_files[i]}: {"damage" if prediction[0] > 0.99 else "no damage" }")

def root():
    """
    Home page
    """
    response = requests.get(config.get("url"))
    print(response.json())

def info():
    """
    Model information
    """
    response = requests.get(f"{config.get("url")}/info")
    print(response.json())


if __name__ == "__main__":
    init()