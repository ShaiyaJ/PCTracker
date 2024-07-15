class Tracker:
    lines: list[list[int]]

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self) -> int:
        # Checking whether to perform the operation
        if self.__index == len(self.lines)-1:
            raise StopIteration

        # Error checking for lines (in case self.__index somehow mutates above len(lines)-1
        if len(self.lines) <= self.__index:
            raise IndexError

        # Returning beep
        beep: int 
        
        try:                # Handling case of empty line
            beep = self.lines[self.__index][-1]
        except IndexError:
            beep = 0

        self.__index += 1   # Incrementing index
        return beep         # Returning final value