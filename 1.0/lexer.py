"""
The Lexer
"""

from peekable import Peekable
from error import *
from token import *


def lex(contents: str, filename: str) -> list[Token]:
    """
    Lexes the contents of a file.
    """
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
                last_line = j + 1
            case ' ' | '\t' | '\r':
                pass
            case '\'':
                k = i
                match next(chars, None):
                    case (_, '\''):
                        raise CharLexError(Position(line, i, k+2, filename), "Expected char literal, found '")
                    case (_, '\\'):
                        k += 1
                        match next(chars, None):
                            case (_, 'n'):
                                c = '\n'
                            case (_, 't'):
                                c = '\t'
                            case (_, '\\'):
                                c = '\\'
                            case (_, '\''):
                                c = '\''
                            case (_, '0'):
                                c = '\0'
                            case (_, 'r'):
                                c = '\r'
                            case None:
                                raise CharLexError(Position(line, i, i+3, filename), "Expected char literal after \\")
                            case (_, c):
                                raise CharLexError(Position(line, i, i+3, filename), f"Invalid escape sequence: \{c}")
                    case (_, a):
                        c = a
                match next(chars, None):
                    case None:
                        raise CharLexError(Position(line, i, k+3, filename), f"Unclosed Char Literal")
                    case (_, '\''):
                        tokens.append(Char(Position(line, i, k+3, filename), c))
                    case (_, c):
                        raise CharLexError(Position(line, i, k+3, filename), f"Expected ', found {c}")
            case '+':
                match chars.peek():
                    case (_, '='):
                        next(chars)
                        tokens.append(PlusAssign(Position(line, i, i + 3, filename)))
                    case (_, '+'):
                        next(chars)
                        tokens.append(Increment(Position(line, i, i + 3, filename)))
                    case _:
                        tokens.append(Plus(Position(line, i, i + 2, filename)))
            case '&':
                match chars.peek():
                    case (_, '='):
                        next(chars)
                        tokens.append(AndAssign(Position(line, i, i + 3, filename)))
                    case _:
                        tokens.append(And(Position(line, i, i + 2, filename)))
            case '|':
                match chars.peek():
                    case (_, '='):
                        next(chars)
                        tokens.append(OrAssign(Position(line, i, i + 3, filename)))
                    case _:
                        tokens.append(Or(Position(line, i, i + 2, filename)))
            case '^':
                match chars.peek():
                    case (_, '='):
                        next(chars)
                        tokens.append(XorAssign(Position(line, i, i + 3, filename)))
                    case _:
                        tokens.append(Xor(Position(line, i, i + 2, filename)))
            case '/':
                match chars.peek():
                    case (_, '='):
                        next(chars)
                        tokens.append(DivideAssign(Position(line, i, i + 3, filename)))
                    case (_, '/'):
                        for i, c in chars:
                            if c == '\n':
                                line += 1
                                last_line = i + 1
                                break
                    case (_, '*'):
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
                            raise UnterminatedCommentError(Position(line, i, i + 1, filename))
                    case _:
                        tokens.append(Divide(Position(line, i, i + 2, filename)))
            case '*':
                match chars.peek():
                    case (_, '='):
                        next(chars)
                        tokens.append(MultiplyAssign(Position(line, i, i + 3, filename)))
                    case (_, '*'):
                        next(chars)
                        match chars.peek():
                            case (_, '='):
                                next(chars)
                                tokens.append(PowerAssign(Position(line, i, i + 4, filename)))
                            case _:
                                tokens.append(Power(Position(line, i, i + 3, filename)))
                    case _:
                        tokens.append(Multiply(Position(line, i, i + 2, filename)))
            case '%':
                match chars.peek():
                    case (_, '='):
                        next(chars)
                        tokens.append(ModAssign(Position(line, i, i + 3, filename)))
                    case _:
                        tokens.append(Mod(Position(line, i, i + 2, filename)))
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
                    case (_, '>'):
                        next(chars)
                        tokens.append(Arrow(Position(line, i, i + 3, filename)))
                    case (_, '-'):
                        next(chars)
                        tokens.append(Decrement(Position(line, i, i + 3, filename)))
                    case _:
                        tokens.append(Minus(Position(line, i, i + 2, filename)))
            case '=':
                match chars.peek():
                    case (_, '='):
                        next(chars)
                        tokens.append(Equals(Position(line, i, i + 3, filename)))
                    case (_, '>'):
                        next(chars)
                        tokens.append(FatArrow(Position(line, i, i + 3, filename)))
                    case _:
                        tokens.append(Assign(Position(line, i, i + 2, filename)))
            case '!':
                match chars.peek():
                    case (_, '='):
                        next(chars)
                        tokens.append(NotEqual(Position(line, i, i + 3, filename)))
                    case _:
                        tokens.append(Not(Position(line, i, i + 2, filename)))
            case ';':
                tokens.append(SemiColon(Position(line, i, i + 2, filename)))
            case ',':
                tokens.append(Comma(Position(line, i, i + 2, filename)))
            case ':':
                tokens.append(Colon(Position(line, i, i + 2, filename)))
            case '[':
                tokens.append(LSquare(Position(line, i, i + 2, filename)))
            case ']':
                tokens.append(RSquare(Position(line, i, i + 2, filename)))
            case '(':
                tokens.append(LParen(Position(line, i, i + 2, filename)))
            case ')':
                tokens.append(RParen(Position(line, i, i + 2, filename)))
            case '{':
                tokens.append(LCurly(Position(line, i, i + 2, filename)))
            case '}':
                tokens.append(RCurly(Position(line, i, i + 2, filename)))
            case '?':
                tokens.append(Question(Position(line, i, i + 2, filename)))
            case '.':
                match chars.peek():
                    case (_, '.'):
                        next(chars)
                        match chars.peek():
                            case (_, '.'):
                                next(chars)
                                tokens.append(TripleDot(Position(line, i, i + 4, filename)))
                            case _:
                                tokens.append(DoubleDot(Position(line, i, i + 3, filename)))
                    case _:
                        tokens.append(Dot(Position(line, i, i + 2, filename)))
            case '$':
                tokens.append(Dollar(Position(line, i, i + 2, filename)))
            case '#':
                tokens.append(Hash(Position(line, i, i + 2, filename)))
            case '@':
                tokens.append(AtTheRate(Position(line, i, i + 2, filename)))
            case '`':
                tokens.append(BackTick(Position(line, i, i + 2, filename)))
            case '~':
                tokens.append(CurvedMinus(Position(line, i, i + 2, filename)))
            case '\\':
                match next(chars, None):
                    case (_, _):
                        pass
                    case None:
                        raise InvalidEscapeError(Position(line, i, i + 2, filename), "Expected a character to escape after \\")
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
                                raise StringLexError(Position(line, i, i + 3, filename), "Invalid escape sequence: \{c}")
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
                    raise StringLexError(Position(line, i, i + 1, filename), "Unclosed String Literal")
                end -= last_line
                tokens.append(String(Position(line, start, end, filename), word))
            case number if number.isnumeric():
                start = i
                end = j + 2
                dot = False
                while (char := chars.peek()):
                    if char[1] == '.':
                        if dot:
                            raise NumberLexError(Position(line, i, i + 2, filename), char[1])
                        dot = True
                    elif not char[1].isnumeric():
                        if char[1].isalpha():
                            raise NumberLexError(Position(line, i, i + 2, filename), char[1])
                        break
                    end = char[0] + 2
                    number += char[1]
                    next(chars)
                end -= last_line
                if dot:
                    tokens.append(Float(Position(line, start, end, filename), float(number)))
                else:
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