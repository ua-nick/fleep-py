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

fleep has main function *get()* that determines file format. It takes an array of bytes (128 bytes are enough) as an argument and returns an instance of class *Info* with the following arguments:

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


    with open("testfile", "rb") as file:
        info = fleep.get(file.read(128))

    print(info.type)  # prints ['image']
    print(info.extension)  # prints ['png']
    print(info.mime)  # prints ['image/png']

    print(info.type_matches("image"))  # prints True
    print(info.extension_matches("gif"))  # prints False
    print(info.mime_matches("image/png"))  # prints True

Tests
-----

You can find tests in *tests* folder. There are results of *speedtest*:

**Workstation**

-  Windows 10 Home x64 bit
-  Intel Pentium G4620 3.70GHz
-  Kingston DDR4-2400 4096MB x2
-  Kingston SSD 120GB

**Results**

+-----------+-----------------+
| Iteration | Max time (sec.) |
+===========+=================+
| 1         | 0.01580         |
+-----------+-----------------+
| 2         | 0.00802         |
+-----------+-----------------+
| 3         | 0.00501         |
+-----------+-----------------+
| 4         | 0.01591         |
+-----------+-----------------+
| 5         | 0.00651         |
+-----------+-----------------+

Supported Formats
-----------------

There is a list of supported formats:

*Image:*

-  AI (Adobe Illustrator Artwork)
-  BMP (Bitmap Picture)
-  GIF (Graphics Interchange Format)
-  JPEG (Joint Photographic Experts Group)
-  JP2 (JPEG 2000)
-  PNG (Portable Network Graphics)
-  WEBP (Google Web Image)
-  ICO (Windows Icon)
-  PSD (Photoshop Document)
-  EPS (Encapsulated PostScript)
-  TIFF (Tagged Image File Format)
-  RAW (Raw Image)
-  ARW (Sony RAW)
-  X3F (Sigma RAW)
-  SRW (Samsung RAW)
-  PEF (Pentax RAW)
-  RW2 (Panasonic Lumix RAW)
-  ORF (Olympus RAW)
-  NEF (Nikon Electronic Format)
-  NRW (Nikon Coolpix RAW)
-  DNG (Adobe Digital Negative)
-  RAF (Fuji RAW)
-  ERF (Epson RAW)
-  CRW (Canon RAW)
-  CR2 (Canon RAW Version 2)

*Audio:*

-  AIFF (Audio Interchange File Format)
-  AAC (Advanced Audio Coding)
-  MIDI (Musical Instrument Digital Interface)
-  MP3 (MPEG Audio Layer III)
-  M4A (Apple Audio Container)
-  OGA (OGG Audio)
-  WAV (Waveform Audio File Format)
-  WMA (Windows Media Audio)
-  FLAC (Free Lossless Audio Codec)
-  MKA (Matroska Audio)
-  AU (Unix sound)
-  RA (Real Audio File)
-  AMR (Adaptive Multi-Rate Audio Codec)
-  AC3 (Audio Codec 3)
-  VOC (Creative Voice File)

*Video:*

-  3G2 (3GPP2 File Format)
-  3GP (3GPP File Format)
-  AVI (Audio Video Interleave)
-  FLV (Flash Video)
-  M4V (Apple Video Container)
-  MKV (Matroska Video)
-  MOV (Apple QuickTime Movie)
-  MP4 (MPEG-4 Video)
-  SWF (Small Web Format)
-  MPG (MPEG Video)
-  VOB (DVD-Video Object)
-  WMV (Windows Media Video)
-  ASF (Advanced Systems Format)
-  OGV (OGG Video)
-  WEBM (Google Web Movie)

*Document:*

-  ODP (OpenDocument Presentation)
-  ODS (OpenDocument Spreadsheet)
-  ODT (OpenDocument Text)
-  DOC (Microsoft Word Binary File Format)
-  PPS (Microsoft PowerPoint Binary File Format)
-  PPT (Microsoft PowerPoint Binary File Format)
-  XLS (Microsoft Excel Binary File Format)
-  DOCX (Word Extensions to the Office Open XML File Format)
-  PPTX (PowerPoint Extensions to the Office Open XML File Format)
-  XLSX (Excel Extensions to the Office Open XML File Format)
-  PAGES (Apple Pages Document)
-  KEY (Apple Keynote Presentation)
-  NUMBERS (Apple Numbers Spreadsheet)
-  PDF (Portable Document Format)
-  RTF (Rich Text Format)
-  EPUB (Electronic Publication)
-  XML (Extensible Markup Language)

*Archive:*

-  7Z (7-Zip Archive)
-  RAR (Roshal Archive)
-  TAR.Z (GNU Compressed Archive)
-  GZ (GZIP Archive)
-  ZIP (ZIP Archive)
-  DMG (Apple Disk Image)
-  ISO (Disk Image)

*Executable:*

-  COM (Component Object Model)
-  EXE (Portable Executable)
-  JAR (Java Archive)

*Font:*

-  TTF (TrueType File)
-  OTF (OpenType File)

*System:*

-  DLL (Dynamic Link Library)
-  SYS (Windows System File)

*Database:*

-  SQLITE (SQLite Database File)

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
.. |pypi version| image:: https://img.shields.io/badge/pypi-v0.4.0-blue.svg
   :target: https://pypi.python.org/pypi/fleep
.. |license| image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://github.com/floyernick/fleep/blob/master/LICENSE