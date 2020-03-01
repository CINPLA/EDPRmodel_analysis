from setuptools import setup
from setuptools import find_packages

setup(
    name="EDPRmodel_analysis",
    packages=find_packages(),
    package_data={'data': ['initial_values/*.dat']},
    version="0.1")
