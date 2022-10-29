class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        # growTime = [y for _,y in sorted(zip(plantTime,growTime))]
        # plantTime.sort()
        cur_plant_time = 0
        result = 0
        indices = sorted(range(len(plantTime)), key=lambda x: -growTime[x]) 
        for i in indices:
            cur_plant_time += plantTime[i]
            result = max(result, cur_plant_time + growTime[i])
        return result
        