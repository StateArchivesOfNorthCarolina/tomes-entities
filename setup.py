import tomes_entities.entities as entities
from setuptools import setup, setuptools

def doc():
    with open("docs/documentation.md") as d:
        return d.read()
		
setup(
    name = entities.__NAME__,
    description = entities.__DESCRIPTION__,
    url = entities.__URL__,
    version = entities.__VERSION__,
    author = entities.__AUTHOR__,
    author_email = entities.__AUTHOR_EMAIL__,
    packages = setuptools.find_packages(),
    python_requires = ">=3",
    license = "LICENSE.txt",
    long_description = doc(),
)
