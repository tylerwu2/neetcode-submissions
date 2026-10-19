class MinStack:
    
    def __init__(self):
        self.vals = []
        self.min_val = []

    def push(self, val: int) -> None:
        self.vals.append(val)
        if len(self.min_val) == 0:
            self.min_val.append(val)
        else:
            self.min_val.append(min(val, self.min_val[-1]))

    def pop(self) -> None:
        self.vals.pop()
        self.min_val.pop()

    def top(self) -> int:
        return self.vals[-1]

    def getMin(self) -> int:
        return self.min_val[-1]
