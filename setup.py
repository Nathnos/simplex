#! /usr/bin/env python3
# coding: utf-8

from setuptools import setup

setup(
    name = 'Simplex Lienar Solver',
    version='1.0',
    author='VILLARD Lorenzo',
    author_email='villard.lorenzo.comptes@protonmail.com',
    packages=[simplex],
    url = 'https://github.com/Nathnos/simplex',
    license='GNU GENERAL PUBLIC LICENSE Version 3',
    description='A linear solver in Python using the simplex algorithm.',
    long_description=open('README.md', 'r').read(),
    long_description_content_type="text/markdown",
    install_requires=['numpy']
)
