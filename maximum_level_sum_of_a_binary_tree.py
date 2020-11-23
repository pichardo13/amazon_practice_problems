"""
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.
Return the smallest level X such that the sum of all the values of nodes at level X is maximal.

Example 1:
Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.

Example 2:
Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if not root:
            return None
        queue = [root]
        max_sum = root.val
        max_level = 1
        level = 1


        while queue:
            i, level_len = 0, len(queue)
            level_sum = 0
            
            while i < level_len:
                curr = queue.pop(0)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                level_sum += curr.val
                i += 1
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = level
            level += 1
        return max_level