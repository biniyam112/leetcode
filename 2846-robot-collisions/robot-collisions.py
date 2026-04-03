class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        order = sorted(range(n), key=lambda i: positions[i])

        monostack = []
        for i in order:
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

        healths = [x for x in healths if x != 0]
        return healths
        