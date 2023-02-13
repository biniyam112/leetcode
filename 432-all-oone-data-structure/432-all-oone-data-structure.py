class AllOne:

    def __init__(self):
        self.strToCount= defaultdict(int)
        self.countToStr = defaultdict(set)
        self.counter = 0
        self.maxCount = float('-inf')
        self.minCount = float('inf')

    def inc(self, key: str) -> None:
        self.counter += 1
        oldCount = self.strToCount[key]
        if oldCount:
            self.countToStr[oldCount].remove(key)
        self.strToCount[key] += 1
        self.countToStr[oldCount+1].add(key)
        if oldCount+1 > self.maxCount:
            self.maxCount = oldCount+1
        if self.minCount == oldCount and not self.countToStr[oldCount]:
            self.minCount += 1
        if oldCount+1 < self.minCount:
            self.minCount = oldCount+1
            
        

    def dec(self, key: str) -> None:
        self.counter -= 1
        oldCount = self.strToCount[key]
        self.countToStr[oldCount].remove(key)
        self.strToCount[key] -= 1
        if not self.strToCount[key]:
            self.strToCount.pop(key)
            for i in range(1,self.maxCount+1):
                if self.countToStr[i]:
                    self.minCount = i
                    break
        else:
            self.countToStr[oldCount-1].add(key)
            if oldCount-1 < self.minCount:
                self.minCount = oldCount-1
        if self.maxCount == oldCount and not self.countToStr[oldCount]:
            self.maxCount -= 1
            
        

    def getMaxKey(self) -> str:
        if not self.counter:
            return ''
        # print(self.countToStr[self.minCount])
        return next(iter(self.countToStr[self.maxCount]))
            
        

    def getMinKey(self) -> str:
        if not self.counter:
            return ''
        # print(self.countToStr[self.minCount])
        return next(iter(self.countToStr[self.minCount]))
        
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()