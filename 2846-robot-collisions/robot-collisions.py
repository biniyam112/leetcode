class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        order = list(range(len(positions)))

        zipped = sorted(zip(positions,healths,directions,order))
        positions,healths,directions,order = [list(x) for x in zip(*zipped)]

        monostack = []
        for i in range(len(directions)):
            # Going to Left
            if directions[i] == 'L':
                while monostack: # There are robots going to Right in stack
                    prev_i = monostack[-1]
                    prev_health = healths[prev_i]
                    if prev_health > healths[i]:
                        healths[prev_i] -= 1
                        healths[i] = 0
                        break
                    elif prev_health < healths[i]:
                        monostack.pop()
                        healths[i] -= 1
                        healths[prev_i] = 0
                    else:
                        monostack.pop()
                        healths[i] = 0
                        healths[prev_i] = 0
                        break
            else:
                # Going to Right
                monostack.append(i)
        
        zipped = sorted(zip(order,healths))
        _,healths = [list(x) for x in zip(*zipped)]
        healths = [x for x in healths if x != 0]
        return healths
        