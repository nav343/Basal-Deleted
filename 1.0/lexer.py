"""
The Lexer
"""

from error import IllegalCharError, Position, NumberLexError
from peekable import Peekable
from token import *


def lex(contents: str, filename: str) -> list[Token]:
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
        (j, char) = char
        i = j - last_line + 1
        last = i + 1
        match char:
            case '\n':
                line += 1
                last_line = char[0] + 1
            case ' ' | '\t' | '\r':
                pass
            case '+':
                match chars.peek():
                    case (_, '='):
                        next(chars)
                        tokens.append(PlusAssign(Position(line, i, i + 3, filename)))
                    case _:
                        tokens.append(Plus(Position(line, i, i + 2, filename)))
            case '<':
                match chars.peek():
                    case (_, '='):
                        next(chars)
                        tokens.append(SmallerThanEqual(Position(line, i, i + 3, filename)))
                    case _:
                        tokens.append(SmallerThan(Position(line, i, i + 2, filename)))
            case '>':
                match chars.peek():
                    case (_, '='):
                        next(chars)
                        tokens.append(GreaterThanEqual(Position(line, i, i + 3, filename)))
                    case _:
                        tokens.append(GreaterThan(Position(line, i, i + 2, filename)))
            case '-':
                match chars.peek():
                    case (_, '='):
                        next(chars)
                        tokens.append(MinusAssign(Position(line, i, i + 3, filename)))
                    case _:
                        tokens.append(Minus(Position(line, i, i + 2, filename)))
            case '=':
                match chars.peek():
                    case (_, '='):
                        next(chars)
                        tokens.append(Equals(Position(line, i, i + 3, filename)))
                    case _:
                        tokens.append(Assign(Position(line, i, i + 2, filename)))
            case ';':
                tokens.append(SemiColon(Position(line, i, i + 2, filename)))
            case number if number.isnumeric():
                start = i
                end = j + 2
                while (char := chars.peek()):
                    if not char[1].isnumeric():
                        if not char[1].isspace():
                            raise NumberLexError(Position(line, i, i + 2, filename), char[1])
                        break
                    end = char[0] + 2
                    number += char[1]
                    next(chars)
                end -= last_line
                tokens.append(Number(Position(line, start, end, filename), int(number)))
            case word if word.isalpha() or word == '_':
                start = i
                end = j + 2
                while (char := chars.peek()):
                    if not (char[1].isalnum() or char[1] == '_'):
                        break
                    end = char[0] + 2
                    word += char[1]
                    next(chars)
                end -= last_line
                if word in KEYWORDS:
                    tokens.append(Keyword(Position(line, start, end, filename), word))
                else:
                    tokens.append(Identifier(Position(line, start, end, filename), word))
            case c:
                raise IllegalCharError(Position(line, i, i + 2, filename), c)

    if last >= last_line:
        last -= last_line

    tokens.append(EOF(Position(line, last, last, filename)))
    return tokens