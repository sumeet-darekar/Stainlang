from lexer import Integer,Float

class Interpreter:
    def __init__(self,tree):
        self.tree=tree

    def readINT(self,value):
        return int(value)
    
    def readFLOAT(self,value):
        return float(value)

    def computeBin(self, left, operator, right):
        left_type = left.dataType
        right_type = right.dataType

        left = getattr(self, f"read{left_type}")(left.value)
        right = getattr(self, f"read{right_type}")(right.value)

        if operator.value == "+":
            output = left + right
        elif operator.value == "-":
            output = left - right
        elif operator.value == "*":
            output = left * right
        elif operator.value == "/":
            output = left / right
        
        return Integer(output) if (left_type == "INT" and right_type == "INT") else Float(output) 

    def interpret(self,tree=None):

        if tree is None:
            tree = self.tree

        leftNode = tree[0]
        if isinstance(leftNode, list):
            leftNode = self.interpret(leftNode)
        
        rightNode = tree[2] 
        if isinstance(rightNode, list):
            rightNode = self.interpret(rightNode)

        operator = tree[1]

        return self.computeBin(leftNode, operator, rightNode)

