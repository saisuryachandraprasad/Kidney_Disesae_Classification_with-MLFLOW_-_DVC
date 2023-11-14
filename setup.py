from setuptools import find_packages, setup


HYPHEN_E_DOT = "-e ."


def get_requirements(filepath:str):
    """This method is responsible to read all requirements to get install"""

    requirements = []

    with open(filepath,'r') as filepath_obj:
        requirements = filepath_obj.readlines()
        requirements = [req.replace("/n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements




setup(
    name= "Kideny_Disease_Classification",
    version= "0.0.1",
    author= "Sai Surya Chandra Prasad",
    author_email="saisuryachandraprasad@gmail.com",
    packages=find_packages(),
    install_requirements = get_requirements("requirements.txt")
)