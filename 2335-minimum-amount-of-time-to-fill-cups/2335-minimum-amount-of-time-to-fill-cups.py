class Solution:
    def fillCups(self, amount: List[int]) -> int:
        fills = 0
        amount.sort(reverse=True)
        while amount[0] > 0:
            amount[0] -= 1
            amount[1] -= 1
            amount.sort(reverse=True)
            fills += 1
        return fills
        