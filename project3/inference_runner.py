import requests
import argparse
import json
import os 
from skimage import io

# GLOBAL VARIABLES
with open("configs.json", "r") as file:
    config = json.load(file)
server_url = config.get("server_url", "")
data_path = config.get("data_path", "")

# checks if the data path is provided
if data_path.strip() == "": raise Exception("ERROR: A data path has not been provided in configs.json")
if server_url.strip() == "": raise Exception("ERROR: A server URL has not been provided in configs.json")

def init():
    # argument parsing
    parser = argparse.ArgumentParser()

    # add an argument
    parser.add_argument("-p", "--predict", action='store_true', help=f"Returns response from '/predict' POST request for the image(s) in {config.get('data_path')} path. Only considers .jpg, .png and .jpeg files and predictions are rendered in a 'pretty' format")
    parser.add_argument("-r", "--root", action='store_true', help="Returns response from '/' GET request. Home page")
    parser.add_argument("-i", "--info", action='store_true', help="Returns response from '/info' GET request. Includes information about the model")

    # parse the arguments
    args = vars(parser.parse_args()) # returns dictionary with the arguments parsed

    # make requestions based on the arguments
    if args.get("predict"): predict()
    if args.get("root"): root()
    if args.get("info"): info()
    if not any(args.values()): print("No arguments provided. Use -h for help")

def predict():
    """
    Predicts the image(s) in the data path
    """
    data = {
        "image": []
    }

    # obtains image paths from data path (only consider .jpg, .png and .jpeg files)
    image_files = os.listdir(data_path)
    image_filter_function = lambda path : path.endswith(".jpg") or path.endswith(".png") or path.endswith(".jpeg")
    image_files = list(filter(image_filter_function, image_files))

    if len(image_files) == 0: print("ERROR: No images found in the data path")

    # reads all images, then converts them into a list
    data["image"] = [io.imread(f"{data_path}/{image}").tolist() for image in image_files]
    try:
        # sending request
        response = requests.post(f"{server_url}/predict", data=json.dumps(data), headers={"Content-Type": "application/json"})
    except Exception as error:
        print(f"An error occured while trying to complete request: {error}")
        return
    
    # prints response error message if unsuccessful
    if response.status_code != 200: 
        print("ERROR: An error occured while trying to complete request")
        print(response.text)
        return
    response_obj = json.loads(response.text)
    # format response
    print(f"{'='*20} PREDICTIONS {'='*20}")
    for i, prediction in enumerate(response_obj):
        print(f"'{image_files[i]}': {'damage' if prediction[0][0] > 0.9 else 'no damage' }")
    print()

def root():
    """
    Home page
    """
    
    response = requests.get(server_url)
    print(f"{'='*20} WELCOME {'='*20}")
    print(response.text)
    print()

def info():
    """
    Model information
    """
    response = requests.get(f"{server_url}/info")
    print(f"{'='*20} METADATA {'='*20}")
    print(response.text)
    print()

if __name__ == "__main__":
    init()