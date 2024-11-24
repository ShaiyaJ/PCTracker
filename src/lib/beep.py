import sys

if sys.platform() == "win32":
    import winsound 

    def beep(freq: int, duration: int):
        winsound.Beep(freq, duration)

elif sys.platform() == "cygwin":
    def beep(freq: int, duration: int):
        pass

elif sys.platform() == "linux":
    def beep(freq: int, duration: int):
        pass

elif sys.platform() == "darwin":
    def beep(freq: int, duration: int):
        pass