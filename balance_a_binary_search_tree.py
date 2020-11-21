class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorder(self, root, arr):
        if root:
            if root.left:
                self.inorder(root.left, arr)
            arr.append(root.val)
            if root.right:
                self.inorder(root.right, arr)
                
    def insert(self, arr):
        if arr:
            mid = len(arr)//2
            root = TreeNode(arr[mid])
            root.left = self.insert(arr[:mid])
            root.right = self.insert(arr[mid+1:])
            return root
        return 
        
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = []
        self.inorder(root, arr)
        
        tree = self.insert(arr)
        return tree

root = TreeNode(4, TreeNode(2, TreeNode(1, TreeNode(0)), TreeNode(3)), TreeNode(5))
sol = Solution()
sol.balanceBST(root)