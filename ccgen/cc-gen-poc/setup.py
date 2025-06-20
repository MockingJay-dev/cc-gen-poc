# setup.py

from setuptools import setup, find_packages

setup(
    name="ccgen-poc",
    version="0.1.0",
    description="POC credit-card data generator (all fictional).",
    author="Your Name",
    license="MIT",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "ccgen=ccgen.cli:main"
        ]
    },
    install_requires=[],
    python_requires=">=3.7",
)

