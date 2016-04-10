#!/usr/bin/env python

from distutils.core import setup

setup(name='Kronos',
	version='0.1',
	description='Scheduled task DSL',
	author='Milos Simic',
	author_email='milossimicsimo@gmail.com',
	url='https://github.com/MilosSimic/Kronos',
	install_requires = ["textX"],
    keywords = "scheduled task language DSL",
	packages=['kronos'],
)