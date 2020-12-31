import os.path
from setuptools import setup

# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))

# The text of the README file
with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

setup(
    name="traveler_client",
    version="0.0.1",
    description="a python client for traveler",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/dongliu/traveler-client-python",
    author="Dong Liu",
    license="MIT",
    packages=["traveler_client"],
)
