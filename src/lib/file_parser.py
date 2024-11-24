def parse(path: str) -> (int, list[int]):
    frame_duration = 0      # Return values, int (frame_duration) -- list[int] (notes)
    notes = []

    # Reading file 
    with open(path, "r") as file:
        raw = file.read()
    
    # Splitting by newline 
    lines = raw.split("\n")
    frame_duration = lines.pop(0)   # Frame duration will always been the first item
                                    # TODO: format error handling

    # Processing values
    for line in lines: 
                                    # TODO: format error handling
        channels = line.split(" ")  # Channels are split by spaces
        notes.append(int(channels[-1])) # Rightmost notes take priority   # TODO: int cast error handling

    # Returning
    return (frame_duration, notes)


def create(path: str, frame_duration: int, notes: list[int]):
    # Building file
    raw = ""
    raw += str(frame_duration) + "\n"
    raw += "\n".join(notes)

    # Opening file (will create a new file if one doesn't already exist)
    with open(path, "w") as file:
        file.write(raw)
