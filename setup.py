import os
import sys
import shlex
import subprocess
import django_fiobank

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages  # NOQA

from setuptools.command.install import install

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


class CompileTranslations(install):
    """Customized setuptools install command - prints a friendly greeting."""
    def run(self):
        curdir = os.getcwd()
        os.chdir(os.path.realpath(os.path.dirname(django_fiobank.__file__)))
        try:
            command = lambda cmd: subprocess.check_call(shlex.split(cmd))
            command('django-admin.py compilemessages')

        except TypeError as e:
            raise e
            pass
        os.chdir(curdir)
        install.run(self)

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
    install_requires=[
        'Django>=1.7', 'fiobank>=0.0.5,<0.1', 'pygal>=1.1.0,<2'
    ],
    include_package_data=True,
    package_data={'django_fiobank': ['locale/*/LC_MESSAGES/*']},
    cmdclass={'install': CompileTranslations},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        "Operating System :: OS Independent",
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet'
    ]
)
