class Solution:
    def frequencySort(self, s: str) -> str:

        output = ''
        letterDict = Counter(s)
        letterDict = OrderedDict(sorted(letterDict.items(), key=operator.itemgetter(1),reverse=True))
        for k,v in letterDict.items():
            output+= k*v
        return output
                    
            
            
        