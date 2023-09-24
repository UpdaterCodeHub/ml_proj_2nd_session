from setuptools import setup
from typing import List

PROJECT_NAME ="housing-predictor"
VERSION ="0.1.1"
AUTHOR="Updater"
DESCRIPTION="My first package related project work"
PACKAGES = ["housing"]
REQUIREMENT_FILE_NAME = "requirements.txt"


def get_requirements_list()->List[str]:
    """
    Description: This function is going to return list of requirement
    mention in requiremnet.txt file

    return this funciton is going to return a list wiwhich contain name
    of libraries mentioned in requiremnts.txt file
    
    """
    
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_file.readlines()




setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=PACKAGES,
    install_requires=get_requirements_list()
)


if __name__=="__main__":
    print(get_requirements_list())