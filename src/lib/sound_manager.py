from .beep import beep
import multiprocessing as mp

class SoundManager:
    playback: list[list[int]]
    playhead: int
    frame_duration: int

    def play(self):
        beep(self.playback[self.playhead][-1], self.frame_duration)
        self.playhead += 1

    def play_loop(self):        # Plays until the end of a song
        while self.playhead < len(self.playback):
            self.play()


    def split_play(self):
        # for note in self.playback[self.playhead]:
        #     print(note)
        #     with mp.Pool() as pool:
        #         pool.apply_async(beep, args=(note, self.frame_duration))
        # print("")

        processes = []

        for note in self.playback[self.playhead]:
            processes.append(mp.Process(target=beep, args=(note, self.frame_duration)))

        for process in processes:
            process.start()

        for process in processes:
            process.join()

            
        self.playhead += 1

    def split_play_loop(self):
        while self.playhead < len(self.playback):
            self.split_play()