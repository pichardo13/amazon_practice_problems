
class TreeNode(object):
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        #returns BFS of tree in string
        res = []
        self.serializeBFS(root, res)
        return res

    def serializeBFS(self, root, res):
        if root:
            res.append(str(root.val))
            self.serializeBFS(root.left, res)
            self.serializeBFS(root.right, res)
        else:
            res.append('X')

                
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        # root = TreeNode(data[0])
        # self.helper(data)
        if not data: return []
        return self.helper(data)
        
    def helper(self, data):
        val = data.pop(0)
        if val == 'X':
            return 
        node = TreeNode(val)
        node.right = self.helper(data)
        node.left = self.helper(data)
        return node
c = Codec()
tree = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
sTree = c.serialize(tree)
# sTree = ['1', '2', '3', 'X', 'X', '4', '5', 'X', 'X', 'X', 'X']
print(c.deserialize(sTree))