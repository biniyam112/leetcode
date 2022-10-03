class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        stack = []
        for i in range(len(colors)):
            if not stack or colors[i] != colors[stack[-1]]:
                stack.append(i)
            else:
                val = (i,neededTime[i])
                while stack and colors[stack[-1]] == colors[i]:
                    if neededTime[stack[-1]] > val[1]:
                        val = (stack[-1],neededTime[stack[-1]])
                    stack.pop()
                stack.append(val[0])
        ans = 0
        for index in stack:
            ans += neededTime[index]
        return sum(neededTime)-ans