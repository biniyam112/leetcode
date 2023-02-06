class DetectSquares:

    def __init__(self):
        self.mapping = defaultdict(dict)
   
    def add(self, point: List[int]) -> None:
        x, y = point[0], point[1]
   
        if y in self.mapping[x]:
            self.mapping[x][y] += 1
        else:
            self.mapping[x][y] = 0
            self.mapping[x][y] += 1

    def count(self, point: List[int]) -> int:
        x, y = point[0], point[1]
        res = 0 
        if x in self.mapping:
            for q in self.mapping[x]:
                d = abs(y-q)
                if d > 0:
                    if x-d in self.mapping and y in self.mapping[x-d] and q in self.mapping[x-d]:
                        res += self.mapping[x-d][y] * self.mapping[x-d][q] * self.mapping[x][q] 
                    if x+d in self.mapping and y in self.mapping[x+d] and q in self.mapping[x+d]:
                        res += self.mapping[x+d][y] * self.mapping[x+d][q] * self.mapping[x][q] 
        return res 