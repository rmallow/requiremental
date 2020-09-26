#!/usr/bin/python3
import setuptools
import io
import os
import sys

# Package meta-data
NAME = 'requiremental'
DESCRIPTION = 'A requirement managemet tool.'
URL = 'https://github.com/rmallow/requiremental'
EMAIL = 'mail@rmallow.com'
AUTHOR = 'Robert Mallow'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = None

# Packages required
REQUIRED = [
		'PyYaml'
		]

here = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
	long_description = '\n' + f.read()

# Load the package's __version__.py
about = {}
if not VERSION:
	with open(os.path.join(here, '__version__.py')) as f:
		exec(f.read(), about)
else:
	about['__version__'] = VERSION

setuptools.setup(
	name=NAME,
	version=about['__version__'],
	description=DESCRIPTION,
	long_description=long_description,
	long_description_content_type="text/markdown",
	author=AUTHOR,
	author_email=EMAIL,
	python_requires=REQUIRES_PYTHON,
	url=URL,
	packages=setuptools.find_packages(),
	install_requires=REQUIRED,
	license='MIT',
	classifiers=[
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
	],
)