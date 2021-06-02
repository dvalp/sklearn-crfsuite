#!/usr/bin/env python
from setuptools import setup

setup(
    name='sklearn-crfsuite',
    version='0.4.0',
    author='Mikhail Korobov',
    author_email='kmike84@gmail.com',
    license='MIT license',
    long_description=open('README.rst').read() + "\n\n" + open('CHANGES.rst').read(),
    description="CRFSuite (python-crfsuite) wrapper which provides interface similar to scikit-learn",
    url='https://github.com/TeamHG-Memex/sklearn-crfsuite',
    zip_safe=False,
    packages=['sklearn_crfsuite'],
    install_requires=[
        "python-crfsuite >= 0.9.7",
        "scikit-learn ~= 0.24.0",
        "six",
        "tabulate",
        "tqdm",
    ],
    extras_require={
        "test": ["pytest"]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
