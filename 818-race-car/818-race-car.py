class Solution:
    def racecar(self, target: int) -> int:
        
        visited = set()
        visited.add((0, 1))
        
        queue = deque([])
        queue.append((0, 1, 0))
        while queue:
            curr_pos, curr_speed, steps = queue.popleft()
            if curr_pos == target: return steps
            
            new_speed = 2 * curr_speed
            new_pos = curr_pos + curr_speed
            
            if abs(new_pos - target) < target and (new_pos, new_speed) not in visited:
                visited.add((new_pos, new_speed))
                queue.append((new_pos, new_speed, steps + 1))

            new_pos = curr_pos
            if curr_speed < 0: new_speed = 1
            else: new_speed = -1
            
            if abs(new_pos - target) < target and (new_pos, new_speed) not in visited:
                visited.add((new_pos, new_speed))
                queue.append((new_pos, new_speed, steps + 1))
                
                
        return -1