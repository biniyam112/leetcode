class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        redpath = defaultdict(list)        
        bluepath = defaultdict(list)
        for s,e in redEdges:
            redpath[s].append(e)
        for s,e in blueEdges:
            bluepath[s].append(e)
        # print(redpath,bluepath)
        
        ans = [-1] * n
        
        bluevisited = set()
        redvisited = set()
        queue = deque()
        queue.append((0,0,True))
        queue.append((0,0,False))
        
        while queue:
            val,steps,red = queue.popleft()
            if ans[val] == -1 or steps < ans[val]:
                ans[val] = steps
            if red == True:
                if val not in redvisited:
                    redvisited.add(val)
                    for i in redpath[val]:
                        queue.append((i,steps+1,False))
            else:
                if val not in bluevisited:
                    bluevisited.add(val)
                    for i in bluepath[val]:
                        queue.append((i,steps+1,True))
        return ans
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # dfs not working
#         def dfs(val,steps,isRed):
#             print(val,steps)
#             if ans[val] == -1 or steps < ans[val]:
#                 ans[val] = steps
#             if isRed:
#                 for i in redpath[val]:
#                     if (val,i) not in redvisited:
#                         redvisited.add((val,i))
#                         dfs(i,steps+1,False)
#             else:
#                 for i in bluepath[val]:
#                     if (val,i) not in bluevisited:
#                         bluevisited.add((val,i))
#                         dfs(i,steps+1,True)
                    
#         if 0 in redpath:
#             dfs(0,0,True)
#         if 0 in bluepath:
#             dfs(0,0,False)
#         return ans