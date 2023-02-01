class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        minwhite = 0
        i,j = 0,0
        for j in range(k):
            if blocks[j] == 'W':
                minwhite += 1
        ans = minwhite
        j += 1
        while j < len(blocks):
            if blocks[j] != blocks[i]:
                if blocks[j] == 'B' and blocks[i] == 'W':
                    minwhite -= 1
                    ans = min(ans,minwhite)
                else:
                    minwhite += 1
            i += 1
            j += 1
        return ans
        