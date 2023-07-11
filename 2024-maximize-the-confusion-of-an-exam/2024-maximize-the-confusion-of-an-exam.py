class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def findMax(key,changes=k):
            i,j = 0,0
            res = 1
            while j < len(answerKey):
                if answerKey[j] != key and changes:
                    changes -= 1
                elif answerKey[j] != key:
                    res = max(res,j-i)
                    # print(res)
                    # looking for takebacks
                    while i < j and answerKey[i] == key:
                        i += 1
                    i += 1
                j += 1
            return max(res,j-i)
        return max(findMax('T'),findMax('F'))