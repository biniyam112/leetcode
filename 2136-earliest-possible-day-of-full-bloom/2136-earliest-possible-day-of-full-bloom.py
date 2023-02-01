class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        zipped = sorted(zip(growTime,plantTime),key= lambda pair : -pair[0])
        n = len(zipped)
        ans = 0
        borrowedTime = 0
        for i in range(n):
            gt,pt = zipped[i]
            # ans += pt+max(0,gt-borrowedTime)
            ans = max(ans,gt+pt+borrowedTime)
            borrowedTime += pt
        return ans
        