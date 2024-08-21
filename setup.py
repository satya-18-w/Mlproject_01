from setuptools import find_packages,setup
from typing import List


def get_requirements()->List[str]:#return list of string
    requirements_list=[] # initializing the empty list
    with open("requirements.txt","r") as file:
        requirements_list=file.readlines()
    return [req.strip() for req in requirements_list if req.strip()]    
    
    




setup(
    name="sensor",
    version="0.0.1",
    author="Satyajit",
    author_email="satyajitsamal198076@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
    
    
    
    
    
)