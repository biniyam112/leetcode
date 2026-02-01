class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()

        minDiff = float('inf')
        items = []

        for i  in range(1,len(arr)):
            diff = arr[i]-arr[i-1]
            if diff < minDiff:
                minDiff = diff
                items = [[arr[i-1],arr[i]]]
            elif diff == minDiff:
                items.append([arr[i-1],arr[i]])
        return items
        