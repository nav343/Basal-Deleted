import lexer

tokens = lexer.lex(contents='var a = 2;', filename="hi")
print(tokens)
