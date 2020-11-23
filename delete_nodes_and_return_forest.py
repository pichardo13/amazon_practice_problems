class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
        

class Solution:
    def delNodes(self, root, to_delete):
        delete = set(to_delete)
        forest = []
        self.helper(root, None, delete, forest)
        return forest

    def helper(self, root, parent, delete, forest):
        if root is None:
            return None

        if root.val in delete:
            self.helper(root.right, None, delete, forest)
            self.helper(root.left, None, delete, forest)
            return None

        root.right = self.helper(root.right, root, delete, forest)
        root.left = self.helper(root.left, root, delete, forest)

        if parent is None:
            forest.append(root)
        return root


            

root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
sol = Solution()
sol.delNodes(root, [3,5])
                