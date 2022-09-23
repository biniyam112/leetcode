class MapSum:

    def __init__(self):
        self.map = {}
        

    def insert(self, key: str, val: int) -> None:
        self.map[key] = val
        

    def sum(self, prefix: str) -> int:
        sum_ = 0
        for k,v in self.map.items():
            if len(k) >= len(prefix) and k[:len(prefix)] == prefix:
                sum_ += v
        return sum_
            
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)