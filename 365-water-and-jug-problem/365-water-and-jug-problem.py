class Solution:
    def canMeasureWater(self, jug1: int, jug2: int, tar: int) -> bool:
        if(jug1 + jug2 < tar):
            return 0
        return tar % math.gcd(jug1, jug2) == 0