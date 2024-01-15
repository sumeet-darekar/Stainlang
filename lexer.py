import os
import sys
class Lexer:

    stopper = [" "]
    operator = "!+-*/()="
    letters = "abcdefghijklmnopqrstuvwxyz"
    keywords = ["set","clear","exit"]
    booleanOperator = ["and","or","not"] 
    comparisonOperator = ["<",">","<=",">=","?="]
    comparisonWords = "><?="

    def __init__(self,line):
        self.line=line
        self.counter=0
        self.currChar=self.line[self.counter]
        self.tokens=[]

    def tokenization(self):
        while self.counter < len(self.line):
            if self.currChar.isdigit() :
                self.wholeDigit=self.extract()
                self.tokens.append(self.wholeDigit)

            elif self.currChar in Lexer.operator:
                self.operant=Operator(self.currChar)
                self.tokens.append(self.operant)
                self.move()

            elif self.currChar in Lexer.letters:
                wholeString = self.extract_string()

                if wholeString in Lexer.keywords:
                    if wholeString == "clear":
                        print("Clearning")
                        os.system('cls')
                        return ["clear"]
                    if wholeString == "exit":
                        print("exiting the program")
                        sys.exit()
                        return ["exit"]
                    token = Declaration(wholeString)
                elif wholeString == "and" or wholeString == "or" or wholeString == "not":
                    token = BooleanOperator(wholeString)
                else:
                    token = Variable(wholeString)

                self.tokens.append(token)
            elif self.currChar in Lexer.comparisonWords:
                operator = ""
                while self.currChar in Lexer.comparisonWords and self.counter < len(self.line):
                    operator += self.currChar
                    self.move()
                token = ComparisonOperator(operator)
                self.tokens.append(token)

            elif self.currChar in Lexer.stopper:
                self.move()

            else:
                self.move()

        return self.tokens

    def extract(self):
        isFloat=False
        wholeDigit=""
        while self.currChar.isdigit() or self.currChar==".":
            if self.counter < len(self.line) or self.currChar=="." and self.currChar not in Lexer.stopper:
                if self.currChar==".":
                    isFloat=True
                wholeDigit += self.currChar
                self.move()
            elif self.currChar in Lexer.stopper:
                self.move() 
            else:
                break
        return Integer(wholeDigit) if not isFloat else Float(wholeDigit)
   
    def extract_string(self):
        word=""
        while self.currChar in Lexer.letters and self.counter < len(self.line):
            word += self.currChar

            self.move()
        return word

    def move(self):
        self.counter+=1
        if self.counter < len(self.line):
            self.currChar=self.line[self.counter]


class Token:
    def __init__(self,dataType,value):
        self.dataType=dataType
        self.value=value

    
    def __repr__(self):
        return str(self.value)

class Integer(Token):
    def __init__(self,value):
        super().__init__("INT",value)

class Float(Token):
    def __init__(self,value):
        super().__init__("FLOAT",value)

class Operator(Token):
    def __init__(self,value):
        super().__init__("OP",value)

class Declaration(Token):
    def __init__(self,value):
        super().__init__("DEL",value)

class Variable(Token):
    def __init__(self,value):
        super().__init__("VAR(?)",value)

class BooleanOperator(Token):
    def __init__(self,value):
        super().__init__("BOOL",value)

class ComparisonOperator(Token):
    def __init__(self,value):
        super().__init__("COMP",value)
