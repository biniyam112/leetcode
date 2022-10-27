class Solution:
    par = {}
    
    def find(self,par,node):
        if par[node] != node:
            par[node] = self.find(par,par[node])
        return par[node]
            
    def union(self,par,node1,node2):
        par1 = self.find(par,node1)
        par2 = self.find(par,node2)
        par[par1] = par2
        
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        for i in range(1,len(edges)+1):
            self.par[i] = i
        for u,v in edges:
            par1 = self.find(self.par,u)
            par2 = self.find(self.par,v)
            if par1 == par2:
                return [u,v]
            self.union(self.par,u,v)
            
            
        
        