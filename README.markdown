WARNING: This is an old version, a rewrite is in process!

The HAL Engine
==============

HAL is an experimental, multi-media chatterbot utilizing a compact and fast
markup language. He can solve large mathematical equations, tell what time
it is, and even answer questions with information retrieved from Wikipedia.
We have released three versions of HAL, which you can download from our
website at http://dev.halbot.co.cc.

HAL on Windows
--------------

Download a pre-packaged version from the website and install it. Enjoy.

HAL on Linux
------------

1. Read the "Requirements" section
2. You need to clone the git repository, then compile the c++ directory using
linux.mak. `make -f linux.mak`
3. Now run `python HALcon.py` in the root directory of HAL.
4. If you got exceptions, try fixing them, and submit as patches.

Note that I have only tested it on Ubuntu 12.04 LTS.

Requirements
------------

The requirement only applies if you are downloading the git version,
Windows users are adviced to download the pre-build packages, unless
they need to develop HAL.

1. boost_python, boost_regex (only if used with GCC) On Ubuntu:
`sudo apt-get install libboost-dev libboost-python-dev libboost-regex-dev`
2. gmpy2, from http://code.google.com/p/gmpy/.
3. pyephem (for weather plugin).

The HAL License
---------------

###For end users

The HAL software is provided as-is. There are no catastrophic bugs in it as
far as we know, but in the case that this program does fry your computer,
the creators of this software will not be held responsible. You agree to
these terms when you download HAL, clone the repository, get the source
from anywhere, etc.

###For Developers

The HAL source is dual licensed under (TBD) and the Death and Repudiation
License.

####TBD License

For now: Any use of the source code must be authorized by the author before
a license is decided.

####Death and Repudiation License

This software may not be used directly by any living being.  ANY use of this
software (even perfectly legitimate and non-commercial uses) until after death
is explicitly restricted.  Any living being using (or attempting to use) this
software will be punished to the fullest extent of the law.

For your protection, corpses will not be punished.  We respectfully request 
that you submit your uses (revisions, uses, distributions, uses, etc.) to 
your children, who may vicariously perform these uses on your behalf.  If 
you use this software and you are found to be not dead, you will be punished 
to the fullest extent of the law.

If you are found to be a ghost or angel, you will be punished to the fullest
extent of the law.

After your following the terms of this license, the author has vowed to
repudiate your claim, meaning that the validity of this contract will no
longer be recognized. This license will be unexpectedly revoked (at a time
which is designated to be most inconvenient) and involved heirs will be
punished to the fullest extent of the law.

Furthermore, if any parties (related or non-related) escape the punishments
outlined herein, they will be severely punished to the fullest extent of a
new revised law that (1) expands the statement "fullest extent of the law"
to encompass an infinite duration of infinite punishments and (2) exacts
said punishments upon all parties (related or non-related).

-- from the syck library
