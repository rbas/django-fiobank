# -*- coding: utf-8 -*-
import os
import sys
import shlex
import subprocess
import django_fiobank

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages  # NOQA

version = django_fiobank.__versionstr__


# release a version, publish to GitHub and PyPI
if sys.argv[-1] == 'publish':
    command = lambda cmd: subprocess.check_call(shlex.split(cmd))
    command('git tag v' + version)
    command('git push --tags origin master:master')
    command('python setup.py sdist upload')
    sys.exit()

base_path = os.path.dirname(__file__)


def read_file(filename):
    return open(os.path.join(base_path, filename)).read()

setup(
    name='django_fiobank',
    version=version,
    description=('Django-app for managing and processing Fio Bank '
                 'transaction'),
    long_description=read_file('README.rst'),
    author='Martin Voldrich',
    author_email='rbas.cz@gmail.com',
    url='https://github.com/rbas/django-fiobank',
    packages=find_packages(),
    license=read_file('LICENSE'),
    install_requires=['fiobank>=0.0.3,<0.1', 'south'],
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet',
    )
)
