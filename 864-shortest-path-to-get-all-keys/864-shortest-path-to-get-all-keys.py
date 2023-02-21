class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        inbound = lambda row,col : 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        dirs = [0,1,0,-1,0]
        keys_count = 0
        start = None
        
        grid = [[x for x in row] for row in grid]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                order = ord(grid[i][j])
                if order == 64:
                    start = (i,j)
                if 97 <= order <= 122:
                    keys_count += 1
    
        visited = set()
        # store upper case ord of discovered keys in set
        queue = deque([(*start,0,tuple())])
        while queue:
            row,col,steps,keys = queue.popleft()
            if (row,col,keys) not in visited:
                visited.add((row,col,keys))
                if len(set(keys)) == keys_count:
                    return steps
                for i in range(4):
                    copyKey = set(keys)
                    new_row,new_col = row+dirs[i],col+dirs[i+1]
                    inGrid = inbound(new_row,new_col)
                    isWall = inGrid and grid[new_row][new_col] == '#'
                    isLock = inGrid and 65 <= ord(grid[new_row][new_col]) <= 90
                    seen = (new_row,new_col,keys) in visited
                    if not inGrid or isWall or seen:
                        continue
                    if isLock and ord(grid[new_row][new_col]) not in copyKey:
                        continue    
                    else:
                        order = ord(grid[new_row][new_col])
                        if 97 <= order <= 122 : copyKey.add(order-32)
                        queue.append((new_row,new_col,steps+1,tuple(copyKey)))
        return -1
                    
        
        
        
        