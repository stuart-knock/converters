#!/usr/bin/env python

"""
Generate a list of all jpg files found below a specified root directory.
Resize the jpg files to hsize by vsize:

If run as main, ie, calling:

    python resizejpg.py

the current working directory(cwd) will be set as ``rootdir``, and jpg will be
resized to hsize=480, vsize=234.
  
.. moduleauthor:: Stuart A. Knock <stuart.knock@gmail.com>

"""

# From Python
import os
import os.path
import logging
LOG = logging.getLogger(__name__)

# From converter
from utils import get_files


def resize_jpg(rootdir, hsize=480, vsize=234):
    """
    Use ImageMagic's convert function to resize jpg images.
        
        ``Args``:
            rootdir (str): The root directory to search for files.
        
        ``Kwargs``:
            hsize (int)[480]: horizontal size in pixels of the resized images.
            vsize (int)[234]: vertical size in pixels  of the resized images.
        
        `` Requires``:
            convert: a program supporting a broad range of image manipulations
                -- it is part of ImageMagic.
    
    """
    jpgfiles = get_files(rootdir, ["jpg", "JPG"])
    
    hvsize = ' %sx%s' % (hsize, vsize)
    
    for jpgfilename in jpgfiles:
        LOG.info("File: %s" % jpgfilename)
        ret1 = os.spawnlp(os.P_WAIT, 'convert', 'convert', '-resize', hvsize, 
                          jpgfilename, jpgfilename)



if __name__ is "__main__":
    ROOT_DIR = os.getcwd()
    resize_jpg(ROOT_DIR)

