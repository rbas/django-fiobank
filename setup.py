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

from setuptools.command.install_lib import install_lib as _install_lib
from distutils.command.build import build as _build
from distutils.cmd import Command

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


class CompileTranslations(Command):
    description = 'compile message catalogs to MO files via django ' \
                  'compilemessages'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import os
        import sys
        from django.core.management.commands.compilemessages import \
            compile_messages

        curdir = os.getcwd()
        os.chdir(os.path.realpath(os.path.dirname(django_fiobank.__file__)))
        compile_messages(stderr=sys.stderr)
        os.chdir(curdir)


class Build(_build):
    sub_commands = [('compile_translations', None)] + _build.sub_commands


class InstallLib(_install_lib):
    def run(self):
        self.run_command('compile_translations')
        _install_lib.run(self)

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
    install_requires=['fiobank>=0.0.4,<0.1', 'south', 'pygal>=1.1.0,<2'],
    include_package_data=True,
    package_data={'django_fiobank': ['locale/*/LC_MESSAGES/*']},
    cmdclass={'build': Build, 'install_lib': InstallLib,
              'compile_translations': CompileTranslations},
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
