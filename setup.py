"""
aio.http
"""
import os
import sys
from setuptools import setup, find_packages

version = '0.0.10'

install_requires = [
    'setuptools',
    'aiohttp',
    'aio.app',
    'zope.dottedname']

if sys.version_info < (3, 4):
    install_requires += ['asyncio']

tests_require = install_requires + ['aio.testing']


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    'Detailed documentation\n'
    + '**********************\n'
    + '\n'
    + read("README.rst")
    + '\n')


setup(
    name='aio.http',
    version=version,
    description="HTTP server for the aio asyncio framework",
    long_description=long_description,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.4",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    keywords='',
    author='Ryan Northey',
    author_email='ryan@3ca.org.uk',
    url='http://github.com/phlax/aio.http',
    license='GPL',
    packages=find_packages(),
    include_package_data=True,
    package_data={'': ['*.rst']},
    zip_safe=False,
    tests_require=tests_require,
    install_requires=install_requires,
    entry_points={})
