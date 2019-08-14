#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='civ6_hooks_matrix',
    version='1.0',
    description='Civ hooks to send message to matrix',
    author='Coolmic',
    author_email='hello@hardmode.fr',
    python_requires='>=3.5',
    install_requires=[
        'Flask',
        'python-dotenv',
        'matrix-client',
    ],
    packages=[
        'civ6_hooks_matrix',
        'civ6_hooks_matrix.matrix',
        'civ6_hooks_matrix.routes',
        'civ6_hooks_matrix.services',
    ],
    entry_points={
        'console_scripts': ['civ6_hooks_matrix=civ6_hooks_matrix:main']
    }
)
