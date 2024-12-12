import argparse
from pathlib import Path

import lib

def output(ipath, opath, split=False, frame_duration=False, playback_head=False):
    pass


def play(ipath, split=False, frame_duration=False, playback_head=False):
    if split:
        # Initialise data
        parsed = lib.file_parser.parse(ipath)
        manager = lib.sound_manager.SoundManager()

        # Assign the file-defined values to the manager
        manager.playback = parsed[1]
        manager.playhead = 0
        manager.frame_duration = parsed[0]

        # Overwrite default values with args if they are defined
        if frame_duration:
            manager.frame_duration = frame_duration
        
        if playback_head:
            manager.playhead = playback_head

        # Play manager
        manager.split_play_loop()
    else:
        # Initialise manager and data
        parsed = lib.file_parser.parse(ipath)
        manager = lib.sound_manager.SoundManager()

        # Assign the file-defined values to the manager
        manager.playback = parsed[1]
        manager.playhead = 0
        manager.frame_duration = parsed[0]

        # Overwrite default values with args if they are defined
        if frame_duration:
            manager.frame_duration = frame_duration
        
        if playback_head:
            manager.playhead = playback_head

        # Play manager
        manager.play_loop()


def start():
    # Args parse setup
    parser = argparse.ArgumentParser(
        prog="PCtracker",
        description="Plays/Exports lists of frequencies through the PCspeaker"
    )

    parser.add_argument("path")
    parser.add_argument("-o", "--output")
    parser.add_argument("-s", "--split", action="store_true")
    parser.add_argument("-fd", "--frame-duration", type=int)
    parser.add_argument("-ph", "--playback-head", type=int)

    # Parsing args
    args = parser.parse_args()

    # File error handling
    # path.Path.exists(args.path)
    # TODO handle error

    # Output if requested
    if args.output:
        output(args.path, args.output, split=args.split, frame_duration=args.frame_duration, playback_head=args.playback_head)
    else:   # Otherwise play the sound
        play(args.path, split=args.split, frame_duration=args.frame_duration, playback_head=args.playback_head)
