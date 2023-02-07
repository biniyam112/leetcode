class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [0-x for x in nums]
        heapq.heapify(heap)
        for i in range(k-1):
            heapq.heappop(heap)
        return 0-heap[0]
        