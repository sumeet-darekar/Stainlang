from lexer import Lexer
from parser import Parser
from interpreter import Interpreter

class Data:
  def __init__(self):
    self.variables = {} 

  def read(self,id):
    return self.variables[id]

  def readAll(self):
    return self.variables
  
  def write(self, variable, expression):
    variableName = variable.value
    self.variables[variableName] = expression

base = Data()

while True:
    text = input("stainLang>> ")
    tokenizer = Lexer(text)
    tokens = tokenizer.tokenization()

    #print(tokens)
    parser = Parser(tokens)
    tree = parser.parse()
    #print(tree)
    interpreter = Interpreter(tree,base)
    output = interpreter.interpret()
    print(output)
