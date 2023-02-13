class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = 0
        output = []
        carry = 0
        while i < max(len(a),len(b)):
            temp = carry
            if i < len(a):
                temp +=  int(a[len(a)-i-1])
            if i < len(b):
                temp += int(b[len(b)-1-i])
            if temp == 0:
                output.append(0)
            elif temp == 1:
                output.append(1)
                carry = 0
            elif temp == 2:
                output.append(0)
                carry = 1
            else:
                output.append(1)
                carry = 1
            i+=1
        if carry:
            output.append(1)
        output.reverse()
        temp = ''
        for i in output:
            temp+=str(i)
        return temp
            