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
        elif operator.value == ">":
            output = True if left > right else False
        elif operator.value == "<":
            output = True if left < right else False
        elif operator.value == ">=":
            output = True if left >= right else False
        elif operator.value == "<=":
            output = True if left <= right else False
        elif operator.value == "?=":
            output = True if left == right else False
        elif operator.value == "and":
            output = True if left and right else False
        elif operator.value == "or":
            output = True if left or right else False
        elif operator.value == "??=":
            output = True if left != right else False


        return Integer(output) if (left_type == "INT" and right_type == "INT") else Float(output) 

    def computeUnary(self,operator,operand):
        operand_type = "VAR" if str(operand.dataType).startswith("VAR") else str(operand.dataType)
        operand = getattr(self, f"read{operand_type}")(operand.value)
        if operator.value == "+":
            return +operand
        elif operator.value == "-":
            return -operand
        elif operator.value == "!":
            return operand
        elif operand.value == "not":
            return True if not operand else False

    def interpret(self,tree=None):

        if tree is None:
            tree = self.tree

        if isinstance(tree, list) and len(tree) == 2 :
            expression = tree[1]
            if isinstance(expression, list):
                expression = self.interpret(expression)
            return self.computeUnary(tree[0],expression)

        elif not isinstance(tree,list):
            return tree

        else:
            leftNode = tree[0] if tree and len(tree) > 0 else None
            if isinstance(leftNode, list):
                leftNode = self.interpret(leftNode)
            
            rightNode = tree[2] if tree and len(tree) > 1 else None
            if isinstance(rightNode, list):
                rightNode = self.interpret(rightNode)
    
            operator = tree[1] if tree and len(tree) > 2 else None

            return self.computeBin(leftNode, operator, rightNode)

