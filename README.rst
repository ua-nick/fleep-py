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

Example
-------

fleep has only one function **get()**. It takes two arguments:

-  *input* -> data to be processed: path to the file or array of bytes
-  *output* (optional) -> format of output values: "extension" (by default) or "mime"

There are some examples:

.. code:: python

    import fleep

    print(fleep.get(input="path_to_jpg_image")) # prints ['jpg']

.. code:: python

    import fleep

    file = open("path_to_flac_file", "rb").read(1024)
    print(fleep.get(input=file, output="mime")) # prints ['audio/flac']

Supported formats
-----------------

There is a list of supported formats:

*IMAGE:*

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

*RAW IMAGE:*

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

*AUDIO:*

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

*VIDEO:*

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

*DOCUMENT:*

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

*ARCHIVE:*

-  7Z (7-Zip Archive)
-  RAR (Roshal Archive)
-  TAR.Z (GNU Compressed Archive)
-  GZ (GZIP Archive)
-  ZIP (ZIP Archive)
-  DMG (Apple Disk Image)
-  ISO (Disk Image)

*EXECUTABLE:*

-  COM (Component Object Model)
-  EXE (Portable Executable)
-  JAR (Java Archive)

*FONT:*

-  TTF (TrueType File)
-  OTF (OpenType File)

*OTHER:*

-  DLL (Dynamic Link Library)
-  SYS (Windows System File)
-  SQLITE (SQLite Database File)

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
.. |pypi version| image:: https://img.shields.io/badge/pypi-v0.3.4-blue.svg
   :target: https://pypi.python.org/pypi/fleep
.. |license| image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://github.com/floyernick/fleep/blob/master/LICENSE