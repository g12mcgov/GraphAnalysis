#!/usr/local/bin/python

#
#   setup.py
#
#   Author: Grant McGovern
#   Date: 26 April 2015
#
#   CSC 222 [] Lab 4 : Graph Exploration
#
#
#
import time
from setuptools import setup, find_packages

print "Setting up environment...\n"
time.sleep(2)

## Get our requirements from our .txt file
with open('requirements.txt') as requirements:
	modules = [line.strip('\n') for line in requirements]

print "Install pip modules... (This might take awhile)\n"

setup(name = 'Lab4',
	description = 'Graph Lab',
	author = 'Grant McGovern',
	author_email = 'mcgoga12@wfu.edu',
	install_requires = modules
)
