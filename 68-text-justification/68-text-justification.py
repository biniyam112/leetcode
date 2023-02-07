class Solution:
    
    def createLine(self,lineStr,lineList,maxWidth):
        if len(lineList) == 1:
            spaces = maxWidth - len(lineStr) + len(lineList)
            lineStr = lineList[0]+ ' '*spaces
        else:
            spaces = maxWidth - len(lineStr)+len(lineList)
            remSpace = spaces % (len(lineList)-1)
            spaces //= (len(lineList)-1)

            lineStr = ''
            for i,word in enumerate(lineList):
                if i == len(lineList)-1:
                    lineStr += word
                else:
                    if remSpace > 0:
                        lineStr += word+ ' ' * (spaces +1)
                        remSpace -= 1
                    else:
                        lineStr += word+ ' ' * spaces
        # print([lineStr])
        return lineStr
    
    def createLastLine(self,lineStr,lineList,maxWidth):
        if lineList:
            spaces = maxWidth - len(lineStr)
            return lineStr + ' ' * spaces
        return ''
    
    
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        lineStr = ''
        lineList = []
        for i,word in enumerate(words):
            # print(lineStr,word)
            if len(lineStr)+len(word) < maxWidth:
                lineStr+= word+' '
                lineList.append(word)
            elif len(lineStr)+len(word) ==  maxWidth:
                lineStr += word
                ans.append(lineStr)
                lineStr = ''
                lineList = []
            elif i == len(words)-1:
                if len(lineStr)+len(word) < maxWidth:
                    lineStr += word
                    lineList.append(word)
                    spaces = maxWidth-len(lineStr)
                    lineStr = ''
                    for added in lineList:
                        lineStr += added
                    lineStr += ' ' * spaces
                    ans.append(lineStr)
                else:
                    line = self.createLine(lineStr,lineList,maxWidth)
                    ans.append(line)
                    spaces = maxWidth - len(word)
                    line = word + ' '* spaces
                    ans.append(line)
                lineList = []
            else:
                line = self.createLine(lineStr,lineList,maxWidth)
                ans.append(line)
                lineStr = word+' '
                lineList = [word]
        if lineList:
            # print(lineList)
            line = self.createLastLine(lineStr,lineList,maxWidth)
            ans.append(line)
        
        return ans
                