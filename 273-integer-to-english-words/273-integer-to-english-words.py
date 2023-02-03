class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        ons = ['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
        els = ['Nineteen', 'Eighteen', 'Seventeen', 'Sixteen', 'Fifteen', 'Fourteen', 'Thirteen', 'Twelve', 'Eleven',''][::-1]
        tns = ['','Ten','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
        
        def handleThree(num,suffix = ''):
            num = num.lstrip('0')
            if not num : return ['']
            if int(num) < 10:
                return [ons[int(num)],suffix]
            vals = [int(x) for x in num]
            if int(num) < 100:
                if vals[0] ==  1 and vals[1] != 0:
                    elves = int(str(vals[0])+str(vals[1]))
                    return [els[elves%10],suffix]
                else:
                    return [tns[vals[0]],ons[vals[1]],suffix]
            else:
                if vals[1] ==  1 and vals[2] != 0:
                    elves = int(str(vals[1])+str(vals[2]))
                    return [ons[vals[0]],'Hundred',els[elves%10],suffix]
                else:
                    return [ons[vals[0]],'Hundred',tns[vals[1]],ons[vals[2]],suffix]
                
        num = [x for x in str(num)]
        def removeTrie():
            val = ''
            for _ in range(min(3,len(num))):
                val += num.pop()
            return val[::-1]
        
        res = deque()
        powers = ['','Thousand','Million','Billion']
        for i in range(len(powers)):
            if num:
                trie = removeTrie()
                trieWord = handleThree(trie,powers[i])
                res.extendleft(trieWord[::-1])
        # print(res)
        
        output = []
        for i in range(len(res)):
            if res[i]:
                output.append(res[i])
        return ' '.join(output).strip(' ')
        