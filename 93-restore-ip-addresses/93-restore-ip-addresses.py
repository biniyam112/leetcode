class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        ans = []
        def findIP(ip=[],idx=n):
            if idx == 0 and len(ip) == 4:
                ip = '.'.join(ip[::-1])
                ans.append(ip)
            rng = min(3,idx)
            for i in range(1,rng+1):
                if i != 1 and s[idx-i] == '0' or len(ip) == 4 or int(s[idx-i:idx]) > 255:
                    continue
                cpy = ip.copy()
                cpy.append(s[idx-i:idx])
                findIP(cpy,idx-i)
        findIP()
        return ans
        
        