class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        mapping = [([False] * numCourses) for i in range(numCourses)]
        # print(mapping)
            
        for pre,post in prerequisites:
            mapping[pre][post] = True
        
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    mapping[i][j] = mapping[i][j] or mapping[i][k] and mapping[k][j]
        ans = []
        for pre,post in queries:
            ans.append(mapping[pre][post])
        return ans
                    