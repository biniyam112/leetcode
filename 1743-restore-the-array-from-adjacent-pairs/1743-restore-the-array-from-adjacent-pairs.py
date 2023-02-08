class Solution:
    def restoreArray(self, adjPairs: List[List[int]]) -> List[int]:
        ans = []
        neghbours =  defaultdict(list)
        
        for (u,v) in adjPairs:
            neghbours[u].append(v)
            neghbours[v].append(u)
            
        queue = deque()
        for k,v in neghbours.items():
            if len(v) ==  1:
                queue.append(k)
                break
        
        ans = []
        while queue:
            val = queue.popleft()
            ans.append(val)
            for neghbour in neghbours[val]:
                if neghbours[neghbour]:
                    queue.append(neghbour)
            neghbours.pop(val)
        return ans
            
            
        