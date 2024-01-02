class Lexer:

    stopper = [" "]
    operator = "+-*/"
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