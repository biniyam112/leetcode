class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = defaultdict(str)
        for equation in equations:
            parent[equation[0]] = equation[0]
            parent[equation[3]] = equation[3]
            
        def find(val):
            if parent[val] == val: return val
            return find(parent[val])
            
        def union(a,b):
            parent[find(a)] = find(b)
            
        for equation in equations:
            if equation[1] == '=':
                union(equation[0],equation[3])
        # print(parent)
        
        for equation in equations:
            # print(equation[0],find(equation[0]))
            # print(equation[3],find(equation[3]))
            if equation[1] == '=' and find(equation[0]) != find(equation[3]):
                return False
            if equation[1] == '!' and find(equation[0]) == find(equation[3]):
                return False
        return True
        