class StockSpanner(object):

    def __init__(self):
        self.st = []
        self.index = -1

    def next(self, price):
        self.index += 1
        while self.st and self.st[-1][1] <= price:
            self.st.pop()
        if not self.st:
            ans = self.index + 1
        else:
            ans = self.index - self.st[-1][0]
        self.st.append((self.index, price))
        return ans
