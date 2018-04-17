from setuptools import setup, setuptools

def doc():
    with open("docs/documentation.md") as d:
        return d.read()
		
setup(
    name="tomes_entities",
    version="0.0.1",
    packages=setuptools.find_packages(),
    python_requires=">=3",
    url="https://github.com/StateArchivesOfNorthCarolina/tomes-entities",
    license="LICENSE.txt",
    author="Nitin Arora",
    author_email="nitin.a.arora@ncdcr.gov",
    description="Part of the TOMES project: creates a Stanford CoreNLP compliant RegexNER mappings file.",
    long_description=doc(),
)
