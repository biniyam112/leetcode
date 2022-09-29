class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        index = bisect_left(arr,x)
        i,j = index,index
        # print(index,x)
        ans = []
        if index < len(arr) and arr[index]-x == 0:
            ans.append(arr[index])
            i -= 1
            j += 1
            k -= 1
        else:
            i -= 1
        while i>=0 and j<len(arr) and k>0:
            if abs(x-arr[i]) > abs(x-arr[j]):
                ans.append(arr[j])
                j+=1
                k -= 1
            else:
                ans.append(arr[i])
                i-=1
                k -= 1
        while k > 0 and j < len(arr):
            ans.append(arr[j])
            j += 1
            k-=1
        while k > 0 and i >= 0:
            ans.append(arr[i])
            i -= 1
            k-=1
            
        ans.sort()
        return ans