import setuptools

from pprintast.pprintast import __VERSION__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pprintast",
    version=__VERSION__,
    author="Travis Clarke, Alex Leone",
    author_email="travis.m.clarke@gmail.com, acleone@gmail.com",
    description="A AST pretty printer for python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/clarketm/pprintast",
    packages=setuptools.find_packages(),
    py_modules=["pprintast"],
    entry_points={"console_scripts": ["pprintast=pprintast.pprintast:cli"]},
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Console",
    ],
)
