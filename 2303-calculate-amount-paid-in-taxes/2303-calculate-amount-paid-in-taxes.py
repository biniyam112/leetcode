class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        taxes = 0
        if income >= brackets[0][0]:
            taxes += brackets[0][0] * brackets[0][1] * 0.01
        else:
            taxes += income * brackets[0][1] * 0.01
        income -= brackets[0][0]
            
        i = 1
        while income > 0 and i < len(brackets):
            if income >= (brackets[i][0]-brackets[i-1][0]):
                taxes += (brackets[i][0]-brackets[i-1][0]) * brackets[i][1] * 0.01
            else:
                taxes += income * brackets[i][1] * 0.01
            income -= brackets[i][0]-brackets[i-1][0]
            i += 1
        return taxes