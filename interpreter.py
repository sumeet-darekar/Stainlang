from lexer import Integer,Float

class Interpreter:
    def __init__(self,tree,base):
        self.tree = tree
        self.data = base

    def readINT(self,value):
        return int(value)
    
    def readFLOAT(self,value):
        return float(value)

    def readVAR(self,id):
        variable = self.data.read(id)
        variableType = variable.dataType

        return getattr(self, f"read{variableType}")(variable.value)

    def computeBin(self, left, operator, right):
        left_type = "VAR" if str(left.dataType).startswith("VAR") else str(left.dataType)
        right_type = "VAR" if str(right.dataType).startswith("VAR") else str(right.dataType)

        if operator.value == "=":
            left.dataType = f"VAR({right_type})"
            self.data.write(left,right)
            return self.data.readAll()

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

