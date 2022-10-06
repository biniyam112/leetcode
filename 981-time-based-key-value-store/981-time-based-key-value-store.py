class TimeMap:

    def __init__(self):
        self.vals = defaultdict(list)
        self.timestamps = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.vals[key].append(value)
        self.timestamps[key].append(timestamp)
        

    def get(self, key: str, timestamp: int) -> str:
        index = bisect_left(self.timestamps[key],timestamp)
        i = 0
        j = len(self.vals[key])-1
        best = -1
        while i <= j:
            mid = i + (j-i)//2
            if self.timestamps[key][mid] == timestamp:
                return self.vals[key][mid]
            elif self.timestamps[key][mid] < timestamp:
                best = mid
                i = mid+1
            else:
                j = mid-1
        if best == -1:
            return ''
        return self.vals[key][best]
                
        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)