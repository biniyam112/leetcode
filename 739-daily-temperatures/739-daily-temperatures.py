class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        howlong = []
        stay_days = [0] * len(temperatures)
        for i,temp in enumerate(temperatures):
            while howlong and temperatures[howlong[-1]] < temp:
                cur = howlong.pop()
                stay_days[cur] = i-cur
            howlong.append(i)
        return stay_days