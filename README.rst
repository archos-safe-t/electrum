Electrum BCD - Lightweight Bitcoin Diamond client
=====================================

::

  Licence: MIT Licence
  Author: BCD Developer
  Language: Python
  Homepage: https://github.com/eveybcd/electrum



Getting started
===============

Electrum BCD is a pure python application. If you want to use the
Qt interface, install the Qt dependencies::

    sudo apt-get install python3-pyqt5

If you downloaded the official package (tar.gz), you can run
Electrum BCD from its root directory, without installing it on your
system; all the python dependencies are included in the 'packages'
directory. To run Electrum from its root directory, just do::

    ./electrum

You can also install Electrum BCD on your system, by running this command::

    sudo apt-get install python3-setuptools
    pip3 install .[fast]

This will download and install the Python dependencies used by
Electrum BCD, instead of using the 'packages' directory.

If you cloned the git repository, you need to compile extra files
before you can run Electrum BCD. Read the next section, "Development
Version".



Development version
===================

Check out the code from GitHub::

    git clone git://github.com/eveybcd/electrum.git
    cd electrum

Run install (this should install dependencies)::

    pip3 install .[fast]

Render the SVG icons to PNGs (optional)::

    for i in lock unlock confirmed status_lagging status_disconnected status_connected_proxy status_connected status_waiting preferences; do convert -background none icons/$i.svg icons/$i.png; done

Compile the icons file for Qt::

    sudo apt-get install pyqt5-dev-tools
    pyrcc5 icons.qrc -o gui/qt/icons_rc.py

Compile the protobuf description file::

    sudo apt-get install protobuf-compiler
    protoc --proto_path=lib/ --python_out=lib/ lib/paymentrequest.proto

Create translations (optional)::

    sudo apt-get install python-requests gettext
    ./contrib/make_locale




Creating Binaries
=================


To create binaries, create the 'packages' directory::

    ./contrib/make_packages

This directory contains the python dependencies used by Electrum.

Mac OS X / macOS
--------

See `contrib/build-osx/`.

Windows
-------

See `contrib/build-wine/`.


Android
-------

See `gui/kivy/Readme.txt` file.
