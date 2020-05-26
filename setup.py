#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages
import os

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = []
with open('requirements.txt') as f:
    for line in f:
        splitted = line.split("#")
        stripped = splitted[0].strip()
        if len(stripped) > 0:
            requirements.append(stripped)

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=3', ]

setup(
    author="portugueslab",
    author_email='vilim@neuro.mpg.de',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Who say NI",
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='theknights',
    name='theknights',
    packages=find_packages(include=['theknights', 'theknights.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/portugueslab/theknights',
    version='0.1.0',
    zip_safe=False,
)