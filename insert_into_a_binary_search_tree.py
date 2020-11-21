'''
https://leetcode.com/problems/insert-into-a-binary-search-tree/
You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the 
insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any 
of them.
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        
        self.insert(root, val)
        return root
    
    def insert(self,root, val):
        if root:
            if root.val < val:
                if root.right:
                    self.insert(root.right, val)
                else:
                    root.right = TreeNode(val)
            else:
                if root.left:
                    self.insert(root.left, val)
                else:
                    root.left = TreeNode(val)

root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
sol = Solution()
sol.insertIntoBST(root, 5)
            