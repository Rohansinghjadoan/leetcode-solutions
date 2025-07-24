class MyStack(object):

    def __init__(self):
        self.q=deque()

    def push(self, x):
        self.q.append(x)
        for _ in range (len(self.q)-1):
            self.q.append(self.q.popleft())
        

    def pop(self):
        if self.q:
            return self.q.popleft()
        return None

    def top(self):
        if self.q:
            return self.q[0]
        return None
        

    def empty(self):
        if self.q:
            return False
        return True

        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()