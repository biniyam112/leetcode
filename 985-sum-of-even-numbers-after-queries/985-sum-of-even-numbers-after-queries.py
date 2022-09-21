class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = sum(x for x in nums if x % 2 == 0)
        ans = []
        for query in queries:
            val = nums[query[1]]
            nums[query[1]] += query[0]
            if val % 2 == 0 and nums[query[1]] % 2 == 0:
                even_sum += nums[query[1]] - val
            elif val % 2 == 0 and nums[query[1]] % 2 != 0:
                even_sum -= val
            elif nums[query[1]] % 2 == 0:
                even_sum += nums[query[1]]
            ans.append(even_sum)
        return ans