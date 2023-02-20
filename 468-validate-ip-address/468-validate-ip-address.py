import string

class Solution:
    def validIPAddress(self, IP: str) -> str:
        def isIPv4(inputStr):
            splitInput = inputStr.split('.') 
			
            if len(splitInput) != 4:
                return False
				
            for group in splitInput:
                if len(group) == 0:
                    return False
                if group[0] == '0' and len(group) > 1: 
                    return False
                if not group.isdigit() or int(group) < 0 or int(group) > 255:
                    return False
					
            return True
        
        def isIPv6(inputStr):
            splitInput = inputStr.split(':') 
            if len(splitInput) != 8:
                return False
            for group in splitInput:
                if len(group) > 4 or len(group) < 1: 
                    return False
                for char in group:
                    if char not in string.hexdigits:
                        return False
            return True
                
        if isIPv4(IP):
            return 'IPv4'
        if isIPv6(IP):
            return 'IPv6'
        return 'Neither'