# RED
This is a file encryption/format/interpretation called RED. It's a terrible format for images. RED files are usually about 30,000 times the size of the original image. They are encoded one pixel at a time and all sorts of conversions are done throughout the process. I never recommend using this image format.

Update:

I added a new script to Application.py that allows you to view the image while still in RED format. The script uses 2 threads because it would take a really long time without multi-threading.

Future Goals:

I want to split into 4 or even 8 threads. Also I would like to make the conversions multi-threaded.
