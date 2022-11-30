class Codec:
    def serialize(self, root):
        if not root: return 'x'
        return ','.join([str(root.val),self.serialize(root.left),self.serialize(root.right)])
        
    def deserialize(self, data):
        self.data = data
        if self.data[0] == 'x': return None
        root = TreeNode(self.data[:self.data.find(',')])
        root.left = self.deserialize(self.data[self.data.find(',')+1:])
        root.right = self.deserialize(self.data[self.data.find(',')+1:])
        return root
            
