class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # pointer to smallest element
        inc_queue = deque()
        # pointer to largest element
        dec_queue = deque()
        
        start = maxLen = 0
        for end,val in enumerate(nums):
            while inc_queue and inc_queue[-1] > val:
                inc_queue.pop()
            inc_queue.append(val)
            
            while dec_queue and dec_queue[-1] < val:
                dec_queue.pop()
            dec_queue.append(val)
            
            while dec_queue[0] - inc_queue[0] > limit:
                atStart = nums[start]
                if atStart == dec_queue[0]:
                    dec_queue.popleft()
                if atStart == inc_queue[0]:
                    inc_queue.popleft()
                start += 1
            maxLen = max(maxLen,end-start+1)
        return maxLen