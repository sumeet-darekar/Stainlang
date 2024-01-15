import sys
from lexer import Lexer
from parser import Parser
from interpreter import Interpreter

class Data:
  def __init__(self):
    self.variables = {} 

  def read(self,id):
    return self.variables[id]

  def readAll(self):
    #return self.variables
    self.variables
  
  def write(self, variable, expression):
    variableName = variable.value
    self.variables[variableName] = expression

base = Data()


while True:
    try:
      text = input("stainLang>> ")
      tokenizer = Lexer(text)
      tokens = tokenizer.tokenization()
  
      if(tokens[0]=="clear" or tokens[0] == "exit"):
        text=""
        continue;
  
  
      #print(tokens)
      parser = Parser(tokens)
      tree = parser.parse()
      #print(tree)
      interpreter = Interpreter(tree,base)
      output = interpreter.interpret()
      if output != None:
        #print("printing none")
        print(output)
    except KeyboardInterrupt as e:
      print(e)
      print("\nkeyboard interrupt")
      print("Bye!!")
      sys.exit()