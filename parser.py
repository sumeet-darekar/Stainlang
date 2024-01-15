
from lexer import Operator


class Parser:
    def __init__(self,tokens):
        self.tokens=tokens
        self.counter=0
        self.token=self.tokens[self.counter]

    def factor(self):
        if self.token.dataType == "INT" or self.token.dataType == "FLOAT":
            return self.token
        elif self.token.value == "(":
            self.move()
            expression = self.boolean_expr()
            return expression
        elif self.token.dataType.startswith("VAR"):
            return self.token
        elif self.token.value == "not":
            operator = self.token
            self.move()
            return [operator, self.boolean_expr()]
        elif self.token.value == "+" or self.token.value == "-" or self.token.value=="!":
            operator = self.token
            self.move()
            operand = self.boolean_expr()
            return [operator,operand]

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

    def comparison_expr(self):
        leftNode = self.expression()
        
        while self.token.dataType == "COMP":
            operator = self.token
            self.move()
            rightNode = self.expression()
        
            leftNode = [leftNode, operator, rightNode]
        return leftNode

    def boolean_expr(self):
        leftNode = self.comparison_expr()

        while self.token.value == "and" or self.token.value == "or":
            operator = self.token
            self.move()
            rightNode = self.comparison_expr()
        
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

    def variable(self):
        if self.token.dataType.startswith("VAR"):
            return self.token

    def statement(self):
        if self.token.dataType == "DEL":
            self.move()
            leftNode = self.variable()
            self.move()
            if self.token.value == "=":
                operation = self.token
                self.move()
                rightNode = self.boolean_expr()

                return [leftNode, operation, rightNode]

        elif self.token.dataType == "INT" or self.token.dataType == "FLOAT" or self.token.dataType == "OP" or self.token.dataType == "not":
            return self.boolean_expr()

    def parse(self):
        return self.statement()

    def move(self):
        self.counter += 1
        if self.counter < len(self.tokens):
            self.token=self.tokens[self.counter]
