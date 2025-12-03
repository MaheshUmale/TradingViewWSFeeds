
from setuptools import setup, find_packages

setup(
    name='tradingview-api',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'requests',
        'websockets',
    ],
)
