class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pq = [(nums1[0] + nums2[0], 0, 0)]
        ans = []
        vis = set([(0, 0)])
        while k and pq:
            s, i1, i2 = heappop(pq)
            ans.append([nums1[i1], nums2[i2]])
            if i1 + 1 < len(nums1) and (i1 + 1, i2) not in vis:
                heappush(pq, (nums1[i1 + 1] + nums2[i2], i1 + 1, i2))
                vis.add((i1 + 1, i2))
            if i2 + 1 < len(nums2) and (i1, i2 + 1) not in vis:
                heappush(pq, (nums1[i1] + nums2[i2 + 1], i1, i2 + 1))
                vis.add((i1, i2 + 1))
            k -= 1
        return ans
