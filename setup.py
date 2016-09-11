from setuptools import setup

setup(
    name='pytest-auto-parametrize',
    py_modules=['pytest_auto_parametrize'],
    entry_points={
        'pytest11': ['pytest_auto_parametrize = pytest_auto_parametrize'],
    },
    classifiers=[
        "Framework :: Pytest",
    ],
)
