class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        
        def mutate(gene):
            visited.add(''.join(gene))
            if ''.join(gene) == end:
                return 0
            ans = float('inf')
            for i in range(len(gene)):
                for option in options:
                    new_gene = gene.copy()
                    new_gene[i] = option
                    if ''.join(new_gene) in bank and ''.join(new_gene) not in visited:
                        # print(''.join(new_gene))
                        ans = min(ans,1+mutate(new_gene))
            return ans
        
        bank = set(bank)
        bank.add(start)
        options = ['A','C','G','T']
        visited = set()
        
        steps = mutate([x for x in start])
        steps = -1 if steps == float('inf') else steps
        return -1 if end not in bank else steps