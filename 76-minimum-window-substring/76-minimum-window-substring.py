class Solution:
    def minWindow(self, s: str, t: str) -> str:
        items = defaultdict(int)
        t = Counter(t)
        def includes(items):
            for k,v in t.items():
                if items[k] < v:
                    return False
            return True
        
        i,j,size,start = 0,0,float('inf'),-1
        while j < len(s):
            items[s[j]] += 1
            if includes(items):
                while includes(items):
                    items[s[i]] -= 1
                    i += 1
                if j-i+2 < size:
                    size = j-i+2
                    start = i-1
            j += 1
        if start == -1 : return ''
        return s[start:start+size]
            
            