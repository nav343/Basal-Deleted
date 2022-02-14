"""
The Lexer
"""

from typing import Iterator
from utils.peekable import Peekable
from utils.token import *
from utils.error import *


def lex(chars: Peekable[tuple[int, str]], filename: str) -> Iterator[Token]:
    """
    Lexes the contents of a file.
    """
    tokens = []
    line = 1
    last_line = 0
    last = 0
    while (char := next(chars, None)):
        (j, char) = char
        i = j - last_line + 1
        last = i + 1
        match char:
            case '\n':
                line += 1
                last_line = j + 1
            case ' ' | '\t' | '\r':
                pass
            case '\'':
                k = i
                match next(chars, None):
                    case(_, '\''):
                        raise CharParseError(
                            Position(line, i, k+2, filename), "Expected char literal, found '")
                    case(_, '\\'):
                        k += 1
                        match next(chars, None):
                            case(_, 'n'):
                                c = '\n'
                            case(_, 't'):
                                c = '\t'
                            case(_, '\\'):
                                c = '\\'
                            case(_, '\''):
                                c = '\''
                            case(_, '0'):
                                c = '\0'
                            case(_, 'r'):
                                c = '\r'
                            case None:
                                raise CharParseError(
                                    Position(line, i, i+3, filename), "Expected char literal after \\")
                            case(_, c):
                                raise CharParseError(
                                    Position(line, i, i+3, filename), f"Invalid escape sequence: \{c}")
                    case(_, a):
                        c = a
                match next(chars, None):
                    case None:
                        raise CharParseError(
                            Position(line, i, k+3, filename), f"Unclosed Char Literal")
                    case(_, '\''):
                        yield Char(Position(line, i, k+3, filename), c)
                    case(_, c):
                        raise CharParseError(
                            Position(line, i, k+3, filename), f"Expected ', found {c}")
            case '+':
                match chars.peek():
                    case(_, '='):
                        next(chars)
                        yield PlusAssign(Position(line, i, i + 3, filename))
                    case(_, '+'):
                        next(chars)
                        yield Increment(Position(line, i, i + 3, filename))
                    case _:
                        yield Plus(Position(line, i, i + 2, filename))
            case '&':
                match chars.peek():
                    case(_, '='):
                        next(chars)
                        yield AndAssign(Position(line, i, i + 3, filename))
                    case _:
                        yield And(Position(line, i, i + 2, filename))
            case '|':
                match chars.peek():
                    case(_, '='):
                        next(chars)
                        yield OrAssign(Position(line, i, i + 3, filename))
                    case _:
                        yield Or(Position(line, i, i + 2, filename))
            case '^':
                match chars.peek():
                    case(_, '='):
                        next(chars)
                        yield XorAssign(Position(line, i, i + 3, filename))
                    case _:
                        yield Xor(Position(line, i, i + 2, filename))
            case '/':
                match chars.peek():
                    case(_, '='):
                        next(chars)
                        yield DivideAssign(
                            Position(line, i, i + 3, filename))
                    case(_, '/'):
                        for i, c in chars:
                            if c == '\n':
                                line += 1
                                last_line = i + 1
                                break
                    case(_, '*'):
                        next(chars)
                        while (char := next(chars, None)):
                            (i, c) = char
                            if c == '*' and (c := next(chars, None)):
                                if c[1] == '/':
                                    break
                            elif c == '\n':
                                line += 1
                                last_line = i + 1
                        else:
                            raise UnterminatedCommentError(
                                Position(line, i, i + 1, filename))
                    case _:
                        yield Divide(Position(line, i, i + 2, filename))
            case '*':
                match chars.peek():
                    case(_, '='):
                        next(chars)
                        yield MultiplyAssign(
                            Position(line, i, i + 3, filename))
                    case(_, '*'):
                        next(chars)
                        match chars.peek():
                            case(_, '='):
                                next(chars)
                                yield PowerAssign(
                                    Position(line, i, i + 4, filename))
                            case _:
                                yield Power(Position(line, i, i + 3, filename))
                    case _:
                        yield Multiply(Position(line, i, i + 2, filename))
            case '%':
                match chars.peek():
                    case(_, '='):
                        next(chars)
                        yield ModAssign(Position(line, i, i + 3, filename))
                    case _:
                        yield Mod(Position(line, i, i + 2, filename))
            case '<':
                match chars.peek():
                    case(_, '='):
                        next(chars)
                        yield SmallerThanEqual(
                            Position(line, i, i + 3, filename))
                    case(_, '<'):
                        next(chars)
                        yield ShiftLeft(
                            Position(line, i, i + 3, filename))
                    case _:
                        yield SmallerThan(
                            Position(line, i, i + 2, filename))
            case '>':
                match chars.peek():
                    case(_, '='):
                        next(chars)
                        yield GreaterThanEqual(
                            Position(line, i, i + 3, filename))
                    case(_, '>'):
                        next(chars)
                        yield ShiftRight(
                            Position(line, i, i + 3, filename))
                    case _:
                        yield GreaterThan(
                            Position(line, i, i + 2, filename))
            case '-':
                match chars.peek():
                    case(_, '='):
                        next(chars)
                        yield MinusAssign(
                            Position(line, i, i + 3, filename))
                    case(_, '>'):
                        next(chars)
                        yield Arrow(Position(line, i, i + 3, filename))
                    case(_, '-'):
                        next(chars)
                        yield Decrement(Position(line, i, i + 3, filename))
                    case _:
                        yield Minus(Position(line, i, i + 2, filename))
            case '=':
                match chars.peek():
                    case(_, '='):
                        next(chars)
                        yield Equals(Position(line, i, i + 3, filename))
                    case(_, '>'):
                        next(chars)
                        yield FatArrow(Position(line, i, i + 3, filename))
                    case _:
                        yield Assign(Position(line, i, i + 2, filename))
            case '!':
                match chars.peek():
                    case(_, '='):
                        next(chars)
                        yield NotEqual(Position(line, i, i + 3, filename))
                    case _:
                        yield Not(Position(line, i, i + 2, filename))
            case ';':
                yield SemiColon(Position(line, i, i + 2, filename))
            case ',':
                yield Comma(Position(line, i, i + 2, filename))
            case ':':
                yield Colon(Position(line, i, i + 2, filename))
            case '[':
                yield LSquare(Position(line, i, i + 2, filename))
            case ']':
                yield RSquare(Position(line, i, i + 2, filename))
            case '(':
                yield LParen(Position(line, i, i + 2, filename))
            case ')':
                yield RParen(Position(line, i, i + 2, filename))
            case '{':
                yield LCurly(Position(line, i, i + 2, filename))
            case '}':
                yield RCurly(Position(line, i, i + 2, filename))
            case '?':
                yield Question(Position(line, i, i + 2, filename))
            case '.':
                yield Dot(Position(line, i, i + 2, filename))
            case '"':
                word = ""
                start = i
                end = j + 2
                escape = False
                for i, c in chars:
                    if escape:
                        match c:
                            case 'n':
                                word += '\n'
                            case 't':
                                word += '\t'
                            case 'r':
                                word += '\r'
                            case '"':
                                word += '"'
                            case '\\':
                                word += '\\'
                            case c:
                                raise StringParseError(
                                    Position(line, i, i + 3, filename), "Invalid escape sequence: \{c}")
                        escape = False
                    elif c == '"':
                        end = i + 2
                        break
                    elif c == '\n':
                        line += 1
                        last_line = i + 1
                        word += c
                    elif c == '\\':
                        escape = True
                    else:
                        word += c
                else:
                    raise StringParseError(
                        Position(line, i, i + 1, filename), "Unclosed String Literal")
                end -= last_line
                yield String(Position(line, start, end, filename), word)
            case number if number.isnumeric():
                start = i
                end = j + 2
                dot = False
                while (char := chars.peek()):
                    if char[1] == '.':
                        if dot:
                            raise NumberParseError(
                                Position(line, i, i + 2, filename), char[1])
                        dot = True
                    elif not char[1].isnumeric():
                        if char[1].isalpha():
                            raise NumberParseError(
                                Position(line, i, i + 2, filename), char[1])
                        break
                    end = char[0] + 2
                    number += char[1]
                    next(chars)
                end -= last_line
                if dot:
                    yield Float(Position(line, start, end, filename), float(number))
                else:
                    yield Number(Position(line, start, end, filename), int(number))
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
                    yield Keyword(Position(line, start, end, filename), word)
                else:
                    yield Identifier(
                        Position(line, start, end, filename), word)
            case c:
                raise IllegalCharError(Position(line, i, i + 2, filename), c)

    if last >= last_line:
        last -= last_line

    yield EOF(Position(line, last, last, filename))
