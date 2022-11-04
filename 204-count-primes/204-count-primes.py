class Solution:
    def countPrimes(self, n: int) -> int:
        if n<2:
            return 0
        prime=[1]*n
        prime[0]=prime[1]=0
        for i in range(2,int(sqrt(n))+1):
            if prime[i] == 1:
                for j in range(i*i,n,i):
                    prime[j] = 0
        return sum(prime)