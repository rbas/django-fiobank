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

# Hack to prevent stupid "TypeError: 'NoneType' object is not callable"
# error in multiprocessing/util.py _exit_function when running `python
# setup.py test`
# try:
#     import multiprocessing  # NOQA
# except ImportError:
#     pass

base_path = os.path.dirname(__file__)

version = django_fiobank.__versionstr__


# release a version, publish to GitHub
if sys.argv[-1] == 'publish':
    command = lambda cmd: subprocess.check_call(shlex.split(cmd))
    command('git tag v' + version)
    command('git push --tags origin master:master')
    sys.exit()

setup(
    name='django_fiobank',
    version=version,
    description=('Django-app for managing and processing Fio Bank '
                 'transaction'),
    long_description=open(os.path.join(base_path, 'README.rst')).read(),
    author='Martin Voldrich',
    author_email='rbas.cz@gmail.com',
    url='https://github.com/rbas/django-fiobank',
    packages=find_packages(),
    license=open(os.path.join(base_path, 'LICENSE')).read(),
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
