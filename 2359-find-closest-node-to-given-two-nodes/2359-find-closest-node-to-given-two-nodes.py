class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        from1 = defaultdict(int)
        from2 = defaultdict(int)
        
        
        def dfs(cur,store,visited,dis=0):
            store[cur] = dis
            visited.add(cur)
            if edges[cur] == -1:
                return
            cur = edges[cur]
            if cur not in visited:
                dfs(cur,store,visited,dis+1)
            
        dfs(node1,from1,set())
        dfs(node2,from2,set())
        
        # print(from1,from2)
        ans = []
        mindis = float('inf')
        for k,dis1 in from1.items():
            if k in from2:
                if max(dis1,from2[k]) < mindis:
                    ans = [k]
                    mindis = max(dis1,from2[k])
                elif max(dis1,from2[k]) == mindis:
                    ans.append(k)
        if not ans : return -1
        return min(ans)