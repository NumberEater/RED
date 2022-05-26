# RED
This is a file encryption/format/interpretation called RED. It's a terrible format for images. RED files are usually about 30,000 times the size of the original image. They are encoded one pixel at a time and all sorts of conversions are done throughout the process. I never recommend using this image format.

# File Info:

The main file is Application.py. That file acts as a hub for the different scripts that the applicaion uses. The three main components are the Reader, Writer, and REDReader. Reader reads the RED and converts it to PNG. Writer reads the JPG and converts it to RED. REDReader is what allows you to view RED files. Without that, the RED format wouldn't be considered as a format. My main focus for optimizations and updates is REDReader.

# Future Goals:

* 8 threaded rendering
* RED editing in REDReader
* File size optimizations
* Multi-threaded conversions

# Requirements:

The only requirement that isn't included with python 3.8 is pillow.
