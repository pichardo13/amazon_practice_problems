# Definition for a binary tree node.
'''
Step 1: Make root with first item in list
Step 2: Since the list, preorder, has items in preorder we know that there mid point for items greater than the root and those less than the root. Split this into left, right.
Step 3: Make left node to the first item in left list, make right node to the first item in right list.
Step 4: Repeat
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstFromPreorder(self, preorder):
        #make root with first item on list, insert rest of list
        return self.insert(TreeNode(preorder[0]), preorder[1:])
        
    
    def insert(self, root, preorder):
        if root:
            split = 0
            for i in preorder:
                if i < root.val:
                    split += 1

            left = preorder[:split]
            right = preorder[split:]
            if left:
                root.left = self.insert(TreeNode(left[0]), left[1:])
            if right:
                root.right = self.insert(TreeNode(right[0]), right[1:])
            return root

sol = Solution()
sol.bstFromPreorder([8,5,1,7,10,12])