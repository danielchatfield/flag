import re
import ast
from setuptools import setup


_version_re = re.compile(r'__version__\s+=\s+(.*)')


with open('flag/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    name='Flag',
    version=version,
    author='Daniel Chatfield',
    author_email='chatfielddaniel@gmail.com',
    packages=['flag'],
    include_package_data=True
)
