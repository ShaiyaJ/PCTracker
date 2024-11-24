from beep import beep

class SoundManager:
    playback: list[int]
    playhead: int
    frame_duration: int

    def play(self):
        beep(self.playback[self.playhead], self.frame_duration)
        playhead += 1

    def blocking_play(self):        # Plays until the end of a song
        while self.playhead < len(self.playback):
            play()

    def set_playhead(self, position: int):
        self.playhead = position