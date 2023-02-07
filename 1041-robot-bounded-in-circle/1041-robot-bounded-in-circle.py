class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        instructions = instructions * 4
        movements = [0,0,0,0]
        dirs = ['n','e','s','w']
        n = 4
        def changedir(change,curdir):
            if change == 'R':
                return (curdir + 1) % n
            return (curdir - 1 + n) % n
                
        curdir = 0
        for move in instructions:
            if move == 'G':
                movements[curdir] += 1
            else:
                curdir = changedir(move,curdir)
        return not (movements[0]-movements[2] or movements[1]-movements[3])
        