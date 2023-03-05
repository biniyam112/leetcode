class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 1:
            return x
        if n == 0:
            return 1
        
        power = self.myPow(x,abs(n)//2)
        if n < 0:
            return 1/(power*power * self.myPow(x,n%2))
        if n % 2:
            return power * power * x
        else:
            return power * power
        
        