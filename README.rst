fleep
=====

File format determination library for Python

|python version| |pypi version| |license|

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

-  Python >= 3.0

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

Examples
--------

.. code:: python

    import fleep

    with open("png_image", "rb") as file:
        info = fleep.get(file.read(128))

    print(info.type)  # prints ['image']
    print(info.extension)  # prints ['png']
    print(info.mime)  # prints ['image/png']

    print(info.type_matches("image"))  # prints True
    print(info.extension_matches("gif"))  # prints False
    print(info.mime_matches("image/png"))  # prints True

Tests
-----

You can find tests in *tests* folder. There are results of *speed test*:

**Workstation**

-  Python 3.6 x64 bit
-  Windows 10 Home x64 bit
-  Intel Pentium G4620 3.70GHz
-  Kingston DDR4-2400 4096MB x2
-  Kingston SSD 120GB

**Results**

+-----------+------------------+------------------+------------------+
| Iteration | Min. time (sec.) | Max. time (sec.) | Avg. time (sec.) |
+===========+==================+==================+==================+
| 1         | 0.0              | 0.0010326        | 0.0000847        |
+-----------+------------------+------------------+------------------+
| 2         | 0.0              | 0.0010331        | 0.0000817        |
+-----------+------------------+------------------+------------------+
| 3         | 0.0              | 0.0010362        | 0.0000820        |
+-----------+------------------+------------------+------------------+
| 4         | 0.0              | 0.0010309        | 0.0000832        |
+-----------+------------------+------------------+------------------+
| 5         | 0.0              | 0.0010326        | 0.0000836        |
+-----------+------------------+------------------+------------------+

Supported Formats
-----------------

There is a list of supported formats (in alphabetical order):

*Image:*

-  AI
-  ARW
-  BMP
-  CR2
-  CRW
-  DNG
-  EPS
-  ERF
-  GIF
-  ICO
-  JP2
-  JPEG
-  NEF
-  NRW
-  ORF
-  PEF
-  PNG
-  PSD
-  RAF
-  RAW
-  RW2
-  SRW
-  TIFF
-  WEBP
-  X3F

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

-  CAT
-  DLL
-  REG
-  SYS

*Database:*

-  SQLITE

Development Status
------------------

fleep is in *Alpha* status, so we add new features quite often.

License
-------

This project is licensed under the *MIT License*.

Contributing
------------

It would be nice to determine more formats. You can help us to deal with it!

Authors
-------

**Mykyta Paliienko** - `GitHub profile`_

.. _GitHub profile: https://github.com/floyernick

.. |python version| image:: https://img.shields.io/badge/python-3-blue.svg
.. |pypi version| image:: https://img.shields.io/badge/pypi-v0.4.3-blue.svg
   :target: https://pypi.python.org/pypi/fleep
.. |license| image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://github.com/floyernick/fleep/blob/master/LICENSE