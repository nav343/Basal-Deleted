"""
The Lexer
"""

from error import IllegalCharError, Position
from peekable import Peekable
from token import Identifier


def lex(contents: str) -> list:
    """
    Lexes the contents of a file.
    """
    parentheses = []
    tokens = []
    line = 1
    last_line = 0
    last = 0
    chars = Peekable(enumerate(contents))
    while (char := next(chars, None)):
        i = char[0] - last_line + 1
        last = i + 1
        match char[1]:
            case '\n':
                line += 1
                last_line = char[0] + 1
            case ' ' | '\t' | '\r':
                pass
            case c if c.isalnum():
                word = c
                start = i
                end = char[0] + 2
                while (char := chars.peek()):
                    if not char[1].isalnum():
                        break
                    end = char[0] + 2
                    word += char[1]
                    chars.__next__()
                end -= last_line
                tokens.append(Identifier(Position(line, start, end), word))
            case _:
                raise IllegalCharError

    return tokens