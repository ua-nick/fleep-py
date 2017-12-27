fleep
=====

File format identification library

Getting Started
---------------

**fleep** is a Python library, that identifies file format by file
signature.

Installation
------------

Simply run in console:

::

    pip install fleep

Example
-------

It has only one function **get()**, that takes path to the file as an
argument and returns a list of suitable extensions. There is a simple example:

.. code:: python

    import fleep
    print(fleep.get(path="PATH_TO_THE_FILE") # prints ['some_extension_1', 'some_extension_2']

Supported formats
-----------------

There is a list of supported formats

- aiff
- cda
- midi
- mp3
- m4a
- ogg
- oga
- wav
- wma
- flac
- 3g2
- 3gp
- 3gg
- avi
- flv
- m4v
- mkv
- mov
- mp4
- swf
- mpg
- vob
- wmv
- ogv
- webm
- 7z
- rar
- rpm
- tar.z
- gz
- zip
- dmg
- iso
- dll
- sys
- com
- exe
- jar
- ai
- bmp
- gif
- jpg
- ico
- psd
- tiff
- odp
- pps
- ppt
- pptx
- ods
- xls
- xlsx
- odt
- doc
- docx
- pdf
- rtf
- sql


License
-------

This project is licensed under the *MIT License*.

Contributing
------------

It would be nice to identify more formats. You can help us to
deal with it!

Authors
-------

**Mykyta Paliienko** - `GitHub profile`_

.. _GitHub profile: https://github.com/floyernick