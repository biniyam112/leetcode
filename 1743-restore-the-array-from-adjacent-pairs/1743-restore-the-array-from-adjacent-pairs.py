class Solution:
    def restoreArray(self, adjPairs: List[List[int]]) -> List[int]:
        ans = []
        neghbours =  defaultdict(list)
        
        for (u,v) in adjPairs:
            neghbours[u].append(v)
            neghbours[v].append(u)
            
        visited = set()
        queue = deque()
        for k,v in neghbours.items():
            if len(v) ==  1:
                queue.append(k)
                visited.add(k)
                break
        
        ans = []
        while queue:
            val = queue.popleft()
            ans.append(val)
            for neghbour in neghbours[val]:
                if neghbour not in visited:
                    queue.append(neghbour)
                    visited.add(neghbour)
        return ans
            
            
        