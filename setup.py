from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Study_Buddy",
    version="0.1",
    author="Arnav",
    packages=find_packages(),
    install_requires = requirements,
)
