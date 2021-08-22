class MyStack:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.body = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.body.append(x)
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.body.pop(-1)
        

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.body[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.body == []

