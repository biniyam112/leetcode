class StockSpanner:

    def __init__(self):
        self.stack = [(float('inf'),0)]
        

    def next(self, price: int) -> int:
        if price < self.stack[-1][0]:
            self.stack.append((price,len(self.stack)))
            return 1
        for i in range(self.stack[-1][1],-1,-1):
            if self.stack[i][0] > price:
                break
        self.stack.append((price,i))
        return len(self.stack)-i-1
        
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)