
from setuptools import setup, find_packages

from codecs import open
from os import path

HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="cs-nds",
    version="0.1.0",
    description="Often used things for Computer Science classes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alexcoder04/cs_nds",
    author="alexcoder04",
    author_email="alexcoder04@protonmail.com",
    classifiers=[
        "Intended Audience :: Education",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ],
    packages=["cs_nds"],
    install_requires=[]
)
