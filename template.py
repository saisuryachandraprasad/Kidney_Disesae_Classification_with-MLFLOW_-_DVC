import os
import logging

logging.basicConfig(level=logging.INFO, format = "[%(asctime)s]: %(message)s" )

project_name = "Kidney_Disease_Classification"


list_of_files =[
    ".github/workflow/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "requirements.txt",
    "params.yaml",
    "setup.py",
    "main.py",
    "app.py",
    "Dockerfile",
    "research/trails.ipynb",
    "templates/index.html"
]

for filepath in list_of_files:
    file_dir, file_name = os.path.split(filepath) 


    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"folder is created for {file_dir}")

    if(not os.path.exists(filepath) ) or   (os.path.getsize(filepath)==0):
        with open(filepath, 'w') as filpath_obj:
            pass
        logging.info(f"filepath is created from {filepath}")

    else:
        logging.info(f"{filepath} is already exist ")  
