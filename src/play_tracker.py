from tracker import Tracker

import platform

if platform.system() == "Linux":
    def play_beep(frequency: int):
        pass

elif platform.system() == "Darwin":
    def play_beep(frequency: int):
        pass

elif platform.system() == "Windows":
    import winsound

    def play_beep(frequency: int):
        winsound.Beep(frequency, 100) 

else:
    raise Exception

def play(inp: Tracker):
    for frequency in inp:
        play_beep(frequency)

