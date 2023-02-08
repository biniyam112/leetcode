class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # [a][b] means a divided by b
        all_equations = defaultdict(defaultdict)
        
        def findEquations(a,b,val):
            if (a,b) not in visited:
                pairs = []
                all_equations[a][b] = val
                all_equations[b][a] = 1/val
                visited.add((a,b))
                visited.add((b,a))
                for k,v in all_equations[a].items():
                    all_equations[b][k] = v * (1/val)
                    all_equations[k][b] = 1/all_equations[b][k]
                    pairs.append((b,k,v * (1/val)))

                for k,v in all_equations[b].items():
                    all_equations[a][k] = v * val
                    all_equations[k][a] = 1/all_equations[a][k]
                    pairs.append((a,k,v * val))

                for a,b,value in pairs:
                    # print(a,b,value)
                    findEquations(a,b,value)

        visited = set()
        for i,(a,b) in enumerate(equations):
            findEquations(a,b,values[i])
        ans = []
        for a,b in queries:
            if a in all_equations and b in all_equations[a]:
                ans.append(all_equations[a][b])
            elif b in all_equations and a in all_equations[b]:
                ans.append(all_equations[b][a])
            else:
                ans.append(-1)
        return ans