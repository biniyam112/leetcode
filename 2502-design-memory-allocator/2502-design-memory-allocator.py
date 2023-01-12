class Allocator:

    def __init__(self, n: int):
        self.memory = [0] * n
        self.indexing = defaultdict(list)
        

    def allocate(self, size: int, mID: int) -> int:
        i,j = 0,0
        while i < len(self.memory):
            if self.memory[i] == 0:
                j = i
                while j < len(self.memory) and self.memory[j] == 0 and j-i+1 < size:
                    j += 1
                if j < len(self.memory) and self.memory[j] == 0:
                    self.indexing[mID].append((i,size))
                    for k in range(i,j+1):
                        self.memory[k] = 1
                    return i
                i = j+1
            else:
                i += 1
        return -1
            

    def free(self, mID: int) -> int:
        newSpace = 0
        for start,size in self.indexing[mID]:
            newSpace += size
            for i in range(start,start+size):
                self.memory[i] = 0
        self.indexing[mID] = []
        return newSpace
        


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)