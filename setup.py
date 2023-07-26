from typing import List
from setuptools import setup,find_packages


PROJECT_NAME="Machine_Learning_Project"
VERSION= "0.0.1"
DESCRIPTION="This is our firt modular machine learning project"
AUTHOR_NAME="Deeksha"
AUTHOR_EMAIL="deekshasingh220@gmail.com"


REQUIREMENTS_FILE_NAME = "requirements.txt"

HYPHEN_E_DOT = "-e ."
# Requriments.txt file open
# read
# \n ""

def get_requirements_list()->List[str]:
    with open(REQUIREMENTS_FILE_NAME) as requriment_file:
        requriment_list = requriment_file.readlines()
        requriment_list = [requriment_name.replace("\n", "") for requriment_name in requriment_list]

        if HYPHEN_E_DOT in requriment_list:
            requriment_list.remove(HYPHEN_E_DOT)

        return requriment_list





setup(name=PROJECT_NAME,
      version=VERSION,
      description=DESCRIPTION,
      author=AUTHOR_NAME,
      author_email=AUTHOR_EMAIL,
     packages=find_packages(),
     install_requries = get_requirements_list()
     )