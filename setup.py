from setuptools import setup, find_packages


setup(
    name="practice module tests",
    version="0.1.0",
    packages=find_packages(),
    author="Robin Kiplangat",
    install_requires=[
        "pytest-mpl==0.10",
        "pytest-mock==1.11.2",
        "scipy==1.3.1",
        "matplotlib==3.4.2",
        "numpy==1.20.1",
        "pytest==6.2.5",
        "setuptools==59.0.1",
    ],
)
