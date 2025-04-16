from setuptools import setup, find_packages

setup(
    name="hindi-tokenizer",
    version="0.1.0",
    packages=find_packages(),
    description="A simple Hindi text tokenizer for NLP",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Lahari Acharya",
    author_email="lahariacharya.31@gmail.com",
    url="https://github.com/lahariacharya/HindiTokenizerNLP",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
