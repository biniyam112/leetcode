class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        original = []
        changed_ = Counter(changed)
        changed.sort()
        # print(changed_)
        i = 0
        counter = 0
        while counter < len(changed):
            if changed_[changed[i]] > 0:
                changed_[changed[i]] -= 1
                counter += 1
                if changed[i] * 2 in changed_ and changed_[changed[i]*2] > 0:
                    original.append(changed[i])
                    changed_[changed[i] * 2] -= 1
                    counter += 1
                else:
                    return []
            i += 1
        return original
        