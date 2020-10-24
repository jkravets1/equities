import sys
import os

import setuptools
import setuptools.command.build_py
import distutils.cmd
import distutils
from distutils.core import setup, Extension
import distutils.log
import subprocess

import distutils.log
distutils.log.set_verbosity(distutils.log.INFO) # Set DEBUG level

with open('requirements.txt') as f:
    required = f.read().splitlines()

with open("README.md", "r") as fh:
    long_description = fh.read()

VERSION = "3.0.3"

setup(
    name="equities", # Replace with your own username
    version=VERSION,
    author="Tiger_Shark",
    author_email="ljwcharles@gmail.com",
    description="equities aims to democratize access to public company financial data.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ljc-codes/equities.git",
    packages=setuptools.find_packages(),
    package_data={'equities.data.symbols': ['cik_api.csv']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=required,
    keywords="sec stock stockmarket equities equity data financials financial company public companies xbrl scraper parser pandas",
    python_requires='>=3.6',
)