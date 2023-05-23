from setuptools import setup, find_packages

setup(
    name='bbox',
    version='0.1.0',
    description='A Python library for handling the 2D bounding box.',
    author='Pandede',
    packages=find_packages(),
    install_requires=[
        "pydantic"
    ]
)
