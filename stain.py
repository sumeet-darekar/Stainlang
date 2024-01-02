from lexer import Lexer
from parser import Parser

while True:
    text=input("stainLang>> ")
    tokenizer=Lexer(text)
    tokens=tokenizer.tokenization()
    print(tokens)
    parser = Parser(tokens)
    tree = parser.parse()
    print(tree)
