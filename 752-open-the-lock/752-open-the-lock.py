class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        def decrease(val):
            if val == '0':
                return '9'
            return str(int(val)-1)
        def increase(val):
            if val == '9':
                return '0'
            return str(int(val)+1)
        queue = deque()
        queue.append(('0000',0))
        while queue:
            comb,steps = queue.popleft()
            if comb == target:
                return steps
            for i in range(4):
                inc = ''.join([comb[j] if j != i else increase(comb[j]) for j in range(len(comb))])
                dec = ''.join([comb[j] if j != i else decrease(comb[j]) for j in range(len(comb))])
                if comb not in deadends:
                    queue.append((inc,steps+1))
                if comb not in deadends:
                    queue.append((dec,steps+1))
            deadends.add(comb)
        return -1
    