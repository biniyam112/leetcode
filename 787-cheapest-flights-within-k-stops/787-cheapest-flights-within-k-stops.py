class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        
        for start,end,price in flights:
            graph[start].append((end,price))
        
        
        visited = defaultdict(int)
        for i in range(0,n):
            for j in range(k+2):
                visited[(i,j)] = float('inf')
            
        
        # price,steps,node
        path = [(0,0,src)]
        heapq.heapify(path)
        while path:
            price,steps,node = heapq.heappop(path)
            if node == dst:
                return price
            if steps <= k:
                for to,cost in graph[node]:
                    new_price = price+cost
                    if new_price < visited[(to,steps)]:
                        heapq.heappush(path,(new_price,steps+1,to))
                        visited[(to,steps+1)] = new_price
        return -1
        