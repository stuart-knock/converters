# Converter

.. danger:: Most functions currently remove or overwrite source files...

.. caution:: Not well tested yet...

.. important:: Depends on tools found under Linux... May work in cygwin, but untested...  

A package containing a bunch of functions for converting files between various
file formats, primarily flac(lossless) to * (common: mp3; aac), but also from
lossy to lossy (ogg to mp3) because sometimes it's necessary.

Also functions for image resizing and conversion.

Run as main it expects rootdir, format_from, format_to, and copy/inplace.
In the absence of args it assumes current dir, flac, mp3, copy.

.. todo:: threading, ie parallel encode/decode on different files.

.. todo:: implement copy to new directory tree


##Music

### flac2mp3


### ogg2mp3
Converts ogg to mp3 in a two step process using oggdec and then lame.

-------------------------------------------------------------------------------

## Images

### resizejpg
Resizes jpg images to a horizontal size of hsize[default=480] pixels and a 
vertical size vsize[default=234] pixels.
