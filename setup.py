# -*- coding: utf-8 -*-

import os
import re
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


TEST_REQUIRES = [
    'six',
    'pytest',
    'httpretty',
    'pytest_httpretty',
]


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()


class PyTest(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = [
            '--verbose'
        ]
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)


def find_version(fname):
    """Attempts to find the version number in the file names fname.
    Raises RuntimeError if not found.

    """
    version = ''
    with open(fname, 'r') as fp:
        reg = re.compile(r'__version__ = [\'"]([^\'"]*)[\'"]')
        for line in fp:
            m = reg.match(line)
            if m:
                version = m.group(1)
                break
    if not version:
        raise RuntimeError('Cannot find version information')
    return version

__version__ = find_version('requests_middleware/__init__.py')


setup(
    name='requests-middleware',
    version=__version__,
    description='Composable HTTP middleware for requests',
    long_description=open('README.rst').read(),
    author='Joshua Carp',
    author_email='jm.carp@gmail.com',
    url='https://github.com/jmcarp/requests-middleware',
    packages=find_packages(exclude=('test*', )),
    package_dir={'requests_middleware': 'requests_middleware'},
    include_package_data=True,
    install_requires=[
        'six',
        'requests',
        'python-dateutil',
    ],
    license=open('LICENSE').read(),
    zip_safe=False,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=TEST_REQUIRES,
    cmdclass={'test': PyTest}
)
