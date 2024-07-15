from parse_tracker import parse, read_raw
from play_tracker import play
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a file")
        exit(1)
        
    file = sys.argv[1]

    obj = parse( read_raw(file) )
    play(obj)