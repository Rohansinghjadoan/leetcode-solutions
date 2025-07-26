class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, val):
        if not self.stack:
            self.stack.append(val)
            self.min = val
        elif val >= self.min:
            self.stack.append(val)
        else:
            # Store encoded value
            self.stack.append(2 * val - self.min)
            self.min = val

    def pop(self):
        if not self.stack:
            return
        top = self.stack.pop()
        if top < self.min:
            # Recover previous min
            self.min = 2 * self.min - top

    def top(self):
        if not self.stack:
            return None
        top = self.stack[-1]
        if top < self.min:
            # Encoded value, so return min
            return self.min
        return top

    def getMin(self):
        return self.min
