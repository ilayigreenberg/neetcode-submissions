class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min or val < self.min[-1][0]:
            self.min.append((val, len(self.stack)))

    def pop(self) -> None:
        if self.min[-1][1] == len(self.stack):
            self.min.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1][0]