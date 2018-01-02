fleep
=====

File format determination library for Python

|python version| |pypi version| |license|

Getting Started
---------------

**fleep** is a library that determines file format by file signature
(also known as "magic number").

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
-  *output* (optional) -> format of output values: extension (by
   default) or MIME type

There are some examples:

.. code:: python

    import fleep

    print(fleep.get(input="path_to_jpg_image", output="extension")) # prints ['jpg']

.. code:: python

    import fleep

    file = open("path_to_flac_file", "rb").read(1024)
    print(fleep.get(input=file, output="mime")) # prints ['audio/flac']

Supported formats
-----------------

There is a list of supported formats:

*Image:*

-  ai
-  bmp
-  gif
-  jpg
-  jp2
-  png
-  webp
-  ico
-  psd
-  eps
-  tiff

*Raw Image:*

-  arw
-  x3f
-  srw
-  pef
-  rw2
-  raw
-  orf
-  nef
-  nrw
-  dng
-  raf
-  erf
-  crw
-  cr2

*Audio:*

-  aiff
-  aac
-  midi
-  mp3
-  m4a
-  oga
-  wav
-  wma
-  flac
-  mka

*Video:*

-  3g2
-  3gp
-  avi
-  flv
-  m4v
-  mkv
-  mov
-  mp4
-  swf
-  mpg
-  vob
-  wmv
-  asf
-  ogv
-  webm

*Document:*

-  odp
-  ods
-  odt
-  doc
-  pps
-  ppt
-  xls
-  docx
-  pptx
-  xlsx
-  pdf
-  rtf
-  epub

*Archive:*

-  7z
-  rar
-  tar.z
-  gz
-  zip
-  dmg
-  iso

*Executable:*

-  com
-  exe
-  jar

*Font:*

-  ttf
-  otf

*Other:*

-  dll
-  sys
-  sqlite

License
-------

This project is licensed under the *MIT License*.

Contributing
------------

It would be nice to determine more formats. You can help us to deal with
it!

Authors
-------

**Mykyta Paliienko** - `GitHub profile`_

.. _GitHub profile: https://github.com/floyernick

.. |python version| image:: https://img.shields.io/badge/python-3-blue.svg
.. |pypi version| image:: https://img.shields.io/badge/pypi-v0.3.2-blue.svg
   :target: https://pypi.python.org/pypi/fleep
.. |license| image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://github.com/floyernick/fleep/blob/master/LICENSE