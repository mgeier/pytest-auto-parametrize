from setuptools import setup
from setuptools.command.test import test as TestCommand
import sys

__version__ = 'unknown'

# "import" __version__
for line in open('pytest_auto_parametrize.py'):
    if line.startswith('__version__'):
        exec(line)
        break


class PyTest(TestCommand):
    """Enable "python setup.py test".
    
    Stripped down from:
    http://doc.pytest.org/en/latest/goodpractices.html#manual-integration
    """

    def run_tests(self):
        import pytest
        sys.exit(pytest.main([]))


setup(
    name='pytest-auto-parametrize',
    py_modules=['pytest_auto_parametrize'],
    version=__version__,
    author='Matthias Geier',
    author_email='Matthias.Geier@gmail.com',
    description='pytest plugin: avoid repeating arguments in parametrize',
    long_description=open('README.rst').read(),
    license='MIT',
    keywords='parametrized testing'.split(),
    url='https://github.com/mgeier/pytest-auto-parametrize',
    platforms='any',
    zip_safe=True,
    classifiers=[
        'Framework :: Pytest',
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
    ],
    entry_points={
        'pytest11': ['pytest_auto_parametrize = pytest_auto_parametrize'],
    },
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
)
