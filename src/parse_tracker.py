from tracker import Tracker

def read_raw(path: str) -> str:
    raw: str

    with open(path, "r") as file:
        raw = file.read()
        file.close()

    return raw

def __is_valid_int[T](val: T) -> bool:
    try:
        int(val)
    except ValueError:
        return False
    
    return True


def parse(raw: str) -> Tracker:
    tracker = Tracker()

    # Splitting file
    lines = raw.split("\n")
    
    # Splitting and filtering each line into integer segments
    for line_index in range(len(lines)):
        lines[line_index] = lines[line_index].split(" ")                        # Splitting line into segments
        lines[line_index] = list( filter(__is_valid_int, lines[line_index]) )   # Filtering out non-integer segments

    # Filtering out empty lines
    lines = list( filter(lambda x: True if x != [] else False, lines) )

    # Converting all strings to integers
    for line in range(len(lines)):
        for segment in range(len(lines[line])):
            lines[line][segment] = int(lines[line][segment])

    # Returning parsed value
    tracker.lines = lines
    return tracker

if __name__ == "__main__":
    TEST = """
0 10 20
10 20 30 comment
comment
20 30 40
"""

    for line in parse(TEST).lines:
        print(line)
