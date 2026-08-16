class MinStack:

    def __init__(self):
        self.stack = []
        self.minimums = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minimums:
            self.minimums.append(val)
            return 
        if val <= self.minimums[-1]:
            self.minimums.append(val)
            
    def pop(self) -> None:
        removed = self.stack.pop()
        if self.minimums and removed == self.minimums[-1]:
            self.minimums.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.minimums:
            return self.minimums[-1]
        else:
            return 0
