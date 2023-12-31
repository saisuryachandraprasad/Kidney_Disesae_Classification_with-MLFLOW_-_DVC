import os
import yaml
from pathlib import Path
from box import ConfigBox
from ensure import ensure_annotations
from box.exceptions import BoxValueError
from src.Kidney_Disease_Classification import logger
import json
import base64


@ensure_annotations
def read_yaml(path_to_yamlfile:Path) -> ConfigBox:
    """This method is responsible for read data from yaml file

    ARGS: path of the yaml file to read
    return: return type will be configbox format
    """

    try:
        with open(path_to_yamlfile) as yamlfile_obj:
            content = yaml.safe_load(yamlfile_obj)

            logger.info(f"Reading done from {path_to_yamlfile} file")

            return ConfigBox(content)
        
    except BoxValueError:
        raise ValueError(f"{path_to_yamlfile} is empty")
    except Exception as e:
        raise e



@ensure_annotations
def create_directory(path_of_directory:list, verbose = True):
    """This method is responsible for creating directories"""

    for directory in path_of_directory:
        os.makedirs(directory,exist_ok= True)

        if verbose:
            logger.info(f"Directory is created for {directory}")


@ensure_annotations
def get_size(path:Path) -> str:
    """ This method is responsible to give size of file if present
    ARGS: take path olf file
    """

    size = round(os.path.getsize(path)/1024)

    return f"~ {size} kb"


@ensure_annotations
def save_json(path:Path, data:dict):
    """This method is responsible for saving file in josn format
    ARGS: path to save the file
    data: data to store in json format
    """

    with open(path, "w") as path_obj:
        json.dump(data, path_obj,indent=4)

        logger.info(f"data is saved in json format")

def image_encode(img_string, filename):
    """This method is responsible to encode image
    img_string: image to encode
    filename: file where to encode image
    """
    imagedata = base64.b64decode(img_string)

    with open(filename, "wb") as file_obj:
        file_obj.write(imagedata)
        file_obj.close()


def encodeimageintobase64(croppedimagepath):
    """This method is responsible to encode image"""
    with open(croppedimagepath,"rb") as file_obj:
        return base64.b64decode(file_obj.read())
