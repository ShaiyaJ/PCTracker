def parse(path: str) -> (int, list[list[int]]):
    frame_duration = 0      # Return values, int (frame_duration) -- list[int] (notes)
    notes = []

    # Reading file 
    with open(path, "r") as file:
        raw = file.read()

    # TODO: format error handling (filter empty lines, filter any string)
    
    # Splitting by newline 
    lines = raw.split("\n")
    frame_duration = int(lines.pop(0))  # Frame duration will always been the first item

    # Processing values
    for line in lines: 
        channels = line.split(" ")  # Channels are split by spaces

        # Converting to int
        for i in range(len(channels)):
            channels[i] = int(channels[i])

        notes.append(channels)      # Rightmost notes take priority   # TODO: int cast error handling

    # Returning
    return (frame_duration, notes)


def create(path: str, frame_duration: int, notes: list[list[int]]):
    # Building file
    raw = ""
    raw += str(frame_duration) + "\n"
    raw += " ".join( "\n".join(notes) )

    # Opening file (will create a new file if one doesn't already exist)
    with open(path, "w") as file:
        file.write(raw)
