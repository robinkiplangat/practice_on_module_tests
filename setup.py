from setuptools import setup, find_packages


setup(
    name='practice module tests',
    version='0.1.0',
    packages=find_packages("src"),
    package_dir={"": "src"},
    author="Robin Kiplangat",
    install_requires=["jupyter==1.0.0",
                        "matplotlib==3.1.1",
                        "numpy==1.21.0",
                        "pytest==5.2.2",
                        "pytest-mpl==0.10",
                        "pytest-mock==1.11.2",
                        "scipy==1.3.1",
                        ]
)