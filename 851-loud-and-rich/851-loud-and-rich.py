class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        richer_first = [0] * len(quiet)
        rich_graph = defaultdict(list)
        for rich,poor in richer:
            rich_graph[rich].append(poor)
            # poor requires poor to be processed first(goes from rich to poor)
            richer_first[poor] += 1
            
        queue = deque()
        for person in range(len(richer_first)):
            if richer_first[person] == 0:
                queue.append(person)
                
        ans = quiet.copy()
        while queue:
            person = queue.popleft()
            for less_rich in rich_graph[person]:
                richer_first[less_rich] -= 1
                ans[less_rich] = min(ans[less_rich],ans[person])
                if richer_first[less_rich] == 0: queue.append(less_rich)
        
        quietness_to_person = {}
        for person,quietness in enumerate(quiet):
            quietness_to_person[quietness] = person
        return [quietness_to_person[quietness] for quietness in ans]
            
        