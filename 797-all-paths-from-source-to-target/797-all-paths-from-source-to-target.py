class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        def recursion(index,path):
            if index == len(graph)-1:
                paths.append(path)
                return
            for i in graph[index]:
                p = path.copy()
                p.append(i)
                recursion(i,p)
        recursion(0,[0])
        return paths
        