#!/usr/bin/env python

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='huntlib',
      version='0.3.0',
      description='A Python library to help with some common threat hunting data analysis operations',
      long_description=long_description,
      url='https://github.com/target/huntlib',
      author='David J. Bianco',
      author_email='david.bianco@target.com',
      packages=['huntlib'],
      tests_require=['pytest'],
      setup_requires=['pytest-runner'],
      install_requires=[
        'future',
        'splunk-sdk',
        'elasticsearch-dsl',
        'pandas',
        'numpy',
        'jellyfish<0.7'
      ],
      zip_safe=True,
      classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License"
      ]
)
