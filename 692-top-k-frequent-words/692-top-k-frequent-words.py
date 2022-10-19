class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freqDict = {}
        for i in words:
            if  i in freqDict:
                freqDict[i] = freqDict[i] + 1
            else:
                freqDict[i] = 1
        freqList = []
        for key,value in freqDict.items():
            freqList.append((-value,key))
        heapq.heapify(freqList)
        output = []
        for i in range(k):
            output.append(heapq.heappop(freqList)[1])
        return output