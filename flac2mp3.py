#!/usr/bin/env python

"""
Generate a list of all flac files found below a specified root directory.
Convert the flac files to mp3 format: flalc(flac) => raw; lame(raw)=>mp3.

+ [flac](https://xiph.org/flac/): a program for reading, writing, and querying
    FLAC files.
+ [lame](http://lame.sourceforge.net/): a program for converting wav to mp3
If run as main, ie, calling:

    python flac2mp3.py

the current working directory(cwd) will be set as ``rootdir``.

.. moduleauthor:: Stuart A. Knock <stuart.knock@gmail.com>

"""

# From Python
import os
import os.path
import logging
LOG = logging.getLogger(__name__)

# From converter
from utils import get_files


def flac2mp3(rootdir):
    """
    Recursively walks the tree under the ``rootdir`` to finds all the flac
    files. Then converts those files from flac to mp3.
        
        ``Args``:
            rootdir (str): The root directory to search for files.
            rootdir (<type>)[<default>]:  <A brief description>.
    
    """
    
    flacfiles = get_files(rootdir, ["flac", "FLAC"])
    LOG.info("Found %d files to convert" % len(flacfiles))
    
    for flacfilename in flacfiles:
        LOG.info("File: %s" % flacfilename)
        rawfilename = os.path.splitext(flacfilename)
        decfilename = rawfilename[0]
        ret1 = os.spawnlp(os.P_WAIT, 'flac', 'flac', "-d", "-o", decfilename, flacfilename)
        if (ret1 == 0):
            LOG.info("Seems to have decoded flac file successfully;")
            mp3filename = rawfilename[0] + '.mp3'
            LOG.info("Converting  raw => mp3...")
            ret2 = os.spawnlp(os.P_WAIT, 'lame', 'lame', "-h", "--quiet", decfilename, mp3filename)
            if (ret2 == 0):
                LOG.info("Seems to have completed successfully, cleaning up...")
                os.spawnlp(os.P_WAIT, 'rm', 'rm', decfilename)
            else:
                LOG.error("Seems to have failed at the step using lame to convert raw to mp3...")
        else:
            LOG.error("Seems to have failed at the decoded flac step...")



if __name__ is "__main__":
    ROOT_DIR = os.getcwd()
    flac2mp3(ROOT_DIR)
