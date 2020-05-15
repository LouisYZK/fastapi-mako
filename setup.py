"""
mako template support for fastapi
"""
import os
import re
import sys
import codecs
from setuptools import setup

with codecs.open(os.path.join(os.path.abspath(os.path.dirname(
        __file__)), 'fastapi_mako.py'), 'r', 'latin1') as fp:
    try:
        version = re.findall(r"^__version__ = '([^']+)'$", fp.read(), re.M)[0]
    except IndexError:
        raise RuntimeError('Unable to determine version.')

setup(
    name='FastAPI-Mako',
    version=version,
    url='https://github.com/dongweiming/fastapi-mako',
    license='Apache 2',
    author='LouisYoung',
    author_email='yangzhikai2007@163.com',
    description='Mako templating support for FastAPI.',
    long_description=__doc__,
    py_modules=['fastapi_mako'],
    zip_safe=False,
    platforms='any',
    install_requires=['starlette', 'Mako'],
    classifiers=[
        'Framework :: AsyncIO',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)