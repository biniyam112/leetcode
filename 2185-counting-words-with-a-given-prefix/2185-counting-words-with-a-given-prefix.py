class TrieNode:
    def __init__(self,precount = 0):
        self.precount = precount
        self.children = {}
        self.isEnd = False

class Solution:
    def insert(self,word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode(1)
            else:
                cur.children[c].precount += 1
            cur = cur.children[c]
        cur.isEnd = True
    def prefixCount(self, words: List[str], pref: str) -> int:
        self.root = TrieNode()
        for word in words:
            self.insert(word)
        cur = self.root
        for c in pref:
            if c not in cur.children:
                return 0
            cur = cur.children[c]
        return cur.precount
            
            
        
        
        