"""
https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/
Given a binary tree, return the sum of values of nodes with even-valued grandparent.  (A grandparent of a node is the parent of its parent, if it exists.)

If there are no nodes with an even-valued grandparent, return 0.

 

Example 1:
Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 18
Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if root:
            return self.helper(root, root.left) + self.helper(root, root.right)
        return 0
    
    def helper(self, groot, root):
        if groot and root:
            if groot.val % 2 == 0:
                if root.left and root.right:
                    return root.left.val + root.right.val + self.helper(root, root.left) + self.helper(root, root.right)
                elif root.left and not root.right:
                    return root.left.val + self.helper(root, root.left)
                elif root.right and not root.left:
                    return root.right.val + self.helper(root, root.right)
                else:
                    return 0
            else:
                return self.sumEvenGrandparent(root)
        
        return 0