#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
===============================
HtmlTestRunner
===============================


.. image:: https://img.shields.io/pypi/v/toxic_comment.svg
        :target: https://pypi.python.org/pypi/toxic_comment
.. image:: https://img.shields.io/travis/lee-sutton/toxic_comment.svg
        :target: https://travis-ci.org/lee-sutton/toxic_comment

Classifies comments as either offensive or not offensive


Links:
---------
* `Github <https://github.com/lee-sutton/toxic_comment>`_
"""

from setuptools import setup, find_packages

requirements = ['Click>=6.0', ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="Lee Sutton",
    author_email='leesutton1@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="Classifies comments as either offensive or not offensive",
    entry_points={
        'console_scripts': [
            'toxic_comment=toxic_comment.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=__doc__,
    include_package_data=True,
    keywords='toxic_comment',
    name='toxic_comment',
    packages=find_packages(include=['toxic_comment']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/lee-sutton/toxic_comment',
    version='0.1.0',
    zip_safe=False,
)
