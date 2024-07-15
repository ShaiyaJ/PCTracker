# PC tracker
## About
PC tracker is a simple python program that takes a file as input and plays sound from that file.

## Use
Windows is the target platform for this project.

### Writing files
To write a PC tracker file you just write in the raw frequencies.

Each line has a target duration of 100ms and the right-most "channel" gets highest priority per line.

### Playing files
Run main.py with a single argument, the path to the target file.

If you see any python errors come up, then chances are the file that you tried to play was invalid. 

## Planned features
This was just a quick weekend project to get back into python programming. I may not return to this project again. If I do then the planned features would be:

* A mode for true multi-channel playback
* A mode for files with notes instead of raw frequencies
* Writing custom error messages for invalid files rather than untidy and confusing python errors
* Cross platform support (currently the program only functions on windows machines)
* A simple UI tracker to help write files (although this may be a separate project altogether)