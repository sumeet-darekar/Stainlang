class Parser:
    def __init__(self,tokens):
        self.tokens=tokens
        self.counter=0
        self.token=self.tokens[self.counter]

    def factor(self):
        if self.token.dataType == "INT" or self.token.dataType == "FLOAT":
            return self.token

    def term(self):
        leftNode = self.factor()
        self.move()
        
        while self.token.value == "*" or self.token.value == "/":
            operator = self.token
            self.move()
            rightNode = self.factor()
            self.move()
            leftNode = [leftNode, operator, rightNode]
        return leftNode
    
    def expression(self):
        leftNode = self.term()
        
        while self.token.value == "+" or self.token.value == "-":
            operator = self.token
            self.move()
            rightNode = self.term()
        
            leftNode = [leftNode, operator, rightNode]
        return leftNode


    def parse(self):
        return self.expression()

    def move(self):
        self.counter += 1
        if self.counter < len(self.tokens):
            self.token=self.tokens[self.counter]