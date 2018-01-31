fleep
=====

File format determination library for Python

|pypi version| |python version| |license|

Getting Started
---------------

**fleep** is a library that determines file format by file signature (also known as "magic number").

Installation
------------

You can install fleep using *pip*. Simply run in CLI:

::

    pip install fleep

Requirements
------------

-  Python >= 3.1

In Use
------

fleep has main function *get()* that determines file format. It takes byte sequence (128 bytes are enough) as an argument and returns an instance of class *Info* with the following arguments:

-  *type* -> list of suitable file types
-  *extension* -> list of suitable file extensions
-  *mime* -> list of suitable file MIME types

You may presume that first element in list will be the most suitable.

Also an instance of class *Info* has the following methods:

-  *type_matches()* -> checks if file type matches with given type as an argument
-  *extension_matches()* -> checks if file extension matches with given extension as an argument
-  *mime_matches()* -> checks if file MIME type matches with given MIME type as an argument

There are 3 more functions:

-  *supported_types()* -> returns a list of supported file types
-  *supported_extensions()* -> returns a list of supported file extensions
-  *supported_mimes()* -> returns a list of supported file MIME types

Examples
--------

You can find examples in *examples* folder. There is a simple example:

.. code:: python

    import fleep

    with open("png_image", "rb") as file:
        info = fleep.get(file.read(128))

    print(info.type)  # prints ['raster-image']
    print(info.extension)  # prints ['png']
    print(info.mime)  # prints ['image/png']

    print(info.type_matches("raster-image"))  # prints True
    print(info.extension_matches("gif"))  # prints False
    print(info.mime_matches("image/png"))  # prints True

Tests
-----

You can find tests in *tests* folder. There are results of speed test:

**Workstation**

-  Python 3.6 x64 bit
-  Windows 10 Home x64 bit
-  Intel Pentium G4620 3.70GHz
-  Kingston DDR4-2400 8192MB
-  Kingston SSD 120GB 550MB/s

**Results**

*Note:* 0.0012345 -> time in seconds

+-----------+---------+-----------+-----------+
| Iteration | Minimum | Maximum   | Average   |
+===========+=========+===========+===========+
| 1         | 0.0     | 0.0005312 | 0.0000851 |
+-----------+---------+-----------+-----------+
| 2         | 0.0     | 0.0005360 | 0.0000858 |
+-----------+---------+-----------+-----------+
| 3         | 0.0     | 0.0005236 | 0.0000837 |
+-----------+---------+-----------+-----------+
| 4         | 0.0     | 0.0005035 | 0.0000833 |
+-----------+---------+-----------+-----------+
| 5         | 0.0     | 0.0005295 | 0.0000835 |
+-----------+---------+-----------+-----------+

Supported Formats
-----------------

There is a list of supported formats (in alphabetical order):

*Raster Image:*

-  BMP
-  GIF
-  ICO
-  JP2
-  JPEG
-  PNG
-  PSD
-  TIFF
-  WEBP

*Raw Image:*

-  ARW
-  CR2
-  CRW
-  DNG
-  ERF
-  NEF
-  NRW
-  ORF
-  PEF
-  RAF
-  RAW
-  RW2
-  SRW
-  X3F

*Vector Image:*

-  AI
-  EPS

*3D Image:*

-  C4D
-  FBX
-  MA
-  MS3D
-  MTL
-  OBJ
-  PLY
-  WRL
-  X3D
-  XSI

*Audio:*

-  AAC
-  AC3
-  AIFF
-  AMR
-  AU
-  FLAC
-  M4A
-  MIDI
-  MKA
-  MP3
-  OGA
-  RA
-  VOC
-  WAV
-  WMA

*Video:*

-  3G2
-  3GP
-  ASF
-  AVI
-  FLV
-  M4V
-  MKV
-  MOV
-  MP4
-  MPG
-  OGV
-  SWF
-  VOB
-  WEBM
-  WMV

*Document:*

-  DOC
-  DOCX
-  EPUB
-  KEY
-  NUMBERS
-  ODP
-  ODS
-  ODT
-  PAGES
-  PDF
-  PPS
-  PPT
-  PPTX
-  RTF
-  XLS
-  XLSX
-  XML

*Archive:*

-  7Z
-  DMG
-  GZ
-  ISO
-  RAR
-  TAR.Z
-  ZIP

*Executable:*

-  COM
-  EXE
-  JAR

*Font:*

-  OTF
-  TTF
-  WOFF
-  WOFF2

*System:*

-  CAB
-  CAT
-  DLL
-  DRV
-  REG
-  SDB
-  SYS

*Database:*

-  SQLITE

Changelog
---------

You can find changelog in *CHANGELOG.md* file.

License
-------

This project is licensed under the *MIT License*.

Authors
-------

**Mykyta Paliienko** - `GitHub profile`_

.. _GitHub profile: https://github.com/floyernick

.. |pypi version| image:: https://img.shields.io/badge/pypi-v1.0.1-blue.svg
   :target: https://pypi.python.org/pypi/fleep
.. |python version| image:: https://img.shields.io/badge/python-3-blue.svg
.. |license| image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://github.com/floyernick/fleep/blob/master/LICENSE