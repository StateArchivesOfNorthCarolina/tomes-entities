import tomes_entities.entities as entities
from setuptools import setup, setuptools

def doc():
    with open("docs/documentation.md") as d:
        return d.read()
		
setup(
    author = entities.__author__,
    author_email = entities.__author_email__,
    description = entities.__description__,
    name = entities.__name__,
    url = entities.__url__,
    version = entities.__version__,
    packages = setuptools.find_packages(),
    python_requires = ">=3",
    license = "LICENSE.txt",
    long_description = doc(),
)
