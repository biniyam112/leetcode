class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        # use union find idea to find the represent whole list with one representative or not                
        
        
        busRoutes = defaultdict(list)
        for bus,route in enumerate(routes):
            for station in route:
                busRoutes[station].append(bus)
                
        
        queue = deque()
        for curBus in busRoutes[source]:
            queue.append((curBus,1))
            
        visited =  set()
        while queue:
            bus,steps = queue.popleft()
            if bus in visited:
                continue
            visited.add(bus)
            if target in routes[bus]:
                return steps
            for station in routes[bus]:
                for next_bus in busRoutes[station]:
                    queue.append((next_bus,steps+1))
        return -1
        
        

        