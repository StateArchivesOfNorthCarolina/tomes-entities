# Introduction
**TOMES Entities** is part of the [TOMES](https://www.ncdcr.gov/resources/records-management/tomes) project.

It is written in Python.

Its purpose is to create a [Stanford CoreNLP](https://stanfordnlp.github.io/CoreNLP/) compliant [RegexNER mappings file](https://stanfordnlp.github.io/CoreNLP/regexner.html#mapping-files) for use with [TOMES Tool](https://github.com/StateArchivesOfNorthCarolina/tomes_tool).

The mappings file is created from a Microsoft Excel 2007+ file using a specific schema, or template. Please refer to "./dictionaries/entity\_dictionary\_template.xlsx".

The file "./dictionaries/TOMES\_Entity\_Dictionary.xlsx" contains the mapping data specific to the TOMES project.

# External Dependencies
TOMES Entities requires the following:

- [Python](https://www.python.org) 3.0+ (using 3.5+)
	- See the "./requirements.txt" file for additional module dependencies.
	- You will also want to install [pip](https://pypi.python.org/pypi/pip) for Python 3.
- Microsoft Office 2007+ or another suite, such as [LibreOffice](https://www.libreoffice.org), capable of creating Excel 2007+ Excel files (.xlsx).

# Installation
After installing the external dependencies above, you'll need to install some required Python packages.

The required packages are listed in the "./requirements.txt" file and can easily be installed via PIP <sup>[1]</sup>: `pip3 install -r requirements.txt`

You should now be able to use TOMES Entities from the command line or as a locally importable Python module.

If you want to install TOMES Entities as a Python package, do: `pip3 install . -r requirements.txt`

Running `pip3 uninstall tomes_entities` will uninstall the TOMES Entities package.

# Unit Tests
While not true unit tests that test each function or method of a given module or class, basic unit tests help with testing overall module workflows.

Unit tests reside in the "./tests" directory and start with "test__".

## Running the tests
To run all the unit tests do <sup>[1]</sup>: `py -3 -m unittest` from within the "./tests" directory. 

## Using the command line
All of the unit tests have command line options.

To see the options and usage examples simply call the scripts with the `-h` option: `py -3 test__[rest of filename].py -h` and try the example.

Sample files are located in the "./tests/sample_files" directory.

The sample files can be used with the command line options of some of the unit tests.

# Modules
TOMES Entities consists of a single-purpose, high level module, **entities.py**. This creates a Stanford CoreNLP compliant version of NER patterns from a source Microsoft Excel file. It can be used as native Python class or as command line script.

## Using entities.py with Python
To get started, import the module and run help():

	Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 08:06:12) [MSC v.1900 64 bit (AM
	D64)] on win32
	Type "help", "copyright", "credits" or "license" for more information.
	>>> from tomes_entities import entities
	>>> help(entities)


*Note: the docstring examples may reference sample files that are NOT included in the installed Python package. Please use appropriate paths to sample files as needed.*

## Using entities.py from the command line
1. From the "./tomes\_entities" directory do: `py -3 entities.py -h` to see an example command.
2. Run the example command.

-----
*[1] Depending on your system configuration, you might need to specify "python3", etc. instead of "py -3" from the command line. Similar differences might apply for PIP.*
