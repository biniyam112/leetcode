class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:        
        result = 0
        monostack = []
        for i in range(len(arr)):
            if not monostack or monostack[-1][0] < arr[i]:
                # (value,removed)
                monostack.append((arr[i],1))
            else:
                lasting = 1
                while monostack and arr[i] < monostack[-1][0]:
                    val,removed = monostack.pop()
                    result += lasting * val * removed
                    lasting += removed
                monostack.append((arr[i],lasting))
                
        # print(monostack)
        remSum = 0
        for i in range(len(monostack)-1,-1,-1):
            val,removed = monostack[i]
            result += val * (len(monostack)-i+remSum) * removed
            remSum += removed-1
            # print(remSum)
    
        result %= 10**9 + 7
        return result