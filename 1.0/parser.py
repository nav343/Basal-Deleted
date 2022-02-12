import lexer

tokens = lexer.lex(contents='var a = 2 ; \n7 > 3  2 + 6 - 1', filename="hi")
print(tokens)
