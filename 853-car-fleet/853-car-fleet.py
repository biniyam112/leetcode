class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # calculate finish time to find if one car can catch up to another
        finishTime = []
        for i,pos in enumerate(position):
            curTime = (target-pos)/speed[i]
            finishTime.append(curTime)
            
        # print(finishTime)
        
        # sort the cars in their starting position(cause we're checking if the car behind can catch up to the car infront)
        pair = sorted(zip(position,finishTime),reverse = True)
        finishTime = [y for _,y in pair]
        
        # print(position,finishTime)
        
        fleet = 0
        curMax = float('-inf')
        for curTime in finishTime:
            if curTime > curMax:
                curMax = curTime
                fleet += 1
        
        return fleet
        