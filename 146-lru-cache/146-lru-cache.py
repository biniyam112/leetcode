from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.mapping = OrderedDict()
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key in self.mapping:
            self.mapping.move_to_end(key)
            return self.mapping[key]
        return -1
        
        
    def put(self, key: int, value: int) -> None:
        if key not in self.mapping and len(self.mapping) == self.capacity:
                self.mapping.popitem(0)
        elif key in self.mapping:
            self.mapping.move_to_end(key)
                
        self.mapping[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)