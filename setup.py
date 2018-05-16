import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "RSAGraphy",
    version = "1.0",
    author = "Siddharth Chandra",
    author_email = "siddharthchandragzb@gmail.com",
    description = ("Project describing the use of RSA in Steganography"),
    license = "MIT",
    keywords = "RSA Steganography Cryptography",
    packages=['RSAGraphy'],
    long_description=read('README.md'),
)
