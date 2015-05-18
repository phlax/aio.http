"""
aio.http
"""
import sys
from setuptools import setup, find_packages

version = '0.0.1'

install_requires = [
    'setuptools',
    'aiohttp',
    'aio.app',
    'zope.dottedname']

if sys.version_info < (3, 4):
    install_requires += ['asyncio']

tests_require = install_requires + ['aio.testing']

setup(
    name='aio.http',
    version=version,
    description="Aio http server",
    classifiers=[
        "Programming Language :: Python 3.4",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    keywords='',
    author='Ryan Northey',
    author_email='ryan@3ca.org.uk',
    url='http://github.com/phlax/aio.http',
    license='GPL',
    packages=find_packages(),
    namespace_packages=['aio'],
    include_package_data=True,
    package_data={'': ['README.rst']},    
    zip_safe=False,
    tests_require=tests_require,
    install_requires=install_requires,
    entry_points={})
