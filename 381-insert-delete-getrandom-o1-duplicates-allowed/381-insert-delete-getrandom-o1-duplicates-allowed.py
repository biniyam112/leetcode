class RandomizedCollection:

    def __init__(self):
        self.items = []
        self.val_address = defaultdict(list)
        

    def insert(self, val: int) -> bool:
        self.val_address[val].append(len(self.items))
        self.items.append(val)
        if len(self.val_address[val]) == 1:
            return True
            
        

    def remove(self, val: int) -> bool:
        if len(self.val_address[val]) > 0:
            val_index = self.val_address[val].pop()
            self.items[val_index] = float('-inf')
            return True
        

    def getRandom(self) -> int:
        while True:
            val = self.items[random.randint(0,len(self.items)-1)]
            if val != float('-inf'):
                return val
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()