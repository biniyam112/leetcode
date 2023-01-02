class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:

        # find prime numbers
        isPrime = [True] * (right+1)
        isPrime[0] = isPrime[1] = False
        for i in range(2,int(math.sqrt(right))+1):
                if isPrime[i]:
                    for j in range(i*i, right+1 ,i):
                        isPrime[j] = False
                
                
        # get closest primes from list of primes
        isPrime = isPrime[left:]
        i = 0
        while i < len(isPrime) and not isPrime[i]:
            i += 1
        j = i+1
        while j < len(isPrime) and not isPrime[j]:
            j += 1
        if left == right or j == len(isPrime):
            return [-1,-1]
        ans = (i+left,j+left)
        minDis = j-i
        i = j
        j += 1
        while j < len(isPrime):
            if isPrime[j]:
                if j-i < minDis:
                    minDis = j-i
                    ans = (i+left,j+left)
                i = j
            j += 1
        return ans
            
