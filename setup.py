from setuptools  import setup, find_packages
from typing import List

HYPHEN_E_DOT = "-e ."
def get_requirements(file_path)-> list[str]:
    """
    This function returns a list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements



setup(
    name="MLPROJECT",
    version="0.0.1",
    author="Zion",
    author_email="oladimeji.oluwaniyi@lmu.edu.ng",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'), 
)