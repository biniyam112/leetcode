class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        population = []
        
        for birth, death in logs:
            population.append((birth, 1))
            population.append((death, -1))
                   
        yr = float('inf')
        cur = hi = 0
        
        for year, change in sorted(population):
            cur += change
            
            if cur > hi:
                hi = cur
                yr = year
            
        return yr