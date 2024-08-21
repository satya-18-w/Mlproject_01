from setuptools import find_packages,setup
from typing import List


# def get_requirements()->List[str]:#return list of string
#     requirements_list=[] # initializing the empty list
#     with open("requirements.txt","r") as file:
#         requirements_list=file.readlines()
#     return [req.strip() for req in requirements_list if req.strip()]    
    
    

# def get_requirements():
#     with open("requirements.txt", "r") as f:
#         requirements = f.readlines()
#     # Strip out comments and empty lines
#     return [r.strip() for r in requirements if r.strip() and not r.startswith("#")]


def get_requirements()->List[str]:
    requirements_list : List[str] = []
    return requirements_list

setup(
    name="sensor",
    version="0.0.1",
    author="Satyajit",
    author_email="satyajitsamal198076@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
    
    
    
    
    
)