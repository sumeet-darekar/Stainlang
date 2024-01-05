from lexer import Lexer
from parser import Parser
from interpreter import Interpreter


while True:
    text = input("stainLang>> ")
    tokenizer = Lexer(text)
    tokens = tokenizer.tokenization()
    print(tokens)
    parser = Parser(tokens)
    tree = parser.parse()
    print(tree) 
  #  interpreter = Interpreter(tree)
  #  output = interpreter.interpret()
#
  #  print(output)
