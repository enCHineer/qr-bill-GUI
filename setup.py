import os
from setuptools import setup, find_packages


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    python_requires='>=3.10.*',
    name="qr-bill_GUI",
    version="0.0.1",
    author="Stefan Umbricht",
    author_email="stefan.umbricht@hotmail.com",
    description="Graphical User Interface for the swiss-qr-bill module.",
    packages=find_packages(),
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    install_requires=[
        'qrbill',
        'svglib',
        'reportlab',
    ],
)
