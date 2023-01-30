class Solution:
    def tribonacci(self, n: int) -> int:
        series = [0,1,1]
        if n < 3: return series[n]
        
        n -= 2
        while n > 0:
            series.append(sum(series[-3:]))
            n -= 1
        return series[-1]
        