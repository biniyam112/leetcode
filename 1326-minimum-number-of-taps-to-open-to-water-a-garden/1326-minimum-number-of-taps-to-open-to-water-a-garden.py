class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        jump_distance = [0] * (n + 1)        
        for index, radius in enumerate(ranges):
            left, right = max(0, index - radius), min(n, index + radius)
            jump_distance[left] = max(jump_distance[left], right - left)
        jump_count, cur_range, next_range = -1, -1, 0
        
        for position, distance in enumerate(jump_distance):
            if position > cur_range:
                if position > next_range:
                    return -1
                jump_count, cur_range = jump_count + 1, next_range            
            next_range = max(next_range, position + distance)
        
        return jump_count