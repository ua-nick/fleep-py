import os
import setuptools


setuptools.setup(
    name="fleep",
    version="0.2.0.0",
    description="File format identification library",
    long_description=open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "README.rst"), "r").read(),
    url="https://github.com/floyernick/fleep",
    author="Mykyta Paliienko",
    author_email="floyernick@gmail.com",
    license="MIT",
    packages=["fleep"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development",
    ],
    python_requires=">=3",
    include_package_data=True,
    zip_safe=False
)
