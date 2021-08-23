class Stack:
    
    def __init__(self):
        self.body = []

    def push(self, x: int) -> None:
        self.body.append(x)
        

    def pop(self) -> int:
        return self.body.pop(-1)
        

    def top(self) -> int:
        return self.body[-1]

    def empty(self) -> bool:
        return self.body == []

def calculate(expression):
    myStack = Stack()
    for j in range(len(expression)-1, -1, -1):
        i = expression[j]
        if(i.isdigit()):
            myStack.push(i)
        else:
            op1 = myStack.pop()
            op2 = myStack.pop()
            res = 0
            if(i == '+'):
                res = int(op1) + int(op2)
            elif(i == '-'):
                res = int(op2) - int(op1)
            elif(i == '*'):
                res = int(op1) * int(op2)
            elif(i == '/'):
                res = int(op2) / int(op1)
            myStack.push(str(res))

    return myStack.pop()

test_expression = "+9*26"
print(calculate(test_expression))