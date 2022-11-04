class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(substring):
            i,j = 0,len(substring)-1
            while i < j:
                if substring[i] != substring[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        def partition(part = [],substring = '',index = 0):
            nonlocal ans
            if index == len(s):
                if substring != ''and isPalindrome(substring):
                    part.append(substring)
                    ans.append(part)
                return
            if not substring:
                substring += s[index]
                part_ = part.copy()
                part_.append(substring)
                partition(part_,'',index+1)
                partition(part,substring,index+1)
            else:
                substring += s[index]
                part_ = part.copy()
                if isPalindrome(substring):
                    part_.append(substring)
                    partition(part_,'',index+1)
                partition(part,substring,index+1)
                
        ans = []
        partition()
        return ans
            