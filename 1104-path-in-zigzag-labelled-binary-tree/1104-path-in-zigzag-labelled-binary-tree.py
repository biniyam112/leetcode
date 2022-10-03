class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        level = 1
        if label == 1:
            return [1]
        temp = label
        while label > 1:
            label //= 2
            level += 1
            
        level -= 1
        label = temp
        ans = []
        ans.append(label)
        while level > 0:
            val = label//2
            val = 2**(level-1) + (2**level-1)-val
            ans.append(val)
            label = val
            level -= 1
        return ans[::-1]
        
        