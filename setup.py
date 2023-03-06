from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="kratos",
    version="0.0.10",
    description="A library to deal with Data Engineering common activities",
    package_dir={"": "lib"},
    packages=find_packages(where="lib"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vireboll/kratos",
    author="Víctor Rebolledo Lorca",
    author_email="vireboll@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    extras_require={
        "dev": [],
    },
    python_requires=">=3.10",
)
