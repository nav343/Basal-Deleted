class Error(Exception):
    pass

class IllegalCharError(Error):
    pass

class Position:
    def __init__(self, line, start, end):
        self.line = line
        self.start = start
        self.end = end