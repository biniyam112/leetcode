class Solution:
#     def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
#         # greedy wouldn't work
#         # no branch if char is same as prev
#         # if prev is deleted then would rather delete this one
#         def count(s):
#             len_ = 0
#             counter = Counter(s)
#             for v in counter.values():
#                 if v == 1:
#                     len_ += 1
#                 else:
#                     len_ += len(str(v))+1
#             return len_
#         def dp(index,k,compressed):
#             if k == 0 or index == len(s):
#                 return count(compressed+s[index:])
#             if (index,k) in visited:
#                 return visited[(index,k)]
#             path1 = path2 = len(s)
#             if not compressed or compressed[-1] != s[index]:
#                 path1 = dp(index+1,k-1,compressed)
#                 path2 = dp(index+1,k,compressed[:]+s[index])
#             elif compressed[-1] == s[index]:
#                 path2 = dp(index+1,k,compressed[:]+s[index])
#             # visited[(index,k)] = min(path1,path2)
#             return min(path1,path2)
        
#         visited = {}
#         return dp(0,k,'')
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @cache
        def dp(i, prev, prev_cnt, k):
            if k < 0: return inf
            # we delete all characters, return 0
            if i == len(s): return 0
            delete = dp(i + 1, prev, prev_cnt, k - 1)
            if s[i] == prev:
                # e.g. a2 -> a3
                keep = dp(i + 1, prev, prev_cnt + 1, k)
                if prev_cnt in [1, 9, 99]:
                    keep += 1
            else:
                keep = dp(i + 1, s[i], 1, k) + 1
            return min(delete, keep)
        return dp(0, "", 0, k)