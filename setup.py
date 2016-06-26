import re
import ast
from setuptools import setup


_version_re = re.compile(r'__version__\s+=\s+(.*)')


with open('flag/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

with open('README.rst', 'r') as f:
    readme = f.read()

setup(
    name='Flag',
    version=version,
    description="Simple flag library for python",
    long_description=readme,
    url='http://github.com/danielchatfield/flag',
    author='Daniel Chatfield',
    author_email='chatfielddaniel@gmail.com',
    packages=['flag'],
    include_package_data=True
)
