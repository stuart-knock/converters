#!/usr/bin/env python

"""
A set of utility functions used by the converter package.

.. moduleauthor:: Stuart A. Knock <stuart.knock@gmail.com>

"""

import os
import os.path


def get_files(rootdir, extensions):
    """
    Return a list of files (full paths), found by recursively walking the tree
    under the ``rootdir``, which end with ``extensions``.

        ``Args``:
            rootdir (str): The root directory to search for files.
            extensions (list[str]): A list containing the file extensions.

       `` Returns``:
            (list[str]): A list containing full paths to all the files with an 
                extension in *extensions*.
    """
    retfiles = []
    for root, subfolders, files in os.walk(rootdir):
        for filename in files:
            if filename.rsplit(".")[-1] in extensions:
                retfiles.append(os.path.join(root, filename))
    
    return retfiles
