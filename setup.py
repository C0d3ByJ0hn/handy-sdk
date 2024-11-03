from setuptools import setup, find_packages

setup(
    name='handy_sdk',
    version='0.1.0',
    description='A Python SDK for the Handy API',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
