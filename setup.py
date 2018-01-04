import os
import setuptools


setuptools.setup(
    name="fleep",
    version="0.3.6",
    description="File format determination library",
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
        "Topic :: Software Development",
    ],
    python_requires=">=3",
    include_package_data=True,
    zip_safe=False
)
