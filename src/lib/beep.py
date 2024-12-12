# Cross-platform implementation of a beep function
import sys

def beep():
    raise NotImplementedError


if sys.platform == "win32":
    import winsound 

    def beep(freq: int, duration: int): # TODO: try catch the ValueError (frequency must be in 37 thru 32767) to allow for "0" to act as spacer 
        print(freq)
        winsound.Beep(freq, duration)

# elif sys.platform() == "cygwin":
#     def beep(freq: int, duration: int):
#         pass

# elif sys.platform() == "linux":
#     def beep(freq: int, duration: int):
#         pass

# elif sys.platform() == "darwin":
#     def beep(freq: int, duration: int):
#         pass