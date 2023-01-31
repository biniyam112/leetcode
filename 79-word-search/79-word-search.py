class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        charFreq = defaultdict(int)
        for char in word:
            charFreq[char] += 1

        for row in range(len(board)):
            for col in range(len(board[row])):
                charFreq[board[row][col]] -= 1

        for freq in charFreq.values():
            if freq > 0:
                return False
        
        m,n = len(board),len(board[0])
        dirs = [0,1,0,-1,0]
        inbound = lambda row,col : 0 <= row < m and 0 <= col < n
        def dfs(row,col,index,visited):
            visited.add((row,col))
            if index == len(word)-1:
                return True
            res = False
            for i in range(4):
                new_row,new_col = row+dirs[i],col+dirs[i+1]
                if inbound(new_row,new_col) and (new_row,new_col) not in visited and board[new_row][new_col] == word[index+1]:
                    res = res or dfs(new_row,new_col,index+1,visited)
            visited.remove((row,col))
            return res
        
        starter = defaultdict(list)
        for i in range(m):
            for j in range(n):
                starter[board[i][j]].append((i,j))
                
        start = word[0]
        ans = False
        for row,col in starter[start]:
            ans = ans or dfs(row,col,0,set())
        return ans
            