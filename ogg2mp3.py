#!/usr/bin/env python

"""
Generate a list of all ogg files found below a specified root directory.
Convert the ogg files to mp3 format: oggdec(ogg) => wav; lame(wav)=>mp3.
        
Requires:

+ [oggdec](http://wiki.xiph.org/Vorbis-tools): a program for reading ogg files.
+ [lame](http://lame.sourceforge.net/): a program for converting wav to mp3

If run as main, ie, calling:

    python ogg2mp3.py

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


def ogg2mp3(rootdir):
    """
    Recursively walks the tree under the ``rootdir`` to finds all the flac
    files. Then converts those files from ogg to mp3.
    
    .. warning:: Currently removes source files after conversion.
        
        ``Args``:
            rootdir (str): The root directory to search for files.
        
        ``Kwargs``:
            <name> (<type>)[<default>]:  <A brief description>.
    
    """
    oggfiles = get_files(rootdir, ["ogg", "ogm"])
    
    for oggfilename in oggfiles:
        LOG.info("File: %s" % oggfilename)
        ret1 = os.spawnlp(os.P_WAIT, 'oggdec', 'oggdec', oggfilename)
        if (ret1 == 0):
            LOG.info("Seems to have converted ogg => wav successfully;")
            rawfilename = os.path.splitext(oggfilename)
            wavfilename = rawfilename[0] + '.wav'
            mp3filename = rawfilename[0] + '.mp3'
            LOG.info("Converting  wav => mp3...")
            ret2 = os.spawnlp(os.P_WAIT, 'lame', 'lame', "-h", "--quiet", wavfilename, mp3filename)
            if (ret2 == 0):
                LOG.info("Seems to have completed successfully, cleaning up...")
                os.spawnlp(os.P_WAIT, 'rm', 'rm', wavfilename)
                os.spawnlp(os.P_WAIT, 'rm', 'rm', oggfilename)
        else:
            LOG.error("Seems to have failed at the ogg => wav conversion.")



if __name__ is "__main__":
    ROOT_DIR = os.getcwd()
    ogg2mp3(ROOT_DIR)





###############################





# def get_files(extensions):
#     files = os.listdir(os.getcwd())
#     retfiles = []
#     for file in files:
#         for extension in extensions:
#             if (file.endswith(extension)):
#                 retfiles.append(file)
    
#     return retfiles


###############################3




#import os
#import sys
#
#rootdir = sys.argv[1]
#
#for root, subFolders, files in os.walk(rootdir):
#    outfileName = os.path.join(root, "py-outfile.txt")
#    print "outfileName is " + outfileName
#    with open( outfileName, 'w' ) as folderOut:
#        for folder in subFolders:
#            print "%s has subdirectory %s" % (root, folder)
#        
#        for filename in files:
#            filePath = os.path.join(root, filename)
#            
#            with open( filePath, 'r' ) as f:
#                toWrite = f.read()
#                folderOut.write("The file %s contains %s" % (filePath, toWrite))
#                folderOut.write( toWrite )






